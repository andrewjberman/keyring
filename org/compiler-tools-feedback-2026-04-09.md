# Compiler Tools Feedback Report
**Date:** 2026-04-09
**Author:** 1.0.0_SA_CTO
**Respondents:** 8 agents (DS~A, DS~B, DS~C, DS~D, DE~A, DE~B, DE~C, DE~D) | COMPLETE

---

## Summary

7 of 8 canvassed agents responded. The picture that emerges is a tool suite that works
well for DS cross-layer questions (pipescript io, platinum reverse, blast) but has several
silent failure modes, parser bugs, and a consistent non-adoption pattern on the DE side
driven by tool friction rather than tool irrelevance. Key findings:

- **3 confirmed bugs** that produce wrong or harmful output
- **4 high-value gaps** where no tool covers a common workflow
- **DE adoption is near-zero** this session — not because tools are useless, but because
  the workflow friction (shell round-trip, wrong working directory, already answered by grep)
  consistently loses to direct Grep/Read for targeted questions
- **DS adoption is strong** for cross-layer questions; comp-pipescript and comp-platinum
  are genuinely load-bearing

---

## Part 1 — DS Feedback

### Respondents
- 0.4.0_DS_ClientPlatform~A (ADVI_49PUSH .044, .010, .017, .040)
- 0.4.0_DS_ClientPlatform~B (ADVI_49PUSH .045 / C_08 fee efficiency)
- 0.4.0_DS_ClientPlatform~C (ADVI_49PUSH .018 auth architecture, .010 dead code)
- 0.4.0_DS_ClientPlatform~D (.023, .025, .027, .033 / D_01, D_04, D_00)

---

### DS: Tools Actually Used

| Tool | Used By | Verdict |
|------|---------|---------|
| `comp-pipescript io` | DS~A, DS~B, DS~C | Accurate and fast for S3-backed scripts; f-string keys show "?" (see Bugs) |
| `comp-pipescript consumers` | DS~A | Correct; confirmed dead code |
| `comp-routes auth-map` | DS~C | Perfectly accurate; matched actual code |
| `comp-routes behaviors` | DS~C | Authoritative; 23-behavior listing used for auth architecture doc |
| `comp-platinum reverse` | DS~A, DS~B | Fast, accurate producer trace |
| `comp-blast` | DS~B | Replaced grep sweep reliably |
| `comp-trace` | DS~A | Negative result useful; exit code bug (see below) |
| `comp-routes trace` | DS~A | Used; accuracy not disputed |
| `comp-transform trace/fields` | DS~B | Failed silently (see below) |
| None | DS~D | Bypassed in favor of S3 Python queries |

---

### DS: What Worked

**comp-pipescript io (DS~A, DS~B)**
- Instant and accurate for scripts with S3 I/O declared via s3_layout.py constants
- READS list for D_03/D_04 replaced opening a 1,500-line file
- The `FUNC` annotation on keyed partition outputs (C_08) was immediately useful
- DS~B: "One command replaced a full grep across 694 lines"

**comp-platinum reverse (DS~A, DS~B)**
- Traced mix_summary.json and timeseries_overview.json back to D_04 in one call
- Confirmed serving path and CloudFront behavior accurately
- DS~A: narrowed investigation from "somewhere in the pipeline" to "inside D_04" instantly

**comp-blast (DS~B)**
- Confirmed D_04 is the only consumer of advisor_fee_efficiency.json before schema change
- One command; zero ambiguity

**comp-pipescript consumers (DS~A)**
- Accurately listed only the 5 live artifacts consumed downstream from D_00
- advisor_rolling_flows and architect_leaderboard correctly absent (dead code confirmed)

**comp-routes auth-map and behaviors (DS~C)**
- auth-map was perfectly accurate for .018 — the EDGE JWT ONLY vs EDGE+APIGW distinction matched
  the actual code with no surprises
- behaviors: 23-behavior listing with AUTH/ROUTER annotations was the primary source for the auth
  architecture doc. DS~C: "clean, authoritative"
- DS~C overall: "comp-pipescript and comp-routes are load-bearing tools that save significant time"

**comp-trace "no nodes" result (DS~A)**
- Getting a negative result (artifact not in graph) is valid signal for dead code
- Result was correct; the issue is exit code behavior (see Bugs)

---

### DS: Bugs and Failures

**BUG 1 — comp-routes: platinum path parser reports wrong S3 prefix**
- Reporter: DS~D (ADVI_49PUSH.006 session log)
- Symptom: comp-routes displays `gold/artifacts/platinum/...` for platinum paths; Lambda@Edge
  index.mjs actually strips the `/platinum/` prefix and resolves to `/platinum/...`
- Impact: During 401 routing diagnosis, the wrong prefix made the routing appear incorrect
  when it was correct. Created unnecessary doubt and investigation overhead.
- Severity: HIGH — misleading output during incident diagnosis

**BUG 2 — comp-pipescript io: silent "none detected" for dynamic-path scripts (B_01b)**
- Reporter: DS~A
- Symptom: comp-pipescript io B_01b returned "READS: none detected, WRITES: none detected"
  B_01b actually reads from S3 (gold/timeseries/holdings_lots/*.parquet), writes to DynamoDB
  (bd-securities table), and writes an S3 watermark (gold/manifests/classify_watermark.json)
- Root cause: parser only resolves s3_layout.py constants; dynamic f-string paths and
  DynamoDB references are invisible to it
- Impact: Any agent trusting this output gets a wrong mental model. Silent failure is a trap.
- Severity: HIGH — silent wrong output (not an error, looks like a valid empty result)

**BUG 3 — comp-trace: exits non-zero for "no nodes matching"**
- Reporter: DS~A
- Symptom: comp-trace on advisor_rolling_flows exited non-zero, which cancelled the entire
  parallel tool block (other tool calls in the same message were killed)
- Impact: Forced sequential execution instead of parallel; added latency to investigation
- Fix needed: "No nodes matching query" is a valid result, not an error. Exit 0.
- Severity: MEDIUM — productivity impact on parallel workflows

**BUG 4 — comp-transform fields/trace: returns file path only for accessor-pattern components**
- Reporter: DS~B
- Symptom: comp-transform fields FeeEfficiencyPanel and comp-transform trace FeeEfficiencyPanel
  both returned only the file path. No field list, no rendered fields, no data flow.
- Root cause: FeeEfficiencyPanel uses an accessor helper `const r = (a: any) => ({...})`
  rather than direct prop destructuring. The parser appears to only recognize standard
  prop destructure or typed interface patterns; it misses all field access through the `r()` helper.
- Impact: DS~B had to read a 458-line TSX file manually. Tool provided no value.
- Severity: MEDIUM — common component pattern not handled

**BUG DS-5a — comp-pipescript io: f-string S3 keys show "?" instead of key template**
- Reporter: DS~C (independently echoed DS~A's dynamic path gap)
- Symptom: comp-pipescript io D_04 WRITES shows "?" for all platinum write targets
  e.g. "platinum/firm/dashboard.json: ? -> (terminal)" — because D_04 uses f-strings or
  string concatenation to build S3 keys rather than s3_layout.py constants
- Impact: for platinum publisher scripts, every write target shows "?" — still requires
  reading D_04 to understand actual key patterns. Significantly reduces tool value for
  the most important gold scripts (the platinum publishers)
- DS~C: "This is a significant gap — for platinum publishers, every write target shows ?"
- Fix: regex-extract the literal string parts of f-strings to produce a KEY TEMPLATE
  (e.g., "platinum/advisors/{advisor_id}/summary.json") instead of "?"
- Severity: HIGH — affects all platinum publisher scripts (D_04 and similar)

**BUG 5 — comp-platinum reverse: "CONSUMED BY: (no components found)" is misleading**
- Reporter: DS~B
- Symptom: comp-platinum reverse platinum/firm/fee_efficiency.json reported no frontend
  consumer. FeeEfficiencyPanel IS the consumer but is not found.
- Root cause: The reverse lookup doesn't follow the data through D_04's pass-through into
  the dashboard/leaderboard split logic, nor through Lambda pseudonymization paths.
- Impact: DS reading cold would conclude the artifact is unused. Creates false dead-code signal.
- Severity: MEDIUM — misleading output on real artifacts

---

### DS: Gaps (Missing Coverage)

**GAP DS-1 — No parquet schema inspection tool**
- Need: `comp-schema gold/timeseries/account_performance.parquet` → columns, dtypes, null rates,
  min/max, row count
- DS~D reported 6-8 Python round-trips per session just to understand parquet column schemas
  (account_performance, accounts_dimension, account_team, client_dimension, nna_aua_by_advisor)
- This was the single highest-friction workflow in DS~D's session
- Requested by: DS~D (primary), echoed in DS~B (output schema gap)

**GAP DS-2 — Column-level I/O in comp-pipescript (not just file-level)**
- Current: comp-pipescript io shows which files a script reads/writes
- Need: which COLUMNS from each file are consumed or produced
- Example that would have helped: immediately seeing that D_01 reads only the `architect`
  column from nna_aua_by_advisor (not multi-role) vs account_team which has all 5 roles
- Requested by: DS~D

**GAP DS-3 — DynamoDB not tracked in comp-pipescript**
- Any script touching DynamoDB (B_01b, C_07, A_01 SCD) is invisible to comp-pipescript
- When B_01b returns "none detected," it's actually doing DynamoDB writes — the empty result
  is correct for S3 but completely wrong for the script's actual output
- Fix: even a static grep for DynamoDB table references with a "DYNAMODB: table (write/read)"
  annotation would close the most common case
- Requested by: DS~A

**GAP DS-4 — Parquet column to portal field lineage**
- Current: comp-platinum traces S3 artifact -> CloudFront -> component
- Need: parquet column in gold script -> platinum JSON field -> portal rendered field
- DS~D: "comp-transform traces React component -> fetch, but nothing traces 'this column
  in C_03 account_performance -> which portal field shows it?'"
- The parquet-to-platinum segment has no coverage

**GAP DS-5a — comp-routes doesn't surface catch-all scope**
- Reporter: DS~C
- Symptom: comp-routes showed platinum paths routing through catch-all
  (`/api/scoped/advisor-intelligence/*` -> APIGateway) but didn't make it explicit that
  this catch-all also covers `platinum/*`. Required manual tracing.
- Fix: annotate catch-all behaviors with a note showing which known sub-prefixes they cover
- Requested by: DS~C

**GAP DS-5b — Authorizer context payload not visible in comp-routes**
- Reporter: DS~C
- Symptom: comp-routes shows WHICH auth layers apply but not WHAT data flows through the
  authorizer context (what keys are injected into Lambda context)
- DS~C had to read portal-authorizer/index.mjs manually for `context.allowedFirmIds`,
  `context.role`, etc.
- Proposed: comp-routes --payload flag showing the authorizer context fields

**GAP DS-5c — Cross-script gold-to-gold field type consistency**
- Reporter: DS~C
- Symptom: no tool verifies that field types/grains match between gold scripts
  (e.g., D_02 write field key format `(date, advisor_name, role)` vs what another script
  generates for the same grain)
- comp-transform covers frontend; comp-pipescript covers file I/O; neither covers
  the TYPE of data inside the files at a schema level across scripts

**GAP DS-5 — "Is this code deployed?" (S3 artifact vs repo)**
- DS~A spent time during .040 verifying whether D_02's role_breakdown code was actually
  on the EC2 runner
- DS~B independently flagged the same need (comp-pipescript deployed subcommand)
- Both want: compare s3://opal-data-bd/code/gold/{script}.py etag/size against local HEAD
- verify-local.sh exists for Lambda; gold scripts have no equivalent

---

### DS: Suggested Improvements (Existing Tools)

| Priority | Tool | Change |
|----------|------|--------|
| P0 | comp-routes | Fix platinum path parser: should show `/platinum/...` not `gold/artifacts/platinum/...` |
| P0 | comp-pipescript io | When parse yields zero I/O, emit WARN: "no constants detected -- may use dynamic paths or DynamoDB. Manual review recommended." Never silently return "none detected." |
| P0 | comp-trace | Exit 0 for "No nodes matching." Reserve non-zero for actual parse/runtime errors. |
| P1 | comp-transform | Fix accessor pattern parser: handle `const r = (a: any) => ({...})` field access |
| P1 | comp-platinum reverse | When "no components found": fallback search for S3 key path in Lambda@Edge and opal-partners-data code; list Lambda handlers that reference the key |
| P1 | comp-platinum reverse | Add function name to PRODUCER line: "D_04 :: build_firm_mix_summary()" not just "D_04" |
| P1 | comp-pipescript io | For f-string S3 keys: show key TEMPLATE using literal string parts (e.g., "platinum/advisors/{advisor_id}/summary.json") instead of "?". Affects all platinum publishers. |
| P2 | comp-pipescript | Add `output-schema` subcommand: extract top-level JSON keys from each write path in the script |
| P2 | comp-pipescript | Add `deployed` subcommand: compare S3 code artifact etag/size against local repo file; print MATCH / STALE / MISSING |
| P2 | comp-pipescript | Add `--diff` flag: show what changed in a script's I/O manifest vs its last run |
| P2 | comp-pipescript io | Flag DynamoDB table references even if not tracked in graph: "DYNAMODB: bd-securities (write)" |
| P2 | comp-routes | Annotate catch-all behaviors with known sub-prefixes they cover (e.g., "includes platinum/*") |
| P2 | comp-routes | Add `--payload` flag: show authorizer context fields injected by portal-authorizer/index.mjs |

---

## Part 2 — DE Feedback

### Respondents
- 0.4.0_DE_ClientPlatform~A (ADVI_49PUSH waves 3-11)
- 0.4.0_DE_ClientPlatform~B (ADVI_49PUSH wave 6-11)
- 0.4.0_DE_ClientPlatform~C (ADVI_49PUSH .028-.041 / DistributionTab, AdvisorsTab, AdvisorDrilldownPage)
- 0.4.0_DE_ClientPlatform~D (ADVI_49PUSH .046, .026, .034 / FeeEfficiencyPanel, GRO tile, DistributionTab)

---

### DE: Tools Actually Used

| Tool | Used By | Verdict |
|------|---------|---------|
| comp-transform schema-check | DE~A (prior sessions only) | Genuinely useful; adapter-aware, caught missing fields |
| comp-cache collisions | DE~A, DE~B (prior sessions) | Useful pre-ship for React Query key safety |
| None | DE~A, DE~B, DE~C, DE~D (this session) | All 4 bypassed tools in favor of Grep/Read |

**The DE adoption pattern:** Every DE agent was prescribed specific comp-* calls in their task
orders. None ran them. This is a consistent signal, not individual preference.

---

### DE: Why Tools Were Skipped

Three independent reasons surfaced across all 4 DE agents:

1. **Grep/Read wins for targeted questions.** DE work is predominantly frontend-only (TSX,
   TypeScript). For "is this function called anywhere?" or "what does this type look like?",
   a single grep answers in 2 seconds. comp-blast for a zero-call-site check is slower.

2. **Tool scope mismatch.** Several TOs prescribed comp-pipescript and comp-routes, which
   don't cover portal/src. DE~B: "I didn't know if comp-diff covered portal tsx or only infra."
   The CLAUDE.md directive ("use comp-* before grepping") doesn't clarify scope.

3. **Shell friction after portal build.** After running portal builds, DE agents were not
   in workspace root. comp-* tools require workspace root. The extra `cd` step plus tool
   latency makes Grep the path of least resistance.

4. **Work already done by another instance.** Several DE agents arrived at a TO that had
   already been partially or fully executed by ~B/~C/~D. Running comp-transform on committed
   work confirms wiring but doesn't tell you if the implementation is correct — still requires
   code reading. The tool adds no value in this coordination failure mode.

---

### DE: What Worked (Prior Sessions)

**comp-transform schema-check (DE~A)**
- Quickly confirmed which platinum fields were rendering vs. UNUSED without reading 2,000-line files
- Adapter-aware: caught missing field names after the platinum path switchover
- "The adapter-aware schema check caught missing field names after the platinum path switchover"

**comp-cache collisions (DE~A, DE~B)**
- Useful pre-ship for confirming no React Query key collisions
- DE~B: "genuinely useful before adding new React Query keys"

---

### DE: Bugs and Failures

**BUG DE-1 — comp-transform schema-check: flags optional fields as UNUSED (false positives)**
- Reporter: DE~C
- Symptom: schema-check flags TypeScript optional fields (`?`) absent from live S3 JSON as
  UNUSED — correct behavior pre-data-run, but confusing/noisy when the data hasn't landed yet
- Context: DE~C was wiring new .027/.033 fields (relationship_count, geo_aua_grain). The
  platinum data didn't exist yet (pre-AE re-run). schema-check would flag all new fields as dead.
- Fix needed: a `--pending` mode that treats optional-typed fields absent from live data as
  INFO (not UNUSED/WARNING) when the type marks them optional

**BUG DE-2 — comp-pii is too broad for pseudonymized data models**
- Reporter: DE~C
- Symptom: comp-pii sweeps for all PII fields including display_name in ClientSegment, which
  is intentionally pseudonymized at the DS layer. The tool cannot distinguish pseudonymized
  fields (safe) from cleartext PII (unsafe).
- Impact: comp-pii output is noise for the Distribution tab — would flag intentionally-present
  pseudonymized fields as concerns. DE~C skipped it entirely.
- Fix needed: a mode that allows declaring specific fields as "pseudonymized, not a concern"
  and only flags truly raw cleartext PII

---

### DE: Gaps (Missing Coverage)

**GAP DE-1 — Multi-instance coordination tools**
- The #1 friction source across ALL DE agents this session
- DE~A: "Which ~instance last modified a file, is work actually committed, what's the delta
  between task order status and git log?" — no tool covers this
- DE~C: Discovered duplicate enforceTop9Other implementation via git log after the fact.
  "comp-diff --live or comp-xref --since-agent" would have caught this.
- DE~D: Received messages intended for other ~instances (inbox routing noise — separate issue,
  but also a coordination signal)
- Need: comp-instance showing which ~suffix agent last touched each file (via git author);
  comp-diff --agent <serial> showing what a specific instance changed since last sync

**GAP DE-2 — Task order status vs. git commit reconciliation**
- DE~A: "cross-reference TO status XML with git log --oneline manually every time"
- No tool bridges "task order says in_progress" and "git log shows it's committed"
- Proposed as comp-gold-status (per TO: show gold scripts, committed status, runner execution)
- Would have saved DE~A ~20 min this session

**GAP DE-3 — comp-transform schema-check: TypeScript type vs. S3 JSON key mismatch**
- DE~A: PlatinumRoleBreakdown field name drift (managed_aua vs aua vs total_aua)
  comp-transform caught rendered fields but didn't flag that the TypeScript field name
  differed from the platinum JSON key
- Need: a field-name mismatch mode that cross-references TypeScript field names against
  the actual S3 JSON key names (via gold script output schema)

**GAP DE-4 — No export naming collision check**
- DE~B: no tool to check if a new function being added collides with existing exports
  in advisor-intelligence.ts
- Closest: comp-blast on the file, but that's downstream consumers, not sibling exports

---

### DE: Suggested Improvements (Existing Tools)

| Priority | Tool | Change |
|----------|------|--------|
| P0 | CLAUDE.md / docs | Clarify which comp-* tools cover portal/src (tsx) vs infra/gold only. Table: tool -> scope. Without this, DE agents will keep skipping tools that might actually apply. |
| P1 | comp-transform schema-check | Add `--pending` mode: optional-typed fields absent from live JSON are INFO, not UNUSED |
| P1 | comp-transform schema-check | Add field-name mismatch mode: cross-reference TS field names against actual S3 JSON keys |
| P1 | comp-transform schema-check | Auto-run as post-commit hook on ADVI tsx files; report UNUSED fields as warnings |
| P1 | comp-pii | Add `--mode distribution` (or `--allow-pseudonymized`): declare fields as pseudonymized; only flag cleartext PII |
| P2 | comp-blast | Add `--dry-run` flag: one line per call site, pasteable into commit messages/session logs |
| P2 | comp-cache | Flag granularity-keyed query key collisions (e.g., new_clients_by_period key vs existing keys) |
| P2 | comp-transform schema-check | When flagging UNUSED: show TypeScript type and last commit that touched the field |

---

## Cross-Role Analysis

### Adoption by Question Type

| Question Type | DS Adoption | DE Adoption | Right Tool |
|---|---|---|---|
| "What does this gold script read/write?" | HIGH | N/A | comp-pipescript io |
| "Who consumes this artifact?" | HIGH | N/A | comp-blast, comp-pipescript consumers |
| "What serves this platinum file?" | HIGH | LOW | comp-platinum reverse |
| "What fields does this component render?" | ATTEMPTED (failed) | LOW (greg faster) | comp-transform fields |
| "Are my React Query keys safe?" | N/A | MEDIUM (prior sessions) | comp-cache collisions |
| "Is this field used / missing?" | N/A | MEDIUM (prior sessions) | comp-transform schema-check |
| "Is this code actually deployed?" | NOT COVERED | NOT COVERED | gap |
| "What did another agent change?" | NOT COVERED | NOT COVERED | gap |
| "What columns does this parquet have?" | NOT COVERED | N/A | gap |

### Common Themes Across Both Roles

1. **Silent failures are worse than explicit errors.** Both DS and DE hit cases where a tool
   returned a syntactically valid but semantically wrong result (comp-pipescript "none detected",
   comp-platinum "no components found", comp-transform returning only file path). These erode
   trust and cause agents to silently stop using tools that look unreliable.

2. **Multi-instance coordination is the biggest uncovered surface.** Both DE~A and DE~C
   independently identified parallel-agent write conflicts as their #1 time sink. No comp-*
   tool touches this. It's explicitly a gap, not a misuse.

3. **"Is this deployed?" is a recurring DS need with no answer.** DS~A and DS~B independently
   asked the same question in different forms. The Lambda verify-local.sh pattern should extend
   to gold scripts.

4. **DE tools are underused because task orders prescribe them but friction wins.** The fix is
   not to mandate harder — it's to reduce the friction (auto-hooks, clearer scope docs, one-liner
   output formats that integrate with session logs).

---

## Recommended Next Actions

### P0 — Fix before next gold run (breaks things)
1. **comp-trace**: exit 0 for "no nodes matching" — currently cancels parallel tool calls
2. **comp-routes**: fix platinum path parser bug — actively misleads during incident diagnosis
3. **comp-pipescript io**: warn on empty I/O parse — silent wrong output is dangerous

### P1 — Fix before next major sprint
4. **comp-pipescript io**: f-string key templates instead of "?" — affects all platinum publishers;
   independently flagged by DS~A (dynamic paths) and DS~C (f-string writes)
5. **comp-transform**: fix accessor pattern parser (`r()` helper) — common component pattern
6. **comp-platinum reverse**: fallback to Lambda code when no frontend found; add function name to PRODUCER
7. **comp-transform schema-check**: add `--pending` mode for pre-data-run validation
8. **Docs**: table of comp-* tool scope (portal tsx vs infra vs gold) — closes DE adoption gap

### P2 — New tools, high ROI
9. **comp-schema**: parquet column schema from S3 (DS~D's #1 request; would replace 6-8 Python
   round-trips per session)
10. **comp-pipescript deployed**: S3 artifact vs repo hash check (requested by DS~A and DS~B independently)
11. **comp-instance / comp-diff --agent**: multi-instance coordination (DE~A and DE~C independently)
12. **comp-pipescript output-schema**: extract JSON keys from write paths
13. **comp-pipescript io + DynamoDB**: flag DynamoDB references even if not fully tracked
14. **comp-routes --payload**: authorizer context field map (DS~C)
15. **comp-blast**: promote to first tool listed in dead-code-removal TOs (DS~C: most natural fit,
    buried in current mandates)

---

---

## Post-Fix Validation Results (2026-04-09)

Fixes shipped in commits e50ccedf, 4670baaa, 78feb216, 45d9f918 and tested by 7 agents.

| Fix | Commits | Agents | Result |
|-----|---------|--------|--------|
| comp-trace exit 0 on "no nodes" | e50ccedf | DS~B/C/D | PASS |
| comp-pipescript io WARN on empty | e50ccedf | DS~B/C/D | PASS |
| comp-pipescript io hardcoded path display (no more `?`) | e50ccedf | DS~A | PASS |
| comp-transform schema-check NameError (resp_type) | e50ccedf | DE~B/C/D | PASS |
| comp-routes platinum path parser | pre-existing fix | DS~A/D | PASS (was already correct -- stale cache caused the .006 symptom) |
| comp-transform fields accessor pattern (prop-based) | 78feb216 | DE~A/D, DS~C/B | PASS |
| comp-transform fields JS builtin noise (.map) | 45d9f918 | — | Patched |
| comp-platinum reverse CONSUMED BY | 78feb216 | DS~C/B | PARTIAL |

### Partial: comp-platinum reverse CONSUMED BY

The direct consumer (`FeeEfficiencyPanel`) is not surfaced because it receives data
via props from a parent component, not by directly importing the endpoint function.
The directory-prefix fallback (Fallback 2) correctly finds `getPlatinumFirmDashboard ->
ClientsTab` as the aggregate source, but also returns 5 noisy sibling endpoints in the
same `platinum/firm/` directory. The right answer is present but buried.

**Root cause:** `_parse_component_bindings` only tracks components that IMPORT endpoint
functions. Prop-based consumers (panels that receive data from parents) are invisible.
Full resolution requires prop-passing tracing, which is a larger architectural change.

### Known remaining gap: `??` chain expansion in accessor detector

The accessor detector captures only the FIRST field in a `??` fallback chain.
For `r = (a) => ({ fee_bps: a.advisor_effective_bps ?? a.fee_bps_weighted ?? 0 })`,
only `advisor_effective_bps` is captured; `fee_bps_weighted` and `fee_yield_bps` are missed.
This is a known limitation — full `??` chain expansion is a P2 improvement.

### Cache staleness note (comp-routes)

DS~D's .006 session report of `gold/artifacts/platinum/...` was caused by a stale `.comp-graph`
cache, not a code bug. The platinum rewrite rule was already present, but the cached graph
reflected pre-fix routing. Running `comp-build` clears it. If comp-routes output looks wrong,
run `comp-build` first before debugging the source code.

*All 8 respondents received and retested. Survey + fix cycle complete.*
*Generated by 1.0.0_SA_CTO — 2026-04-09*
