#!/bin/sh
# Wire the R3 prd-header-notify post-commit trigger (idempotent). APPENDS to the existing
# post-commit hook (never clobbers siblings); re-run safe. Same pattern as install-directives-check.sh.
set -e
WS="$(git rev-parse --show-toplevel)"
HOOK="$WS/.git/hooks/post-commit"
mkdir -p "$WS/org/mcp/.prd-notify"
if [ ! -f "$HOOK" ]; then
  printf '#!/bin/sh\n' > "$HOOK"
  chmod +x "$HOOK"
fi
mark="prd-header-notify-post-commit"
if grep -q "$mark" "$HOOK" 2>/dev/null; then
  echo "OK: $mark already wired in $HOOK"
  exit 0
fi
line1="$(printf '\n# %s (installed %s; R3 notifier, release condition 7; backgrounded, never blocks)' "$mark" "$(date -u +%Y-%m-%dT%H:%M:%SZ)")"
line2="$(printf '_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/%s.sh"' "$mark")"
if grep -q '^exit 0[[:space:]]*$' "$HOOK" 2>/dev/null; then
  # insert before the final exit 0 (LD-0343 pre-exit insert pattern)
  tmp="$HOOK.tmp.$$"
  awk -v l1="$line1" -v l2="$line2" '
    /^exit 0[[:space:]]*$/ && !done { print l1; print l2; done=1 }
    { print }' "$HOOK" > "$tmp" && mv -f "$tmp" "$HOOK"
else
  printf '%s\n%s\n' "$line1" "$line2" >> "$HOOK"
fi
chmod +x "$HOOK"
echo "OK: wired $mark into $HOOK"
