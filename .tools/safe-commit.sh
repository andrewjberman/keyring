#!/usr/bin/env bash
# ADHC_OWNPTH.007 -- safe-commit.sh
# Wraps `git commit --only -- <pathspec>` with a staged-index vs pathspec
# contamination check. Aborts on mismatch unless --force is passed (logs bypass).
#
# Usage:
#   .tools/safe-commit.sh [--force] [--author "name <email>"] [-m "msg"] -- <path1> [path2...]
#   .tools/safe-commit.sh --help
#
# Audit log (FORCE-BYPASS only): org/git-author-override-audit.log
#   Format: {ISO8601} FORCE-BYPASS  {agent}  {N_extra}  ({first 5 extras truncated})

set -euo pipefail

show_help() {
  cat <<'EOF'
safe-commit.sh -- git commit wrapper with index-contamination guard.

USAGE:
  .tools/safe-commit.sh [--force] [git-commit-options...] -- <path1> [path2...]
  .tools/safe-commit.sh --help

BEHAVIOR:
  1. Captures the full staged index (git diff --cached --name-only).
  2. Compares against the declared pathspec (everything after --).
  3. If staged set contains any file NOT in the pathspec, abort with exit 1
     and list the contaminating files. The commit does NOT proceed.
  4. With --force, the abort is bypassed and a FORCE-BYPASS entry is written
     to org/git-author-override-audit.log. Use only when you cannot clean
     the shared index (e.g. multi-agent worktree contention).
  5. On pass (or after --force log), runs:
        git commit --only [git-commit-options] -- <pathspec>
     so the commit is scoped to the listed paths regardless of what else
     is in the shared index.

OPTIONS:
  --force              Bypass contamination check; log to audit trail.
  --help               Show this help and exit.
  -- <pathspec...>     Files to commit. Required. Forwarded to git commit --only.

ENV:
  SAFE_COMMIT_AUDIT_LOG  Override audit log path (default: <repo>/org/git-author-override-audit.log).

EXAMPLES:
  safe-commit.sh --author "0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>" \
    -m "infra(cloudops): bump shared-infra" \
    -- infra/aws/terraform/shared-infra/main.tf

  safe-commit.sh --force --author "..." -m "emergency hotfix" -- path/to/file
EOF
}

if [ $# -eq 0 ]; then
  show_help
  exit 0
fi

FORCE=0
COMMIT_ARGS=()
PATHSPEC=()
SEEN_DOUBLEDASH=0

while [ $# -gt 0 ]; do
  case "$1" in
    --help|-h)
      show_help
      exit 0
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --)
      SEEN_DOUBLEDASH=1
      shift
      while [ $# -gt 0 ]; do
        PATHSPEC+=("$1")
        shift
      done
      ;;
    *)
      COMMIT_ARGS+=("$1")
      shift
      ;;
  esac
done

if [ $SEEN_DOUBLEDASH -eq 0 ] || [ ${#PATHSPEC[@]} -eq 0 ]; then
  echo "ERROR: pathspec required after '--'." >&2
  echo "  See: $0 --help" >&2
  exit 2
fi

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "ERROR: not inside a git repository." >&2
  exit 2
}
AUDIT_LOG="${SAFE_COMMIT_AUDIT_LOG:-$REPO_ROOT/org/git-author-override-audit.log}"
ISO_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Extract agent name from --author "agent <email>" for audit log attribution
RAW_AUTHOR=""
n=${#COMMIT_ARGS[@]}
i=0
while [ $i -lt $n ]; do
  if [ "${COMMIT_ARGS[$i]}" = "--author" ]; then
    j=$((i + 1))
    if [ $j -lt $n ]; then
      RAW_AUTHOR="${COMMIT_ARGS[$j]}"
    fi
    break
  fi
  i=$((i + 1))
done
AGENT="${RAW_AUTHOR%% <*}"
AGENT="${AGENT:-UNKNOWN}"

# Capture staged set
STAGED="$(git diff --cached --name-only 2>/dev/null || true)"

# Build pathspec lookup
declare -A PATHSPEC_SET=()
for p in "${PATHSPEC[@]}"; do
  PATHSPEC_SET["$p"]=1
done

# Find contaminating files
EXTRA=()
if [ -n "$STAGED" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ -z "${PATHSPEC_SET[$f]+x}" ]; then
      EXTRA+=("$f")
    fi
  done <<< "$STAGED"
fi

N_EXTRA="${#EXTRA[@]}"

if [ "$N_EXTRA" -gt 0 ]; then
  if [ "$FORCE" -eq 1 ]; then
    # First 5 extras for audit detail, truncate the rest
    SHOW_N=$N_EXTRA
    [ $SHOW_N -gt 5 ] && SHOW_N=5
    DETAIL=""
    k=0
    while [ $k -lt $SHOW_N ]; do
      if [ -n "$DETAIL" ]; then
        DETAIL="${DETAIL},${EXTRA[$k]}"
      else
        DETAIL="${EXTRA[$k]}"
      fi
      k=$((k + 1))
    done
    if [ "$N_EXTRA" -gt 5 ]; then
      DETAIL="${DETAIL}...+$((N_EXTRA - 5))"
    fi
    mkdir -p "$(dirname "$AUDIT_LOG")"
    echo "${ISO_TS} FORCE-BYPASS  ${AGENT}  ${N_EXTRA}  (${DETAIL})" >> "$AUDIT_LOG"
    echo "WARN: --force bypass; ${N_EXTRA} contaminating staged file(s) ignored:" >&2
    printf '  %s\n' "${EXTRA[@]}" >&2
    echo "  Audit: ${AUDIT_LOG}" >&2
  else
    echo "ERROR: staged index contains files not in declared pathspec." >&2
    echo "       Commit aborted. Use --force to bypass (logs to audit)." >&2
    echo "" >&2
    echo "Declared pathspec (${#PATHSPEC[@]} file(s)):" >&2
    printf '  %s\n' "${PATHSPEC[@]}" >&2
    echo "" >&2
    echo "Contaminating staged files (${N_EXTRA}):" >&2
    printf '  %s\n' "${EXTRA[@]}" >&2
    echo "" >&2
    echo "Fix options:" >&2
    echo "  - git reset HEAD -- <extras>     # unstage extras, commit yours cleanly" >&2
    echo "  - rerun with --force             # log bypass to audit and proceed" >&2
    exit 1
  fi
fi

# Proceed with the actual scoped commit
exec git commit --only "${COMMIT_ARGS[@]}" -- "${PATHSPEC[@]}"
