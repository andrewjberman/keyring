#!/usr/bin/env bash
# =============================================================================
# missions-tree-check.sh -- pre-commit wiring for the PROJECT TREE's own validator.
#
# CVO review residual R-i (CVO_REVIEW_TREE_PREREQ_SET_20260902.md @580c4f72a2): the generator's
# `check` (.tools/missions-tree-index.py, 2.0.0_SA_COO) refuses the states the contract names
# (R1-R5, ROW-*, INDEX-*) -- and, measured, NO commit ran it (0 of 56 commit-time files). A refusal
# nobody invokes is a description. Andrew-direct 2026-09-02 ~23:5xZ at the 1.0.0_SA_CTO terminal,
# verbatim "rec approved: [... wired into the commit gate as a refusal for staged tree/register
# paths ... before L3's commit, so the registration is the first commit the tree validates
# mechanically]". Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/
# ANDREW_DIRECT_20260902_235xZ_R_I_CHECK_INTO_COMMIT_GATE_BEFORE_L3.md.
#
# SCOPED: fires only when the staged set touches org/missions/D<n>/** (a tree folder: the
# directive-level regex of org/standards/PROJECT_TREE.contract.json is ^D(0|[1-9][0-9]?)$) or
# org/projects/*.json (the flat index, which the tree generates into). Everything else prints one
# SKIP line and runs nothing -- the generator reads 350+ rows, and running it on every commit by
# every seat would tax the fabric for two folders.
#
# FAIL-CLOSED, like rcg-manifest-check.sh and unlike the `if [ -f ]` siblings: when a tree/register
# path is staged and the generator is missing or cannot run (its rc 2), that is a DENY. A gate that
# vanishes silently reads exactly like its approval.
#
# BOUND, stated: `check` reads the WORKTREE, not the staged index. A file staged differently from
# its worktree copy is validated as the worktree has it. The step-6 gate's limb 5 reads the staged
# index for the same reason this one does not yet: the generator has no --staged mode. Named here
# so it is a known hole, not a discovered one.
#
# rc: 0 = clean or not-applicable | 1 = DENY (violations, or the gate could not evaluate itself).
# Rule 16: Git Bash default utilities only. ASCII only.
#
# Author: 1.0.0_SA_CTO, 2026-09-02.
# =============================================================================
set -e

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$ROOT" ] || exit 0

STAGED="${OWNED_PATHS_STAGED_FILES:-}"
if [ -z "$STAGED" ]; then
    STAGED="$(git -C "$ROOT" diff --cached --name-only --diff-filter=d 2>/dev/null || true)"
fi

# The trigger population: a tree folder or the flat index.
HITS="$(printf '%s\n' "$STAGED" | grep -E '^org/missions/D(0|[1-9][0-9]?)/|^org/projects/[^/]+\.json$' || true)"
if [ -z "$HITS" ]; then
    echo "SKIP: missions-tree-check -- no org/missions/D*/ or org/projects/*.json path staged; check not run"
    exit 0
fi

TOOL="$ROOT/.tools/missions-tree-index.py"
if [ ! -f "$TOOL" ]; then
    echo "BLOCKED: missions-tree-check -- $(printf '%s\n' "$HITS" | grep -c .) tree/register path(s) staged but $TOOL is missing (fail-closed)." >&2
    exit 1
fi

# The generator's rc is CAPTURED, never let loose: under `set -e` a plain OUT="$(cmd)" whose cmd
# returns 1 kills this script at the assignment, BEFORE the case below prints anything -- the first
# cut of this hook refused the planted mutant with rc 1 and NO TEXT (measured 2026-09-02 23:5xZ,
# direct hook run: last line was the surprise-row gate's OK). A silent refusal reads like a broken
# hook, and a silent pass would read like approval; neither is a gate.
RC=0
OUT="$(cd "$ROOT" && python "$TOOL" check 2>&1)" || RC=$?
case "$RC" in
    0)
        echo "OK: missions-tree-check -- $(printf '%s\n' "$HITS" | grep -c .) tree/register path(s) staged; $(printf '%s\n' "$OUT" | grep -E '^RESULT' | head -1)"
        exit 0 ;;
    1)
        echo "BLOCKED: missions-tree-check -- the project tree's validator REFUSES this commit (staged: $(printf '%s\n' "$HITS" | tr '\n' ' '))" >&2
        printf '%s\n' "$OUT" | grep -v '^  value enum' >&2
        echo "  remedy: fix the state the violation names (R5 = the register's members list, 0.0.0_AB_MSTR's lane); never bypass." >&2
        exit 1 ;;
    *)
        echo "BLOCKED: missions-tree-check -- the validator could not run (rc=$RC); refusing rather than passing a commit it did not grade." >&2
        printf '%s\n' "$OUT" | tail -5 >&2
        exit 1 ;;
esac
