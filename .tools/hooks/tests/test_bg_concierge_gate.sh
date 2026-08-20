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
SID_BGPATH="test-bgpath-$$"; SID_BGPATH_OTHER="test-bgpath-other-$$"; SID_BGPATH_BG="test-bgpath-bg-$$"
trap 'rm -f "$WS/org/mcp/sessions/${SID}.serial" "$WS/org/mcp/sessions/${SID_OTHER}.serial" "$WS/org/mcp/sessions/${SID_BGPATH}".* "$WS/org/mcp/sessions/${SID_BGPATH_OTHER}".* "$WS/org/mcp/sessions/${SID_BGPATH_BG}".*' EXIT

PASS=0; FAIL=0
# Verdicts (F8 widened the set; PASS means SILENT pass): PASS | LOUD (permitted + a named systemMessage line) | DENY.
# The probe runs with OPAL_AGENT_SERIAL UNSET unless run_env is used -- an ajb-launched seat running this suite
# would otherwise resolve every "unresolvable" probe to ITSELF (the pre-F8 fail-open case was mis-measured that way).
run() { # run <expect:PASS|LOUD|DENY> <label> <json>
    _run_with "" "$@"
}
run_env() { # run_env <OPAL_AGENT_SERIAL value> <expect> <label> <json>
    _run_with "$1" "$2" "$3" "$4"
}
_run_with() {
    local envserial="$1" expect="$2" label="$3" json="$4" out rc
    if [ -n "$envserial" ]; then
        out=$(printf '%s' "$json" | env OPAL_AGENT_SERIAL="$envserial" bash "$GATE" 2>&1); rc=$?
    else
        out=$(printf '%s' "$json" | env -u OPAL_AGENT_SERIAL bash "$GATE" 2>&1); rc=$?
    fi
    local verdict="PASS"
    if printf '%s' "$out" | grep -q '"systemMessage"'; then verdict="LOUD"; fi
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
run LOUD "unresolvable serial, no BG marker: LOUD-PASS (F8-3, was silent fail-open)" "$(j "no-such-session" Bash '{"command":"git commit -m x"}')"

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

# =========================================================================================
# F8 (OPAL_ANALYST.W6-T1, Andrew-direct "rec approved" @ad2585793c): the OUTCOME SET over
# (serial state x BG-launch-path marker) -- ACTIVE-ENFORCE / SILENT-PASS / LOUD-CLOSED / LOUD-PASS
# -- each cell exercised, plus the two mutants (F8-4). The marker is org/mcp/sessions/<sid>.launch-path
# (ajb.ps1 writes it at the BG launch BEFORE the serial file).
# =========================================================================================
printf 'bg-concierge 2026-08-20T00:00:00Z launcher=test host=test\n' > "$WS/org/mcp/sessions/${SID_BGPATH}.launch-path"       # marker, NO serial
printf 'bg-concierge test\n' > "$WS/org/mcp/sessions/${SID_BGPATH_OTHER}.launch-path"; echo "0.4.0_DS_ClientPlatform" > "$WS/org/mcp/sessions/${SID_BGPATH_OTHER}.serial"
printf 'bg-concierge test\n' > "$WS/org/mcp/sessions/${SID_BGPATH_BG}.launch-path";    echo "0.0.3_BG_BBGTerminal" > "$WS/org/mcp/sessions/${SID_BGPATH_BG}.serial"

# cell SILENT-PASS: identity wins over the marker -- another seat on a BG-marked session id is silent, untouched
run PASS "F8 SILENT-PASS: marker present, serial resolves to ANOTHER seat -> silent" "$(j "$SID_BGPATH_OTHER" Bash '{"command":"git commit -m x"}')"
# cell ACTIVE-ENFORCE (F8-2 positive control): the healthy ajb launch = marker + serial file = BG; the four classes as today
run DENY "F8-2 ACTIVE: healthy BG launch, G2 git commit denied"                 "$(j "$SID_BGPATH_BG" Bash '{"command":"git commit -m x"}')"
run PASS "F8-2 ACTIVE: healthy BG launch, own-logs write passes (G1 allowlist)"  "$(j "$SID_BGPATH_BG" Write '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-20/x.md"}')"
run DENY "F8-2 ACTIVE: healthy BG launch, refs/ write denied (G1)"               "$(j "$SID_BGPATH_BG" Write '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/refs/X.md"}')"
run DENY "F8-2 ACTIVE: healthy BG launch, historical_data denied (G3)"           "$(j "$SID_BGPATH_BG" mcp__bloomberg__bloomberg_historical_data '{"securities":["SPX Index"]}')"
run PASS "F8-2 ACTIVE: healthy BG launch, 1-security reference_data passes (G3 carve-out)" "$(j "$SID_BGPATH_BG" mcp__bloomberg__bloomberg_reference_data '{"securities":["SPX Index"],"fields":["PX_LAST"]}')"
run DENY "F8-2 ACTIVE: healthy BG launch, opal-gateway (Andrew) denied (G4)"     "$(j "$SID_BGPATH_BG" mcp__opal-gateway__list_chats '{}')"
run PASS "F8-2 ACTIVE: healthy BG launch, -bbg Teams poll passes (G4 allowlist)" "$(j "$SID_BGPATH_BG" mcp__opal-gateway-bbg__poll_addressed_teams_messages '{}')"
# cell ACTIVE via env only (no session file, OPAL_AGENT_SERIAL=BG) -- the second identity source still works
run_env "0.0.3_BG_BBGTerminal" DENY "F8 ACTIVE via env: no session file, OPAL_AGENT_SERIAL=BG -> git commit denied" "$(j "no-such-session" Bash '{"command":"git commit -m x"}')"
run_env "0.4.0_DS_ClientPlatform" PASS "F8 SILENT-PASS via env: OPAL_AGENT_SERIAL=another seat -> silent" "$(j "no-such-session" Bash '{"command":"git commit -m x"}')"
# cell LOUD-CLOSED (F8-1; = F8-4 mutant 1: serial unset ON the BG launch path): every classed call DENIED with a named line
run DENY "F8-1 LOUD-CLOSED: G1-allowlisted own-logs write is DENIED (closed means closed)" "$(j "$SID_BGPATH" Write '{"file_path":"org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-20/x.md"}')"
run DENY "F8-1 LOUD-CLOSED: read-class git log is DENIED (Bash is classed)"     "$(j "$SID_BGPATH" Bash '{"command":"git log --oneline -1"}')"
run DENY "F8-1 LOUD-CLOSED: PowerShell is DENIED"                                "$(j "$SID_BGPATH" PowerShell '{"command":"Get-Date"}')"
run DENY "F8-1 LOUD-CLOSED: bloomberg_health is DENIED (Bloomberg tools are classed)" "$(j "$SID_BGPATH" mcp__bloomberg__bloomberg_health '{}')"
run DENY "F8-1 LOUD-CLOSED: -bbg Teams poll is DENIED (gateway tools are classed)" "$(j "$SID_BGPATH" mcp__opal-gateway-bbg__poll_addressed_teams_messages '{}')"
run LOUD "F8-1 LOUD-CLOSED: Read is unclassed -> permitted WITH the named line (nothing silent)" "$(j "$SID_BGPATH" Read '{"file_path":"CLAUDE.md"}')"
out=$(printf '%s' "$(j "$SID_BGPATH" Bash '{"command":"git log"}')" | env -u OPAL_AGENT_SERIAL bash "$GATE" 2>&1)
if printf '%s' "$out" | grep -q 'bg-concierge-gate F8' && printf '%s' "$out" | grep -q 'FAILS CLOSED'; then PASS=$((PASS+1)); echo "ok   [NAMED] F8-1 deny line names F8 + FAILS CLOSED + the fix"
else FAIL=$((FAIL+1)); echo "FAIL [NAMED] F8-1 deny line is not the named line :: $out"; fi
# cell LOUD-PASS (F8-3 negative control): unresolvable, NO marker -> permitted, loud -- a blanket block here = FAIL
run LOUD "F8-3 LOUD-PASS: non-BG unresolvable, git commit PERMITTED with the loud line" "$(j "no-such-session" Bash '{"command":"git commit -m x"}')"
run LOUD "F8-3 LOUD-PASS: non-BG unresolvable, CLAUDE.md write PERMITTED with the loud line" "$(j "no-such-session" Write '{"file_path":"C:/ws/CLAUDE.md"}')"
run LOUD "F8-3 LOUD-PASS: non-BG unresolvable, Read PERMITTED with the loud line"    "$(j "no-such-session" Read '{"file_path":"CLAUDE.md"}')"
out=$(printf '%s' "$(j "no-such-session" Bash '{"command":"git commit -m x"}')" | env -u OPAL_AGENT_SERIAL bash "$GATE" 2>&1)
if printf '%s' "$out" | grep -q 'LOUD-PASS' && ! printf '%s' "$out" | grep -q '"permissionDecision"'; then PASS=$((PASS+1)); echo "ok   [NAMED] F8-3 loud line names LOUD-PASS and carries no decision"
else FAIL=$((FAIL+1)); echo "FAIL [NAMED] F8-3 loud line :: $out"; fi
# F8-4 mutant 2 (inverse): REMOVE the marker from the BG-path session -> the same unresolvable session is LOUD-PASS
rm -f "$WS/org/mcp/sessions/${SID_BGPATH}.launch-path"
run LOUD "F8-4 inverse mutant: marker REMOVED -> same unresolvable session is LOUD-PASS (scope predicate load-bearing)" "$(j "$SID_BGPATH" Bash '{"command":"git log --oneline -1"}')"
# marker back -> LOUD-CLOSED re-fires (the forward mutant, re-exercised after the inverse)
printf 'bg-concierge test\n' > "$WS/org/mcp/sessions/${SID_BGPATH}.launch-path"
run DENY "F8-4 mutant 1 re-fire: marker back, serial still unresolvable -> LOUD-CLOSED denies git log" "$(j "$SID_BGPATH" Bash '{"command":"git log --oneline -1"}')"
# a marker whose first line is NOT bg-concierge is not the BG path (the signal is the content, not the file)
printf 'something-else\n' > "$WS/org/mcp/sessions/${SID_BGPATH}.launch-path"
run LOUD "F8 marker content control: launch-path file without 'bg-concierge' -> LOUD-PASS, not closed" "$(j "$SID_BGPATH" Bash '{"command":"git log --oneline -1"}')"
printf 'bg-concierge test\n' > "$WS/org/mcp/sessions/${SID_BGPATH}.launch-path"
# ajb's second write lands (the serial file) -> the same session becomes ACTIVE: reads pass silently, mutations deny
echo "0.0.3_BG_BBGTerminal" > "$WS/org/mcp/sessions/${SID_BGPATH}.serial"
run PASS "F8 resolve: serial file written (ajb's act) -> ACTIVE: git log (read) passes silently" "$(j "$SID_BGPATH" Bash '{"command":"git log --oneline -1"}')"
run DENY "F8 resolve: ... and ACTIVE denies git commit"                          "$(j "$SID_BGPATH" Bash '{"command":"git commit -m x"}')"
run PASS "BG: -bbg data refresh upload"    "$(j "$SID" mcp__opal-gateway-bbg__opal_data_refresh_upload '{}')"
run DENY "BG: -bbg send_email"             "$(j "$SID" mcp__opal-gateway-bbg__send_email '{"to":"x","subject":"y"}')"

echo "----"
echo "RESULT: $PASS passed, $FAIL failed (denominator: $((PASS+FAIL)) cases)"
[ $FAIL -eq 0 ]
