#!/usr/bin/env python3
"""Cross-post today's articles to Dev.to"""
import json, os, sys

API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
TRACKING_FILE = os.path.expanduser("~/.hermes/devto_posted.txt")
POSTS_DIR = "/home/freebox/the-agent-report/_posts"

def strip_hyphens(tag):
    """Remove hyphens from tag, lowercase, truncate to 12 chars"""
    t = tag.lower().replace("-", "").replace("_", "")
    return t[:12]

def truncate(text, maxlen):
    return text[:maxlen]

def extract_frontmatter_and_body(filepath):
    """Extract frontmatter dict and body text from a Jekyll post"""
    with open(filepath) as f:
        content = f.read()
    
    # Split on ---
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, None
    
    fm_text = parts[1].strip()
    body = parts[2].strip()
    
    # Simple YAML-like frontmatter parser (good enough for our format)
    fm = {}
    current_key = None
    multiline_value = []
    in_multiline = False
    
    for line in fm_text.split("\n"):
        # Handle multiline values (lines starting with spaces after a key)
        if in_multiline:
            if line.startswith("  ") or line.startswith("\t"):
                multiline_value.append(line.strip().strip('"'))
                continue
            else:
                fm[current_key] = " ".join(multiline_value)
                multiline_value = []
                in_multiline = False
        
        if ":" in line and not line.strip().startswith("-"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            
            if val == ">" or val == "|":
                current_key = key
                multiline_value = []
                in_multiline = True
            elif val == "":
                # Could be start of list, check next lines
                current_key = key
                in_multiline = False
            else:
                fm[key] = val
        elif line.strip().startswith("-") and current_key:
            # List item
            val = line.strip()[1:].strip().strip('"').strip("'")
            if current_key not in fm:
                fm[current_key] = []
            fm[current_key].append(val)
    
    if in_multiline and multiline_value:
        fm[current_key] = " ".join(multiline_value)
    
    return fm, body

def process_article(filepath, slug):
    """Process a single article and post to Dev.to"""
    fm, body = extract_frontmatter_and_body(filepath)
    if not fm or not body:
        print(f"ERROR: Could not parse {filepath}")
        return False
    
    title = fm.get("title", "").strip().strip('"').strip("'")
    ref = fm.get("ref", slug)
    lang = fm.get("lang", "en")
    permalink = fm.get("permalink", "")
    translation_of = fm.get("translation_of", "")
    
    # Parse tags
    raw_tags = fm.get("tags", [])
    if isinstance(raw_tags, str):
        # Try to parse as JSON-like list
        raw_tags = [t.strip().strip('"').strip("'") for t in raw_tags.strip("[]").split(",")]
    
    # Take first 4 tags, strip hyphens, lowercase, truncate 12 chars
    tags = [strip_hyphens(t) for t in raw_tags[:4]]
    
    # Meta description
    meta_desc = fm.get("meta_description", fm.get("description", "")).strip().strip('"').strip("'")
    description = truncate(meta_desc, 155)
    
    # Canonical URL
    if permalink:
        canonical = f"https://the-agent-report.com{permalink}"
    elif lang == "fr" and translation_of:
        canonical = f"https://the-agent-report.com/fr/2026/06/{ref}/"
    else:
        canonical = f"https://the-agent-report.com/2026/06/{ref}/"
    
    # Build body_markdown with footer
    footer = "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*"
    body_markdown = body + footer
    
    payload = {
        "article": {
            "title": title,
            "body_markdown": body_markdown,
            "published": True,
            "canonical_url": canonical,
            "description": description,
            "tags": tags,
            "series": "The Agent Report"
        }
    }
    
    # Write payload to temp file and curl it
    tmpfile = f"/tmp/devto_{ref}.json"
    with open(tmpfile, "w") as f:
        json.dump(payload, f, ensure_ascii=False)
    
    import subprocess
    result = subprocess.run(
        ["curl", "-s", "-w", "\n%{http_code}", "-X", "POST",
         "https://dev.to/api/articles",
         "-H", "Content-Type: application/json",
         "-H", f"api-key: {API_KEY}",
         "-d", f"@{tmpfile}"],
        capture_output=True, text=True, timeout=30
    )
    
    output = result.stdout.strip()
    lines = output.split("\n")
    http_code = lines[-1] if lines else "000"
    response_body = "\n".join(lines[:-1]) if len(lines) > 1 else ""
    
    print(f"\n{'='*60}")
    print(f"Article: {title}")
    print(f"Slug: {ref}")
    print(f"Canonical URL: {canonical}")
    print(f"Tags: {tags}")
    print(f"Description ({len(description)} chars): {description[:80]}...")
    print(f"Body length: {len(body_markdown)} chars")
    print(f"HTTP {http_code}")
    
    if http_code in ("200", "201", "202"):
        print("SUCCESS!")
        # Try to get the dev.to URL
        try:
            resp = json.loads(response_body)
            devto_url = resp.get("url", "N/A")
            print(f"Dev.to URL: {devto_url}")
        except:
            pass
        
        # Add to tracking file
        with open(TRACKING_FILE, "a") as f:
            f.write(f"{ref}\n")
        return True
    else:
        print(f"FAILED: {response_body[:500]}")
        return False

def main():
    # Determine today's date
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"Today (UTC): {today}")
    
    # Read tracking file
    posted = set()
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE) as f:
            for line in f:
                posted.add(line.strip())
    
    print(f"Already posted: {len(posted)} articles")
    
    # Find today's articles
    prefix = today
    today_files = sorted([
        f for f in os.listdir(POSTS_DIR)
        if f.startswith(prefix) and f.endswith(".md")
    ], reverse=True)
    
    print(f"Today's files: {today_files}")
    
    success_count = 0
    for filename in today_files:
        # Extract slug: remove date prefix and .md extension
        slug = filename[len(prefix)+1:-3]  # +1 for the dash
        filepath = os.path.join(POSTS_DIR, filename)
        
        if slug in posted:
            print(f"\nSKIP (already posted): {slug}")
            continue
        
        print(f"\nPROCESSING: {slug}")
        if process_article(filepath, slug):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY: {success_count}/{len(today_files)} articles posted to Dev.to")
    
    if success_count == 0:
        print("[SILENT]")  # Will be filtered
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
