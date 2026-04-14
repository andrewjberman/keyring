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

INBOX="$INBOX_BASE/$AGENT_DIR"
mkdir -p "$INBOX/read"

# Determine if a message file is addressed to this instance.
# Returns 0 (match) when any of:
#   1. No ~suffix on SERIAL (base serial watches all messages)
#   2. Message **To:** field matches SERIAL exactly (e.g. ~A gets ~A messages)
#   3. Message **To:** field matches BASE_SERIAL (broadcast to all instances)
#   4. Message has no **To:** field (legacy/malformed -- only base serial picks these up)
is_for_me() {
    local f="$1"

    # No suffix -- base serial agent takes everything
    if [ "$SERIAL" = "$BASE_SERIAL" ]; then
        return 0
    fi

    # Read To: line from file content
    local to_line
    to_line=$(grep -m1 "^\*\*To:\*\*" "$f" 2>/dev/null || true)

    if [ -z "$to_line" ]; then
        # No To: field -- skip (base serial would have caught it above)
        return 1
    fi

    # Exact match on full serial (e.g. **To:** 0.4.0_DS_ClientPlatform~A)
    if echo "$to_line" | grep -qF "$SERIAL"; then
        return 0
    fi

    # Match on base serial with no suffix (broadcast message)
    # Only match if the To: value IS the base serial exactly (not another ~sibling)
    if echo "$to_line" | grep -qE "\*\*To:\*\* ${BASE_SERIAL}$"; then
        return 0
    fi

    return 1
}

# Poll until message(s) addressed to this instance arrive, then print and exit.
# Self-respawning: before exiting, a child watcher is spawned so the inbox
# is never unmonitored. The parent exits to trigger the Claude Code task
# notification (queue drain); the child catches anything that arrives during
# the parent's processing window.
while true; do
    FOUND_FOR_ME=0
    for f in "$INBOX"/*.md; do
        [ -f "$f" ] || continue
        if is_for_me "$f"; then
            FOUND_FOR_ME=1
            break
        fi
    done

    if [ "$FOUND_FOR_ME" -eq 1 ]; then
        echo ""
        echo "[INBOX] New messages for $SERIAL:"
        echo ""
        for msg in "$INBOX"/*.md; do
            [ -f "$msg" ] || continue
            if is_for_me "$msg"; then
                # Claim atomically via mv before printing. If two watchers
                # race (self-spawn + manual relaunch overlap), only the one
                # that wins the mv delivers the message; the other sees no file.
                dest="$INBOX/read/$(basename "$msg")"
                mv "$msg" "$dest" 2>/dev/null || continue
                echo "===================================================================="
                echo "FROM: $(basename "$dest")"
                echo "===================================================================="
                cat "$dest"
                echo ""
            fi
            # Messages for other ~siblings are left in place -- not archived
        done
        echo "===================================================================="
        echo ""
        # NO self-respawn. An orphan child's stdout is disconnected from the
        # Claude Code Bash-tool tracker, so if the orphan wins the atomic mv
        # race on a subsequent message, the task-notification never fires
        # and the message is silently swallowed. Agents MUST relaunch this
        # script via the Bash tool (run_in_background=true) after each
        # notification so every delivery has a tracked owner.
        exit 0
    fi
    sleep 5
done
