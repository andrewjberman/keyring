#!/usr/bin/env bash
# inbox-watch.sh — inbox watcher for Opal agents
#
# TWO MODES:
#
#   stream  (PREFERRED, post-LD persistent-Monitor model):
#       bash org/mcp/inbox-watch.sh <agent_serial> stream
#     Run this UNDER THE MONITOR TOOL (persistent: true), NOT Bash
#     run_in_background. Polls forever; on each new .md it mv's the message to
#     read/, appends .unread-deliveries, and emits ONE stdout line
#     ("[INBOX] <file>"). The Monitor tool turns each stdout line into a chat
#     notification, so the agent is interrupted per message while it keeps
#     working. The watcher NEVER exits -> no relaunch cycle, no single-watcher
#     race, no auto-respawn orphan, no tracker subsystem. Survives in-session
#     compaction (it's a session task). Armed ONCE at load by /watcher; the
#     only thing that ends it is the session itself (a fresh session re-arms).
#
#   legacy  (DEFAULT, exit-on-delivery — retained ONLY for in-flight agents
#            launched under the pre-LD /watcher; do not use for new launches):
#       bash org/mcp/inbox-watch.sh <agent_serial>
#     Polls every 5s; on the first delivery it prints the message(s) and EXITS,
#     firing a Bash-tool background-task completion notification. The agent must
#     re-launch after every notification. This is the design the whole
#     failure-mode catalog (ORPHAN / MULTIPLE / RELATIVE-PATH /
#     AUTO-RESPAWN-INTERRUPT-LOST / the misleading exit-143) grew up around.
#
# Per-tilde isolation (2026-04-20) — both modes:
#   - Serial WITHOUT ~suffix watches ONLY the base dir (inbox/<agent>/)
#   - Serial WITH ~suffix watches ONLY the nested dir
#     (inbox/<agent>/~<suffix>/) -- strictly isolated from base + siblings
#   - No body filtering needed: filesystem routing makes every message in
#     the watched dir unambiguously addressed to this instance.

set -euo pipefail

SERIAL="${1:?Usage: inbox-watch.sh <agent_serial> [stream]}"
MODE="${2:-legacy}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INBOX_BASE="$SCRIPT_DIR/inbox"

# Single-watcher guard: legacy mode only. Stream mode is single-instanced
# structurally — /watcher checks the session TaskList before arming, and the
# atomic mv below makes any accidental double-stream exactly-once anyway (the
# loser's mv fails -> `|| continue` -> it emits nothing). The legacy guard's
# `$NF == ser` test would not even match a stream launch (last field is
# "stream", not the serial), so we skip it explicitly.
if [ "$MODE" != "stream" ]; then
# Single-watcher guard: if another inbox-watch.sh is already running for this
# exact serial, exit immediately. Prevents accidental double-launch races on
# the atomic mv (one winner's task-notification fires, the other's is lost).
# Uses pgrep -f pattern match on the script path + serial. $$ is excluded.
# pgrep may be absent on some minimal shells; failure falls through silently.
if command -v pgrep >/dev/null 2>&1; then
    existing=$(pgrep -f "inbox-watch\.sh $SERIAL$" 2>/dev/null | grep -v "^$$\$" || true)
elif command -v ps >/dev/null 2>&1; then
    existing=$(ps -ef | grep -v eval | awk -v ser="$SERIAL" -v me="$$" '$2 != me && $NF == ser && $0 ~ "inbox-watch[.]sh" {print $2}')
else
    existing=""
fi
for pid in $existing; do
    ppid=$(ps -p "$pid" -o ppid= 2>/dev/null | tr -d ' ') || true
    if [ -z "$ppid" ] || ! kill -0 "$pid" 2>/dev/null; then
        echo "inbox-watch: reaping dead watcher pid $pid (process gone)" >&2
        kill "$pid" 2>/dev/null || true
    else
        echo "inbox-watch already running for $SERIAL (pid $pid, parent $ppid alive). Exiting." >&2
        exit 0
    fi
done
fi  # end legacy-only single-watcher guard

# Split serial into base + tilde suffix.
# 0.4.0_DS_ClientPlatform~D -> BASE=0.4.0_DS_ClientPlatform, SUFFIX=D
BASE_SERIAL="${SERIAL%%~*}"
SUFFIX=""
if [ "$SERIAL" != "$BASE_SERIAL" ]; then
    SUFFIX="${SERIAL#*~}"
fi

# Resolve agent folder name (match on base serial)
AGENT_DIR=""
for tier in tier0_exec tier0_utility tier1_exec tier2_senior tier3_junior; do
    for d in "$SCRIPT_DIR/../$tier"/*/; do
        [ -d "$d" ] || continue
        case "$(basename "$d")" in
            *"$BASE_SERIAL"*) AGENT_DIR="$(basename "$d")"; break 2 ;;
        esac
    done
done

if [ -z "$AGENT_DIR" ]; then
    echo "ERROR: No agent folder found matching '$BASE_SERIAL'" >&2
    exit 1
fi

# Resolve the single watched dir based on isolation rules.
if [ -n "$SUFFIX" ]; then
    WATCH_DIR="$INBOX_BASE/$AGENT_DIR/~$SUFFIX"
else
    WATCH_DIR="$INBOX_BASE/$AGENT_DIR"
fi
mkdir -p "$WATCH_DIR/read"

# ===========================================================================
# STREAM MODE (preferred): persistent poll, one stdout line per message, never
# exits. Run under the Monitor tool (persistent: true). The Monitor turns each
# emitted line into a chat notification. mv-on-emit makes delivery exactly-once
# and keeps check-inbox's top-level view clean. No respawn, no guard, no
# tracker -- the whole exit-on-delivery machinery below is bypassed.
# ===========================================================================
if [ "$MODE" = "stream" ]; then
    # ------------------------------------------------------------------------
    # PARENT-LIVENESS SELF-EXIT (2026-07-14, 0.0.0_AB_MSTR -- the orphan-thief
    # ROOT fix). This loop was `while true` with NO exit path: when a session
    # died, the harness reaped the Monitor task + eval wrapper but NOT this
    # child, which kept polling forever -- mv'ing messages to read/ (below)
    # before echoing into a dead pipe. An orphan is not inert, it is a thief:
    # dead MSTR's orphan drained both of COO's respawn requests during the
    # 2026-07-13 70-min zero-builder outage, while every reachability probe
    # read REACHABLE (w>0 BECAUSE the orphan ran; u==0 BECAUSE it drained).
    # The register-hook reap treats that symptom at the NEXT registration --
    # a serial that never returns leaves an orphan nothing collects. THIS
    # exits the thief at the source, within one poll cycle of parent death.
    #
    #   - $PPID is the Monitor's eval wrapper (an MSYS bash -- visible in ps).
    #     TaskStop/session end reaps the wrapper but not this child (exercised
    #     2026-07-10: wrapper 701462 reaped, child 701546 survived). kill -0
    #     on the dead wrapper then fails here -> clean exit 0.
    #   - PPID<=1 = native/unknown parent (MSYS renders a non-MSYS parent as
    #     1; a naive check would suicide healthy watchers -- the documented
    #     7-false-positive trap). FAIL OPEN: skip the check, behavior is
    #     exactly pre-fix. Never kill on a probe that cannot see its subject.
    #   - INBOX_WATCH_NO_PARENT_CHECK=1 disables the check (debug/manual runs).
    #   - Windows PID recycling can only delay the exit by one lifetime, never
    #     cause a false one mid-flight; the failure direction is the safe one.
    # ------------------------------------------------------------------------
    WATCH_PARENT="$PPID"
    PARENT_CHECK=1
    if [ -n "${INBOX_WATCH_NO_PARENT_CHECK:-}" ] || [ "$WATCH_PARENT" -le 1 ]; then
        PARENT_CHECK=0
    fi
    # NO-SPAWN WAIT (Andrew cleanup 2026-07-30, MSTR low-level audit): `sleep` is an
    # EXTERNAL binary in Git Bash, so the old loop created ONE PROCESS PER 5s PER
    # WATCHER (~121K/day at 7 watchers), each a Windows CreateProcess + MSYS fork +
    # an EDR filter-driver inspection. `read -t` against a held-open FIFO waits
    # IN-PROCESS: zero spawns per cycle (exercised on this box: rc=142 at exactly
    # the timeout, no child). mkfifo failure falls back to the old sleep --
    # correctness identical, only the spawn cost differs (Rule 16 guarded pattern).
    _WAIT_FIFO="$(mktemp -u 2>/dev/null || echo "/tmp/inbox-watch-wait-$$")"
    _NOSPAWN=0
    if mkfifo "$_WAIT_FIFO" 2>/dev/null; then
        exec 9<>"$_WAIT_FIFO"
        rm -f "$_WAIT_FIFO"
        _NOSPAWN=1
    fi
    _wait5() {
        if [ "$_NOSPAWN" -eq 1 ]; then read -rt 5 -u 9 _ 2>/dev/null || true; else sleep 5; fi
    }
    echo "inbox-watch: STREAM mode for $SERIAL watching $WATCH_DIR (persistent; parent-tied: $([ "$PARENT_CHECK" -eq 1 ] && echo "pid $WATCH_PARENT" || echo "OFF"); wait=$([ "$_NOSPAWN" -eq 1 ] && echo no-spawn || echo sleep))" >&2
    # EXPIRY ALERT (Andrew-direct 2026-09-21 ~01:4xZ): the harness KILLS every Monitor at its
    # timeout (cap 30 min) and a killed watcher says nothing -- the seat goes deaf on an expiry
    # notice it skims past. So the watcher announces its own end: INBOX_WATCH_EXPIRY_SECS
    # (default 1770 = 30 s inside the 30-min cap) after launch it emits ONE stdout line --
    # one Monitor event -- telling the agent to re-run /watcher, then EXITS. Exiting rather
    # than waiting to be killed makes the alert the LAST event of the stream and guarantees
    # no overlap between this watcher and its successor (so /watcher never sees two script
    # rows of its own making). Arm the Monitor with timeout_ms 1800000 or the harness wins
    # the race and this line never prints. 0 disables the alert.
    _EXPIRY_SECS="${INBOX_WATCH_EXPIRY_SECS:-1770}"
    case "$_EXPIRY_SECS" in (*[!0-9]*|"") _EXPIRY_SECS=1770 ;; esac
    SECONDS=0
    while true; do
        if [ "$PARENT_CHECK" -eq 1 ] && ! kill -0 "$WATCH_PARENT" 2>/dev/null; then
            ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown-ts)"
            echo "$ts  WATCHER-SELF-EXIT  serial=$SERIAL  parent=$WATCH_PARENT gone -- exiting instead of orphaning" >> "$SCRIPT_DIR/orphan-audit.log" 2>/dev/null || true
            exit 0
        fi
        for msg in "$WATCH_DIR"/*.md; do
            [ -f "$msg" ] || continue
            base="$(basename "$msg")"
            dest="$WATCH_DIR/read/$base"
            # Atomic claim. If a concurrent stream won the race, our mv fails and
            # we skip silently -> exactly-once emit across any number of streams.
            mv "$msg" "$dest" 2>/dev/null || continue
            printf '%s\n' "$base" >> "$WATCH_DIR/.unread-deliveries"
            # ONE line == ONE Monitor notification. Filename is enough for the
            # agent to read the message from read/ and act.
            echo "[INBOX] $base"
        done
        if [ "$_EXPIRY_SECS" -gt 0 ] && [ "$SECONDS" -ge "$_EXPIRY_SECS" ]; then
            echo "[WATCHER-EXPIRED] inbox watcher for $SERIAL is ENDING NOW after ${SECONDS}s (Monitors are killed at 30 min). YOU ARE NOT RECEIVING MAIL. RE-RUN /watcher NOW to arm a new Monitor -- do not wait for a quiet moment."
            ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown-ts)"
            echo "$ts  WATCHER-EXPIRY-EXIT  serial=$SERIAL  after=${SECONDS}s" >> "$SCRIPT_DIR/orphan-audit.log" 2>/dev/null || true
            exit 0
        fi
        _wait5
    done
    # unreachable
fi

# Tracker write for sub-case-aware watcher-status (per MSTR TARGET B-EXT
# 2026-05-26T~04:45Z; option (a) session-id-keyed tracker file pattern).
# inbox-watch.sh writes its PID + launch-type (LAUNCH | RESPAWN) + ts + serial
# to a session-scoped tracker file; watcher-status.sh reads it to disambiguate
# ORPHAN sub-cases into DETACHED-OK / AUTO-RESPAWN-INTERRUPT-LOST. Tracker file
# is per-session ephemeral; gitignored at org/mcp/tracked_watchers/*.list.
if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    TRACKER_DIR="$SCRIPT_DIR/tracked_watchers"
    mkdir -p "$TRACKER_DIR" 2>/dev/null || true
    TRACKER_FILE="$TRACKER_DIR/${CLAUDE_CODE_SESSION_ID}.list"
    if [ "${INBOX_WATCH_RESPAWN:-}" = "1" ]; then
        LAUNCH_TYPE="RESPAWN"
    else
        LAUNCH_TYPE="LAUNCH"
    fi
    printf '%s|%s|%s|%s\n' "$$" "$LAUNCH_TYPE" "$(date -u +%FT%TZ)" "$SERIAL" >> "$TRACKER_FILE" 2>/dev/null || true
fi

# Poll until message(s) arrive in the watched dir, then print and exit.
# Exit-on-message is load-bearing: Claude Code background task completion fires
# the interrupt that wakes the agent.
#
# Auto-respawn: on delivery, a new untracked copy is spawned (nohup, 1s delay)
# so the inbox is always watched. The untracked copy writes to
# /tmp/inbox-watch-<serial>.log but will NOT fire a Claude Code interrupt.
# To restore full interrupt coverage after the untracked copy has been running
# a while, re-register a tracked instance via run_in_background=true.
while true; do
    FOUND_FOR_ME=0

    for f in "$WATCH_DIR"/*.md; do
        [ -f "$f" ] || continue
        FOUND_FOR_ME=1
        break
    done

    if [ "$FOUND_FOR_ME" -eq 1 ]; then
        echo ""
        echo "[INBOX] New messages for $SERIAL:"
        echo ""

        for msg in "$WATCH_DIR"/*.md; do
            [ -f "$msg" ] || continue
            dest="$WATCH_DIR/read/$(basename "$msg")"
            mv "$msg" "$dest" 2>/dev/null || continue
            # Deterministic delivery sentinel: append the delivered filename to
            # .unread-deliveries. The supervisor /loop body Step 0 (org/XXX.md)
            # cats this file every tick as a failsafe against the agent replying
            # to the task-notification without reading the messages above. The
            # untracked auto-respawn copy also appends here, so deliveries it
            # makes silently (no interrupt) are still recorded for the next tick.
            printf '%s\n' "$(basename "$dest")" >> "$WATCH_DIR/.unread-deliveries"
            echo "===================================================================="
            echo "FROM: $(basename "$dest")"
            echo "===================================================================="
            cat "$dest"
            echo ""
        done

        echo "===================================================================="
        echo ""
        echo "DETERMINISTIC SENTINEL: $WATCH_DIR/.unread-deliveries"
        echo "  Lists the message(s) just delivered. After reading and acting on"
        echo "  them, delete the file. The supervisor /loop body Step 0 cats it"
        echo "  every tick as a failsafe -- see org/XXX.md '/loop' section."
        echo ""
        # Respawn next watcher (untracked). Sleep 1s first so this instance
        # exits before the new copy starts -- otherwise the single-watcher guard
        # in the new copy sees this PID as a live duplicate and kills itself.
        # INBOX_WATCH_RESPAWN=1 marks the respawn for watcher-status sub-case
        # disambiguation per LD-TARGET-B-EXT (MSTR 2026-05-26T~04:45Z).
        SAFE_SERIAL=$(printf '%s' "$SERIAL" | tr '/~' '__')
        ( sleep 1; INBOX_WATCH_RESPAWN=1 exec bash "$0" "$SERIAL" >> "/tmp/inbox-watch-${SAFE_SERIAL}.log" 2>&1 ) &
        disown $! 2>/dev/null || true
        exit 0
    fi
    sleep 5
done
