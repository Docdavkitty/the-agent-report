#!/usr/bin/env python3
import json, re, sys, urllib.request, urllib.error

BASE = "/home/freebox/the-agent-report/_posts/"
TRACKING = "/home/freebox/.hermes/devto_posted.txt"
API_KEY = "Jg2dEJuXgS6usj4Siori8jB3"
API_URL = "https://dev.to/api/articles"
SITE = "https://the-agent-report.com"

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

def parse_frontmatter(text):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
    if not m:
        raise ValueError("no frontmatter")
    fm_raw = m.group(1)
    body = m.group(2)
    if HAVE_YAML:
        fm = yaml.safe_load(fm_raw)
    else:
        fm = {}
        # minimal fallback: not expected
    return fm, body

def make_tags(fm):
    tags = fm.get('tags') or []
    out = []
    for t in tags[:4]:
        t = str(t).lower().replace('-', '').replace('_', '')
        if len(t) > 12:
            t = t[:12]
        out.append(t)
    return out

def truncate(s, n=155):
    s = s.strip()
    return s if len(s) <= n else s[:n].rstrip()

def load_tracking():
    try:
        with open(TRACKING) as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def append_tracking(slug):
    with open(TRACKING, 'a') as f:
        f.write(slug + "\n")

import os
files = [f for f in os.listdir(BASE) if f.endswith('.md')]
files = sorted(files, reverse=True)
today = '2026-08-27'
todays = [f for f in files if f.startswith(today + '-')]
print("Today's files:", todays)

posted = load_tracking()
print("Tracking has", len(posted), "entries")

results = []
for fname in todays:
    # slug = filename without date prefix and .md
    slug = fname[len(today)+1:-3]
    if slug in posted:
        print(f"[SKIP] already posted: {slug}")
        continue
    with open(BASE + fname) as f:
        text = f.read()
    fm, body = parse_frontmatter(text)
    title = fm.get('title', '')
    desc = truncate(fm.get('meta_description', ''))
    tags = make_tags(fm)
    # canonical url
    permalink = fm.get('permalink')
    if permalink:
        canonical = SITE + permalink
    else:
        canonical = f"{SITE}/2026/08/{fm.get('ref', slug)}/"

    body_final = body.rstrip() + "\n\n---\n*Cet article a été initialement publié sur [The Agent Report](https://the-agent-report.com/).*\n"

    payload = {
        "article": {
            "title": title,
            "body_markdown": body_final,
            "published": True,
            "canonical_url": canonical,
            "description": desc,
            "tags": tags,
            "series": "The Agent Report",
        }
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(API_URL, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'TheAgentReport/1.0')
    req.add_header('api-key', API_KEY)
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        code = resp.getcode()
        rbody = resp.read().decode('utf-8')
        results.append((fname, code, rbody))
        if code in (200, 201):
            append_tracking(slug)
            print(f"[POSTED] {slug} -> {code}")
            print("  title:", title)
            print("  tags:", tags)
            print("  desc:", desc)
            print("  canonical:", canonical)
            print("  desc_len:", len(desc))
        else:
            print(f"[ERROR] {slug} -> {code}: {rbody}")
    except urllib.error.HTTPError as e:
        rbody = e.read().decode('utf-8')
        results.append((fname, e.code, rbody))
        print(f"[HTTP ERROR] {slug} -> {e.code}: {rbody}")
    except Exception as e:
        results.append((fname, 'EXC', str(e)))
        print(f"[EXC] {slug}: {e}")

print("\n=== SUMMARY ===")
for r in results:
    print(r[0], "->", r[1])
