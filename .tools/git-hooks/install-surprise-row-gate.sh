#!/usr/bin/env bash
# install-surprise-row-gate.sh -- Idempotent: appends the SURPRISE-CHANNEL ROW GATE (steps 7 + 10)
# to .git/hooks/pre-commit, precomp_v1 orchestrator pattern.
#
# Authority: Andrew-direct 2026-09-01, /open-calls card 2 of 9 -> "All recs approved", then
# "build the row validators".
#
# WHY THIS EXISTS SEPARATELY FROM safe-commit.sh: the gate is already wired in safe-commit.sh,
# which is REPO-TRACKED and travels to every clone. A raw `git commit` bypasses safe-commit
# entirely. .git/hooks/ is per-clone and untracked, so the hook path needs an installer to be
# reproducible. Wiring BOTH closes the asymmetry -- safe-commit carries it across clones, the
# hook carries it across invocation styles.
#
# Modelled on install-to-pipeline-gate.sh, which wires the sibling TO gate the same way.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
MARKER="surprise-row-gate.py"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK does not exist -- run the precomp_v1 orchestrator installer first." >&2
    exit 1
fi

if grep -q "$MARKER" "$HOOK" 2>/dev/null; then
    echo "OK: already installed ($MARKER present in pre-commit) -- idempotent no-op."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 10. SURPRISE-CHANNEL ROW GATE (steps 7 + 10; Andrew-direct 2026-09-01) ----------
# A NEW investigation row must carry the step-7 trigger's BOTH halves (spec_asserts + world_is).
# A NEW remediation row must carry route + loop_target satisfying the LOCKED MAPPING
#   SPEC_ERROR->6 | DECOMP_INVALIDATING->5 | SCOPE_CHANGE->2.
# PROSPECTIVE: diffs row IDs HEAD-vs-staged and grades only ids NEW in this commit, so the ~190
# legacy rows across 18 files are never re-graded.
# FAIL-CLOSED on the sentinel: a staged channel file with the checker missing = DENY.
if [ -f "$ROOT/.tools/surprise-row-gate.py" ]; then
    ROOT="$ROOT" STAGED="$STAGED" python "$ROOT/.tools/surprise-row-gate.py" || exit 1
elif git diff --cached --name-only 2>/dev/null | grep -qE '(org/surprise_channel/[^/]+|/surprise-channel/(investigations|adjudications|remediations))/(INVESTIGATION|ADJUDICATION|REMEDIATION)_v'; then
    echo "BLOCKED: a surprise-channel row file is staged but .tools/surprise-row-gate.py is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: appended the surprise-row gate stage to $HOOK"
echo "     verify: grep -n '$MARKER' .git/hooks/pre-commit"
