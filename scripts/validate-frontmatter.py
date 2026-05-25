#!/usr/bin/env python3
"""Validate and fix Jekyll post frontmatter for The Agent Report.

Checks:
  - layout: post (required for Jekyll post template)
  - author: The Agent Report (required for author display)
  - last_modified_at: <date> (required for freshness metadata)

Usage:
  ./validate-frontmatter.py          # check only, exit 1 on errors
  ./validate-frontmatter.py --fix    # auto-fix missing fields
"""

import os
import re
import sys

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
FIX_MODE = '--fix' in sys.argv

REQUIRED_FIELDS = {
    'layout': 'post',
    'author': 'The Agent Report',
}

def parse_frontmatter(lines):
    """Return (start, end) indices of frontmatter, or (None, None)."""
    if not lines or lines[0].strip() != '---':
        return None, None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break
    if end is None:
        return None, None
    return 0, end

def check_file(filepath):
    basename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fm_start, fm_end = parse_frontmatter(lines)
    if fm_start is None:
        return 0  # no frontmatter, skip

    fm_lines = lines[fm_start+1:fm_end]  # between the two ---
    has_layout = any(re.match(r'^layout:\s', l) for l in fm_lines)
    has_author = any(re.match(r'^author:\s', l) for l in fm_lines)
    has_lastmod = any(re.match(r'^last_modified_at:\s', l) for l in fm_lines)
    has_date = any(re.match(r'^date:\s', l) for l in fm_lines)

    errors = 0
    fixes = []

    if not has_layout:
        errors += 1
        if FIX_MODE:
            fixes.append(('layout', 1, 'layout: post\n'))
            print(f"  ❌ layout: post  — manquant → ✅ ajouté")

    if not has_author:
        errors += 1
        if FIX_MODE:
            fixes.append(('author', fm_end, 'author: The Agent Report\n'))
            print(f"  ❌ author — manquant → ✅ ajouté")

    # last_modified_at: use date value if available
    if not has_lastmod:
        date_val = ''
        for l in fm_lines:
            m = re.match(r'^date:\s*(.+)', l)
            if m:
                date_val = m.group(1).strip()
                break
        errors += 1
        if FIX_MODE and date_val:
            # find the date line index in original file
            for i in range(fm_start + 1, fm_end):
                if re.match(r'^date:\s', lines[i]):
                    fixes.append(('last_modified_at', i + 1, f'last_modified_at: {date_val}\n'))
                    break
            print(f"  ❌ last_modified_at — manquant → ✅ ajouté (copié de date: {date_val})")
        elif FIX_MODE and not date_val:
            print(f"  ⚠️  last_modified_at manquant et pas de date — impossible de fix auto")

    if errors == 0:
        return 0

    # Apply fixes (in reverse order to preserve line indices)
    if FIX_MODE and fixes:
        fixes.sort(key=lambda x: x[1], reverse=True)
        for field, idx, text in fixes:
            lines.insert(idx, text)

        # layout goes right after the opening ---
        if any(f[0] == 'layout' for f in fixes):
            pass  # already handled

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    if errors > 0 and not FIX_MODE:
        details = []
        if not has_layout:
            details.append('layout')
        if not has_author:
            details.append('author')
        if not has_lastmod:
            details.append('last_modified_at')
        print(f"  ❌ {', '.join(details)} — manquant")
        return errors

    return 0

def main():
    print(f"=== Validation des frontmatter — The Agent Report ===")
    print(f"Dossier : {POSTS_DIR}")
    print(f"Mode : {'🔧 AUTO-FIX' if FIX_MODE else '🔍 CHECK ONLY'}")
    print()

    total_errors = 0
    total_files = 0
    error_files = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith('.md'):
            continue
        total_files += 1
        fpath = os.path.join(POSTS_DIR, fname)
        errs = check_file(fpath)
        if errs > 0:
            total_errors += errs
            error_files.append(fname)
            if not FIX_MODE:
                print(f"  → {errs} erreur(s) dans {fname}")

    print()
    if total_errors > 0:
        if FIX_MODE:
            print(f"✅ {len(error_files)} fichiers corrigés ({total_errors} fixes appliqués).")
        else:
            print(f"⚠️  {total_errors} erreur(s) dans {len(error_files)}/{total_files} fichiers.")
            print(f"   Relancez avec --fix pour corriger automatiquement.")
            sys.exit(1)
    else:
        print(f"✅ Tous les {total_files} articles sont valides !")

if __name__ == '__main__':
    main()
