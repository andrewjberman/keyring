#!/usr/bin/env bash
# install-safe-deploy-hook.sh -- Idempotent bootstrap for the pre-push safe-deploy gate.
# ADHC_DSFLOW.005 (0.7.0_AE_CloudOps, 2026-05-11)
#
# Usage: bash .tools/git-hooks/install-safe-deploy-hook.sh
#
# - Creates .git/hooks/pre-push (delegates to pre-push-safe-deploy.sh)
# - If .git/hooks/pre-push already contains a pre-push-safe-deploy reference: no-op
# - If .git/hooks/pre-push exists with different content: chains the existing hook
# - Safe to re-run: idempotent

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_SRC="$REPO_ROOT/.tools/git-hooks/pre-push-safe-deploy.sh"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-push"

if [ ! -f "$HOOK_SRC" ]; then
    echo "ERROR: $HOOK_SRC not found -- ADHC_DSFLOW.005 must ship first" >&2
    exit 1
fi

# Already wired check
if [ -f "$HOOK_DEST" ] && grep -q "pre-push-safe-deploy.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: safe-deploy pre-push hook already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

WRAPPER='#!/usr/bin/env bash
# safe-deploy pre-push hook -- delegates to .tools/git-hooks/pre-push-safe-deploy.sh
# ADHC_DSFLOW.005
HOOK="$(git rev-parse --show-toplevel 2>/dev/null)/.tools/git-hooks/pre-push-safe-deploy.sh"
if [ ! -f "$HOOK" ]; then
    echo "WARN: pre-push-safe-deploy.sh not found at $HOOK -- skipping deploy gate" >&2
    exit 0
fi
exec bash "$HOOK" "$@"'

if [ ! -f "$HOOK_DEST" ]; then
    printf '%s\n' "$WRAPPER" > "$HOOK_DEST"
    chmod +x "$HOOK_DEST"
    echo "OK: safe-deploy pre-push hook installed at $HOOK_DEST"
else
    # Chain after existing hook
    EXISTING="$(cat "$HOOK_DEST")"
    CHAIN='#!/usr/bin/env bash
# safe-deploy chain wrapper -- runs pre-existing pre-push hook then safe-deploy gate
# ADHC_DSFLOW.005 (chained)
set -e
'"$EXISTING"'
# safe-deploy gate
SAFE_HOOK="$(git rev-parse --show-toplevel 2>/dev/null)/.tools/git-hooks/pre-push-safe-deploy.sh"
if [ -f "$SAFE_HOOK" ]; then
    bash "$SAFE_HOOK" "$@"
fi'
    printf '%s\n' "$CHAIN" > "$HOOK_DEST"
    chmod +x "$HOOK_DEST"
    echo "OK: safe-deploy gate chained after existing pre-push at $HOOK_DEST"
fi
