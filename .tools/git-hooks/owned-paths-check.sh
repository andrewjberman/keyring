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

# precomp_v1 (RV0017-F002): orchestrator may pre-resolve REPO_ROOT via
# PRECOMP_REPO_ROOT to skip the redundant git rev-parse subprocess.
REPO_ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
YAML="$REPO_ROOT/.owned-paths.yaml"
VALIDATE="$REPO_ROOT/.tools/owned-paths-validate.py"
# ONE LOG FOR EVERY WORKTREE (gap 4 of v3's first drain, 2026-09-04; 3.0.0_SA_CVO 94007, 4.0.0_SA_CRO 94014; placement
# 0.0.0_AB_MSTR 94049): the audit log is gitignored, so a LINKED worktree (a spine-v3 worker's) wrote its PASS/BLOCK/OVERRIDE
# rows into its own checkout's copy, which died with the worktree -- worker ~2's two OVERRIDE lines never reached the main
# tree. The log now resolves to the MAIN worktree root (the parent of `git rev-parse --git-common-dir`), same filename, so
# every reader keeps looking where it always did and every linked worktree writes the one log. In the main worktree the
# two roots coincide; a git that cannot answer falls back to REPO_ROOT (never to nowhere).
_GCD="$(git rev-parse --git-common-dir 2>/dev/null || true)"
case "$_GCD" in
    "") MAIN_ROOT="$REPO_ROOT" ;;
    /*|[A-Za-z]:*) MAIN_ROOT="$(cd "$_GCD/.." 2>/dev/null && pwd || echo "$REPO_ROOT")" ;;
    *) MAIN_ROOT="$(cd "$REPO_ROOT/$_GCD/.." 2>/dev/null && pwd || echo "$REPO_ROOT")" ;;
esac
# Test seam: OWNED_PATHS_AUDIT_LOG lets unit tests redirect the audit log.
AUDIT_LOG="${OWNED_PATHS_AUDIT_LOG:-$MAIN_ROOT/org/git-author-override-audit.log}"
MODE="${OWNED_PATHS_MODE:-block}"  # ADHC_OWNPTH.005 phase-2 flip 2026-04-30: was warn, flipped to block per Andrew directive
OVERRIDE="${GIT_COMMIT_AUTHOR_OVERRIDE:-}"

ISO_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

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
    echo "${ISO_TS} PASS  ${AGENT:-UNKNOWN}  0  (MERGE COMMIT -- per-file lane check exempt; merged files were gated at their own authorship)" >> "$AUDIT_LOG" 2>/dev/null || true
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

# Edge case: no staged files
if [ -z "$STAGED" ]; then
    echo "${ISO_TS} PASS  ${AGENT:-UNKNOWN}  0  (no staged files)" >> "$AUDIT_LOG" 2>/dev/null || true
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

# ---------------------------------------------------------------------------
# Override escape hatch
# ---------------------------------------------------------------------------
if [ -n "$OVERRIDE" ]; then
    echo "${ISO_TS} OVERRIDE  ${AGENT:-UNKNOWN}  ${N_FILES}  (--author-override ${OVERRIDE} applied)" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# Agent unknown
# ---------------------------------------------------------------------------
if [ -z "$AGENT" ]; then
    echo "WARN: GIT_AUTHOR_NAME not set -- skipping lane check" >&2
    echo "${ISO_TS} WARN  UNKNOWN  ${N_FILES}  (GIT_AUTHOR_NAME unset)" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi

# ---------------------------------------------------------------------------
# YAML not found
# ---------------------------------------------------------------------------
if [ ! -f "$YAML" ]; then
    echo "WARN: .owned-paths.yaml not found at $YAML -- skipping lane check" >&2
    if [ "$MODE" = "block" ]; then
        echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (YAML missing -- block mode EXIT 1)" \
            >> "$AUDIT_LOG" 2>/dev/null || true
        exit 1
    fi
    echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (YAML missing -- warn mode exit 0)" \
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
    echo "${ISO_TS} PASS  ${AGENT}  ${N_FILES}  (all paths in-lane)" \
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
    echo "${ISO_TS} BLOCK  ${AGENT}  ${N_FILES}  (${DETAIL})" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 1
else
    echo "WARN: owned-paths lane violation(s) detected (warn mode -- commit proceeds):" >&2
    printf '%s\n' "$VIOLATIONS" | grep -a '^VIOLATION:' >&2
    echo "  hint: use .tools/safe-commit.sh -- <paths> to scope commit to declared pathspec" >&2
    echo "${ISO_TS} WARN  ${AGENT}  ${N_FILES}  (${DETAIL})" \
        >> "$AUDIT_LOG" 2>/dev/null || true
    exit 0
fi
