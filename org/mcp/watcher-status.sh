#!/usr/bin/env bash
# watcher-status.sh -- read-only diagnostic for an agent's inbox-watch health.
#
# Usage:  bash org/mcp/watcher-status.sh <agent_serial>
#
# Scans `ps -ef` for the inbox watcher(s) belonging to <agent_serial>, classifies
# each one, and prints a single VERDICT line the /watcher skill keys on.
# READ-ONLY: never kills, never launches. The /watcher skill owns remediation.
#
# VERDICT values (worst-wins precedence):
#   NONE           no watcher process found for this serial
#   WRONG-CHANNEL  CL agent on the ajb watcher, or a ws agent on the feature_clb watcher
#   MULTIPLE       more than one watcher process for this serial (atomic-mv race)
#   ORPHAN         a watcher has no live eval-launcher parent (PPID=1 / dead / reparented)
#   RELATIVE-PATH  a watcher was launched via the banned relative `org/mcp/inbox-watch.sh`
#   PROCESS-OK     exactly one watcher: correct channel, absolute path, live launcher parent
#
# IMPORTANT: PROCESS-OK means the process *tree* is healthy. It does NOT prove the
# watcher belongs to the CURRENT session. A prior session's watcher also reports
# PROCESS-OK -- and it delivers its exit notification to a dead session, so the
# current session is deaf. Only the session task list proves current-session
# tracking; the /watcher skill checks that in its Step 3.
#
# Rule 16 (CLAUDE.md): uses only Git Bash 3.6.7 default utilities -- ps, awk,
# grep, printf. No pgrep/pkill.

set -uo pipefail
SERIAL="${1:?Usage: watcher-status.sh <agent_serial>}"

# --- channel detection -------------------------------------------------------
# CL-channel agents (the feature_clb / COMP_LEARNS team) watch a separate inbox
# via cl-inbox-watch.sh. Everyone else uses the ajb_workspace inbox-watch.sh.
case "$SERIAL" in
  *CompLearns*|1.1.0_SA_CTO|2.1.0_SA_COO|2.1.0_SC_*) CHANNEL="cl" ;;
  *) CHANNEL="ws" ;;
esac

PSOUT="$(ps -ef 2>/dev/null || true)"

# --- enumerate watcher processes for this EXACT serial -----------------------
# A watcher process cmdline ends with '<...>inbox-watch.sh <SERIAL>'. Exclude
# the eval-launcher wrappers and this diagnostic itself. Exact `$NF == serial`
# match keeps base/tilde lanes isolated (a base query never matches a ~C watcher).
WATCHERS="$(printf '%s\n' "$PSOUT" \
  | grep 'inbox-watch\.sh' \
  | grep -v 'eval' \
  | grep -v 'watcher-status' \
  | awk -v s="$SERIAL" '$NF == s {print $2"|"$3}' || true)"

echo "watcher-status: $SERIAL  (channel: $CHANNEL)"

COUNT=0
[ -n "$WATCHERS" ] && COUNT="$(printf '%s\n' "$WATCHERS" | grep -c . || true)"

if [ "$COUNT" -eq 0 ]; then
  echo "  (no watcher process found for this serial)"
  echo "FLAGS: NONE"
  echo "VERDICT: NONE"
  exit 0
fi

SAW_RELATIVE=0; SAW_ORPHAN=0; SAW_WRONGCHAN=0
while IFS='|' read -r pid ppid; do
  [ -z "$pid" ] && continue
  wline="$(printf '%s\n' "$PSOUT" | awk -v p="$pid" '$2==p')"

  # path form
  if printf '%s' "$wline" | grep -q 'feature_clb'; then
    form="cl"
  elif printf '%s' "$wline" | grep -qE 'bash[[:space:]]+org/mcp/'; then
    form="relative"; SAW_RELATIVE=1
  else
    form="absolute"
  fi

  # channel correctness
  wchan="ws"; [ "$form" = "cl" ] && wchan="cl"
  [ "$wchan" != "$CHANNEL" ] && SAW_WRONGCHAN=1

  # parent classification -- a healthy tracked watcher has a live eval-launcher parent
  if [ "$ppid" = "1" ]; then
    parent="orphan"; SAW_ORPHAN=1
  else
    pline="$(printf '%s\n' "$PSOUT" | awk -v p="$ppid" '$2==p')"
    if [ -z "$pline" ]; then
      parent="orphan(dead-parent)"; SAW_ORPHAN=1
    elif printf '%s' "$pline" | grep -q 'eval'; then
      parent="launcher"
    else
      parent="reparented"; SAW_ORPHAN=1
    fi
  fi

  echo "  PID $pid  parent=$parent($ppid)  pathform=$form"
done <<EOF
$WATCHERS
EOF

# --- ORPHAN sub-case disambiguation (per MSTR TARGET B-EXT 2026-05-26T~04:45Z) -
# Read session-scoped tracker file to distinguish DETACHED-OK (this-session LAUNCH
# whose launcher detached) from AUTO-RESPAWN-INTERRUPT-LOST (this-session RESPAWN
# from inbox-watch.sh:130-137 post-delivery) from PRIOR-SESSION-ORPHAN (not in
# this session's tracker at all). Only fires when COUNT=1 + ORPHAN; multi-PID
# orphans fall through to MULTIPLE.
ORPHAN_SUBCASE=""
if [ "$SAW_ORPHAN" -eq 1 ] && [ "$COUNT" -eq 1 ] && [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
  SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
  TRACKER_FILE="$SCRIPT_DIR/tracked_watchers/${CLAUDE_CODE_SESSION_ID}.list"
  if [ -f "$TRACKER_FILE" ]; then
    ORPHAN_PID="$(printf '%s\n' "$WATCHERS" | head -1 | cut -d'|' -f1)"
    # Look up the latest tracker entry for this PID
    TRACKER_ENTRY="$(grep "^${ORPHAN_PID}|" "$TRACKER_FILE" 2>/dev/null | tail -1)"
    if [ -n "$TRACKER_ENTRY" ]; then
      LAUNCH_TYPE="$(echo "$TRACKER_ENTRY" | cut -d'|' -f2)"
      case "$LAUNCH_TYPE" in
        LAUNCH)  ORPHAN_SUBCASE="DETACHED-OK" ;;
        RESPAWN) ORPHAN_SUBCASE="AUTO-RESPAWN-INTERRUPT-LOST" ;;
      esac
    else
      ORPHAN_SUBCASE="PRIOR-SESSION-ORPHAN"
    fi
  fi
fi

# --- verdict (worst-wins) ----------------------------------------------------
FLAGS=""
[ "$COUNT" -gt 1 ]        && FLAGS="$FLAGS MULTIPLE"
[ "$SAW_WRONGCHAN" -eq 1 ] && FLAGS="$FLAGS WRONG-CHANNEL"
[ "$SAW_ORPHAN" -eq 1 ]    && FLAGS="$FLAGS ORPHAN"
[ "$SAW_RELATIVE" -eq 1 ]  && FLAGS="$FLAGS RELATIVE-PATH"
[ -n "$ORPHAN_SUBCASE" ]   && FLAGS="$FLAGS $ORPHAN_SUBCASE"
echo "FLAGS:${FLAGS:- (none)}"

if   [ "$SAW_WRONGCHAN" -eq 1 ]; then V="WRONG-CHANNEL"
elif [ "$COUNT" -gt 1 ];         then V="MULTIPLE"
elif [ "$SAW_ORPHAN" -eq 1 ] && [ -n "$ORPHAN_SUBCASE" ]; then V="$ORPHAN_SUBCASE"
elif [ "$SAW_ORPHAN" -eq 1 ];    then V="ORPHAN"
elif [ "$SAW_RELATIVE" -eq 1 ];  then V="RELATIVE-PATH"
else V="PROCESS-OK"; fi
echo "VERDICT: $V"

if [ "$V" = "PROCESS-OK" ] || [ "$V" = "DETACHED-OK" ]; then
  echo "NOTE: process-tree health only -- confirm via your session task list that"
  echo "      THIS session launched it. A prior session's watcher also reads OK here."
fi
if [ "$V" = "AUTO-RESPAWN-INTERRUPT-LOST" ]; then
  echo "NOTE: this PID is the legitimate auto-respawn copy from inbox-watch.sh:130-137"
  echo "      (deaf to Claude Code interrupts). Kill + relaunch tracked to restore"
  echo "      interrupt path; deliveries to filesystem still work via .unread-deliveries."
fi
if [ "$V" = "PRIOR-SESSION-ORPHAN" ]; then
  echo "NOTE: this PID does not appear in the current session's tracker file"
  echo "      ($SCRIPT_DIR/tracked_watchers/\${CLAUDE_CODE_SESSION_ID}.list);"
  echo "      kill + relaunch tracked."
fi
