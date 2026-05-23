#!/usr/bin/env bash
# complete-commitment.sh -- remove a completed commitment from the active ledger.
#
# Ported from corporeal mcp_runner/complete-commitment.sh (2026-05-20). Adapted
# to the ajb_workspace tilde-lane-aware inbox layout.
#
# Usage:
#   bash org/mcp/complete-commitment.sh <SERIAL> <TIMESTAMP_PREFIX>
#
#   <SERIAL>           = your own agent serial (incl. ~lane suffix if any)
#   <TIMESTAMP_PREFIX> = ISO timestamp prefix uniquely identifying the line
#                        (full `2026-05-20T13:14:33Z` or unique prefix)
#
# Removes matching lines from the agent's .active-commitments ledger. If the
# ledger ends up empty it is deleted (parallels .unread-deliveries cleanup).
# Call this after the supervisor /loop body Step 0.5 has fully executed the
# committed work. Sibling pattern: paired write-then-pop with append-commitment.sh.

set -euo pipefail

SERIAL="${1:?Usage: complete-commitment.sh <SERIAL> <TIMESTAMP_PREFIX>}"
PREFIX="${2:?Usage: complete-commitment.sh <SERIAL> <TIMESTAMP_PREFIX>}"

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
LEDGER="$WATCH_DIR/.active-commitments"

if [ ! -f "$LEDGER" ]; then
    echo "[complete-commitment] no ledger; nothing to do" >&2
    exit 0
fi

matched="$(grep -c "^${PREFIX}" "$LEDGER" 2>/dev/null || true)"
if [ "${matched:-0}" -eq 0 ]; then
    echo "[complete-commitment] no commitment lines match prefix: $PREFIX" >&2
    exit 0
fi

TMP="$(mktemp)"
grep -v "^${PREFIX}" "$LEDGER" > "$TMP" || true
mv "$TMP" "$LEDGER"
echo "[complete-commitment] removed $matched line(s) matching: $PREFIX" >&2

if [ ! -s "$LEDGER" ]; then
    rm "$LEDGER"
    echo "[complete-commitment] ledger now empty; removed" >&2
fi
