#!/usr/bin/env bash
# mstr-no-tier2-writes.sh -- PreToolUse hook. MSTR CANNOT WRITE A TIER-2 SEAT.
#
# Andrew-direct 2026-09-03 ~17:0xZ at the 0.0.0_AB_MSTR~Z terminal, VERBATIM, three messages
# then the rule:
#   "You should never be engaging with tier2 agents"
#   "I need you to adjust your prompt or gating or something so that this is impossible"
#   "it subverts chain of command and /canonical-flow"
#   "YEAH IF THEIR SERIAL STARTS WITH A 0 AND THEY ARE NOT TIER0 AGENT (LIKE BBGTerminal BG
#    agent) you should not be able to write them"
#
# This is an EXPLICITLY ANDREW-REQUESTED gate, so CLAUDE.md's no-manufactured-gates NEVER rule
# is satisfied by his word -- the same footing as bg-concierge-gate.sh.
#
# WHAT PROVOKED IT, named so the gate is not mistaken for prophylaxis: 0.0.0_AB_MSTR~Z sent
# msg 19838 directly to 0.7.0_AE_CloudOps~S (a Tier-2 worker seated on TO-OP-S-16-17-8R2),
# routing around 2.0.0_SA_COO~Z as issuer. Under the canonical workflow L6 is the COO's limb
# and L7 is the worker's; a Tier-0 seat writing a worker inserts a second instruction source
# into a lane that has exactly one. The worker then replied to MSTR (17:01Z), which is the
# channel the first message created.
#
# THE RULE, exactly as he stated it:
#   recipient serial starts with "0."  AND  recipient is NOT a Tier-0 agent   ->  DENY
# Everything else passes. So:
#   1.0.0_SA_CTO*, 2.0.0_SA_COO*, 3.0.0_SA_CVO*, 4.0.0_SA_CRO*   PASS (do not start with 0)
#   0.0.0_AB_MSTR* (Tier-0, org/tier0_exec/)                     PASS
#   0.0.3_BG_BBGTerminal, 0.0.1_UA_*, 0.0.2_UA_* (org/tier0_utility/)  PASS
#   0.1.0_DS_*, 0.4.0_DE_*, 0.7.0_AE_*, 0.8.0_AE_* ...           DENY
#
# TIER-0 MEMBERSHIP IS READ FROM THE ESTATE'S OWN RECORD, never from a hardcoded list: a base
# serial is Tier-0 iff a directory for it exists under org/tier0_exec/ or org/tier0_utility/.
# An enumerated allow-list would lapse silently the day a Tier-0 seat is added or renamed --
# the same failure mode CLAUDE.md records for the cross-firm ban list.
# ~lane suffixes are stripped before the lookup (a lane is not a separate agent for this).
#
# WARN: ONE READING OF HIS WORDS I HAD TO CHOOSE, stated so he can correct it in one word: the
# parenthetical "(LIKE BBGTerminal BG agent)" is attached to "TIER0 AGENT", i.e. BG is offered
# as an EXAMPLE OF a Tier-0 agent and is therefore PERMITTED. It reads that way because BG
# lives at org/tier0_utility/0.0.3_BG_BBGTerminal and because his stated harm is chain of
# command and /canonical-flow -- BG holds no task order and sits in no L6/L7 lane, so writing
# it cannot subvert either. The other reading (BG as an example of a seat to block) is one
# line to switch: add 0.0.3_BG_BBGTerminal to TIER0_EXTRA_DENY below.
#
# SCOPE: fires ONLY when the calling session's serial is an 0.0.0_AB_MSTR seat (any ~lane).
# For every other seat this is a fast no-op -- 2.0.0_SA_COO MUST be able to write Tier-2, that
# is L6, and a fabric-wide version of this gate would break the workflow it exists to protect.
#
# FAIL CLOSED, FOR MSTR ONLY. Once the caller is known to be MSTR, anything the gate cannot
# read -- no jq, unparseable input, a recipient it cannot classify -- is a DENY with a named
# reason. A gate that stands down silently on its own blind spot is the shape this estate has
# measured repeatedly; here the cost of a false deny is one message re-routed through a Tier-1
# seat, which is where Andrew says it should have gone anyway.
#
# Block mechanism: JSON permissionDecision="deny", exit 0. A bare exit 2 is a hook ERROR rather
# than a block (see never-rules-gate.sh:53 and bg-concierge-gate.sh:52).
#
# Battery: .tools/hooks/tests/test_mstr_no_tier2_writes.sh -- pass AND deny controls, plus a
# mutant arm (the gate must FAIL when the rule is inverted, or it is proving nothing).

set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
WS="${CLAUDE_PROJECT_DIR:-$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)}"

# Extra serials to treat as DENY even if they resolve Tier-0 (the BG fork above).
TIER0_EXTRA_DENY="${MSTR_TIER2_EXTRA_DENY:-}"

if [ -x "$SCRIPT_DIR/../jq.exe" ]; then
    JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    JQ=""
fi

# ---------- identity: is the caller an MSTR seat? (never-rules-gate pattern) ----------
_SID=""; _CALLER=""
if [ -n "$JQ" ]; then
    _SID=$(printf '%s' "$INPUT" | "$JQ" -r '.session_id // empty' 2>/dev/null || true)
    [ -n "$_SID" ] && [ -r "$WS/org/mcp/sessions/${_SID}.serial" ] && \
        _CALLER=$(tr -d '[:space:]' < "$WS/org/mcp/sessions/${_SID}.serial" 2>/dev/null || true)
fi
[ -z "$_CALLER" ] && _CALLER="${OPAL_AGENT_SERIAL:-}"

case "$_CALLER" in
    0.0.0_AB_MSTR|0.0.0_AB_MSTR~*) : ;;                 # this gate's subject
    "" ) # UNRESOLVABLE. Cannot tell MSTR from a COO doing legitimate L6 dispatch.
         # Loud, not blocking: a fabric-wide fail-closed here would break L6 for every seat
         # whose serial file is missing, which is a worse outcome than the one being prevented.
         if [ -n "$JQ" ]; then
             _M="mstr-no-tier2-writes: caller identity UNRESOLVABLE (no org/mcp/sessions/${_SID:-<no session_id>}.serial and OPAL_AGENT_SERIAL unset) -- the MSTR Tier-2 write fence could NOT be evaluated and the call is permitted. If you are 0.0.0_AB_MSTR, STOP: route through a Tier-1 seat. Then run org/XXX.md A.1 so every gate can see you."
             "$JQ" -nc --arg m "$_M" '{systemMessage:$m, hookSpecificOutput:{hookEventName:"PreToolUse", additionalContext:$m}}'
         else
             echo "mstr-no-tier2-writes: caller UNRESOLVABLE and jq missing -- fence not evaluated, call permitted. If you are MSTR, route through Tier-1." >&2
         fi
         exit 0 ;;
    * ) exit 0 ;;                                        # positively another seat: no-op
esac

# ---------- from here the caller IS MSTR: fail closed on anything unreadable ----------
deny() {
    if [ -n "$JQ" ]; then
        "$JQ" -nc --arg r "$1" \
          '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    else
        echo "$1" >&2
    fi
    exit 0
}

if [ -z "$JQ" ]; then
    deny "BLOCKED (mstr-no-tier2-writes): jq not found, so recipients cannot be read. This fence FAILS CLOSED for 0.0.0_AB_MSTR. Fix: git checkout .tools/jq.exe, then retry -- or route the message through a Tier-1 seat, which is where it belongs."
fi

TOOL=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_name // empty' 2>/dev/null || true)
[ "$TOOL" = "mcp__opal-agent-comms__send_message" ] || exit 0

# Recipients: to_agent (single) + to_agents (array). Both shapes, one list.
# tr -d '\r' IS LOAD-BEARING, NOT HYGIENE. The vendored jq.exe is a Windows binary and its
# stdout carries CRLF, so every recipient line arrives with a trailing CR. `0.0.3_BG_BBGTerminal\r`
# then misses `[ -d .../org/tier0_utility/0.0.3_BG_BBGTerminal ]` and a TIER-0 SEAT IS REFUSED AS
# TIER-2 -- measured 2026-09-04, the gate blocking a legitimate send to the BG terminal.
RECIPIENTS=$(printf '%s' "$INPUT" | "$JQ" -r '
  [ (.tool_input.to_agent // empty), ((.tool_input.to_agents // []) | .[]? ) ]
  | map(select(. != null and . != "")) | .[]' 2>/dev/null | tr -d '\r' || true)

if [ -z "$RECIPIENTS" ]; then
    deny "BLOCKED (mstr-no-tier2-writes): the send names no readable recipient in to_agent or to_agents, so this fence cannot classify it. FAIL CLOSED for MSTR. Re-issue with an explicit recipient serial."
fi

is_tier0() {   # $1 = base serial (lane already stripped)
    [ -d "$WS/org/tier0_exec/$1" ] && return 0
    [ -d "$WS/org/tier0_utility/$1" ] && return 0
    return 1
}

BLOCKED=""
while IFS= read -r r; do
    [ -z "$r" ] && continue
    base="${r%%~*}"
    case "$base" in
        0.*)
            if is_tier0 "$base"; then
                for x in $TIER0_EXTRA_DENY; do
                    [ "$base" = "$x" ] && BLOCKED="$BLOCKED $r (Tier-0 but on the extra-deny list)"
                done
            else
                BLOCKED="$BLOCKED $r"
            fi
            ;;
        *) : ;;   # does not start with 0. -> Tier-1+ -> passes
    esac
done <<EOF
$RECIPIENTS
EOF

[ -z "$BLOCKED" ] && exit 0

deny "BLOCKED (mstr-no-tier2-writes) -- Andrew-direct 2026-09-03 ~17:0xZ: \"You should never be engaging with tier2 agents ... it subverts chain of command and /canonical-flow ... IF THEIR SERIAL STARTS WITH A 0 AND THEY ARE NOT TIER0 AGENT you should not be able to write them.\" Refused recipient(s):${BLOCKED}. These serials start with 0. and have no directory under org/tier0_exec/ or org/tier0_utility/, so they are Tier-2. ROUTE IT THROUGH TIER-1 INSTEAD: the issuer of the task order (2.0.0_SA_COO or its lane) owns L6 dispatch, 1.0.0_SA_CTO owns the PRD and any spec correction, 3.0.0_SA_CVO owns adjudication. If the content is a finding, the surprise channel row is the carrier and needs no message at all. Tier-1 and Tier-0 recipients in the same call are refused with it -- re-send those separately."
