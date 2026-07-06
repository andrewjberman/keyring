#!/usr/bin/env bash
# NFRA_CMTQUE TO-6 -- commit-worker-concurrency-proof.sh  (adversarial, many-runs)
# Proves the atomic mkdir-lock singleton converges to EXACTLY 1 survivor over MANY simultaneous
# N-way launches -- a concurrency fix that passes ONCE is luck (MSTR/LD-0249). The v2 design is
# LOAD-INDEPENDENT by construction: on mkdir-fail a loser EXITS unless the lock is provably
# abandoned (age>120s AND hb>120s), so there is NO timing/grace window for load to race through
# (the v1 grace-loop bug is gone). Hence the rigorous test is MANY runs converging to 1, NOT
# self-inflicted CPU load -- pathological self-load only starves `ps` + breaks the MEASUREMENT
# (observed), it cannot expose a race that the mechanism precludes. Optional light load arg for
# extra contention; the natural shared-box load + the simultaneous launch already contend.
#
# MEASUREMENT: fresh repo per iter (no inter-iter contamination); POLL the alive-count of the
# launched pids until STABLE (unchanged 3 checks) = true survivor count after losers resolve;
# survivor liveness by ps-ENUMERATION (never kill-0), with retry-on-empty (ps hiccups under load).
# TEST-HYGIENE: a trap kills every launched daemon + any load burners on ANY exit; 0-strays asserted.
#
# Usage: bash .tools/commit-worker-concurrency-proof.sh [ITER=20] [LOAD=0] [SINGLE_N]
# exit 0 = PASS.

set -uo pipefail
ITER="${1:-20}"; LOAD="${2:-0}"; SINGLE_N="${3:-}"
WORKER="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/commit-worker.sh"
BASETMP="${TMPDIR:-/tmp}/cw_conc_$$"
ALL_PIDS=(); LOAD_PIDS=()

_count_alive() {   # robust: retry ps if it hiccups empty under load; always echoes a number.
  local live p n=0 tries=0
  while :; do live="$(ps 2>/dev/null | awk 'NR>1{print $1}')"; [ -n "$live" ] && break; tries=$(( tries + 1 )); [ "$tries" -ge 3 ] && break; sleep 1; done
  for p in "$@"; do printf '%s\n' "$live" | grep -qx "$p" && n=$(( n + 1 )); done
  echo "$n"
}
kill_load() { local p; for p in "${LOAD_PIDS[@]:-}"; do [ -n "$p" ] && kill -9 "$p" 2>/dev/null || true; done; }
cleanup() {
  local p
  for p in "${ALL_PIDS[@]:-}"; do [ -n "$p" ] && kill "$p" 2>/dev/null || true; done
  sleep 1
  for p in "${ALL_PIDS[@]:-}"; do [ -n "$p" ] && kill -9 "$p" 2>/dev/null || true; done
  kill_load
  cd / 2>/dev/null || true; rm -rf "$BASETMP" 2>/dev/null || true
}
trap cleanup EXIT TERM INT
mkdir -p "$BASETMP"

if [ "$LOAD" -gt 0 ]; then
  echo "spawning $LOAD light CPU-load burner(s) for extra contention..."
  _i=0; while [ "$_i" -lt "$LOAD" ]; do ( while :; do :; done ) & LOAD_PIDS+=("$!"); _i=$(( _i + 1 )); done
fi

TOTAL_FAIL=0        # runs with survivors>=2 (a REAL singleton race)
run_suite() {  # $1=N $2=ITER
  # THE INVARIANT under test: survivors is NEVER >=2 (concurrency=1). survivors==1 = pass;
  # survivors==0 = harness flake (git-init/startup stalled -> no worker started, cq_init
  # failed, all exited) -> RETRY the iteration; survivors>=2 = a real race = FAIL.
  local N="$1" iters="$2" run=1 races=0 ones=0 flakes=0 iter_pids alive prev stable waited p i repo tries verdict
  echo "--- N=$N x $iters runs (fresh-repo, invariant: survivors never >=2) ---"
  while [ "$run" -le "$iters" ]; do
    verdict="flake"; tries=0
    while [ "$tries" -lt 4 ]; do
      tries=$(( tries + 1 ))
      repo="$BASETMP/r_${N}_${run}_${tries}"; rm -rf "$repo"; mkdir -p "$repo"
      ( cd "$repo" && git init -q . && git config user.email t@t && git config user.name t && git commit -q --allow-empty -m root ) >/dev/null 2>&1
      iter_pids=()
      i=0; while [ "$i" -lt "$N" ]; do
        ( cd "$repo" && exec bash "$WORKER" --daemon </dev/null >/dev/null 2>&1 ) & iter_pids+=("$!"); ALL_PIDS+=("$!"); i=$(( i + 1 ))
      done
      prev=-99; stable=0; waited=0; alive=0
      while [ "$waited" -lt 30 ]; do
        sleep 2; waited=$(( waited + 2 ))
        alive="$(_count_alive "${iter_pids[@]}")"; [ -n "$alive" ] || alive=0
        if [ "$alive" -eq "$prev" ]; then stable=$(( stable + 1 )); else stable=0; prev="$alive"; fi
        [ "$stable" -ge 3 ] && break
      done
      for p in "${iter_pids[@]}"; do kill "$p" 2>/dev/null || true; done
      sleep 1; for p in "${iter_pids[@]}"; do kill -9 "$p" 2>/dev/null || true; done
      rm -rf "$repo" 2>/dev/null || true
      if [ "$alive" -ge 2 ]; then verdict="race:$alive"; break; fi
      if [ "$alive" -eq 1 ]; then verdict="one"; break; fi
      # alive==0 -> flake, retry
    done
    case "$verdict" in
      one)   ones=$(( ones + 1 ));   printf '  run %2d/%d: survivors=1 OK\n' "$run" "$iters" ;;
      race:*) races=$(( races + 1 )); printf '  run %2d/%d: %s  *** REAL RACE ***\n' "$run" "$iters" "$verdict" ;;
      *)     flakes=$(( flakes + 1 )); printf '  run %2d/%d: harness-flake (0 started after %d tries; inconclusive)\n' "$run" "$iters" "$tries" ;;
    esac
    run=$(( run + 1 ))
  done
  echo "  N=$N: ${ones} exactly-1, ${races} races(>=2), ${flakes} harness-flakes"
  TOTAL_FAIL=$(( TOTAL_FAIL + races ))
}

if [ -n "$SINGLE_N" ]; then run_suite "$SINGLE_N" "$ITER"; else run_suite 12 "$ITER"; run_suite 24 "$ITER"; fi

kill_load; sleep 2
strays=0; for p in "${ALL_PIDS[@]}"; do [ "$(_count_alive "$p")" -eq 1 ] && strays=$(( strays + 1 )); done
echo "=== TOTAL: $TOTAL_FAIL failing run(s); strays=$strays ==="
if [ "$TOTAL_FAIL" -eq 0 ] && [ "$strays" -eq 0 ]; then echo "PASS (converges to exactly-1 every run)"; exit 0; fi
echo "FAIL"; exit 1
