#!/usr/bin/env bash
# install-owned-paths.sh -- Idempotent bootstrap for the owned-paths pre-commit hook.
#
# Usage: bash .tools/git-hooks/install-owned-paths.sh
#
# - Creates .git/hooks/pre-commit (wrapper that delegates to owned-paths-check.sh)
# - If .git/hooks/pre-commit already contains an owned-paths reference: no-op
# - If .git/hooks/pre-commit exists with different content: chains the existing hook
#   by inserting an exec call to owned-paths-check.sh after it
# - Safe to re-run: idempotent
#
# Exit codes:
#   0 = hook installed or already present (idempotent no-op)
#   1 = owned-paths-check.sh not found (TO 2 not yet shipped)
#
# ADHC_OWNPTH.003 (0.7.0_AE_CloudOps, 2026-04-24)

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_SRC="$REPO_ROOT/.tools/git-hooks/owned-paths-check.sh"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"

# Gate: TO 2 must be shipped
if [ ! -f "$HOOK_SRC" ]; then
    echo "ERROR: $HOOK_SRC not found -- ADHC_OWNPTH.002 (DS hook script) must ship first." >&2
    exit 1
fi

# Already wired check: look for owned-paths-check.sh reference in existing hook
if [ -f "$HOOK_DEST" ] && grep -q "owned-paths-check.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: owned-paths hook already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

# Generate the wrapper content
WRAPPER='#!/usr/bin/env bash
# owned-paths hook wrapper -- delegates to .tools/git-hooks/owned-paths-check.sh
# Windows Git Bash does not support true symlinks without Developer Mode.
# This wrapper ensures the hook always executes the current source version.
# ADHC_OWNPTH.003
HOOK="$(git rev-parse --show-toplevel 2>/dev/null)/.tools/git-hooks/owned-paths-check.sh"
if [ ! -f "$HOOK" ]; then
    echo "WARN: owned-paths-check.sh not found at $HOOK -- skipping lane check" >&2
    exit 0
fi
exec bash "$HOOK" "$@"'

if [ ! -f "$HOOK_DEST" ]; then
    # Clean install: write wrapper directly
    printf '%s\n' "$WRAPPER" > "$HOOK_DEST"
    chmod +x "$HOOK_DEST"
    echo "OK: owned-paths hook installed at $HOOK_DEST"
else
    # Pre-existing hook: chain by creating a wrapper that calls both
    EXISTING="$(cat "$HOOK_DEST")"
    CHAIN="#!/usr/bin/env bash
# owned-paths chain wrapper -- calls pre-existing hook then owned-paths-check.sh
# ADHC_OWNPTH.003 (chained)
set -e

# Pre-existing hook (inlined)
$EXISTING

# owned-paths lane check
OWNED_HOOK=\"\$(git rev-parse --show-toplevel 2>/dev/null)/.tools/git-hooks/owned-paths-check.sh\"
if [ -f \"\$OWNED_HOOK\" ]; then
    bash \"\$OWNED_HOOK\" \"\$@\"
fi"
    printf '%s\n' "$CHAIN" > "$HOOK_DEST"
    chmod +x "$HOOK_DEST"
    echo "OK: owned-paths hook chained after existing pre-commit at $HOOK_DEST"
fi
