#!/usr/bin/env bash
# inbox-watch.sh — background inbox watcher for Opal agents
#
# Usage (run in background at session startup):
#   bash org/mcp/inbox-watch.sh <agent_serial>
#
# Polls the agent's inbox directory every 5 seconds.
# When new .md files appear addressed to this instance, prints them and EXITS.
# Exiting triggers a background task completion notification in
# Claude Code, which interrupts the agent and forces them to
# read the messages. The agent MUST re-launch this script after
# processing each notification.
#
# Per-tilde isolation (2026-04-20):
#   - Serial WITHOUT ~suffix watches ONLY the base dir (inbox/<agent>/)
#   - Serial WITH ~suffix watches ONLY the nested dir
#     (inbox/<agent>/~<suffix>/) -- strictly isolated from base + siblings
#   - No body filtering needed: filesystem routing makes every message in
#     the watched dir unambiguously addressed to this instance.

set -euo pipefail

SERIAL="${1:?Usage: inbox-watch.sh <agent_serial>}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INBOX_BASE="$SCRIPT_DIR/cl_inbox"

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

# Split serial into base + tilde suffix.
# 0.4.0_DS_ClientPlatform~D -> BASE=0.4.0_DS_ClientPlatform, SUFFIX=D
BASE_SERIAL="${SERIAL%%~*}"
SUFFIX=""
if [ "$SERIAL" != "$BASE_SERIAL" ]; then
    SUFFIX="${SERIAL#*~}"
fi

# Resolve agent folder name (match on base serial)
AGENT_DIR=""
for tier in tier1_exec tier2_senior tier3_junior; do
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

# Poll until message(s) arrive in the watched dir, then print and exit.
# NO self-respawn (removed 2026-04-14): agents MUST relaunch via Bash tool
# run_in_background=true after each notification so every delivery has a
# tracked owner (orphan stdout disconnects from Claude Code task tracker).
# Exit-on-message is load-bearing -- Claude Code's background task completion
# notification is what interrupts the agent. Do NOT convert to a loop.
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
            echo "===================================================================="
            echo "FROM: $(basename "$dest")"
            echo "===================================================================="
            cat "$dest"
            echo ""
        done

        echo "===================================================================="
        echo ""
        exit 0
    fi
    sleep 5
done
