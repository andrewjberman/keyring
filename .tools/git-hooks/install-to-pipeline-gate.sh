#!/usr/bin/env bash
# install-to-pipeline-gate.sh -- Idempotent: appends the DIRECTIVE EXECUTION PIPELINE gate
# (layers 1B / 2-complement / 3) to .git/hooks/pre-commit, precomp_v1 orchestrator pattern.
#
# Authority: Andrew-direct 2026-09-01 at the 3.0.0_SA_CVO terminal -- "re-authorize the three
# enforcement layers and add the stage-3 preflight" / "we need these set up in a manner that
# they are actually mandated".
#
# WHY THIS EXISTS SEPARATELY FROM safe-commit.sh: the gate is already wired in safe-commit.sh,
# which is REPO-TRACKED and therefore travels to every clone. But a raw `git commit` bypasses
# safe-commit entirely. .git/hooks/ is per-clone and untracked, so the hook path needs an
# installer to be reproducible. Wiring BOTH closes the asymmetry: safe-commit carries it across
# clones, the hook carries it across invocation styles. Named as a limb in d19c0add42 and closed
# here rather than left as a known hole.
#
# Modelled on install-to-proof-of-spec.sh, which wires the sibling <decomp_ref> lint the same way.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
MARKER="to-pipeline-gate.py"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK does not exist -- run the precomp_v1 orchestrator installer first." >&2
    exit 1
fi

if grep -q "$MARKER" "$HOOK" 2>/dev/null; then
    echo "OK: already installed ($MARKER present in pre-commit) -- idempotent no-op."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 9. DIRECTIVE EXECUTION PIPELINE gate (Andrew-direct 2026-09-01 re-authorization) ----------
# Layer 3: a NEW TO's project must exist and declare a dep_stage from the ratified enum.
# Stage-3 preflight: a NEW TO must carry <preflight> with comp-schedule / comp-iam /
#   comp-adversary each RUN or DECLARED-NOT-APPLICABLE with a reason.
# Layer 1B: a TO flipping to a terminal <status> on a pipeline-registered project must have a
#   VALID proof-of-spec instance.
# The sibling stage 8 above owns the <decomp_ref> presence check; this one does not duplicate it.
# FAIL-CLOSED on the sentinel: a staged task_orders file with the checker missing = DENY.
if [ -f "$ROOT/.tools/to-pipeline-gate.py" ]; then
    ROOT="$ROOT" STAGED="$STAGED" python "$ROOT/.tools/to-pipeline-gate.py" || exit 1
elif git diff --cached --name-only 2>/dev/null | grep -qE '(^|/)task[_-]orders/[^/]+\.md$'; then
    echo "BLOCKED: a task_orders file is staged but .tools/to-pipeline-gate.py is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: appended the pipeline gate stage to $HOOK"
echo "     verify: grep -n '$MARKER' .git/hooks/pre-commit"
