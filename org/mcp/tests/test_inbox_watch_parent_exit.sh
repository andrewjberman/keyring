#!/usr/bin/env bash
# Parent-liveness self-exit exercise for inbox-watch.sh stream mode (GA-3 era fix,
# 2026-07-14, 0.0.0_AB_MSTR).
#
# THE DEFECT THIS GUARDS AGAINST RETURNING: the stream loop was `while true` with no
# exit path -- a dead session's watcher kept polling forever, mv'ing messages to read/
# before echoing into a dead pipe (the orphan-thief; dead MSTR's orphan ate COO's two
# respawn requests during the 2026-07-13 zero-builder outage).
#
# THE FIX UNDER TEST: the loop checks its parent (the Monitor eval wrapper) each cycle
# and exits 0 when the parent is gone.
#
# BOTH directions are asserted -- the fix's own failure mode is SUICIDE ON A LIVE
# PARENT (the documented 7-false-positive ppid trap), so the positive control (watcher
# stays up + still delivers while the parent lives) is as load-bearing as the kill.
#
# Uses a nonexistent tilde lane of the MSTR serial so the watch dir is isolated: no
# real traffic, no race with any live watcher (per-tilde isolation).
#
#     bash org/mcp/tests/test_inbox_watch_parent_exit.sh
set -uo pipefail

WS="$(cd "$(dirname "$0")/../../.." && pwd)"
WATCH_SH="$WS/org/mcp/inbox-watch.sh"
SERIAL="0.0.0_AB_MSTR~ZZTESTPX"
WATCH_DIR="$WS/org/mcp/inbox/0.0.0_AB_MSTR/~ZZTESTPX"
OUT="$WS/org/mcp/tests/.test_inbox_watch_parent_exit.out"

PASS=0; FAIL=0
check() { # name, condition-rc (0=pass)
    if [ "$2" -eq 0 ]; then PASS=$((PASS+1)); echo "  PASS  $1";
    else FAIL=$((FAIL+1)); echo "  FAIL  $1"; fi
}

find_child() {
    ps -ef | grep "inbox-watch\.sh $SERIAL stream" | grep -v grep | awk '{print $2}' | head -1
}

cleanup() {
    local c; c="$(find_child)"
    [ -n "$c" ] && kill -9 "$c" 2>/dev/null
    rm -rf "$WATCH_DIR" 2>/dev/null
    rm -f "$OUT" 2>/dev/null
}
trap cleanup EXIT
cleanup 2>/dev/null || true

# Launch under a wrapper we control. The trailing `:` prevents bash's exec
# optimisation, so the watcher is a CHILD of the wrapper (the Monitor topology).
bash -c "bash '$WATCH_SH' '$SERIAL' stream > '$OUT' 2>&1; :" &
WRAPPER=$!

sleep 3
CHILD="$(find_child)"
[ -n "$CHILD" ]; check "watcher child started (detector negative-control: it IS findable)" $?

# POSITIVE CONTROL -- parent alive across >1 poll cycle: the watcher must SURVIVE.
sleep 7
kill -0 "${CHILD:-0}" 2>/dev/null; check "watcher SURVIVES a live parent (no suicide)" $?

# Delivery still works under the parent-check build.
echo "px-test" > "$WATCH_DIR/pxtest.md"
sleep 8
[ -f "$WATCH_DIR/read/pxtest.md" ]; check "message still claimed to read/ (stream delivery intact)" $?
grep -q "\[INBOX\] pxtest.md" "$OUT" 2>/dev/null; check "stream still emits the [INBOX] event" $?

# THE KILL -- reap the wrapper the way TaskStop/session-death does (child NOT reaped).
kill -9 "$WRAPPER" 2>/dev/null
sleep 12   # up to 2 poll cycles + slack
kill -0 "${CHILD:-0}" 2>/dev/null; RC=$?
[ "$RC" -ne 0 ]; check "watcher SELF-EXITED within 2 cycles of parent death (the fix)" $?

tail -5 "$WS/org/mcp/orphan-audit.log" 2>/dev/null | grep -q "WATCHER-SELF-EXIT  serial=$SERIAL"
check "self-exit wrote its WATCHER-SELF-EXIT audit line" $?

echo ""
echo "$PASS passed, $FAIL failed"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
