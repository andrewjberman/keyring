# Session Log — 0.7.0_AE_CloudOps — YALP_MDSRC.B4 — 2026-05-22

## Summary

Executed **YALP_MDSRC.B4** — the AE deploy-half of B3 (daily-SmartX-direct
upgrade). Committed + deployed the two DS-authored, locally-verified B3 files
across two pipelines, deploy-order pull-Lambda-first-then-producer. Both
Lambdas invoked; the daily sidecar + the additive timeseries rework verified
live. 0.4.0_DS signalled to run the closing e2e verification.

## Deployment Sequence

### Artifact 1 — smartx-model-monthly-pull (smartx-pipeline)

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `aa9f285bc` feat(smartx-pipeline): B3 daily-SmartX-direct sidecar -- pull Lambda |
| 2 | build-and-upload (`BAU_PARITY_SKIP=1`) | SHA256 `Fb1sCIedOPN/OrZbStGGADxQ1p3sJVajCLT1eXaJcVM=`; `smartx-pipeline/smartx-model-monthly-pull.zip` |
| 3 | Commit source map | `83ce5d898` ci(smartx-pipeline): upload artifact |
| 4 | terraform plan | 0 add, 1 change, 0 destroy (model_monthly_pull in-place) |
| 5 | safe-apply (HALTGT clean) | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff replan | No changes. Infrastructure matches the configuration. |
| 7 | Invoke once | StatusCode 200; output_keys = [_smartx_model_monthly.json, _smartx_model_daily.json] |
| 8 | record-deploy + tag + push | `5e1093780` ci: record deploy; tag `smartx-pipeline-v1.2.0` |

### Artifact 2 — yang-model-portfolio-benchmarks (yang-pipeline)

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `9f6357634` feat(yang-pipeline): B3 producer -- model return SmartX-realized e2e |
| 2 | build-and-upload | SHA256 in source map; `yang-pipeline/yang-model-portfolio-benchmarks.zip` |
| 3 | Commit source map | `38803287d` ci(yang-pipeline): upload artifact |
| 4 | terraform plan | 0 add, 1 change, 0 destroy (module.model_portfolio_benchmarks in-place) |
| 5 | safe-apply (HALTGT clean) | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff replan | No changes. Infrastructure matches the configuration. |
| 7 | Invoke once | StatusCode 200; 3 outputs written; timeseries_row_count 2675 |
| 8 | record-deploy + tag + push | `243b08167` ci: record deploy; tag `yang-v2.4.8` |

## Deployment Tags

| Pipeline | Tag | Source commit |
|----------|-----|---------------|
| smartx-pipeline | `smartx-pipeline-v1.2.0` | `aa9f285bc` |
| yang-pipeline | `yang-v2.4.8` | `9f6357634` |

## Verification

- Both Lambdas: `State=Active`, `LastUpdateStatus=Successful`.
- `_smartx_model_daily.json` live in `s3://opal-data-portal-v2/json/benchmarks/`
  — 246,535 bytes, LastModified 2026-05-22T15:03:11Z, schema
  `smartx_model_daily_v1`, as_of_date 2026-05-21, cadence daily, label
  smartx_realized. 5 models: ST/LTA/INT/LTC 432 days from 2024-09-03; UST 327
  days from 2025-02-03 (matches the B3 brief coverage windows). Present BEFORE
  the producer ran (deploy-order honored — no missing-sidecar window).
- `model_portfolio_benchmarks.json` — 1D / WTD / 1M `model_source=smartx_realized`
  (was `yang_design` for 1D/WTD under B1). 5 models.
- `model_portfolio_timeseries.json` — top-level keys include both `timeseries`
  (2675 rows, model-DESIGN series — additive rework, unchanged so MDLP_RVVALT is
  unaffected) and the new `timeseries_realized` (2055 rows, SmartX-direct). No
  truncating replace — the CTO R3 no-regression gate is satisfied live.

## Compiler Tools

| Phase | Tool | Result vs expect |
|-------|------|------------------|
| 1 (before commit) | `.tools/ds-commit-gate.sh` on both files | PASS — "All checks passed!" on both (py_compile + ds-precommit-check + ruff py39). |
| 1 (before commit) | `comp-iam service` on the SmartX pull Lambda | N/A — IAM did not change. The new `_smartx_model_daily.json` key is under `json/benchmarks/`, already covered by the existing `s3:PutObject arn:...:opal-data-portal-v2/json/benchmarks/*` prefix grant (model-perf-pull.tf). No iam.tf edit. |
| 2 (before apply) | `comp-iam gaps` | N/A — no iam.tf change in either pipeline. |
| 3 (after apply) | terraform 0-diff replan; `aws lambda get-function-configuration`; S3 head-object on the daily sidecar | All PASS — both pipelines 0-diff; both Lambdas Active/Successful; daily sidecar confirmed present + fresh before the producer run. |

## Current State

| Item | Status |
|------|--------|
| B4 Artifact 1 (smartx pull) | DEPLOYED — `smartx-pipeline-v1.2.0`; invoked; daily sidecar live |
| B4 Artifact 2 (yang producer) | DEPLOYED — `yang-v2.4.8`; invoked; 1D/WTD smartx_realized + timeseries_realized additive |
| B4 RAVC2 | SENT — COO + CC CTO + CC 0.4.0_DS |
| B3 e2e re-verify | HANDED to 0.4.0_DS — b1_e2e_verify.py CHECK 5/8 against the fresh artifacts |

## Next Steps

1. [0.4.0_DS] Run b1_e2e_verify.py CHECK 5/8 against the fresh artifacts -> confirm 10/10; send the closing B3 RAVC2.
2. [2.0.0_SA_COO] RAVC4 / close B4 on the DS verification verdict.
3. [~self] YALP_MDSRC.C1 — YCharts capture-Lambda dormant deploy (image built, Docker up); then SEC1 ITEM 2.1 (FRED SM-rewire) + 2.2 (JWT cutover outline).
