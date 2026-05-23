#!/usr/bin/env bash
# append-commitment.sh -- record an active-work commitment that survives turn
# boundaries.
#
# Ported from corporeal mcp_runner/append-commitment.sh (2026-05-20). Adapted
# to the ajb_workspace tilde-lane-aware inbox layout: the ledger lives in the
# same watched directory inbox-watch.sh polls, alongside .unread-deliveries.
#
# Usage:
#   bash org/mcp/append-commitment.sh <SERIAL> "<DESCRIPTION>"
#
#   <SERIAL>      = your own agent serial (incl. ~lane suffix if any)
#   <DESCRIPTION> = single-line plain-text description of the committed work
#
# Appends `<ISO_TIMESTAMP>|<DESCRIPTION>` to the agent's .active-commitments
# ledger. The supervisor /loop body Step 0.5 (org/XXX.md) cats this file every
# tick; if non-empty it executes each committed line in-turn before end-turn --
# a deterministic failsafe against the supervisor-loop-swallows-active-work
# failure mode. Pop completed lines with complete-commitment.sh.
#
# Call this at turn-end when you state "next turn I'll do X". If you finish the
# work in the SAME turn, do NOT append. The post-send-commitment.sh PostToolUse
# hook calls this automatically when an outbound send_message carries commitment
# language -- manual invocation is the fallback for commitments the hook missed.

set -euo pipefail

SERIAL="${1:?Usage: append-commitment.sh <SERIAL> \"<DESCRIPTION>\"}"
DESCRIPTION="${2:?Usage: append-commitment.sh <SERIAL> \"<DESCRIPTION>\"}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INBOX_BASE="$SCRIPT_DIR/inbox"

# Resolve tilde-lane-aware watched inbox dir (mirrors inbox-watch.sh).
BASE_SERIAL="${SERIAL%%~*}"
SUFFIX=""
[ "$SERIAL" != "$BASE_SERIAL" ] && SUFFIX="${SERIAL#*~}"

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
    echo "ERROR: no agent folder found matching '$BASE_SERIAL'" >&2
    exit 1
fi

if [ -n "$SUFFIX" ]; then
    WATCH_DIR="$INBOX_BASE/$AGENT_DIR/~$SUFFIX"
else
    WATCH_DIR="$INBOX_BASE/$AGENT_DIR"
fi
mkdir -p "$WATCH_DIR"
LEDGER="$WATCH_DIR/.active-commitments"

# Reject newlines (one commitment per line) and pipes (field separator).
stripped="${DESCRIPTION//$'\n'/}"
if [ ${#stripped} -ne ${#DESCRIPTION} ]; then
    echo "ERROR: DESCRIPTION must be single-line (no newlines)" >&2
    exit 1
fi
case "$DESCRIPTION" in
    *"|"*) echo "ERROR: DESCRIPTION must not contain '|' (field separator)" >&2; exit 1 ;;
esac

ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "${ISO}|${DESCRIPTION}" >> "$LEDGER"
echo "[append-commitment] appended: ${ISO}|${DESCRIPTION}" >&2
