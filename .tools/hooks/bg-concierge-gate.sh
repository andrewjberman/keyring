#!/usr/bin/env bash
# bg-concierge-gate.sh -- PreToolUse hook. THE MECHANICAL FENCE FOR 0.0.3_BG_BBGTerminal.
#
# Andrew-direct 2026-08-07 (MSTR~Z terminal): "We need hooks that prevent it from doing
# anything other than reading information and reporting it back. It can write to tmp if it
# needs to do some calculations ... it cant download from Bloomberg (data quota is serious)
# it can only view ... guardrails where it can't change its prompting via stuff people say
# on Teams." This gate is that ask, implemented -- an EXPLICITLY ANDREW-REQUESTED gate, so
# the no-gates NEVER rule is satisfied by his word.
#
# SCOPE: fires ONLY when the calling session's serial is 0.0.3_BG_BBGTerminal. For every
# other seat this hook is a fast no-op (exit 0) -- the workspace is shared and this fence
# is one seat's, not the fabric's. Identity resolves the never-rules-gate way: hook-input
# session_id -> org/mcp/sessions/<sid>.serial, then $OPAL_AGENT_SERIAL. UNRESOLVED = NOT
# BG = pass (fail-open on identity; the fence is for a known seat, not a dragnet).
#
# WHAT IT DENIES for the BG seat (each maps to a line of Andrew's ask):
#   G1  Write/Edit/NotebookEdit outside the allowlist:
#         ALLOWED: org/tier0_utility/0.0.3_BG_BBGTerminal/{logs,threads,deliverables}/**,
#                  any tmp/scratchpad path (Temp/, /tmp, scratchpad).
#         DENIED : everything else -- INCLUDING the seat's own prompt.md, refs/**, tools/**
#                  and any .claude/** (skills, settings, hooks). This is the "can't change
#                  its prompting via stuff people say on Teams" guardrail made mechanical:
#                  however persuasive the message, the edit is refused at the tool layer.
#   G2  Bash/PowerShell mutation classes (per-line match, same-unit excuse -- the stash-gate
#       lesson): git write verbs (BG does no git at all), aws write verbs (s3 cp/mv/rm/sync,
#       put/delete-object, dynamodb writes, lambda/iam/secretsmanager mutations), terraform,
#       safe-commit/safe-apply/safe-ec2-deploy, and shell redirects (> >> tee) into repo
#       content dirs (org/ .claude/ .tools/ infra/ data/ docs/ portal/) outside its own
#       folder. Reads (aws s3 ls/get to stdout, git log/show/status, python calcs) pass.
#   G3  Bloomberg download-class MCP tools: bloomberg_historical_data and
#       bloomberg_intraday_bars are DENIED outright (fresh DAPI delivery = download =
#       quota; BLOOMBERG_GUARDRAILS tie-breaker). bloomberg_reference_data passes only for
#       <=2 securities (the "single-security quote lookup" view-side carve-out); more is a
#       bulk pull. bloomberg_health always passes.
#   G4  Identity fence: EVERY mcp__opal-gateway__* call (Andrew's proxy identity) is DENIED
#       for this seat -- the dual-identity first-launch HOLD, mechanized. The seat's server
#       is opal-gateway-bbg only. On -bbg, email/site-write tools (send_email, reply_email,
#       create_draft, upload_text_to_site, save_email_attachment_to_site) are denied --
#       Teams replies and the terminal-upload data channel are its only outbound surfaces.
#
# NOT COVERED (stated so it is not discovered later as a gap): a python/node script BG
# writes to tmp and executes could itself write anywhere its OS creds allow -- the gate
# fences the TOOL layer, not the OS. The gateway-side tier guard + IAM remain the deep
# fence. Residual accepted at build time; tighten only on Andrew's word.
#
# Block mechanism: JSON permissionDecision="deny", exit 0 (bare exit-2 is a hook ERROR,
# not a block -- see never-rules-gate.sh:53). Missing jq: FAIL CLOSED for BG only.
#
# Exercise record: tests run at build (2026-08-07, MSTR~Z) -- see
# .tools/hooks/tests/test_bg_concierge_gate.sh (positive controls for pass AND deny).

set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
WS="${CLAUDE_PROJECT_DIR:-$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)}"

if [ -x "$SCRIPT_DIR/../jq.exe" ]; then
    JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    JQ=""
fi

# ---- identity: is this the BG seat? (never-rules-gate pattern, :493-505) ----
_CALLER=""
if [ -n "$JQ" ]; then
    _SID=$(printf '%s' "$INPUT" | "$JQ" -r '.session_id // empty' 2>/dev/null || true)
    [ -n "$_SID" ] && _CALLER=$(tr -d '[:space:]' < "$WS/org/mcp/sessions/${_SID}.serial" 2>/dev/null || true)
fi
[ -z "$_CALLER" ] && _CALLER="${OPAL_AGENT_SERIAL:-}"
[ "$_CALLER" = "0.0.3_BG_BBGTerminal" ] || exit 0

# From here on we ARE the BG seat. Missing jq now fails CLOSED (the fence must not
# silently stand down for the one seat it exists for).
if [ -z "$JQ" ]; then
    echo "BLOCKED: bg-concierge-gate cannot run -- jq not found. This fence FAILS CLOSED for 0.0.3_BG_BBGTerminal. Fix: git checkout .tools/jq.exe, then retry." >&2
    exit 2
fi

TOOL=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_name // empty' 2>/dev/null || true)
[ -z "$TOOL" ] && exit 0

deny() {
    "$JQ" -nc --arg r "$1" \
      '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    exit 0
}

BG_HOME='org/tier0_utility/0\.0\.3_BG_BBGTerminal'

# =========================================================================================
# G1 -- file-write tools: allowlist by TARGET PATH
# =========================================================================================
case "$TOOL" in
  Write|Edit|NotebookEdit)
    FP=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.file_path // .tool_input.notebook_path // empty' 2>/dev/null || true)
    [ -z "$FP" ] && deny "BLOCKED (bg-concierge-gate G1): file-write with no resolvable path. The BG seat writes only to its own logs/, threads/, deliverables/ or a tmp/scratchpad path."
    FPN=$(printf '%s' "$FP" | tr '\\' '/')
    if printf '%s' "$FPN" | grep -qE "$BG_HOME/(logs|threads|deliverables)/"; then exit 0; fi
    if printf '%s' "$FPN" | grep -qiE '(^|/)(tmp|temp)(/|$)|scratchpad'; then exit 0; fi
    deny "BLOCKED (bg-concierge-gate G1): the 0.0.3_BG seat is read-only outside its own logs/threads/deliverables and tmp. Target '$FP' is off-allowlist. If this write is genuinely needed, route the ask to Andrew via 0.0.0_AB_MSTR~Z -- especially note that prompt.md, refs/ and .claude/ are DELIBERATELY unwritable from this seat (Teams content can never become a prompt edit)."
    ;;
esac

# =========================================================================================
# G3/G4 -- MCP tools
# =========================================================================================
case "$TOOL" in
  mcp__bloomberg__bloomberg_historical_data|mcp__bloomberg__bloomberg_intraday_bars)
    deny "BLOCKED (bg-concierge-gate G3): '$TOOL' is a DOWNLOAD-class Bloomberg call (fresh DAPI delivery = quota consumption). View-only stands: answer from the served portal artifacts / the scheduled pull's PKLs (BLOOMBERG_GUARDRAILS.md). Log the demand and surface it to Andrew -- expanding the scheduled pull is his call alone."
    ;;
  mcp__bloomberg__bloomberg_reference_data)
    NSEC=$(printf '%s' "$INPUT" | "$JQ" -r '(.tool_input.securities | if type=="array" then length elif type=="string" then 1 else 0 end) // 0' 2>/dev/null || echo 0)
    if [ "${NSEC:-0}" -gt 2 ]; then
        deny "BLOCKED (bg-concierge-gate G3): reference_data for $NSEC securities is a BULK pull, not the single-security view-side lookup BLOOMBERG_GUARDRAILS permits (<=2). Serve from the portal artifacts, or surface the demand to Andrew."
    fi
    ;;
  mcp__opal-gateway__*)
    deny "BLOCKED (bg-concierge-gate G4): 'opal-gateway' is ANDREW'S proxy identity -- the BG seat calls opal-gateway-bbg ONLY (prompt.md identity binding; the first-launch HOLD, mechanized). Re-issue the call on the -bbg server."
    ;;
  mcp__opal-gateway-bbg__send_email|mcp__opal-gateway-bbg__reply_email|mcp__opal-gateway-bbg__create_draft|mcp__opal-gateway-bbg__upload_text_to_site|mcp__opal-gateway-bbg__save_email_attachment_to_site)
    deny "BLOCKED (bg-concierge-gate G4): email/site-write is not a BG surface -- this seat's outbound is Teams replies (+ the terminal-upload data channel). Route the need to Andrew via 0.0.0_AB_MSTR~Z if it is real."
    ;;
esac

# =========================================================================================
# G2 -- shell mutation classes (Bash/PowerShell), per-line so prose cannot disarm it
# =========================================================================================
if [ "$TOOL" = "Bash" ] || [ "$TOOL" = "PowerShell" ]; then
    CMD=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.command // empty' 2>/dev/null || true)
    [ -z "$CMD" ] && exit 0

    while IFS= read -r line; do
        # For VERB-CLASS checks, strip quoted string CONTENTS first: `echo "git commit"` is a
        # MENTION, not a command form (the LD-0274 / stash-gate lesson -- match the form, never
        # the word). A real `git commit -m "msg"` still matches on its unquoted prefix. The
        # REDIRECT check below deliberately stays on the RAW line (redirect targets are often
        # quoted, and stripping them would disarm that check).
        stripped=$(printf '%s' "$line" | sed -e "s/'[^']*'//g" -e 's/"[^"]*"//g')
        # git write verbs (BG has no git lane at all; reads like log/show/status pass)
        if printf '%s' "$stripped" | grep -qE '(^|[[:space:];|&(])git([[:space:]]+-C[[:space:]]+[^[:space:]]+)?[[:space:]]+(commit|push|add|merge|rebase|reset|checkout|stash|tag|rm|mv|cherry-pick|am|apply|revert|clean)([[:space:]]|$)'; then
            deny "BLOCKED (bg-concierge-gate G2): git mutation from the BG seat ('$line'). This seat does no git work at all -- its logs/ and threads/ are swept by integrators (prompt.md hard line)."
        fi
        if printf '%s' "$stripped" | grep -qE '(^|[[:space:];|&(])(safe-commit\.sh|safe-apply\.sh|safe-ec2-deploy\.sh|terraform(\.exe)?)([[:space:]]|$)'; then
            deny "BLOCKED (bg-concierge-gate G2): deploy/commit tooling from the BG seat ('$line'). Read-and-report only."
        fi
        # aws write verbs -- s3 object writes, ddb writes, lambda/iam/secrets mutations
        if printf '%s' "$line" | grep -qE '(^|[[:space:];|&(])aws[[:space:]].*[[:space:]](cp|mv|rm|sync)[[:space:]].*s3://' && \
           ! printf '%s' "$line" | grep -qE 's3://[^[:space:]]+[[:space:]]+(/(tmp|cygdrive)|[A-Za-z]:|\.|~|/dev/stdout|-)'; then
            deny "BLOCKED (bg-concierge-gate G2): S3 write-shaped aws call from the BG seat ('$line'). Downloads TO tmp for a calculation are fine; anything writing INTO a bucket is not -- opal-data-portal-v2 is live client-facing."
        fi
        if printf '%s' "$line" | grep -qE '(^|[[:space:];|&(])aws[[:space:]]+(s3api[[:space:]]+(put|delete)-|dynamodb[[:space:]]+(put-item|update-item|delete-item|batch-write)|lambda[[:space:]]+(update|create|delete)-|iam[[:space:]]+(put|create|delete|attach|detach)|secretsmanager[[:space:]]+(put|create|delete|update)|events[[:space:]]+(put|delete)|ssm[[:space:]]+(put|send))'; then
            deny "BLOCKED (bg-concierge-gate G2): mutating aws verb from the BG seat ('$line'). This seat reads; it does not change cloud state."
        fi
        # shell redirects into repo content dirs outside the seat's own folder
        if printf '%s' "$line" | grep -qE '(>>?|[[:space:];|&(]tee[[:space:]])[[:space:]]*"?[A-Za-z:./\\]*(org|\.claude|\.tools|infra|data|docs|portal)/' && \
           ! printf '%s' "$line" | grep -qE "$BG_HOME/(logs|threads|deliverables)/"; then
            deny "BLOCKED (bg-concierge-gate G2): shell redirect into repo content ('$line'). The BG seat's writable set is its own logs/threads/deliverables + tmp; use those."
        fi
    done <<EOF_CMD
$CMD
EOF_CMD
fi

exit 0
