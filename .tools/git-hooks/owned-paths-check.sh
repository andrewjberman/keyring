#!/usr/bin/env bash
# ADHC_OWNPTH.002 -- Owned-paths commit-time lane enforcement hook.
#
# Reads GIT_AUTHOR_NAME from env, extracts agent serial, resolves staged
# files against .owned-paths.yaml, and flags lane violations.
#
# Phase logic (controlled by OWNED_PATHS_MODE env var):
#   warn  (default / Phase 1): violations printed to stderr + audit log; EXIT 0
#   block (Phase 2): violations EXIT 1
#
# Escape hatch: set GIT_COMMIT_AUTHOR_OVERRIDE=<LANE> to skip lane check
# for this commit (always logged as OVERRIDE).
#
# Test seam: set OWNED_PATHS_STAGED_FILES to a newline-separated file list
# to bypass "git diff --cached --name-only" (used in unit tests).
#
# Audit log: org/git-author-override-audit.log
#   Format: {ISO8601} {PASS|WARN|BLOCK|OVERRIDE}  {agent}  {N_files}  ({detail})

set -euo pipefail

# GIT-ENV-CLEAN CROSS-REPO CALL (OA-w-2): inside a pre-commit hook, git EXPORTS
# GIT_DIR/GIT_INDEX_FILE (and, for some invocations, GIT_WORK_TREE) pinned to the repo
# whose commit is in flight -- measured here for a nested (submodule) commit, where
# they point at the NESTED repo. Those env vars OUTRANK a bare `-C <other-repo>`: git
# resolves "the current repo" from GIT_DIR first and only falls back to `-C`/cwd
# discovery when it is unset, so `git -C "$SUPERPROJECT" rev-parse --git-common-dir`
# silently answers for the NESTED repo again, one directory too deep, unless these are
# cleared for that one call. Use `_git_x -C <dir> ...` for any query that must land on
# a DIFFERENT repo than the one whose hook is running.
_git_x() { env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE -u GIT_COMMON_DIR \
    -u GIT_OBJECT_DIRECTORY -u GIT_ALTERNATE_OBJECT_DIRECTORIES git "$@"; }

# precomp_v1 (RV0017-F002): orchestrator may pre-resolve REPO_ROOT via
# PRECOMP_REPO_ROOT to skip the redundant git rev-parse subprocess.
REPO_ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
YAML="$REPO_ROOT/.owned-paths.yaml"
VALIDATE="$REPO_ROOT/.tools/owned-paths-validate.py"

# ---------------------------------------------------------------------------
# NESTED-REPO GATE (OA-w-2, 2026-09-24): a commit made INSIDE a mapped submodule
# (opal_ai/**) has REPO_ROOT above pointed at the NESTED repo's own toplevel, which
# carries neither .owned-paths.yaml nor the validator -- in block mode (the default)
# that fails EVERY nested commit closed before any lane is ever consulted. A nested
# repo is graded against the PARENT's (superproject's) lane file instead, with staged
# paths re-based to PARENT-relative (opal_ai/<path>) so a worker's <paths> grant
# (written parent-relative) and the lane rows match on the same string. In the parent
# itself (no superproject) SUPERPROJECT resolves empty and this is a no-op.
# ---------------------------------------------------------------------------
NESTED_PREFIX=""
SUPERPROJECT="$(git rev-parse --show-superproject-working-tree 2>/dev/null || true)"
_NESTED_MAIN_WT=""
_IS_SUBMODULE=""
if [ -z "$SUPERPROJECT" ]; then
    # A LINKED WORKTREE of the nested repo (not its main/registered checkout) has no
    # superproject relationship of its OWN -- `--show-superproject-working-tree` only
    # answers for the repo's registered (main) worktree. OA-e-11 (row NFRA_OPALAI-Z-S17):
    # the superproject is resolved from the COMMON GITDIR of the committing worktree,
    # NEVER from the first `git worktree list` entry -- for a submodule that entry is
    # the GITDIR (<super>/.git/modules/<name>), which has no superproject, so a linked
    # worktree outside every parent worktree used to skip the lane check and land.
    # A submodule's common gitdir sits under .git/modules/ (or .git/worktrees/<wt>/modules/
    # when the parent itself is a linked worktree) and carries core.worktree = the nested
    # MAIN checkout; ask THAT checkout for the superproject.
    _GCD_RAW="$(git rev-parse --git-common-dir 2>/dev/null || true)"
    _GCD_ABS=""
    [ -n "$_GCD_RAW" ] && _GCD_ABS="$(cd "$_GCD_RAW" 2>/dev/null && pwd || true)"
    case "$_GCD_ABS" in
        */.git/modules/*|*/.git/worktrees/*/modules/*)
            _IS_SUBMODULE=1
            _CW="$(git config --file "$_GCD_ABS/config" core.worktree 2>/dev/null || true)"
            if [ -n "$_CW" ]; then
                _CW_ABS="$(cd "$_GCD_ABS" 2>/dev/null && cd "$_CW" 2>/dev/null && pwd || true)"
                if [ -n "$_CW_ABS" ]; then
                    SUPERPROJECT="$(_git_x -C "$_CW_ABS" rev-parse --show-superproject-working-tree 2>/dev/null || true)"
                    if [ -n "$SUPERPROJECT" ]; then
                        _NESTED_MAIN_WT="$(_git_x -C "$_CW_ABS" rev-parse --show-toplevel 2>/dev/null || true)"
                    fi
                fi
            fi
            ;;
    esac
fi
if [ -n "$SUPERPROJECT" ]; then
    _PREFIX_BASE="${_NESTED_MAIN_WT:-$REPO_ROOT}"
    NESTED_PREFIX="$(realpath --relative-to="$SUPERPROJECT" "$_PREFIX_BASE" 2>/dev/null || true)"
    case "$NESTED_PREFIX" in
        ""|.|..|../*) NESTED_PREFIX="" ;;  # could not place it under the superproject -- do not guess
    esac
    if [ -n "$NESTED_PREFIX" ]; then
        REPO_ROOT="$SUPERPROJECT"
        YAML="$REPO_ROOT/.owned-paths.yaml"
        VALIDATE="$REPO_ROOT/.tools/owned-paths-validate.py"
    fi
fi

# ONE LOG FOR EVERY WORKTREE (gap 4 of v3's first drain, 2026-09-04; 3.0.0_SA_CVO 94007, 4.0.0_SA_CRO 94014; placement
# 0.0.0_AB_MSTR 94049): the audit log is gitignored, so a LINKED worktree (a spine-v3 worker's) wrote its PASS/BLOCK/OVERRIDE
# rows into its own checkout's copy, which died with the worktree -- worker ~2's two OVERRIDE lines never reached the main
# tree. The log now resolves to the MAIN worktree root (the parent of `git rev-parse --git-common-dir`), same filename, so
# every reader keeps looking where it always did and every linked worktree writes the one log. In the main worktree the
# two roots coincide; a git that cannot answer falls back to REPO_ROOT (never to nowhere).
# `-C "$REPO_ROOT"` (not a bare cwd-scoped call): when the NESTED-REPO GATE above
# re-pointed REPO_ROOT at the superproject, the common-dir must be THAT repo's, not
# the nested repo's -- otherwise a nested commit's audit row would land in the wrong
# tree's log (or fail to land at all). `_git_x` (defined above): GIT_DIR is pinned to
# the nested repo in this process, which would otherwise silently out-rank `-C`.
_GCD="$(_git_x -C "$REPO_ROOT" rev-parse --git-common-dir 2>/dev/null || true)"
case "$_GCD" in
    "") MAIN_ROOT="$REPO_ROOT" ;;
    /*|[A-Za-z]:*) MAIN_ROOT="$(cd "$_GCD/.." 2>/dev/null && pwd || echo "$REPO_ROOT")" ;;
    *) MAIN_ROOT="$(cd "$REPO_ROOT/$_GCD/.." 2>/dev/null && pwd || echo "$REPO_ROOT")" ;;
esac
# Test seam: OWNED_PATHS_AUDIT_LOG lets unit tests redirect the audit log.
case "${AGENTBUS_DEVICE:-}" in ""|*[!a-z0-9-]*) GAO_REL="org/git-author-override-audit.log" ;; *) GAO_REL="org/git-author-override-audit.${AGENTBUS_DEVICE}.log" ;; esac  # one file per box (shape (a), MSTR consensus 2026-10-11); unset device -> legacy shared file
AUDIT_LOG="${OWNED_PATHS_AUDIT_LOG:-$MAIN_ROOT/$GAO_REL}"
MODE="${OWNED_PATHS_MODE:-block}"  # ADHC_OWNPTH.005 phase-2 flip 2026-04-30: was warn, flipped to block per Andrew directive
OVERRIDE="${GIT_COMMIT_AUTHOR_OVERRIDE:-}"

ISO_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
ACT_SUFFIX=" act=none paths=0:"  # GS-h-2: replaced by the real act key + full path list once the staged list is known

# ---------------------------------------------------------------------------
# Extract agent serial from GIT_AUTHOR_NAME (strip <email@...> suffix)
# ---------------------------------------------------------------------------
RAW_AUTHOR="${GIT_AUTHOR_NAME:-}"
AGENT="${RAW_AUTHOR%% <*}"

# ---------------------------------------------------------------------------
# MERGE EXEMPTION -- a merge does NOT author the files it carries.
# ---------------------------------------------------------------------------
# A merge commit legitimately spans every lane: it integrates origin's ALREADY-COMMITTED work
# by OTHER authors, each of which was lane-checked WHEN IT WAS FIRST COMMITTED. Re-checking
# those files against the INTEGRATOR's lane is a category error -- the integrator is not their
# author -- and it blocks every legitimate integration.
#
# WHY THIS IS A NARROW EXEMPTION AND NOT A HOLE: without it, integrators must `--no-verify`
# EVERY window merge, which bypasses NOT JUST THIS GATE BUT EVERY OTHER PRE-COMMIT GATE
# (surface-check, ledger-check, the never-rules gate). A GATE THAT BLOCKS A LEGITIMATE,
# UNAVOIDABLE, RECURRING OPERATION DOES NOT GET OBEYED -- IT GETS ROUTED AROUND, AND THE
# DETOUR IS WIDER THAN THE GATE. The absence of this narrow exemption forces a broad bypass.
#
# Non-merge commits are unaffected: this fires ONLY when MERGE_HEAD exists (a merge in
# progress) or HEAD already has 2+ parents. Found independently by 1.0.0_SA_CTO and
# 0.0.0_AB_MSTR (integrator, LD-0367) within one hour, both blocked on real merges.
# ⛔ MERGE_HEAD *ONLY*. Do NOT add "HEAD has two parents" as a second condition.
# In a PRE-COMMIT hook, HEAD is the PREVIOUS commit -- so a two-parent-HEAD test exempts the
# next ORDINARY commit after any merge, silently, for every agent. Caught by exercising this
# very hook while HEAD happened to be a merge: the broadened form reported the exemption as
# reachable and would have shipped a hole in an OWNERSHIP gate. MERGE_HEAD exists if and only
# if a merge is in progress and is the commit about to be created -- which is exactly the case
# being exempted, and nothing else.
# ⛔ AND DO NOT RE-ADD AN `OWNED_PATHS_STAGED_FILES` GUARD HERE. It was here, and IT KILLED THE
# EXEMPTION IN PRODUCTION: the active .git/hooks/pre-commit (precomp_v1) HOISTS the staged list and
# passes it to children via that env var, so in a REAL pre-commit run the var is ALWAYS SET, the
# `-z` test is FALSE, and the exemption NEVER FIRED. It fired only on the direct-invocation path --
# WHICH IS THE PATH I TESTED IT ON. My guard was written to keep the exemption out of the unit-test
# seam and turned out to BE the production condition, inverted. A MERGE IS A MERGE REGARDLESS OF
# HOW THE STAGED LIST WAS SOURCED. Found by 0.0.0_AB_MSTR on the exemption's FIRST REAL EXERCISE,
# window-3, who HELD the stuck merge rather than --no-verify-ing it. (The STAGED= logic below still
# honours both sources for the non-merge path; that is where the env var belongs.)
if git rev-parse -q --verify MERGE_HEAD >/dev/null 2>&1; then
    echo "${ISO_TS} PASS  ${AGENT:-UNKNOWN}  0  (MERGE COMMIT -- per-file lane check exempt; merged files were gated at their own authorship)${ACT_SUFFIX}" >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# Get staged files (real git or test seam)
# ---------------------------------------------------------------------------
if [ -n "${OWNED_PATHS_STAGED_FILES:-}" ]; then
    STAGED="$OWNED_PATHS_STAGED_FILES"
else
    STAGED="$(git diff --cached --name-only 2>/dev/null || true)"
fi

# NESTED-REPO GATE (cont'd): staged paths above are NESTED-repo-relative (e.g.
# "src/foo.py"); re-base to PARENT-relative (opal_ai/src/foo.py) before grading, so
# the resolved lane/worker-grant matches strings written parent-relative everywhere
# else in the estate.
if [ -n "$NESTED_PREFIX" ] && [ -n "$STAGED" ]; then
    STAGED="$(printf '%s\n' "$STAGED" | sed "s#^#${NESTED_PREFIX}/#")"
fi

# Edge case: no staged files
if [ -z "$STAGED" ]; then
    echo "${ISO_TS} PASS  ${AGENT:-UNKNOWN}  0  (no staged files)${ACT_SUFFIX}" >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# Bash-builtin file count (avoids printf | grep -c subprocess fan-out).
# Counts non-empty lines via positional-parameter expansion.
_OLDIFS="$IFS"
IFS=$'\n'
# shellcheck disable=SC2086
set -- $STAGED
N_FILES=$#
IFS="$_OLDIFS"
unset _OLDIFS

# GS-h-2: one act key (12 hex of sha256 over agent, newline, sorted staged paths) and the full sorted path list on every line logged.
_SORTED="$(printf '%s
' "$STAGED" | LC_ALL=C sort -u)"
ACT_KEY="$(printf '%s
%s' "${AGENT:-}" "$_SORTED" | sha256sum | cut -c1-12)"
ACT_PATHS="$(printf '%s' "$_SORTED" | tr '
' '|')"
ACT_SUFFIX=" act=${ACT_KEY} paths=$(printf '%s
' "$_SORTED" | grep -c .):${ACT_PATHS}"

# ---------------------------------------------------------------------------
# Override escape hatch
# ---------------------------------------------------------------------------
if [ -n "$OVERRIDE" ]; then
    echo "${ISO_TS} OVERRIDE  ${AGENT:-UNKNOWN}  ${N_FILES}  (--author-override ${OVERRIDE} applied)${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# FAIL CLOSED (OA-e-11): a commit in a SUBMODULE whose superproject did not resolve
# is refused in EVERY mode -- never a skipped lane check.
# ---------------------------------------------------------------------------
if [ -n "${_IS_SUBMODULE}${SUPERPROJECT}" ] && [ -z "$NESTED_PREFIX" ]; then
    echo "ERROR: owned-paths: this repo is a submodule (common gitdir ${_GCD_ABS:-unknown}) but its superproject could not be resolved -- refusing the commit (fail closed; the lane check is never skipped). Check core.worktree in the submodule's gitdir config." >&2
    echo "${ISO_TS} BLOCK  ${AGENT:-UNKNOWN}  ${N_FILES}  (submodule superproject unresolved -- fail closed)${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 1
fi

# ---------------------------------------------------------------------------
# Agent unknown
# ---------------------------------------------------------------------------
if [ -z "$AGENT" ]; then
    echo "WARN: GIT_AUTHOR_NAME not set -- skipping lane check" >&2
    echo "${ISO_TS} WARN  UNKNOWN  ${N_FILES}  (GIT_AUTHOR_NAME unset)${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# YAML not found
# ---------------------------------------------------------------------------
if [ ! -f "$YAML" ]; then
    echo "WARN: .owned-paths.yaml not found at $YAML -- skipping lane check" >&2
    if [ "$MODE" = "block" ]; then
        echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (YAML missing -- block mode EXIT 1)${ACT_SUFFIX}" \
            >> "$AUDIT_LOG" 2>/dev/null || true
        exit 1
    fi
    echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (YAML missing -- warn mode exit 0)${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# Resolve violations via Python validator
# ---------------------------------------------------------------------------
VIOLATIONS="$(printf '%s\n' "$STAGED" \
    | python3 "$VALIDATE" --check-agent "$AGENT" "$YAML" 2>&1 | tr -d '\r' || true)"
N_VIOLATIONS="$(printf '%s\n' "$VIOLATIONS" | grep -ac '^VIOLATION:' || true)"

if [ "$N_VIOLATIONS" -eq 0 ]; then
    echo "${ISO_TS} PASS  ${AGENT}  ${N_FILES}  (all paths in-lane)${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# Violations found — WARN or BLOCK based on MODE
# ---------------------------------------------------------------------------
FIRST3="$(printf '%s\n' "$VIOLATIONS" | grep -a '^VIOLATION:' | head -3 | tr '\n' '; ')"
DETAIL="${N_VIOLATIONS} violation(s): ${FIRST3}"

if [ "$MODE" = "block" ]; then
    echo "ERROR: owned-paths lane violation(s) detected (block mode):" >&2
    printf '%s\n' "$VIOLATIONS" | grep -a '^VIOLATION:' >&2
    echo "  hint: use .tools/safe-commit.sh -- <paths> to scope commit to declared pathspec" >&2
    echo "${ISO_TS} BLOCK  ${AGENT}  ${N_FILES}  (${DETAIL})${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 1
else
    echo "WARN: owned-paths lane violation(s) detected (warn mode -- commit proceeds):" >&2
    printf '%s\n' "$VIOLATIONS" | grep -a '^VIOLATION:' >&2
    echo "  hint: use .tools/safe-commit.sh -- <paths> to scope commit to declared pathspec" >&2
    echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (${DETAIL})${ACT_SUFFIX}" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi
