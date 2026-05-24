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

# Strip ~suffix for folder lookup (0.4.0_DS_ClientPlatform~A -> 0.4.0_DS_ClientPlatform)
BASE_SERIAL="${SERIAL%%~*}"
SUFFIX=""
if [ "$SERIAL" != "$BASE_SERIAL" ]; then
    SUFFIX="${SERIAL#*~}"
fi

# Resolve agent folder name (match on base serial)
AGENT_DIR=""
for tier in tier0_exec tier1_exec tier2_senior tier3_junior; do
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
# - caller with ~suffix reads per-instance dir AND base dir (broadcasts)
# - caller without suffix reads only base dir
INBOX_BASE_DIR="$INBOX_BASE/$AGENT_DIR"
mkdir -p "$INBOX_BASE_DIR/read"
INBOX_DIRS=("$INBOX_BASE_DIR")
if [ -n "$SUFFIX" ]; then
    INBOX_INSTANCE_DIR="$INBOX_BASE/${AGENT_DIR}~${SUFFIX}"
    mkdir -p "$INBOX_INSTANCE_DIR/read"
    INBOX_DIRS=("$INBOX_INSTANCE_DIR" "$INBOX_BASE_DIR")
fi

# Collect pending messages across all applicable dirs
FOUND=0
for d in "${INBOX_DIRS[@]}"; do
    for f in "$d"/*.md; do
        [ -f "$f" ] || continue
        FOUND=1
        break 2
    done
done

if [ "$FOUND" -eq 0 ]; then
    echo "[check-inbox] No pending messages for $SERIAL"
    exit 0
fi

echo ""
echo "[check-inbox] Messages for $SERIAL:"
echo ""
for d in "${INBOX_DIRS[@]}"; do
    for msg in "$d"/*.md; do
        [ -f "$msg" ] || continue
        # Atomic claim via mv before reading. If a concurrent inbox-watch or
        # another check-inbox run wins the race, mv fails and we skip silently.
        dest="$d/read/$(basename "$msg")"
        mv "$msg" "$dest" 2>/dev/null || continue
        echo "===================================================================="
        echo "FROM: $(basename "$dest")"
        echo "===================================================================="
        cat "$dest"
        echo ""
    done
done
echo "===================================================================="
echo "[check-inbox] All messages read. Re-launch inbox-watch.sh to monitor for new ones."
echo "===================================================================="
