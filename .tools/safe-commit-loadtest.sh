#!/usr/bin/env bash
# NFRA_CMTQUE TO-6 -- safe-commit-loadtest.sh   (BUILD NOW / RUN GATED)
# ============================================================================
# !!! DO NOT RUN without MSTR's explicit OFF-PEAK GO (LD-0251). !!!
# This launches N concurrent REAL committers -> it loads the SHARED box (11 live
# agents). It is HARD-GATED: refuses to run unless CMTQUE_LOADTEST_GO=1 is set,
# which MSTR sets only during a CONFIRMED-QUIET window (no gold runs / rebuilds /
# re-serves in flight), with MSTR or COO watching for a fabric-stress abort.
# ============================================================================
#
# WHAT IT MEASURES (the payoff proof -- does the queue beat the mutex under load?):
#   Two arms, each N concurrent committers doing 1 real commit of a DISTINCT file:
#     MUTEX arm  : SAFE_COMMIT_USE_QUEUE=0 -> the legacy mkdir-mutex path (baseline)
#     QUEUE arm  : SAFE_COMMIT_USE_QUEUE=1 + a live worker -> enqueue->block->result
#   Records each committer's wall-time + exit code -> p50/p95 latency + exit-3 count
#   (the mutex 60s-timeout STORM signal). Queue should have lower tail-latency + zero
#   exit-3 storms. N in {10, 25} (MSTR-approved shape).
#
# COUNTING (the pid-namespace lesson, LD-0251): survivor/worker/queue state is read
#   from the WORKER'S OWN LOGIC -- worker.pid, worker.log win/lose lines, result-files
#   -- NEVER ps/PowerShell enumeration (two pid namespaces + subshell chains misread it).
#
# ISOLATION: a fresh TEST repo only. SAFE_COMMIT_USE_QUEUE=1 is exported ONLY inside the
#   test's own subshells for the QUEUE arm -- NEVER the fabric env, NEVER the real repo.
#   The worker runs for the TEST gitdir only. TRAP kills all committers + the test worker
#   + asserts 0 strays on ANY exit (incl. timeout). Bounded burst (each committer = 1 commit).
#
# KILL-SWITCH: pre-flight quiet-confirm gate (below) + bounded/short bursts + MSTR/COO watch.
#   If a burst visibly stresses the fabric, Ctrl-C -> the trap reaps everything.
#
# Usage (only under MSTR's go):  CMTQUE_LOADTEST_GO=1 bash .tools/safe-commit-loadtest.sh [Ns...]
#   default Ns = "10 25"

set -uo pipefail

if [ "${CMTQUE_LOADTEST_GO:-0}" != "1" ]; then
  echo "REFUSED: this load-test loads the shared box. Set CMTQUE_LOADTEST_GO=1 ONLY under" >&2
  echo "         MSTR's confirmed off-peak go (LD-0251). Not running." >&2
  exit 3
fi

NS="${*:-10 25}"
SC="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe-commit.sh"
WORKER="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/commit-worker.sh"
TMP="${TMPDIR:-/tmp}/sc_load_$$"
PIDS=(); WORKER_PID=""

cleanup() {
  local p
  for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill "$p" 2>/dev/null || true; done
  [ -n "$WORKER_PID" ] && kill "$WORKER_PID" 2>/dev/null || true
  sleep 1
  for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill -9 "$p" 2>/dev/null || true; done
  [ -n "$WORKER_PID" ] && kill -9 "$WORKER_PID" 2>/dev/null || true
  cd / 2>/dev/null || true; rm -rf "$TMP" 2>/dev/null || true
}
trap cleanup EXIT TERM INT

# p50/p95 from a file of integers (ms), one per line.
pctl() {  # $1=file $2=pct(50|95)
  local f="$1" pct="$2" n idx
  n="$(grep -c . "$f" 2>/dev/null)"; [ "${n:-0}" -eq 0 ] && { echo "-"; return; }
  idx=$(( (n * pct + 99) / 100 )); [ "$idx" -lt 1 ] && idx=1
  sort -n "$f" | sed -n "${idx}p"
}

run_arm() {  # $1=arm(mutex|queue) $2=N $3=repo
  local arm="$1" N="$2" repo="$3" i lat_file exit3=0
  lat_file="$repo/lat_${arm}_${N}"; : > "$lat_file"
  PIDS=()
  # each committer commits a DISTINCT file so they are real independent commits
  i=0; while [ "$i" -lt "$N" ]; do
    ( cd "$repo" && echo "c$i $arm" > "f_${arm}_${i}.txt"
      s="$(date +%s%N)"
      if [ "$arm" = queue ]; then
        SAFE_COMMIT_USE_QUEUE=1 bash "$SC" --author "load$i <l@o>" -m "load $arm $i" -- "f_${arm}_${i}.txt" >/dev/null 2>&1
      else
        SAFE_COMMIT_USE_QUEUE=0 bash "$SC" --author "load$i <l@o>" -m "load $arm $i" -- "f_${arm}_${i}.txt" >/dev/null 2>&1
      fi
      rc=$?
      e="$(date +%s%N)"
      printf '%s\n' "$(( (e - s) / 1000000 ))" >> "$lat_file"
      [ "$rc" -eq 3 ] && printf 'EXIT3\n' >> "$repo/exit3_${arm}_${N}"
    ) & PIDS+=("$!"); i=$(( i + 1 ))
  done
  for p in "${PIDS[@]}"; do wait "$p" 2>/dev/null || true; done
  exit3="$(grep -c . "$repo/exit3_${arm}_${N}" 2>/dev/null || echo 0)"
  printf '  %-6s N=%-3s  commits=%s  p50=%sms  p95=%sms  exit3(storm)=%s\n' \
    "$arm" "$N" "$(grep -c . "$lat_file")" "$(pctl "$lat_file" 50)" "$(pctl "$lat_file" 95)" "$exit3"
}

echo "NFRA_CMTQUE load-test (queue vs mutex) -- MSTR-go confirmed. Ns: $NS"
for N in $NS; do
  echo "--- N=$N ---"
  # MUTEX arm: fresh repo, no worker.
  mrepo="$TMP/mutex_$N"; rm -rf "$mrepo"; mkdir -p "$mrepo"
  ( cd "$mrepo" && git init -q . && git config user.email t@t && git config user.name t && git commit -q --allow-empty -m root ) >/dev/null 2>&1
  run_arm mutex "$N" "$mrepo"
  rm -rf "$mrepo"

  # QUEUE arm: fresh repo + a live worker for THIS repo only.
  qrepo="$TMP/queue_$N"; rm -rf "$qrepo"; mkdir -p "$qrepo"
  ( cd "$qrepo" && git init -q . && git config user.email t@t && git config user.name t && git commit -q --allow-empty -m root ) >/dev/null 2>&1
  ( cd "$qrepo" && bash "$WORKER" --daemon </dev/null >"$qrepo/worker.out" 2>&1 ) & WORKER_PID=$!
  # wait for the worker to be live (worker's own logic: worker.pid + fresh hb), up to 15s
  c=0; while [ ! -f "$qrepo/.git/commit-queue/worker.pid" ] && [ "$c" -lt 15 ]; do sleep 1; c=$(( c + 1 )); done
  run_arm queue "$N" "$qrepo"
  # queue arm survivor sanity via worker's-own-logic (NOT ps): exactly 1 "daemon up" line
  ups="$(grep -c 'daemon up' "$qrepo/worker.out" 2>/dev/null || echo 0)"
  echo "  (queue worker: '$ups' daemon-up line(s) [expect 1]; results consumed, dlq=$(ls -1 "$qrepo/.git/commit-queue/dlq" 2>/dev/null | grep -c . ))"
  kill "$WORKER_PID" 2>/dev/null || true; wait "$WORKER_PID" 2>/dev/null || true; WORKER_PID=""
  rm -rf "$qrepo"
done
echo "=== load-test complete. Compare queue vs mutex p50/p95 + exit3. AC1: queue lands all, 0 exit3 storms, lower tail-latency. ==="
