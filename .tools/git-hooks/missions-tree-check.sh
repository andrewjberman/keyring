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
# READS THE STAGED BYTES, SCOPED TO THE ACT (NFRA_GATSCP GS-t-2): the run is `check --staged --act-from-env`.
# --staged reads every input from the git index git resolves (GIT_INDEX_FILE / GIT_DIR honoured), never the
# working tree, so a file staged differently from its working copy is graded as staged and another seat's
# unsaved edit is not graded inside this commit. --act scopes the refusal: a violation in a project the staged
# list does not touch is printed as `STANDING <CODE> ...` and does not refuse; a violation in a project the list
# touches refuses as before. A staged DIRECTIVES.yaml / MACROS.yaml / contract puts every project in the act.
# No rule (R1-R6, ROW-*, INDEX-*) changed. Without OWNED_PATHS_STAGED_FILES the act also carries the staged
# DELETIONS, so removing a tree row cannot leave its orphaned index entry as someone else's STANDING.
#
# rc: 0 = clean or not-applicable | 1 = DENY (violations, or the gate could not evaluate itself).
# Rule 16: Git Bash default utilities only. ASCII only.
#
# Author: 1.0.0_SA_CTO, 2026-09-02.
# =============================================================================
set -e

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
case "${AGENTBUS_DEVICE:-}" in ""|*[!a-z0-9-]*) GAO_REL="org/git-author-override-audit.log" ;; *) GAO_REL="org/git-author-override-audit.${AGENTBUS_DEVICE}.log" ;; esac  # one file per box (shape (a), MSTR consensus 2026-10-11); unset device -> legacy shared file
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
ACT_LIST="$STAGED"
if [ -z "${OWNED_PATHS_STAGED_FILES:-}" ]; then
    ACT_LIST="$ACT_LIST
$(git -C "$ROOT" diff --cached --name-only --diff-filter=D 2>/dev/null || true)"
fi
OUT="$(cd "$ROOT" && MTC_ACT_PATHS="$ACT_LIST" python "$TOOL" check --staged --act-from-env MTC_ACT_PATHS 2>&1)" || RC=$?

# NFRA_CTLPLN CT-s-8 -- a round is not counted finished without a reviewer on the box and a grade by it. When a staged
# org/missions/D*/*/<CODE>/project.json moves dep_stage TO ROUND_CLOSE or CLOSED, .tools/round-close-check.py runs for that
# project; verdict=REFUSED is printed (WARN, the default: the commit goes on) or refuses (ENFORCE, only while
# org/mcp/seat-gates.round-close.missions-tree-check.enforce exists; OPAL_SEAT_GATES_ENFORCE_DIR points a test at another
# directory, as in safe-apply.sh; the retired org/mcp/seat-gates.enforce turns on nothing; nothing here creates a switch).
# Audited override: SEAT_GATES_OVERRIDE="reason" (org/git-author-override-audit.log). Any other dep_stage change, and any
# commit that stages no project.json, never reaches it. Returns 1 only to refuse the commit.
close_gate() {
    local p old new code out rc last mode enf worst=0 pj sgd n rargs
    sgd="${OPAL_SEAT_GATES_ENFORCE_DIR:-$ROOT/org/mcp}"
    enf="$sgd/seat-gates.round-close.missions-tree-check.enforce"
    mode=WARN; [ -e "$enf" ] && mode=ENFORCE
    pj="$(printf '%s\n' "$HITS" | grep -E '^org/missions/D(0|[1-9][0-9]?)/[^/]+/[^/]+/project\.json$' || true)"
    [ -n "$pj" ] || return 0
    [ -e "$sgd/seat-gates.enforce" ] && echo "WARN: missions-tree-check close-gate -- org/mcp/seat-gates.enforce is retired and turns on nothing; the close gate's switch is org/mcp/seat-gates.round-close.missions-tree-check.enforce." >&2
    while IFS= read -r p; do
        [ -n "$p" ] || continue
        new="$(MSYS_NO_PATHCONV=1 git -C "$ROOT" show ":$p" | tr -d '\r' | sed -n 's/.*"dep_stage"[[:space:]]*:[[:space:]]*"\([A-Z_]*\)".*/\1/p' | head -1)" || new=""
        [ -n "$new" ] || { echo "WARN: missions-tree-check close-gate -- the staged $p carries no readable dep_stage; not read as a ROUND_CLOSE move." >&2; continue; }
        case "$new" in ROUND_CLOSE|CLOSED) ;; *) continue ;; esac
        old=""
        if git -C "$ROOT" cat-file -e "HEAD:$p" 2>/dev/null; then
            old="$(MSYS_NO_PATHCONV=1 git -C "$ROOT" show "HEAD:$p" | tr -d '\r' | sed -n 's/.*"dep_stage"[[:space:]]*:[[:space:]]*"\([A-Z_]*\)".*/\1/p' | head -1)" || old=""
        fi
        [ "$old" != "$new" ] || continue
        code="$(basename "$(dirname "$p")")"
        rc=0
        n="$(git -C "$ROOT" grep --cached -h -o -E '<round>[0-9]+</round>' -- "$(dirname "$p")/task-orders/" 2>/dev/null | tr -d '' | sed 's/[^0-9]//g' | sort -n | tail -1)" || n=""
        rargs=()
        if [ -n "$n" ]; then rargs=(--round "$n"); else echo "WARN: missions-tree-check close-gate -- $code: no <round> in the staged task orders; grading all rounds." >&2; fi
        out="$(cd "$ROOT" && python .tools/round-close-check.py --project "$code" "${rargs[@]}" --staged 2>&1)" || rc=$?
        last="$(printf '%s\n' "$out" | tr -d '\r' | tail -1)"
        case "$last" in
            ROUND-CLOSE\ *"verdict=MAY-CLOSE")
                echo "OK: missions-tree-check close-gate -- $code dep_stage $old -> $new: $last" ;;
            ROUND-CLOSE\ *"verdict=REFUSED")
                printf '%s\n' "$out" | sed 's/^/  | /' >&2
                if [ "$mode" = ENFORCE ]; then
                    if [ -n "${SEAT_GATES_OVERRIDE:-}" ]; then
                        printf '%s SEAT_GATES_OVERRIDE actor=%s missions-tree-check close-gate project=%s reason=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
                            "${OPAL_AGENT_SERIAL:-UNKNOWN}" "$code" "$SEAT_GATES_OVERRIDE" >> "$ROOT/$GAO_REL"
                        echo "WARN: missions-tree-check close-gate OVERRIDDEN (audited): $SEAT_GATES_OVERRIDE -- $last" >&2
                    else
                        echo "BLOCKED: missions-tree-check close-gate -- $code dep_stage $old -> $new REFUSED (ENFORCE, org/mcp/seat-gates.round-close.missions-tree-check.enforce present): $last" >&2
                        echo "  remedy: a CVO-kind reviewer live on the box and a CVO row grading every judgment criterion; override: SEAT_GATES_OVERRIDE=\"reason\"." >&2
                        worst=1
                    fi
                else
                    echo "WARN: missions-tree-check close-gate -- $code dep_stage $old -> $new would be REFUSED under ENFORCE; WARN mode admits it: $last" >&2
                fi ;;
            *)
                if [ "$mode" = ENFORCE ] && [ -z "${SEAT_GATES_OVERRIDE:-}" ]; then
                    echo "BLOCKED: missions-tree-check close-gate -- round-close-check.py gave no verdict for $code (rc=$rc); refusing rather than passing a close it did not grade (ENFORCE)." >&2
                    printf '%s\n' "$out" | tail -5 >&2
                    worst=1
                else
                    echo "WARN: missions-tree-check close-gate -- round-close-check.py gave no verdict for $code (rc=$rc); the close goes on (WARN)." >&2
                fi ;;
        esac
    done <<EOF
$pj
EOF
    return "$worst"
}

case "$RC" in
    0)
        printf '%s
' "$OUT" | grep -E '^STANDING ' || true
        close_gate || exit 1
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
