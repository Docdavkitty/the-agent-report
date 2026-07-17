#!/usr/bin/env python3
"""Post today's articles to Dev.to that haven't been posted yet."""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
DEVTO_API = "https://dev.to/api/articles"
POSTS_DIR = "/home/freebox/the-agent-report/_posts"
TRACKING_FILE = os.path.expanduser("~/.hermes/devto_posted.txt")
SITE_URL = "https://the-agent-report.com"

def load_posted_slugs():
    """Load already-posted slugs from tracking file."""
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE) as f:
        return set(line.strip() for line in f if line.strip())

def save_posted_slug(slug):
    """Append a posted slug to the tracking file."""
    with open(TRACKING_FILE, "a") as f:
        f.write(slug + "\n")
    print(f"  ✓ Tracking updated: {slug}")

def parse_frontmatter_and_body(content):
    """Parse YAML frontmatter and body from markdown content."""
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return {}, content
    frontmatter_text = parts[1]
    body = parts[2]
    
    # Simple YAML parsing (handles the fields we need)
    meta = {}
    for line in frontmatter_text.strip().split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if key == "tags" or (value.startswith("[") and value.endswith("]")):
                # Parse list: strip brackets, split by comma, strip quotes/spaces
                v = value
                if v.startswith("["):
                    v = v[1:]
                if v.endswith("]"):
                    v = v[:-1]
                items = []
                for item in v.split(","):
                    item = item.strip().strip('"').strip("'")
                    if item:
                        items.append(item)
                value = items
            else:
                value = value.strip().strip('"').strip("'")
            meta[key] = value
    return meta, body

def get_slug(filename):
    """Extract slug from filename: YYYY-MM-DD-slug.md → slug"""
    base = filename.replace(".md", "")
    parts = base.split("-", 3)
    if len(parts) >= 4:
        return parts[3]
    return base

def get_date_prefix(filename):
    """Extract YYYY-MM-DD from filename."""
    base = filename.replace(".md", "")
    parts = base.split("-", 3)
    if len(parts) >= 3:
        return f"{parts[0]}-{parts[1]}-{parts[2]}"
    return ""

def prepare_tags(tags):
    """Take up to 4 tags, lowercase, remove hyphens, truncate to 12 chars."""
    result = []
    for tag in tags[:4]:
        tag = tag.lower().replace("-", "").replace(" ", "")
        if len(tag) > 12:
            tag = tag[:12]
        result.append(tag)
    return result

def build_canonical_url(meta, slug, date_prefix):
    """Build canonical URL for the article."""
    year, month, day = date_prefix.split("-")
    if meta.get("lang") == "fr":
        return f"{SITE_URL}/fr/{year}/{month}/{slug}/"
    return f"{SITE_URL}/{year}/{month}/{slug}/"

def post_to_devto(title, body_markdown, canonical_url, description, tags):
    """POST an article to Dev.to API."""
    # Truncate description to 155 chars
    desc = description[:155] if description else ""
    
    payload = {
        "article": {
            "title": title,
            "body_markdown": body_markdown,
            "published": True,
            "canonical_url": canonical_url,
            "description": desc,
            "tags": tags,
            "series": "The Agent Report"
        }
    }
    
    json_payload = json.dumps(payload, ensure_ascii=False)
    
    cmd = [
        "curl", "-s", "-w", "\n%{http_code}",
        "-X", "POST", DEVTO_API,
        "-H", "Content-Type: application/json",
        "-H", f"api-key: {API_KEY}",
        "-d", json_payload,
        "--max-time", "30"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
    output = result.stdout.strip()
    
    # Split response body and HTTP code
    lines = output.rsplit("\n", 1)
    if len(lines) == 2:
        response_body, http_code = lines
    else:
        response_body = output
        http_code = "000"
    
    if http_code == "201":
        try:
            resp = json.loads(response_body)
            print(f"  ✅ Posted! Dev.to ID: {resp.get('id')}, URL: {resp.get('url')}")
            return True
        except json.JSONDecodeError:
            print(f"  ✅ Posted! (HTTP 201, raw response: {response_body[:200]})")
            return True
    else:
        print(f"  ❌ Failed (HTTP {http_code}): {response_body[:300]}")
        return False

def main():
    today_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"=== Dev.to Cross-Post — {today_utc} ===\n")
    
    # Load tracking
    posted = load_posted_slugs()
    print(f"Tracking: {len(posted)} slugs already posted\n")
    
    # Find today's articles
    files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith(".md") and f != "meta_descriptions.json"], reverse=True)
    
    today_files = [f for f in files if get_date_prefix(f) == today_utc]
    
    if not today_files:
        print("No articles for today. [SILENT]")
        return 1  # signal silent
    
    print(f"Found {len(today_files)} article(s) for today:")
    for f in today_files:
        print(f"  - {f}")
    print()
    
    posted_count = 0
    
    for filename in today_files:
        slug = get_slug(filename)
        date_prefix = get_date_prefix(filename)
        
        if slug in posted:
            print(f"⏭  SKIP '{filename}' — slug '{slug}' already posted")
            continue
        
        print(f"📝 Processing: {filename}")
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath) as f:
            content = f.read()
        
        meta, body = parse_frontmatter_and_body(content)
        
        title = meta.get("title", slug)
        description = meta.get("meta_description", meta.get("description", ""))
        tags = prepare_tags(meta.get("tags", []))
        canonical_url = build_canonical_url(meta, slug, date_prefix)
        
        # Add footer
        footer = "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*"
        body_markdown = body.rstrip() + footer
        
        print(f"  Title: {title}")
        print(f"  Canonical: {canonical_url}")
        print(f"  Desc: {description[:80]}...")
        print(f"  Tags: {tags}")
        
        success = post_to_devto(title, body_markdown, canonical_url, description, tags)
        
        if success:
            save_posted_slug(slug)
            posted_count += 1
        
        print()
    
    if posted_count == 0:
        print("All today's articles were already posted. [SILENT]")
        return 1
    
    print(f"=== Done: {posted_count} article(s) posted ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
