#!/usr/bin/env bash
# install-missions-tree-check.sh -- Idempotent: appends the PROJECT TREE validator stage to
# .git/hooks/pre-commit (per-clone, untracked, hence an installer), fail-closed on the sentinel
# like the rcg stage. Andrew-direct 2026-09-02 ~23:5xZ (R-i approved, "before L3's commit").
# Modelled on install-to-pipeline-gate.sh / install-rcg-manifest.sh.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
MARKER="missions-tree-check.sh"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK does not exist -- run the precomp_v1 orchestrator installer first." >&2
    exit 1
fi
if grep -q "$MARKER" "$HOOK" 2>/dev/null; then
    echo "OK: already installed ($MARKER present in pre-commit) -- idempotent no-op."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 10. PROJECT TREE validator (CVO residual R-i; Andrew-direct 2026-09-02 ~23:5xZ) ----------
# Scoped: no-ops unless the staged set touches org/missions/D<n>/** or org/projects/*.json.
# Runs .tools/missions-tree-index.py check (2.0.0_SA_COO's generator) and DENIES on rc 1 (the
# contract's refusals R1-R5 / ROW-* / INDEX-*) or rc 2 (could not run). FAIL-CLOSED on the
# sentinel. Wired by .tools/git-hooks/install-missions-tree-check.sh.
if [ -f "$ROOT/.tools/git-hooks/missions-tree-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/missions-tree-check.sh" "$@" || exit 1
elif printf '%s\n' "$STAGED" | grep -qE '^org/missions/D(0|[1-9][0-9]?)/|^org/projects/[^/]+\.json$'; then
    echo "BLOCKED: a tree/register path is staged but .tools/git-hooks/missions-tree-check.sh is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: appended the project-tree validator stage to $HOOK"
echo "     verify: grep -n '$MARKER' .git/hooks/pre-commit"
