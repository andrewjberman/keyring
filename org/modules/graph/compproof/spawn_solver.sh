#!/usr/bin/env bash
# NFRA_COMPPROOF B -- REFERENCE sanitized blind-solver launch (Vector-1 clean-room close).
# MSTR owns + finalizes the exact `claude -p` spawn flags for its tooling; this script is the
# AUTHORITATIVE recipe for the structure: (1) emit the diff-gate-verified answer-free payload,
# (2) prepare a sanitized cwd OUTSIDE the workspace tree, (3) NEVER#4 pre-flight assert_clean_context,
# (4) bare-launch skeleton + tool-log capture. Git Bash 3.6.7 default utils only (Rule 16 -- no
# pgrep/pkill/flock/setsid). See AFFORDANCE_SPEC.md for the full mechanism.
set -eu

WS="/c/Users/AndrewBerman/Desktop/ajb_workspace"
CP="$WS/org/modules/graph/compproof"
CASE="${1:?usage: spawn_solver.sh <case_id e.g. B-01> [sanitized_cwd]}"
PAYLOAD="$CP/solver_view_${CASE}.txt"
# sanitized cwd OUTSIDE the ws tree (so claude finds NO CLAUDE.md/memory/org-XXX up-tree)
OUTDIR="${2:-$(mktemp -d -t "compproof_${CASE}_XXXXXX")}"

# 1. emit the answer-free payload (render_solver_prompt is fail-closed on any strip leak)
python "$CP/corpus_loader.py" --emit-case "$CASE" --out "$PAYLOAD"

# 2. NEVER#4 pre-flight: the launch cwd must inject NO fabric narrative (CLAUDE.md states corpus
#    root-causes verbatim). Fail-closed -- abort the spawn if the cwd is context-contaminated.
python -c "import sys; sys.path.insert(0,'$CP'); import harness; \
r=harness.assert_clean_context('$OUTDIR'); print('clean_context:', r['clean'], r['leaks']); \
sys.exit(0 if r['clean'] else 3)"

# 3. LAUNCH (MSTR finalizes the flags): bare 'claude -p' from the sanitized cwd -- memory auto-recall
#    OFF, no org/XXX.md fabric startup, no fabric-lane spawn wrapper. Full SUBSTRATE file-access is
#    RETAINED (absolute paths + comp-tools on PATH); only the auto-injected CONTEXT is suppressed.
#    Capture the ACTUAL tool-log (every Read/Grep/comp-tool call) -- that is what the B2 judge audits.
#    Skeleton (adapt to the spawn tooling):
#      ( cd "$OUTDIR" && claude -p "$(cat "$PAYLOAD")" \
#          --output-format stream-json > "$OUTDIR/run.jsonl" 2> "$OUTDIR/err.log" )
#      # then extract tool-calls -> solver_results["'"$CASE"'"] = {concluded_root_cause, traversal_path,
#      #   tool_log, confidence}  (tool_log is authoritative for harness.cheat_check)

echo "PREPARED: case=$CASE"
echo "  payload=$PAYLOAD (diff-gate-verified answer-free)"
echo "  sanitized_cwd=$OUTDIR (clean-context verified)"
echo "NEXT (MSTR): bare-launch claude -p from the sanitized cwd; capture tool_log; drop solver_results[$CASE]."
