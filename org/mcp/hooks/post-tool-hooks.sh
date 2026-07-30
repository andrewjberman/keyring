#!/bin/bash
# post-tool-hooks.sh -- THE consolidated PostToolUse '*' hook (telemetry + commitment).
#
# CANONICAL SOURCE: org/mcp/hooks/post-tool-hooks.sh (version-controlled)
# INSTALL TARGET:   .tools/hooks/post-tool-hooks.sh (gitignored, copied via install)
#
# CONSOLIDATION (Andrew cleanup 2026-07-30, MSTR low-level audit): settings.json
# previously ran TWO PostToolUse '*' hook commands per tool call --
# post-tool-telemetry.sh and post-send-commitment.sh -- and telemetry then spawned
# classify-tool-kind.sh as a THIRD bash. On MSYS every spawn is a Windows
# CreateProcess + fork emulation + an EDR filter-driver inspection, at every tool
# call of every session (~12-15 process creations/sec measured fabric-wide with the
# fabric HALTED). This file does all three jobs in ONE process: one bounded stdin
# read, one jq resolution, the classifier as an inline function, and the
# commitment detector as an inline function behind the same tool_name short-circuit.
#
# TWO DELIBERATE BEHAVIOR CHANGES, both strengthenings:
#   (1) the commitment detector previously resolved jq via bare `jq` on PATH --
#       which the profile-less hook shell does NOT have -- so it has been a SILENT
#       NO-OP here (2 spawns per tool call to do nothing). It now shares the
#       telemetry jq ladder and actually fires.
#   (2) the commitment detector previously resolved the agent serial from
#       OPAL_AGENT_SERIAL / the SHARED .agent_context (last-writer-wins, the
#       mis-attribution class XXX.md bans as an identity source). It now uses the
#       telemetry hook's session-id-keyed resolution -- same precedence the rest of
#       the fabric trusts.
#
# The retired standalone scripts stay on disk, unchanged, for in-flight sessions
# still carrying the old hook config; remove them only after those sessions cycle.
#
# CV-B1 PRIVACY INVARIANT (canonical section 3.4 HARD RULE):
#   jsonl gets tool_name ONLY; tool arguments + tool outputs are NEVER written.
#   The jq -nc invocation below explicitly enumerates allowed fields.
#
# Failures are silent by design -- a hook error must never disrupt the agent.

set -u  # NOT -e: a hook must degrade, never hard-stop mid-file (the jsonl write
        # and every external call below carry their own explicit failure handling)

# BOUNDED stdin read (Andrew-direct 2026-07-30): a bare $(cat) on a hook stdin that
# never closes blocked a 3-process chain of the predecessor script for 5 days
# (PIDs 850873/93/94, Jul 25->30). timeout(1) is Git Bash default-install
# (Rule 16-safe); 10s >> any real payload delivery; on expiry the partial payload
# proceeds -- a truncated payload fails the jq parse and exits empty and loud in
# the starvation counter, never a hung process.
if command -v timeout >/dev/null 2>&1; then
  HOOK_INPUT="$(timeout 10 cat 2>/dev/null || true)"
else
  HOOK_INPUT="$(cat)"
fi

# jq resolution LADDER (NFRA_TOOLCHECK.P1 req#1): must not depend on SCRIPT_DIR
# alone -- the PostToolUse shell's cd fails intermittently (TELEMETRY_HOOK_NO_JQ
# x252 was starvation from exactly that, not a genuinely missing jq).
SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "${SCRIPT_DIR}/../.." 2>/dev/null && pwd)}"
[ -z "${ROOT}" ] && ROOT="."
JQ=""
for _cand in "${CLAUDE_PROJECT_DIR:-}/.tools/jq.exe" ".tools/jq.exe" "${SCRIPT_DIR}/../jq.exe"; do
    if [ -x "${_cand}" ]; then JQ="${_cand}"; break; fi
done
if [ -z "${JQ}" ] && command -v jq >/dev/null 2>&1; then JQ="jq"; fi

if [ -z "${JQ}" ]; then
    # GUARDED-JQ-FALLBACK: jq genuinely unavailable at every candidate. DO NOT
    # starve the USED-axis. Emit a best-effort telemetry line with PURE BASH.
    # Privacy invariant HOLDS: only tool_name + session_id are extracted.
    # (Commitment detection needs jq and correctly stays dark here -- identical
    # to its lifelong behavior in a jq-less shell, now visible in this comment
    # instead of silent.)
    set +e
    _sid="${CLAUDE_CODE_SESSION_ID:-}"
    if [ -z "${_sid}" ]; then
        _sid="$(printf '%s' "${HOOK_INPUT}" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
    fi
    _tool="$(printf '%s' "${HOOK_INPUT}" | sed -n 's/.*"tool_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
    [ -z "${_tool}" ] && _tool="_unknown_"
    _agent=""
    [ -n "${_sid}" ] && _agent="$(cat "${ROOT}/org/mcp/sessions/${_sid}.serial" 2>/dev/null)"
    [ -z "${_agent}" ] && _agent="${OPAL_AGENT_SERIAL:-$(awk -F= '/^SERIAL=/{print $2}' "${ROOT}/.comp-graph/.agent_context" 2>/dev/null)}"
    [ -z "${_agent}" ] && _agent="_unknown_lane_check_needed"
    _ts="$(date -u +%FT%T.%3NZ 2>/dev/null || date -u +%FT%TZ)"
    _tsu="$(date +%s 2>/dev/null)"
    _jpath="${ROOT}/org/mcp/agent_telemetry/${_agent}.jsonl"
    mkdir -p "$(dirname "${_jpath}")" 2>/dev/null
    printf '{"ts":"%s","ts_unix":%s,"serial":"%s","tool_name":"%s","kind":"work","serial_source":"nojq-fallback","session_id":"%s"}\n' \
        "${_ts}" "${_tsu:-0}" "${_agent}" "${_tool}" "${_sid}" >> "${_jpath}" 2>/dev/null
    echo "${_ts} TELEMETRY_HOOK_NO_JQ_FALLBACK_EMITTED session_id=${_sid} tool=${_tool} serial=${_agent}" >> "${ROOT}/org/mcp/hook_errors.log" 2>/dev/null
    exit 0
fi
export JQ

# Session-id-keyed serial resolution (canonical section 7.2 binding).
SESSION_ID="$(echo "${HOOK_INPUT}" | "$JQ" -r '.session_id // empty')"
if [[ -z "${SESSION_ID}" && -n "${CLAUDE_CODE_SESSION_ID:-}" ]]; then
    SESSION_ID="${CLAUDE_CODE_SESSION_ID}"
fi

# FREEFORM standdown (shared /freeform marker with comp-tool-hud.sh). Covers BOTH
# jobs -- the standalone commitment hook carried the identical block, so a live
# marker standing the whole file down preserves both semantics exactly.
if [[ -n "${SESSION_ID}" ]]; then
    _FF="${ROOT}/org/mcp/sessions/${SESSION_ID}.freeform"
    if [[ -f "${_FF}" ]]; then
        _FF_EXP="$(tr -dc '0-9' < "${_FF}" 2>/dev/null || true)"
        _FF_NOW="$(date +%s 2>/dev/null | tr -dc '0-9' || true)"
        if [[ -n "${_FF_EXP}" && -n "${_FF_NOW}" && "${_FF_NOW}" -lt "${_FF_EXP}" ]]; then
            exit 0
        fi
    fi
fi

AGENT=""
if [[ -n "${SESSION_ID}" ]]; then
    AGENT="$(cat "${ROOT}/org/mcp/sessions/${SESSION_ID}.serial" 2>/dev/null || echo "")"
fi
SERIAL_SOURCE="session-id-keyed"
# Session-keyed clobber-PROOF secondary BEFORE the shared .agent_context fallback.
if [[ -z "${AGENT:-}" && -n "${SESSION_ID}" ]]; then
    _MK="$(ls -t "${ROOT}/org/mcp/sessions/${SESSION_ID}."*.orphan-cleaned 2>/dev/null | head -1 || true)"
    if [[ -n "${_MK}" ]]; then
        AGENT="$(basename "${_MK}")"; AGENT="${AGENT#"${SESSION_ID}".}"; AGENT="${AGENT%.orphan-cleaned}"
        SERIAL_SOURCE="session-id-keyed-marker"
    fi
fi
if [[ -z "${AGENT:-}" ]]; then
    AGENT="${OPAL_AGENT_SERIAL:-$(awk -F= '/^SERIAL=/{print $2}' "${ROOT}/.comp-graph/.agent_context" 2>/dev/null)}"
    SERIAL_SOURCE="fallback"
fi
if [[ -z "${AGENT:-}" ]]; then
    AGENT="_unknown_lane_check_needed"
    SERIAL_SOURCE="missing"
    echo "$(date -u +%FT%TZ) WARN: hook unresolved serial; session_id=${SESSION_ID}" >> "${ROOT}/org/mcp/hook_errors.log"
fi

TOOL_NAME="$(echo "${HOOK_INPUT}" | "$JQ" -r '.tool_name // "_unknown_"')"
TS_UNIX="$(date +%s.%N)"
TS_ISO="$(date -u +%FT%T.%3NZ)"

# ============================================================================
# JOB 1 of 2 -- TELEMETRY (canonical TELEMETRY_LIVENESS_FRAMEWORK.md v0.4)
# ============================================================================

# Kind classification, INLINE (was classify-tool-kind.sh -- one bash spawn per
# tool call; a pure case-match needs no process). Same section 3.2/3.3 tables;
# tool_input reads happen in-memory and are never echoed (CV-B1).
_classify_kind() {
    case "${TOOL_NAME}" in
        Bash)
            local _cmd
            _cmd="$(echo "${HOOK_INPUT}" | "$JQ" -r '.tool_input.command // empty' 2>/dev/null || echo "")"
            case "${_cmd}" in
                *inbox-watch*|*watcher-status*|*kill-orphans*|*cleanup-poller*|*check-inbox*) echo "watcher" ;;
                *) echo "work" ;;
            esac ;;
        Skill)
            local _sk
            _sk="$(echo "${HOOK_INPUT}" | "$JQ" -r '.tool_input.skill // empty' 2>/dev/null || echo "")"
            case "${_sk}" in
                watcher) echo "watcher" ;;
                *)       echo "work" ;;
            esac ;;
        ToolSearch|TaskCreate|TaskUpdate|TaskGet|TaskList|TaskStop|TaskOutput|TaskRead) echo "upkeep" ;;
        ScheduleWakeup|CronCreate|CronDelete|CronList|Monitor|PushNotification) echo "upkeep" ;;
        EnterPlanMode|ExitPlanMode|EnterWorktree|ExitWorktree) echo "upkeep" ;;
        ListMcpResourcesTool|ReadMcpResourceTool) echo "upkeep" ;;
        mcp__opal-agent-comms__register_agent|mcp__opal-agent-comms__heartbeat) echo "upkeep" ;;
        mcp__opal-agent-comms__get_agent_status|mcp__opal-agent-comms__check_inbox|mcp__opal-agent-comms__get_live_agents|mcp__opal-agent-comms__get_org_summary|mcp__opal-agent-comms__list_agents|mcp__opal-agent-comms__list_task_orders) echo "upkeep" ;;
        mcp__opal-agent-comms__set_summary|mcp__opal-agent-comms__deregister_agent|mcp__opal-agent-comms__deregister_all_stale) echo "upkeep" ;;
        *) echo "work" ;;
    esac
}
KIND="$(_classify_kind 2>/dev/null || echo "work")"
[[ -z "${KIND}" ]] && KIND="work"

# bg_task event detection (canonical section 4)
BG_EVENT="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.event // empty')"
BG_TASK_ID="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.task_id // empty')"
BG_EXIT_CODE="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.exit_code // empty')"

# CV-B1 PRIVACY INVARIANT ENFORCEMENT -- allowed fields enumerated explicitly.
JSONL_LINE="$("$JQ" -nc \
    --arg ts "${TS_ISO}" \
    --arg ts_unix "${TS_UNIX}" \
    --arg serial "${AGENT}" \
    --arg tool "${TOOL_NAME}" \
    --arg kind "${KIND}" \
    --arg source "${SERIAL_SOURCE}" \
    --arg sid "${SESSION_ID}" \
    --arg bge "${BG_EVENT}" \
    --arg bgi "${BG_TASK_ID}" \
    --arg bgx "${BG_EXIT_CODE}" \
    '{ts:$ts, ts_unix:($ts_unix|tonumber), serial:$serial, tool_name:$tool, kind:$kind, serial_source:$source, session_id:$sid} +
     (if $bge != "" then {bg_task:{event:$bge, task_id:$bgi, exit_code:($bgx | (try tonumber catch null))}} else {} end)')"

# SYNC: jsonl write (durability)
JSONL_PATH="${ROOT}/org/mcp/agent_telemetry/${AGENT}.jsonl"
mkdir -p "$(dirname "${JSONL_PATH}")"
if ! echo "${JSONL_LINE}" >> "${JSONL_PATH}"; then
    echo "$(date -u +%FT%TZ) JSONL_WRITE_FAIL ${AGENT} ${TOOL_NAME}" >> "${ROOT}/org/mcp/hook_errors.log"
fi

# ASYNC: broker hot-path (latency-sensitive; backgrounded). FLAGGED, deliberately
# NOT cut in the consolidation: this is one python launch per tool call and the
# single largest remaining per-call spawn; replacing it needs a design decision
# (long-lived recorder / batching), not a cleanup edit. See the 2026-07-30 audit.
{ python3 "${ROOT}/.tools/hooks/broker-record-tool-call.py" \
    --serial "${AGENT}" \
    --kind "${KIND}" \
    --tool-name "${TOOL_NAME}" \
    --ts-unix "${TS_UNIX}" \
    ${BG_EVENT:+--bg-event "${BG_EVENT}" --bg-task-id "${BG_TASK_ID}"} \
    ${BG_EXIT_CODE:+--bg-exit-code "${BG_EXIT_CODE}"} \
    2>/dev/null & } &> /dev/null
disown 2>/dev/null || true

# ============================================================================
# JOB 2 of 2 -- ACTIVE-COMMITMENT DETECTION (was post-send-commitment.sh)
# Short-circuits on everything except send_message, so the common path costs a
# string compare. Ported verbatim: phrase tables, negation table, DESC build,
# append via org/mcp/append-commitment.sh. Differences from the standalone are
# the two strengthenings in the file header (shared jq ladder; session-keyed
# serial), nothing else.
# ============================================================================
if [ "${TOOL_NAME}" = "mcp__opal-agent-comms__send_message" ] \
   && [ -n "${AGENT}" ] && [ "${AGENT}" != "_unknown_lane_check_needed" ]; then
    BODY=$(printf '%s' "$HOOK_INPUT" | "$JQ" -r '.tool_input.body // ""' 2>/dev/null || echo "")
    if [ -n "$BODY" ]; then
        SUBJECT=$(printf '%s' "$HOOK_INPUT" | "$JQ" -r '.tool_input.subject // ""' 2>/dev/null || echo "")
        TO_AGENT=$(printf '%s' "$HOOK_INPUT" | "$JQ" -r '.tool_input.to_agent // ""' 2>/dev/null || echo "")
        LOWER_BODY=$(printf '%s' "$BODY" | tr '[:upper:]' '[:lower:]')
        MATCHED=0
        for phrase in \
            "next turn" "next cycle" "next wake" "standing by on" "pending dispatch" \
            "drafting next" "queued for" "follow-up to" "follow on to" \
            "i'll draft" "i'll dispatch" "i'll execute" "i'll ship" "i'll route" \
            "i'll reply" "i'll surface" "i'll send" "i'll commit" \
            "i will draft" "i will dispatch" "i will execute" "i will ship" \
            "i will route" "i will reply" "i will surface" \
            "i need to draft" "i need to dispatch" "i plan to" \
            "awaiting your" "awaiting principal" "eta " ; do
            if printf '%s' "$LOWER_BODY" | grep -F -q "$phrase"; then
                MATCHED=1
                break
            fi
        done
        if [ "$MATCHED" -eq 1 ]; then
            NEGATED=0
            for neg in \
                "won't" "wont " "will not" "not going to" "no commit" \
                "nothing to dispatch" "nothing to ledger" "nothing to surface" \
                "no urgency" "no action required" ; do
                if printf '%s' "$LOWER_BODY" | grep -F -q "$neg"; then
                    NEGATED=1
                    break
                fi
            done
            if [ "$NEGATED" -eq 0 ]; then
                if [ -n "$SUBJECT" ]; then
                    DESC=$(printf '%s' "$SUBJECT" | sed -E 's/^[A-Z][A-Z 0-9_]*[—-][ ]*//; s/[|]/_/g')
                else
                    DESC=$(printf '%s' "$BODY" | head -c 200 | tr '\n' ' ' | sed 's/[|]/_/g')
                fi
                DESC=$(printf '%s' "$DESC" | head -c 250)
                [ -n "$TO_AGENT" ] && DESC="[->$TO_AGENT] $DESC"
                bash "${ROOT}/org/mcp/append-commitment.sh" "$AGENT" "$DESC" >/dev/null 2>&1 || true
            fi
        fi
    fi
fi

exit 0
