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

BEHAVIOR (commit-mutex v2 -- stage-inside-lock, MSTR-approved 2026-05-29):
  DO NOT pre-`git add` -- this wrapper stages your declared pathspec itself.
  1. Acquires a per-worktree mkdir-mutex (serializes concurrent agents).
  2. Captures the BASELINE staged set at lock-entry (peers' / pre-staged files).
  3. Stages your declared pathspec inside the lock: git add -f -- <pathspec>
     (force so a new file under a gitignored prefix needs no separate add).
  4. Contamination = files staged by THIS run that are outside the pathspec
     AND not in the baseline. Peers' baseline files are IGNORED (git commit
     --only can never commit them anyway). If contamination found, abort
     exit 1 (or --force bypass with FORCE-BYPASS audit entry).
  5. Runs: git commit --only [git-commit-options] -- <pathspec>
     scoped to the listed paths regardless of index state. Mutex released
     on EXIT (trap). Stale lock reclaimed via dead-PID or age>=timeout.

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

# RV-0017 F-006 Pattern A -- mkdir-mutex commit-serialization (Rule 16 Git-Bash
# compatible; flock not available). Serializes safe-commit.sh body across all
# concurrent agents in this repo so the shared-index contamination race
# (git diff --cached returning a peer's staged paths) cannot trip lane-violation
# BLOCKs that aren't real. Lock held from staged-index capture through commit +
# pre-commit hook completion. Stale-lock reclaim via kill -0 on holder PID.
# Worktree-safe: $REPO_ROOT/.git is a FILE (gitdir pointer) in a linked worktree,
# so mkdir "$REPO_ROOT/.git/commit-queue.lock" fails ENOTDIR and the lock can
# NEVER be acquired (spins to timeout -> agents fall back to unserialized/force
# commits -> commit storm). --absolute-git-dir resolves the per-worktree gitdir,
# which is ALWAYS a real directory (main: .git ; worktree: .git/worktrees/<name>),
# giving correct per-index serialization in every checkout. (Fix: worktree commit-storm 2026-05-29)
LOCK_DIR="${SAFE_COMMIT_LOCK_DIR:-$(git rev-parse --absolute-git-dir 2>/dev/null)/commit-queue.lock}"
LOCK_TIMEOUT_SEC="${SAFE_COMMIT_LOCK_TIMEOUT:-60}"
LOCK_ACQUIRED=0
elapsed=0
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  # Stale-lock detection #1: holder PID dead -> reclaim immediately.
  if [ -f "$LOCK_DIR/pid" ]; then
    holder_pid="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
    if [ -n "$holder_pid" ] && ! kill -0 "$holder_pid" 2>/dev/null; then
      rm -rf "$LOCK_DIR" 2>/dev/null || true
      continue
    fi
  fi
  # Stale-lock detection #2 (ADHC commit-mutex v2): age-based break. Covers the
  # PID-reuse hole -- a crashed holder whose PID was recycled by a different live
  # process would read as alive under kill -0 and deadlock the fabric forever.
  # If the lock dir is >= LOCK_TIMEOUT_SEC old, break it. mtime via `stat -c %Y`
  # (Git-Bash 3.6.7 default, Rule 16 OK); `find -mmin` guarded fallback.
  lock_mtime=""
  if command -v stat >/dev/null 2>&1; then
    lock_mtime="$(stat -c %Y "$LOCK_DIR" 2>/dev/null || true)"
  fi
  if [ -n "$lock_mtime" ]; then
    now_s="$(date +%s)"
    if [ $((now_s - lock_mtime)) -ge "$LOCK_TIMEOUT_SEC" ]; then
      rm -rf "$LOCK_DIR" 2>/dev/null || true
      continue
    fi
  elif find "$LOCK_DIR" -maxdepth 0 -mmin +1 2>/dev/null | grep -q .; then
    # stat unavailable -> 1-minute mmin fallback
    rm -rf "$LOCK_DIR" 2>/dev/null || true
    continue
  fi
  elapsed=$((elapsed + 1))
  if [ "$elapsed" -ge "$LOCK_TIMEOUT_SEC" ]; then
    echo "ERROR: safe-commit mutex held >${LOCK_TIMEOUT_SEC}s by PID $(cat "$LOCK_DIR/pid" 2>/dev/null || echo unknown)." >&2
    echo "       Other agent's commit stuck or hung. Inspect $LOCK_DIR." >&2
    exit 3
  fi
  sleep 1
done
echo "$$" > "$LOCK_DIR/pid"
LOCK_ACQUIRED=1
trap '[ "$LOCK_ACQUIRED" -eq 1 ] && rm -rf "$LOCK_DIR" 2>/dev/null || true' EXIT

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

# ADHC commit-mutex v2 (MSTR-approved 2026-05-29): stage-inside-lock + baseline-diff.
# WHY: the mutex alone (LD-0138) serializes safe-commit bodies but NOT the `git add`
# callers ran separately, nor a peer's out-of-band add on the shared index -- so
# `git diff --cached` saw peers' staged files and false-aborted (empirically 2x
# 2026-05-29). Fix: (1) capture BASELINE first (foreign/pre-staged files present at
# lock-entry); (2) stage our OWN declared pathspec INSIDE the lock (callers no longer
# pre-`git add`); (3) contamination = (staged-now \ baseline) \ pathspec -- i.e. ONLY
# files THIS run staged outside its own pathspec. Peers' baseline files are excluded
# (and `git commit --only` structurally can never commit them anyway). The guard still
# catches a genuine self-scope error; it stops policing peers.

# (1) BASELINE: what was already staged at lock-entry (foreign + any caller pre-add).
BASELINE="$(git diff --cached --name-only 2>/dev/null || true)"
declare -A BASELINE_SET=()
if [ -n "$BASELINE" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    BASELINE_SET["$f"]=1
  done <<< "$BASELINE"
fi

# (2) Stage our declared pathspec inside the lock. -f so a new file under a
# gitignored prefix (e.g. .tools/) is staged without a separate caller `git add -f`
# (the caller listed it explicitly = intent). Idempotent for already-tracked/staged.
git add -f -- "${PATHSPEC[@]}" 2>/dev/null || true

# Build pathspec lookup
declare -A PATHSPEC_SET=()
for p in "${PATHSPEC[@]}"; do
  PATHSPEC_SET["$p"]=1
done

# (3) Contamination = staged-now files that are NEITHER in the declared pathspec
# NOR in the baseline (= files THIS run staged beyond its own scope).
STAGED="$(git diff --cached --name-only 2>/dev/null || true)"
EXTRA=()
if [ -n "$STAGED" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ -z "${PATHSPEC_SET[$f]+x}" ] && [ -z "${BASELINE_SET[$f]+x}" ]; then
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

# Proceed with the actual scoped commit. Use plain invocation (not exec) so the
# EXIT trap fires after commit completion and releases the mutex.
git commit --only "${COMMIT_ARGS[@]}" -- "${PATHSPEC[@]}"
exit $?
