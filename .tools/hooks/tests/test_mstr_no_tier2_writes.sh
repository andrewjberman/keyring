#!/usr/bin/env bash
# Battery for mstr-no-tier2-writes.sh -- PASS controls, DENY controls, and a MUTANT arm.
#
# A battery with only DENY cases proves the gate can refuse and nothing about whether it can
# ever permit; a battery with only PASS cases proves the inverse. The mutant arm exists because
# a battery that cannot fail is decoration: it inverts the gate's core predicate and asserts the
# battery goes RED. If the mutant run is green, the battery is not testing the rule.
#
# Run:  bash .tools/hooks/tests/test_mstr_no_tier2_writes.sh

set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WS="$(cd "$HERE/../../.." && pwd)"
GATE="${GATE_OVERRIDE:-$WS/.tools/hooks/mstr-no-tier2-writes.sh}"
export CLAUDE_PROJECT_DIR="$WS"

PASS=0; FAIL=0
# fire <expect: allow|deny> <caller-serial> <label> <tool_input-json>
fire() {
    local expect="$1" caller="$2" label="$3" ti="$4"
    local out rc verdict
    out=$(printf '{"session_id":"__none__","tool_name":"mcp__opal-agent-comms__send_message","tool_input":%s}' "$ti" \
          | OPAL_AGENT_SERIAL="$caller" bash "$GATE" 2>&1)
    rc=$?
    if printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then verdict="deny"; else verdict="allow"; fi
    if [ "$verdict" = "$expect" ]; then
        PASS=$((PASS+1)); printf '  ok   %-58s %s (rc=%s)\n' "$label" "$verdict" "$rc"
    else
        FAIL=$((FAIL+1)); printf '  FAIL %-58s expected %s got %s (rc=%s)\n' "$label" "$expect" "$verdict" "$rc"
        printf '       %s\n' "$(printf '%s' "$out" | head -c 300)"
    fi
}
# a non-send tool must always pass, whoever calls it
fire_other() {
    local caller="$1" tool="$2"
    local out verdict
    out=$(printf '{"session_id":"__none__","tool_name":"%s","tool_input":{"to_agent":"0.7.0_AE_CloudOps~S"}}' "$tool" \
          | OPAL_AGENT_SERIAL="$caller" bash "$GATE" 2>&1)
    if printf '%s' "$out" | grep -q '"permissionDecision":"deny"'; then verdict="deny"; else verdict="allow"; fi
    if [ "$verdict" = "allow" ]; then PASS=$((PASS+1)); printf '  ok   %-58s allow\n' "other tool: $tool"
    else FAIL=$((FAIL+1)); printf '  FAIL %-58s expected allow got deny\n' "other tool: $tool"; fi
}

echo "GATE: $GATE"
echo "-- DENY controls (MSTR caller, Tier-2 recipients) --"
fire deny  0.0.0_AB_MSTR~Z "MSTR -> 0.7.0_AE_CloudOps~S (the actual violation)" '{"to_agent":"0.7.0_AE_CloudOps~S"}'
fire deny  0.0.0_AB_MSTR   "MSTR base -> 0.4.0_DS_ClientPlatform"               '{"to_agent":"0.4.0_DS_ClientPlatform"}'
fire deny  0.0.0_AB_MSTR~Z "MSTR -> Tier-2 via to_agents array"                 '{"to_agents":["0.1.0_DS_MarketIntelligence~C"]}'
fire deny  0.0.0_AB_MSTR~Z "MIXED list: one Tier-1 + one Tier-2 refuses whole"  '{"to_agents":["2.0.0_SA_COO~Z","0.8.0_AE_CloudComp"]}'
fire deny  0.0.0_AB_MSTR~Z "unknown 0.x serial with no tier0 dir"               '{"to_agent":"0.9.9_ZZ_NotAThing"}'
fire deny  0.0.0_AB_MSTR~Z "no recipient at all -> fail closed for MSTR"        '{"subject":"x"}'

echo "-- PASS controls (the gate must be able to permit) --"
fire allow 0.0.0_AB_MSTR~Z "MSTR -> 1.0.0_SA_CTO~Z"                            '{"to_agent":"1.0.0_SA_CTO~Z"}'
fire allow 0.0.0_AB_MSTR~Z "MSTR -> 2.0.0_SA_COO~Z"                            '{"to_agent":"2.0.0_SA_COO~Z"}'
fire allow 0.0.0_AB_MSTR~Z "MSTR -> 3.0.0_SA_CVO~Z + 4.0.0_SA_CRO"             '{"to_agents":["3.0.0_SA_CVO~Z","4.0.0_SA_CRO"]}'
fire allow 0.0.0_AB_MSTR~Z "MSTR -> 0.0.0_AB_MSTR (Tier-0, org/tier0_exec)"    '{"to_agent":"0.0.0_AB_MSTR"}'
fire allow 0.0.0_AB_MSTR~Z "MSTR -> 0.0.3_BG_BBGTerminal (Tier-0 utility)"     '{"to_agent":"0.0.3_BG_BBGTerminal"}'
fire allow 2.0.0_SA_COO~Z  "COO -> 0.7.0_AE_CloudOps~S (L6 dispatch, MUST work)" '{"to_agent":"0.7.0_AE_CloudOps~S"}'
fire allow 1.0.0_SA_CTO~Z  "CTO -> Tier-2 (not this gate's subject)"            '{"to_agent":"0.7.0_AE_CloudOps~Z"}'
fire allow 3.0.0_SA_CVO~Z  "CVO -> Tier-2 (not this gate's subject)"            '{"to_agent":"0.4.0_DS_ClientPlatform~J"}'

# ---- THE CROSS-PRODUCT CELLS THE FIRST BATTERY LEFT UNTESTED ----
# The original 16 arms varied TWO dimensions and never crossed them: every DENY control used the
# to_agents ARRAY, every Tier-0 PASS control used the scalar to_agent. So (array x Tier-0) was
# never exercised -- and that is the exact cell where jq.exe's CRLF welded a \r to the serial,
# making a Tier-0 seat miss its own directory and refuse as Tier-2. Measured live 2026-09-04.
fire allow 0.0.0_AB_MSTR~Z "ARRAY x Tier-0 utility: BG alone in to_agents"      '{"to_agents":["0.0.3_BG_BBGTerminal"]}'
fire allow 0.0.0_AB_MSTR~Z "ARRAY x Tier-0 exec: the laptop peer alone"         '{"to_agents":["0.0.0_AB_MSTR"]}'
fire allow 0.0.0_AB_MSTR~Z "ARRAY x mixed Tier-1 + Tier-0, all permitted"       '{"to_agents":["1.0.0_SA_CTO~Z","0.0.3_BG_BBGTerminal","2.0.0_SA_COO~Z"]}'
fire allow 0.0.0_AB_MSTR~Z "ARRAY x Tier-0 LAST (trailing element, CRLF-prone)" '{"to_agents":["2.0.0_SA_COO~Z","0.0.3_BG_BBGTerminal"]}'
fire deny  0.0.0_AB_MSTR~Z "SCALAR x Tier-2 (the mirror of the array denies)"   '{"to_agent":"0.7.0_AE_CloudOps~S"}'
fire_other 0.0.0_AB_MSTR~Z mcp__opal-agent-comms__check_inbox
fire_other 0.0.0_AB_MSTR~Z mcp__opal-agent-comms__heartbeat

echo
echo "RESULT: $PASS passed, $FAIL failed (denominator $((PASS+FAIL)))"
[ "$FAIL" -eq 0 ] || exit 1

# ---------------- MUTANT ARM: the battery must go RED against a broken gate ----------------
if [ -n "${SKIP_MUTANT:-}" ]; then echo "MUTANT: skipped"; exit 0; fi
MUT="$(mktemp -t mstrgate-mutant-XXXXXX.sh 2>/dev/null || echo "${TMPDIR:-/tmp}/mstrgate-mutant.$$.sh")"
# invert the core predicate: treat every 0.* recipient as Tier-0 (i.e. never block)
sed 's/^            if is_tier0 "\$base"; then/            if true; then/' "$GATE" > "$MUT"
if ! grep -q 'if true; then' "$MUT"; then
    echo "MUTANT: could not apply the mutation -- the battery cannot prove it can fail. TREAT AS RED."; rm -f "$MUT"; exit 1
fi
echo "-- MUTANT arm (gate's tier0 test forced true; the battery MUST go red) --"
if SKIP_MUTANT=1 GATE_OVERRIDE="$MUT" bash "$0" >/dev/null 2>&1; then
    echo "MUTANT: *** the battery passed a BROKEN gate -- it is not testing the rule. RED. ***"; rm -f "$MUT"; exit 1
else
    echo "MUTANT: battery correctly went RED against the inverted gate."; rm -f "$MUT"
fi
echo "ALL GREEN with a working mutant control."
