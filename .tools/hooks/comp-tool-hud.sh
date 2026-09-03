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
_orig_query="$query"   # the T1 rail may narrow $query to one SEGMENT for classification; the override marker + log rows read the ORIGINAL

WS="$(cd "$SCRIPT_DIR/../.." 2>/dev/null && pwd)" || WS="."
RAIL_LOG="$WS/org/mcp/comp-which-rail.log"
_q80() { printf '%s' "$_orig_query" | tr '\n\r' '  ' | head -c 100; }

# emit_deny -- the ONE deny path (shared by the T1 search rail and the aws/infra tiers). Honors the
# `# rail-checked: <why>` override (allow + audit) and writes the DENY row. Uses $class/$msg/$query.
emit_deny() {
  local _ts; _ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')"
  if printf '%s' "$_orig_query" | grep -qE '#[[:space:]]*rail-checked:'; then
    local _why; _why="$(printf '%s' "$_orig_query" | sed -E 's/.*#[[:space:]]*rail-checked:[[:space:]]*//' | tr '\n' ' ' | head -c 200)"
    echo "$_ts  RUN-OVERRIDE  tool=$tool  class=$class  reason=$_why  q=$(_q80)" >> "$RAIL_LOG" 2>/dev/null || true
    exit 0
  fi
  echo "$_ts  DENY  tool=$tool  class=$class  q=$(_q80)" >> "$RAIL_LOG" 2>/dev/null || true
  local _reason; _reason="$(printf '%s' "$msg" | sed -E 's/[[:space:]]*\(advisory -- your [a-z]+ still runs\.\)//')"
  _reason="${_reason} -- GATED per CLAUDE.md Rule 21 (comp-which-first). Run the comp-tool above instead. If NO comp-tool truly fits this exact search, re-run the command with a trailing '# rail-checked: <why no comp-tool fits>' marker (auditable, logged). For a time-boxed speed push, /freeform stands the whole rail down."
  local _enc; _enc=$(printf '%s' "$_reason" | "$JQ" -Rs . 2>/dev/null) || exit 0
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":%s}}' "$_enc"
  exit 0
}

# === CENSUS-FILTERED -- a census denominator cannot be post-filtered away (LD-0526 / BR-2) ===
# Classify before the generic "already a comp-tool" escape below. The classifier operates on
# shell segments and masks quoted bodies before looking for structural pipes, so a regex alternation
# inside quotes is not mistaken for a pipeline. Every census pipeline is measured, including the
# allowed forms; no historical telemetry carried the receiver at all.
if [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE 'comp-(read|find|surprise|schedule)'; then
  _census_masked="$(printf '%s' "$query" | tr '\n\r' ';;' | sed -E "s/'[^']*'/'Q'/g; s/\"[^\"]*\"/\"Q\"/g")"
  _census_segs="$(printf '%s' "$_census_masked" | sed -E 's/&&|\|\||;/\n/g')"
  while IFS= read -r _cs; do
    _cs="$(printf '%s' "$_cs" | sed -E 's/^[[:space:]]*//; s/^(([A-Za-z_][A-Za-z0-9_]*=[^[:space:]]*|env|sudo|time|nice)[[:space:]]+)*//; s/#.*$//')"
    [ -z "$_cs" ] && continue
    _cfirst="$(printf '%s' "$_cs" | sed -E 's/\|.*$//')"
    _clead="$(printf '%s' "$_cfirst" | awk '{print $1}')"
    _clead_base="${_clead##*/}"
    if printf '%s' "$_clead_base" | grep -qE '^(python|python3|py|py\.exe)$'; then
      _clead="$(printf '%s' "$_cfirst" | awk '{print $2}')"
      _clead_base="${_clead##*/}"
    fi
    case "$_clead_base" in
      comp-read|comp-find|comp-surprise|comp-schedule) : ;;
      *) continue ;;
    esac
    printf '%s' "$_cs" | grep -q '|' || continue
    _cstatus=ALLOW
    if printf '%s' "$_cs" | grep -qE '\|[[:space:]]*(grep|egrep|fgrep|rg|head|tail|cut|awk|sed|wc)([[:space:]]|$)' \
       && ! printf '%s' "$_orig_query" | grep -qE 'ENUMERATE|DENOMINATOR' \
       && ! printf '%s' "$_orig_query" | grep -qE '#[[:space:]]*rail-checked:'; then
      _cstatus=DENY
    fi
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  CENSUS-PIPE  $_cstatus  q=$(printf '%s' "$_orig_query" | tr '\n\r\t' '   ' | head -c 80)" >> "$RAIL_LOG" 2>/dev/null || true
    if [ "$_cstatus" = DENY ]; then
      class=CENSUS-FILTERED
      msg="comp-tool on the HUD: a census command ($_clead_base) pipes into a receiver that can erase its denominator. Use the tool's own --limit, --page, --width, --band, or --json flags. Summary-aware filters containing ENUMERATE or DENOMINATOR are allowed. If no native flag fits, use '# rail-checked: <why>'."
      emit_deny
    elif printf '%s' "$_orig_query" | grep -qE '#[[:space:]]*rail-checked:' \
         && printf '%s' "$_cs" | grep -qE '\|[[:space:]]*(grep|egrep|fgrep|rg|head|tail|cut|awk|sed|wc)([[:space:]]|$)'; then
      class=CENSUS-FILTERED
      msg="census receiver allowed by audited rail-checked escape"
      emit_deny
    fi
  done <<EOF
$_census_segs
EOF
fi

# === T1 -- THE PER-SEGMENT SEARCH RAIL (Andrew-direct 2026-08-28, "All approved" on the /open-calls
# cards; audit org/tier1_exec/1.0.0_SA_CTO/deliverables/COMPRAIL_GREP_GATE_AUDIT_20260828.md) ======
# The 07-08 LEADING-VERB gate exited on any operational lead verb unless a later segment was a
# grep-family word, and the old Gate-1 denied only recursive greps over an ESTATE path list with no
# `|` anywhere in the command. Measured 2026-08-28 (24 shapes fed to this hook): `grep -rn foo .`,
# `grep -rn foo org/`, `grep -rn foo portal/src | head`, `cd X && grep ...`, `find org -name`, and
# `cd X && aws iam get-role` ALL passed SILENT -- the rail stood only where the command already said
# infra/aws, .tf or portal/src. RULE NOW: the command is split into SEGMENTS (&&, ||, ;, newline);
# each segment's FIRST pipeline stage is its command.
#   - lead in {grep rg egrep fgrep findstr ack ag} that is RECURSIVE or DIRECTORY-scoped, or `find`
#     with anything -> a REPO SEARCH -> DENY (marker-gated: org/mcp/comprail-gate1.enforce is the
#     fabric kill switch), routed to comp-find. Any path. Any lead verb before it. A `|` after it
#     does not matter (that is post-processing OUR search, still a search).
#   - a grep-family lead over ONE FILE (no -r, last arg is an existing file or looks like one) stays
#     free (T2, deferred a week on Andrew's word) and is LOGGED as ALLOW-SEARCH shape=single-file --
#     the denominator the 08-28 audit found missing. (An infra/.tf single file still hits the
#     pre-existing infra_grep tier below -- nothing loosened.)
#   - grep as a pipe RECEIVER (`cmd | grep`) is post-processing, free, LOGGED shape=pipe-receiver.
#   - an `aws` lead matching the INSPECTION regexes is classified on ITS OWN SEGMENT below, so the
#     lead-verb hole closes with no second mechanism.
#   - native Grep/Glob tools: unchanged (nudge-and-proceed, Andrew 06-22 + re-affirmed 08-28).
# COST: one tr/sed split per Bash call (ms). NON-APPLICATION: pipe-receiver grep, single-file grep,
# `# rail-checked:`, /freeform, non-search Bash, the native tools.
_search_seg=""; _search_shape=""; _aws_seg=""; _pipe_receiver=0
# FAST PATH (measured 2026-08-28: the segment loop costs ~0.7s on `git status` under MSYS, where every
# sed/awk/grep is a ~100ms process): a command with NO search-family / aws token anywhere pays ONE grep.
if [ "$tool" = Bash ] && ! printf '%s' "$query" | grep -qE '(^|[^A-Za-z0-9_-])(grep|rg|egrep|fgrep|findstr|ack|ag|find|aws)([^A-Za-z0-9_-]|$)'; then
  _lead="$(printf '%s' "$query" | sed -E 's/^[[:space:]]*//' | grep -oE '^[A-Za-z0-9_./-]+' | head -1)"
  case "$_lead" in
    python|python3|pip|pip3|npm|npx|node|bun|deno|terraform|tofu|git|pytest|make|docker|bash|sh|zsh|\
    cargo|go|mvn|gradle|ruby|perl|java|dotnet|safe-*|comp-to|echo|ls|cd|mkdir|rm|cp|mv|touch|chmod|export) exit 0 ;;
  esac
  _search_shape=none
fi
if [ "$tool" = Bash ] && [ "$_search_shape" != none ]; then
  if printf '%s' "$query" | grep -qE '\|[[:space:]]*(grep|rg|egrep|fgrep|findstr|ack|ag)([[:space:]]|$)'; then _pipe_receiver=1; fi
  # QUOTED STRINGS ARE OPAQUE. A `|`, `;` or `&&` INSIDE a quoted pattern (`grep -n 'a\|b' f.py`) is
  # not a pipe or a separator; masking quoted bodies to Q before the split keeps the first stage and
  # the segment boundaries honest. Measured 2026-08-28 on this seat: the unmasked splitter cut
  # `grep -n '^def \|^X' .tools/_comprail.py | head` at the pattern's `\|` and DENIED a single-file
  # grep as "directory" -- a false deny the FP test now carries.
  _masked="$(printf '%s' "$query" | tr '\n\r' ';;' | sed -E "s/'[^']*'/'Q'/g; s/\"[^\"]*\"/\"Q\"/g")"
  _segs="$(printf '%s' "$_masked" | sed -E 's/&&|\|\||;/\n/g')"
  while IFS= read -r _s; do
    _s="$(printf '%s' "$_s" | sed -E 's/^[[:space:]]*//; s/^(([A-Za-z_][A-Za-z0-9_]*=[^[:space:]]*|env|sudo|time|nice)[[:space:]]+)*//; s/#.*$//')"
    [ -z "$_s" ] && continue
    _first="$(printf '%s' "$_s" | sed -E 's/\|.*$//')"
    _lead="$(printf '%s' "$_first" | grep -oE '^[A-Za-z0-9_./-]+' | head -1)"
    _lead_base="${_lead##*/}"
    case "$_lead_base" in
      grep|egrep|fgrep)
        if printf '%s' "$_first" | grep -qE '(^|[[:space:]])-[A-Za-z]*[rR][A-Za-z]*([[:space:]]|$)|--(dereference-)?recursive'; then _search_seg="$_s"; _search_shape=recursive; break; fi
        _last="$(printf '%s' "$_first" | awk '{for(i=NF;i>2;i--) if ($i !~ /^-/) {print $i; exit}}' | tr -d "'\"")"
        if [ -z "$_last" ]; then _search_shape=stdin; continue; fi                  # `grep pat` reads stdin: not a repo search
        if [ -d "$WS/$_last" ] || [ -d "$_last" ] || [ "$_last" = "." ] || printf '%s' "$_last" | grep -qE '[*?]|/$'; then _search_seg="$_s"; _search_shape=directory; break; fi
        _search_shape=single-file ;;
      rg|ack|ag|findstr)
        _last="$(printf '%s' "$_first" | awk '{for(i=NF;i>2;i--) if ($i !~ /^-/) {print $i; exit}}' | tr -d "'\"")"
        if [ -n "$_last" ] && { [ -f "$WS/$_last" ] || [ -f "$_last" ]; } && ! printf '%s' "$_first" | grep -qE '(^|[[:space:]])(-r|/s)([[:space:]]|$)'; then _search_shape=single-file; else _search_seg="$_s"; _search_shape=recursive; break; fi ;;
      find) _search_seg="$_s"; _search_shape=find; break ;;
      aws) [ -z "$_aws_seg" ] && _aws_seg="$_first" ;;
    esac
  done <<EOF
$_segs
EOF
  if [ -n "$_search_seg" ] && [ -f "$WS/org/mcp/comprail-gate1.enforce" ]; then
    class=repo_search
    msg="comp-tool on the HUD: a raw repo search in Bash (${_search_shape}: $(printf '%s' "$_search_seg" | head -c 80)). The rail is comp-find: \`comp-find '<pattern>' [pathspec]\` = content (graded bands, PRINTED denominator, gitignored content included by default); \`comp-find --name '<glob>' [pathspec]\` = files; \`comp-which \"<question>\"\` = the router. A \`cmd | grep\` pipe RECEIVER stays free."
    emit_deny
  fi
  if [ -n "$_search_seg" ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  ALLOW-SEARCH  tool=Bash  shape=${_search_shape}-marker-off  q=$(_q80)" >> "$RAIL_LOG" 2>/dev/null || true
  elif [ "$_search_shape" = single-file ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  ALLOW-SEARCH  tool=Bash  shape=single-file  q=$(_q80)" >> "$RAIL_LOG" 2>/dev/null || true
  elif [ "$_pipe_receiver" = 1 ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  ALLOW-SEARCH  tool=Bash  shape=pipe-receiver  q=$(_q80)" >> "$RAIL_LOG" 2>/dev/null || true
  fi
  # An aws INSPECTION segment is classified on its own text (closes `cd X && aws iam ...`).
  if [ -n "$_aws_seg" ]; then
    query="$_aws_seg"
  elif [ "$_search_shape" != single-file ] && [ "$_pipe_receiver" = 1 ]; then
    exit 0   # pure pipe-receiver command (ps | grep, git log | grep): post-processing, no nudge
  elif [ "$_search_shape" = "" ]; then
    # A search-family/aws TOKEN appeared but no segment LED with one (e.g. `echo "use grep"`,
    # `python find_dupes.py`): keep the 07-08 leading-verb quiet path for operational commands.
    _lead="$(printf '%s' "$query" | sed -E 's/^[[:space:]]*//' | grep -oE '^[A-Za-z0-9_./-]+' | head -1)"
    case "$_lead" in
      python|python3|pip|pip3|npm|npx|node|bun|deno|terraform|tofu|git|pytest|make|docker|bash|sh|zsh|\
      cargo|go|mvn|gradle|ruby|perl|java|dotnet|safe-*|comp-to|echo|ls|cd|mkdir|rm|cp|mv|touch|chmod|export) exit 0 ;;
    esac
  fi
fi

# --- NEGATIVE FILTER (CVO #3: the non-noise guarantee). Suppress when: ---
#  (a) the search is scoped to a SINGLE FILE -> grepping a file's internals, NOT a
#      relationship search (comp-pipescript io gives the I/O contract, not internals).
#  (b) the query already references a comp tool -> tool-use / archaeology, not a bypass.
#  (c) Bash OPERATIONAL aws (invoke/deploy/verify/TF) is NOT a relationship/inspection
#      query -> never nudge it (only raw-aws INSPECTION + infra-grep are comp-answerable).
if printf '%s' "$gpath" | grep -qE '\.[A-Za-z0-9]+$'; then exit 0; fi      # path ends in a file extension = single file
if printf '%s' "$query" | grep -qE 'comp-'; then exit 0; fi      # already a comp-tool reference
if [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE 'lambda invoke|s3(api)? (cp|sync|put-object|mv)|get-function-configuration|safe-apply|safe-ec2-deploy|safe-commit|terraform |update-function-code|start-build|run-task|dynamodb (put-item|update-item|delete-item|batch-write-item|get-item|scan|query|batch-get-item)'; then exit 0; fi
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
  # NFRA_TOOLBHVR.ROUTE (0.8.0_AE_CloudComp~B, 2026-07-23; AC-2 ruled by CTO~Z 211924Z).
  # THIS ONE COMMAND SHAPE CARRIES TWO INTENTS and the rail CANNOT tell them apart: an
  # `aws s3 ls` on a served-key prefix is byte-identical whether the agent is asking
  # "is it FRESH?" or "what SERVES this key / what is the path?". The rail types by COMMAND
  # SHAPE, never by QUESTION TYPE (its 14 classes contain no path/lineage class), so the
  # path-intent first-match-wins into THIS freshness class and gets answered with a
  # freshness tool -- the rail FIRES, the answer does not FIT, and the agent hand-greps
  # anyway (the COO MDPF served-key incident; 18 of 268 calls in this class are path-shaped,
  # and 67 `rail-checked` overrides are the measured "did not fit, going anyway" set).
  # Until TOOLSEM types the QUERY, the honest fix is to SERVE BOTH INTENTS and state plainly
  # which one has NO COVERAGE -- routing path-intent at an undiscriminating tool would be
  # strictly worse than the grep (it reads authoritative and cannot fail).
  msg="comp-tool on the HUD: raw \`aws s3 ls\` on a served/artifact prefix answers TWO different questions -- say which you are asking. (1) IS IT FRESH -> \`comp-freshness <artifact>\` = EXISTS/FRESH/SCALED/NOT-FROZEN (the validate-on-served check), not a listing + mtime eyeball. (2) WHAT SERVES THIS KEY / the URL->S3 path -> \`comp-routes trace --json <url>\` RESOLVES THIS (@a119bc34c). USE --json AND KEY ON THE \`outcome\` ENUM -- it is NOT an oracle and the enum is the only safe discriminator: RESOLVED | UNRESOLVED_NO_RULE (the static table does not COVER that prefix -- NOT proof no key exists) | CATCHALL_DEFAULT (a DEFAULT, NOT a resolution -- returned for ANY unmodelled path) | NO_MATCH. TREAT ANYTHING != RESOLVED AS NOT-A-RESOLUTION: on a catch-all \`s3_key\` MAY BE NON-NULL while outcome is CATCHALL_DEFAULT, so keying on 'did I get a key?' reads a default as an answer. AND KNOW THE BOUNDARY OF RESOLVED ITSELF: it means THE MODELLED TABLE PRODUCED A KEY -- NOT that the router will serve it. The table is TRANSCRIBED from the routers, so an auth/PII branch can 401 a path that trace resolves S3-direct (live case: pseudonymized platinum summary paths). RESOLVED is a claim about the MODEL, never a grant of access -- never infer servability or authorization from it. AND \`s3_uri\`'s BUCKET CAN BE THE WRONG FIRM'S: for scoped advisor-intelligence paths the router picks the origin bucket PER FIRM AT REQUEST TIME (bd|inf|cot), while trace reports ONE fixed bucket -- never carry that bucket into a firm-separation judgement (CLAUDE.md NEVER #2). The payload carries its own \`disclosure\`, \`plane\`, \`vintage\` and \`blind_spots\` FROM comp-routes' output contract -- read them there rather than from this nudge (one source; this message deliberately does not restate them). NOTE \`blind_spots\` is a DECLARED STRUCTURAL LIMIT LIST, not a health signal -- it is non-empty on a perfectly good RESOLVED answer and means 'what this answer does not cover'. Treat a bare ls as evidence of PRESENCE only, never of the serving path. (3) WHAT IS ACTUALLY SERVED RIGHT NOW -> LIVE S3 IS the authority (NOT comp-estate's resolver snapshot (names-only; keys re-derive live -- read its header vintage), NOT kuzu for a post-build key); \`comp-freshness\` reads live S3 and frames age correctly, which a raw ls does not -- its LastModified renders in LOCAL time on this host, a known false-staleness trap. If you genuinely need the raw listing itself, that is a legitimate \`# rail-checked:\` case. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE 'aws dynamodb (describe-table|list-tables)'; then
  class=aws_dynamodb
  msg="comp-tool on the HUD: \`aws dynamodb describe-table/list-tables\`. For the table AS A GRAPH NODE: \`comp-aws\` = its edges/consumers; \`comp-freshness <table> --ddb\` = firm-config drift. (Row DATA-ACCESS -- get-item/scan/query -- is operational/no-graph, off the rail.) (advisory -- your command still runs.)"
elif [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE '(grep|rg|findstr)([^|;]*)(infra/aws/|\.tf([^A-Za-z0-9]|$))'; then
  class=infra_grep
  # NFRA_TOOLBHVR.ROUTE 2026-07-23: the old text promised "`comp-routes` = the serving path".
  # That claim is REFUTED for the URL->S3-key hop (~D positive control: `comp-routes trace`
  # falls through to the catch-all CF behavior and returns byte-identical output for a path
  # WITH a known rewrite rule vs one without). comp-routes IS trustworthy as a CONFIG-DERIVED
  # LISTING (behaviors/origins/rewrites/api-routes) -- so the nudge now promises exactly that
  # and no more. Promising a resolution the tool cannot make is how a nudge trains bypass.
  msg="comp-tool on the HUD: grepping infra/.tf. \`comp-aws\` = the resource edges/blast-radius (relationship-aware, not text -- the destructive-op pre-gate basis); \`comp-iam\` = the perms; \`comp-routes behaviors|origins|rewrites|api-routes\` = the CF/edge CONFIG listing (NOT a URL->S3-key resolution -- \`comp-routes trace\` is undiscriminating for the static-rewrite class). Repo-scoped + edge-aware vs a blind .tf grep. (advisory -- your command still runs.)"
elif printf '%s' "$query" | grep -qE '(^|[^A-Za-z0-9_])(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?([^A-Za-z0-9_]|$)'; then
  _id=$(printf '%s' "$query" | grep -oE '(INF_)?[A-DIS]_-?[0-9]{1,2}[a-z]?' | head -1)
  class=script_id
  msg="comp-tool on the HUD: searching for gold-script id '${_id}'. \`comp-pipescript io ${_id}\` = its inputs/outputs + upstream writers + downstream consumers (or \`feeds\`/\`consumers\` for one direction); \`comp-estate --resource ${_id}\` = its whole named thread. Deterministic, no tree-grep. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 's3://opal-|opal-data-[A-Za-z0-9_]+|(^|/)(gold|platinum|silver)/|\.parquet([^A-Za-z0-9]|$)'; then
  class=s3_artifact
  msg="comp-tool on the HUD: searching for an S3 artifact/key. \`comp-estate --resource <substr>\` = which named thread + producer owns it; \`comp-pipescript io <script>\` = a gold script's reads/writes incl. portal consumers. Deterministic. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'useQuery|useMutation|useInfiniteQuery|queryKey'; then
  class=react_query
  msg="comp-tool on the HUD: searching React Query keys/hooks. \`comp-cache collisions\` = shared/colliding query keys across components (the stale-cache + cross-cohort key-bleed class) -- deterministic vs grepping useQuery across .tsx. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'portal/src/|\.tsx([^A-Za-z0-9]|$)|/api/(scoped|general|private|public)/|getAdvisor[A-Za-z]*'; then
  class=portal
  msg="comp-tool on the HUD: searching a portal component/route. \`comp-transform schema-check <Component>\` = its data-prop type contract (MISSING = runtime undefined); \`comp-routes behaviors\` = the serving/CF path (4xx/HTML masking). \`comp-estate <thread>\` shows the backend that feeds it. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'opal-[a-z][a-z-]+|(inf|bd)-[a-z-]+-(trigger|runner|publisher|daily)|yang-generate-[a-z-]+|causality-[a-z-]+'; then
  class=lambda
  msg="comp-tool on the HUD: searching for a lambda. \`comp-iam service <fn>\` = its IAM/perms; \`comp-aws\` = its edges/blast; \`comp-estate --resource <fn>\` = which named thread it's in. (advisory -- your search still runs.)"
elif printf '%s' "$query" | grep -qE 'iam[_-]?role|:role/|aws_iam_policy'; then
  class=iam_role
  msg="comp-tool on the HUD: searching for an IAM role/policy. \`comp-iam service <lambda>\` / \`comp-iam gaps\` = perms before deploy (mind: a Principal:* on Effect=Deny is a GUARDRAIL, not a public grant). (advisory -- your search still runs.)"
elif [ "$tool" = Bash ] && printf '%s' "$query" | grep -qE 'find[^|]*-(mtime|mmin|newer|atime)|git log[^|]*--name-only'; then
  # estate write-freshness / hygiene intent (NFRA_TOOLHUD ext 2026-06-25). Conservative: only
  # time-based `find` + `git log --name-only` (clear staleness/change-history signals). Bare
  # `git status` / `ls -t` deliberately NOT matched -- too operationally common (FP-noise).
  class=object_heat
  msg="comp-tool on the HUD: time-based file-staleness search. \`comp-heat freshness [path]\` = per-path hot/warm/cold + ranked COLD SUBTREES (archive candidates) from git WRITE-history (not just fs mtime, + the locality signal a flat find misses); \`comp-heat drift\` = writes-not-in-a-commit. ADVISORY-ONLY estate hygiene; distinct from comp-freshness (data-pipeline). (advisory -- your command still runs.)"
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
# down above (exits before here). RAMP NOTE (CORRECTED 2026-07-19): the ESTATE-scoped subset of broad
# repo-file-grep IS ARMED + DENIES -- Gate-1 (marker-gated at :207-221 on org/mcp/comprail-gate1.enforce,
# COO-flipped 06-26). NON-estate broad-grep + compound-shape commands stay advisory nudge. This note
# previously read "STAGED as nudge ... not a deny" for ALL broad-grep -- STALE SINCE 06-26; it misled a
# CTO law edit + a CVO verify (2026-07-19). THE MARKER FILE is the arming state, NOT this comment.
# GOVERNING PRINCIPLE (Andrew-direct 2026-06-23): comp-tools mandatory IFF the target has an
# ASSOCIATED GRAPH. DENY fires ONLY on graph-backed classes (aws/infra here; the ramp adds more
# graph-backed tiers). The unclassified comp_which catch-all = the NO-GRAPH bucket (new project /
# web search / local FS / self-contained library not in any comp-graph) -> NEVER deny it; off-the-
# rails is correct there, not a wall. A gate class exists IFF a graph backs it.
_gate=0
if [ "$tool" = Bash ]; then
  case "$class" in
    aws_iam_inspect|aws_route|aws_deploy_verify|aws_freshness) _gate=1 ;;  # tier 1: raw-aws-INSPECTION (DDB data-plane reads = operational/no-graph, exempted above; describe/list = nudge-not-deny -- operational-vs-structural split, CVO TO-5 2026-06-23)
    infra_grep) _gate=1 ;;                                                              # tier 2a: infra/.tf grep
  esac
fi
# GATE-1 (LD-0207 LEG-A, option-a conservative scope, CTO 2026-06-25) -- estate-scoped broad-repo-grep
# DENY, enforced ONLY when the marker org/mcp/comprail-gate1.enforce is present (announce-then-enforce:
# ABSENT = advisory default = ZERO behavior change; COO flips it ON post-announce+grace via LEG-C). Scope:
# the comp_which catch-all (UNCLASSIFIED broad search -- the specific classes keep their own advisory tier)
# that is a STANDALONE recursive repo search (grep -r/-R / rg / find -- NOT a pipe-grep) over an ESTATE/
# graph-backed path. No-graph (new project / non-estate lib [exited above via the deck_generation carve-out]
# / generic / pathless) stays advisory, NEVER denied (governing principle + AC#5 over-gate guard). The
# #rail-checked override + /freeform are honored by the shared deny path below. FP-test: comprail-gate1-fptest.sh.
# SCOPE PRECISION (exercised 2026-07-19, ~Z): Gate-1 fires ONLY on class=comp_which, so EARLIER classifiers
# SHADOW two estate sub-shapes to ADVISORY before Gate-1 sees them -- s3_artifact (:144, (gold|silver|platinum)/)
# captures data/*/scripts/{gold,silver}, and portal (:150) captures portal/src. So the estate regex below
# MATCHES data/*/scripts|portal/src, but the LIVE HARD-DENY reaching Gate-1 is NARROWER: {bare data/*/scripts,
# .../bronze/, infra/aws, .tf}. gold/silver-layer + portal-src get the earlier class's ADVISORY nudge (railed,
# not denied). Tightening this shadow (should they hard-deny?) = a DEFERRED rail-behavior call, not a doc fix.
# (The 06-25 Gate-1 block -- estate-path-scoped broad grep -- stood here; SUPERSEDED 2026-08-28 by the
#  per-segment T1 rail above, which denies every standalone repo search regardless of path. The
#  aws/infra tiers keep their deny via the shared emit_deny.)
if [ "$_gate" = 1 ]; then
  emit_deny
fi

# log every hit (CVO's before/after measurement), then advise per the class's throttle
#
# TELEMETRY FIDELITY (NFRA_TOOLCHECK P3, 2026-07-09): the query is flattened to ONE line and the cap
# raised 80 -> 200. The old `head -c 80` alone emitted the query RAW, so any multi-line command (the
# common Bash-tool shape: `cd <ws>\n<real command>`) split a single HUD-HIT across several log lines
# -- the entry recorded only its FIRST line (usually a bare `cd`), and the continuation lines were
# unparseable noise. Measured on the live log: of 5190 BEFORE-window Bash entries, 3514 were
# multi-line and 1517 were 80-char-truncated, leaving only 159 (3.1%) whose command was actually
# recoverable. That made this log unable to serve the "CVO before/after measurement" its own comment
# claims -- and it silently biases any false-fire count toward whatever the first line happens to be.
# tr-to-space keeps the record single-line + greppable; 200 chars captures the operative verb + the
# search segment. No consumer parses this file structurally (only freeform.sh APPENDS), so widening
# is safe.
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo '?')  HUD-HIT  tool=$tool  class=$class  q=$(printf '%s' "$query" | tr '\n\r\t' '   ' | head -c 200)" >> "$WS/org/mcp/comp-tool-hud.log" 2>/dev/null || true
if [ -n "$sid" ]; then
  d="$WS/org/mcp/sessions"; mkdir -p "$d" 2>/dev/null || true
  # NFRA_TOOLCHECK P3 req#3a (2026-07-08, INVERTED): the LEAST-specific class (comp_which, the
  # catch-all) used to fire on EVERY unclassified search -- backwards, since it's the class most
  # prone to banner-blindness. PRECISE classes (portal/lambda/iam/...) used to fire ONCE-EVER per
  # session -- also backwards, since a long session legitimately re-hits the same class against a
  # different target and then goes permanently silent for the rest of the session. Swap the two
  # mechanisms: comp_which now throttles HARD (once per session -- the old precise-class behavior);
  # precise classes now RECUR every CLASS_EVERY-th hit (the old comp_which mechanism, reused), so
  # they stay salient without going silent for the remainder of a long session.
  if [ "$class" = comp_which ]; then
    m="$d/${sid}.comphud.${class}.seen"
    [ -f "$m" ] && exit 0
    : > "$m" 2>/dev/null || true
  else
    CLASS_EVERY=5
    cf="$d/${sid}.comphud.${class}.count"
    n=$(cat "$cf" 2>/dev/null || echo 0); n=$(( n + 1 )); printf '%s' "$n" > "$cf" 2>/dev/null || true
    [ $(( (n - 1) % CLASS_EVERY )) -ne 0 ] && exit 0
  fi
fi

# NFRA_TOOLCHECK P3 req#3d (2026-07-08): the catch-all used to fire static "a tool exists, go use
# comp-which" boilerplate regardless of whether comp-which would find anything for THIS query -- a
# standing banner, easy to tune out. ACTUALLY run comp-which (via ~A's --route-only guard, so a
# preview can never side-effect a real grep/glob subprocess) and surface the EXACT tool + call it
# picked; if comp-which itself would fall back to grep/glob (no rich tool fits), suppress the nudge
# entirely instead of repeating the generic banner -- a specific nudge is far less ignorable than a
# standing one, and nudging toward nothing is worse than no nudge. Only touches the ADVISORY message
# for comp_which -- the DENY-gate reason above already ran off the original generic $msg, untouched
# (GATE-1 is live; not risking the security-relevant path on a live subprocess call). FAIL-SAFE: any
# python/route error leaves $msg as the original generic boilerplate (never lose the advisory).
if [ "$class" = comp_which ] && [ -z "${COMPRAIL_NO_ROUTE:-}" ] && command -v python >/dev/null 2>&1; then
  # COMPRAIL_NO_ROUTE=1 is set ONLY by comprail-gate1-fptest.sh: the deny/allow VERDICT is decided above
  # this line, and the 5s comp-which subprocess per allowed case made a 43-case run exceed 5 minutes.
  _route_out="$(timeout 5 python "$WS/.tools/comp-which" --route-only "$query" 2>/dev/null)" || _route_out=""
  if printf '%s' "$_route_out" | grep -q "NO-ROUTE"; then
    exit 0   # comp-which itself would fall back to grep/glob -- nothing specific to nudge toward
  fi
  _call_line="$(printf '%s' "$_route_out" | grep -m1 -E '^[[:space:]]*->' | sed -E 's/^[[:space:]]*->[[:space:]]*//')"
  if [ -n "$_call_line" ]; then
    msg="comp-tool on the HUD: comp-which routes this to -> ${_call_line}  (run it -- your search still proceeds). RULE (Andrew-direct 2026-06-18): comp-which/comp-tool is the DEFAULT for every search + inspection; raw grep/aws is the EXCEPTION, used ONLY when comp-which confirms no tool fits."
  fi
fi

enc=$(printf '%s' "$msg" | "$JQ" -Rs . 2>/dev/null) || exit 0
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":%s}}' "$enc"
exit 0
