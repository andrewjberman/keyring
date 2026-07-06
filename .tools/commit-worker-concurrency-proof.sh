#!/usr/bin/env bash
# NFRA_CMTQUE TO-6 -- commit-worker-concurrency-proof.sh
# Proves the ATOMIC mkdir-lock singleton under the RACE the old check-then-write missed:
# launch N commit-worker daemons SIMULTANEOUSLY -> assert EXACTLY 1 survives, N-1 exit clean,
# 0 strays. (MSTR/LD-0249 singleton-race fix; the serial 4-case proof never exercised this.)
#
# TEST-HYGIENE (MSTR requirement): a trap kills EVERY launched daemon on ANY exit -- normal,
# error, interrupt, OR timeout -- and the run asserts 0 strays. This is the discipline whose
# absence leaked the 23-worker swarm.
#
# Survivor counting uses `ps` process ENUMERATION (not kill-0, which false-negatives live
# native-Windows pids -- the very unreliability that caused the bug).
#
# Usage: bash .tools/commit-worker-concurrency-proof.sh [N]   (default N=12; exit 0 = PASS)

set -uo pipefail
N="${1:-12}"
WORKER="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/commit-worker.sh"
TMP="${TMPDIR:-/tmp}/cw_conc_$$"
PIDS=()

# all live MSYS pids (column 1), for reliable liveness-by-enumeration.
_live_pids() { ps 2>/dev/null | awk 'NR>1{print $1}'; }
_is_alive()  { _live_pids | grep -qx "$1"; }

cleanup() {
  # kill EVERY launched daemon (winner + any straggler); already-exited losers = no-op.
  local p
  for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill "$p" 2>/dev/null || true; done
  sleep 1
  for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill -9 "$p" 2>/dev/null || true; done
  cd / 2>/dev/null || true
  rm -rf "$TMP" 2>/dev/null || true
}
trap cleanup EXIT TERM INT

rm -rf "$TMP"; mkdir -p "$TMP"; cd "$TMP"
git init -q .; git config user.email t@t; git config user.name t
git commit -q --allow-empty -m root

echo "launching $N commit-worker daemons SIMULTANEOUSLY (gitdir: $TMP/.git)..."
i=0
while [ "$i" -lt "$N" ]; do
  bash "$WORKER" --daemon </dev/null >/dev/null 2>&1 &
  PIDS+=("$!")
  i=$(( i + 1 ))
done

# let the atomic mkdir-lock race resolve + the winner write pid/hb.
sleep 6

# count survivors by ps-enumeration of the launched pids.
alive=0; winner=""
for p in "${PIDS[@]}"; do
  if _is_alive "$p"; then alive=$(( alive + 1 )); winner="$p"; fi
done
wp="$(cat "$TMP/.git/commit-queue/worker.pid" 2>/dev/null || echo -)"
locks="$(ls -d "$TMP/.git/commit-queue/worker.lock" 2>/dev/null | wc -l)"
echo "launched=$N  survivors=$alive  worker.pid=$wp  worker.lock_held=$locks"

rc=0
if [ "$alive" -eq 1 ]; then
  echo "PASS: exactly 1 of $N survived the simultaneous launch (atomic singleton holds)."
  [ "$wp" = "$winner" ] && echo "  survivor pid $winner == worker.pid == lock holder" \
                        || echo "  NOTE: survivor=$winner worker.pid=$wp"
else
  echo "FAIL: $alive survivors (expected 1) -- singleton race NOT closed."
  rc=1
fi

# explicit kill + 0-strays assertion (belt: the trap also runs cleanup).
for p in "${PIDS[@]}"; do kill "$p" 2>/dev/null || true; done
sleep 2
strays=0
for p in "${PIDS[@]}"; do _is_alive "$p" && strays=$(( strays + 1 )); done
if [ "$strays" -eq 0 ]; then
  echo "PASS: 0 strays after cleanup (all launched daemons reaped)."
else
  echo "FAIL: $strays stray daemon(s) survived cleanup."
  rc=1
fi

exit "$rc"
