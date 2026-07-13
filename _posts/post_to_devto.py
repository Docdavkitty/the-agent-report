#!/usr/bin/env python3
"""Cross-post today's articles to Dev.to"""
import json, os, sys, re, urllib.request, urllib.error

API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
TRACKING_FILE = os.path.expanduser("~/.hermes/devto_posted.txt")
POSTS_DIR = "/home/freebox/the-agent-report/_posts"
BASE_URL = "https://the-agent-report.com"
DEVTO_API = "https://dev.to/api/articles"

def get_slug(filename):
    """Extract slug from filename: 2026-07-13-slug.md -> slug"""
    name = os.path.splitext(os.path.basename(filename))[0]
    # Remove date prefix
    return re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)

def load_tracking():
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE) as f:
        return set(line.strip() for line in f if line.strip())

def save_tracking(slug):
    with open(TRACKING_FILE, 'a') as f:
        f.write(slug + '\n')

def parse_frontmatter(content):
    """Parse YAML-like frontmatter to extract metadata and body"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text = match.group(1)
    body = match.group(2)
    
    meta = {}
    # Simple line-by-line parser for YAML frontmatter
    for line in fm_text.split('\n'):
        # Handle key: value
        m = re.match(r'^(\w+):\s*(.*)', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            meta[key] = val
        # Handle list items (tags)
        elif line.strip().startswith('- ') and 'tags' in meta.get('_in_list', ''):
            tag_val = line.strip()[2:].strip().strip('"').strip("'")
            if isinstance(meta.get('tags'), list):
                meta['tags'].append(tag_val)
        # Detect list start
        if line.strip().startswith('tags:'):
            meta['_in_list'] = 'tags'
            tag_line = line.split(':', 1)[1].strip()
            if tag_line.startswith('['):
                # Inline JSON-like list
                tags_str = tag_line.strip('[]')
                tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',')]
                meta['tags'] = [t for t in tags if t]
                meta['_in_list'] = None
            else:
                meta['tags'] = []
        elif line.strip() and not line.strip().startswith('-'):
            meta['_in_list'] = None
    
    return meta, body

def prepare_tags(tags_list):
    """Take first 4 tags, lowercase, remove dashes, truncate >12 chars"""
    result = ["ai", "agents"]  # base tags
    count = 0
    for tag in tags_list:
        if count >= 2:
            break
        # Clean: lowercase, remove dashes
        cleaned = tag.lower().replace('-', '')
        if cleaned in result:
            continue
        # Truncate >12 chars
        if len(cleaned) > 12:
            cleaned = cleaned[:12]
        result.append(cleaned)
        count += 1
    return result[:4]

def post_article(slug, title, body_md, description, tags, canonical_url):
    """Post to Dev.to API"""
    payload = {
        "article": {
            "title": title,
            "body_markdown": body_md,
            "published": True,
            "canonical_url": canonical_url,
            "description": description,
            "tags": tags,
            "series": "The Agent Report"
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        DEVTO_API,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'api-key': API_KEY
        },
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            print(f"  ✓ Posted successfully: {result.get('url', 'unknown URL')}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"  ✗ HTTP {e.code}: {error_body}")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    today = "2026-07-13"
    print(f"=== Dev.to Cross-poster: {today} ===\n")
    
    # Find today's articles
    posts = sorted(
        [f for f in os.listdir(POSTS_DIR) if f.startswith(today) and f.endswith('.md')],
        reverse=True
    )
    
    if not posts:
        print("No articles for today. [SILENT]")
        return 0
    
    print(f"Found {len(posts)} articles for today: {posts}\n")
    
    tracking = load_tracking()
    posted_count = 0
    
    for post_file in posts:
        slug = get_slug(post_file)
        print(f"--- Processing: {slug} ---")
        
        if slug in tracking:
            print(f"  Already posted, skipping.")
            continue
        
        # Read article
        filepath = os.path.join(POSTS_DIR, post_file)
        with open(filepath, 'r') as f:
            content = f.read()
        
        meta, body = parse_frontmatter(content)
        
        title = meta.get('title', slug)
        meta_desc = meta.get('meta_description', meta.get('description', ''))
        description = meta_desc[:155]
        
        # Get tags from frontmatter
        raw_tags = meta.get('tags', [])
        tags = prepare_tags(raw_tags)
        
        # Determine canonical URL
        lang = meta.get('lang', 'en')
        if lang == 'fr':
            canonical_url = f"{BASE_URL}/fr/2026/07/{slug}/"
        else:
            canonical_url = f"{BASE_URL}/2026/07/{slug}/"
        
        # Add footer
        body_md = body.rstrip() + "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*"
        
        print(f"  Title: {title}")
        print(f"  Tags: {tags}")
        print(f"  Canonical: {canonical_url}")
        print(f"  Description: {description[:80]}...")
        print(f"  Body length: {len(body_md)} chars")
        
        # Post
        success = post_article(slug, title, body_md, description, tags, canonical_url)
        if success:
            save_tracking(slug)
            posted_count += 1
        
        print()
    
    print(f"=== Done: {posted_count} articles posted ===")
    return 0 if posted_count > 0 else 1  # return 1 means "silent"

if __name__ == '__main__':
    sys.exit(main())
