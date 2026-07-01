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

# MSYS-PATH GOTCHA (run-1 bug, MSTR 150812Z): native-Windows python CANNOT resolve an MSYS `/c/...`
# path -- neither for sys.path import NOR os.path.abspath (it mangles `/c/...` to `C:\c\...`). So do
# NOT pass `$CP`/`$OUTDIR` (MSYS form) straight into python. Fix: run python FROM $CP (cwd resolves
# `import harness` + a relative --out) and pass any absolute path to python in WINDOWS form (cygpath -w).
# Lesson banked: a module self-test passing does NOT prove the LAUNCHER works on the real cross-tooling
# (MSYS bash -> native python) invocation -- exactly the success-shaped-but-wrong class B studies.
OUTDIR_WIN="$(cygpath -w "$OUTDIR")"

# 1. emit the answer-free payload (render_solver_prompt is fail-closed on any strip leak). From $CP so
#    'corpus_loader.py' + the relative --out resolve without MSYS-path translation.
( cd "$CP" && python corpus_loader.py --emit-case "$CASE" --out "solver_view_${CASE}.txt" )

# 2. NEVER#4 pre-flight: the launch cwd must inject NO fabric narrative (CLAUDE.md states corpus
#    root-causes verbatim). Run python FROM $CP ('import harness' via cwd) + pass OUTDIR in Windows
#    form. Fail-closed (set -e + exit 3) -- abort the spawn if the cwd is context-contaminated.
( cd "$CP" && python -c "import harness; \
r=harness.assert_clean_context(r'''$OUTDIR_WIN'''); print('clean_context:', r['clean'], r['leaks']); \
import sys; sys.exit(0 if r['clean'] else 3)" )

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
