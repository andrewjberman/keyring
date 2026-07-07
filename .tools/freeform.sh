#!/usr/bin/env bash
# freeform.sh -- arm / off / status the comp-tool RAIL escape (Andrew-invoked speed mode).
#
# WHAT IT SUSPENDS: ONLY the comp-tool RAIL discipline for ONE session -- the comp-tool-hud nudge
#   (comp-which-first) + the future NFRA_COMPRAIL grep/aws-inspection GATE. While armed, the agent
#   may grep/glob/aws-inspect freely (off the graph rail) to move fast.
# WHAT IT DOES NOT TOUCH: every SAFETY/CORRECTNESS gate -- safe-commit, owned-paths, surface-check,
#   commit-gate, never-widen, HALTGT, destructive-op confirmations. freeform = exploration SPEED,
#   NOT a license to bypass deploy/ownership/safety. Those stay fully armed.
# PROPERTIES: per-session (keyed by session id) | TIME-BOXED + auto-expiring (can't silently become
#   the permanent default) | LOGGED (every window on the record, comp-tool-hud.log) | Andrew-authorized.
# The comp-tool-hud hook reads the marker directly + fails CLOSED (any parse issue -> rail ENFORCED).
set -uo pipefail
WS="$(cd "$(dirname "$0")/.." 2>/dev/null && pwd)" || WS="."
SESS="$WS/org/mcp/sessions"; LOG="$WS/org/mcp/comp-tool-hud.log"
cmd="${1:-status}"; sid="${2:-}"; dur="${3:-60}"
[ -z "$sid" ] && { echo "freeform: need a session id (arg 2). usage: freeform.sh {arm|off|status} <sid> [duration_min]"; exit 1; }
mkdir -p "$SESS" 2>/dev/null || true
ff="$SESS/${sid}.freeform"
now=$(date +%s 2>/dev/null || echo 0)
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')

case "$cmd" in
  arm|on)
    case "$dur" in ''|*[!0-9]*) dur=60 ;; esac        # non-numeric -> default 60m
    [ "$dur" -lt 1 ] 2>/dev/null && dur=1
    [ "$dur" -gt 240 ] 2>/dev/null && dur=240         # hard cap 4h (auto-expire is the safety)
    exp=$(( now + dur * 60 ))
    printf '%s\n' "$exp" > "$ff" 2>/dev/null || { echo "freeform: could not write marker"; exit 1; }
    echo "$ts  FREEFORM-ARM  sid=$sid  dur=${dur}m  expires=$exp" >> "$LOG" 2>/dev/null || true
    echo "freeform ARMED for $sid: ${dur}m. comp-tool RAIL stood down (grep/glob/aws-inspect freely)."
    echo "  SAFETY gates UNAFFECTED (safe-commit / owned-paths / surface-check / never-widen still enforced)."
    echo "  auto-expires in ${dur}m; '/freeform off' to end early. Logged." ;;
  off|stop)
    rm -f "$ff" 2>/dev/null || true
    echo "$ts  FREEFORM-OFF  sid=$sid" >> "$LOG" 2>/dev/null || true
    echo "freeform OFF for $sid: comp-tool rail RE-ARMED." ;;
  status)
    if [ -f "$ff" ]; then
      exp=$(tr -dc '0-9' < "$ff" 2>/dev/null)
      if [ -n "$exp" ] && [ "$now" -lt "$exp" ] 2>/dev/null; then
        echo "freeform ACTIVE for $sid: ~$(( (exp - now) / 60 ))m remaining (rail stood down)."
      else
        echo "freeform EXPIRED for $sid (rail ENFORCED; stale marker -- run 'off' to clear)."
      fi
    else echo "freeform OFF for $sid (rail ENFORCED)."; fi ;;
  *) echo "usage: freeform.sh {arm|off|status} <sid> [duration_min]"; exit 1 ;;
esac
