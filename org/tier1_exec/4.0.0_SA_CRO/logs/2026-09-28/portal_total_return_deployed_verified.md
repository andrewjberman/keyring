# Portal total-return fixes deployed with reproducible proof - 4.0.0_SA_CRO~I
**archetype:** MIXED

**Date:** 2026-09-28
**Task Order:** ad-hoc portal-total-return-20260928-croi; Andrew-direct
**Status:** COMPLETE
**Window:** 2026-09-28T22:23:02Z -> 2026-09-28T23:36:23Z
**Basis:** No previous exact-seat log found across the 109 existing CRO logs,
including the latest two dated directories (2026-09-28 and 2026-09-26).
The window starts at the earliest dated substantive intake and covers this session.
**Coverage:** 6 commits; 5 significant messages; 9 deploy/ruling/validation groups
(one production rollout, one deployment authorization, seven verification groups).

## Objective

Investigate the Inflection Portal performance question, prove whether the
displayed numbers include income, identify the responsible producers, and then
implement, deploy and verify the corrections under Andrew's explicit instruction.
The final instruction also requested this one-shot log. No recurring cadence is armed.

## Compiler Tools

| Tool | Command/scope | Result | Note |
|---|---|---|---|
| comp-which | Route questions before searches/inspection | PARTIAL | Several useful routes; ambiguous queries explicitly admitted NO FIT/raw inspection |
| comp-find | Exact Lambda source, methods, deployment helpers, ownership, logs | PASS | Located definitions and measured the absence of prior exact-seat logs |
| comp-blast | Both modified Yang generators | PARTIAL | 19 downstream nodes each; graph was a lower bound, supplemented by direct output enumeration |
| comp-pipescript io | Both functions with --pipeline yang | WARN | Yang is not a supported pipeline choice; this was a coverage gap, not a clean dependency verdict |
| comp-routes trace | Positioning, aggregate and ETF JSON API paths | PASS | Declared /api/general/ to json/ mapping; live router/CloudFront checked separately |
| comp-pulse diff | Commit wrapper reflex | PARTIAL | Missing memory citation, broad source-map warnings, and deleted-sentinel SUBJECT_ABSENT_FROM_CORPUS were not treated as clean results |
| comp-tagauthz | safe-apply plan gate | PASS | No planned tag overwrite; code-only update touched no candidate tag resources |
| comp-lambdamap reconcile-deployed | Two-function deployed set | PASS | 2 already in parity, 0 held; recorder preserved other 26 Yang rows |

**What worked:** Exact definition searches, route tracing, scoped source-map
recording, deterministic artifact building and live byte comparison supplied
concrete boundaries for the deployment and verification.

**What failed:** The initial sparse worktree lacked several gate dependencies;
expanded checkout restored graph, naming registry, standards and directives
files without bypassing those gates. safe-apply initially selected a different
Terraform binary; SAFE_APPLY_TERRAFORM pinned the same installed binary used
for init/plan and the guarded retry succeeded. One local replay initially took
the non-Lambda AUM branch; setting its Lambda environment made the control faithful.

**Gap found:** Yang is absent from comp-pipescript's accepted pipeline registry.
The reflex's cited memory/feedback_structural_over_cultural_pattern.md was absent
at its reported path. The source-map files[] and downloaded ZIP members were
checked directly, so that missing citation did not substitute for package proof.

## Work Completed

### Investigation and intake

Loaded exact seat 4.0.0_SA_CRO~I through repository-local startup, measured 9/9
readiness, and preserved launcher ownership of all runtime helpers. The gateway
MCP was unavailable. Read and ACKed the exact base-CRO lossless relay
20260928T222302Z_4.0.0_SA_CRO__ANDREW-DIRECT__investigate__Inflection_.md,
acted on it, then archived that exact file. No client email was sent.

The five significant messages were Andrew's investigation request, his
total-return clarification, his cross-Portal Lambda question, his production
deployment authorization, and the base-CRO relay. The hard nudge was a duplicate
notification of that relay, not a separate authorization.

RCN-0019 established the Bloomberg DAY_TO_DAY_TOT_RETURN_GROSS_DVDS -> PKL ->
deployed Lambda -> JSON -> frontend binding chain. Historical/current Benchmark
cells matched (300/300); Positioning YTD cells matched (160/160). The bug was
Positioning's exclusion of opening-day WTD/MTD/QTD/YTD returns. Additional
inconsistencies were its 90-day 1Q and the ETF Performance feed's 21/63/252-row
trailing periods. Benchmark and Market Overview already had the correct boundaries.

### Deployment sequence

| Step | Action | Result |
|---|---|---|
| 1 | Commit source, authority and regression contract | 978e4b0eec |
| 2 | Build/upload only yang-generate-positioning and yang-generate-etf-returns | Deterministic ZIP metadata/size verified |
| 3 | Commit artifacts, rollback versions and verification script | 58162c16ed |
| 4 | Review saved Terraform plan | Exactly two in-place code updates; zero add/destroy; no configuration change |
| 5 | safe-apply | 0 added, 2 changed, 0 destroyed at 23:25:55Z |
| 6 | Download code; invoke both generators; verify outputs | Complete ZIP member parity; successful real Lambda invocations |
| 7 | Full untargeted Terraform plan | Exit 0: No changes. Your infrastructure matches the configuration. |
| 8 | Scoped recorder and tag | 652cf48876; local yang-v2.4.20; 2/28 rows stamped |
| 9 | Verify data, invalidate cache, close six-leg ledger | 7777fc2223; no open sentinel |
| 10 | safe-merge to shared CLOUD | b6cd9b4979; preserved peer work; no push |

### Verification

Seven groups: input total-return provenance; regression/negative controls;
deployed source parity; published numerical reconciliation; AUM input control;
full Terraform zero-diff; completed CloudFront invalidation.

- Four regression tests pass across all four producers and both ETF input
  representations. Old deployed code fails 49 subtest comparisons with zero errors.
- Published data: Positioning 1280/1280 (including mirrored holdings), aggregate
  240/240, ETF Performance 45/45, Benchmark 150/150. Total 1715/1715.
- Both deployed ZIPs equal their committed source member-by-member. Positioning
  CodeSha256: SGeYjRaOfPRsywinUrhrgYWJyAyrzCfqhuz3lTQWnu0=; ETF:
  pqOCSw8hl9CjLgi4H9YfSNDGO1TAvz8ALROWlOaJaTE=.
- Regeneration picked up September 25 AUM instead of September 24. Replaying the
  old handler with the exact new AUM version, with all S3 writes intercepted,
  reproduced every non-return field. No unexplained non-return difference remains.
- Distribution EVTSA9VEHNZVH invalidation IA4G138SBPNP00E74PL6N1R5UI completed.
  Six scoped request/rewrite paths include query variants.

## Decisions Made

| Decision | Rationale |
|---|---|
| Act on Andrew's direct deployment authorization | Explicitly extends this CRO task to implementation, deployment and verification |
| Retain Benchmark's 30/91/365-day rolling convention | Already the methodology of record; June 1 ruling is cited in existing Benchmark source |
| Use inclusive to-date starts and exclusive rolling cutoffs | Daily total returns on the opening day belong to WTD/MTD/QTD/YTD |
| Keep total-return sources and existing SI/full-history policies | Correct the identified period defects without changing model construction |
| Use scoped audited YANG_PIPELINE_DEPLOY commit override | Andrew-direct authority is durably recorded; author remains exact CRO seat |
| Retain newer AUM after controlled verification | Existing production input advanced normally; identical old-code behavior explains the delta |
| Keep commits/tag LOCAL | Shared CLOUD no-push boundary; origin/CLOUD observed at fd045338c40d3d3785d6e5c9c90e64da2024a276 |

## Files Modified

| File/group | Change | Committed |
|---|---|---|
| deliverables/RCN-0019_INFLECTION_PORTAL_PERFORMANCE_20260928.md and initial audit scripts/results/provenance | Investigation and source proof | 5cf12bee0e |
| infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py | Opening-day/as-of/1Q corrections | 978e4b0eec |
| infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/lambda_function.py | Calendar trailing windows, sorted legacy input | 978e4b0eec |
| infra/aws/lambda/ci/lambda-source-map.json and infra/aws/terraform/yang-pipeline/CHANGELOG.json | Scoped artifact and deployed-source record | 58162c16ed, 652cf48876 |
| deliverables/ANDREW_DIRECT_20260928_PORTAL_TOTAL_RETURN_FIX.md | Exact deployment authority | 978e4b0eec |
| deliverables/PORTAL_TOTAL_RETURN_FIX_20260928.md and inflection-performance-fix-20260928/ | Contract tests, independent reconciliation, replay, rollback, code/output/version/cache evidence | 978e4b0eec, 58162c16ed, 7777fc2223 |
| org/critical_paths/change_management/20260928T2314Z_portal-total-return-20260928-croi_deploy_completion.md | All six deployment legs CLOSED; sentinel removed | 7777fc2223 |

Deliverable paths abbreviated above are under org/tier1_exec/4.0.0_SA_CRO/.

## Blockers

None for the authorized correction. Authenticated browser rendering was not
available and is not claimed. Verification is against live deployed code,
origin data, route bindings and completed cache invalidation; it is self-verification,
not a separate CVO certification. The initial audit's 2.36-basis-point upstream
model-versus-weighted-ETF YTD difference and unflagged downloader fallback remain
separate provenance limitations, recorded without changing upstream methodology.

## Current State

Both fixed Lambdas are live in us-east-1, account 313476888478. The regenerated
objects are opal-data-portal-v2/json/positioning/positioning_data.json (version
lLg._UuvChRHF9CS5BLBLKuYdVmG0_5k), json/positioning/opal_aggregate.json
(yHniNbOUkeKw947DQCkKmbnkysosfpS0), and json/benchmarks/etf_returns.json
(0xSv6BeWmnBP78VjXyeBwWzol73cBPkE), as of September 25. Benchmark JSON is unchanged.

All implementation/evidence commits are merged locally into CLOUD at b6cd9b4979;
tag yang-v2.4.20 identifies the deployment record. The exact-seat inbox and staged
index were empty before logging. The isolated worktree at
C:/Users/AndrewBerman/Desktop/cro-i-portal-return-fix-20260928 is retained with
ignored rollback ZIPs, raw outputs and execution logs; its unrelated checkout
line-ending artifacts were not merged or committed. No additional runtime helper
or recurring logger was started.

## Next Steps

No remaining implementation or deployment step for this instruction. Refresh
the Portal to load the corrected outputs. Any later work on the separately
documented upstream provenance limitations should use its own explicit scope.
