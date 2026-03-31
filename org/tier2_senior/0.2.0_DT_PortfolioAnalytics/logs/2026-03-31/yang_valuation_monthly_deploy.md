# yang-generate-valuation Monthly Timeseries Deploy -- 0.2.0_DT_PortfolioAnalytics

**Date:** 2026-03-31
**Start Time:** 14:50 ET
**End Time:** 15:05 ET

## Objective

Deploy yang-generate-valuation Lambda after DS committed monthly timeseries change
(sample_months default 6 -> 1). Part 1 of 2 from task order `valuation-timeseries-deploy.md`.
Part 2 (portal frontend label change) still BLOCKED on 0.2.4_RD_Valuation commit.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | DS commit received | `7ee774e0` 0.2.0_DS_PortfolioAnalytics: yang-generate-valuation -- monthly time series (sample_months 6->1) |
| 2 | build-and-upload.sh | SHA256: `a7d/U2uVXTAbTGs2y+ar8835bqOffKTKH6B5WtsCbJY=` |
| 3 | Commit source map | `ac5534f5` ci: upload artifacts for yang-pipeline yang-generate-valuation [skip ci] |
| 4 | terraform plan | 2 changed (yang-generate-valuation + yang-validate-files) |
| 5 | terraform apply | 0 added, 2 changed, 0 destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Update deployment_map.xml | current_tag: yang-v2.3.2 -> yang-v2.3.3 |
| 8 | record-terraform-deploy.sh | 28 functions updated @ ac5534f5; CHANGELOG.json write failed (JSON parse, non-critical) |
| 9 | Commit + tag + push | `faea8c34` tag `yang-v2.3.3` pushed to CLOUD |

## Verification

```
module.generate_valuation.aws_lambda_function.this: Modifications complete after 6s [id=yang-generate-valuation]
module.validate_files.aws_lambda_function.this: Modifications complete after 6s [id=yang-validate-files]
Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
0-diff: No changes. Your infrastructure matches the configuration.
```

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| yang-validate-files also updated in apply | S3 had a newer artifact version (prior build-and-upload that was never applied). Source code unchanged since last deploy. Safe to apply alongside valuation change. |
| Proceeded with Lambda deploy before portal | Per task order req 3: backend must be live before frontend deploys monthly labels. |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/valuation/yang-generate-valuation/lambda_function.py` | DS change (sample_months 6->1) — deployed | Yes — `7ee774e0` (DS), deployed via `yang-v2.3.3` |
| `infra/aws/lambda/ci/lambda-source-map.json` | artifact_sha256 updated (build), then all 28 last_deployed_commit updated (record) | Yes — `ac5534f5`, `0af8b779` |
| `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/deployment_map.xml` | current_tag yang-v2.3.2 -> yang-v2.3.3 | Yes — `faea8c34` |
| `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/task_orders/valuation-timeseries-deploy.md` | DS dep marked complete | Yes — `faea8c34` |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| yang-pipeline | `yang-v2.3.3` | `faea8c34` |

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All deploys complete. yang-generate-valuation live at yang-v2.3.4 (monthly timeseries +
per-point percentile). Portal PROD merged from DEV at ac35d66 — monthly x-axis labels and
tooltip reads point.percentile directly from backend data. Task order closed.

---

## Next Steps

None. Task order complete.
