#!/usr/bin/env bash
# Wire the NFRA_MSBEFF.R4 post-commit triggers (idempotent):
#   R4-A closeout->comp-state       (closeout-comp-state-post-commit.sh)
#   R4-B deploy->pipescript-deployed (deploy-pipescript-check-post-commit.sh)
# APPENDS each to the existing post-commit hook (never clobbers stitch-refresh). Re-run safe.
#
# TWO DEFECTS FIXED 2026-07-29 (LD-0343) -- both were LATENT because this installer had
# never actually been run on the base device (the pre-missions post-commit backup contains
# only stitch-refresh). Running it via the new .tools/install-all-git-hooks.sh exposed both
# at once, and it wired TWO DEAD LINES before they were caught:
#
#   (1) APPENDED AFTER `exit 0`. The post-commit hook acquired a trailing `exit 0`, so any
#       line appended below it NEVER EXECUTES. The install printed "OK: wired ..." and the
#       hook did nothing, forever -- a silent no-op that looks exactly like success.
#       Now: insert BEFORE any trailing `exit 0`.
#
#   (2) BAKED AN INSTALL-TIME ABSOLUTE PATH into the hook line. `$WS` is a `pwd`-derived
#       path in the INSTALLING shell's flavor (MSYS `/c/...` under Git Bash, `/cygdrive/c/...`
#       under Cygwin), and the hook is plain `sh` that may be EXECUTED under a different
#       flavor. It is also a USER-rooted path, which breaks on any clone at a different
#       location (Andrew-direct: repo functions cap at the REPO path). install-stitch-refresh.sh
#       already documented and fixed this class 2026-07-25; this file was never updated.
#       Now: resolve at RUN time via `git rev-parse --show-toplevel`, matching its sibling.
set -e
WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK="$WS/.git/hooks/post-commit"

if [ ! -f "$HOOK" ]; then
  printf '#!/bin/sh\n' > "$HOOK"
fi

wire() {  # $1 = marker/body-basename
  local mark="$1"
  local body="$WS/.tools/git-hooks/${mark}.sh"
  if grep -q "$mark" "$HOOK" 2>/dev/null; then
    echo "OK: $mark already wired (idempotent no-op)."
    return 0
  fi
  if [ ! -f "$body" ]; then
    echo "FAIL: body not found at $body -- refusing to wire a dead hook line." >&2
    return 1
  fi
  # Run-time root resolution + insert before any trailing `exit 0`. See header.
  local line1 line2
  line1="$(printf '\n# %s (installed %s; run-time root + pre-exit insert, LD-0343)' "$mark" "$(date -u +%Y-%m-%dT%H:%M:%SZ)")"
  line2="$(printf '_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/%s.sh"' "$mark")"
  if grep -q '^exit 0[[:space:]]*$' "$HOOK" 2>/dev/null; then
    local tmp="$HOOK.tmp.$$"
    sed '/^exit 0[[:space:]]*$/d' "$HOOK" > "$tmp"
    printf '%s\n%s\nexit 0\n' "$line1" "$line2" >> "$tmp"
    mv "$tmp" "$HOOK"
  else
    printf '%s\n%s\n' "$line1" "$line2" >> "$HOOK"
  fi
  echo "OK: wired $mark -> $HOOK"
}

wire "closeout-comp-state-post-commit"
wire "deploy-pipescript-check-post-commit"
chmod +x "$HOOK" 2>/dev/null || true
