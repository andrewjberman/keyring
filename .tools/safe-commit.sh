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
# LEGACY PATH (default; also the D6 fallback for worker-down / enqueue-fail).
# PRESERVED byte-for-byte from the pre-queue safe-commit.sh, EXCEPT the
# sensitive-leak detection now calls the SHARED cg_sensitive_hits (no drift).
# ==========================================================================
LOCK_DIR="${SAFE_COMMIT_LOCK_DIR:-$(git rev-parse --absolute-git-dir 2>/dev/null)/commit-queue.lock}"
LOCK_TIMEOUT_SEC="${SAFE_COMMIT_LOCK_TIMEOUT:-60}"
LOCK_ACQUIRED=0
elapsed=0
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  if [ -f "$LOCK_DIR/pid" ]; then
    holder_pid="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
    if [ -n "$holder_pid" ] && ! kill -0 "$holder_pid" 2>/dev/null; then
      rm -rf "$LOCK_DIR" 2>/dev/null || true
      continue
    fi
  fi
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

# (1) BASELINE: what was already staged at lock-entry (foreign + any caller pre-add).
BASELINE="$(git diff --cached --name-only 2>/dev/null || true)"
declare -A BASELINE_SET=()
if [ -n "$BASELINE" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    BASELINE_SET["$f"]=1
  done <<< "$BASELINE"
fi

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
  if ADD_ERR="$(git add -f -- "${PATHSPEC[@]}" 2>&1)"; then
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

# Advisory surface-check gate (QUERY-only; never blocks).
if command -v comp-surface-check >/dev/null 2>&1 && [ -n "$IN_SCOPE" ]; then
  _sc_args=()
  while IFS= read -r _f; do
    [ -z "$_f" ] && continue
    _sc_args+=("--file" "$_f")
  done <<< "$IN_SCOPE"
  if [ ${#_sc_args[@]} -gt 0 ]; then
    comp-surface-check check --mode advisory "${_sc_args[@]}" 2>&1 \
      | sed 's/^/  [surface-check] /' || true
  fi
fi

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

# Advisory comp-coverage-check gate (COMPUNIFY; never blocks).
if command -v comp-coverage-check >/dev/null 2>&1 && [ -n "$IN_SCOPE" ]; then
  if echo "$IN_SCOPE" | grep -qE 'comp-coverage-map\.yaml|\.tools/comp-'; then
    comp-coverage-check check 2>&1 | sed 's/^/  [coverage-check] /' || true
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
    if ! GATE_OUT="$(bash "$SCRIPT_DIR/commit-gate.sh" "${GATE_FILES[@]}" 2>&1)"; then
      # Unstage the in-scope files (mirror the sensitive/contamination reject: a BLOCKED
      # request must never leave its files staged for a later invocation to (mis-)inherit).
      for _gf in "${GATE_FILES[@]}"; do git reset -q HEAD -- "$_gf" 2>/dev/null || true; done
      echo "ERROR: BLOCKED -- commit-gate failed (py_compile / ruff / lint). Commit aborted; files unstaged." >&2
      printf '%s\n' "$GATE_OUT" | sed 's/^/  [commit-gate] /' >&2
      echo "  Fix the reported issue(s) and re-commit. This gate is UNIVERSAL + fail-closed on ALL .py" >&2
      echo "  (Rule 14); --force does NOT bypass a gate failure (it only overrides the contamination check)." >&2
      exit 1
    fi
  fi
fi

# Proceed with the actual scoped commit (plain invocation so the EXIT trap fires).
git commit --only "${COMMIT_ARGS[@]}" -- "${PATHSPEC[@]}"
exit $?
