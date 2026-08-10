#!/usr/bin/env bash
# test_bg_concierge_gate.sh -- exercise bg-concierge-gate.sh BOTH directions.
# A gate exercised only on its deny cases has never been shown to pass honest work,
# and one exercised only on pass cases has never been shown to block anything.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
GATE="$HERE/../bg-concierge-gate.sh"
WS="$(cd "$HERE/../../.." && pwd)"
export CLAUDE_PROJECT_DIR="$WS"

SID="test-bg-gate-$$"
mkdir -p "$WS/org/mcp/sessions"
echo "0.0.3_BG_BBGTerminal" > "$WS/org/mcp/sessions/${SID}.serial"
SID_OTHER="test-nonbg-gate-$$"
echo "0.4.0_DS_ClientPlatform" > "$WS/org/mcp/sessions/${SID_OTHER}.serial"
trap 'rm -f "$WS/org/mcp/sessions/${SID}.serial" "$WS/org/mcp/sessions/${SID_OTHER}.serial"' EXIT

PASS=0; FAIL=0
run() { # run <expect:PASS|DENY> <label> <json>
    local expect="$1" label="$2" json="$3" out rc
    out=$(printf '%s' "$json" | bash "$GATE" 2>&1); rc=$?
    local verdict="PASS"
    if printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then verdict="DENY"; fi
    [ $rc -ne 0 ] && verdict="ERROR(rc=$rc)"
    if [ "$verdict" = "$expect" ]; then PASS=$((PASS+1)); echo "ok   [$expect] $label"
    else FAIL=$((FAIL+1)); echo "FAIL [$label] expected $expect got $verdict :: $out"; fi
}

j() { # j <sid> <tool> <input-json-fragment>
    printf '{"session_id":"%s","tool_name":"%s","tool_input":%s}' "$1" "$2" "$3"
}

# --- identity scoping: a NON-BG seat is never touched (the most important pass case) ---
run PASS "non-BG seat: git commit passes untouched"      "$(j "$SID_OTHER" Bash '{"command":"git commit -m x"}')"
run PASS "non-BG seat: write to CLAUDE.md passes"        "$(j "$SID_OTHER" Write '{"file_path":"C:/ws/CLAUDE.md"}')"
run PASS "unresolvable serial: passes (fail-open)"       "$(j "no-such-session" Bash '{"command":"git commit -m x"}')"

# --- G1 file writes ---
run PASS "BG: write own daily log"    "$(j "$SID" Write '{"file_path":"C:/x/org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-07/a.md"}')"
run PASS "BG: write thread memory"    "$(j "$SID" Write '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/threads/t/2026-08-07.md"}')"
run PASS "BG: write tmp calc"         "$(j "$SID" Write '{"file_path":"C:/Users/x/AppData/Local/Temp/claude/scratchpad/calc.py"}')"
run DENY "BG: edit own prompt.md"     "$(j "$SID" Edit '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md"}')"
run DENY "BG: edit own refs catalog"  "$(j "$SID" Edit '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/refs/REQUEST_CATALOG.md"}')"
run DENY "BG: write a skill"          "$(j "$SID" Write '{"file_path":".claude/skills/bbg-teams-assist/SKILL.md"}')"
run DENY "BG: write repo code"        "$(j "$SID" Write '{"file_path":"data/assets/scripts/gold/x.py"}')"

# --- G2 shell ---
run DENY "BG: git commit"             "$(j "$SID" Bash '{"command":"git commit -m hello"}')"
run DENY "BG: git -C push"            "$(j "$SID" Bash '{"command":"git -C portal push origin DEV"}')"
run PASS "BG: git log (read)"         "$(j "$SID" Bash '{"command":"git log --oneline -5"}')"
run PASS "BG: prose mentions commit"  "$(j "$SID" Bash '{"command":"echo \"we never git commit from this seat\""}')"
run DENY "BG: aws s3 cp INTO bucket"  "$(j "$SID" Bash '{"command":"aws s3 cp /tmp/f.json s3://opal-data-portal-v2/json/x.json"}')"
run PASS "BG: aws s3 cp DOWN to tmp"  "$(j "$SID" Bash '{"command":"aws s3 cp s3://opal-data-portal-v2/json/macro/macro_data.json /tmp/m.json"}')"
run PASS "BG: aws s3 ls (read)"       "$(j "$SID" Bash '{"command":"aws s3 ls s3://opal-data-portal-v2/json/"}')"
run DENY "BG: ddb put-item"           "$(j "$SID" Bash '{"command":"aws dynamodb put-item --table-name t --item {}"}')"
run PASS "BG: ddb query (read)"       "$(j "$SID" Bash '{"command":"aws dynamodb query --table-name opal-news-articles --key-condition-expression x"}')"
run DENY "BG: terraform"              "$(j "$SID" Bash '{"command":"terraform apply"}')"
run DENY "BG: redirect into org/"     "$(j "$SID" Bash '{"command":"echo hi > org/projects/X.json"}')"
run PASS "BG: redirect into own logs" "$(j "$SID" Bash '{"command":"echo hi > org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-07/x.md"}')"
run PASS "BG: redirect to tmp"        "$(j "$SID" Bash '{"command":"python calc.py > /tmp/out.txt"}')"

# --- G3 Bloomberg ---
run DENY "BG: historical_data"        "$(j "$SID" mcp__bloomberg__bloomberg_historical_data '{"securities":["SPX Index"]}')"
run DENY "BG: intraday_bars"          "$(j "$SID" mcp__bloomberg__bloomberg_intraday_bars '{"security":"SPX Index"}')"
run PASS "BG: reference_data 1 sec"   "$(j "$SID" mcp__bloomberg__bloomberg_reference_data '{"securities":["SPX Index"],"fields":["PX_LAST"]}')"
run DENY "BG: reference_data 5 secs"  "$(j "$SID" mcp__bloomberg__bloomberg_reference_data '{"securities":["a","b","c","d","e"],"fields":["PX_LAST"]}')"
run PASS "BG: bloomberg_health"       "$(j "$SID" mcp__bloomberg__bloomberg_health '{}')"

# --- G4 gateway identity ---
run DENY "BG: opal-gateway (Andrew) send"  "$(j "$SID" mcp__opal-gateway__send_chat_message '{"chat_id":"x","message":"hi"}')"
run DENY "BG: opal-gateway (Andrew) read"  "$(j "$SID" mcp__opal-gateway__list_chats '{}')"
run PASS "BG: -bbg Teams send"             "$(j "$SID" mcp__opal-gateway-bbg__send_chat_message '{"chat_id":"x","message":"hi"}')"
run PASS "BG: -bbg Teams poll"             "$(j "$SID" mcp__opal-gateway-bbg__poll_addressed_teams_messages '{}')"
run PASS "BG: -bbg data refresh upload"    "$(j "$SID" mcp__opal-gateway-bbg__opal_data_refresh_upload '{}')"
run DENY "BG: -bbg send_email"             "$(j "$SID" mcp__opal-gateway-bbg__send_email '{"to":"x","subject":"y"}')"

echo "----"
echo "RESULT: $PASS passed, $FAIL failed (denominator: $((PASS+FAIL)) cases)"
[ $FAIL -eq 0 ]
