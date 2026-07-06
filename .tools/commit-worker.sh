#!/usr/bin/env bash
# NFRA_CMTQUE TO-1 -- commit-worker.sh
# The single serial commit-worker daemon: the ONLY process that touches the git
# index once the queue path is live. Drains the local durable queue (TO-3) FIFO,
# commits each request in its own uncontended critical section, and returns a
# per-request result (commit hash | rejected+reason) to the blocking client.
#
# CONCURRENCY = 1, HARD. This is a single process with a serial loop: one request
# is fully processed (staged, gated, committed, result-written) before the next is
# claimed. There is no backgrounding, no parallel dispatch. Git's index/branch is a
# strict single-writer; the graph pattern capped at 2 and STILL hit a 409-race ->
# 298k-DLQ flood (item2b.tf). Git is stricter -> exactly one at a time, structurally.
#
# GATES PRESERVED (G4) -- all run inside the worker, attributed to the REQUESTER:
#   - sensitive-leak fail-closed (ported verbatim from safe-commit.sh:236-285)
#   - owned-paths lane enforcement + COMP-branch isolation (the real pre-commit hook,
#     which keys on `git var GIT_AUTHOR_IDENT` -> the worker EXPORTS GIT_AUTHOR_* from
#     the request so the hook sees req.author, NOT the worker identity -- R4)
#   - author identity (--author passed verbatim, in commit_args)
#   - --force + FORCE-BYPASS / SENSITIVE-BLOCK audit (worker writes the audit log)
#   - atomic per-agent commit (git commit --only, one commit per request)
#   ds-commit-gate (py_compile/ruff) stays AGENT-SIDE fail-fast (don't enqueue a
#   non-compiling .py); TO-5 formalizes the worker re-assert.
#
# CONTAMINATION GUARD RETIRED (D5): a single index-writer means git diff --cached can
# only ever show THIS worker's own in-scope stage -> the baseline/contamination
# apparatus is dead weight and is NOT ported. git commit --only stays pathspec-scoped.
#
# RETRY (D2, from incremental_updater): bounded exponential backoff. A git GATE/HOOK
# rejection is DETERMINISTIC -> NOT retried (fails identically); it becomes a clean
# client-visible rejected-result. Only a genuinely TRANSIENT fault (index.lock / ref-
# lock contention) is retried. Exhaustion + corrupt-request + crash-orphan -> DLQ +
# loud alarm-metric (never silent -- G5).
#
# DLQ SEMANTIC (design refinement -- flag for CTO arch-gate): the PRD says "hard fail
# -> DLQ". This worker splits that: a DETERMINISTIC gate/hook rejection (bad pathspec,
# owned-paths violation, sensitive leak, nothing-to-commit) is a NORMAL client-visible
# rejection (result=rejected, exit code returned, sensitive/force also durably audited)
# -- it does NOT enter the DLQ, because DLQ-depth>0 fires an ops alarm (AC4) and a
# fat-fingered pathspec must not page ops. The DLQ is reserved for POISON: a transient-
# exhausted request, a corrupt/unparseable request, or a crash-orphan. Every request
# still gets a definitive outcome (hash | rejected+reason | error+dlq) -- nothing
# silently dropped (AC5 intent preserved). Rationale documented for CTO to ratify.
#
# RULE 16 (Git Bash 3.6.7): default utilities only. No flock/pgrep/pkill/pidof/setsid.
#
# MODES:
#   commit-worker.sh                 # run as the daemon (default)
#   commit-worker.sh --drain-once    # process exactly one queued request, then exit (test)
#   commit-worker.sh --selftest      # end-to-end real-commit round-trip in a throwaway repo
#   commit-worker.sh --status        # print worker liveness + queue depths, exit

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=commit_queue_lib.sh
source "$SCRIPT_DIR/commit_queue_lib.sh"

# ---- config -------------------------------------------------------------
WORKER_POLL_SEC="${CQ_WORKER_POLL_SEC:-1}"      # idle poll interval
COMMIT_MAX_ATTEMPTS="${CQ_COMMIT_MAX_ATTEMPTS:-5}"
BACKOFF_BASE_S="${CQ_BACKOFF_BASE_S:-1}"
BACKOFF_CAP_S="${CQ_BACKOFF_CAP_S:-15}"
ORPHAN_MAX_AGE_SEC="${CQ_ORPHAN_MAX_AGE_SEC:-120}"  # processing/ orphan -> DLQ

# ---- sensitive-leak gate regexes (ported verbatim from safe-commit.sh) ---
_LEAK_ALWAYS_RE='\.(har|pem|p12|pfx|jks|keystore|ppk)$|(^|/)id_(rsa|dsa|ecdsa|ed25519)([./]|$)|(^|/)\.(netrc|pgpass)$'
_LEAK_IF_IGNORED_RE='\.(env|key|crt|cer)$|(cookie|secret|credential|password|apikey|api_key|private_key|access_token|auth_token)|(^|/)(\.aws|\.ssh|\.gnupg|sources)/'
_LEAK_EXCLUDE_RE='\.env\.(template|example|sample|dist)$'

log() { printf '%s commit-worker[%s]: %s\n' "$(cq_now_iso)" "$$" "$*" >&2; }

# ---- observability stub (TO-4 wires real CloudWatch put-metric-data) ------
# Best-effort local metric sink; TO-4 replaces the body with `aws cloudwatch
# put-metric-data`. Never fails the worker.
cw_metric() {
  local name="$1" value="$2"
  local sink; sink="$(cq_root)/metrics.log"
  printf '%s %s %s\n' "$(cq_now_iso)" "$name" "$value" >> "$sink" 2>/dev/null || true
}

# ---- singleton ----------------------------------------------------------
cw_acquire_singleton() {
  local pidf; pidf="$(cq_worker_pid)"
  if [ -f "$pidf" ]; then
    local other; other="$(cat "$pidf" 2>/dev/null || true)"
    if [ -n "$other" ] && [ "$other" != "$$" ] && kill -0 "$other" 2>/dev/null; then
      log "another worker alive (pid $other) -- exiting (singleton)"
      exit 0
    fi
  fi
  cq_init || { log "cq_init failed"; exit 1; }
  printf '%s' "$$" > "$pidf"
  cq_heartbeat
}

cw_release_singleton() {
  local pidf; pidf="$(cq_worker_pid)"
  local cur; cur="$(cat "$pidf" 2>/dev/null || true)"
  [ "$cur" = "$$" ] && rm -f "$pidf" 2>/dev/null || true
}

# ---- parse a request file into globals ----------------------------------
# Sets: REQ_ID REQ_CWD REQ_FORCE REQ_AUTHOR REQ_CARGS[] REQ_PATHS[] REQ_ENVS[]
cw_parse_request() {
  local f="$1"
  REQ_ID="$(cq_field "$f" REQID)"
  REQ_CWD="$(cq_b64dec "$(cq_field "$f" CWD)")"
  REQ_FORCE="$(cq_field "$f" FORCE)"
  REQ_AUTHOR="$(cq_b64dec "$(cq_field "$f" AUTHOR)")"
  REQ_CARGS=(); REQ_PATHS=(); REQ_ENVS=()
  local line
  # NB: no -n guard on CARG/PATH -- an empty grep result yields 0 read iterations
  # (process-sub of empty output), so empty ELEMENTS (e.g. -m "") are preserved.
  while IFS= read -r line; do REQ_CARGS+=("$(cq_b64dec "$line")"); done < <(cq_field_all "$f" CARG)
  while IFS= read -r line; do REQ_PATHS+=("$(cq_b64dec "$line")"); done < <(cq_field_all "$f" PATH)
  while IFS= read -r line; do [ -n "$line" ] && REQ_ENVS+=("$(cq_b64dec "$line")"); done < <(cq_field_all "$f" ENV)
  [ -n "$REQ_ID" ] || return 1
  [ "${#REQ_PATHS[@]}" -gt 0 ] || return 1
  return 0
}

# ---- transient-fault classifier -----------------------------------------
# A transient fault is a lock-contention / FS-flake that will likely succeed on
# retry. A gate/hook rejection is DETERMINISTIC -> not transient. rc 0 = transient.
cw_is_transient() {
  local stderr="$1"
  printf '%s' "$stderr" | grep -qiE "index\.lock|unable to create.*\.lock|cannot lock ref|another git process|Unable to create.*index" && return 0
  return 1
}

# ---- sensitive-leak gate (in-worker) ------------------------------------
# Given the current IN_SCOPE staged set, echo the offending files (one/line).
# Mirrors safe-commit.sh:236-261 exactly.
cw_sensitive_hits() {
  local in_scope="$1" f
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    printf '%s\n' "$f" | grep -qiE "$_LEAK_EXCLUDE_RE" && continue
    if printf '%s\n' "$f" | grep -qiE "$_LEAK_ALWAYS_RE"; then
      printf '%s\n' "$f"
    elif printf '%s\n' "$f" | grep -qiE "$_LEAK_IF_IGNORED_RE" \
         && git check-ignore --no-index -q -- "$f" 2>/dev/null; then
      printf '%s\n' "$f"
    fi
  done <<< "$in_scope"
}

# ---- process ONE claimed request ----------------------------------------
# Arg: the processing/ path of the claimed request. Emits a result and clears
# the processing file (rm on committed/rejected; cq_dlq on error).
cw_process() {
  local proc="$1"
  if ! cw_parse_request "$proc"; then
    log "CORRUPT request $(basename "$proc") -> DLQ"
    local rid; rid="$(cq_field "$proc" REQID)"
    [ -n "$rid" ] && cq_write_result "$rid" error 1 "" "corrupt/unparseable request" "" "corrupt request"
    cq_dlq "$proc"; cw_metric dlq_depth 1
    return
  fi

  local audit_log="${SAFE_COMMIT_AUDIT_LOG:-$(git rev-parse --show-toplevel 2>/dev/null)/org/git-author-override-audit.log}"
  local ts; ts="$(cq_now_iso)"

  # (A) resolve the requester CWD (pathspecs are cwd-relative).
  if [ ! -d "$REQ_CWD" ]; then
    log "req $REQ_ID cwd gone: $REQ_CWD"
    cq_write_result "$REQ_ID" rejected 2 "" "requester cwd no longer exists: $REQ_CWD" "" ""
    rm -f "$proc" 2>/dev/null || true
    cw_metric rejected_count 1
    return
  fi

  # Everything below runs in a subshell so cd + env exports don't leak between
  # requests (concurrency=1 makes this belt-and-suspenders, but keeps each
  # request hermetic). The subshell echoes a status line the parent parses.
  local outcome
  outcome="$(
    cd "$REQ_CWD" || { echo "ERR|2|cwd-cd-failed"; exit 0; }

    # (B) apply request env (SAFE_COMMIT_ALLOW_SENSITIVE, SAFE_COMMIT_AUDIT_LOG, ...)
    local kv
    for kv in "${REQ_ENVS[@]:-}"; do [ -n "$kv" ] && export "$kv"; done

    # (C) R4: make the pre-commit hook (owned-paths / COMP) see the REQUESTER.
    # The hook keys on `git var GIT_AUTHOR_IDENT`; export it from req.author so
    # attribution is the requester, not the worker. --author (in CARGS) sets the
    # final commit author to the same value; the two agree.
    local a_name a_email
    a_name="${REQ_AUTHOR%% <*}"
    a_email="${REQ_AUTHOR#*<}"; a_email="${a_email%>}"
    export GIT_AUTHOR_NAME="$a_name"
    export GIT_AUTHOR_EMAIL="$a_email"

    # (D) stage the declared pathspec (-f: force past .gitignore, mirrors safe-commit).
    git add -f -- "${REQ_PATHS[@]}" 2>/dev/null || true

    # (E) IN_SCOPE = git-expanded files under the pathspec.
    local in_scope
    in_scope="$(git diff --cached --name-only -- "${REQ_PATHS[@]}" 2>/dev/null || true)"

    # (F) SENSITIVE-LEAK GATE (fail-closed). Override: SAFE_COMMIT_ALLOW_SENSITIVE.
    local hits
    hits="$(cw_sensitive_hits "$in_scope")"
    if [ -n "$hits" ]; then
      local n; n="$(printf '%s\n' "$hits" | grep -c .)"
      if [ -n "${SAFE_COMMIT_ALLOW_SENSITIVE:-}" ]; then
        mkdir -p "$(dirname "$audit_log")" 2>/dev/null || true
        echo "${ts} SENSITIVE-OVERRIDE  ${a_name}  ${n}  ($(printf '%s' "$hits" | tr '\n' ' '))  reason=${SAFE_COMMIT_ALLOW_SENSITIVE}" >> "$audit_log"
      else
        # space-safe per-file unstage (mirrors safe-commit's array reset)
        local hf
        while IFS= read -r hf; do [ -n "$hf" ] && git reset -q HEAD -- "$hf" 2>/dev/null || true; done <<< "$hits"
        mkdir -p "$(dirname "$audit_log")" 2>/dev/null || true
        echo "${ts} SENSITIVE-BLOCK  ${a_name}  ${n}  ($(printf '%s' "$hits" | tr '\n' ' '))" >> "$audit_log"
        echo "REJ|1|sensitive-leak blocked (${n} file(s)): $(printf '%s' "$hits" | tr '\n' ' ')"
        exit 0
      fi
    fi

    # (G) commit, with bounded retry on TRANSIENT faults only.
    # CRITICAL: capture via FILES (not $(git commit ...)) + `-c gc.auto=0` + </dev/null.
    # `git commit` can spawn a DETACHED `gc --auto` child that inherits a command-
    # substitution stdout pipe and holds it open -> $(git commit) HANGS forever even
    # though the commit landed. Redirecting git's stdout to a FILE means the gc child
    # inherits the file fd (not the capture pipe); gc.auto=0 suppresses the spawn
    # entirely; </dev/null prevents any stdin block. (Proven: a bare $()-capture hung
    # at 12s with the commit already landed.)
    local attempt=1 rc cout cerr
    local of="${TMPDIR:-/tmp}/cw_out.$REQ_ID" ef="${TMPDIR:-/tmp}/cw_err.$REQ_ID"
    while [ "$attempt" -le "$COMMIT_MAX_ATTEMPTS" ]; do
      git -c gc.auto=0 commit --only "${REQ_CARGS[@]}" -- "${REQ_PATHS[@]}" >"$of" 2>"$ef" </dev/null
      rc=$?
      cout="$(cat "$of" 2>/dev/null || true)"; cerr="$(cat "$ef" 2>/dev/null || true)"
      rm -f "$of" "$ef" 2>/dev/null || true
      if [ "$rc" -eq 0 ]; then
        echo "OK|0|$(git rev-parse HEAD 2>/dev/null)"
        exit 0
      fi
      if cw_is_transient "$cerr" && [ "$attempt" -lt "$COMMIT_MAX_ATTEMPTS" ]; then
        local delay=$(( BACKOFF_BASE_S * (1 << (attempt - 1)) ))
        [ "$delay" -gt "$BACKOFF_CAP_S" ] && delay="$BACKOFF_CAP_S"
        sleep "$delay"
        attempt=$(( attempt + 1 ))
        continue
      fi
      # deterministic (hook/gate/nothing-to-commit/bad-path) OR transient-exhausted
      if cw_is_transient "$cerr"; then
        echo "ERR|${rc}|transient-exhausted after ${attempt} attempts: $(printf '%s' "$cerr" | tr '\n' ' ' | cut -c1-300)"
      else
        echo "REJ|${rc}|$(printf '%s' "$cerr" | tr '\n' ' ' | cut -c1-300)"
      fi
      exit 0
    done
    echo "ERR|1|worker-loop-fell-through"
  )"

  # (H) classify the subshell verdict and emit result / DLQ.
  local verd="${outcome%%|*}"; local rest="${outcome#*|}"
  local rc2="${rest%%|*}"; local reason="${rest#*|}"
  case "$verd" in
    OK)
      cq_write_result "$REQ_ID" committed 0 "$reason" "" "" ""
      rm -f "$proc" 2>/dev/null || true
      cw_metric committed 1
      log "req $REQ_ID committed $reason"
      ;;
    REJ)
      cq_write_result "$REQ_ID" rejected "$rc2" "" "$reason" "" "$reason"
      rm -f "$proc" 2>/dev/null || true
      cw_metric rejected_count 1
      log "req $REQ_ID rejected rc=$rc2: $reason"
      ;;
    ERR|*)
      cq_write_result "$REQ_ID" error "$rc2" "" "$reason" "" "$reason"
      cq_dlq "$proc"; cw_metric dlq_depth 1
      log "req $REQ_ID ERROR->DLQ rc=$rc2: $reason"
      ;;
  esac
}

# ---- startup sweep: crash-orphans in processing/ ------------------------
# A request in processing/ with no worker = a prior worker crashed mid-flight.
# CONSERVATIVE: we do NOT auto-requeue (a crash in the ~ms between `git commit`
# returning and writing the result would double-commit on requeue). Instead,
# aged orphans -> DLQ + error result + alarm; a human/ops decides. (Hardening
# path for deterministic recovery: stamp PRE_HEAD before commit + compare HEAD
# author/message on recovery -- noted for TO-1 hardening / CTO arch-gate.)
cw_startup_sweep() {
  local proc_dir; proc_dir="$(cq_processing_dir)"
  local f base age now mt
  now="$(cq_now_epoch)"
  for f in "$proc_dir"/*.req; do
    [ -f "$f" ] || continue
    mt="$(stat -c %Y "$f" 2>/dev/null || echo "$now")"
    age=$(( now - mt ))
    base="$(basename "$f")"
    local rid; rid="$(cq_field "$f" REQID)"
    log "startup-sweep orphan $base (age ${age}s) -> DLQ (conservative, no auto-requeue)"
    [ -n "$rid" ] && cq_write_result "$rid" error 1 "" "crash-orphan recovered to DLQ; re-run your commit" "" ""
    cq_dlq "$f"; cw_metric dlq_depth 1
  done
}

# ---- daemon main loop ---------------------------------------------------
cw_daemon() {
  cw_acquire_singleton
  trap 'cw_release_singleton; exit 0' TERM INT
  trap 'cw_release_singleton' EXIT
  log "daemon up (concurrency=1); root=$(cq_root)"
  cw_startup_sweep
  while true; do
    cq_heartbeat; cw_metric worker_liveness 1
    local proc
    if proc="$(cq_claim_oldest)"; then
      cw_process "$proc"
    else
      cw_metric queue_depth 0
      sleep "$WORKER_POLL_SEC"
    fi
  done
}

# ---- --drain-once (test): process exactly one request, then exit --------
cw_drain_once() {
  cw_acquire_singleton
  trap 'cw_release_singleton; exit 0' TERM INT
  trap 'cw_release_singleton' EXIT
  cw_startup_sweep
  local proc
  if proc="$(cq_claim_oldest)"; then
    cw_process "$proc"
    echo "drained 1 request"
  else
    echo "queue empty"
  fi
}

# ---- --status -----------------------------------------------------------
cw_status() {
  local root; root="$(cq_root)" || { echo "not in a git repo"; return 1; }
  if cq_worker_alive; then echo "worker: ALIVE (pid $(cat "$(cq_worker_pid)" 2>/dev/null))"; else echo "worker: DOWN (client would fall back to mutex)"; fi
  local d
  for d in requests processing results dlq; do
    printf '  %-11s %s\n' "$d" "$(ls -1 "$root/$d" 2>/dev/null | grep -c . || echo 0)"
  done
}

# ========================================================================
# --selftest: end-to-end single-request commit round-trip + concurrency=1
# proof, in a THROWAWAY temp git repo (never touches ajb_workspace .git).
# ========================================================================
cw_selftest() {
  local tmp; tmp="${TMPDIR:-/tmp}/cw_selftest_$$"
  rm -rf "$tmp" 2>/dev/null; mkdir -p "$tmp" || { echo "FAIL mktemp"; return 1; }
  (
    cd "$tmp" || exit 1
    git init -q .
    git config user.email "worker@opal.agent"; git config user.name "worker"
    git commit -q --allow-empty -m "root" --author "seed <seed@opal.agent>"
    echo "hello" > a.txt

    # IN-PROCESS test: this selftest already runs inside the worker process, so it
    # claims + calls cw_process DIRECTLY -- no nested `bash commit-worker.sh`
    # subprocess (which spawns MSYS job-control + git-gc-in-subprocess fragility and
    # is compute-heavy). cw_process is proven in-process below.

    # (1) ROUND-TRIP: author carries a ~lane suffix + the message carries shell-nasty
    # chars -> interface + R4 attribution + fidelity proof. cargs = --author X -m MSG.
    local author='0.7.0_AE_CloudOps~B <0.7.0_AE_CloudOps@opal.agent>'
    local msg='feat(x): round-trip [pure] "q" $V `c`'
    local rid proc
    rid="$(cq_enqueue "$tmp" 0 "$author" 4 "--author" "$author" "-m" "$msg" 1 "a.txt" 0)" || { echo "FAIL enqueue"; exit 1; }
    proc="$(cq_claim_oldest)" || { echo "FAIL claim"; exit 1; }
    cw_process "$proc"

    if ! cq_result_ready "$rid"; then echo "FAIL: no result written"; exit 1; fi
    local rp status hash
    rp="$(cq_result_path "$rid")"
    status="$(cq_field "$rp" STATUS)"
    hash="$(cq_field "$rp" COMMIT_HASH)"
    [ "$status" = "committed" ] || { echo "FAIL status=$status reason=$(cq_b64dec "$(cq_field "$rp" REASON)")"; exit 1; }
    local landed_author landed_msg
    landed_author="$(git log -1 --format='%an <%ae>' 2>/dev/null)"
    landed_msg="$(git log -1 --format='%s' 2>/dev/null)"
    [ "$hash" = "$(git rev-parse HEAD)" ] || { echo "FAIL hash mismatch"; exit 1; }
    [ "$landed_author" = "$author" ] || { echo "FAIL R4 author: [$landed_author] != [$author]"; exit 1; }
    [ "$landed_msg" = "$msg" ]       || { echo "FAIL msg fidelity: [$landed_msg] != [$msg]"; exit 1; }
    echo "  committed hash=${hash:0:12} R4-requester-attribution=OK msg-fidelity=OK"

    # (2) SENSITIVE-LEAK fail-closed: pathspec sweeps a gitignored .env with a secret
    # -> worker must REJECT, NOT commit it.
    printf 'evil/\n' > .gitignore
    mkdir -p evil; printf 'AWS_SECRET_ACCESS_KEY=xxx\n' > evil/.env
    git add -f .gitignore >/dev/null 2>&1
    local rid2 proc2
    rid2="$(cq_enqueue "$tmp" 0 "$author" 4 "--author" "$author" "-m" "leak test" 1 "evil/.env" 0)" || { echo "FAIL enqueue2"; exit 1; }
    proc2="$(cq_claim_oldest)" || { echo "FAIL claim2"; exit 1; }
    cw_process "$proc2"
    local s2; s2="$(cq_field "$(cq_result_path "$rid2")" STATUS)"
    [ "$s2" = "rejected" ] || { echo "FAIL sensitive gate did not reject (status=$s2)"; exit 1; }
    git log --all --oneline 2>/dev/null | grep -qi "leak test" && { echo "FAIL: secret got committed"; exit 1; }
    echo "  sensitive-leak gate fail-closed=OK (evil/.env rejected, not committed)"

    # (3) SINGLETON / concurrency=1 guard: plant a KNOWN-LIVE pid ($$, alive + != a
    # child worker's pid) in worker.pid; cw_acquire_singleton must refuse (print
    # "another worker alive ... singleton" + exit). Run it in a subshell so its
    # exit 0 doesn't end the test; capture its stderr.
    cq_init
    printf '%s' "$PPID" > "$(cq_worker_pid)"   # a DIFFERENT live pid (not $$, which the guard treats as self)
    local guard; guard="$( ( cw_acquire_singleton ) 2>&1 )"
    rm -f "$(cq_worker_pid)" 2>/dev/null || true
    printf '%s' "$guard" | grep -qi "singleton" || { echo "FAIL: guard did NOT refuse a live holder (out=$guard)"; exit 1; }
    echo "  singleton/concurrency=1 guard=OK (acquire refused while a live pid held worker.pid)"

    echo "PASS: commit-worker selftest (round-trip + R4-attribution + msg-fidelity + sensitive-fail-closed + singleton)"
  )
  local rc=$?
  rm -rf "$tmp" 2>/dev/null || true
  return $rc
}

# ---- dispatch -----------------------------------------------------------
case "${1:-}" in
  --drain-once) cw_drain_once ;;
  --selftest)   cw_selftest ;;
  --status)     cw_status ;;
  ""|--daemon)  cw_daemon ;;
  *) echo "usage: commit-worker.sh [--daemon|--drain-once|--selftest|--status]" >&2; exit 2 ;;
esac
