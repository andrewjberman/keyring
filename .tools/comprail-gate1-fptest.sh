#!/usr/bin/env bash
# comprail-gate1-fptest.sh -- the over/under-gate guard for the Bash search rail in
# .tools/hooks/comp-tool-hud.sh.
#
# HISTORY: 2026-06-25 (CTO) AC#5 for NFRA_COMPRAIL TO-6 LEG-A Gate-1 (estate-scoped broad grep).
# 2026-08-28 (1.0.0_SA_CTO~D, Andrew-direct "All approved" on the /open-calls cards, audit
# org/tier1_exec/1.0.0_SA_CTO/deliverables/COMPRAIL_GREP_GATE_AUDIT_20260828.md): T1 -- EVERY standalone
# repo search in Bash is DENIED per SEGMENT (any path, any lead verb, a pipe elsewhere or not) and
# routed to comp-find; pipe-RECEIVER grep, single-file grep (T2 deferred a week), `# rail-checked:`
# and /freeform stay free; raw-aws INSPECTION denies per segment too (closes the `cd X && aws iam`
# hole CLAUDE.md measured 2026-08-28). The 24 shapes below were the audit's probe table; every one
# was RED against the pre-T1 hook before the hook changed (the test is the falsifier, not the
# transcript).
#
# MARKER: org/mcp/comprail-gate1.enforce is the fabric KILL SWITCH for the search deny (absent =
# advisory only; the aws tiers were never marker-gated). The test SAVES the live marker state, toggles
# it per case, and RESTORES it on ANY exit (the 06-25 version REFUSED to run while the marker existed,
# which -- since the marker has been ON since 2026-06-26 -- meant the test could never run in
# production; a guard that cannot run is not a guard).
#
# Run from workspace root:  bash .tools/comprail-gate1-fptest.sh [--verbose]
# Exit 0 = every case as expected; exit 1 = a regression (a false-deny or a missed-deny).
set -uo pipefail

WS="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="${COMPRAIL_HOOK:-$WS/.tools/hooks/comp-tool-hud.sh}"   # COMPRAIL_HOOK=<path> runs the cases against another hook build (the red-first control)
MARKER="$WS/org/mcp/comprail-gate1.enforce"
VERBOSE=0; [ "${1:-}" = "--verbose" ] && VERBOSE=1

_HAD_MARKER=0; [ -f "$MARKER" ] && _HAD_MARKER=1
restore() { if [ "$_HAD_MARKER" = 1 ]; then : > "$MARKER" 2>/dev/null || true; else rm -f "$MARKER" 2>/dev/null || true; fi; }
trap restore EXIT INT TERM

# A fresh session id per run so the per-session nudge throttles never make a case order-dependent.
SID="gate1-fptest-$(date -u +%s)-$$"
# The verdict (DENY/ALLOW) is decided before the comp_which nudge's 5s comp-which subprocess; skip it
# here or a 43-case run takes >5 minutes. Production hook behaviour is unchanged (flag unset).
export COMPRAIL_NO_ROUTE=1

# decision(command) -> DENY | ALLOW   (ALLOW = silent OR advisory nudge; both let the command run)
decision() {
  local cmd="$1"
  local enc; enc=$(printf '%s' "$cmd" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))')
  printf '{"tool_name":"Bash","session_id":"%s","tool_input":{"command":%s}}' "$SID" "$enc" \
    | bash "$HOOK" 2>/dev/null | python -c '
import json,sys
s=sys.stdin.read().strip()
if not s: print("ALLOW"); raise SystemExit
try:
  h=json.loads(s).get("hookSpecificOutput",{})
  print("DENY" if h.get("permissionDecision")=="deny" else "ALLOW")
except Exception: print("ALLOW")'
}

# reason(command) -> the deny text (empty when allowed)
reason() {
  local cmd="$1"
  local enc; enc=$(printf '%s' "$cmd" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))')
  printf '{"tool_name":"Bash","session_id":"%s","tool_input":{"command":%s}}' "$SID" "$enc"     | bash "$HOOK" 2>/dev/null | python -c '
import json,sys
s=sys.stdin.read().strip()
try: print(json.loads(s).get("hookSpecificOutput",{}).get("permissionDecisionReason",""))
except Exception: print("")'
}

# cases: state(on|off) | expected | command
# expected may be DENY~<substring>: the case must DENY and the deny text must contain <substring>
# (the DIRECTED gate, Andrew-direct 2026-10-09: every denial hands over the command that answers).
CASES=(
  # ---- BR-2: census tools cannot pipe away their denominator ------------------
  "on|DENY|comp-read f --enumerate x | grep -E '^\\s+[0-9]+ '"
  "on|ALLOW|comp-read f --enumerate x | grep -E 'ENUMERATE|^\\s+[0-9]+ '"
  "on|DENY|comp-find p --files | head"
  "on|ALLOW|comp-read f --for q | tee o.txt"
  "on|ALLOW|ps -ef | grep x"
  "on|ALLOW|comp-read f --enumerate x | head # rail-checked: reading my own scratch output"
  # ---- T1: standalone repo searches -> DENY regardless of path / lead verb / pipe elsewhere ----
  "on|DENY|grep -rn foo ."
  "on|DENY|grep -rn foo org/"
  "on|DENY|grep -rln foo ."
  "on|DENY|rg -n foo org/"
  "on|DENY|rg foo"
  "on|DENY|find org -name *.md"
  "on|DENY|find . -name *.tf"
  "on|DENY|grep -rn foo org/ | head"
  "on|DENY|cd /x && grep -rn foo org/"
  "on|DENY|ls org/ && grep -rn foo docs/"
  "on|DENY|python x.py && grep -rn foo docs/"
  "on|DENY|grep -rn foo daily_reports/"
  "on|DENY|grep -rn TENANT infra/"
  "on|DENY|grep -rn foo portal/src"
  "on|DENY|grep -rn compute_aua data/bd/scripts/"
  "on|DENY|grep -Rn helper data/inf/scripts/"
  "on|DENY|grep -rn thing infra/aws/terraform/"
  "on|DENY|grep -rn baz newproject/"
  "on|DENY|grep -rn foo deck_generation/engine/"
  # 2026-10-09: -r over ONE existing file is a single-file read
  "on|ALLOW|grep -rn foo daily_reports/README.md"
  # 2026-10-09: single-file infra/.tf read passes (507 false denials/month)
  "on|ALLOW|grep -n foo infra/aws/terraform/opal-gateway/alb.tf"
  # ---- T1: raw-aws INSPECTION denies per segment (the cd/echo/export hole) ----
  # 2026-10-09: a live get on ONE named resource is APPLIED evidence
  "on|ALLOW|aws iam get-role --role-name r"
  "on|ALLOW|cd /x && aws iam get-role --role-name r"
  "on|ALLOW|echo === ; aws lambda get-policy --function-name f"
  # a per-resource list, not an enumeration
  "on|ALLOW|export AWS_PROFILE=x; aws iam list-attached-role-policies --role-name r"
  # ---- stays free: pipe-RECEIVER grep, single-file grep (T2 deferred), override, non-search ----
  "on|ALLOW|ps -ef | grep inbox-watch"
  "on|ALLOW|cat file.py | grep x"
  "on|ALLOW|git log | grep fix"
  "on|ALLOW|aws s3 ls s3://bucket/ | grep 2026"
  "on|ALLOW|grep -n foo daily_reports/README.md"
  "on|ALLOW|grep -n foo data/bd/scripts/gold/x.py"
  "on|ALLOW|grep -c foo .tools/comp-find"
  "on|ALLOW|grep -n '^def \\|^CORPUS_MODES' .tools/_comprail.py | head -30"
  "on|ALLOW|grep -n \"x && y; z\" daily_reports/README.md"
  "on|DENY|grep -rn 'a;b' org/"
  "on|DENY|grep -rn 'a\\|b' org/ | head"
  "on|ALLOW|grep -rn x data/bd/scripts/ # rail-checked: no comp-tool fits this exact search"
  "on|ALLOW|cd /x && aws iam get-role --role-name r # rail-checked: live IAM read for a deploy ledger"
  "on|ALLOW|git status && git log -3"
  "on|ALLOW|python daily_reports/scripts/publish_daily_report.py --date 2026-08-27"
  "on|ALLOW|aws s3 ls s3://opal-data-portal-v2/daily-reports/"
  "on|ALLOW|comp-find foo org/"
  "on|ALLOW|ls -la org/ ; echo done"
  # ---- marker OFF = kill switch: search deny off, aws tier-1 unaffected ----
  "off|ALLOW|grep -rn foo ."
  "off|ALLOW|cd /x && grep -rn foo org/"
  "off|ALLOW|aws iam get-role --role-name r"
  "off|DENY|grep -rn thing infra/aws/terraform/"
  # ---- DIRECTED GATE 2026-10-09 (design COMP_RAIL_DIRECTED_GATE_DESIGN_20261008.md section 3 + the build list) ----
  "on|DENY~RUN NEXT: comp-find 'foo' .|grep -rn foo ."
  "on|DENY~NOTHING IN THIS CALL RAN|grep -rn foo ."
  "on|DENY~comp-find --name '*.md' org|find org -name *.md"
  "on|DENY~comp-find -i --files 'needle' org|grep -rli needle org/"
  "on|DENY~comp-find --files 'inf-ec2-launch-monitor|grep -rn -l -E \"inf-ec2-launch-monitor|inf-ec2-retry-launch\" infra/aws/terraform/"
  "on|DENY~comp-estate --resource|grep -rn thing infra/aws/terraform/"
  "on|DENY~RUN NEXT: comp-find --name 'BUCKETLESS*' --limit 6|comp-find --name 'BUCKETLESS*' --limit 6 2>&1 | tail"
  "on|DENY~comp-find p --files --limit 20|comp-find p --files | head"
  "on|ALLOW|comp-find --help | grep -E -- '--(files|band)'"
  "on|DENY~REMAINDER (the rest of your call, which did not run): cd /x ; git checkout -- f|cd /x; git checkout -- f; grep -rn p org/"
  "on|ALLOW|grep -rn foo C:/Users/AndrewBerman/AppData/Local/Temp"
  "on|ALLOW|git status"
  "on|ALLOW|aws iam get-role --role-name x"
  "on|DENY~comp-find --corpus aws '.' IAM_ROLE|aws iam list-roles"
  "on|DENY~comp-find --corpus aws '.' LAMBDA|aws lambda list-functions --region us-east-1"
  "on|DENY~deny_id=|aws iam list-users"
)

# R3 needs a LIVE linked worktree. Take one that exists at run time: a fixed path dies when its round closes (the
# first fixture, C:/tmp/wk-blankfix-4, did, and read as a regression). The main checkout is listed first and is not one.
_self="$(cd "$WS" && (pwd -W 2>/dev/null || pwd))"
LINKED_WT="$(git -C "$WS" worktree list --porcelain 2>/dev/null | awk '/^worktree /{n++; if (n>1) print substr($0,10)}' | grep -vxF "$_self" | head -1)"
if [ -n "$LINKED_WT" ]; then
  CASES+=("on|DENY~cd '$LINKED_WT' && comp-find 'foo'|grep -rn foo $LINKED_WT/org")
else
  echo "  SKIP R3 worktree case: no linked worktree exists to test against"
fi
# NOTE: this test toggles $MARKER, the LIVE rail kill switch of the tree it runs in. Run it from a linked worktree
# (its own marker), and never two runs at once in one tree: they flip enforcement under each other.

fails=0; n=0
for row in "${CASES[@]}"; do
  state="${row%%|*}"; rest="${row#*|}"; exp="${rest%%|*}"; cmd="${rest#*|}"
  n=$((n+1))
  if [ "$state" = on ]; then : > "$MARKER"; else rm -f "$MARKER"; fi
  want="${exp%%~*}"; sub=""; [ "$want" != "$exp" ] && sub="${exp#*~}"
  got=$(decision "$cmd")
  if [ -n "$sub" ] && [ "$got" = DENY ]; then
    if ! reason "$cmd" | grep -qF -- "$sub"; then got="DENY(text lacks: $sub)"; fi
  fi
  exp="$want"
  if [ "$got" != "$exp" ]; then
    fails=$((fails+1))
    printf '  FAIL [marker %-3s] exp=%-5s got=%-5s  %s\n' "$state" "$exp" "$got" "$cmd"
  elif [ "$VERBOSE" = 1 ]; then
    printf '  ok   [marker %-3s] %-5s  %s\n' "$state" "$got" "$cmd"
  fi
done
restore

echo ""
echo "comprail search-rail FP-test: $((n-fails))/$n cases as expected (marker restored to $([ "$_HAD_MARKER" = 1 ] && echo ON || echo OFF))"
if [ "$fails" -ne 0 ]; then echo "RESULT: FAIL ($fails over/under-gate regressions)"; exit 1; fi
echo "RESULT: PASS"
