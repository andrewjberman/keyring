#!/usr/bin/env bash
# inbox-watch.sh — background inbox watcher for Opal agents
#
# Usage (run in background at session startup):
#   bash org/mcp/inbox-watch.sh <agent_serial>
#
# Polls the agent's inbox directory every 5 seconds.
# When new .md files appear, prints ALL of them and EXITS.
# Exiting triggers a background task completion notification in
# Claude Code, which interrupts the agent and forces them to
# read the messages. The agent MUST re-launch this script after
# processing each notification.

set -euo pipefail

SERIAL="${1:?Usage: inbox-watch.sh <agent_serial>}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INBOX_BASE="$SCRIPT_DIR/inbox"

# Resolve agent folder name (serial may be partial)
AGENT_DIR=""
for tier in tier1_exec tier2_senior tier3_junior; do
    for d in "$SCRIPT_DIR/../$tier"/*/; do
        [ -d "$d" ] || continue
        case "$(basename "$d")" in
            *"$SERIAL"*) AGENT_DIR="$(basename "$d")"; break 2 ;;
        esac
    done
done

if [ -z "$AGENT_DIR" ]; then
    echo "ERROR: No agent folder found matching '$SERIAL'" >&2
    exit 1
fi

INBOX="$INBOX_BASE/$AGENT_DIR"
mkdir -p "$INBOX/read"

# Poll until message(s) arrive, then print and exit
while true; do
    for f in "$INBOX"/*.md; do
        [ -f "$f" ] || continue

        # Found at least one message — print ALL pending, then exit
        echo ""
        echo "[INBOX] New messages for $SERIAL:"
        echo ""
        for msg in "$INBOX"/*.md; do
            [ -f "$msg" ] || continue
            echo "===================================================================="
            echo "FROM: $(basename "$msg")"
            echo "===================================================================="
            cat "$msg"
            echo ""
            mv "$msg" "$INBOX/read/"
        done
        echo "===================================================================="
        echo ""
        echo "<mandatory>"
        echo "RELAUNCH inbox-watch.sh IMMEDIATELY after acting on the above messages."
        echo "Run: bash org/mcp/inbox-watch.sh $SERIAL"
        echo "Use Bash tool with run_in_background: true. Do NOT use &."
        echo "Without inbox-watch running you will receive NO further messages."
        echo "</mandatory>"
        echo ""
        exit 0
    done
    sleep 5
done
