# ADVI_MVP318 WS1 -- Geo Parquet Rebuild (country encoding fix) -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-18
**Start Time:** 16:20 UTC
**End Time:** 16:28 UTC

## Objective

Deploy DS commit fec1f7e4 (script 07 country normalization fix) to EC2 and regenerate
the geo parquet so that US clients are no longer classified as stateless non-US clients
in `nna_aua_by_geography.parquet`. This unblocks the geo timeseries view (WS1).

---

## Root Cause (per DS)

Script 07 `_modal_geo()` checked `country != 'USA'` to identify non-US clients, but BD
stores client country as `'United States'` (full name). Every US client was treated as
non-US, causing `state` to be wiped to `''`. The Lambda then filtered
`country.isin(['USA','US',''])` — `'United States'` matched none of these — producing
an empty `geo_us` dataframe and zero categories in `timeseries_chart.json` geo view.

DS fix (fec1f7e4): normalize `'United States'`/`'US'` → `'USA'` before the non-US check.
Lambda defensively updated with `_US_COUNTRY_VARIANTS` constant covering all BD encoding
variants across all 4 filter sites.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS commit fec1f7e4 on CLOUD | Confirmed — `07_build_nna_aua_by_geography.py` + `bd-portal-publisher/lambda_function.py` |
| 2 | `aws s3 cp` script 07 to `s3://opal-data-bd/code/gold/` | Uploaded |
| 3 | Start EC2 i-01003b035d2988dfb (was stopped) | Running, SSM online |
| 4 | SSM command `f994c0f3`: run script 07 in isolation | Success |
| 5 | Verify geo parquet output | TX: $900.8M AUA, 49 states, 3,555 households |

---

## Verification Output

```
Date range:    2020-06-30 -> 2026-03-16
State view:    75,086 rows | 49 distinct states
City view:     1,073,824 rows | 995 cities across 48 states
31 unknown geography (expected)

Top states by AUA (as of 2026-03-16):
  TX   $900,754,857
  GA   $102,432,860
  FL   $ 89,778,061
  CA   $ 74,980,035
  AR   $ 62,596,703

Total AUA: $1,605,964,409
```

TX AUA ($900M) is now correctly in the state view — previously swallowed into empty geo.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/07_build_nna_aua_by_geography.py` | Country normalization fix | DS commit `fec1f7e4` |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | `_US_COUNTRY_VARIANTS` constant at all 4 filter sites | DS commit `fec1f7e4` |

---

## Current State

**Status:** COMPLETE (AE steps)

Geo parquet rebuilt on S3 with correct state encoding for all US clients. The remaining
step for the full fix to be visible in the portal is DT deploying `bd-portal-publisher`
at commit `fec1f7e4` (bd-pipeline Terraform apply). Once deployed, the next
`pipeline-complete.json` trigger will cause the Lambda to regenerate `timeseries_chart.json`
with populated geo categories.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Deploy `bd-portal-publisher` at commit `fec1f7e4`
   (bd-pipeline Terraform apply) — required for Lambda geo filter fix to take effect.
2. **[nightly or manual trigger]** After DT deploys, re-run gold layer or manually trigger
   `pipeline-complete.json` to cause Lambda to regenerate `timeseries_chart.json`.
3. **[0.4.0_DS_ClientPlatform / DT]** Run `.tmp_segment_analytics_diag.py` to confirm
   TX appears in geo categories.

**Do NOT:**
- Run script 07 again — geo parquet is correct as of 2026-03-18T16:27 UTC
- Skip DT Lambda deploy — the Lambda's own filter still needs the `_US_COUNTRY_VARIANTS` fix
  to be resilient to future BD encoding changes
