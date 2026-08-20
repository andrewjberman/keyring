#!/usr/bin/env bash
# Wire the LD-0433 directives-check post-commit trigger (idempotent):
#   directives-check-post-commit.sh -- comp-directives invariants at the register-touch moment.
# APPENDS to the existing post-commit hook (never clobbers siblings). Re-run safe.
# Pattern verbatim from install-closeout-comp-state.sh incl. BOTH its LD-0343 lessons:
# run-time root resolution (never an install-time absolute path) + insert BEFORE any trailing
# `exit 0` (a line appended after it never executes and reads exactly like success).
set -e
WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK="$WS/.git/hooks/post-commit"

if [ ! -f "$HOOK" ]; then
  printf '#!/bin/sh\n' > "$HOOK"
fi

mark="directives-check-post-commit"
body="$WS/.tools/git-hooks/${mark}.sh"
if grep -q "$mark" "$HOOK" 2>/dev/null; then
  echo "OK: $mark already wired (idempotent no-op)."
else
  if [ ! -f "$body" ]; then
    echo "FAIL: body not found at $body -- refusing to wire a dead hook line." >&2
    exit 1
  fi
  line1="$(printf '\n# %s (installed %s; run-time root + pre-exit insert, LD-0343 pattern)' "$mark" "$(date -u +%Y-%m-%dT%H:%M:%SZ)")"
  line2="$(printf '_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/%s.sh"' "$mark")"
  if grep -q '^exit 0[[:space:]]*$' "$HOOK" 2>/dev/null; then
    tmp="$HOOK.tmp.$$"
    sed '/^exit 0[[:space:]]*$/d' "$HOOK" > "$tmp"
    printf '%s\n%s\nexit 0\n' "$line1" "$line2" >> "$tmp"
    mv "$tmp" "$HOOK"
  else
    printf '%s\n%s\n' "$line1" "$line2" >> "$HOOK"
  fi
  echo "OK: wired $mark -> $HOOK"
fi
chmod +x "$HOOK" 2>/dev/null || true
