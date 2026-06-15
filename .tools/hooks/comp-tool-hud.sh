#!/usr/bin/env bash
# comp-tool-hud.sh -- PreToolUse ADVISORY hook (NFRA_TOOLHUD #1, Andrew-direct 2026-06-15).
#
# THE PROBLEM: comp-* tools are stronger (deterministic, repo-scoped, fast) than
# blind grep, but grep is the zero-friction default reflex -- so agents grep
# instead of reaching for the better tool. Documentation (CLAUDE.md, the catalog)
# is the FLOOR; salience-at-decision-time is the real currency. This hook puts the
# right tool on the agent's HUD AT THE MOMENT it reaches for grep.
#
# WHAT IT DOES: on a Grep/Glob whose query matches a HIGH-CONFIDENCE comp-answerable
# signature, surface the specific comp call via `additionalContext` (a system
# reminder the model sees) -- ADVISORY: the search still proceeds. Once per
# pattern-class per session (anti-noise: a repeated identical advisory becomes
# ignorable, which is worse than nothing). Precision-over-recall: only patterns
# where a comp tool is almost-certainly the better answer.
#
# Mechanism (claude-code-guide confirmed, docs code.claude.com/docs/en/hooks):
#   stdout JSON {"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"..."}} + exit 0.
# FAIL-SAFE: any jq/parse issue -> silent exit 0 (NEVER break a search). No -e (grep no-match is fine).
#
# Pattern set is TIER-1 (high-confidence). Tune + extend (Read, lambda/portal/IAM
# patterns, the comp-which router #2) to CVO's #3 telemetry baseline when it lands.
set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
if [ -x "$SCRIPT_DIR/../jq.exe" ]; then JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then JQ="jq"
else exit 0; fi   # no jq -> fail-safe pass-through

# ONE jq pass: tool_name, session_id, and the query (Grep/Glob pattern; else file_path).
parsed=$(printf '%s' "$INPUT" | "$JQ" -r '[(.tool_name // ""), (.session_id // ""), (.tool_input.pattern // .tool_input.file_path // "")] | @tsv' 2>/dev/null) || exit 0
IFS=$'\t' read -r tool sid query <<< "$parsed"
case "$tool" in Grep|Glob) : ;; *) exit 0 ;; esac
[ -z "$query" ] && exit 0

WS="$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)" || WS="."

_log() {  # $1=class
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  HUD-HIT  tool=$tool  class=$1  q=$(printf '%s' "$query" | head -c 80)" \
    >> "$WS/org/mcp/comp-tool-hud.log" 2>/dev/null || true
}
_seen_once() {  # $1=class ; returns 0 if ALREADY advised this class this session
  [ -z "$sid" ] && return 1
  local d="$WS/org/mcp/sessions"; mkdir -p "$d" 2>/dev/null || return 1
  local m="$d/${sid}.comphud.$1.seen"
  [ -f "$m" ] && return 0
  : > "$m" 2>/dev/null || true
  return 1
}
_advise() {  # $1=class  $2=message
  _log "$1"
  _seen_once "$1" && exit 0   # already advised this class this session -> stay silent (still logged)
  local enc; enc=$(printf '%s' "$2" | "$JQ" -Rs . 2>/dev/null) || exit 0
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":%s}}' "$enc"
  exit 0
}

# --- TIER-1 high-confidence patterns ---

# A. GOLD/SILVER/BRONZE SCRIPT ID (D_04, INF_C_01, C_07, B_03, A_02, S_00, INF_A_-1)
if printf '%s' "$query" | grep -qE '(^|[^A-Za-z0-9_])(INF_)?[A-DS]_-?[0-9]{1,2}[a-z]?([^A-Za-z0-9_]|$)'; then
  _id=$(printf '%s' "$query" | grep -oE '(INF_)?[A-DS]_-?[0-9]{1,2}[a-z]?' | head -1)
  _advise script_id "comp-tool on the HUD: you're searching for the gold-script id '${_id}'. \`comp-pipescript io ${_id}\` gives its inputs/outputs + upstream writers + downstream consumers deterministically (or \`feeds\`/\`consumers\` for one direction); \`pipescript --resource ${_id}\` shows its whole named thread. Stronger + faster than grep here. (advisory -- your search still runs.)"
fi

# B. S3 ARTIFACT / served key (s3://, platinum|gold|silver|bronze/, .parquet)
if printf '%s' "$query" | grep -qE 's3://|(^|/)(platinum|gold|silver|bronze)/|\.parquet([^A-Za-z0-9]|$)'; then
  _advise s3_artifact "comp-tool on the HUD: you're searching for an S3 artifact/key. \`pipescript --resource <substr>\` names which thread + producer owns it; \`comp-pipescript io <script>\` maps a gold script's reads/writes incl. portal consumers -- deterministic, no blind grep across the tree. (advisory -- your search still runs.)"
fi

exit 0
