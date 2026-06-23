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
case "$tool" in Grep|Glob|Bash) : ;; *) exit 0 ;; esac
sid=$(printf '%s' "$INPUT" | "$JQ" -r '.session_id // ""' 2>/dev/null || true)
# --- FREEFORM escape (Andrew-invoked speed mode, /freeform skill) -----------------------------
# If this session has a LIVE (unexpired) freeform marker, STAND DOWN -- the agent is explicitly
# off the comp-tool rail for a speed push, so no nudge/gate. FAIL-CLOSED: any parse weirdness
# (non-numeric, empty, clock issue) -> fall through to ENFORCE. Safety gates are elsewhere + UNAFFECTED.
if [ -n "$sid" ]; then
  _ff="$SCRIPT_DIR/../../org/mcp/sessions/${sid}.freeform"
  if [ -f "$_ff" ]; then
    _exp=$(tr -dc '0-9' < "$_ff" 2>/dev/null); _now=$(date +%s 2>/dev/null | tr -dc '0-9')
    if [ -n "$_exp" ] && [ -n "$_now" ] && [ "$_now" -lt "$_exp" ] 2>/dev/null; then exit 0; fi
  fi
fi
# Bash -> .command ; Grep/Glob -> .pattern/.file_path. The command-first chain means
# a Bash raw-aws/infra-grep gets matched against the aws-inspection classes below
# (NFRA_TOOLHUD ext 2026-06-18, Andrew-direct: agents reaching for raw aws/grep where
# comp-aws/comp-iam/comp-routes give higher-context answers = the low-context-shoddy risk).
query=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.command // .tool_input.pattern // .tool_input.file_path // ""' 2>/dev/null || true)
gpath=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.path // ""' 2>/dev/null || true)
[ -z "$query" ] && exit 0

# --- NEGATIVE FILTER (CVO #3: the non-noise guarantee). Suppress when: ---
#  (a) the search is scoped to a SINGLE FILE -> grepping a file's internals, NOT a
#      relationship search (comp-pipescript io gives the I/O contract, not internals).
#  (b) the query already references a comp tool -> tool-use / archaeology, not a bypass.
#  (c) Bash OPERATIONAL aws (invoke/deploy/verify/TF) is NOT a relationship/inspection
#      query -> never nudge it (only raw-aws INSPECTION + infra-grep are comp-answerable).
if printf '%s' "$gpath" | grep -qE '\.[A-Za-z0-9]+$'; then exit 0; fi      # path ends in a file extension = single file
if printf '%s' "$query" | grep -qE 'comp-|pipescript'; then exit 0; fi      # already a comp-tool reference
if [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE 'lambda invoke|s3(api)? (cp|sync|put-object|mv)|get-function-configuration|safe-apply|safe-ec2-deploy|safe-commit|terraform |update-function-code|start-build|run-task|dynamodb (put-item|update-item|delete-item|batch-write-item)'; then exit 0; fi
# (d) NON-ESTATE LOCAL CODE LIBRARY (the deck-generation engine deck_generation/) -- a symbol/def/
#     signature/arg-shape lookup INSIDE a self-contained local code library has NO cross-system
#     coupling for a comp-tool to illuminate (comp-tools answer estate/pipeline/IAM/graph/component
#     coupling, NOT intra-library symbol shapes) -> grep/Read is the CORRECT tool, not a bypass.
#     Estate code (data/*/scripts/{gold,silver,bronze}, portal/src, infra, .tf, lambda src) is
#     EXCLUDED -> it stays on the rail. Exiting here means no nudge AND no future broad-grep DENY.
#     (RD deck-engine case 2026-06-23; NFRA_COMPRAIL/LD-0207 Gate-1 carve-out. Allowlist extends as
#     more non-estate libraries surface via the override-telemetry.)
if printf '%s' "$query $gpath" | grep -qE 'deck_generation/' \
   && ! printf '%s' "$query $gpath" | grep -qE 'data/[A-Za-z0-9_]+/scripts/(gold|silver|bronze)|portal/src|infra/aws/|\.tf([^A-Za-z0-9]|$)|(^|[^a-z])lambda'; then exit 0; fi
# a bare `aws s3 ls`/`list-objects` with NO code/ or gold|platinum|silver|json prefix = a generic
# listing (no targeted comp answer) -> stay silent; do NOT fall through to the s3_artifact grep-class
# on the bucket-name alone. (The targeted code//gold/ s3-ls classes below carry code//gold/ so this skips THEM out.)
if [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE 'aws s3(api)? (ls|list-objects)' && ! printf '%s' "$query" | grep -qE 'code/|(^|/)(gold|platinum|silver|json)/'; then exit 0; fi

WS="$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)" || WS="."

# --- CLASS MATCH (first-match-wins, priority = CVO bypass-volume ranking) ---
class=""; msg=""
# Bash raw-aws / infra-grep INSPECTION classes (NFRA_TOOLHUD ext 2026-06-18) -- highest
# priority so a raw-aws inspection gets the aws-framed comp nudge, not the grep-framed one.
if printf '%s' "$query" | grep -qE 'aws iam (get|list|simulate)|aws s3api get-bucket-(policy|acl)|aws lambda get-policy|get-resource-policy'; then
  class=aws_iam_inspect
  msg="comp-tool on the HUD: raw \`aws\` IAM/policy inspection. \`comp-iam service <fn>\` / \`comp-iam gaps\` gives the perms WITH the TF-vs-live reconcile -- it catches a DECLARED-but-unapplied control (the phantom-backstop class: a contract/doc citing a Deny that was planned, never applied) that a single live get-policy will not -- plus the Deny=guardrail-not-public-grant context. Higher-context than raw aws. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE 'aws cloudfront|aws apigateway'; then
  class=aws_route
  msg="comp-tool on the HUD: raw \`aws\` CloudFront/API-GW inspection. \`comp-routes behaviors\`/\`trace\` gives the full serving path + the CF custom-error-rule masking (4xx->HTML) a raw get-distribution won't surface. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE 'aws s3(api)? (ls|list-objects)[^|]*code/'; then
  class=aws_deploy_verify
  msg="comp-tool on the HUD: raw \`aws s3 ls\` of a code/ prefix = deploy-verify. \`comp-pipescript deployed [<script>|--firm bd|inf|cot|mdpf]\` = MATCH/STALE/MISSING per script WITH bucket-attribution + firm-separation -- catches a stranded/half-landed deploy a raw ls won't frame. Run before any gold/silver run. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE 'aws s3(api)? (ls|list-objects)[^|]*(^|/)(gold|platinum|silver|json)/'; then
  class=aws_freshness
  msg="comp-tool on the HUD: raw \`aws s3 ls\` + timestamp for artifact freshness. \`comp-freshness <artifact>\` = EXISTS/FRESH/SCALED/NOT-FROZEN (the validate-on-served check), not just a listing + mtime eyeball. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE 'aws dynamodb (scan|get-item|query|describe-table|list-tables)'; then
  class=aws_dynamodb
  msg="comp-tool on the HUD: raw \`aws dynamodb\` inspection. \`comp-freshness <table> --ddb\` = firm-config drift framing; \`comp-aws\` = the table's edges/consumers. Higher-context than a raw scan. (advisory -- your command still runs.)"
elif [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE '(grep|rg|findstr)([^|;]*)(infra/aws/|\.tf([^A-Za-z0-9]|$))'; then
  class=infra_grep
  msg="comp-tool on the HUD: grepping infra/.tf. \`comp-aws\` = the resource edges/blast-radius (relationship-aware, not text -- the destructive-op pre-gate basis); \`comp-iam\` = the perms; \`comp-routes\` = the serving path. Repo-scoped + edge-aware vs a blind .tf grep. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE '(^|[^A-Za-z0-9_])(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?([^A-Za-z0-9_]|$)'; then
  _id=$(printf '%s' "$query" | grep -oE '(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?' | head -1)
  class=script_id
  msg="comp-tool on the HUD: searching for gold-script id '${_id}'. \`comp-pipescript io ${_id}\` = its inputs/outputs + upstream writers + downstream consumers (or \`feeds\`/\`consumers\` for one direction); \`pipescript --resource ${_id}\` = its whole named thread. Deterministic, no tree-grep. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 's3://opal-|opal-data-[A-Za-z0-9_]+|(^|/)(gold|platinum|silver)/|\.parquet([^A-Za-z0-9]|$)'; then
  class=s3_artifact
  msg="comp-tool on the HUD: searching for an S3 artifact/key. \`pipescript --resource <substr>\` = which named thread + producer owns it; \`comp-pipescript io <script>\` = a gold script's reads/writes incl. portal consumers. Deterministic. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'useQuery|useMutation|useInfiniteQuery|queryKey'; then
  class=react_query
  msg="comp-tool on the HUD: searching React Query keys/hooks. \`comp-cache collisions\` = shared/colliding query keys across components (the stale-cache + cross-cohort key-bleed class) -- deterministic vs grepping useQuery across .tsx. (advisory -- your search still runs.)"
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

# --- comp-which FALLBACK (Andrew-direct 2026-06-18: DEFAULT TO THE RAIL) ------------------------
# A SEARCH that matched no specific class still gets the ROUTER on the HUD: comp-which maps a
# plain-English question to the canonical comp-call, so an UNCLASSIFIED grep is no longer a silent
# bypass -- the agent checks the rail first, defers to raw grep only if comp-which says no tool fits.
# Fires on SEARCH intent only (Grep/Glob, or a Bash grep/rg/find family) -- a non-search Bash
# (ls/git/npm/operational) is NOT a search, no nudge. Throttled to RECUR every COMPWHICH_EVERY-th
# unclassified search (persistent rail-pressure WITHOUT per-grep banner-blindness; tunable below).
if [ -z "$class" ]; then
  _search=0
  case "$tool" in Grep|Glob) _search=1 ;; esac
  if [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE '(^|[^-A-Za-z])(grep|rg|egrep|fgrep|findstr|ack|ag|find)([^A-Za-z]|$)'; then _search=1; fi
  [ "$_search" = 0 ] && exit 0
  class=comp_which
  msg="comp-tool on the HUD: comp-which is the RAIL -- use it FIRST. \`comp-which \"<your question in plain English>\"\` maps any search to the canonical comp-call (we built ~30 comp-tools across graph/IAM/routes/freshness/pipeline/cache -- you don't memorize them). RULE (Andrew-direct 2026-06-18): comp-which/comp-tool is the DEFAULT for every search + inspection; raw grep/aws is the EXCEPTION, used ONLY when comp-which confirms no tool fits the exact use. (native-tool nudge; raw aws/grep-in-Bash is being hard-gated to the rail.)"
fi
[ -z "$class" ] && exit 0

# === TO-4 GATE (NFRA_COMPRAIL: gated-not-banned; hardness-order ramp; announce-then-enforce -- COO
#     broadcast 2026-06-22; CLAUDE.md Rule 21) =====================================================
# HARD-DENY surfaces (Bash only): raw-aws-INSPECTION (tier 1) + infra/.tf grep (tier 2a). Everything
# else -- native Grep/Glob tools, the other Bash search classes, broad repo-file-grep, the comp-which
# fallback -- stays ADVISORY (the existing additionalContext nudge below). "native escape is fine"
# (Andrew 2026-06-22): native Grep/Glob NEVER deny. OVERRIDE = a trailing `# rail-checked: <why>` on
# the Bash command -> allow + audit (no deny, no nudge). FAIL-SAFE: deny only on the enumerated tiers;
# any doubt falls through to advisory -- never a spurious wall. /freeform already stood the whole rail
# down above (exits before here). RAMP NOTE: broad repo-file-grep (grep -r / rg over repo source) is
# STAGED as nudge -- it is the friction-sensitive tier (PRD §6 "native/broad LAST"), enables only after
# its dedicated FP-test pass; today it routes to the comp-which advisory nudge, not a deny.
# GOVERNING PRINCIPLE (Andrew-direct 2026-06-23): comp-tools mandatory IFF the target has an
# ASSOCIATED GRAPH. DENY fires ONLY on graph-backed classes (aws/infra here; the ramp adds more
# graph-backed tiers). The unclassified comp_which catch-all = the NO-GRAPH bucket (new project /
# web search / local FS / self-contained library not in any comp-graph) -> NEVER deny it; off-the-
# rails is correct there, not a wall. A gate class exists IFF a graph backs it.
_gate=0
if [ "$tool" = Bash ]; then
  case "$class" in
    aws_iam_inspect|aws_route|aws_deploy_verify|aws_freshness|aws_dynamodb) _gate=1 ;;  # tier 1: raw-aws-INSPECTION
    infra_grep) _gate=1 ;;                                                              # tier 2a: infra/.tf grep
  esac
fi
if [ "$_gate" = 1 ]; then
  RAIL_LOG="$WS/org/mcp/comp-which-rail.log"
  _ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')"
  _q80="$(printf '%s' "$query" | head -c 100)"
  # OVERRIDE: an explicit, auditable `# rail-checked: <why>` marker -> authorized one-off; allow.
  if printf '%s' "$query" | grep -qE '#[[:space:]]*rail-checked:'; then
    echo "$_ts  RUN-OVERRIDE  tool=$tool  class=$class  q=$_q80" >> "$RAIL_LOG" 2>/dev/null || true
    exit 0
  fi
  echo "$_ts  DENY  tool=$tool  class=$class  q=$_q80" >> "$RAIL_LOG" 2>/dev/null || true
  # deny reason = the class's comp-tool guidance (strip the advisory tail) + the gate + the override.
  _reason="$(printf '%s' "$msg" | sed -E 's/[[:space:]]*\(advisory -- your [a-z]+ still runs\.\)//')"
  _reason="${_reason} -- GATED per CLAUDE.md Rule 21 (comp-which-first). Run the comp-tool above instead. If NO comp-tool truly fits this exact search, re-run the command with a trailing '# rail-checked: <why no comp-tool fits>' marker (auditable, logged). For a time-boxed speed push, /freeform stands the whole rail down."
  _enc=$(printf '%s' "$_reason" | "$JQ" -Rs . 2>/dev/null) || exit 0
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":%s}}' "$_enc"
  exit 0
fi

# log every hit (CVO's before/after measurement), then advise per the class's throttle
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  HUD-HIT  tool=$tool  class=$class  q=$(printf '%s' "$query" | head -c 80)" >> "$WS/org/mcp/comp-tool-hud.log" 2>/dev/null || true
if [ -n "$sid" ]; then
  d="$WS/org/mcp/sessions"; mkdir -p "$d" 2>/dev/null || true
  if [ "$class" = comp_which ]; then
    # EVERY-TIME mandate (Andrew-direct: hard-nudge the native tools). COMPWHICH_EVERY=1 = fire on
    # every unclassified native search; raise it later if CVO hud-telemetry shows banner-blindness.
    COMPWHICH_EVERY=1
    cf="$d/${sid}.compwhich.count"
    n=$(cat "$cf" 2>/dev/null || echo 0); n=$(( n + 1 )); printf '%s' "$n" > "$cf" 2>/dev/null || true
    [ $(( (n - 1) % COMPWHICH_EVERY )) -ne 0 ] && exit 0
  else
    m="$d/${sid}.comphud.${class}.seen"
    [ -f "$m" ] && exit 0          # specific class: advise ONCE per class per session
    : > "$m" 2>/dev/null || true
  fi
fi
enc=$(printf '%s' "$msg" | "$JQ" -Rs . 2>/dev/null) || exit 0
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":%s}}' "$enc"
exit 0
