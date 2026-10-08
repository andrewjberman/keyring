#!/bin/sh
# Wire the fabric-activity post-commit trigger (idempotent). APPENDS to the existing post-commit hook (never clobbers
# siblings); re-run safe. Same pattern as install-prd-header-notify.sh. Andrew-direct 2026-10-08 ~17:0xZ ("Call 1,
# sure"): every box installs it, each box's MSTR running this once. Rollback: delete the two lines it adds.
set -e
WS="$(git rev-parse --show-toplevel)"
HOOK="$(git rev-parse --git-common-dir)/hooks/post-commit"
case "$HOOK" in /*|?:*) ;; *) HOOK="$WS/$HOOK" ;; esac
if [ ! -f "$HOOK" ]; then
  printf '#!/bin/sh\n' > "$HOOK"
  chmod +x "$HOOK"
fi
mark="fabric-activity-post-commit"
if grep -q "$mark" "$HOOK" 2>/dev/null; then
  echo "OK: $mark already wired in $HOOK"
  exit 0
fi
python -c "import sys; sys.path.insert(0, 'lib'); import devices; n, b = devices.this_device(); print('box:', n or 'UNRESOLVED', '|', b)" 2>&1 || true
line1="$(printf '\n# %s (installed %s; who-is-working-on-what activity record; backgrounded, never blocks)' "$mark" "$(date -u +%Y-%m-%dT%H:%M:%SZ)")"
line2="$(printf '_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && [ -f "$_ws/.tools/git-hooks/%s.sh" ] && sh "$_ws/.tools/git-hooks/%s.sh"' "$mark" "$mark")"
if grep -q '^exit 0[[:space:]]*$' "$HOOK" 2>/dev/null; then
  tmp="$HOOK.tmp.$$"
  awk -v l1="$line1" -v l2="$line2" '
    /^exit 0[[:space:]]*$/ && !done { print l1; print l2; done=1 }
    { print }' "$HOOK" > "$tmp" && mv -f "$tmp" "$HOOK"
else
  printf '%s\n%s\n' "$line1" "$line2" >> "$HOOK"
fi
chmod +x "$HOOK"
echo "OK: wired $mark into $HOOK"
