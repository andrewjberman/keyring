#!/usr/bin/env bash
# =============================================================================
# install-rcg-manifest.sh -- Idempotent wiring of the rcg/ folder-contract gate
# into .git/hooks/pre-commit.
#
# Usage: bash .tools/git-hooks/install-rcg-manifest.sh
#
# NFRA_REPOCOHERENCEGRAPH D-0001 item 3 (1.0.0_SA_CTO~B, R-0021/D-0004).
#
# WHY AN INSTALLER AND NOT A HAND-EDIT: .git/hooks/ is NOT tracked by git. A hand
# edit to .git/hooks/pre-commit protects exactly one clone on one machine and is
# invisible to review, to a fresh checkout, and to site Z. This repo has already
# paid for that exact shape -- CLAUDE.md's own note that .tools/aws.cmd "were
# invisible to git, which is how an unreviewable file broke every aws call in the
# fabric", and the 2026-07-29 forwarder collapse where a non-durable fix silently
# propagated its expiry into durable artifacts. The tracked installer is the
# durable half; running it is the local half. Follows the established sibling
# pattern (install-owned-paths.sh, install-mass-deletion-check.sh, ...).
#
# NOTE ON THE STILL-OPEN GAP THIS DOES NOT CLOSE: there is no single entry point
# that installs all hooks (a named, unbuilt item recorded in .owned-paths.yaml:114
# -- "The install-all entry point remains a real, named, unbuilt item (CTO to
# route)"). This adds a NINTH installer to that set rather than fixing it. That is
# deliberate scope discipline, not an oversight; it is surfaced, not silently
# inherited.
#
# Exit codes:
#   0 = wired, or already wired (idempotent no-op)
#   1 = the gate script is missing, or no pre-commit hook exists to extend
#
# Author: 1.0.0_SA_CTO~B, 2026-08-04.
# =============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GATE_SRC="$REPO_ROOT/.tools/git-hooks/rcg-manifest-check.sh"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"

if [ ! -f "$GATE_SRC" ]; then
    echo "ERROR: $GATE_SRC not found -- nothing to wire." >&2
    exit 1
fi

if [ -f "$HOOK_DEST" ] && grep -q "rcg-manifest-check.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: rcg-manifest gate already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

if [ ! -f "$HOOK_DEST" ]; then
    echo "ERROR: no pre-commit hook at $HOOK_DEST." >&2
    echo "       Run 'bash .tools/git-hooks/install-owned-paths.sh' first -- this gate" >&2
    echo "       EXTENDS the composed hook rather than replacing it, so that a partial" >&2
    echo "       install can never silently drop the owned-paths or ledger stages." >&2
    exit 1
fi

# Append as a new stage. The parent hook runs `set -e`, so a non-zero rc here
# aborts the commit; the explicit `|| exit 1` states that intent rather than
# leaving it to inherited shell semantics.
cat >> "$HOOK_DEST" <<'STAGE'

# ---------- 5. rcg/ folder-contract gate (NFRA_REPOCOHERENCEGRAPH PRD s.12) ----------
# Scoped: no-ops unless the staged set touches rcg/. FAIL-CLOSED when it does --
# unlike stages 2-4, a missing gate script here is a DENY, not a silent skip.
# Wired by .tools/git-hooks/install-rcg-manifest.sh (D-0001 item 3, R-0021).
if [ -f "$ROOT/.tools/git-hooks/rcg-manifest-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/rcg-manifest-check.sh" "$@" || exit 1
elif printf '%s\n' "$STAGED" | grep -q '^rcg/'; then
    echo "BLOCKED: rcg/ staged but .tools/git-hooks/rcg-manifest-check.sh is missing." >&2
    exit 1
fi
STAGE

chmod +x "$HOOK_DEST"
echo "OK: rcg-manifest gate wired into $HOOK_DEST (stage 5)"
