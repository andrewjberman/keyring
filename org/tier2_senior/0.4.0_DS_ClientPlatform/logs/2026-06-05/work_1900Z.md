# 0.4.0_DS_ClientPlatform — work_1900Z (MDLP I2-residual aum-metrics re-source built+handed; I3 geo served-verified)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

## MDLP_DISTFIX I2-residual — aum-metrics GLOBAL re-source: BUILT + GATE-CLEAN + RECONCILED + handed to AE

Andrew-direct run-now (DISTFIX I2-residual). `data/smartx/scripts/generate_smartx_timeseries_and_metrics.py`
re-sourced per COO spec + base-DE's confirm. The producer's GLOBAL current snapshot (donut by_model +
Total-AUM card) now reads the LIVE MDPF feed instead of the dead `smartx_allocations.parquet`
(was I1-pinned-to-49F + `total_aum=$0` served bug).

### What changed (surgical)
- New `load_mdpf_current_override()`: per-model donut from `model_aua_positions` union {49financial,
  inflection} (cohort_class=='model') -> AUM/counts + model_total; Total-AUM card from the **canonical
  `opal_aggregate_aua`** field of `json/mdpf/global/aggregate-aua-timeseries.json` — READ the
  pre-computed field, NOT a feeder re-sum (base-DE confirm 184724Z: my $1.899B feeder-sum
  double-counted cohort_2b $90.9M; correct headline = $1.808B). Returns `None` on read-fail ->
  falls back to the timeseries current point (never regresses the served value).
- `generate_metrics(current_override=...)`: per-model donut = MODEL-ONLY ($1.492B, reconciles with
  the corrected bell-curve); Total-AUM card/center = full-enterprise `opal_aggregate_aua` ($1.808B);
  kills `total_aum=$0`. Q0-Q3 historical baselines PRESERVED (growth %s self-correct). Per-firm UNTOUCHED.
- Fix-forward (required for gate + CLAUDE.md): stripped 20 emoji prints -> ASCII (was crashing the
  Windows charmap on the local dry-run + a no-emoji-on-AWS violation); added `from __future__ import
  annotations` (FA100); auto-fixed 5 F541.

### Validation
- **Gate** `.tools/ds-commit-gate.sh` -> **exit 0** (py_compile + AST undefined-name + sync-guard TRIPLE
  + ruff). "All checks passed."
- **Dry-run reconcile** (read-only, no upload, no gold-runner — C1-clean), confirmed on a clean Windows
  run post-emoji-strip:
  - `total.aum` (card, was $0): **$1,807,839,716.27** == canonical `opal_aggregate_aua`
  - by_model donut slice-sum: **$1,492,003,158.45** == `model_aum` == corrected bell-curve (donut reconciles)
  - `non_model_aum`: $382,182,172.12 (fresh canonical; overrides the stale $315.8M enterprise value)
  - period 2026-06-05 / `total_aum` != $0 / Q0-Q3 growth self-corrected (q0 +21.66%; 2 INF blends q0=None — no history, expected)
- **Handed to 0.7.0_AE 185858Z** (data/smartx/** = AE owned-paths -> Option-(b)): AE ACK'd 190001Z —
  folding all 3 MDPF-sourced producers into ONE event-gated 11:30Z `smartx_ingestion_pipeline` daily
  job (isolated try/except), IAM composes, will confirm the correct CloudFront dist for the aum-metrics
  path, smoke-verify served -> RAVC2-close. base-DE + I co-own post-deploy served-verify.
- Non-blocking flag carried to served-verify: account_count basis 7,334 (model-union funded) vs the
  bell-curve 7,301 — minor grain/timing, won't read as a regression (AE + base-DE aware).

## MDLP_DISTFIX I3 geo — PUBLISHED + INDEPENDENTLY SERVED-VERIFIED
- AE ran `inf-gold-layer-runner --single INF_D_04` (deployed 95c5833b == repo HEAD == the I3 fix;
  SKIP_EXISTING=0; --upload; runner auto-shutdown 25.4s — C1-clean) + CloudFront-invalidated
  `/api/scoped/advisor-intelligence/*` on EVTSA9VEHNZVH.
- I independently re-read served `opal-data-inf/platinum/firm/partner_analytics_monthly.json`
  (LastModified 18:48:39Z) `views.geo.{window}.distribution.total.percentiles`:
  current p10 **$11,729.60** (min $1,052.42) | m1 $11,760.09 | m2 $11,849.57 | m3 $10,951.73 —
  **ALL 4 windows p10 >= $1K**. The $8.42 dust on the Inflection Segment Analytics geo P10 is GONE.
- Surfaced to COO 185959Z (for COO->CTO->Andrew). Remaining I3-close = the VISUAL smoke half
  (memory `feedback_portal_project_close_needs_visual_smoke_gate`) — requested COO loop Andrew /
  /frontend-dev on the live panel -> RAVC2-close.

## Standing / open obligations
- **I2-residual + I1+I2 close:** AE deploying all 3 producers (one 11:30Z job); base-DE + I co-own the
  post-deploy served-verify on the scheduled cadence -> RAVC2-close.
- **I3 close:** visual-smoke half (COO loops Andrew / /frontend-dev) -> RAVC2-close.
- **R2 close:** next-day CloudWatch `BucketSizeBytes` trend read (C1, no forced run) -> RAVC2-close.
- **GLDINC §5:** parallel design track; engages on P0 reconcile-gate when 0.6.0_AE starts P0 CHECKPOINT.
- IDLE on next item.

## Compiler Tools
| Tool | Run | Result | Notes |
|---|---|---|---|
| ds-commit-gate | generate_smartx_timeseries_and_metrics.py | exit 0 | py_compile + AST undefined-name + sync-guard(triple) + ruff (post emoji-strip + future-import + F541 fix) |
| (functional smoke) | python generate_smartx... --output-dir (dry-run, no --upload) | PASS + RECONCILES | card $1.808B == canonical opal_aggregate_aua; donut-sum $1.492B == model_aum == bell-curve; total_aum!=$0; read-only, no gold-runner (C1) |
| (S3 served read) | boto3 get_object served partner_analytics_monthly.json (I3 geo verify) | PASS | all 4 geo windows p10>=$1K; independent confirm of AE's publish |

work-cycle:0018
