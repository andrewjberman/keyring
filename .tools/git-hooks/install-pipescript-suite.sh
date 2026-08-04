#!/usr/bin/env bash
# =============================================================================
# install-pipescript-suite.sh -- Idempotent wiring of the comp-pipescript suite
# gate (dial F9) into .git/hooks/pre-commit as stage 7.
#
# Usage: bash .tools/git-hooks/install-pipescript-suite.sh
#
# Mirrors install-rcg-sweep.sh: EXTENDS the composed pre-commit hook (never
# replaces it, never a standalone hook racing the chain -- TO scope 3). The
# stanza's missing-script backstop keys on ONE sentinel path; the canonical
# watch list lives ONLY in pipescript-suite-check.sh (single derivation point).
#
# Exit codes: 0 = wired or already wired | 1 = gate script missing / no pre-commit hook
# TO: ADHOC.comp-pipescript-suite-commit-gate-f9. Author: 0.8.0_AE_CloudComp~D, 2026-08-04.
# =============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GATE_SRC="$REPO_ROOT/.tools/git-hooks/pipescript-suite-check.sh"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"

if [ ! -f "$GATE_SRC" ]; then
    echo "ERROR: $GATE_SRC not found -- refusing to wire a gate whose own parts are missing." >&2
    exit 1
fi

if [ -f "$HOOK_DEST" ] && grep -q "pipescript-suite-check.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: pipescript-suite gate already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

if [ ! -f "$HOOK_DEST" ]; then
    echo "ERROR: no pre-commit hook at $HOOK_DEST." >&2
    echo "       Run 'bash .tools/git-hooks/install-owned-paths.sh' first; this gate" >&2
    echo "       EXTENDS the composed hook rather than replacing it." >&2
    exit 1
fi

cat >> "$HOOK_DEST" <<'STAGE'

# ---------- 7. comp-pipescript suite gate (dial F9, TO ADHOC.comp-pipescript-suite-commit-gate-f9) ----------
# Scoped-stage: no-ops unless a staged path can break the comp-pipescript
# suite. The watch list lives in pipescript-suite-check.sh (SINGLE derivation
# point); the elif sentinel below is ONE load-bearing member used only as the
# missing-script backstop, NOT a copy of the list.
# FAIL-CLOSED on the sentinel: engine staged while the gate script is missing = DENY.
# Wired by .tools/git-hooks/install-pipescript-suite.sh.
if [ -f "$ROOT/.tools/git-hooks/pipescript-suite-check.sh" ]; then
    PIPESCRIPT_SUITE_STAGED_FILES="$STAGED" bash "$ROOT/.tools/git-hooks/pipescript-suite-check.sh" "$@" || exit 1
elif printf '%s\n' "$STAGED" | grep -q '^org/modules/graph/pipeline_cli\.py$'; then
    echo "BLOCKED: org/modules/graph/pipeline_cli.py staged but .tools/git-hooks/pipescript-suite-check.sh is missing." >&2
    exit 1
fi
STAGE

chmod +x "$HOOK_DEST"
echo "OK: pipescript-suite gate wired into $HOOK_DEST (stage 7)"
