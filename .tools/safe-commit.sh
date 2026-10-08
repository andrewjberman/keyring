#!/usr/bin/env bash
# NFRA_CMTQUE TO-2 -- safe-commit.sh: THIN ENQUEUE CLIENT (+ legacy mkdir-mutex fallback).
# LANDED 2026-07-06 (CVO-verified PASS 9a53b84ea, MSTR go, LD-0247-adjacent). The queue
# path is DORMANT: SAFE_COMMIT_USE_QUEUE defaults OFF -> the legacy path runs -> byte-for-
# byte the pre-queue behavior for all ~1338 callers (verified by the compat matrix). The
# TO-6 cutover flips the flag ON after the load-test + CVO-verify + CTO-consult. Do NOT
# set SAFE_COMMIT_USE_QUEUE=1 outside the TO-6 canary until then.
#
# INTERFACE: byte-for-byte identical to the pre-queue safe-commit.sh (arg parse + exit
# codes {0 commit / 1 contamination|sensitive / 2 usage|not-repo / 3 timeout / git rc
# passthrough}). The ONLY caller-visible change, and ONLY on the (dormant) queue path, is
# the success stdout (a synthesized "[branch hash] subject [commit-queue]" line instead of
# git's multi-line summary -- CVO-verified 0 callers parse safe-commit stdout). No caller change.
#
# TWO PATHS:
#   QUEUE  (SAFE_COMMIT_USE_QUEUE=1 AND a live worker): build a commit-request, enqueue
#          to the local durable queue, BLOCK for the result, reproduce exit/reason. The
#          single concurrency=1 worker owns the git index -> no mutex, no 60s storm, no
#          contamination race. This path is DORMANT by default (flag off) until the
#          TO-6 canary/cutover flips it.
#   LEGACY (default, OR the D6 fallback when the flag is on but the worker is DOWN):
#          today's mkdir-mutex + stage + sensitive-gate + contamination + git commit,
#          PRESERVED byte-for-byte -- except the sensitive-leak gate now calls the SHARED
#          cg_sensitive_hits (commit_gate_lib.sh, TO-5) so there is ONE gate impl, no
#          copy-drift between the worker and this fallback (CTO directive).
#
# So: worker down / flag off -> today's exact behavior (never a regression); worker up +
# flag on -> the queue. A dead worker degrades to today, never blocks (D6).

set -euo pipefail

show_help() {
  cat <<'EOF'
safe-commit.sh -- git commit wrapper. Enqueue-client (concurrency=1 worker) with a
legacy mkdir-mutex fallback. Byte-for-byte CLI-compatible with the pre-queue version.

USAGE:
  .tools/safe-commit.sh [--force] [git-commit-options...] -- <path1> [path2...]
  .tools/safe-commit.sh --help

BEHAVIOR:
  DO NOT pre-`git add` -- this wrapper stages your declared pathspec itself.
  With SAFE_COMMIT_USE_QUEUE=1 and a live commit-worker, the request is enqueued to a
  durable local queue and a single serial worker commits it (no lock contention, no
  60s timeout-storm). Otherwise (default, or worker down) it uses the legacy per-worktree
  mkdir-mutex + stage + sensitive-leak gate + contamination check + git commit --only.

SECURITY -- the -f overrides .gitignore (read before committing near secrets):
  Staging uses `git add -f`, which FORCE-adds files EVEN IF gitignored. A DIRECTORY
  pathspec (e.g. `-- workflows/`) silently sweeps in gitignored secrets/PII (HARs with
  live cookies, .env, keys). The SENSITIVE-LEAK GATE fail-CLOSED-blocks a would-be leak
  (unambiguous secret types always; contextual patterns when also gitignored). Pass
  EXPLICIT file paths near a sources/HAR/.env tree -- never a bare directory.

OPTIONS:
  --force              Bypass contamination check (legacy path); log to audit trail.
  --help               Show this help and exit.
  -- <pathspec...>     Files to commit. Required. Forwarded to git commit --only.

ENV:
  SAFE_COMMIT_USE_QUEUE        1 -> use the commit-queue worker when it's live (default 0).
  SAFE_COMMIT_QUEUE_TIMEOUT    seconds to await a worker result before erroring (default 120).
  SAFE_COMMIT_AUDIT_LOG        Override audit log path.
  SAFE_COMMIT_ALLOW_SENSITIVE  Reason string to override the sensitive-leak gate (audited).

EXAMPLES:
  safe-commit.sh --author "0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>" \
    -m "infra(cloudops): bump shared-infra" -- infra/aws/terraform/shared-infra/main.tf
  safe-commit.sh --force --author "..." -m "emergency hotfix" -- path/to/file
EOF
}

if [ $# -eq 0 ]; then
  show_help
  exit 0
fi

# --------------------------------------------------------------------------
# Arg parse -- PRESERVED byte-for-byte from the pre-queue safe-commit.sh.
# --------------------------------------------------------------------------
_SC_ORIG_ARGS=("$@")   # two-phase re-exec on a same-path race replays these
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

# ----------------------------------------------------------------------------
# MESSAGE-FLAG GATE (2026-08-27, Andrew-direct at the COO terminal after the
# 19:34Z index.lock outage). A safe-commit invoked with NO message flag used to
# pass straight through to `git commit`, which opened $EDITOR and waited on a
# human forever -- holding .git/index.lock and blocking EVERY seat on the shared
# worktree (measured cost: one flag omission = a fabric-wide write outage; the
# holder was a live process that could never finish). This script's message code
# was all CONSUMING gates (scan/override/verify) that yield "" on an absent flag
# -- no arm ever REQUIRED one. Rule 14a's -F imperative is now mechanical here.
# Satisfying flags: -F/--file (the lawful form), -m/--message (deprecated but
# legal), -C/--reuse-message (carries a message without an editor). -c and
# --reedit-message do NOT satisfy it: they reach an editor BY DESIGN and a
# headless session cannot answer one.
# ----------------------------------------------------------------------------
_HAS_MSG_FLAG=0
_mfi=0
while [ $_mfi -lt ${#COMMIT_ARGS[@]} ]; do
  case "${COMMIT_ARGS[$_mfi]}" in
    -m|--message|-F|--file|-C|--reuse-message) _HAS_MSG_FLAG=1; break ;;
    -m=*|--message=*|-F=*|--file=*|-C=*|--reuse-message=*) _HAS_MSG_FLAG=1; break ;;
  esac
  _mfi=$((_mfi + 1))
done
if [ "$_HAS_MSG_FLAG" -eq 0 ]; then
  echo "ERROR: no commit-message flag (-F <file> / -m / -C). REFUSED before any staging." >&2
  echo "  A message-less commit sends git to an interactive \$EDITOR no headless session" >&2
  echo "  can answer -- it hangs holding .git/index.lock and blocks EVERY seat" >&2
  echo "  (2026-08-27 19:34Z outage). Rule 14a: write the message with a NON-SHELL writer" >&2
  echo "  and pass it via -F <msgfile>. -m is deprecated for bodies with special chars." >&2
  exit 2
fi

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "ERROR: not inside a git repository." >&2
  exit 2
}

# NESTED-REPO GATE (OA-w-2, 2026-09-24): a commit made INSIDE a mapped submodule
# (opal_ai/**) has REPO_ROOT above at the NESTED repo's own toplevel, which carries no
# org/ tree of its own -- the audit log belongs on the PARENT's MAIN tree, the one
# shared log every reader already looks at (same fix owned-paths-check.sh already
# carries for a linked worktree, chained one level deeper here). Git operations
# themselves (staging, mutex, commit) stay scoped to the nested repo via cwd/git-dir
# as today -- only the AUDIT LOG's root moves. Empty-superproject (the parent itself,
# every existing caller) leaves _AUDIT_ROOT == REPO_ROOT: byte-identical to before.
_AUDIT_ROOT="$REPO_ROOT"
_SUPERPROJECT="$(git rev-parse --show-superproject-working-tree 2>/dev/null || true)"
if [ -z "$_SUPERPROJECT" ]; then
  # A LINKED WORKTREE of the nested repo: ask its MAIN worktree (always listed first)
  # for ITS superproject, same reasoning as owned-paths-check.sh.
  _NESTED_MAIN_WT="$(git worktree list --porcelain 2>/dev/null | awk '/^worktree /{print $2; exit}')"
  if [ -n "$_NESTED_MAIN_WT" ]; then
    _SUPERPROJECT="$(git -C "$_NESTED_MAIN_WT" rev-parse --show-superproject-working-tree 2>/dev/null || true)"
  fi
fi
if [ -n "$_SUPERPROJECT" ]; then
  _AUDIT_ROOT="$_SUPERPROJECT"
  # Chain to the superproject's OWN main worktree if it too is a linked one (a spine-v3
  # worker's checkout) so the nested commit's row still lands in the one shared log.
  _GCD="$(git -C "$_AUDIT_ROOT" rev-parse --git-common-dir 2>/dev/null || true)"
  case "$_GCD" in
    "") : ;;
    /*|[A-Za-z]:*) _AUDIT_ROOT="$(cd "$_GCD/.." 2>/dev/null && pwd || echo "$_AUDIT_ROOT")" ;;
    *) _AUDIT_ROOT="$(cd "$_AUDIT_ROOT/$_GCD/.." 2>/dev/null && pwd || echo "$_AUDIT_ROOT")" ;;
  esac
fi
AUDIT_LOG="${SAFE_COMMIT_AUDIT_LOG:-$_AUDIT_ROOT/org/git-author-override-audit.log}"
ISO_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"


# Extract agent name from --author "agent <email>" for audit attribution + the request.
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

# --------------------------------------------------------------------------
# MERGE IN PROGRESS -> REFUSE BEFORE ANYTHING IS STAGED (2026-09-04, 1.0.0_SA_CTO;
# NFRA_CLDGRPH-S35, the class measured from both sides: 2.0.0_SA_COO~A 94170 named it
# from the drain, this seat took it from the swept side, 2.0.0_SA_COO 94196 confirmed
# the file is lane ANY and the fix belongs here).
#
# THE CHAIN THIS CUTS, every step measured on 2026-09-04:
#   1. a drain merge is in progress in the SHARED worktree (MERGE_HEAD present);
#   2. another seat runs safe-commit; `git commit --only -- <pathspec>` is REFUSED by
#      git during a merge -> rc 128, and the run dies AFTER its staging step;
#   3. the failed run leaves the seat's file STAGED in the shared index;
#   4. the drain's own merge commit carries it -- measured: b687429234, 15 files, 14 the
#      worker's and 1 this seat's Andrew-direct record -- under the DRAINING seat's
#      authorship, and `git log -- <that file>` names the merge as its only commit;
#   5. nothing refuses, because owned-paths-check EXEMPTS merges by design (correctly,
#      for files a merge really carries -- that one it did not).
#
# >> THE RESIDUE IS THE WHOLE MECHANISM. Refusing here, before the mutex and before the
#    staging step, leaves nothing for a merge to sweep. Anything downstream of the
#    staging is a control on a symptom. <<
#
# TWO PROPERTIES, both named by 2.0.0_SA_COO 94196 out of its own tool's mirror defect:
#   (a) REFUSE -- never fall back to a commit without `--only`. That would sweep the
#       MERGE's own staged set under the committing seat: the same false attribution one
#       layer over, and worse because it would look like a success.
#   (b) Read the TARGET WORKTREE's own merge state via `git rev-parse --git-path
#       MERGE_HEAD`, not "$REPO_ROOT/.git/MERGE_HEAD" -- a linked worktree keeps its
#       merge state in its own gitdir, and the shared-tree case is exactly where this
#       bites.
# NO OVERRIDE IS OFFERED. An override here would re-open the sweep, and the remedy is
# never a flag: wait for the drain, or finish the merge. rc 3 is NOT a new code: it is
# this file's existing NOTHING-LANDED-TRY-AGAIN family (the queue timeout at :279 and the
# mutex timeout at :349 already use it), which is exactly what a merge in flight is --
# contention, not a fault in the caller's commit.
_MERGE_HEAD_PATH="$(git rev-parse --git-path MERGE_HEAD 2>/dev/null || echo "")"
if [ -n "$_MERGE_HEAD_PATH" ] && [ -f "$_MERGE_HEAD_PATH" ]; then
  _merge_other="$(cat "$_MERGE_HEAD_PATH" 2>/dev/null | head -1)"
  _merge_staged="$(git diff --cached --name-only 2>/dev/null | wc -l | tr -d ' ')"
  {
    echo "======================================================================"
    echo "safe-commit: REFUSED -- A MERGE IS IN PROGRESS IN THIS WORKTREE"
    echo "======================================================================"
    echo "  MERGE_HEAD : ${_merge_other:-<unreadable>}"
    echo "  worktree   : $REPO_ROOT"
    echo "  staged now : ${_merge_staged} path(s) -- the MERGE's, not yours"
    echo ""
    echo "  git refuses 'commit --only -- <pathspec>' during a merge, so this run"
    echo "  would fail at the commit step AFTER staging your files -- and the next"
    echo "  merge commit would then carry them under the MERGING seat's authorship,"
    echo "  where the owned-paths merge exemption means no lane check sees it."
    echo "  Measured 2026-09-04: merge b687429234 carried 15 files, 1 of them a"
    echo "  foreign seat's record (NFRA_CLDGRPH-S35)."
    echo ""
    echo "  NOTHING WAS STAGED BY THIS RUN. Your files are untouched."
    echo ""
    echo "  Do one of:"
    echo "    - wait for the merge to finish (a drain closes in its own time), then re-run;"
    echo "    - if the merge is YOURS, finish it (git merge --continue / --abort) first."
    echo "  There is deliberately no override: a flag here re-opens the sweep."
    echo "======================================================================"
  } >&2
  echo "${ISO_TS} MERGE-REFUSED  ${AGENT:-UNKNOWN}  ${_merge_staged}  (MERGE_HEAD ${_merge_other:0:12} present; nothing staged by this run)" \
    >> "$AUDIT_LOG" 2>/dev/null || true
  exit 3
fi

# --------------------------------------------------------------------------
# Source the shared libs (queue primitives + the SHARED sensitive-leak gate).
# The libs run `set -uo pipefail` at load -> re-assert -euo after to keep this
# script's intended options (the legacy path relies on -e as a safety net).
# --------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=commit_gate_lib.sh
source "$SCRIPT_DIR/commit_gate_lib.sh"
# shellcheck source=commit_queue_lib.sh
source "$SCRIPT_DIR/commit_queue_lib.sh"
set -euo pipefail

# ==========================================================================
# QUEUE PATH -- only when explicitly enabled AND a live worker is present.
# Dormant by default (flag off) until the TO-6 canary/cutover.
# ==========================================================================
if [ "${SAFE_COMMIT_USE_QUEUE:-0}" = "1" ] && cq_worker_alive; then
  # forward the per-commit env the worker's gate needs.
  ENV_LIST=()
  [ -n "${SAFE_COMMIT_ALLOW_SENSITIVE:-}" ] && ENV_LIST+=("SAFE_COMMIT_ALLOW_SENSITIVE=${SAFE_COMMIT_ALLOW_SENSITIVE}")
  [ -n "${SAFE_COMMIT_AUDIT_LOG:-}" ] && ENV_LIST+=("SAFE_COMMIT_AUDIT_LOG=${SAFE_COMMIT_AUDIT_LOG}")

  REQID="$(cq_enqueue "$PWD" "$FORCE" "$RAW_AUTHOR" \
    "${#COMMIT_ARGS[@]}" "${COMMIT_ARGS[@]}" \
    "${#PATHSPEC[@]}" "${PATHSPEC[@]}" \
    "${#ENV_LIST[@]}" "${ENV_LIST[@]}")" || {
      echo "ERROR: commit-queue enqueue failed; falling back to legacy path." >&2
      REQID=""
  }

  if [ -n "$REQID" ]; then
    # BLOCK for the result -- an orderly FIFO drain by a warm worker (no 60s storm).
    QTIMEOUT="${SAFE_COMMIT_QUEUE_TIMEOUT:-120}"
    waited=0
    while ! cq_result_ready "$REQID"; do
      sleep 1
      waited=$((waited + 1))
      if [ "$waited" -ge "$QTIMEOUT" ]; then
        echo "ERROR: commit-queue worker returned no result for $REQID in ${QTIMEOUT}s." >&2
        echo "       Request is enqueued -- do NOT blindly retry (double-commit risk):" >&2
        echo "       verify with 'git log -1'; inspect the queue at $(cq_root)." >&2
        exit 3
      fi
    done

    RP="$(cq_result_path "$REQID")"
    R_STATUS="$(cq_field "$RP" STATUS)"
    R_EXIT="$(cq_field "$RP" EXIT_CODE)"
    R_HASH="$(cq_field "$RP" COMMIT_HASH)"
    R_REASON="$(cq_b64dec "$(cq_field "$RP" REASON)")"
    R_STDERR="$(cq_b64dec "$(cq_field "$RP" STDERR)")"
    rm -f "$RP" 2>/dev/null || true   # consume the result -> results/ stays clean

    if [ "$R_STATUS" = "committed" ]; then
      # synthesized git-style first line (subject from -m; branch + short hash).
      SUBJECT=""
      k=0
      while [ $k -lt ${#COMMIT_ARGS[@]} ]; do
        if [ "${COMMIT_ARGS[$k]}" = "-m" ] && [ $((k + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
          SUBJECT="${COMMIT_ARGS[$((k + 1))]%%$'\n'*}"; break
        fi
        k=$((k + 1))
      done
      BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo HEAD)"
      echo "[$BRANCH ${R_HASH:0:9}] ${SUBJECT} [commit-queue]"
      exit 0
    else
      # rejected (gate/hook/nothing-to-commit) or error -> reproduce reason + exit code.
      [ -n "$R_REASON" ] && echo "$R_REASON" >&2
      [ -n "$R_STDERR" ] && echo "$R_STDERR" >&2
      exit "${R_EXIT:-1}"
    fi
  fi
  # REQID empty -> enqueue failed -> fall through to the legacy path (D6).
fi

# ==========================================================================
# TWO-PHASE COMMIT (opt-in: SAFE_COMMIT_TWO_PHASE=1). GitOps; Andrew-direct 2026-10-08 ~16:5xZ and his ruling ~17:0xZ
# ("Yes go ahead"), record org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_165xZ_LEAD_COMMIT_LOCK_SHRINK_BUILD.md.
# VALIDATE, with NO lock: staging, every safe-commit gate below, and the pre-commit, prepare-commit-msg and commit-msg
#   hooks run in a PRIVATE git dir whose HEAD is pinned at BASE (the tip read here) and whose index is private, over
#   the SHARED working tree (GIT_DIR=<private dir>, GIT_WORK_TREE=<this worktree>; the private dir's `commondir` file
#   names the real common git dir, so objects, refs, config and hooks are the real ones). HEAD cannot move under the
#   gates, and the shared index is never touched while they run.
# LAND, under the SAME lock the legacy path takes: write the validated entries onto the CURRENT tip with git plumbing
#   (read-tree, update-index, write-tree, commit-tree, update-ref with the expected old value), bring the shared index's
#   entries for those paths level with the commit, release. THEN run the post-commit hook, outside the lock, in a
#   second private git dir whose HEAD is pinned at the NEW commit (every post-commit script reads HEAD; pinned, a peer's
#   commit cannot be read as this one). Three of them leave background jobs that keep that dir in use, so it is not
#   removed here: each two-phase run removes such dirs older than an hour.
# A commit that loses the race waits only for the land lock and never re-validates, UNLESS a commit that landed after
#   BASE changed one of the same paths: then this run re-executes itself from the top, at most 3 attempts in all.
# Not eligible -> the legacy path below, unchanged, with one line saying why.
# ==========================================================================
_SC_2P=0
_SC2P_WHY=""
_SC2P_DIR=""
_SC2P_MSGKIND=""
_SC2P_MSGFILE=""
_SC2P_MSGS=()
_sc_on_exit() {
  if [ "${LOCK_ACQUIRED:-0}" -eq 1 ]; then rm -rf "$LOCK_DIR" 2>/dev/null || true; fi
  if [ -n "${_SC2P_DIR:-}" ]; then rm -rf "$_SC2P_DIR" 2>/dev/null || true; fi
  return 0
}
_sc2p_eligible() {
  local k=0 a=""
  [ "${SAFE_COMMIT_TWO_PHASE:-0}" = "1" ] || { _SC2P_WHY="flag off"; return 1; }
  [ "${SAFE_COMMIT_USE_QUEUE:-0}" != "1" ] || { _SC2P_WHY="the queue path was requested"; return 1; }
  [ -z "${GIT_DIR:-}${GIT_WORK_TREE:-}${GIT_INDEX_FILE:-}" ] || { _SC2P_WHY="the caller set GIT_DIR, GIT_WORK_TREE or GIT_INDEX_FILE"; return 1; }
  [ -z "${_SUPERPROJECT:-}" ] || { _SC2P_WHY="a nested repo (submodule)"; return 1; }
  # The commit lock is per worktree, so only the MAIN (shared) worktree has contention to remove; a linked worktree
  # keeps the legacy path (its own lock, nobody else in it).
  [ "$(git rev-parse --path-format=absolute --git-dir 2>/dev/null)" = "$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null)" ]     || { _SC2P_WHY="a linked worktree (its lock is its own; nothing to gain)"; return 1; }
  git symbolic-ref -q HEAD >/dev/null 2>&1 || { _SC2P_WHY="HEAD is detached"; return 1; }
  case "$(git config --get commit.cleanup 2>/dev/null || true)" in ""|default|whitespace) ;; *) _SC2P_WHY="commit.cleanup is set"; return 1 ;; esac
  while [ $k -lt ${#COMMIT_ARGS[@]} ]; do
    a="${COMMIT_ARGS[$k]}"
    case "$a" in
      --author) k=$((k + 2)); continue ;;
      -F|--file)
        [ -z "$_SC2P_MSGKIND" ] || { _SC2P_WHY="more than one message source"; return 1; }
        _SC2P_MSGKIND=F; _SC2P_MSGFILE="${COMMIT_ARGS[$((k + 1))]:-}"; k=$((k + 2)); continue ;;
      --file=*)
        [ -z "$_SC2P_MSGKIND" ] || { _SC2P_WHY="more than one message source"; return 1; }
        _SC2P_MSGKIND=F; _SC2P_MSGFILE="${a#--file=}"; k=$((k + 1)); continue ;;
      -m|--message)
        [ "$_SC2P_MSGKIND" != F ] || { _SC2P_WHY="-m mixed with -F"; return 1; }
        _SC2P_MSGKIND=m; _SC2P_MSGS+=("${COMMIT_ARGS[$((k + 1))]:-}"); k=$((k + 2)); continue ;;
      --message=*)
        [ "$_SC2P_MSGKIND" != F ] || { _SC2P_WHY="-m mixed with -F"; return 1; }
        _SC2P_MSGKIND=m; _SC2P_MSGS+=("${a#--message=}"); k=$((k + 1)); continue ;;
      *) _SC2P_WHY="commit argument '$a' is not handled by the two-phase path"; return 1 ;;
    esac
  done
  [ -n "$_SC2P_MSGKIND" ] || { _SC2P_WHY="no -F or -m message"; return 1; }
  if [ "$_SC2P_MSGKIND" = F ]; then
    { [ "$_SC2P_MSGFILE" != "-" ] && [ -f "$_SC2P_MSGFILE" ]; } || { _SC2P_WHY="the -F file is missing or is stdin"; return 1; }
  fi
  local _re='^[^<>]+ <[^<>]*>$'
  [[ "$RAW_AUTHOR" =~ $_re ]] || { _SC2P_WHY="--author is missing or not 'Name <email>'"; return 1; }
  return 0
}
if _sc2p_eligible; then
  _SC_2P=1
elif [ "${SAFE_COMMIT_TWO_PHASE:-0}" = "1" ]; then
  echo "safe-commit: two-phase NOT used (${_SC2P_WHY}); legacy path." >&2
fi
if [ "$_SC_2P" -eq 1 ]; then
  _SC2P_T0="$EPOCHREALTIME"
  _SC2P_BASE="$(git rev-parse --verify HEAD)"
  _SC2P_REAL_GITDIR="$(git rev-parse --absolute-git-dir)"
  _SC2P_COMMON="$(git rev-parse --path-format=absolute --git-common-dir)"
  _SC2P_WT="$(git rev-parse --show-toplevel)"
  _SC2P_REAL_INDEX="$(git rev-parse --path-format=absolute --git-path index)"
  _SC2P_NOW="${EPOCHSECONDS:-0}"
  for _old in "${_SC2P_REAL_GITDIR}"/sc2p-*-*; do
    [ -d "$_old" ] || continue
    _oe="${_old##*/sc2p-}"; _oe="${_oe#pc-}"; _oe="${_oe%%-*}"
    case "$_oe" in (*[!0-9]*|"") continue ;; esac
    if [ $((_SC2P_NOW - _oe)) -gt 3600 ]; then rm -rf "$_old" 2>/dev/null || true; fi
  done
  _SC2P_DIR="${_SC2P_REAL_GITDIR}/sc2p-${_SC2P_NOW}-$$"
  trap '_sc_on_exit' EXIT
  rm -rf "$_SC2P_DIR" 2>/dev/null || true
  mkdir -p "$_SC2P_DIR"
  printf '%s\n' "$_SC2P_BASE" > "$_SC2P_DIR/HEAD"
  printf '%s\n' "$_SC2P_COMMON" > "$_SC2P_DIR/commondir"
  export GIT_DIR="$_SC2P_DIR" GIT_WORK_TREE="$_SC2P_WT"
  git read-tree "$_SC2P_BASE"
fi

# Release the land lock early (the two-phase path; the legacy path keeps its EXIT-trap release).
_sc_release_lock() {
  if [ "${LOCK_ACQUIRED:-0}" -eq 1 ]; then rm -rf "$LOCK_DIR" 2>/dev/null || true; LOCK_ACQUIRED=0; fi
  return 0
}

# _sc2p_commit: the hooks (validate, pinned env), then the land. Sets _commit_out; returns git-commit-like codes
# (0 landed; 1 a hook refused or nothing to commit; 3 contention, nothing landed). Called in a conditional, so set -e
# is off inside: every step checks its own rc.
_sc2p_commit() {
  local out="" rc=0 msg="" k=0 meta="" path="" n=0 cur="" tree="" commit="" subject="" branch="" pc_out="" att=""
  local t_v1="" t_l1="" t_l2="" t_l3="" t_b="" t_r="" overlap="" stat="" pc_dir=""
  local -A _mine=()
  GIT_AUTHOR_NAME="${RAW_AUTHOR% <*}"; GIT_AUTHOR_EMAIL="${RAW_AUTHOR##*<}"; GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL%>}"
  export GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL
  # (V1) pre-commit, on the private index with HEAD pinned at BASE.
  out="$(GIT_EDITOR=false git hook run --ignore-missing pre-commit 2>&1)" || rc=$?
  if [ "$rc" -ne 0 ]; then _commit_out="$out"; return 1; fi
  # (V2) the message, as git commit builds it: -F verbatim, or the -m paragraphs joined by a blank line.
  msg="$_SC2P_DIR/COMMIT_EDITMSG"
  if [ "$_SC2P_MSGKIND" = F ]; then
    cat -- "$_SC2P_MSGFILE" > "$msg" || { _commit_out="ERROR: could not read the -F file $_SC2P_MSGFILE"; return 1; }
  else
    { k=0; for m in "${_SC2P_MSGS[@]}"; do [ "$k" -gt 0 ] && printf '\n\n'; printf '%s' "$m"; k=$((k + 1)); done; printf '\n'; } > "$msg"
  fi
  out="${out}$(GIT_EDITOR=false git hook run --ignore-missing prepare-commit-msg -- "$msg" message 2>&1)" || rc=$?
  if [ "$rc" -ne 0 ]; then _commit_out="$out"; return 1; fi
  out="${out}$(GIT_EDITOR=false git hook run --ignore-missing commit-msg -- "$msg" 2>&1)" || rc=$?
  if [ "$rc" -ne 0 ]; then _commit_out="$out"; return 1; fi
  git stripspace < "$msg" > "$msg.clean" || { _commit_out="ERROR: git stripspace failed"; return 1; }
  if [ ! -s "$msg.clean" ]; then _commit_out="${out}"$'\n'"Aborting commit due to empty commit message."; return 1; fi
  IFS= read -r subject < "$msg.clean" || true
  # (V3) the validated entries: index vs BASE, limited exactly as `commit --only -- PATHSPEC EXCLUDES` limits it.
  if ! git diff --cached --raw -z --no-renames --no-abbrev "$_SC2P_BASE" -- "${PATHSPEC[@]}" "${COMMIT_EXCLUDES[@]}" > "$_SC2P_DIR/raw"; then
    _commit_out="${out}"$'\n'"ERROR: could not list the staged entries"; return 1
  fi
  : > "$_SC2P_DIR/info"; : > "$_SC2P_DIR/paths"
  while IFS= read -r -d '' meta && IFS= read -r -d '' path; do
    read -r _o_m _n_m _o_s _n_s _st <<< "$meta"
    printf '%s %s\t%s\0' "$_n_m" "$_n_s" "$path" >> "$_SC2P_DIR/info"
    printf '%s\0' "$path" >> "$_SC2P_DIR/paths"
    _mine["$path"]=1
    n=$((n + 1))
  done < "$_SC2P_DIR/raw"
  if [ "$n" -eq 0 ]; then _commit_out="${out}"$'\n'"nothing to commit: no change under the pathspec"; return 1; fi
  t_v1="$EPOCHREALTIME"

  # (L) land. Back to the real git dir, index and HEAD.
  unset GIT_DIR GIT_WORK_TREE
  _sc_take_lock
  t_l1="$EPOCHREALTIME"
  if [ -f "$(git rev-parse --git-path MERGE_HEAD 2>/dev/null)" ]; then
    _sc_release_lock
    echo "${ISO_TS} MERGE-REFUSED-LATE  ${AGENT:-UNKNOWN}  ${n}  (two-phase: a merge opened before the land; nothing landed)" >> "$AUDIT_LOG" 2>/dev/null || true
    _commit_out="${out}"$'\n'"safe-commit: REFUSED -- a merge is open in this worktree; nothing landed. Re-run after it lands."
    return 3
  fi
  cur="$(git rev-parse --verify HEAD)"
  if [ "$cur" != "$_SC2P_BASE" ]; then
    while IFS= read -r -d '' path; do
      if [ -n "${_mine[$path]+x}" ]; then overlap="${overlap}${overlap:+ }${path}"; fi
    done < <(git diff --name-only -z --no-renames "$_SC2P_BASE" "$cur" 2>/dev/null)
  fi
  if [ -n "$overlap" ]; then
    _sc_release_lock
    att="${SAFE_COMMIT_2P_ATTEMPT:-1}"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) RETRY-2P  ${AGENT:-UNKNOWN}  attempt=${att}  same-path=(${overlap})" >> "$AUDIT_LOG" 2>/dev/null || true
    if [ "$att" -ge 3 ]; then
      _commit_out="${out}"$'\n'"safe-commit: REFUSED -- commits that landed during validation changed the same path(s) on 3 attempts: ${overlap}. Nothing landed; re-run."
      return 3
    fi
    echo "safe-commit: two-phase -- a commit that landed after this run's base changed the same path(s): ${overlap}. Re-validating (attempt $((att + 1)) of 3)." >&2
    rm -rf "$_SC2P_DIR" 2>/dev/null || true; _SC2P_DIR=""
    unset GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL
    exec env SAFE_COMMIT_2P_ATTEMPT=$((att + 1)) bash "$0" "${_SC_ORIG_ARGS[@]}"
  fi
  if ! GIT_INDEX_FILE="$_SC2P_DIR/land.index" git read-tree "$cur" \
     || ! GIT_INDEX_FILE="$_SC2P_DIR/land.index" git update-index -z --index-info < "$_SC2P_DIR/info"; then
    _sc_release_lock; _commit_out="${out}"$'\n'"ERROR: two-phase land could not build the tree; nothing landed."; return 1
  fi
  tree="$(GIT_INDEX_FILE="$_SC2P_DIR/land.index" git write-tree)" || { _sc_release_lock; _commit_out="${out}"$'\n'"ERROR: git write-tree failed; nothing landed."; return 1; }
  if [ "$tree" = "$(git rev-parse "${cur}^{tree}")" ]; then
    _sc_release_lock; _commit_out="${out}"$'\n'"nothing to commit: the tip already holds this content"; return 1
  fi
  t_b="$EPOCHREALTIME"
  commit="$(git commit-tree "$tree" -p "$cur" -F "$msg.clean")" || { _sc_release_lock; _commit_out="${out}"$'\n'"ERROR: git commit-tree failed; nothing landed."; return 1; }
  if ! git update-ref -m "commit: ${subject}" HEAD "$commit" "$cur"; then
    _sc_release_lock; _commit_out="${out}"$'\n'"ERROR: the branch moved under the land lock (a writer outside safe-commit?); nothing landed. Commit object ${commit} is unreferenced."; return 3
  fi
  # The shared index: set this commit's paths to the committed entries (pathspec from a NUL file: no argv cliff).
  for k in 1 2 3 4 5; do
    if GIT_LITERAL_PATHSPECS=1 git reset -q "$commit" --pathspec-from-file="$_SC2P_DIR/paths" --pathspec-file-nul 2>/dev/null; then k=0; break; fi
    sleep "$k"
  done
  if [ "$k" -ne 0 ]; then
    echo "WARN: commit ${commit:0:10} LANDED, but the shared index was not updated for its paths. Run: git reset -q HEAD -- <your paths>" >&2
  fi
  t_r="$EPOCHREALTIME"
  _sc_release_lock
  t_l2="$EPOCHREALTIME"
  pc_dir="${_SC2P_REAL_GITDIR}/sc2p-pc-${EPOCHSECONDS:-0}-$$"
  if mkdir -p "$pc_dir" && printf '%s
' "$commit" > "$pc_dir/HEAD" && printf '%s
' "$_SC2P_COMMON" > "$pc_dir/commondir"; then
    pc_out="$(GIT_DIR="$pc_dir" GIT_WORK_TREE="$_SC2P_WT" GIT_INDEX_FILE="$_SC2P_REAL_INDEX" git hook run --ignore-missing post-commit 2>&1)" || true
  else
    pc_out="WARN: could not pin a post-commit view; post-commit hook NOT run for ${commit:0:10}"
  fi
  t_l3="$EPOCHREALTIME"
  branch="$(git symbolic-ref --short -q HEAD 2>/dev/null || echo HEAD)"
  stat="$(git diff --shortstat "$cur" "$commit" 2>/dev/null || true)"
  _commit_out="${out:+${out}$'\n'}[${branch} ${commit:0:10}] ${subject}"$'\n'"${stat}${pc_out:+$'\n'${pc_out}}"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) LANDED-2P  ${AGENT:-UNKNOWN}  ${commit:0:10}  paths=${n}  validate=$(_sc2p_s "$_SC2P_T0" "$t_v1")s  wait=$(_sc2p_s "$t_v1" "$t_l1")s  hold=$(_sc2p_s "$t_l1" "$t_l2")s  build=$(_sc2p_s "$t_l1" "$t_b")s  ref=$(_sc2p_s "$t_b" "$t_r")s  post-commit=$(_sc2p_s "$t_l2" "$t_l3")s  attempt=${SAFE_COMMIT_2P_ATTEMPT:-1}" >> "$AUDIT_LOG" 2>/dev/null || true
  return 0
}
# seconds between two EPOCHREALTIME stamps, 2 decimals, no subprocess
_sc2p_s() {
  local a="${1/[.,]/}" b="${2/[.,]/}" d
  d=$(( (10#$b - 10#$a) / 10000 ))
  printf '%d.%02d' $((d / 100)) $((d % 100))
}

# ==========================================================================
# LEGACY PATH (default; also the D6 fallback for worker-down / enqueue-fail).
# PRESERVED byte-for-byte from the pre-queue safe-commit.sh, EXCEPT the
# sensitive-leak detection now calls the SHARED cg_sensitive_hits (no drift).
# ==========================================================================
# LOCK RECLAIM BY LIVENESS (GitOps F2; 1.0.0_SA_CTO FAST_FIX_RULINGS_20261008_162xZ.md item 7). The old loop deleted the
# lock once its DIRECTORY was 60 s old; nothing refreshed that mtime, so a LIVE holder whose gates ran past 60 s lost
# its lock and two commits shared one index, with no log row. Now a waiter reclaims only when (a) the holder pid is
# dead, (b) no pid file appeared for 10 polls, or (c) it has watched the SAME live holder for LOCK_STALE_SEC, counted
# by its own loop and never by mtime. Every reclaim appends LOCK-RECLAIM, every waited acquisition LOCK-WAIT, to
# AUDIT_LOG. The wait is `read -t 1` on a held-open FIFO (no process per poll; inbox-watch.sh's _wait5 pattern), with
# `sleep 1` as the fallback. Harness: extract this block (LOCK_DIR= .. LOCK_ACQUIRED=1) and source it.
_sc_take_lock() {   # the legacy path calls this here; the two-phase path calls it at its land step
LOCK_DIR="${SAFE_COMMIT_LOCK_DIR:-$(git rev-parse --absolute-git-dir 2>/dev/null)/commit-queue.lock}"
LOCK_TIMEOUT_SEC="${SAFE_COMMIT_LOCK_TIMEOUT:-300}"
LOCK_STALE_SEC="${SAFE_COMMIT_LOCK_STALE_SEC:-240}"   # 240 < the 300 s give-up, so (c) can fire (CTO msg 106996)
LOCK_ACQUIRED=0
elapsed=0
_lk_nopid=0
_lk_same=""
_lk_same_n=0
_lk_fd=0
_lk_reclaim() {   # $1 holder seen, $2 reason; re-read first so a lock a peer just re-took is never removed
  local _now=""
  if [ -f "$LOCK_DIR/pid" ]; then read -r _now < "$LOCK_DIR/pid" 2>/dev/null || true; fi
  if [ "$1" != "none" ] && [ -n "$_now" ] && [ "$_now" != "$1" ]; then return 0; fi
  if [ "$1" = "none" ] && [ -n "$_now" ]; then return 0; fi
  rm -rf "$LOCK_DIR" 2>/dev/null || true
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) LOCK-RECLAIM  ${AGENT:-UNKNOWN}  holder=$1  reason=$2  waiter=$$" >> "$AUDIT_LOG" 2>/dev/null || true
  return 0
}
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  if [ "$_lk_fd" -eq 0 ]; then
    _lk_fd=2   # 2 = tried; 1 = FIFO open
    _lk_fifo="${TMPDIR:-/tmp}/safe-commit-wait.$$"
    if mkfifo "$_lk_fifo" 2>/dev/null; then
      if exec 9<>"$_lk_fifo"; then _lk_fd=1; fi
      rm -f "$_lk_fifo" 2>/dev/null || true
    fi
  fi
  _lk_holder=""
  if [ -f "$LOCK_DIR/pid" ]; then read -r _lk_holder < "$LOCK_DIR/pid" 2>/dev/null || true; fi
  if [ -n "$_lk_holder" ]; then
    _lk_nopid=0
    if ! kill -0 "$_lk_holder" 2>/dev/null; then
      _lk_reclaim "$_lk_holder" "holder-dead"
      continue
    fi
    if [ "$_lk_holder" = "$_lk_same" ]; then _lk_same_n=$((_lk_same_n + 1)); else _lk_same="$_lk_holder"; _lk_same_n=0; fi
    if [ "$_lk_same_n" -ge "$LOCK_STALE_SEC" ]; then
      _lk_reclaim "$_lk_holder" "live-holder-${_lk_same_n}-polls"
      _lk_same_n=0
      continue
    fi
  else
    _lk_nopid=$((_lk_nopid + 1))
    if [ "$_lk_nopid" -ge 10 ]; then
      _lk_reclaim "none" "no-pid-file-10-polls"
      _lk_nopid=0
      continue
    fi
  fi
  elapsed=$((elapsed + 1))
  if [ "$elapsed" -ge "$LOCK_TIMEOUT_SEC" ]; then
    echo "ERROR: safe-commit mutex held >${LOCK_TIMEOUT_SEC}s by PID ${_lk_holder:-unknown}." >&2
    echo "       Other agent's commit stuck or hung. Inspect $LOCK_DIR." >&2
    exit 3
  fi
  if [ "$_lk_fd" -eq 1 ]; then read -r -t 1 -u 9 _lk_x || true; else sleep 1; fi
done
if [ "$_lk_fd" -eq 1 ]; then exec 9<&- || true; fi
echo "$$" > "$LOCK_DIR/pid"
if [ "$elapsed" -gt 0 ]; then
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) LOCK-WAIT  ${AGENT:-UNKNOWN}  ${elapsed}s" >> "$AUDIT_LOG" 2>/dev/null || true
fi
LOCK_ACQUIRED=1
trap '_sc_on_exit' EXIT
}
if [ "$_SC_2P" -eq 0 ]; then _sc_take_lock; fi

# (1) BASELINE: what was already staged at lock-entry (foreign + any caller pre-add).
BASELINE="$(git diff --cached --name-only 2>/dev/null || true)"
declare -A BASELINE_SET=()
if [ -n "$BASELINE" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    BASELINE_SET["$f"]=1
  done <<< "$BASELINE"
fi

# OPEN-MERGE PATHS (row NFRA_OPLGTW-Z-S61, 0.0.0_AB_MSTR~Z 2026-10-07). The refusal-residue loops below unstage
# "staged-now MINUS the lock-entry BASELINE". A drain that OPENS after the baseline stages its own paths into the
# shared index, so that subtraction attributes them to THIS call; and git refuses `commit --only` during a merge, so
# this call fails and the loop resets the merge's paths to the pre-merge HEAD. safe-merge.sh then commits from its
# private index: HEAD carries the merge, the shared index holds the old blobs, and they read as staged reverts nobody
# made. Reproduced in a scratch repo (2 of 2 merged paths stale). Called at residue time, never cached: the merge
# may open or land at any point after the baseline. Paths in this set are LEFT STAGED and counted, never reset.
declare -A _OPEN_MERGE_SET=()
_load_open_merge_set() {
  _OPEN_MERGE_SET=()
  local _mh _p
  _mh="$(git rev-parse --git-path MERGE_HEAD 2>/dev/null || echo "")"
  [ -n "$_mh" ] && [ -f "$_mh" ] || return 0
  while IFS= read -r _p; do if [ -n "$_p" ]; then _OPEN_MERGE_SET["$_p"]=1; fi; done < <(git diff --name-only HEAD MERGE_HEAD 2>/dev/null || true)
  return 0   # set -e is on: this helper must never be the reason a refusal path exits early
}

# (2) Stage our declared pathspec inside the lock (-f past .gitignore).
#
# The staging error must NOT be swallowed. A failed `git add` here -- index.lock
# contention from a concurrent lane on the shared worktree -- used to pass
# silently, and step (5)'s `git commit --only -- PATHSPEC` then aborted with
#     pathspec 'X' did not match any file(s) known to git
# pointing the agent at their OWN PATH instead of at the lock. The suppression
# did not merely hide an error, it MANUFACTURED a false one -- and a misleading
# claim is worse than a silent one (CTO 20260709T195435Z). Observed 3x on
# 2026-07-09 while MSTR held the shared index; a bare retry fixed it every time.
#
# Retry ONLY on lock contention (transient -- other lanes commit in seconds).
# Any other failure (bad pathspec, permissions) surfaces immediately: it is not
# transient, and retrying only delays a true error behind a false one.
ADD_ERR=""
ADD_OK=0
for attempt in 1 2 3 4 5; do
  # cg_stage_pathspec (commit_gate_lib.sh, pure-deletion TO): ONE measured branch
  # per path -- pure deletions stage via `add -A`, already-staged deletions no-op
  # (re-adding them fatals rc=128), pycache artifacts are excluded loud, everything
  # else keeps the existing `add -f`. Untracked+missing still fails loud below.
  if ADD_ERR="$(cg_stage_pathspec "${PATHSPEC[@]}" 2>&1)"; then
    ADD_OK=1
    break
  fi
  case "$ADD_ERR" in
    *index.lock*|*"Unable to create"*|*"File exists"*)
      [ "$attempt" -lt 5 ] && sleep "$attempt"   # 1s,2s,3s,4s backoff (Rule 16: no flock)
      ;;
    *)
      break
      ;;
  esac
done
if [ "$ADD_OK" -ne 1 ]; then
  echo "ERROR: safe-commit could not stage the declared pathspec. Commit aborted." >&2
  echo "       git add reported:" >&2
  printf '       %s\n' "$ADD_ERR" >&2
  echo "" >&2
  echo "  If that mentions index.lock: a concurrent lane holds the shared index." >&2
  echo "  Transient -- retry. (safe-commit already retried 5x over ~10s.)" >&2
  echo "  Otherwise the pathspec itself is the problem, and THIS is the real error," >&2
  echo "  not the 'pathspec did not match' you would previously have seen." >&2
  exit 1
fi
# Re-emit git's own non-fatal chatter (e.g. CRLF warnings) that 2>&1 captured.
[ -n "$ADD_ERR" ] && printf '%s\n' "$ADD_ERR" >&2

# (2b) RE-CHECK FOR A MERGE AFTER STAGING (DSGN_AMGTV1 round 7: 6fcaa52f79 swept 14 of this kind of file). The merge
# check above ran BEFORE staging; a drain that opened in between would carry what we just staged under ITS author.
# Unstage exactly what this run added that the merge does not itself touch, and refuse as the pre-check does.
if [ -n "$_MERGE_HEAD_PATH" ] && [ -f "$_MERGE_HEAD_PATH" ]; then
  _merge_own="$(git diff --name-only HEAD MERGE_HEAD 2>/dev/null || true)"
  declare -A _MERGE_OWN_SET=()
  while IFS= read -r f; do [ -n "$f" ] && _MERGE_OWN_SET["$f"]=1; done <<< "$_merge_own"
  _undo=(); _clash=()
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    [ -n "${BASELINE_SET[$f]:-}" ] && continue
    if [ -n "${_MERGE_OWN_SET[$f]:-}" ]; then _clash+=("$f"); else _undo+=("$f"); fi
  done <<< "$(git diff --cached --name-only -- "${PATHSPEC[@]}" 2>/dev/null || true)"
  if [ "${#_undo[@]}" -gt 0 ]; then git restore --staged -- "${_undo[@]}" 2>/dev/null || true; fi
  echo "safe-commit: REFUSED -- a merge OPENED in this worktree while this run was staging (MERGE_HEAD $(head -c 12 "$_MERGE_HEAD_PATH" 2>/dev/null))." >&2
  echo "             Unstaged this run's ${#_undo[@]} path(s); your working copies are untouched. Re-run after the merge lands." >&2
  if [ "${#_clash[@]}" -gt 0 ]; then
    echo "             ${#_clash[@]} path(s) are ALSO part of the merge -- this run's staging replaced the merge's version; tell the merging seat:" >&2
    printf '               %s\n' "${_clash[@]}" >&2
  fi
  echo "${ISO_TS} MERGE-REFUSED-LATE  ${AGENT:-UNKNOWN}  ${#_undo[@]}  (merge opened during staging; unstaged; clash=${#_clash[@]})" >> "$AUDIT_LOG" 2>/dev/null || true
  exit 3
fi

# (3) IN_SCOPE: git-expanded files matching our declared pathspec.
IN_SCOPE="$(git diff --cached --name-only -- "${PATHSPEC[@]}" 2>/dev/null || true)"
declare -A IN_SCOPE_SET=()
if [ -n "$IN_SCOPE" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    IN_SCOPE_SET["$f"]=1
  done <<< "$IN_SCOPE"
fi

# SENSITIVE-LEAK GATE (fail-closed) via the SHARED detector (TO-5, no copy-drift).
LEAK_HITS=()
if [ -n "$IN_SCOPE" ]; then
  while IFS= read -r f; do
    [ -n "$f" ] && LEAK_HITS+=("$f")
  done <<< "$(cg_sensitive_hits "$IN_SCOPE")"
fi
if [ "${#LEAK_HITS[@]}" -gt 0 ]; then
  mkdir -p "$(dirname "$AUDIT_LOG")"
  if [ -n "${SAFE_COMMIT_ALLOW_SENSITIVE:-}" ]; then
    echo "${ISO_TS} SENSITIVE-OVERRIDE  ${AGENT}  ${#LEAK_HITS[@]}  (${LEAK_HITS[*]})  reason=${SAFE_COMMIT_ALLOW_SENSITIVE}" >> "$AUDIT_LOG"
    echo "WARN: SAFE_COMMIT_ALLOW_SENSITIVE override -- ${#LEAK_HITS[@]} sensitive file(s) WILL be committed:" >&2
    printf '  %s\n' "${LEAK_HITS[@]}" >&2
    echo "  Audit: ${AUDIT_LOG}" >&2
  else
    git reset -q HEAD -- "${LEAK_HITS[@]}" 2>/dev/null || true
    echo "${ISO_TS} SENSITIVE-BLOCK  ${AGENT}  ${#LEAK_HITS[@]}  (${LEAK_HITS[*]})" >> "$AUDIT_LOG"
    echo "ERROR: BLOCKED -- the pathspec would commit SENSITIVE file(s) (secret/PII leak risk)." >&2
    echo "       safe-commit uses 'git add -f', which OVERRIDES .gitignore -- a DIRECTORY pathspec" >&2
    echo "       force-adds gitignored secrets. A leaked live credential or client PII is" >&2
    echo "       UNRECOVERABLE from git history." >&2
    echo "" >&2
    echo "Would-be-leaked (${#LEAK_HITS[@]}) -- now UNSTAGED for you:" >&2
    printf '  %s\n' "${LEAK_HITS[@]}" >&2
    echo "" >&2
    echo "Fix: pass EXPLICIT non-sensitive file paths -- never a directory pathspec that sweeps these in." >&2
    echo "     Verify with: git show --name-only HEAD  (before pushing near a sources/HAR/.env tree)." >&2
    echo "     Genuine sanitized fixture? SAFE_COMMIT_ALLOW_SENSITIVE=\"reason\" (audited)." >&2
    exit 1
  fi
fi

# Contamination = staged-now files NEITHER in the in-scope set NOR in the baseline.
STAGED="$(git diff --cached --name-only 2>/dev/null || true)"
EXTRA=()
if [ -n "$STAGED" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ -z "${IN_SCOPE_SET[$f]+x}" ] && [ -z "${BASELINE_SET[$f]+x}" ]; then
      EXTRA+=("$f")
    fi
  done <<< "$STAGED"
fi

N_EXTRA="${#EXTRA[@]}"

if [ "$N_EXTRA" -gt 0 ]; then
  if [ "$FORCE" -eq 1 ]; then
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

# LOG-COMMIT SOURCE-SWEEP GUARD (fail-closed; AMENDMENT-2, CTO ratified 190021Z).
# A log(-class commit (session-log commit) whose staged set DELETES paths OUTSIDE
# the session-log/org-record surface REFUSES loud, per-path -- the ES-1 class
# (64b6b9d65 deleted 15 exec-summary source files under a "log(...)" subject and
# sat unnoticed 11 weeks). Detection is the shared cg_log_sweep_offenders (no
# drift with the worker). Audited override: SAFE_COMMIT_ALLOW_LOG_DELETIONS.
_SC_SUBJECT="$(cg_extract_subject "${COMMIT_ARGS[@]}")"
_SC_DELS="$(git diff --cached --diff-filter=D --name-only -- "${PATHSPEC[@]}" 2>/dev/null || true)"
LOG_SWEEP=()
if [ -n "$_SC_DELS" ]; then
  while IFS= read -r _f; do
    [ -n "$_f" ] && LOG_SWEEP+=("$_f")
  done <<< "$(cg_log_sweep_offenders "$_SC_SUBJECT" "$_SC_DELS")"
fi
if [ "${#LOG_SWEEP[@]}" -gt 0 ]; then
  mkdir -p "$(dirname "$AUDIT_LOG")"
  if [ -n "${SAFE_COMMIT_ALLOW_LOG_DELETIONS:-}" ]; then
    echo "${ISO_TS} LOG-SWEEP-OVERRIDE  ${AGENT}  ${#LOG_SWEEP[@]}  (${LOG_SWEEP[*]})  reason=${SAFE_COMMIT_ALLOW_LOG_DELETIONS}" >> "$AUDIT_LOG"
    echo "WARN: SAFE_COMMIT_ALLOW_LOG_DELETIONS override -- a log( commit is deleting ${#LOG_SWEEP[@]} non-log/non-org path(s):" >&2
    printf '  %s\n' "${LOG_SWEEP[@]}" >&2
    echo "  Audit: ${AUDIT_LOG}" >&2
  else
    # Unstage the offending deletions (mirror the sensitive/contamination reject:
    # a BLOCKED request must not leave its deletions staged for a later inherit).
    for _f in "${LOG_SWEEP[@]}"; do git reset -q HEAD -- "$_f" 2>/dev/null || true; done
    echo "${ISO_TS} LOG-SWEEP-BLOCK  ${AGENT}  ${#LOG_SWEEP[@]}  (${LOG_SWEEP[*]})" >> "$AUDIT_LOG"
    echo "ERROR: BLOCKED -- a log( session-log commit is DELETING source/infra path(s) outside the log/org-record surface." >&2
    echo "       This is the ES-1 class: commit 64b6b9d65 deleted 15 exec-summary source files under a" >&2
    echo "       \"log(...)\" subject and sat unnoticed 11 weeks (Rule-10 rebuild hole). A session-log commit" >&2
    echo "       should ADD a log + touch org records, never sweep source." >&2
    echo "" >&2
    echo "Offending deletion(s) (${#LOG_SWEEP[@]}) -- now UNSTAGED for you:" >&2
    printf '  %s\n' "${LOG_SWEEP[@]}" >&2
    echo "" >&2
    echo "Fix: commit the deletions in a SEPARATE, honestly-subjected commit (fix/chore/refactor)," >&2
    echo "     not under a log( subject. Legitimately-intended mixed commit?" >&2
    echo "     SAFE_COMMIT_ALLOW_LOG_DELETIONS=\"reason\" (audited)." >&2
    exit 1
  fi
fi

# surface-check gate REMOVED 2026-08-06 -- comp-surface-check RETIRED (Andrew-direct,
# "I want comp-surface-check retired. i do not like that tool."). The invocation was
# advisory + command-v guarded + `|| true`, so it failed OPEN; removing it changes no
# blocking behaviour here. The ENFORCING half lived in the portal repo, retired with it.

# Advisory NERVES risk reflex (NFRA_NERVES L5; QUERY-only; never blocks). Scores the staged set
# against the danger map -- a staged file under a recorded HOLD/RISK prints its citation HERE,
# before the commit, instead of relying on the author having read the prose.
if command -v comp-pulse >/dev/null 2>&1 && [ -n "$IN_SCOPE" ]; then
  _rr_args=()
  while IFS= read -r _f; do
    [ -z "$_f" ] && continue
    _rr_args+=("$_f")
  done <<< "$IN_SCOPE"
  if [ ${#_rr_args[@]} -gt 0 ]; then
    comp-pulse diff "${_rr_args[@]}" 2>&1 \
      | sed 's/^/  [risk-reflex] /' || true
  fi
fi

# BLOCKING comp-coverage-check gate (COMPUNIFY S2). Flipped advisory->blocking 2026-07-28
# (3.0.0_SA_CVO, Andrew-direct) on a measured basis: 538ms fixed cost, does NOT scale with commit
# size, tri-state with an honest UNVERIFIABLE, and its own selfcheck demonstrates it FAILS on
# injected defects (an unplaced tool / silent overlap / stale projection) -- i.e. it can fail, so
# its PASS carries information.
#
# >> THE DEFECT THIS ALSO CLOSES, and it is the reason the `command -v` guard is no longer a silent
# skip: comp-coverage-check WAS NOT ON PATH (only 4 of 92 comp-tools resolved bare before the
# 2026-07-28 forwarder widening). `command -v` returned false, the whole block was skipped, and
# THE GATE REPORTED NOTHING WHILE BEING OFF -- on every commit, indefinitely. A gate that cannot be
# FOUND is not advisory, it is absent, and absence looked exactly like a pass. Never let a missing
# gate binary be silent again.
if [ -n "$IN_SCOPE" ] && echo "$IN_SCOPE" | grep -qE 'comp-coverage-map\.yaml|\.tools/comp-'; then
  if ! command -v comp-coverage-check >/dev/null 2>&1; then
    # LOUD, not silent. Cannot block on a missing binary (that would wedge every commit on a
    # machine that never provisioned the shims) -- but it must never again pass unremarked.
    echo "  [coverage-check] WARN: comp-coverage-check NOT ON PATH -- the COMPUNIFY gate did NOT" >&2
    echo "  [coverage-check]       run for this commit. Fix: bash .tools/provision-path-shims.sh" >&2
  else
    _cc_out="$(comp-coverage-check check 2>&1)" && _cc_rc=0 || _cc_rc=$?
    printf '%s\n' "$_cc_out" | sed 's/^/  [coverage-check] /'
    if [ "$_cc_rc" -eq 1 ]; then
      echo "BLOCKED: comp-coverage-check FAIL -- the comp-tool coverage map has drifted from the" >&2
      echo "  territory (unplaced tool / silent overlap / phantom seam / stale projection /" >&2
      echo "  incomplete inventory). The offending node is NAMED above. Fix the map, then re-commit." >&2
      exit 1
    elif [ "$_cc_rc" -eq 2 ]; then
      # UNVERIFIABLE (rc=2) = THE GATE ITSELF IS BROKEN (ledger unreadable, or a gate_contract rule
      # has no checker) -- NOT that the map is bad. DELIBERATE ASYMMETRY: rc=1 BLOCKS, rc=2 WARNS.
      #
      # WHY NOT BLOCK ON rc=2. Blocking would wedge EVERY in-scope commit fabric-wide the moment the
      # gate broke -- converting a broken instrument into a self-inflicted outage. Today already
      # produced the inverse defect (this gate silently OFF for want of a PATH entry); shipping a
      # gate-wedge tonight would just be the same mistake mirrored.
      #
      # IT IS STILL NOT A PASS. It prints UNVERIFIABLE on stderr on EVERY in-scope commit until
      # fixed -- loud, repeated, and impossible to mistake for a clean run. Per the tool's own
      # tri-state doctrine and CVO's: could-not-verify is a FINDING, and a finding that shouts on
      # every commit is not a silent one.
      #
      # (An audited-override form was written first and REMOVED: it keyed on $COMMIT_MSG_RAW, a
      # variable that DOES NOT EXIST in this script -- the real message extraction builds CS_MSG
      # ~90 lines further down. The override could never have matched. A dead escape hatch that
      # reads as a live one is worse than no escape hatch, so it is gone rather than plausible.)
      echo "  [coverage-check] UNVERIFIABLE (rc=2) -- THE GATE COULD NOT EVALUATE ITSELF." >&2
      echo "  [coverage-check]   The ledger was unreadable, or a gate_contract rule has no checker." >&2
      echo "  [coverage-check]   This is NOT a pass. It does not block (a broken gate must not wedge" >&2
      echo "  [coverage-check]   the fabric) -- but it will print on every in-scope commit until fixed." >&2
    fi
  fi
fi

# UNIVERSAL FAIL-CLOSED commit-gate re-assert (CTO-called 2026-07-09, ADHC_COMMITGATE
# universal-enforcement). THE DEFECT this closes: the gate (commit-gate.sh -> py_compile +
# ruff + the universal lints) was ENFORCED (blocking) only on the QUEUE-worker path
# (commit-worker.sh F2) + the pipeline-scoped safe-deploy pre-push -- so a failing
# NON-pipeline .py committed via THIS legacy path (the default) with nothing stopping it
# (git has no opinion on Python; the agent-side commit-gate.sh is advisory). A ruff-F541
# .tools/*.py landed exactly this way (18c92b9ac). Re-asserting the SAME gate here, fail-
# closed, on ALL in-scope files makes enforcement UNIVERSAL, matching the worker path.
# CTO (verbatim, 0.5.0's principle): "a gate that reports failure into a pipeline whose exit
# status is swallowed is a gate that does not gate; the gate that stops you is the one whose
# exit code reaches a decision." The CHECK-SET stays file-type-appropriate INSIDE the runner
# (ds-precommit silver-ids self-scopes to data/*/scripts/silver/*.py via _path_is_silver_builder;
# a .tools/*.py runs py_compile + ruff + the universal lints only -> NO silver-ids false-fail,
# verified). --force does NOT bypass a gate FAILURE (only the contamination/sensitive checks
# carry audited bypasses -- a non-compiling/ruff-failing file is never intentional).
if [ -n "$IN_SCOPE" ]; then
  GATE_FILES=()
  while IFS= read -r _gf; do [ -n "$_gf" ] && GATE_FILES+=("$_gf"); done <<< "$IN_SCOPE"
  if [ "${#GATE_FILES[@]}" -gt 0 ]; then
    # AUDIBILITY (1.0.0_SA_CTO 2026-08-26, found by 3.0.0_SA_CVO 72103): GATE_OUT was printed ONLY
    # inside the failure branch below. A WARN-ONLY check ALWAYS RETURNS 0 by design -- so success is
    # exactly the path that threw its warnings away, and warn-only mode was STRUCTURALLY UNABLE TO
    # WARN ANYONE through this wrapper. Live 26 days; zero announcements; 7 self-strips across 6
    # serials by authors who knew the rule. You cannot learn from a gate that never speaks.
    # This PRINTS on both paths. It adds NO gate: nothing new refuses, blocks or checks anything.
    # set-e-safe rc capture, same idiom as :569.
    GATE_OUT=""; GATE_RC=0
    GATE_OUT="$(bash "$SCRIPT_DIR/commit-gate.sh" "${GATE_FILES[@]}" 2>&1)" || GATE_RC=$?
    if [ "$GATE_RC" -ne 0 ]; then
      # Unstage the in-scope files (mirror the sensitive/contamination reject: a BLOCKED
      # request must never leave its files staged for a later invocation to (mis-)inherit).
      for _gf in "${GATE_FILES[@]}"; do git reset -q HEAD -- "$_gf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- commit-gate failed (py_compile / ruff / lint). Commit aborted; files unstaged." >&2
      printf '%s\n' "$GATE_OUT" | sed 's/^/  [commit-gate] /' >&2
      echo "  Fix the reported issue(s) and re-commit. This gate is UNIVERSAL + fail-closed on ALL .py" >&2
      echo "  (Rule 14); --force does NOT bypass a gate failure (it only overrides the contamination check)." >&2
      exit 1
    elif [ -n "$GATE_OUT" ]; then
      # PASSED, but the gate said something (WARN-only findings live here and ONLY here).
      printf '%s
' "$GATE_OUT" | sed 's/^/  [commit-gate] /' >&2
    fi
  fi
fi

# ---------------------------------------------------------------------------------------------
# THE NAMING LIMB (LGIC_ENFORCE cell EN-g-1; PRD candidate E7; DEC-6's matrix and context rule).
# ONE stage. It grades the ADDED lines of the staged graded files (.py .js .mjs .ts .tf .json .yaml .yml)
# with lib/opal_naming.py grade(): a NEW out-of-pattern or alias literal, a NEW hand-kept firm token, an
# edit to a GENERATED file, and an existing out-of-pattern literal in a live remediation's surface are
# REFUSE verdicts; the rest warn or pass. Verdict lines are appended to org/mcp/naming-gate-verdicts.log
# (runtime state, gitignored by *.log, never committed).
# THE WARN WINDOW. ENFORCE is on only when org/mcp/naming-gate.enforce exists or NAMING_GATE_ENFORCE=1.
# In WARN mode this stage NEVER changes this script's exit code -- not on a REFUSE verdict, not on the
# limb's own internal error (NAMING ERROR), not on a crashed interpreter -- because it sits on every
# seat's commit path. In ENFORCE mode it is fail-closed: any non-zero exit unstages and aborts, like the
# commit-gate above. The live flip is gate G-F, outside LGIC_ENFORCE round 1.
if [ -n "$IN_SCOPE" ] && [ -f "$SCRIPT_DIR/naming-gate.py" ]; then
  NGATE_FILES=()
  while IFS= read -r _nf; do
    case "$_nf" in
      *.py|*.js|*.mjs|*.ts|*.tf|*.json|*.yaml|*.yml) NGATE_FILES+=("$_nf") ;;
    esac
  done <<< "$IN_SCOPE"
  if [ "${#NGATE_FILES[@]}" -gt 0 ]; then
    NGATE_ENFORCE=0
    if [ "${NAMING_GATE_ENFORCE:-}" = "1" ] || [ -e "$SCRIPT_DIR/../org/mcp/naming-gate.enforce" ]; then
      NGATE_ENFORCE=1
    fi
    NGATE_DIFF="$(mktemp "${TMPDIR:-/tmp}/naming-gate.XXXXXX" 2>/dev/null || echo "${TMPDIR:-/tmp}/naming-gate.$$.diff")"
    NGATE_OUT=""; NGATE_RC=0
    if git diff --cached --no-color --no-ext-diff -- "${NGATE_FILES[@]}" > "$NGATE_DIFF" 2> "$NGATE_DIFF.err"; then
      NGATE_OUT="$(python "$SCRIPT_DIR/naming-gate.py" --diff "$NGATE_DIFF" --post-from-index 2>&1)" || NGATE_RC=$?
    else
      NGATE_OUT="NAMING ERROR git diff --cached failed: $(head -c 300 "$NGATE_DIFF.err" 2>/dev/null || true)"; NGATE_RC=2
    fi
    rm -f "$NGATE_DIFF" "$NGATE_DIFF.err" 2>/dev/null || true
    if [ "$NGATE_ENFORCE" -eq 1 ] && [ "$NGATE_RC" -ne 0 ]; then
      for _nf in "${NGATE_FILES[@]}"; do git reset -q HEAD -- "$_nf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged." >&2
      printf '%s\n' "$NGATE_OUT" | sed 's/^/  [naming-gate] /' >&2
      exit 1
    elif [ -n "$NGATE_OUT" ]; then
      printf '%s\n' "$NGATE_OUT" | sed 's/^/  [naming-gate] /' >&2
    fi
  fi
fi

# ---------------------------------------------------------------------------------------------
# LAYER 2 of the CANONICAL FABRIC WORKFLOW -- the TO issuance gate.
# Andrew-direct 2026-09-01 (3.0.0_SA_CVO terminal): "re-authorize the three enforcement layers
# and add the stage-3 preflight" / "we need these set up in a manner that they are actually
# mandated" / "I prefer gates and deterministic methodology because anything that is simply
# 'guidance' may dissipate or otherwise be inconsistent over long-running sessions."
#
# WHY HERE: commit-gate.sh reads only .py/.sh/.tf/org/projects/*.json -- a TO is a .md and falls
# through it entirely. safe-commit is the neck every TO must pass (Rule 14a). MEASURED 2026-09-01:
# 130 of 2233 TO files carry a naming <decomp_ref> (5.8%), so layer 1's ENFORCE path -- which is
# BUILT and works -- is inert on 94% of the estate. This gate is what feeds it.
# PROSPECTIVE ONLY: fires on NEWLY-ADDED task_orders/*.md; never refuses an existing TO.
# Fail-closed, and it unstages on refusal exactly like the commit-gate above.
if [ -n "$IN_SCOPE" ]; then
  TOGATE_FILES=()
  while IFS= read -r _tf; do [ -n "$_tf" ] && TOGATE_FILES+=("$_tf"); done <<< "$IN_SCOPE"
  if [ "${#TOGATE_FILES[@]}" -gt 0 ] && [ -f "$SCRIPT_DIR/to-pipeline-gate.py" ]; then
    TOGATE_OUT=""; TOGATE_RC=0
    TOGATE_OUT="$(python "$SCRIPT_DIR/to-pipeline-gate.py" "${TOGATE_FILES[@]}" 2>&1)" || TOGATE_RC=$?
    if [ "$TOGATE_RC" -ne 0 ]; then
      for _tf in "${TOGATE_FILES[@]}"; do git reset -q HEAD -- "$_tf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged." >&2
      printf '%s\n' "$TOGATE_OUT" | sed 's/^/  /' >&2
      exit 1
    elif [ -n "$TOGATE_OUT" ]; then
      printf '%s\n' "$TOGATE_OUT" | sed 's/^/  /' >&2
    fi
  fi
fi

# SURPRISE-CHANNEL ROW GATE (steps 7 + 10; Andrew-direct 2026-09-01 "All recs approved", card 2).
# A NEW investigation row must carry the step-7 trigger's BOTH halves (spec_asserts + world_is); a
# NEW remediation row must carry route + loop_target satisfying the LOCKED MAPPING. Fail-closed.
# PROSPECTIVE BY CONSTRUCTION: the gate diffs row IDS between HEAD and the staged blob and grades
# only ids NEW in this commit -- ~190 legacy rows are never re-graded.
# ⛔ KEYED ON PATHSPEC, **NOT** IN_SCOPE. IN_SCOPE is the .py/.sh gate scope and every channel file
# is .md, so wiring this the way the TO gate above is wired would have produced a gate that never
# fires and reports OK -- the silent-no-op class. Mirrors the comp-system gate's pathspec keying.
if [ ${#PATHSPEC[@]} -gt 0 ] && [ -f "$SCRIPT_DIR/surprise-row-gate.py" ]; then
  SRGATE_FILES=()
  for _sf in "${PATHSPEC[@]}"; do
    case "$_sf" in
      # BOTH ROOTS (2026-09-03, 1.0.0_SA_CTO on 0.0.0_AB_MSTR~Z's site-Z finding, relay 93546): this set keyed on the
      # LEGACY spelling only, so for a TREE project the block below -- and the surprise-row-override reader inside
      # it -- never ran; CVO~Z's L10 slug for NFRA_OPSEC202609 could not carry an audited override and landed by
      # re-entry rows only. The tree spelling is the contract's (PROJECT_TREE.contract.json surprise_channel_glob).
      # ADJUDICATIONS ADDED 2026-09-04 (1.0.0_SA_CTO on 3.0.0_SA_CVO's ESTATE_GOVERNANCE-S4, msg 94260).
      # This set named investigations/ and remediations/ and NOT adjudications/ -- so for an
      # ADJUDICATIONS-ONLY commit the whole block below never ran, which meant the ONLY reader of
      # '# surprise-row-override:' never ran either, and the git hook then refused with no override
      # in hand. THE DOCUMENTED ESCAPE WAS UNREACHABLE ON EXACTLY THE CVO'S OWN L9 DOCUMENT, and it
      # is the one document only that seat writes -- so nobody else could hit it and report it.
      # Same class as the 2026-09-03 tree-spelling fix at the lines above: that one added the tree
      # root and missed this one folder. A pattern list is a DECLARED DOMAIN (Rule 24 i) and the
      # uncovered member has to be hunted, not waited for.
      *org/surprise_channel/*INVESTIGATION_v*|*org/surprise_channel/*REMEDIATION_v*|*org/surprise_channel/*ADJUDICATION_v*|*org/missions/*/surprise-channel/investigations/*|*org/missions/*/surprise-channel/remediations/*|*org/missions/*/surprise-channel/adjudications/*)
        SRGATE_FILES+=("$_sf") ;;
    esac
  done
  if [ "${#SRGATE_FILES[@]}" -gt 0 ]; then
    SRGATE_OUT=""; SRGATE_RC=0
    SRGATE_OUT="$(python "$SCRIPT_DIR/surprise-row-gate.py" "${SRGATE_FILES[@]}" 2>&1)" || SRGATE_RC=$?
    # READ THE OVERRIDE FIRST, INDEPENDENT OF THE STAGE VERDICT (2026-09-11, 1.0.0_SA_CTO on 0.0.0_AB_MSTR
    # 95726 / LD-0549). This reader used to live INSIDE `if [ "$SRGATE_RC" -ne 0 ]`, so it ran only when the
    # stage run above refused. Measured on 8322dd0b31: the stage run graded the SHARED INDEX at one instant
    # (303 rows, 0 new -> a vacuous pass) while the pre-commit hook graded `git commit --only`'s OWN index
    # (306 rows, 3 new -> refused). Two runs of one gate over two populations; the reader sat behind the
    # first's refusal and never ran, so no audit line, no export, and the hook refused with nothing in hand
    # -- the documented escape hatch was disabled by a pass. A vacuous green must not disarm the hatch: the
    # override is extracted whenever a channel file is in the pathspec, and if present it is audited and
    # exported whatever the stage run said. The hook honours it only if IT finds a violation; an override
    # declared for a commit the hook admits costs one audit line and nothing else.
    # Reads the ACTUAL commit message, -m AND -F, mirroring the system-current-override extractor below.
    # (The first cut of this block referenced a $COMMIT_MSG_BODY that DOES NOT EXIST ANYWHERE IN THIS SCRIPT
    # -- under `set -euo pipefail` that aborts, and it aborts ONLY on the refusal path, i.e. exactly when the
    # gate matters. A NEW reference to an EXISTING-LOOKING variable is a claim that needs checking.)
    SR_MSG=""; _srk=0
    while [ $_srk -lt ${#COMMIT_ARGS[@]} ]; do
      _sra="${COMMIT_ARGS[$_srk]}"; _srf=""
      if [ "$_sra" = "-m" ] && [ $((_srk + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
        SR_MSG="${SR_MSG}"$'\n'"${COMMIT_ARGS[$((_srk + 1))]}"; _srk=$((_srk + 2)); continue
      elif { [ "$_sra" = "-F" ] || [ "$_sra" = "--file" ]; } && [ $((_srk + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
        _srf="${COMMIT_ARGS[$((_srk + 1))]}"; _srk=$((_srk + 2))
      elif [ "${_sra#--file=}" != "$_sra" ]; then
        _srf="${_sra#--file=}"; _srk=$((_srk + 1))
      else
        _srk=$((_srk + 1)); continue
      fi
      if [ -n "$_srf" ] && [ "$_srf" != "-" ] && [ -f "$_srf" ]; then
        SR_MSG="${SR_MSG}"$'\n'"$(cat -- "$_srf" 2>/dev/null || true)"
      fi
    done
    SR_OVR="$(printf '%s' "$SR_MSG" | sed -n 's/^[[:space:]]*#\{0,1\}[[:space:]]*surprise-row-override:[[:space:]]*//p' | head -1)"
    if [ -n "$SR_OVR" ]; then
      mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true
      echo "${ISO_TS} SURPRISE-ROW-OVERRIDE  ${AGENT}  reason=${SR_OVR}" >> "$AUDIT_LOG" 2>/dev/null || true
      if [ "$SRGATE_RC" -ne 0 ]; then
        echo "WARN: surprise-row-gate OVERRIDDEN (audited): ${SR_OVR}" >&2
        printf '%s\n' "$SRGATE_OUT" | sed 's/^/  /' >&2
      else
        echo "WARN: surprise-row-gate: the stage run PASSED but the message declares an override -- audited and exported anyway, so the hook's run (which grades the commit's OWN index, not the shared one) honours it if IT refuses: ${SR_OVR}" >&2
        [ -n "$SRGATE_OUT" ] && printf '%s\n' "$SRGATE_OUT" | sed 's/^/  /' >&2
      fi
      # CARRY THE AUDITED OVERRIDE TO THE HOOK (2026-09-03, 1.0.0_SA_CTO~Z's measurement via 0.0.0_AB_MSTR~Z 93575,
      # landed at the base): this stage audits and warns, but .git/hooks/pre-commit block 10 re-runs the gate with no
      # knowledge of the message and exits 1 regardless -- so the audited override never worked on ANY path. The gate
      # honours this variable (prints the violations as WARN, exits 0) and ONLY safe-commit sets it, after the audit
      # line above; a raw `git commit` has no such variable and stays refused, which is the asymmetry the installer
      # exists to close. Scoped to this process: git inherits it for the hook, nothing else does.
      export SURPRISE_ROW_OVERRIDE="${SR_OVR}"
    elif [ "$SRGATE_RC" -ne 0 ]; then
      # NFRA_OPLGTW Z-S46 / Z-S50 (3.0.0_SA_CVO~O msgs 29037, 29046): this branch exits before the REMAIN STAGED
      # post-check below, so it makes the same check itself, over the SAME set: everything THIS call staged (staged-now
      # MINUS the lock-entry BASELINE), not only the gate files -- a non-gate path in the pathspec is staged too. A file
      # still staged after the reset is REPORTED, never claimed unstaged; a failed read counts as still staged, and an
      # unreadable index is said out loud (an empty listing must never read as "nothing left").
      _sr_reset=0; _sr_stuck=0; _sr_merge=0
      _load_open_merge_set
      _sr_list="$(git diff --cached --name-only 2>/dev/null)"; _sr_lrc=$?
      while IFS= read -r _sf; do
        [ -z "$_sf" ] && continue
        [ -n "${BASELINE_SET[$_sf]+x}" ] && continue
        if [ -n "${_OPEN_MERGE_SET[$_sf]+x}" ]; then _sr_merge=$((_sr_merge + 1)); continue; fi
        git reset -q HEAD -- "$_sf" 2>/dev/null || true
        if git diff --cached --quiet -- "$_sf" 2>/dev/null; then _sr_reset=$((_sr_reset + 1)); else _sr_stuck=$((_sr_stuck + 1)); fi
      done <<< "$_sr_list"
      echo "ERROR: BLOCKED -- surprise-channel row gate (steps 7/10). Commit aborted." >&2
      if [ "$_sr_lrc" -ne 0 ]; then
        echo "  WARN: the index could not be read (rc=$_sr_lrc); files staged by THIS call may REMAIN STAGED." >&2
        echo "        Check: git diff --cached --name-only, and clear them yourself: git reset HEAD -- <path>" >&2
      elif [ "$_sr_stuck" -gt 0 ]; then
        echo "  WARN: $_sr_stuck file(s) could NOT be unstaged and REMAIN STAGED -- another seat can adopt" >&2
        echo "        them under their author line. Clear them yourself: git reset HEAD -- <path>" >&2
      else
        echo "       Unstaged $_sr_reset file(s) staged by THIS call; none remains staged; staging from before it is untouched." >&2
      fi
      [ "$_sr_merge" -gt 0 ] && echo "       Left $_sr_merge path(s) staged that belong to a merge OPEN in this worktree (Z-S61); they are the draining seat's." >&2
      printf '%s\n' "$SRGATE_OUT" | sed 's/^/  /' >&2
      exit 1
    elif [ -n "$SRGATE_OUT" ]; then
      printf '%s\n' "$SRGATE_OUT" | sed 's/^/  /' >&2
    fi
  fi
fi

# STEP-4 PRD SURFACE-MANIFEST GATE (Andrew-direct 2026-09-09 ~19:2xZ at the 1.0.0_SA_CTO~Z terminal,
# VERBATIM: "the surface_manifest first of all is mandatory; a PRD literally cannot be committed
# unless it has one."). This MOVES an existing refusal rather than inventing one: the L6 TO gate's
# step-4 conformance limb already refused a TO whose PRD lacked a manifest, so the refusal pointed at
# the COO's artifact for the CTO's omission -- which is precisely how NFRA_REPORT v0.1 committed clean
# with no manifest (@ff9900b0ea) and was caught by two READERS instead of by the machinery.
# CRITICAL: KEYED ON PATHSPEC, NOT IN_SCOPE -- every PRD is .md and IN_SCOPE is the .py/.sh gate scope, so
# wiring this like the .py gate would produce a gate that never fires and reports OK (the silent-no-op
# class the surprise-row-gate block above documents at length).
# DOMAIN: only a doc whose PRD_HEADER declares `step: 4` -- 205 tracked *_PRD.md, 8 are step-4 PRDs.
# MEASURED BEFORE SHIPPING (`prd-manifest-gate.py --census` @f060f2354e): 0 of 8 refused today, so
# there is NO legacy carve-out and none is needed (Andrew, same session: "we dont need legacy carve
# out, that is all tbd"). NO audited override, deliberately -- his word is "literally cannot".
if [ ${#PATHSPEC[@]} -gt 0 ] && [ -f "$SCRIPT_DIR/prd-manifest-gate.py" ]; then
  PMGATE_FILES=()
  for _pf in "${PATHSPEC[@]}"; do
    case "$_pf" in
      # 2026-09-10: the ADDENDUM shape is included DELIBERATELY. The gate's limb F (an addendum may
      # define no outcome absent from its PRD) was unreachable in production while this filter took
      # *_PRD.md alone -- the gate held the domain and the CALLER filtered it out, so the limb could
      # never fire. That is the same class the limb itself exists to catch: a rule nothing enforces.
      *_PRD.md|*_PRD_ADDENDUM*.md) PMGATE_FILES+=("$_pf") ;;
    esac
  done
  if [ "${#PMGATE_FILES[@]}" -gt 0 ]; then
    PMGATE_OUT=""; PMGATE_RC=0
    PMGATE_OUT="$(python "$SCRIPT_DIR/prd-manifest-gate.py" "${PMGATE_FILES[@]}" 2>&1)" || PMGATE_RC=$?
    if [ "$PMGATE_RC" -ne 0 ]; then
      for _pf in "${PMGATE_FILES[@]}"; do git reset -q HEAD -- "$_pf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- step-4 PRD surface-manifest gate. Commit aborted; files unstaged." >&2
      printf '%s\n' "$PMGATE_OUT" | sed 's/^/  /' >&2
      exit 1
    elif [ -n "$PMGATE_OUT" ]; then
      printf '%s\n' "$PMGATE_OUT" | sed 's/^/  /' >&2
    fi
  fi
fi

# WS-2 comp-system 06_current_state staleness gate (NFRA_SYSPARITY, CTO arch-gate 20260719T213935Z).
# A commit that touches a comp-system _SOURCE must not leave 06 stale. FAIL-CLOSED on GENUINE drift
# (source-fingerprint / managed-region), STALENESS-CONDITIONED (comp-system --gate --changed evaluates
# drift ONLY on a _SOURCE touch -> never wall-clock / false-Monday), alert-suspension-clean (commit-time,
# no new CI cadence). Escape valve: an AUDITED `system-current-override: <reason>` -m trailer (over-rate
# is the monitored P2.5 auto-regen signal). FAIL-SAFE: ONLY a clean rc2 (genuine drift) blocks; a tool
# error (rc1) or any other rc -> WARN + proceed, so a broken gate NEVER wedges the fabric's commit path.
# Keyed on PATHSPEC (the FULL declared changeset -- incl. *.yaml/*.json sources, which IN_SCOPE's .py/.sh
# gate-scope would miss). The cheap grep pre-check keeps NON-source commits from spawning comp-system.
if [ ${#PATHSPEC[@]} -gt 0 ] && printf '%s\n' "${PATHSPEC[@]}" | grep -qE '\.tools/comp-|org/modules/graph/|0\.4\.0_DS_ClientPlatform/deliverables/' && command -v comp-system >/dev/null 2>&1; then
  # set-e-safe rc capture (a command-substitution assignment of a nonzero-exit cmd would trip `set -e`).
  CS_OUT="$(comp-system --gate --changed "${PATHSPEC[@]}" 2>&1)" && CS_RC=0 || CS_RC=$?
  if [ "$CS_RC" = "2" ]; then
    CS_MSG=""; _csk=0
    while [ $_csk -lt ${#COMMIT_ARGS[@]} ]; do
      if [ "${COMMIT_ARGS[$_csk]}" = "-m" ] && [ $((_csk + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
        CS_MSG="${CS_MSG}"$'\n'"${COMMIT_ARGS[$((_csk + 1))]}"
      fi
      _csk=$((_csk + 1))
    done
    # ADDITIVE (TO safe-commit-F-read-override-fix, 2026-07-21): ALSO fold in any -F/--file
    # commit-body FILE contents so the LD-0276-mandated -F path can carry the
    # system-current-override that the F-010 git gate blocks on -m ($(/backtick). STRICTLY
    # ADDITIVE -- the -m loop above and the CS_OVR extract below are BYTE-UNCHANGED; this
    # inserts a separate loop (own vars _cf*) that ONLY APPENDS -F-file text to CS_MSG. The -F
    # file is NEVER shell-parsed -> ZERO injection surface (unlike -m). A -F body WITHOUT the
    # trailer appends no match -> clean no-override (the commit still BLOCKs, exactly as today).
    # Handles the mandated -F <file> plus --file <file> / --file=<file>; skips stdin (-).
    _cfk=0
    while [ $_cfk -lt ${#COMMIT_ARGS[@]} ]; do
      _cfa="${COMMIT_ARGS[$_cfk]}"; _cff=""
      if [ "$_cfa" = "-m" ] && [ $((_cfk + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
        _cfk=$((_cfk + 2)); continue                                  # skip -m VALUE (read above)
      elif { [ "$_cfa" = "-F" ] || [ "$_cfa" = "--file" ]; } && [ $((_cfk + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
        _cff="${COMMIT_ARGS[$((_cfk + 1))]}"; _cfk=$((_cfk + 2))       # -F <file> / --file <file>
      elif [ "${_cfa#--file=}" != "$_cfa" ]; then
        _cff="${_cfa#--file=}"; _cfk=$((_cfk + 1))                     # --file=<file>
      else
        _cfk=$((_cfk + 1)); continue
      fi
      if [ -n "$_cff" ] && [ "$_cff" != "-" ] && [ -f "$_cff" ]; then
        # Normalize an optional leading comment marker on the trailer line
        # (`# system-current-override:` -> `system-current-override:`) so the -F body can carry
        # the override in the codebase's `# <marker>: <reason>` comment convention (cf.
        # `# never-override:` / `# rail-checked:`) AND still be read by the BYTE-UNCHANGED extract
        # below. A plain (no-#) trailer passes through untouched -> -F matches -m identically.
        CS_MSG="${CS_MSG}"$'\n'"$(cat -- "$_cff" 2>/dev/null | sed 's/^[[:space:]]*#[[:space:]]*system-current-override:/system-current-override:/' || true)"
      fi
    done
    CS_OVR="$(printf '%s' "$CS_MSG" | sed -n 's/^[[:space:]]*system-current-override:[[:space:]]*//p' | head -1)"
    if [ -n "$CS_OVR" ]; then
      mkdir -p "$(dirname "$AUDIT_LOG")"
      echo "${ISO_TS} SYSTEM-CURRENT-OVERRIDE  ${AGENT}  reason=${CS_OVR}" >> "$AUDIT_LOG"
      echo "  [comp-system-gate] OVERRIDE (audited -> ${AUDIT_LOG}): 06 stale, overridden -- reason=${CS_OVR}" >&2
      printf '%s\n' "$CS_OUT" | sed 's/^/  [comp-system-gate] /' >&2
    else
      for _csf in "${PATHSPEC[@]}"; do git reset -q HEAD -- "$_csf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- comp-system 06_current_state is STALE and this commit touches a _SOURCE." >&2
      printf '%s\n' "$CS_OUT" | sed 's/^/  [comp-system-gate] /' >&2
      echo "  FIX: run 'comp-system' (regenerate 06), stage infra/system/06_current_state.{md,json} + the" >&2
      echo "       refreshed sibling docs, then re-commit. OR add a one-line AUDITED override to your -m:" >&2
      echo "       'system-current-override: <reason>' (over-rate is monitored -> escalates to P2.5 auto-regen)." >&2
      echo "" >&2
      echo "  IF YOUR COMMIT TOUCHES org/modules/graph/ (the rule bank): THE REGEN FIX ABOVE CANNOT WORK." >&2
      echo "       comp-system would have to compile an UNCOMMITTED source -- i.e. launder unlanded work into" >&2
      echo "       a committed artifact -- so it refuses. Each gate is correct and each points at the other." >&2
      echo "       Land-then-recompile is TWO-PHASE BY NECESSITY and the override IS the legal path, not a" >&2
      echo "       lapse. Use the RESERVED PREFIX so the monitored rate can tell the two populations apart:" >&2
      echo "         system-current-override: STRUCTURAL-TWOPHASE/rule-bank -- <what landed>" >&2
      echo "       DISCHARGE IT IN-SESSION with the recompile commit. A STRUCTURAL override left undischarged" >&2
      echo "       IS a discipline event; a discharged one is not, and the prefix is what distinguishes them." >&2
      echo "       (CTO arch-gate ruling, LD-0362: the gates are sound; the rate instrument's predicate merged" >&2
      echo "        a correctness signal with a discipline signal, so a rising count read as the reverse.)" >&2
      exit 1
    fi
  elif [ "$CS_RC" = "1" ]; then
    echo "  [comp-system-gate] WARN (fail-safe, NOT blocking): --gate tool error rc1 -- a broken gate must not wedge commits: ${CS_OUT}" >&2
  elif printf '%s' "$CS_OUT" | grep -q "AGE-WARN"; then
    printf '%s\n' "$CS_OUT" | sed 's/^/  [comp-system-gate] /' >&2
  fi
fi

# PIPELINE GATE LAYER 2 (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md; build routed to the
# tooling lane on Andrew's word in the ratification; built 2026-08-24 by 0.8.0_AE_CloudComp~F).
# A NEW task order for a PIPELINE-REGISTERED project must carry <decomp_ref>. The choke-point
# principle (:164): nothing executes without a TO, so requiring the ref at ISSUANCE requires the
# decomp, the PRD and the registration behind it -- one gate at the neck instead of four.
#
# SCOPED THREE WAYS so it cannot become a tax on anything else: NEW files only
# (--diff-filter=A), under **/task_orders/ only, on projects carrying a dep_stage only
# (10 of 326 project JSONs on 2026-08-24).
#
# ANNOUNCE BY DEFAULT: it prints and does NOT block until org/mcp/pipeline-gate2.enforce exists
# (the NFRA_COMPRAIL announce-then-enforce ramp -- arming is one reviewable act, not a code
# change). THE MARKER IS THE AUTHORITY, NOT THIS COMMENT: read the marker, never this paragraph,
# to know whether it is enforcing (Rule 21's measured stale-comment class).
#
# Invoked with NO path arguments ON PURPOSE -- it derives its subject from
# `git diff --cached --diff-filter=A`, which here is exactly what is about to be committed.
# Passing $IN_SCOPE would hand it MODIFIED files too, and editing an existing TO is not
# issuance: retro-fitting <decomp_ref> onto criteria never derived from cells produces the
# false alignment the layer-1 checker exists to refuse.
if [ -f "$SCRIPT_DIR/to-decomp-ref-lint.py" ]; then
  # Self-contained override extraction (-m and the LD-0276-mandated -F). Deliberately NOT
  # reusing CS_MSG: that variable is built only inside the comp-system gate's rc==2 branch, so
  # an override keyed on it would silently work on some commits and not others.
  G2_MSG=""; _g2k=0
  while [ $_g2k -lt ${#COMMIT_ARGS[@]} ]; do
    if [ "${COMMIT_ARGS[$_g2k]}" = "-m" ] && [ $((_g2k + 1)) -lt ${#COMMIT_ARGS[@]} ]; then
      G2_MSG="${G2_MSG}"$'\n'"${COMMIT_ARGS[$((_g2k + 1))]}"; _g2k=$((_g2k + 2)); continue
    fi
    case "${COMMIT_ARGS[$_g2k]}" in
      -F|--file)
        if [ $((_g2k + 1)) -lt ${#COMMIT_ARGS[@]} ] && [ "${COMMIT_ARGS[$((_g2k + 1))]}" != "-" ]; then
          G2_MSG="${G2_MSG}"$'\n'"$(cat -- "${COMMIT_ARGS[$((_g2k + 1))]}" 2>/dev/null || true)"
        fi
        _g2k=$((_g2k + 2)); continue ;;
      --file=*)
        G2_MSG="${G2_MSG}"$'\n'"$(cat -- "${COMMIT_ARGS[$_g2k]#--file=}" 2>/dev/null || true)"
        _g2k=$((_g2k + 1)); continue ;;
    esac
    _g2k=$((_g2k + 1))
  done
  # Tolerate the trailer with or without a leading '#': a -F body carries it commented.
  G2_OVR="$(printf '%s' "$G2_MSG" | sed -n 's/^[[:space:]]*#\?[[:space:]]*pipeline-gate2-override:[[:space:]]*//p' | head -1)"
  if [ -n "$G2_OVR" ]; then
    _g2_out="$(python "$SCRIPT_DIR/to-decomp-ref-lint.py" --override-reason "$G2_OVR" 2>&1)" && _g2_rc=0 || _g2_rc=$?
  else
    _g2_out="$(python "$SCRIPT_DIR/to-decomp-ref-lint.py" 2>&1)" && _g2_rc=0 || _g2_rc=$?
  fi
  # WARN: carries the deliverables-grant mismatch (CVO~Z msg 29834); it never blocks, but it must be seen at the cut.
  if [ "$_g2_rc" -ne 0 ] || printf '%s' "$_g2_out" | grep -q -E 'REFUSED|WARN:'; then
    printf '%s\n' "$_g2_out" | sed 's/^/  [gate2] /' >&2
  fi
  if [ "$_g2_rc" -eq 1 ]; then
    for _gf in $(git diff --cached --diff-filter=A --name-only 2>/dev/null); do
      git reset -q HEAD -- "$_gf" 2>/dev/null || true
    done
    echo "ERROR: BLOCKED -- pipeline gate 2: a NEW task order for a pipeline-registered project" >&2
    echo "  must carry <decomp_ref> naming its decomp run and cells. New files unstaged." >&2
    echo "  FIX the TO, or state an audited reason in the commit message:" >&2
    echo "    # pipeline-gate2-override: <reason>" >&2
    exit 1
  fi
fi

# Proceed with the actual scoped commit (plain invocation so the EXIT trap fires).
#
# AMENDMENT-1 belt: `commit --only` re-takes the WORKTREE state of the pathspec at
# commit time, so a .pyc created by the gate's own py_compile AFTER staging (the
# c36710809 / fbdb335b4 mechanism) would be swept in even though staging filtered
# it. The exclude magic closes that window; anything it excludes RIGHT NOW is
# printed first (never silent -- the ZERO_CHECKS lesson).
COMMIT_EXCLUDES=()
while IFS= read -r _ex; do COMMIT_EXCLUDES+=("$_ex"); done < <(cg_commit_exclude_pathspec)
_late_pyc="$(git status --porcelain -- "${PATHSPEC[@]}" 2>/dev/null | cut -c4- | grep -E "$CG_PYCACHE_RE" || true)"
if [ -n "$_late_pyc" ]; then
  while IFS= read -r _p; do
    [ -n "$_p" ] && echo "SKIP: pycache-artifact (never committed): $_p" >&2
  done <<< "$_late_pyc"
fi
# set-e-safe rc capture -- THE SAME IDIOM AS :569, AND THE REASON IS MEASURED, NOT STYLISTIC.
# `set -euo pipefail` (:30) KILLS THE SHELL on a bare `x="$(cmd)"` whose command exits NONZERO.
# So on a hook-BLOCKED commit the shell died ON THIS LINE: `_commit_rc` was never assigned, the
# printf below never ran, and the gate's BLOCKED text -- which IS captured into `_commit_out` by
# the `2>&1` -- was discarded with it. The seat saw SILENCE and its files stayed STAGED, which is
# indistinguishable from a slow commit or a no-op.
# BOTH ARMS EXERCISED 2026-08-25 (1.0.0_SA_CTO), one variable changed: the fragile form loses the
# text and dies; this form captures rc, prints the text, and reaches `exit $_commit_rc` at :end.
# Symptom reported by 2.0.0_SA_COO (71511); `set -e` mechanism found by 3.0.0_SA_CVO (71562).
# GIT_EDITOR=false belt behind the message-flag gate: if ANY residual path still
# reaches git without a message (a hook, a template, a future arg the gate does
# not know), git runs `false` as the editor and ABORTS LOUDLY instead of hanging
# on an editor no headless session can answer. An abort lands in the rc!=0
# cleanup below; a hang holds index.lock fabric-wide. Belt, not the gate --
# deliberately unexercised (exercising it requires a bare message-less git
# commit, which is itself banned); its failure mode is a visible refusal.
if [ "$_SC_2P" -eq 1 ]; then
  _sc2p_commit && _commit_rc=0 || _commit_rc=$?
else
_commit_out="$(GIT_EDITOR=false git commit --only "${COMMIT_ARGS[@]}" -- "${PATHSPEC[@]}" "${COMMIT_EXCLUDES[@]}" 2>&1)" && _commit_rc=0 || _commit_rc=$?
fi
printf '%s
' "$_commit_out"

# ============================================================================
# REFUSAL RESIDUE (measured 2026-08-25 by 2.0.0_SA_COO, 3.0.0_SA_CVO, 0.5.0_AE_OpalETL~B).
# A REFUSED commit leaves THIS CALL'S staging sitting in the index. On a ~12-seat shared
# worktree the next seat's safe-commit ADOPTS those files under THEIR author line and subject
# -- not hypothetical: it swept a CLAUDE.md Rule 17b edit into 6df0f160c6 under a foreign
# author tonight. Unstage ONLY what THIS call staged -- staged-now MINUS the lock-entry
# BASELINE -- so a caller's or a peer's pre-existing staging is never touched.
# THIS ADDS NO GATE: the refusal is git's / the hook's and has ALREADY happened; this only
# cleans up after it and says so. A file that could NOT be unstaged is REPORTED, never
# silently left -- an unreported residue is the whole hazard.
# ============================================================================
if [ "$_commit_rc" -ne 0 ] && [ "$_SC_2P" -eq 1 ]; then
  echo "ERROR: safe-commit did NOT commit (rc=$_commit_rc). The refusal text is printed above." >&2
  echo "       Two-phase path: everything was staged in a PRIVATE index, so the shared index holds nothing from this call." >&2
elif [ "$_commit_rc" -ne 0 ]; then
  _resid=0; _stuck=0; _mleft=0
  _load_open_merge_set
  while IFS= read -r _sf; do
    [ -z "$_sf" ] && continue
    [ -n "${BASELINE_SET[$_sf]+x}" ] && continue
    if [ -n "${_OPEN_MERGE_SET[$_sf]+x}" ]; then _mleft=$((_mleft + 1)); continue; fi
    if git reset -q HEAD -- "$_sf" 2>/dev/null; then _resid=$((_resid + 1)); else _stuck=$((_stuck + 1)); fi
  done < <(git diff --cached --name-only 2>/dev/null || true)
  echo "ERROR: safe-commit did NOT commit (rc=$_commit_rc). The refusal text is printed above." >&2
  echo "       Unstaged $_resid file(s) staged by THIS call; anything staged beforehand is untouched." >&2
  [ "$_mleft" -gt 0 ] && echo "       Left $_mleft path(s) staged that belong to a merge OPEN in this worktree (Z-S61); they are the draining seat's. Re-run after the merge lands." >&2
  if [ "$_stuck" -gt 0 ]; then
    echo "  WARN: $_stuck file(s) could NOT be unstaged and REMAIN STAGED -- another seat can adopt" >&2
    echo "        them under their author line. Clear them yourself: git reset HEAD -- <path>" >&2
  fi
  echo "       DO NOT grep THIS OUTPUT to decide whether it committed. Ask the REPOSITORY:" >&2
  echo "         git log -1 --format=%h~%an~%s <hash>   (negative control: a bogus hash must fail)" >&2
  echo "       A tool stdout line is the TOOL DESCRIBING ITSELF; git log is the REPOSITORY" >&2
  echo "       ANSWERING. Measured 2026-08-25 by 0.4.0_DS_ClientPlatform~J: this reminder used to" >&2
  echo "       quote the success marker verbatim, so a naive grep for it returned PASS on a FAILED" >&2
  echo "       commit. A check that parses a tool prose inherits every future edit to that prose." >&2
fi

# ============================================================================
# MESSAGE SELF-VERIFY (Andrew-direct 2026-08-24 ~23:5xZ, COO record @91011a1a1d:
# "seems to me like the 'checker' should have that built in") -- after a
# SUCCESSFUL commit, compare the message of THIS COMMIT'S OWN HASH against the
# -F/--file source, trailing newlines stripped from BOTH, and FAIL LOUD naming
# the first differing character index. WHY HERE AND NOWHERE ELSE: safe-commit is
# the only actor holding both the message file and its own new hash at the
# moment of the act. Every after-the-fact form broke on a reconstruction step --
# flag spelling (%B vs pretty=format:%B disagree by exactly one byte), a peer's
# HEAD in a 15-seat shared worktree (two false hash claims in one night), or
# newline normalisation (four control variants falsified in an hour, LD-0449).
# This block reads its own hash inside the wrapper's flow (never a latest-commit
# read) and normalises both sides identically (raw cat-file object; rstrip CR/LF
# only). A mismatch does NOT undo the commit (a commit is a fact); it exits 3 so
# the seat corrects SAME-TURN instead of broadcasting a stale message as landed.
# Prints the new hash + subject either way -- a claim about the commit starts
# from the commit's own bytes, never from git log -1 in a shared worktree.
# ============================================================================
if [ "$_commit_rc" -eq 0 ]; then
  _sv_file=""; _svk=0
  while [ $_svk -lt ${#COMMIT_ARGS[@]} ]; do
    case "${COMMIT_ARGS[$_svk]}" in
      -F|--file)
        [ $((_svk + 1)) -lt ${#COMMIT_ARGS[@]} ] && [ "${COMMIT_ARGS[$((_svk + 1))]}" != "-" ] && _sv_file="${COMMIT_ARGS[$((_svk + 1))]}"
        _svk=$((_svk + 2)); continue ;;
      --file=*) _sv_file="${COMMIT_ARGS[$_svk]#--file=}"; _svk=$((_svk + 1)); continue ;;
    esac
    _svk=$((_svk + 1))
  done
  # !! THE HASH COMES FROM `git commit`'S OWN OUTPUT, NEVER FROM `git rev-parse HEAD`.
  # MEASURED 2026-08-25 ~03:3xZ IN THIS VERY BLOCK, ON ITS AUTHOR: a peer commit landed
  # BETWEEN the commit and the rev-parse in this 15-seat shared worktree, so msg-verify
  # reported a PEER'S hash and subject for MY commit -- the exact shared-worktree HEAD class
  # this feature exists to kill, reintroduced inside the fix. `git commit` prints
  # "[BRANCH abcdef123] subject" and that hash is ITS OWN, immune to any concurrent write.
  _sv_hash="$(printf '%s' "$_commit_out" | sed -n 's/^\[[^ ]* \([0-9a-f]\{7,40\}\)\].*/\1/p' | head -1)"
  if [ -z "$_sv_hash" ]; then
    # FAIL LOUD, never fall back to HEAD: an unparsed hash means the output shape changed,
    # and silently reading HEAD is precisely the defect above.
    echo "  [msg-verify] CANNOT PARSE the commit hash from git commit output -- NOT falling back to HEAD (that is the race this replaced). Verify by hand: git log -1 --format=%H -- <your paths>" >&2
    exit "$_commit_rc"
  fi
  _sv_subject="$(git log -1 --pretty=format:%s "$_sv_hash" 2>/dev/null)"
  echo "  [msg-verify] committed ${_sv_hash:0:10}  subject: ${_sv_subject:0:100}"
  if [ -n "$_sv_file" ] && [ -f "$_sv_file" ]; then
    _sv_out="$(python "$SCRIPT_DIR/safe_commit_msg_verify.py" "$_sv_file" "$_sv_hash" 2>&1)" && _sv_rc=0 || _sv_rc=$?
    if [ "$_sv_rc" -ne 0 ]; then
      printf '%s
' "$_sv_out" | sed 's/^/  [msg-verify] /' >&2
      echo "ERROR: msg-verify FAILED -- the COMMITTED message differs from the -F file." >&2
      echo "  The commit $_sv_hash STANDS (a commit is a fact); the -F path was stale or" >&2
      echo "  swapped (LD-0449 class). CORRECT SAME-TURN: read the committed message" >&2
      echo "  (git cat-file commit <hash>), decide which text is true, follow up, and" >&2
      echo "  never broadcast the file's text as this commit's message." >&2
      exit 3
    fi
    echo "  [msg-verify] ${_sv_out}"
  fi
fi
exit $_commit_rc
