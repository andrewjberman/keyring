#!/bin/bash
# post-tool-telemetry.sh -- LD-0070 WS-B WB-2 implementation
# Reads PostToolUse hook stdin per Claude Code spec; emits telemetry per canonical
# TELEMETRY_LIVENESS_FRAMEWORK.md v0.4 §3 (kind classification + jsonl write + broker hot-path).
#
# CANONICAL SOURCE: org/mcp/hooks/post-tool-telemetry.sh (version-controlled)
# INSTALL TARGET:   .tools/hooks/post-tool-telemetry.sh (gitignored, copied via install)
# INSTALL SCRIPT:   .tools/hooks/install-telemetry-hook.sh (idempotent + marker check)
#
# CV-B1 PRIVACY INVARIANT (canonical §3.4 HARD RULE):
#   Hook writes tool_name ONLY; tool arguments + tool outputs are NEVER written to jsonl.
#   The jq -nc invocation below explicitly enumerates allowed fields. Adding a new field
#   requires modifying this template (code-review surface).

set -euo pipefail

HOOK_INPUT="$(cat)"

# Resolve jq ROBUSTLY. Claude Code's PostToolUse hook shell does NOT load the user
# profile, so workspace .tools/ is NOT on PATH. The OLD resolution depended on
# SCRIPT_DIR = $(cd $(dirname $0)) resolving to .tools/hooks/ -- but that cd fails
# INTERMITTENTLY in the PostToolUse shell (SCRIPT_DIR falls back to "."), so
# ${SCRIPT_DIR}/../jq.exe pointed at the wrong place AND `command -v jq` also failed
# -> the else branch STARVED telemetry (NFRA_TOOLCHECK: TELEMETRY_HOOK_NO_JQ x252,
# script_dir=. -- an intermittent USED-axis starvation, NOT a genuine missing jq).
# FIX (NFRA_TOOLCHECK.P1 req#1, 0.8.0_AE_CloudComp~D 2026-07-08): a resolution LADDER
# that does NOT depend on SCRIPT_DIR -- most-robust first:
#   (1) $CLAUDE_PROJECT_DIR/.tools/jq.exe  (the SAME var settings.json uses to launch this hook)
#   (2) .tools/jq.exe                       (cwd-relative; the hook runs from the workspace root)
#   (3) ${SCRIPT_DIR}/../jq.exe             (works when dirname DID resolve)
#   (4) command -v jq                       (Linux/Mac dev on PATH)
# and even when jq is GENUINELY absent everywhere, the pure-bash GUARDED-JQ-FALLBACK
# below STILL emits a telemetry line (CLAUDE.md r16 canonical guarded-util pattern,
# org/mcp/inbox-watch.sh) -- the USED-axis is never starved again.
SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
# DC-5 spill fix (OPAL_TAXONOMY, CTO ruling-20 2026-07-17): a PostToolUse hook fires with the AGENT's
# cwd, NOT the repo root -- so every REPO-RELATIVE path below spills into {cwd}/org/mcp/... when an
# agent is cd'd inside e.g. data/assets/scripts/. ANCHOR all repo-relative reads/writes to the repo
# root: $CLAUDE_PROJECT_DIR (the SAME var line ~37 already trusts for jq) preferred; fallback derives
# it from the INSTALLED hook location (.tools/hooks/ -> ../.. = repo root). Closes the spill CLASS.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "${SCRIPT_DIR}/../.." 2>/dev/null && pwd)}"
[ -z "${ROOT}" ] && ROOT="."
JQ=""
for _cand in "${CLAUDE_PROJECT_DIR:-}/.tools/jq.exe" ".tools/jq.exe" "${SCRIPT_DIR}/../jq.exe"; do
    # -x on a non-existent path is simply false, so an empty $CLAUDE_PROJECT_DIR (-> /.tools/jq.exe) is skipped.
    if [ -x "${_cand}" ]; then JQ="${_cand}"; break; fi
done
if [ -z "${JQ}" ] && command -v jq >/dev/null 2>&1; then JQ="jq"; fi

if [ -z "${JQ}" ]; then
    # GUARDED-JQ-FALLBACK: jq genuinely unavailable at every candidate. DO NOT starve the
    # USED-axis (the old code exit-0'd here, writing NOTHING). Emit a best-effort telemetry
    # line with PURE BASH. Privacy invariant HOLDS: we extract ONLY tool_name + session_id
    # (never tool args/outputs). Fail-open (set +e -- telemetry is non-critical, never crash).
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
export JQ   # classify-tool-kind.sh honors $JQ (same PATH-less hook-shell condition)

# §7.2 session-id-keyed serial resolution (canonical §7.2 binding)
SESSION_ID="$(echo "${HOOK_INPUT}" | "$JQ" -r '.session_id // empty')"
# WB-1.1 empirical fix (2026-05-26T~04:05Z, commit 0e8fffe1e): Claude Code hook stdin does NOT
# always carry .session_id field in production runtime; $CLAUDE_CODE_SESSION_ID env var is the
# reliable source per LD-0070 §7.2.
if [[ -z "${SESSION_ID}" && -n "${CLAUDE_CODE_SESSION_ID:-}" ]]; then
    SESSION_ID="${CLAUDE_CODE_SESSION_ID}"
fi
# --- FREEFORM standdown (shared /freeform marker with the comp-rail comp-tool-hud.sh) -----------
# If this session has a LIVE (unexpired) freeform marker, telemetry is a friction TAX -- NOT a
# safety guard -- so stand down: a freestyling agent runs unhampered + un-instrumented for the
# speed push. Mirrors comp-tool-hud.sh's freeform block (same marker, same expiry parse).
# SCRIPT_DIR/../../ = repo root (robust regardless of agent cwd). Best-effort: any ambiguity just
# records telemetry as normal (telemetry is non-critical -- fail-open is correct here).
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
if [[ -n "${SESSION_ID}" ]]; then
    AGENT="$(cat "${ROOT}/org/mcp/sessions/${SESSION_ID}.serial" 2>/dev/null || echo "")"
fi
SERIAL_SOURCE="session-id-keyed"
# session-keyed clobber-PROOF secondary BEFORE the shared .agent_context fallback (register_agent hook
# writes org/mcp/sessions/${SESSION_ID}.${serial}.orphan-cleaned -- serial-in-filename, this-session-scoped;
# fixes the mis-attribution where an absent .serial fell to .agent_context last-writer -- CloudOps 5x defect twin).
if [[ -z "${AGENT:-}" && -n "${SESSION_ID}" ]]; then
    _MK="$(ls -t "${ROOT}/org/mcp/sessions/${SESSION_ID}."*.orphan-cleaned 2>/dev/null | head -1 || true)"
    if [[ -n "${_MK}" ]]; then
        AGENT="$(basename "${_MK}")"; AGENT="${AGENT#"${SESSION_ID}".}"; AGENT="${AGENT%.orphan-cleaned}"
        SERIAL_SOURCE="session-id-keyed-marker"
    fi
fi
# Fallback chain per canonical §7.4 (OPAL_AGENT_SERIAL env preferred over the shared .agent_context file)
if [[ -z "${AGENT:-}" ]]; then
    AGENT="${OPAL_AGENT_SERIAL:-$(awk -F= '/^SERIAL=/{print $2}' "${ROOT}/.comp-graph/.agent_context" 2>/dev/null)}"
    SERIAL_SOURCE="fallback"
fi
if [[ -z "${AGENT:-}" ]]; then
    AGENT="_unknown_lane_check_needed"
    SERIAL_SOURCE="missing"
    echo "$(date -u +%FT%TZ) WARN: hook unresolved serial; session_id=${SESSION_ID}" >> "${ROOT}/org/mcp/hook_errors.log"
fi

# Parse tool info from hook input
TOOL_NAME="$(echo "${HOOK_INPUT}" | "$JQ" -r '.tool_name // "_unknown_"')"
TS_UNIX="$(date +%s.%N)"
TS_ISO="$(date -u +%FT%T.%3NZ)"

# §3.2 kind classification (canonical §3.2 + §3.3 binding). Resolve via SCRIPT_DIR
# (PATH-less hook shell). Classification is non-fatal: fall back to "work" on any
# classifier error so a classifier hiccup never blocks the durable jsonl write.
KIND="$("${SCRIPT_DIR}/classify-tool-kind.sh" "${TOOL_NAME}" <<<"${HOOK_INPUT}" 2>/dev/null || echo "work")"
[[ -z "${KIND}" ]] && KIND="work"

# bg_task event detection (canonical §4)
BG_EVENT="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.event // empty')"
BG_TASK_ID="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.task_id // empty')"
BG_EXIT_CODE="$(echo "${HOOK_INPUT}" | "$JQ" -r '.bg_task.exit_code // empty')"

# === CV-B1 PRIVACY INVARIANT ENFORCEMENT (canonical §3.4 HARD RULE binding) ===
# Allowed fields enumerated explicitly. DO NOT echo $HOOK_INPUT to jsonl.
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

# §6.1 sync jsonl + async broker hot-path (FN-1 binding)

# SYNC: jsonl write (durability)
JSONL_PATH="${ROOT}/org/mcp/agent_telemetry/${AGENT}.jsonl"
mkdir -p "$(dirname "${JSONL_PATH}")"
if ! echo "${JSONL_LINE}" >> "${JSONL_PATH}"; then
    # §6.4 jsonl write failure handling
    echo "$(date -u +%FT%TZ) JSONL_WRITE_FAIL ${AGENT} ${TOOL_NAME}" >> "${ROOT}/org/mcp/hook_errors.log"
fi

# ASYNC: broker hot-path call (latency-sensitive; backgrounded; nohup so doesn't block exit)
{ python3 "${ROOT}/.tools/hooks/broker-record-tool-call.py" \
    --serial "${AGENT}" \
    --kind "${KIND}" \
    --tool-name "${TOOL_NAME}" \
    --ts-unix "${TS_UNIX}" \
    ${BG_EVENT:+--bg-event "${BG_EVENT}" --bg-task-id "${BG_TASK_ID}"} \
    ${BG_EXIT_CODE:+--bg-exit-code "${BG_EXIT_CODE}"} \
    2>/dev/null & } &> /dev/null
disown 2>/dev/null || true

exit 0
