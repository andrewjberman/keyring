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
# Supports ~suffix instances (e.g. 0.4.0_DS_ClientPlatform~A):
#   - Folder lookup uses base serial (strips ~suffix) so the script
#     finds the shared inbox folder correctly
#   - Message delivery filters by full serial so only messages addressed
#     to THIS instance (or to the base serial) are delivered
#   - Messages for other ~suffix siblings are left untouched in the inbox
#     so their intended recipient can pick them up

set -euo pipefail

SERIAL="${1:?Usage: inbox-watch.sh <agent_serial>}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INBOX_BASE="$SCRIPT_DIR/inbox"

# Single-watcher guard: if another inbox-watch.sh is already running for this
# exact serial, exit immediately. Prevents accidental double-launch races on
# the atomic mv (one winner's task-notification fires, the other's is lost).
# Uses pgrep -f pattern match on the script path + serial. $$ is excluded.
# pgrep may be absent on some minimal shells; failure falls through silently.
if command -v pgrep >/dev/null 2>&1; then
    existing=$(pgrep -f "inbox-watch\.sh $SERIAL$" 2>/dev/null | grep -v "^$$\$" || true)
    if [ -n "$existing" ]; then
        echo "inbox-watch already running for $SERIAL (pid $existing). Exiting." >&2
        exit 0
    fi
fi

# Strip ~suffix for folder lookup (0.4.0_DS_ClientPlatform~A -> 0.4.0_DS_ClientPlatform)
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

# Serialization-aware inbox set (locked 2026-04-16):
# - caller with ~suffix polls per-instance dir FIRST (private, all msgs are mine)
#   then base dir (broadcasts; may collide with ~sibling lanes -- first-mv wins)
# - caller without suffix polls only base dir
# is_for_me body-filter is retained as belt-and-suspenders for pre-migration
# messages or mistargeted sends that land in the base dir.
INBOX_BASE_DIR="$INBOX_BASE/$AGENT_DIR"
mkdir -p "$INBOX_BASE_DIR/read"
INBOX_INSTANCE_DIR=""
if [ -n "$SUFFIX" ]; then
    INBOX_INSTANCE_DIR="$INBOX_BASE/${AGENT_DIR}~${SUFFIX}"
    mkdir -p "$INBOX_INSTANCE_DIR/read"
fi

# Determine if a message file from the BASE dir is addressed to this instance.
# Per-instance dir messages are always for me -- no filter needed.
# Returns 0 (match) when any of:
#   1. No ~suffix on SERIAL (base serial watches all messages)
#   2. Message **To:** field matches SERIAL exactly (legacy pre-migration)
#   3. Message **To:** field matches BASE_SERIAL (broadcast to all instances)
#   4. Message has no **To:** field (legacy/malformed -- only base serial picks up)
is_for_me_in_base() {
    local f="$1"

    # No suffix -- base serial agent takes everything in base dir
    if [ -z "$SUFFIX" ]; then
        return 0
    fi

    local to_line
    to_line=$(grep -m1 "^\*\*To:\*\*" "$f" 2>/dev/null || true)

    if [ -z "$to_line" ]; then
        return 1
    fi

    # Exact match on full serial (pre-migration sends may still use body-only routing)
    if echo "$to_line" | grep -qF "$SERIAL"; then
        return 0
    fi

    # Match on base serial with no suffix (broadcast message)
    if echo "$to_line" | grep -qE "\*\*To:\*\* ${BASE_SERIAL}$"; then
        return 0
    fi

    return 1
}

# Poll until message(s) addressed to this instance arrive, then print and exit.
# NO self-respawn (removed 2026-04-14): agents MUST relaunch via Bash tool
# run_in_background=true after each notification so every delivery has a
# tracked owner (orphan stdout disconnects from Claude Code task tracker).
while true; do
    FOUND_FOR_ME=0

    # Check per-instance dir first (all contents are for me, no filter)
    if [ -n "$INBOX_INSTANCE_DIR" ]; then
        for f in "$INBOX_INSTANCE_DIR"/*.md; do
            [ -f "$f" ] || continue
            FOUND_FOR_ME=1
            break
        done
    fi

    # Check base dir (apply body filter for ~suffix instances)
    if [ "$FOUND_FOR_ME" -eq 0 ]; then
        for f in "$INBOX_BASE_DIR"/*.md; do
            [ -f "$f" ] || continue
            if is_for_me_in_base "$f"; then
                FOUND_FOR_ME=1
                break
            fi
        done
    fi

    if [ "$FOUND_FOR_ME" -eq 1 ]; then
        echo ""
        echo "[INBOX] New messages for $SERIAL:"
        echo ""

        # Per-instance dir: everything is mine, claim all
        if [ -n "$INBOX_INSTANCE_DIR" ]; then
            for msg in "$INBOX_INSTANCE_DIR"/*.md; do
                [ -f "$msg" ] || continue
                dest="$INBOX_INSTANCE_DIR/read/$(basename "$msg")"
                mv "$msg" "$dest" 2>/dev/null || continue
                echo "===================================================================="
                echo "FROM: $(basename "$dest")"
                echo "===================================================================="
                cat "$dest"
                echo ""
            done
        fi

        # Base dir: claim only those matching is_for_me_in_base
        for msg in "$INBOX_BASE_DIR"/*.md; do
            [ -f "$msg" ] || continue
            if is_for_me_in_base "$msg"; then
                dest="$INBOX_BASE_DIR/read/$(basename "$msg")"
                mv "$msg" "$dest" 2>/dev/null || continue
                echo "===================================================================="
                echo "FROM: $(basename "$dest")"
                echo "===================================================================="
                cat "$dest"
                echo ""
            fi
        done

        echo "===================================================================="
        echo ""
        exit 0
    fi
    sleep 5
done
