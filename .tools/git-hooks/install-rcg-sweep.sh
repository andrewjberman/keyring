#!/usr/bin/env bash
# =============================================================================
# install-rcg-sweep.sh -- Idempotent wiring of the RCG sweep gate (ruling
# CTOB-RCG-001) into .git/hooks/pre-commit as stage 6.
#
# Usage: bash .tools/git-hooks/install-rcg-sweep.sh
#
# ORDERING MATTERS AND IS THE POINT: this gate is what makes the sweep identity's
# broad delete lane safe. A clone that has the LANE GRANT but not this GATE is the
# one genuinely unsafe configuration in the whole design (ruling s.9 residual 3).
# Until the estate has a single install-all entry point -- still the real, named,
# unbuilt item at .owned-paths.yaml:114 -- running this installer and OBSERVING its
# output is a recorded per-batch prep step, not a one-time setup assumption, and
# batches execute on the primary laptop only.
#
# Exit codes: 0 = wired or already wired | 1 = gate script missing / no pre-commit hook
# Author: 1.0.0_SA_CTO~B, 2026-08-04.
# =============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GATE_SRC="$REPO_ROOT/.tools/git-hooks/rcg-sweep-check.sh"
ENGINE="$REPO_ROOT/.tools/rcg_sweep_verify.py"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"

for f in "$GATE_SRC" "$ENGINE"; do
    if [ ! -f "$f" ]; then
        echo "ERROR: $f not found -- refusing to wire a gate whose own parts are missing." >&2
        exit 1
    fi
done

if [ -f "$HOOK_DEST" ] && grep -q "rcg-sweep-check.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: rcg-sweep gate already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

if [ ! -f "$HOOK_DEST" ]; then
    echo "ERROR: no pre-commit hook at $HOOK_DEST." >&2
    echo "       Run 'bash .tools/git-hooks/install-owned-paths.sh' first; this gate" >&2
    echo "       EXTENDS the composed hook rather than replacing it." >&2
    exit 1
fi

cat >> "$HOOK_DEST" <<'STAGE'

# ---------- 6. RCG sweep gate (ruling CTOB-RCG-001) ----------
# Fires on the sweep-executor AUTHOR IDENTITY -- not on a trailer -- so that
# identity has no un-gated commit shape. Silent no-op for every other author.
# FAIL-CLOSED: a missing gate script while that identity commits is a DENY.
# Wired by .tools/git-hooks/install-rcg-sweep.sh.
if [ -f "$ROOT/.tools/git-hooks/rcg-sweep-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/rcg-sweep-check.sh" "$@" || exit 1
elif [ "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" = "${RCG_SWEEP_IDENTITY:-4.0.0_SA_CRO~SWEEP}" ]; then
    echo "BLOCKED: sweep identity is committing but .tools/git-hooks/rcg-sweep-check.sh is missing." >&2
    exit 1
fi
STAGE

chmod +x "$HOOK_DEST"
echo "OK: rcg-sweep gate wired into $HOOK_DEST (stage 6)"
