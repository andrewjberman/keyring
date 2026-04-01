#!/usr/bin/env bash
# check-inbox.sh — one-shot inbox check for Opal agents
#
# Usage:
#   bash org/mcp/check-inbox.sh <agent_serial>
#
# Checks the agent's inbox directory once.
# Prints any pending messages and moves them to read/.
# Exits with 0 whether or not messages were found.
#
# Contrast with inbox-watch.sh, which loops until a message arrives
# (designed for background task notification on delivery).
# Use check-inbox.sh for startup checks and manual polling.

SERIAL="${1:?Usage: check-inbox.sh <agent_serial>}"
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

# Collect pending messages
FOUND=0
for f in "$INBOX"/*.md; do
    [ -f "$f" ] || continue
    FOUND=1
    break
done

if [ "$FOUND" -eq 0 ]; then
    echo "[check-inbox] No pending messages for $SERIAL"
    exit 0
fi

echo ""
echo "[check-inbox] Messages for $SERIAL:"
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
echo "[check-inbox] All messages read. Re-launch inbox-watch.sh to monitor for new ones."
echo "===================================================================="
