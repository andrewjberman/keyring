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

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
YAML="$REPO_ROOT/.owned-paths.yaml"
VALIDATE="$REPO_ROOT/.tools/owned-paths-validate.py"
# Test seam: OWNED_PATHS_AUDIT_LOG lets unit tests redirect the audit log.
AUDIT_LOG="${OWNED_PATHS_AUDIT_LOG:-$REPO_ROOT/org/git-author-override-audit.log}"
MODE="${OWNED_PATHS_MODE:-warn}"
OVERRIDE="${GIT_COMMIT_AUTHOR_OVERRIDE:-}"

ISO_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ---------------------------------------------------------------------------
# Extract agent serial from GIT_AUTHOR_NAME (strip <email@...> suffix)
# ---------------------------------------------------------------------------
RAW_AUTHOR="${GIT_AUTHOR_NAME:-}"
AGENT="${RAW_AUTHOR%% <*}"

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

N_FILES="$(printf '%s\n' "$STAGED" | grep -c . || true)"

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
