#!/usr/bin/env bash
# Wire the NFRA_MSBEFF.R4 post-commit triggers (idempotent):
#   R4-A closeout->comp-state       (closeout-comp-state-post-commit.sh)
#   R4-B deploy->pipescript-deployed (deploy-pipescript-check-post-commit.sh)
# APPENDS each to the existing post-commit hook (never clobbers stitch-refresh). Re-run safe.
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
  printf '\n# %s (installed %s)\nsh "%s"\n' "$mark" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$body" >> "$HOOK"
  echo "OK: wired $mark -> $HOOK"
}

wire "closeout-comp-state-post-commit"
wire "deploy-pipescript-check-post-commit"
chmod +x "$HOOK" 2>/dev/null || true
