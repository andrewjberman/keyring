# work-cycle 0015 — aum-metrics deploy+publish + INF_D_04 adv-view bug diagnosis -> DS-fix -> republish

**archetype:** DEPLOY (publish) **secondary:** DIAGNOSE, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~1900-1915Z
**Trigger:** DS handoff 185858Z + COO Andrew-direct RUN-NOW 190118Z (aum-metrics); COO Andrew-direct RUN-NOW 190250Z (INF_D_04 adv $8.42)

## A. aum-metrics GLOBAL re-source (MDLP I2-residual) — DONE+verified
Folded DS-authored generate_smartx_timeseries_and_metrics.py as the 3rd producer in the smartx_ingestion_pipeline event-gated daily job (all 3 MDLP producers share the MDPF feed + 11:30Z cadence; each isolated try/except). Commit 315cce24b. No IAM change (existing role covers DynamoDB + opal-data-mdpf Get/List + portal-v2 Get/Put). No local-write trap (--upload S3-only; history=DynamoDB). Built + targeted safe-apply (sha zHaGaTeMehl). Smoke-invoked -> all 3 success.
VERIFIED served aum-metrics.json (19:08:58Z): period 2026-06-05, total.aum (card) $1,807,839,716.27 (was $0 -- bug killed) == canonical opal_aggregate_aua; total.model_aum $1,492,003,158.45 == by_model donut slice-sum (7 models, reconciles); non_model $382,182,172.12. Matches DS dry-run to the cent. CF-flushed /api/general/portfolios/* on EVTSA9VEHNZVH (I28U771...) -- covers aum-metrics + account-distribution (latter's first proper flush; original MDLP deploy never flushed it).

## B. INF_D_04 views.adv $8.42 — verify-before-execute catch -> DS code fix -> republish
COO asked re-run; I VERIFIED FIRST and found a re-run would be FUTILE: my 18:48 run rewrote the whole artifact but the deployed code built views.adv.current.distribution.total with RAW quantiles (L2483), bypassing the >=$1K floor geo + per-advisor use (served adv min -11.7 / p10 $8.42 vs geo $1,052/$11,729). Surfaced the exact bug + 2-line fix to DS (re-run futile).
DS GREENLIT + fixed+deployed (commit 25154e161, their Rule-13 inf-gold lane) -- mirrored _build_geo_view: kept sum/count FULL (so adv.total.sum == donut total -- correctly rejected my floor_series which would've subset the sum), sourced size-stats from floored_distribution_stats. I verified deployed eb95e553 == origin/CLOUD HEAD, ran --single INF_D_04 (RC=0, runner self-stopped), published.
VERIFIED served (19:13:55Z): adv min -$11.70 -> $1,052.42, p10 $8.42 -> $11,729.60; geo UNCHANGED. L0 geo==adv now identical (min/p10/p50/p90/sum $206.08M) -- GEO!=ADV resolved. CF-flushed /api/scoped/advisor-intelligence/* on EVTSA9VEHNZVH (I3U5UEWK...).

## Session scoreboard (all 4 Andrew-watched surfaces GREEN)
MDPF_COUNTS counts live | INF_D_04 geo $11.7K | aum-metrics card $1.808B/donut $1.492B | INF_D_04 adv $11.7K.

## Lessons reinforced
- Verify-before-execute: the futile-re-run catch (deployed code deterministic) saved a wasted run + false-success; the WIN was diagnosing the code bug, not blindly re-running.
- floor semantics: floored_distribution_stats FILTERS (>=$1K), doesn't clamp; a call-site keeping a FULL sum must source only size-stats from the floored set (DS's correction to my floor_series suggestion).

## Compiler tools
sha byte-verify deployed-vs-origin/CLOUD (x2), SSM send-command/get-command-invocation (x2 single-script), s3api head-object + served-content verify (x3), cloudfront get-distribution-config behavior-audit + create-invalidation (PowerShell, x3). terraform targeted safe-apply.
