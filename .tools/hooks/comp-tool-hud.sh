#!/usr/bin/env bash
# comp-tool-hud.sh -- PreToolUse ADVISORY hook (NFRA_TOOLHUD #1, Andrew-direct 2026-06-15).
#
# THE PROBLEM: comp-* tools are stronger (deterministic, repo-scoped, fast) than
# blind grep, but grep is the zero-friction default reflex -- so agents grep
# instead of reaching for the better tool. Documentation is the FLOOR; salience-
# at-decision-time is the real currency. This hook puts the right tool on the HUD
# AT THE MOMENT an agent reaches for grep.
#
# WHAT IT DOES: on a Grep/Glob whose query matches a HIGH-CONFIDENCE comp-answerable
# class, surface the specific comp call via `additionalContext` (a system reminder
# the model sees) -- ADVISORY: the search still proceeds. Once per class per
# session (anti-noise). FIRST-MATCH-WINS (priority order). Plus a NEGATIVE FILTER
# (CVO #3 baseline bdf7a0a9a: the precision-maker -- without it the advisory becomes
# ignorable noise).
#
# Pattern set + negative filter + priority = CVO #3 measured baseline (~15-20% of
# clean repo relationship-searches are comp-answerable; comp-pipescript + portal-
# tools = ~80% of bypass volume). Re-tune to the post-hook re-measure (hud3_classify.py).
#
# Mechanism (claude-code-guide confirmed): stdout JSON
#   {"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"..."}} + exit 0.
# FAIL-SAFE: any jq/parse issue -> silent exit 0 (NEVER break a search). No -e (grep no-match ok).
set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
if [ -x "$SCRIPT_DIR/../jq.exe" ]; then JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then JQ="jq"
else exit 0; fi

# Extract fields with SEPARATE jq calls -- NOT one @tsv + IFS read. A single
# IFS-whitespace (tab) read COLLAPSES consecutive empty fields and shifts left, so
# an absent session_id would SILENTLY no-op the whole hook (CVO catch -- the
# silent-dead-hook failure class). Separate calls can't collapse. Check tool first
# and exit early (saves the other calls on the common non-search path).
tool=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_name // ""' 2>/dev/null) || exit 0
case "$tool" in Grep|Glob) : ;; *) exit 0 ;; esac
sid=$(printf '%s' "$INPUT" | "$JQ" -r '.session_id // ""' 2>/dev/null || true)
query=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.pattern // .tool_input.file_path // ""' 2>/dev/null || true)
gpath=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.path // ""' 2>/dev/null || true)
[ -z "$query" ] && exit 0

# --- NEGATIVE FILTER (CVO #3: the non-noise guarantee). Suppress when: ---
#  (a) the search is scoped to a SINGLE FILE -> grepping a file's internals, NOT a
#      relationship search (comp-pipescript io gives the I/O contract, not internals).
#  (b) the query already references a comp tool -> tool-use / archaeology, not a bypass.
#  ((c) aws-against-live is inherently excluded: this hook matches Grep|Glob only, not Bash.)
if printf '%s' "$gpath" | grep -qE '\.[A-Za-z0-9]+$'; then exit 0; fi      # path ends in a file extension = single file
if printf '%s' "$query" | grep -qE 'comp-|pipescript'; then exit 0; fi      # already a comp-tool reference

WS="$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)" || WS="."

# --- CLASS MATCH (first-match-wins, priority = CVO bypass-volume ranking) ---
class=""; msg=""
if printf '%s' "$query" | grep -qE '(^|[^A-Za-z0-9_])(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?([^A-Za-z0-9_]|$)'; then
  _id=$(printf '%s' "$query" | grep -oE '(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?' | head -1)
  class=script_id
  msg="comp-tool on the HUD: searching for gold-script id '${_id}'. \`comp-pipescript io ${_id}\` = its inputs/outputs + upstream writers + downstream consumers (or \`feeds\`/\`consumers\` for one direction); \`pipescript --resource ${_id}\` = its whole named thread. Deterministic, no tree-grep. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 's3://opal-|opal-data-[A-Za-z0-9_]+|(^|/)(gold|platinum|silver)/|\.parquet([^A-Za-z0-9]|$)'; then
  class=s3_artifact
  msg="comp-tool on the HUD: searching for an S3 artifact/key. \`pipescript --resource <substr>\` = which named thread + producer owns it; \`comp-pipescript io <script>\` = a gold script's reads/writes incl. portal consumers. Deterministic. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'portal/src/|\.tsx([^A-Za-z0-9]|$)|/api/(scoped|general|private|public)/|getAdvisor[A-Za-z]*'; then
  class=portal
  msg="comp-tool on the HUD: searching a portal component/route. \`comp-transform schema-check <Component>\` = its data-prop type contract (MISSING = runtime undefined); \`comp-routes behaviors\` = the serving/CF path (4xx/HTML masking). \`pipescript <thread>\` shows the backend that feeds it. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'opal-[a-z][a-z-]+|(inf|bd)-[a-z-]+-(trigger|runner|publisher|daily)|yang-generate-[a-z-]+|causality-[a-z-]+'; then
  class=lambda
  msg="comp-tool on the HUD: searching for a lambda. \`comp-iam service <fn>\` = its IAM/perms; \`comp-aws\` = its edges/blast; \`pipescript --resource <fn>\` = which named thread it's in. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'iam[_-]?role|:role/|aws_iam_policy'; then
  class=iam_role
  msg="comp-tool on the HUD: searching for an IAM role/policy. \`comp-iam service <lambda>\` / \`comp-iam gaps\` = perms before deploy (mind: a Principal:* on Effect=Deny is a GUARDRAIL, not a public grant). (advisory -- your search still runs.)"
fi
[ -z "$class" ] && exit 0

# log every hit (CVO's before/after measurement), then advise ONCE per class per session
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  HUD-HIT  tool=$tool  class=$class  q=$(printf '%s' "$query" | head -c 80)" >> "$WS/org/mcp/comp-tool-hud.log" 2>/dev/null || true
if [ -n "$sid" ]; then
  d="$WS/org/mcp/sessions"; mkdir -p "$d" 2>/dev/null || true
  m="$d/${sid}.comphud.${class}.seen"
  [ -f "$m" ] && exit 0          # already advised this class this session -> silent (logged above)
  : > "$m" 2>/dev/null || true
fi
enc=$(printf '%s' "$msg" | "$JQ" -Rs . 2>/dev/null) || exit 0
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":%s}}' "$enc"
exit 0
