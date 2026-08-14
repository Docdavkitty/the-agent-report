#!/usr/bin/env python3
"""Cross-post today's articles to Dev.to (correct canonical URLs + FR handling)."""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
DEVTO_API = "https://dev.to/api/articles"
POSTS_DIR = "/home/freebox/the-agent-report/_posts"
TRACKING_FILE = os.path.expanduser("~/.hermes/devto_posted.txt")
SITE_URL = "https://the-agent-report.com"
FOOTER = "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*"


def load_posted():
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE) as f:
        return set(line.strip() for line in f if line.strip())


def save_slug(slug):
    with open(TRACKING_FILE, "a") as f:
        f.write(slug + "\n")


def get_slug(filename):
    base = filename.replace(".md", "")
    parts = base.split("-", 3)
    if len(parts) >= 4:
        return parts[3]
    return base


def get_date_prefix(filename):
    base = filename.replace(".md", "")
    parts = base.split("-", 3)
    if len(parts) >= 3:
        return f"{parts[0]}-{parts[1]}-{parts[2]}"
    return ""


def parse(content):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not m:
        return {}, content.strip()
    fm_text, body = m.group(1), m.group(2)
    meta = {}
    for line in fm_text.split("\n"):
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if key == "tags":
            v = value.strip()
            if v.startswith("["):
                v = v[1:]
            if v.endswith("]"):
                v = v[:-1]
            items = []
            for it in v.split(","):
                it = it.strip().strip('"').strip("'")
                if it:
                    items.append(it)
            meta[key] = items
        else:
            v = value.strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            meta[key] = v
    return meta, body.strip()


def prepare_tags(tags):
    result = []
    for tag in tags[:4]:
        t = tag.lower().replace("-", "").replace(" ", "")
        if len(t) > 12:
            t = t[:12]
        result.append(t)
    return result


def canonical_url(meta, slug, date_prefix):
    year, month, day = date_prefix.split("-")
    permalink = meta.get("permalink", "")
    if permalink:
        return SITE_URL + permalink.rstrip("/") + "/"
    if meta.get("lang") == "fr":
        base_slug = slug[:-3] if slug.endswith("-fr") else slug
        return f"{SITE_URL}/fr/{year}/{month}/{base_slug}/"
    return f"{SITE_URL}/{year}/{month}/{slug}/"


def post(payload):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    for attempt in range(6):
        req = urllib.request.Request(DEVTO_API, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("api-key", API_KEY)
        req.add_header("User-Agent", "The-Agent-Report/1.0")
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return resp.status, resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            code = e.code
            body = e.read().decode("utf-8")
            if code == 429:
                time.sleep(20 * (attempt + 1))
                continue
            return code, body
        except Exception as e:
            return 0, str(e)
    return 429, "rate limited"


def main():
    today_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    posted = load_posted()

    files = sorted(
        [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")],
        reverse=True,
    )
    today_files = [f for f in files if get_date_prefix(f) == today_utc]

    if not today_files:
        print("NO_TODAY")
        return

    results = []
    for filename in today_files:
        slug = get_slug(filename)
        date_prefix = get_date_prefix(filename)
        if slug in posted:
            results.append((filename, slug, "SKIP", ""))
            continue
        with open(os.path.join(POSTS_DIR, filename)) as f:
            content = f.read()
        meta, body = parse(content)
        title = meta.get("title", slug)
        description = (meta.get("meta_description") or meta.get("description") or "")[:155]
        tags = prepare_tags(meta.get("tags", []))
        curl = canonical_url(meta, slug, date_prefix)
        body_markdown = body + FOOTER
        payload = {
            "article": {
                "title": title,
                "body_markdown": body_markdown,
                "published": True,
                "canonical_url": curl,
                "description": description,
                "tags": tags,
                "series": "The Agent Report",
            }
        }
        code, resp_body = post(payload)
        if code == 201:
            try:
                j = json.loads(resp_body)
                durl = j.get("url", "")
            except Exception:
                durl = ""
            save_slug(slug)
            results.append((filename, slug, "POSTED", durl))
        else:
            results.append((filename, slug, f"FAILED({code})", resp_body[:200]))

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
