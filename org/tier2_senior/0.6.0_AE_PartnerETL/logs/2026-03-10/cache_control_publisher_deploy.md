# Cache-Control Publisher Deploy — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Task Order:** ADVI_49FNV3.005.cache-control-s3-metadata.md
**Tag:** bd-v2.17.2

## Objective

Add `CacheControl='public, max-age=300, s-maxage=3600'` to the `_save_json` S3 put_object call in both `bd-portal-publisher` and `bd-portal-advisor-publisher` Lambdas. Without this header, browsers applied heuristic caching based on Last-Modified age (~18% of age since last modified), causing stale portal data even after CloudFront invalidations.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `bd-portal-publisher/lambda_function.py` line 166 | Added `CacheControl='public, max-age=300, s-maxage=3600'` |
| 2 | Edit `bd-portal-advisor-publisher/lambda_function.py` line 60 | Same change |
| 3 | Build + upload `bd-portal-publisher` via PowerShell | SHA256: `NCbE4nzOnoBBUAelxiPIDrPSmzQwOdIpm2A3Fia7kCg=` |
| 4 | Build + upload `bd-portal-advisor-publisher` via PowerShell | SHA256: `YSu3dTRXSkoDZDhhsA8+9o53ZvnMlMQJXBwyzC1iIOw=` |
| 5 | Update source map SHA256 fields | `infra/aws/lambda/ci/lambda-source-map.json` |
| 6 | Commit source + source map | `b9c483aa` feat(bd-pipeline): add Cache-Control metadata... |
| 7 | `terraform plan` | 2 to change (bd-portal-publisher, bd-portal-advisor-publisher) |
| 8 | `terraform apply` | 2 changed, 0 added, 0 destroyed |
| 9 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 10 | Update pipeline_inventory.xml + source map deployed fields | `current_tag: bd-v2.17.2` |
| 11 | Commit post-deploy records | `0177c5e7` ci: record deploy bd-v2.17.2 [skip ci] |
| 12 | Tag + push | `bd-v2.17.2` pushed to origin CLOUD |
| 13 | Trigger publisher (write pipeline-complete.json) | Publisher ran at 17:15 UTC |
| 14 | Verify Cache-Control on S3 objects | `public, max-age=300, s-maxage=3600` confirmed |
| 15 | CloudFront invalidation | `IBBYOP4C74SMIF09VX049SQGKL` InProgress |

## Verification

```
aws s3api head-object --bucket opal-data-bd --key gold/timeseries_chart.json:
  LastModified: Tue, 10 Mar 2026 17:16:43 GMT
  CacheControl: public, max-age=300, s-maxage=3600  OK

aws s3api head-object on gold/architect_leaderboard.json: public, max-age=300, s-maxage=3600  OK
aws s3api head-object on gold/clients_tab.json:          public, max-age=300, s-maxage=3600  OK
aws s3api head-object on gold/summary/header_metrics.json: public, max-age=300, s-maxage=3600  OK
```

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| bd-pipeline | `bd-v2.17.2` | `0177c5e7` |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `max-age=300` (5 min) | Eliminates browser heuristic caching. Short enough that new data shows within 5 min of next pipeline run. |
| `s-maxage=3600` (1 hr) | Overrides CachingOptimized 24h default TTL at CloudFront edge. Matches typical gold pipeline run frequency. |
| Did not change CloudFront policy | Per task order constraint — CachingOptimized honors s-maxage from origin, no CloudFront change needed. |
| Triggered publisher manually | Needed to rewrite all S3 objects with new header immediately rather than wait for nightly pipeline. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Added `CacheControl=` param to `_save_json` put_object | Yes — `b9c483aa` |
| `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py` | Same | Yes — `b9c483aa` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Updated artifact_sha256 for both publishers; post-deploy fields | Yes — `b9c483aa`, `0177c5e7` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/pipeline_inventory.xml` | Updated current_tag to bd-v2.17.2 | Yes — `0177c5e7` |

---

## Blockers

**Partial gap — out of scope for this task order:**

`gold/partner_analytics/header_metrics_quarterly.json` still has NO Cache-Control header. This file is written by the EC2 gold script `09_generate_partner_analytics.py` (which uses its own S3 boto3 calls), not by the publisher Lambdas. This file is the primary source for the PartnerAnalytics panel AUA display (`getPartnerAnalytics()` in the portal). It will still be subject to browser heuristic caching until script 09 is updated to include Cache-Control.

A follow-up task order to 0.6.0_AE_PartnerETL is needed to fix `09_generate_partner_analytics.py` and any other EC2 gold scripts that write directly to S3.

---

## Current State

> **Status:** COMPLETE (with gap documented above)
> **Active branch:** `CLOUD`

Both publisher Lambdas are deployed at bd-v2.17.2 with Cache-Control headers on all `put_object` calls. S3 objects (`timeseries_chart.json`, `architect_leaderboard.json`, `clients_tab.json`, `header_metrics.json`, etc.) have been rewritten with `CacheControl: public, max-age=300, s-maxage=3600`. CloudFront invalidation `IBBYOP4C74SMIF09VX049SQGKL` fired. After this invalidation completes, browser requests will receive the correct Cache-Control header and will no longer cache stale portal data.

---

## Next Steps

1. **[Andrew] Verify in portal** — after CloudFront invalidation `IBBYOP4C74SMIF09VX049SQGKL` completes (~1-2 min), hard refresh the Advisor Intelligence page. The Network tab should show `Cache-Control: public, max-age=300, s-maxage=3600` in the response headers for `timeseries_chart.json`.
2. **[0.6.0_AE_PartnerETL] Fix EC2 gold script 09** — `09_generate_partner_analytics.py` writes to `gold/partner_analytics/` directly using boto3 without Cache-Control. Needs the same `CacheControl` parameter added to its `put_object` calls. Requires EC2 deployment protocol (repo -> S3 -> EC2 pulls).
3. **[0.6.0_AE_PartnerETL] Audit other gold scripts** — check whether scripts 07, 08, 10 and any other EC2 scripts that write S3 objects also need Cache-Control headers.

**Do NOT:**
- Run `aws lambda update-function-code` directly — Terraform is the only Lambda deployment mechanism
- Forget to trigger the publisher after any future Lambda code change — S3 objects must be rewritten for new headers to take effect
