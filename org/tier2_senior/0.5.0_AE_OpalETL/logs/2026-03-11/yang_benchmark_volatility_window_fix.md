# Volatility Window Floor Fix — yang-generate-benchmark-returns — 0.5.0_AE_OpalETL

**Date:** 2026-03-11

## Objective

Fix inconsistent volatility windows in `yang-generate-benchmark-returns` Lambda. The `calculate_period_returns` function used a 20-day trailing window for 1D volatility but passed raw period data for all other periods. Short to-date periods (WTD, MTD early-month, QTD early-quarter, YTD early-year) could have as few as 3-5 observations, producing null or noisy annualized volatility. The scatter chart lost points and the numbers that appeared were not comparable across the grid.

---

## Work Completed

### 1. Code Fix

Single-line insertion at line 399 of `lambda_function.py`:

```python
vol_data = period_data if len(period_data) >= 20 else series.tail(20)
```

This replaces the prior `vol = calculate_volatility(period_data)` with a 20-calendar-day floor. When a to-date period has fewer than 20 observations, the function falls back to `series.tail(20)` -- the same trailing window 1D already uses. When the period grows past 20 days, its own window takes over naturally.

**Unchanged:**
- 1D path (line 353-357) -- already uses `series.tail(20)`
- Return calculation -- still uses exact `period_data` with geometric compounding
- Long periods (1M, 1Q, 1Y, Since Inception) -- always above 20 observations
- Output schema, downstream consumers, legacy/comprehensive JSON formats

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `ca06e49c` fix(yang-pipeline): volatility window floor for short to-date periods |
| 2 | build-and-upload.sh yang-pipeline yang-generate-benchmark-returns | SHA256: `kXQxJB95zW8yrdFe4EXt+2i71qp++B7cKoTIfA3HVq4=` |
| 3 | Commit source map | `c9a59411` ci: upload yang-generate-benchmark-returns artifact [skip ci] |
| 4 | terraform plan | 1 changed (generate_benchmark_returns source_code_hash + s3_object_version) |
| 5 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | record-deploy + tag + push | `767cd93a` ci: record deploy, tag `yang-v2.2.3` |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| yang-pipeline | `yang-v2.2.3` | `767cd93a` |

## Verification

Terraform 0-diff confirmed after apply. Single Lambda function updated: `yang-generate-benchmark-returns`. S3 artifact version `vPCHFeoLOMx9DSwtt6m7lsTDbt6B_fQc` deployed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 20-day floor (not configurable parameter) | Industry standard (Bloomberg 1M realized vol = 20 trading days). Below 20 obs, sqrt(252) annualization amplifies sampling noise. No reason to make this configurable -- it is a statistical floor, not a business parameter. |
| Floor applied to all non-1D periods uniformly | 1D already had this behavior. Applying the same logic everywhere eliminates the inconsistency. Long periods naturally exceed 20 obs so the floor is a no-op for them. |
| Patch version (v2.2.3) not minor | Single function change, no contract change, no new output fields. Pure bug fix. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` | Added vol_data 20-day floor before calculate_volatility call | Yes -- `ca06e49c` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Updated artifact_sha256 for yang-generate-benchmark-returns | Yes -- `c9a59411`, `767cd93a` |
| `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | Added yang-v2.2.3 entry | Yes -- `767cd93a` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

The volatility window fix is deployed as `yang-v2.2.3`. The Lambda `yang-generate-benchmark-returns` now uses a trailing 20-day floor for volatility calculations across all periods. The next time the Yang pipeline runs (nightly or manual trigger), benchmark_returns.json and model_portfolio_benchmarks.json will populate volatility for short to-date periods that previously showed null.

---

## Next Steps

1. **Verify next pipeline run** -- after the next nightly Yang pipeline execution, spot-check `json/benchmarks/model_portfolio_benchmarks.json` to confirm WTD/MTD volatility values are populated (not null) and reasonable.

**Do NOT:**
- Change the return calculation logic -- only the volatility input window was affected
- Modify calculate_volatility min_points parameter -- the 5-observation minimum inside that function is a separate safety net
