#!/usr/bin/env bash
# NFRA_CMTQUE TO-3 -- commit_queue_lib.sh
# Local durable queue substrate for the commit-worker daemon (concurrency=1).
#
# WHAT: a per-worktree on-disk request/result queue under <gitdir>/commit-queue/.
#   The thin enqueue client (safe-commit.sh, TO-2) writes a REQUEST and blocks
#   polling for a RESULT; the single commit-worker daemon (commit-worker.sh, TO-1)
#   drains requests FIFO, commits, and writes results. Atomic-mv delivery gives
#   exactly-once semantics (the inbox-watch.sh idiom); the result is written ONLY
#   after the git commit returns, so a worker crash mid-commit is recoverable
#   (the request sits in processing/ for the startup sweep) -- never a lost or
#   duplicated commit.
#
# WHY on-disk + local: the git repo is a local filesystem repo shared by all
#   agents on one host. A cloud queue for a same-host operation buys nothing and
#   adds latency + AWS-uptime coupling to every commit. Substrate LOCKED local
#   (Andrew-ratified 2026-07-06). Cloud = observability ONLY (TO-4).
#
# ENCODING: request/result are single files, one "KEY <value>" per line, where
#   free-text values (author, commit-args, pathspec, cwd, env, stdout, stderr,
#   reason) are base64(-w0) encoded so arbitrary content (parens, quotes,
#   newlines, spaces, $, backticks) round-trips with zero shell-escaping risk.
#   Multi-value keys (CARG/PATH/ENV) repeat in order. Single-file atomic mv
#   delivers the whole record indivisibly (build in .tmp.<id>, then mv).
#
# RULE 16 (Git Bash 3.6.7): uses only default utilities -- mv/mkdir/cat/printf/
#   grep/sed/stat/date/base64/kill/rm/ls. No flock/pgrep/pkill/pidof/setsid.
#
# USAGE: source this file, then call cq_* functions. Run directly for a self-test:
#   bash .tools/commit_queue_lib.sh selftest

set -uo pipefail

# --------------------------------------------------------------------------
# Paths -- per-worktree, under the real gitdir (a linked worktree's gitdir is
# .git/worktrees/<name>, always a real dir; mirrors safe-commit's lock location).
# --------------------------------------------------------------------------
cq_root() {
  local gitdir
  gitdir="$(git rev-parse --absolute-git-dir 2>/dev/null)" || return 1
  printf '%s/commit-queue' "$gitdir"
}

cq_requests_dir()   { printf '%s/requests'   "$(cq_root)"; }
cq_processing_dir() { printf '%s/processing' "$(cq_root)"; }
cq_results_dir()    { printf '%s/results'    "$(cq_root)"; }
cq_dlq_dir()        { printf '%s/dlq'        "$(cq_root)"; }
cq_worker_pid()     { printf '%s/worker.pid' "$(cq_root)"; }
cq_worker_hb()      { printf '%s/worker.hb'  "$(cq_root)"; }

# Heartbeat staleness threshold (seconds). Worker refreshes worker.hb each loop;
# a hb older than this (or a dead pid) => worker considered down => client D6
# fallback to the in-line mkdir-mutex path.
CQ_HB_STALE_SEC="${CQ_HB_STALE_SEC:-30}"

cq_init() {
  local root; root="$(cq_root)" || return 1
  mkdir -p "$root/requests" "$root/processing" "$root/results" "$root/dlq" 2>/dev/null || return 1
  return 0
}

# --------------------------------------------------------------------------
# Encoding helpers (base64 -w0; guarded).
# --------------------------------------------------------------------------
cq_b64enc() { printf '%s' "${1-}" | base64 -w0 2>/dev/null; }
cq_b64dec() { printf '%s' "${1-}" | base64 -d 2>/dev/null; }

# --------------------------------------------------------------------------
# Request id + timestamp.  reqid = <epoch>_<pid>_<rand> (unique per enqueue).
# The request FILENAME is <enqueue_ts>_<reqid>.req so a lexical sort of the
# requests dir == chronological FIFO order (the inbox-watch ISO-ts idiom).
# --------------------------------------------------------------------------
cq_now_iso()   { date -u +%Y%m%dT%H%M%SZ; }
cq_now_epoch() { date +%s; }
cq_gen_reqid() {
  local r="${RANDOM:-0}${RANDOM:-0}"
  printf '%s_%s_%s' "$(cq_now_epoch)" "$$" "$r"
}

# --------------------------------------------------------------------------
# ENQUEUE (client side).
#   cq_enqueue <cwd> <force0|1> <author> <n_cargs> <carg...> <n_paths> <path...> <n_env> <env...>
# Echoes the reqid on success (rc 0); rc 1 on failure. Atomic: builds in
# requests/.tmp.<reqid> then mv into requests/<ts>_<reqid>.req.
# --------------------------------------------------------------------------
cq_enqueue() {
  local cwd="$1" force="$2" author="$3"; shift 3
  local n_cargs="$1"; shift
  local cargs=(); local i=0
  while [ "$i" -lt "$n_cargs" ]; do cargs+=("$1"); shift; i=$((i+1)); done
  local n_paths="$1"; shift
  local paths=(); i=0
  while [ "$i" -lt "$n_paths" ]; do paths+=("$1"); shift; i=$((i+1)); done
  local n_env="$1"; shift
  local envs=(); i=0
  while [ "$i" -lt "$n_env" ]; do envs+=("$1"); shift; i=$((i+1)); done

  cq_init || return 1
  local reqid ts req_dir tmp final
  reqid="$(cq_gen_reqid)"
  ts="$(cq_now_iso)"
  req_dir="$(cq_requests_dir)"
  tmp="$req_dir/.tmp.$reqid"
  final="$req_dir/${ts}_${reqid}.req"

  {
    printf 'REQID %s\n' "$reqid"
    printf 'ENQUEUE_TS %s\n' "$ts"
    printf 'CWD %s\n' "$(cq_b64enc "$cwd")"
    printf 'FORCE %s\n' "$force"
    printf 'AUTHOR %s\n' "$(cq_b64enc "$author")"
    local a; for a in "${cargs[@]:-}"; do [ "$n_cargs" -eq 0 ] && break; printf 'CARG %s\n' "$(cq_b64enc "$a")"; done
    local p; for p in "${paths[@]:-}"; do [ "$n_paths" -eq 0 ] && break; printf 'PATH %s\n' "$(cq_b64enc "$p")"; done
    local e; for e in "${envs[@]:-}"; do [ "$n_env" -eq 0 ] && break; printf 'ENV %s\n' "$(cq_b64enc "$e")"; done
  } > "$tmp" 2>/dev/null || { rm -f "$tmp" 2>/dev/null; return 1; }

  mv "$tmp" "$final" 2>/dev/null || { rm -f "$tmp" 2>/dev/null; return 1; }
  printf '%s' "$reqid"
  return 0
}

# --------------------------------------------------------------------------
# CLAIM (worker side). Atomically claims the OLDEST request (lexical FIFO) by
# mv into processing/. Echoes the claimed processing-path (rc 0), or rc 1 if
# the queue is empty. Concurrency=1 makes the mv-race moot, but the atomic
# claim keeps it exactly-once even under an accidental double-worker.
# --------------------------------------------------------------------------
cq_claim_oldest() {
  local req_dir proc_dir f base dest
  req_dir="$(cq_requests_dir)"; proc_dir="$(cq_processing_dir)"
  for f in "$req_dir"/*.req; do
    [ -f "$f" ] || continue          # empty-glob guard
    base="$(basename "$f")"
    dest="$proc_dir/$base"
    if mv "$f" "$dest" 2>/dev/null; then
      printf '%s' "$dest"
      return 0
    fi
    # lost the race (another claimer) -> try next
  done
  return 1
}

# Field readers for a request/result file. cq_field <file> <KEY> -> first match value.
cq_field()    { grep -m1 "^$2 " "$1" 2>/dev/null | sed "s/^$2 //"; }
# cq_field_all <file> <KEY> -> all values (one per line), order preserved.
cq_field_all(){ grep "^$2 " "$1" 2>/dev/null | sed "s/^$2 //"; }

# --------------------------------------------------------------------------
# RESULT (worker writes / client reads). Atomic single-file mv.
#   cq_write_result <reqid> <status> <exit_code> <commit_hash> <reason> <stdout> <stderr>
# --------------------------------------------------------------------------
cq_write_result() {
  local reqid="$1" status="$2" exit_code="$3" hash="$4" reason="$5" out="$6" err="$7"
  local res_dir tmp final
  res_dir="$(cq_results_dir)"
  tmp="$res_dir/.tmp.$reqid"
  final="$res_dir/${reqid}.res"
  {
    printf 'REQID %s\n' "$reqid"
    printf 'STATUS %s\n' "$status"
    printf 'EXIT_CODE %s\n' "$exit_code"
    printf 'COMMIT_HASH %s\n' "${hash:--}"
    printf 'REASON %s\n' "$(cq_b64enc "$reason")"
    printf 'STDOUT %s\n' "$(cq_b64enc "$out")"
    printf 'STDERR %s\n' "$(cq_b64enc "$err")"
    printf 'WORKER_TS %s\n' "$(cq_now_iso)"
  } > "$tmp" 2>/dev/null || { rm -f "$tmp" 2>/dev/null; return 1; }
  mv "$tmp" "$final" 2>/dev/null || { rm -f "$tmp" 2>/dev/null; return 1; }
  return 0
}

cq_result_path()  { printf '%s/%s.res' "$(cq_results_dir)" "$1"; }
cq_result_ready() { [ -f "$(cq_result_path "$1")" ]; }

# --------------------------------------------------------------------------
# DLQ (worker). Move an un-committable request into dlq/ (preserved for the
# alarm + human triage). Keeps the original filename.
# --------------------------------------------------------------------------
cq_dlq() {
  local proc_path="$1"
  local dlq_dir; dlq_dir="$(cq_dlq_dir)"
  mv "$proc_path" "$dlq_dir/$(basename "$proc_path")" 2>/dev/null || return 1
  return 0
}

# --------------------------------------------------------------------------
# Worker liveness (D6 fallback gate). alive = pid file names a live PID AND
# heartbeat is fresh (< CQ_HB_STALE_SEC). rc 0 alive, rc 1 down.
# --------------------------------------------------------------------------
cq_worker_alive() {
  local pidf hbf pid hb now age
  pidf="$(cq_worker_pid)"; hbf="$(cq_worker_hb)"
  [ -f "$pidf" ] || return 1
  pid="$(cat "$pidf" 2>/dev/null || true)"
  [ -n "$pid" ] || return 1
  kill -0 "$pid" 2>/dev/null || return 1
  [ -f "$hbf" ] || return 1
  hb="$(cat "$hbf" 2>/dev/null || true)"
  [ -n "$hb" ] || return 1
  now="$(cq_now_epoch)"
  age=$(( now - hb ))
  [ "$age" -lt "$CQ_HB_STALE_SEC" ] || return 1
  return 0
}

cq_heartbeat() { printf '%s' "$(cq_now_epoch)" > "$(cq_worker_hb)" 2>/dev/null || true; }

# --------------------------------------------------------------------------
# Self-test: exercises enqueue -> claim -> result round-trip, FIFO order,
# base64 fidelity of a nasty payload, and crash-durability (a claimed request
# with no result stays in processing/). Pure lib test -- no git commit.
# --------------------------------------------------------------------------
cq_selftest() {
  local root; root="$(cq_root)" || { echo "FAIL: not in a git repo"; return 1; }
  echo "commit_queue_lib selftest -- root=$root"
  cq_init || { echo "FAIL: cq_init"; return 1; }

  # nasty payload: parens, quotes, spaces, $, backticks, unicode-free ascii-only
  local msg='fix(x) [pure] "q" $VAR `cmd` a&b|c'
  local author='0.7.0_AE_CloudOps~B <0.7.0_AE_CloudOps@opal.agent>'
  local p1='path/with space/file (1).json'

  local r1 r2 r3
  r1="$(cq_enqueue "/some/cwd" 0 "$author" 2 "-m" "$msg" 1 "$p1" 1 "SAFE_COMMIT_ALLOW_SENSITIVE=reason x")" || { echo "FAIL enqueue r1"; return 1; }
  sleep 1  # ensure distinct ts prefix for FIFO ordering check
  r2="$(cq_enqueue "/cwd2" 1 "$author" 1 "--force-ish" 1 "b.txt" 0)" || { echo "FAIL enqueue r2"; return 1; }
  echo "  enqueued r1=$r1 r2=$r2"

  # FIFO: first claim must be r1 (older ts)
  local c1 c2
  c1="$(cq_claim_oldest)" || { echo "FAIL claim c1"; return 1; }
  [ "$(cq_field "$c1" REQID)" = "$r1" ] || { echo "FAIL FIFO: expected $r1 got $(cq_field "$c1" REQID)"; return 1; }
  echo "  FIFO ok: first claim = r1"

  # base64 fidelity: decode CARG/PATH/AUTHOR
  local got_msg got_path got_author got_force
  got_author="$(cq_b64dec "$(cq_field "$c1" AUTHOR)")"
  got_force="$(cq_field "$c1" FORCE)"
  # second CARG value is the message (-m then msg)
  got_msg="$(cq_b64dec "$(cq_field_all "$c1" CARG | sed -n '2p')")"
  got_path="$(cq_b64dec "$(cq_field_all "$c1" PATH | sed -n '1p')")"
  [ "$got_author" = "$author" ] || { echo "FAIL author fidelity"; return 1; }
  [ "$got_msg" = "$msg" ]       || { echo "FAIL msg fidelity: [$got_msg] != [$msg]"; return 1; }
  [ "$got_path" = "$p1" ]       || { echo "FAIL path fidelity"; return 1; }
  [ "$got_force" = "0" ]        || { echo "FAIL force field"; return 1; }
  echo "  base64 fidelity ok (author/msg/path/force round-trip exact)"

  # crash-durability: c1 claimed, NO result written -> stays in processing/
  [ -f "$c1" ] || { echo "FAIL: claimed request not in processing/"; return 1; }
  echo "  crash-durability ok: claimed req persists in processing/ until result"

  # result round-trip
  cq_write_result "$r1" committed 0 "abc123def" "" "[main abc123def] $msg" "" || { echo "FAIL write_result"; return 1; }
  cq_result_ready "$r1" || { echo "FAIL result not ready"; return 1; }
  local rstatus rhash
  rstatus="$(cq_field "$(cq_result_path "$r1")" STATUS)"
  rhash="$(cq_field "$(cq_result_path "$r1")" COMMIT_HASH)"
  [ "$rstatus" = "committed" ] || { echo "FAIL result status"; return 1; }
  [ "$rhash" = "abc123def" ]   || { echo "FAIL result hash"; return 1; }
  echo "  result round-trip ok (status=committed hash=$rhash)"

  # claim r2, DLQ it
  c2="$(cq_claim_oldest)" || { echo "FAIL claim c2"; return 1; }
  cq_dlq "$c2" || { echo "FAIL dlq"; return 1; }
  [ -f "$(cq_dlq_dir)/$(basename "$c2")" ] || { echo "FAIL: not in dlq"; return 1; }
  echo "  dlq ok"

  # cleanup selftest artifacts
  rm -f "$c1" "$(cq_result_path "$r1")" "$(cq_dlq_dir)/$(basename "$c2")" 2>/dev/null || true

  echo "PASS: commit_queue_lib selftest (all checks)"
  return 0
}

# Run selftest if invoked directly with 'selftest'.
if [ "${1:-}" = "selftest" ]; then
  cq_selftest
  exit $?
fi
