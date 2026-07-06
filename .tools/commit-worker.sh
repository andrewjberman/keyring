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

# ${BASH_SOURCE[0]} (not $0) so SCRIPT_DIR resolves correctly whether this file is
# executed OR sourced (CW_SOURCE_ONLY=1 by a test / TO-2's fallback -- when sourced,
# $0 is the sourcing shell, not this script).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=commit_queue_lib.sh
source "$SCRIPT_DIR/commit_queue_lib.sh"
# SHARED sensitive-leak gate (TO-5): single source of the leak patterns + detector,
# also sourced by safe-commit's fallback (TO-2) -> no security-gate copy-drift.
# shellcheck source=commit_gate_lib.sh
source "$SCRIPT_DIR/commit_gate_lib.sh"

# ---- config -------------------------------------------------------------
WORKER_POLL_SEC="${CQ_WORKER_POLL_SEC:-1}"      # idle poll interval
COMMIT_MAX_ATTEMPTS="${CQ_COMMIT_MAX_ATTEMPTS:-5}"
BACKOFF_BASE_S="${CQ_BACKOFF_BASE_S:-1}"
BACKOFF_CAP_S="${CQ_BACKOFF_CAP_S:-15}"
ORPHAN_MAX_AGE_SEC="${CQ_ORPHAN_MAX_AGE_SEC:-120}"  # processing/ orphan -> DLQ

# sensitive-leak patterns + detector now live in commit_gate_lib.sh (cg_sensitive_hits) --
# single source shared with safe-commit's fallback (TO-5, CTO no-drift directive).

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

# ---- cargs value extractor ----------------------------------------------
# Echo the value following <flag> in REQ_CARGS (e.g. --author, -m). Used for the
# R4 author single-source (env must derive from the SAME value git uses) and for
# crash-recovery landed-commit matching. rc 1 if the flag is absent.
cw_cargs_value() {
  local flag="$1" i=0
  while [ "$i" -lt "${#REQ_CARGS[@]}" ]; do
    if [ "${REQ_CARGS[$i]}" = "$flag" ] && [ "$((i+1))" -lt "${#REQ_CARGS[@]}" ]; then
      printf '%s' "${REQ_CARGS[$((i+1))]}"; return 0
    fi
    i=$((i+1))
  done
  return 1
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

  # PRE_HEAD stamp (CTO v1: crash-recovery determinism). Record the requester's
  # pre-commit HEAD into the processing record BEFORE committing, so a startup
  # sweep can tell landed-from-not-landed after a worker crash (never double-commit,
  # never lose a landed commit to the DLQ).
  local pre_head
  pre_head="$(cd "$REQ_CWD" 2>/dev/null && git rev-parse HEAD 2>/dev/null || true)"
  printf 'PRE_HEAD %s\n' "$pre_head" >> "$proc" 2>/dev/null || true

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
    # The hook keys on `git var GIT_AUTHOR_IDENT` (author, NOT committer). Export
    # GIT_AUTHOR_* SINGLE-SOURCED from the SAME --author value git will use for the
    # commit (CTO confirm 2a: env and --author must never diverge) -- parse it from
    # CARGS, fall back to the AUTHOR field only if --author is somehow absent.
    local auth_src a_name a_email
    auth_src="$(cw_cargs_value --author)"; [ -n "$auth_src" ] || auth_src="$REQ_AUTHOR"
    a_name="${auth_src%% <*}"
    a_email="${auth_src#*<}"; a_email="${a_email%>}"
    export GIT_AUTHOR_NAME="$a_name"
    export GIT_AUTHOR_EMAIL="$a_email"

    # (D) stage the declared pathspec (-f: force past .gitignore, mirrors safe-commit).
    git add -f -- "${REQ_PATHS[@]}" 2>/dev/null || true

    # (E) IN_SCOPE = git-expanded files under the pathspec.
    local in_scope
    in_scope="$(git diff --cached --name-only -- "${REQ_PATHS[@]}" 2>/dev/null || true)"

    # (F) SENSITIVE-LEAK GATE (fail-closed) via the SHARED detector. Override: SAFE_COMMIT_ALLOW_SENSITIVE.
    local hits
    hits="$(cg_sensitive_hits "$in_scope")"
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

# ---- startup sweep: crash-orphans in processing/ (PRE_HEAD deterministic) ---
# A request in processing/ with no worker = a prior worker crashed mid-flight.
# Using the PRE_HEAD stamp (CTO v1), recovery is a clean binary under concurrency=1:
#   - HEAD advanced AND the top commit's author+subject MATCH the orphan  -> it LANDED
#       -> recover the hash, write a committed-result, NO requeue (never double-commit,
#          never lose a landed commit to the DLQ).
#   - HEAD == PRE_HEAD (unchanged)                                        -> did NOT land
#       -> safe to REQUEUE (mv back to requests/); it will be retried.
#   - HEAD advanced but does NOT match (another commit intervened), or no PRE_HEAD/parse
#     fail                                                                -> AMBIGUOUS
#       -> conservative DLQ + error result (never blind-requeue -- the cardinal
#          never-double-commit invariant wins over convenience).
cw_startup_sweep() {
  local proc_dir reqs_dir f
  proc_dir="$(cq_processing_dir)"; reqs_dir="$(cq_requests_dir)"
  for f in "$proc_dir"/*.req; do
    [ -f "$f" ] || continue
    if ! cw_parse_request "$f"; then
      log "startup-sweep: CORRUPT orphan $(basename "$f") -> DLQ"
      cq_dlq "$f"; cw_metric dlq_depth 1; continue
    fi
    local pre_head cur_head
    pre_head="$(cq_field "$f" PRE_HEAD)"
    cur_head="$(cd "$REQ_CWD" 2>/dev/null && git rev-parse HEAD 2>/dev/null || true)"

    if [ -n "$cur_head" ] && [ -n "$pre_head" ] && [ "$cur_head" = "$pre_head" ]; then
      # proven NOT landed -> safe requeue
      if mv "$f" "$reqs_dir/$(basename "$f")" 2>/dev/null; then
        log "startup-sweep: orphan $REQ_ID proven-not-landed (HEAD==PRE_HEAD) -> REQUEUED"
      else
        cq_write_result "$REQ_ID" error 1 "" "crash-orphan requeue failed; re-run" "" ""
        cq_dlq "$f"; cw_metric dlq_depth 1
        log "startup-sweep: orphan $REQ_ID requeue mv failed -> DLQ"
      fi
    elif [ -n "$cur_head" ] && [ "$cur_head" != "$pre_head" ]; then
      # HEAD advanced -- did THIS request land? match author + subject.
      local want_author want_msg top_author top_msg
      want_author="$(cw_cargs_value --author || true)"
      want_msg="$(cw_cargs_value -m || true)"; want_msg="${want_msg%%$'\n'*}"
      top_author="$(cd "$REQ_CWD" 2>/dev/null && git log -1 --format='%an <%ae>' 2>/dev/null || true)"
      top_msg="$(cd "$REQ_CWD" 2>/dev/null && git log -1 --format='%s' 2>/dev/null || true)"
      if [ -n "$want_author" ] && [ "$top_author" = "$want_author" ] && [ "$top_msg" = "$want_msg" ]; then
        cq_write_result "$REQ_ID" committed 0 "$cur_head" "" "recovered: commit landed before crash" ""
        rm -f "$f" 2>/dev/null || true; cw_metric recovered_committed 1
        log "startup-sweep: orphan $REQ_ID LANDED pre-crash -> recovered hash $cur_head (no requeue)"
      else
        cq_write_result "$REQ_ID" error 1 "" "crash-orphan: HEAD advanced by another commit; re-run" "" ""
        cq_dlq "$f"; cw_metric dlq_depth 1
        log "startup-sweep: orphan $REQ_ID AMBIGUOUS (HEAD moved, no author/subject match) -> DLQ"
      fi
    else
      # no PRE_HEAD or cwd/HEAD unresolvable -> conservative DLQ (never blind-requeue)
      cq_write_result "$REQ_ID" error 1 "" "crash-orphan indeterminate (no PRE_HEAD or HEAD unreadable); re-run" "" ""
      cq_dlq "$f"; cw_metric dlq_depth 1
      log "startup-sweep: orphan $REQ_ID indeterminate -> DLQ"
    fi
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

    # (4) CRASH-RECOVERY (PRE_HEAD determinism). Both branches -- never double-commit,
    # never lose a landed commit.
    local rauthor='0.7.0_AE_CloudOps~B <0.7.0_AE_CloudOps@opal.agent>'

    # (4a) LANDED orphan: enqueue, claim, stamp PRE_HEAD, ACTUALLY make the commit
    # (simulating "worker committed then crashed before writing the result"), sweep.
    local pre_a rid_a proc_a rmsg_a='recover me A'
    pre_a="$(git rev-parse HEAD)"
    rid_a="$(cq_enqueue "$tmp" 0 "$rauthor" 4 "--author" "$rauthor" "-m" "$rmsg_a" 1 "reccA.txt" 0)"
    proc_a="$(cq_claim_oldest)"
    printf 'PRE_HEAD %s\n' "$pre_a" >> "$proc_a"
    echo A > reccA.txt; git add -f reccA.txt >/dev/null 2>&1
    git -c gc.auto=0 commit -q --author "$rauthor" -m "$rmsg_a" -- reccA.txt >/dev/null 2>&1 </dev/null
    cw_startup_sweep >/dev/null 2>&1
    local ra_status ra_hash
    ra_status="$(cq_field "$(cq_result_path "$rid_a")" STATUS)"
    ra_hash="$(cq_field "$(cq_result_path "$rid_a")" COMMIT_HASH)"
    [ "$ra_status" = "committed" ]          || { echo "FAIL recovery-LANDED status=$ra_status"; exit 1; }
    [ "$ra_hash" = "$(git rev-parse HEAD)" ] || { echo "FAIL recovery-LANDED hash mismatch"; exit 1; }
    [ ! -f "$proc_a" ]                       || { echo "FAIL recovery-LANDED: processing not cleared"; exit 1; }
    [ -z "$(ls "$(cq_requests_dir)" 2>/dev/null)" ] || { echo "FAIL recovery-LANDED: REQUEUED a landed commit (double-commit risk)"; exit 1; }
    echo "  crash-recovery LANDED=OK (recovered hash ${ra_hash:0:12}, NO requeue)"

    # (4b) NOT-LANDED orphan: enqueue, claim, stamp PRE_HEAD=current HEAD, NO commit,
    # sweep -> must REQUEUE (HEAD unchanged = proven not landed), no result, no dup.
    local pre_b rid_b proc_b
    pre_b="$(git rev-parse HEAD)"
    rid_b="$(cq_enqueue "$tmp" 0 "$rauthor" 4 "--author" "$rauthor" "-m" "not landed B" 1 "reccB.txt" 0)"
    proc_b="$(cq_claim_oldest)"
    printf 'PRE_HEAD %s\n' "$pre_b" >> "$proc_b"
    cw_startup_sweep >/dev/null 2>&1
    ls "$(cq_requests_dir)"/*"$rid_b"* >/dev/null 2>&1 || { echo "FAIL recovery-NOTLANDED: not requeued"; exit 1; }
    [ ! -f "$proc_b" ]                              || { echo "FAIL recovery-NOTLANDED: still in processing"; exit 1; }
    cq_result_ready "$rid_b" && { echo "FAIL recovery-NOTLANDED: wrote a result (should just requeue)"; exit 1; }
    rm -f "$(cq_requests_dir)"/*"$rid_b"* 2>/dev/null || true
    echo "  crash-recovery NOT-LANDED=OK (requeued, HEAD==PRE_HEAD, no double-commit)"

    echo "PASS: commit-worker selftest (round-trip + R4-attribution + msg-fidelity + sensitive-fail-closed + singleton + crash-recovery)"
  )
  local rc=$?
  rm -rf "$tmp" 2>/dev/null || true
  return $rc
}

# ---- dispatch -----------------------------------------------------------
# CW_SOURCE_ONLY=1 loads the functions WITHOUT dispatching -- lets tests (and
# TO-2's safe-commit fallback) source the worker's helpers without launching a daemon.
if [ "${CW_SOURCE_ONLY:-}" != "1" ]; then
case "${1:-}" in
  --drain-once) cw_drain_once ;;
  --selftest)   cw_selftest ;;
  --status)     cw_status ;;
  ""|--daemon)  cw_daemon ;;
  *) echo "usage: commit-worker.sh [--daemon|--drain-once|--selftest|--status]" >&2; exit 2 ;;
esac
fi
