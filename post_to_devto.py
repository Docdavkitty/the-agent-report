#!/usr/bin/env python3
"""Cross-post today's articles from The Agent Report to Dev.to (via curl)."""
import json, os, re, subprocess, sys
from datetime import datetime, timezone

API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
API_URL = "https://dev.to/api/articles"
TRACKING_FILE = os.path.expanduser("~/.hermes/devto_posted.txt")
POSTS_DIR = "/home/freebox/the-agent-report/_posts"
FOOTER = "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*"

def load_tracked():
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE) as f:
        return set(line.strip() for line in f if line.strip())

def save_tracked(slug):
    with open(TRACKING_FILE, "a") as f:
        f.write(slug + "\n")

def parse_frontmatter(content):
    m = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = m.group(2).strip()
    
    fm = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            val = re.sub(r'^["\'](.*)["\']$', r'\1', val)
            if val.startswith('[') and val.endswith(']'):
                items = val[1:-1].split(',')
                fm[key] = [re.sub(r'^["\'\s]*(.*?)["\'\s]*$', r'\1', item.strip()) for item in items]
            else:
                fm[key] = val
    return fm, body

def process_tags(tags_list):
    result = []
    for tag in tags_list[:4]:
        t = tag.lower().replace('-', '')
        if len(t) > 12:
            t = t[:12]
        result.append(t)
    return result

def post_article(title, body_md, canonical_url, description, tags):
    """Post via curl (reliable auth handling)."""
    payload = json.dumps({
        "article": {
            "title": title,
            "body_markdown": body_md,
            "published": True,
            "canonical_url": canonical_url,
            "description": description[:155],
            "tags": tags,
            "series": "The Agent Report"
        }
    })
    
    cmd = [
        "curl", "-s", "-w", "\n%{http_code}",
        "-X", "POST", API_URL,
        "-H", "Content-Type: application/json",
        "-H", f"api-key: {API_KEY}",
        "-d", payload
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    output = result.stdout.strip()
    
    # Last line is HTTP code
    lines = output.split('\n')
    http_code = lines[-1].strip()
    response_body = '\n'.join(lines[:-1])
    
    if http_code == '201':
        try:
            data = json.loads(response_body)
            return True, data.get('url', 'OK')
        except:
            return True, 'OK'
    else:
        return False, f"HTTP {http_code}: {response_body[:200]}"

def main():
    tracked = load_tracked()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    files = sorted(os.listdir(POSTS_DIR), reverse=True)
    today_files = [f for f in files if f.startswith(today) and f.endswith('.md') and f != 'meta_descriptions.json']
    
    if not today_files:
        print("[SILENT]")
        return
    
    results = []
    
    for filename in today_files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath) as f:
            content = f.read()
        
        fm, body = parse_frontmatter(content)
        basename = filename.replace('.md', '')
        slug = fm.get('ref', basename)
        
        if slug in tracked:
            results.append(f"  ⏭ {slug} — déjà posté")
            continue
        
        title = fm.get('title', slug)
        
        if fm.get('lang') == 'fr':
            canonical_url = f"https://the-agent-report.com/fr/{today.replace('-', '/')}/{slug}/"
        else:
            canonical_url = f"https://the-agent-report.com/{today.replace('-', '/')}/{slug}/"
        
        raw_tags = fm.get('tags', [])
        if isinstance(raw_tags, str):
            raw_tags = [raw_tags]
        tags = process_tags(raw_tags)
        
        description = fm.get('meta_description', fm.get('description', ''))[:155]
        full_body = body + FOOTER
        
        success, msg = post_article(title, full_body, canonical_url, description, tags)
        
        if success:
            save_tracked(slug)
            results.append(f"  ✅ {slug} — posté : {msg}")
        else:
            results.append(f"  ❌ {slug} — ÉCHEC : {msg}")
    
    today_str = datetime.now(timezone.utc).strftime("%d %B %Y")
    print(f"📡 Cross-posting The Agent Report → Dev.to ({today_str})")
    print(f"Fichiers du jour : {len(today_files)}")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
