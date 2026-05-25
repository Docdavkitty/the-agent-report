#!/usr/bin/env bash
# Validate Jekyll post frontmatter for The Agent Report
# Checks: layout, author, last_modified_at on every _posts/*.md
# Usage: ./scripts/validate-frontmatter.sh [--fix]
#   --fix : auto-insert missing fields using date value for last_modified_at

set -euo pipefail

POSTS_DIR="$(cd "$(dirname "$0")/../_posts" && pwd)"
FIX_MODE=false
HAS_ERRORS=false

if [[ "${1:-}" == "--fix" ]]; then
  FIX_MODE=true
fi

check_post() {
  local file="$1"
  local basename
  basename="$(basename "$file")"
  local errors=0
  local fixable=0

  # Read frontmatter (between first two ---)
  local fm
  fm="$(sed -n '1,/^---$/p' "$file" | head -n -1 | tail -n +2)"

  # Check layout
  if ! echo "$fm" | grep -q '^layout: '; then
    echo "  ❌ layout: post  — manquant"
    errors=$((errors + 1))
    if $FIX_MODE; then
      if [[ "$(uname)" == "Darwin" ]]; then
        sed -i '' '2s/^/layout: post\n/' "$file"
      else
        sed -i '2s/^/layout: post\n/' "$file"
      fi
      echo "     → ✅ ajouté"
      fixable=$((fixable + 1))
    fi
  fi

  # Check author
  if ! echo "$fm" | grep -q '^author: '; then
    echo "  ❌ author — manquant"
    errors=$((errors + 1))
    if $FIX_MODE; then
      # Insert before last line of frontmatter (before ---)
      if [[ "$(uname)" == "Darwin" ]]; then
        sed -i '' '$s/^/author: The Agent Report\n/' "$file"
      else
        sed -i '$s/^/author: The Agent Report\n/' "$file"
      fi
      echo "     → ✅ ajouté"
      fixable=$((fixable + 1))
    fi
  fi

  # Check last_modified_at
  if ! echo "$fm" | grep -q '^last_modified_at: '; then
    local post_date
    post_date="$(echo "$fm" | grep '^date: ' | sed 's/^date: //')"
    echo "  ❌ last_modified_at — manquant (date du post: ${post_date:-inconnue})"
    errors=$((errors + 1))
    if $FIX_MODE && [[ -n "$post_date" ]]; then
      local date_line
      date_line="$(grep -n '^date: ' "$file" | head -1 | cut -d: -f1)"
      if [[ -n "$date_line" ]]; then
        insert_at=$((date_line + 1))
        if [[ "$(uname)" == "Darwin" ]]; then
          sed -i '' "${insert_at}i\\
last_modified_at: ${post_date}" "$file"
        else
          sed -i "${insert_at}ilast_modified_at: ${post_date}" "$file"
        fi
        echo "     → ✅ ajouté (last_modified_at: ${post_date})"
        fixable=$((fixable + 1))
      fi
    fi
  fi

  if [[ $errors -gt 0 ]]; then
    echo "  → $errors erreur(s) dans $basename"
    HAS_ERRORS=true
  fi
}

echo "=== Validation des frontmatter — The Agent Report ==="
echo "Dossier : $POSTS_DIR"
echo "Mode : $([ "$FIX_MODE" = true ] && echo '🔧 AUTO-FIX' || echo '🔍 CHECK ONLY')"
echo ""

for f in "$POSTS_DIR"/*.md; do
  check_post "$f"
done

echo ""
if $HAS_ERRORS; then
  if $FIX_MODE; then
    echo "✅ Corrections appliquées."
  else
    echo "⚠️  Des erreurs détectées. Relancez avec --fix pour corriger automatiquement."
    exit 1
  fi
else
  echo "✅ Tous les articles sont valides !"
fi
