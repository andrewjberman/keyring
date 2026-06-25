#!/usr/bin/env bash
# comprail-gate1-fptest.sh -- the AC#5 over-gate guard for NFRA_COMPRAIL TO-6 LEG-A Gate-1
# (CTO 2026-06-25). Proves the estate-scoped broad-repo-grep DENY does NOT false-deny legitimate
# generic / no-graph / pipe-grep / single-file / override searches, AND does deny the intended
# comp_which-estate broad grep -- BOTH with the enforce marker ON and (the zero-change default) OFF.
#
# SAFETY: the test toggles the REAL marker org/mcp/comprail-gate1.enforce; a leaked marker would
# enforce Gate-1 fabric-wide. A trap removes it on ANY exit (pass/fail/interrupt). It also refuses to
# run if the marker already exists (so the test never clobbers a real operator-set enforce state).
#
# Run from workspace root:  bash .tools/comprail-gate1-fptest.sh [--verbose]
# Exit 0 = all cases as expected; exit 1 = a regression (a false-deny or a missed-deny).
set -uo pipefail

WS="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$WS/.tools/hooks/comp-tool-hud.sh"
MARKER="$WS/org/mcp/comprail-gate1.enforce"
VERBOSE=0; [ "${1:-}" = "--verbose" ] && VERBOSE=1

if [ -f "$MARKER" ]; then
  echo "REFUSE: $MARKER already exists (operator enforce state) -- not running the toggle test to avoid clobbering it."
  exit 2
fi
trap 'rm -f "$MARKER" 2>/dev/null || true' EXIT INT TERM

# decision(command, marker_state) -> DENY | ADVISE | FREE   (FREE = exit 0, no JSON: silent/override/no-match)
decision() {
  local cmd="$1"
  local enc; enc=$(printf '%s' "$cmd" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))')
  printf '{"tool_name":"Bash","session_id":"gate1-fptest","tool_input":{"command":%s}}' "$enc" \
    | bash "$HOOK" 2>/dev/null | python -c '
import json,sys
s=sys.stdin.read().strip()
if not s: print("FREE"); raise SystemExit
try:
  h=json.loads(s).get("hookSpecificOutput",{})
  if h.get("permissionDecision")=="deny": print("DENY")
  elif h.get("additionalContext"): print("ADVISE")
  else: print("FREE")
except Exception: print("FREE")'
}

# cases: state(on|off) | expected | command
CASES=(
  # marker OFF -- the zero-change default: Gate-1 never fires, current behavior intact
  "off|ADVISE|grep -rn compute_aua data/bd/scripts/"
  "off|ADVISE|grep -rn baz newproject/"
  "off|ADVISE|cat file.py | grep x"
  "off|DENY|grep -rn thing infra/aws/terraform/"
  # marker ON -- Gate-1 enforces, narrow estate scope, everything else stays free
  "on|DENY|grep -rn compute_aua data/bd/scripts/"
  "on|DENY|grep -Rn helper data/inf/scripts/"
  "on|ADVISE|grep -rn baz newproject/"
  "on|ADVISE|grep -rn thing src/somelib/"
  "on|ADVISE|cat file.py | grep x"
  "on|ADVISE|git log | grep fix"
  "on|FREE|grep -rn foo deck_generation/engine/"
  "on|ADVISE|rg pattern"
  "on|FREE|grep -rn x data/bd/scripts/ # rail-checked: no comp-tool fits this exact search"
  "on|DENY|grep -rn thing infra/aws/terraform/"
)

fails=0; n=0
for row in "${CASES[@]}"; do
  state="${row%%|*}"; rest="${row#*|}"; exp="${rest%%|*}"; cmd="${rest#*|}"
  n=$((n+1))
  if [ "$state" = on ]; then : > "$MARKER"; else rm -f "$MARKER"; fi
  got=$(decision "$cmd")
  rm -f "$MARKER"
  if [ "$got" != "$exp" ]; then
    fails=$((fails+1))
    printf '  FAIL [marker %-3s] exp=%-7s got=%-7s  %s\n' "$state" "$exp" "$got" "$cmd"
  elif [ "$VERBOSE" = 1 ]; then
    printf '  ok   [marker %-3s] %-7s  %s\n' "$state" "$got" "$cmd"
  fi
done

echo ""
echo "comprail Gate-1 FP-test (AC#5): $((n-fails))/$n cases as expected"
if [ "$fails" -ne 0 ]; then echo "RESULT: FAIL ($fails over/under-gate regressions)"; exit 1; fi
echo "RESULT: PASS -- no false-deny on generic/no-graph/pipe-grep/single-file/override; estate broad-grep denies under marker; marker-OFF = zero change."
exit 0
