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

# Resolve jq + classifier deterministically. Claude Code's PostToolUse hook shell
# does NOT load the user profile, so workspace .tools/ is NOT on PATH and a bare
# `jq` call fails 127 -> `set -e` kills the script BEFORE any jsonl/error write
# (silent telemetry death -- root cause of the 05-26->05-29 freeze, AE diag
# 2026-05-29). Resolve relative to this script's location (always .tools/hooks/ at
# runtime), then fall back to PATH for Linux/Mac dev. Same pattern as
# .tools/hooks/block-bare-inbox-watch.sh.
SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
if [ -x "${SCRIPT_DIR}/../jq.exe" ]; then
    JQ="${SCRIPT_DIR}/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    # jq genuinely unavailable -- log once and exit cleanly (never silent-crash).
    echo "$(date -u +%FT%TZ) TELEMETRY_HOOK_NO_JQ session_id=${CLAUDE_CODE_SESSION_ID:-} script_dir=${SCRIPT_DIR}" >> org/mcp/hook_errors.log 2>/dev/null || true
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
if [[ -n "${SESSION_ID}" ]]; then
    AGENT="$(cat "org/mcp/sessions/${SESSION_ID}.serial" 2>/dev/null || echo "")"
fi
# Fallback chain per canonical §7.4
if [[ -z "${AGENT:-}" ]]; then
    AGENT="${OPAL_AGENT_SERIAL:-$(awk -F= '/^SERIAL=/{print $2}' .comp-graph/.agent_context 2>/dev/null)}"
    SERIAL_SOURCE="fallback"
else
    SERIAL_SOURCE="session-id-keyed"
fi
if [[ -z "${AGENT:-}" ]]; then
    AGENT="_unknown_lane_check_needed"
    SERIAL_SOURCE="missing"
    echo "$(date -u +%FT%TZ) WARN: hook unresolved serial; session_id=${SESSION_ID}" >> org/mcp/hook_errors.log
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
JSONL_PATH="org/mcp/agent_telemetry/${AGENT}.jsonl"
mkdir -p "$(dirname "${JSONL_PATH}")"
if ! echo "${JSONL_LINE}" >> "${JSONL_PATH}"; then
    # §6.4 jsonl write failure handling
    echo "$(date -u +%FT%TZ) JSONL_WRITE_FAIL ${AGENT} ${TOOL_NAME}" >> org/mcp/hook_errors.log
fi

# ASYNC: broker hot-path call (latency-sensitive; backgrounded; nohup so doesn't block exit)
{ python3 .tools/hooks/broker-record-tool-call.py \
    --serial "${AGENT}" \
    --kind "${KIND}" \
    --tool-name "${TOOL_NAME}" \
    --ts-unix "${TS_UNIX}" \
    ${BG_EVENT:+--bg-event "${BG_EVENT}" --bg-task-id "${BG_TASK_ID}"} \
    ${BG_EXIT_CODE:+--bg-exit-code "${BG_EXIT_CODE}"} \
    2>/dev/null & } &> /dev/null
disown 2>/dev/null || true

exit 0
