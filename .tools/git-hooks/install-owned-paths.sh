#!/usr/bin/env bash
# install-owned-paths.sh -- Idempotent bootstrap for the owned-paths pre-commit hook.
#
# Usage: bash .tools/git-hooks/install-owned-paths.sh
#        bash .tools/git-hooks/install-owned-paths.sh --submodule <parent-relative-path>
#
# - Creates .git/hooks/pre-commit (wrapper that delegates to owned-paths-check.sh)
# - If .git/hooks/pre-commit already contains an owned-paths reference: no-op
# - If .git/hooks/pre-commit exists with different content: chains the existing hook
#   by inserting an exec call to owned-paths-check.sh after it
# - Safe to re-run: idempotent
# - --submodule <path>: installs into the NAMED nested repo's OWN hooks dir instead of
#   this repo's. <path> is parent-relative (e.g. "opal_ai"). The nested repo's hooks
#   dir is resolved via `git -C <path> rev-parse --absolute-git-dir`, which follows a
#   submodule's gitfile pointer (".git" is a FILE there, not a directory -- appending
#   "/hooks/pre-commit" to a plain toplevel path is wrong (OA-w-2)) to the real gitdir
#   under the superproject's .git/modules/<name>, whether <path> is the submodule's own
#   registered checkout or one of its linked worktrees.
#   BOUND: this script never targets the real opal_ai on its own -- the caller names the
#   path, and the round's issuer is the only caller with standing to name the real one.
#
# Exit codes:
#   0 = hook installed or already present (idempotent no-op)
#   1 = owned-paths-check.sh not found (TO 2 not yet shipped), or --submodule path
#       does not resolve to a git worktree
#
# ADHC_OWNPTH.003 (0.7.0_AE_CloudOps, 2026-04-24); --submodule: OA-w-2 (2026-09-24)

set -euo pipefail

# Resolve the repo from THIS SCRIPT's location, never the caller's ambient cwd (row NFRA_OPALAI-Z-W5-S1):
# invoked by absolute path from another repo's cwd, the ambient form silently targeted that other repo.
_SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(git -C "$_SELF_DIR" rev-parse --show-toplevel 2>/dev/null || git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_SRC="$REPO_ROOT/.tools/git-hooks/owned-paths-check.sh"

SUBMODULE_PATH=""
while [ $# -gt 0 ]; do
    case "$1" in
        --submodule)
            SUBMODULE_PATH="${2:-}"
            shift 2
            ;;
        --submodule=*)
            SUBMODULE_PATH="${1#--submodule=}"
            shift
            ;;
        *)
            echo "ERROR: unrecognized argument: $1" >&2
            exit 1
            ;;
    esac
done

if [ -n "$SUBMODULE_PATH" ]; then
    SUB_ABS="$REPO_ROOT/$SUBMODULE_PATH"
    SUB_GITDIR="$(git -C "$SUB_ABS" rev-parse --absolute-git-dir 2>/dev/null || true)"
    if [ -z "$SUB_GITDIR" ]; then
        echo "ERROR: --submodule $SUBMODULE_PATH does not resolve to a git worktree under $REPO_ROOT" >&2
        exit 1
    fi
    HOOK_DEST="$SUB_GITDIR/hooks/pre-commit"
else
    HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"
fi

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
# NESTED-REPO NOTE (OA-w-2): when this wrapper is installed into a nested repo's OWN
# hooks dir (--submodule), owned-paths-check.sh itself is NOT present at that repo's
# own toplevel -- it lives only under the PARENT's .tools/git-hooks/. Resolve the
# superproject the same way owned-paths-check.sh resolves it for the LANE FILE (direct
# `--show-superproject-working-tree`, else the common gitdir'"'"'s core.worktree -- OA-e-11:
# never the first `git worktree list` entry, which for a submodule is its gitdir; a
# submodule with no resolvable superproject is REFUSED, never skipped), and fall back to this repo'"'"'s own toplevel (the
# parent-repo install, unchanged).
WRAPPER='#!/usr/bin/env bash
# owned-paths hook wrapper -- delegates to .tools/git-hooks/owned-paths-check.sh
# Windows Git Bash does not support true symlinks without Developer Mode.
# This wrapper ensures the hook always executes the current source version.
# ADHC_OWNPTH.003; nested-repo resolution OA-w-2 (2026-09-24)
_TOP="$(git rev-parse --show-toplevel 2>/dev/null)"
_SUPER="$(git rev-parse --show-superproject-working-tree 2>/dev/null)"
_IS_SUB=""
if [ -z "$_SUPER" ]; then
    # OA-e-11: resolve from the COMMON GITDIR of the committing worktree, never from the first
    # `git worktree list` entry (for a submodule that entry is its gitdir, which has no superproject).
    _GCD_RAW="$(git rev-parse --git-common-dir 2>/dev/null)"
    _GCD="$(cd "$_GCD_RAW" 2>/dev/null && pwd)"
    case "$_GCD" in
        */.git/modules/*|*/.git/worktrees/*/modules/*)
            _IS_SUB=1
            _CW="$(git config --file "$_GCD/config" core.worktree 2>/dev/null)"
            if [ -n "$_CW" ]; then
                _CWA="$(cd "$_GCD" 2>/dev/null && cd "$_CW" 2>/dev/null && pwd)"
                [ -n "$_CWA" ] && _SUPER="$(env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE -u GIT_COMMON_DIR git -C "$_CWA" rev-parse --show-superproject-working-tree 2>/dev/null)"
            fi
            ;;
    esac
    if [ -n "$_IS_SUB" ] && [ -z "$_SUPER" ]; then
        echo "ERROR: owned-paths: this repo is a submodule (common gitdir $_GCD) but its superproject could not be resolved -- refusing the commit (fail closed; the lane check is never skipped)." >&2
        exit 1
    fi
fi
HOOK="${_SUPER:-$_TOP}/.tools/git-hooks/owned-paths-check.sh"
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
