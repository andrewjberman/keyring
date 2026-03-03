# Session Log — Attribution TOTAL (BPS) and Positioning Yield Postmortem

**Date:** 2026-03-03
**Agent:** 0.4.0_DT_MarketIntelligence (Dashboard Engineer)
**Session type:** Investigation + Hotfix
**Tag deployed:** `yang-v2.1.5`

---

## Objective

Investigate two reported data quality issues on the Positioning page:

1. **Attribution table — TOTAL (BPS) column:** Numbers in the asset class table did not
   reconcile. Asset Alloc + Fund Select + Style Alloc did not equal Total for the same row.
   Reported example: `25.15 + 8.37 + 126.06 ≠ 110.14` (INT portfolio, QTD).

2. **Positioning Summary — Yield row:** Yang reported that portfolio yields shown on the
   dashboard were 50-100bps higher than his Excel model across multiple portfolios.

---

## Issue 1: Attribution TOTAL (BPS) — Root Cause and Fix

### What Was Found

The asset class table in the Attribution page (`AssetAllocationSummary.tsx`) renders four
columns from two entirely separate JSON files:

| Column | Source JSON | Aggregation |
|--------|------------|-------------|
| Asset Alloc (bps) | `allocation_summary.json` | Excel subtotal row |
| Fund Select (bps) | `holdings_attribution_data.json` | Sum of holding rows |
| Style Alloc (bps) | `holdings_attribution_data.json` | Sum of holding rows |
| Total (bps) | `allocation_summary.json` | Excel subtotal row |

These two files are produced by two separate lambdas:

- `yang-generate-holdings-attribution` — parses Yang's Attribution Excel, extracts
  per-holding fund_selection and style_allocation, and captures asset class subtotals
  (asset_allocation and total_attribution) from Excel's aggregate rows. Writes
  `holdings_attribution_data.json`.

- `yang-generate-allocation-summary` — reads `holdings_attribution_data.json`, groups
  holdings by asset class, extracts the subtotal values, and writes
  `allocation_summary.json`.

### Root Cause: Orphaned Lambda

`yang-generate-allocation-summary` was **not wired into the Step Functions pipeline**.

Branch 5 of the `ProcessFileTypes` parallel state (`CheckAttributionExcel`) ended at
`GenerateHoldingsAttribution` with `"End": true`. The allocation summary lambda was never
automatically triggered by an Attribution Excel upload.

As a result, every time Yang uploaded a new Attribution Excel:
- `holdings_attribution_data.json` was regenerated (holdings lambda fired)
- `allocation_summary.json` was NOT regenerated (allocation summary lambda never fired)

The two files drifted out of sync. On 2026-03-03 the gap was 4 hours 28 minutes:

```
holdings_attribution_data.json:  last modified 2026-03-02 22:20 UTC
allocation_summary.json:          last modified 2026-03-02 17:52 UTC
```

This caused the four table columns to display numbers from different data runs. The columns
did not reconcile because they were literally not from the same computation. The math was
correct within each file; the files just did not agree with each other.

In addition, `allocation_summary.json` was cached in CloudFront (both distributions
`E2LPCXXBLDGWXY` and `EVTSA9VEHNZVH`) and the stale version continued to be served even
after S3 was updated, because the allocation summary lambda was invoked manually (outside
the pipeline) and did not trigger the `yang-invalidate-cloudfront` step.

### Contributing Factor: Missing `processed.$` Parameter

The `GenerateHoldingsAttribution` state in the Step Functions definition was also missing
`"processed.$": "$.processed"` from its Parameters block. The `processed` payload carries
`model_pkl_key` downstream. Without it, any lambda downstream of holdings-attribution that
needed the pkl key (including allocation-summary) would have to fall back to inference from
the manifest, which is fragile.

### Fix Applied (yang-v2.1.5)

1. **Pipeline wiring** — Added `GenerateAllocationSummaryAfterAttribution` as a sequential
   successor to `GenerateHoldingsAttribution` in Branch 5:
   ```
   CheckAttributionExcel
     -> GenerateHoldingsAttribution
     -> GenerateAllocationSummaryAfterAttribution
     -> END
   ```

2. **Parameter passthrough** — Added `"processed.$": "$.processed"` to the
   `GenerateHoldingsAttribution` Parameters block.

3. **Hotfix** — Manually invoked `yang-generate-allocation-summary` to regenerate
   `allocation_summary.json` from current holdings data, then invoked
   `yang-invalidate-cloudfront` to bust CloudFront cache on both distributions.

4. **Terraform** — `terraform apply` applied cleanly, zero-diff plan confirmed.

### Verification

Post-fix reconciliation across all five portfolios (QTD):

| Portfolio | Asset Class | AA (bps) | FS (bps) | SA (bps) | Total (bps) | Diff |
|-----------|-------------|----------|----------|----------|-------------|------|
| UST | Fixed Income | 0.00 | 5.74 | -8.53 | -2.79 | 0.00 |
| ST | Fixed Income | 0.83 | -4.10 | -55.84 | -59.11 | 0.00 |
| ST | Equity | 4.73 | 7.37 | 31.74 | 43.84 | 0.00 |
| INT | Fixed Income | 13.40 | 0.63 | -20.21 | -6.18 | 0.00 |
| INT | Equity | 8.93 | 7.74 | 146.27 | 162.94 | 0.00 |
| LTC | Fixed Income | 11.84 | 0.06 | -9.78 | 2.12 | 0.00 |
| LTC | Equity | 2.09 | -11.56 | 231.10 | 221.63 | 0.00 |
| LTA | Fixed Income | 11.09 | 0.13 | -9.80 | 1.41 | +0.01 |
| LTA | Equity | 1.96 | -25.52 | 235.79 | 212.23 | 0.00 |

All diffs are within floating point rounding tolerance.

### What `yang-generate-holdings-attribution` Is and Is Not Responsible For

This lambda is responsible for:
- Parsing the Attribution Excel (horizontal and vertical formats)
- Extracting fund_selection and style_allocation at the individual holding row level
- Capturing asset_allocation, style_allocation, and total_attribution from
  Excel's asset class subtotal rows (the Equity / Fixed Income aggregate rows)
- Attaching those subtotals to holdings via `_asset_class_subtotal` so the allocation
  summary lambda can consume them
- DynamoDB ETFClassifier lookup for canonical asset_class assignment
- Normalizing asset_class to display format ('Fixed Income', 'Equity') for frontend
  string-match grouping

This lambda is NOT responsible for:
- Computing Total (bps) — that comes from `total_attribution` on the Excel subtotal row,
  read verbatim. `total_attribution` is hardcoded to 0 at the holding level
  (intentional — the subtotal path is the authoritative source).
- Generating `allocation_summary.json` — that is `yang-generate-allocation-summary`.

### Prior Fixes in This Series (for context)

| Tag | Fix |
|-----|-----|
| yang-v2.1.1 | Restore dual-format Excel parser (underscore sheet detection) |
| yang-v2.1.2 | Wire DynamoDB ETFClassifier + IAM GetItem/Query permissions |
| yang-v2.1.3 | Normalize DynamoDB asset_class to display format (fixed_income -> Fixed Income) |
| yang-v2.1.4 | (prior work) |
| yang-v2.1.5 | Wire allocation summary into pipeline; add processed.$ param passthrough |

---

## Issue 2: Positioning Summary — Yield Row (PARTIALLY ADDRESSED)

### What Was Found

Yield data for model portfolios on the Positioning Summary panel comes from the following
chain:

```
model_{YYYYMMDD}_v1.pkl (S3: opal-data-portal-v2/benchmarks/)
  -> etf_characteristics['yield'] per ETF
  -> yang-generate-positioning Lambda (calculate_characteristics())
     weighted avg: sum(etf_yield * weight) / sum(weight with yield)
  -> positioning_data.json
  -> GET /api/general/positioning/positioning_data.json
  -> PositioningSummary.tsx -> Yield (%) row
```

Pkl analyzed: `model_20260226_v1.pkl` (closest available to 2026-02-27; no Feb 27 pkl exists).

### Holdings Latest Date Issue

The pkl contains holdings for multiple rebalance dates per model. The date situation as of
the Feb 26 pkl:

| Portfolio | Latest Holdings Date | Notes |
|-----------|---------------------|-------|
| INT | 2026-02-04 | Current |
| LTA | 2026-02-04 | Current |
| LTC | 2026-02-04 | Current |
| ST | 2026-02-04 | Current |
| UST | 2026-01-07 | STALE — one full rebalance behind |

UST holdings in the pkl are a month old. If UST was rebalanced after Jan 7 in Yang's model
but the pkl was not regenerated to include it, the portal is showing stale yield for UST.

### Yield Calculation: NaN Exclusion Inflating Results

The `calculate_characteristics()` function in `yang-generate-positioning` computes portfolio
yield as a weighted average:

```python
yield = sum(etf_yield * weight) / sum(weight_of_holdings_with_yield)
```

Critically, the **denominator excludes holdings with NaN yield**. Three ETFs in the current
`etf_characteristics` DataFrame have no yield data:

| ETF | Portfolios | Approximate Weight | Impact |
|-----|-----------|-------------------|--------|
| PFDE | INT, LTA, LTC, ST | 7-11% | Excluded from denominator |
| PFOE | INT, LTA, LTC, ST | 7-11% | Excluded from denominator |
| DFSD | UST | 7.3% | Excluded from denominator |

The effect of NaN exclusion is that the weighted average is computed over only 78-94% of
the portfolio by weight. If PFDE and PFOE carry lower yield than the remainder of the
portfolio (which is likely — they appear to be equity factor ETFs), excluding them inflates
the reported yield.

For LTA and LTC, PFDE + PFOE together represent approximately 20-22% of the portfolio.
Computing a weighted average over only 78-80% of the portfolio while those 20-22% may hold
zero or near-zero yield is a material overstatement. This is the most likely driver of the
50-100bps discrepancy Yang is seeing vs. his Excel model (where PFDE and PFOE presumably
have explicit yield entries or are treated as 0%).

### Benchmark Hardcoded Fallback (Secondary Issue)

In `yang-generate-positioning/lambda_function.py` (line 862), introduced 2026-01-02:

```python
lbustruu_yield = 4.0  # Default Bloomberg Agg Index yield ~4%
if etf_characteristics_df is not None:
    agg_data = etf_characteristics_df[etf_characteristics_df.iloc[:, 0] == 'AGG']
    if not agg_data.empty and pd.notna(agg_data.iloc[0]['yield']):
        lbustruu_yield = float(agg_data.iloc[0]['yield'])
```

This fallback should resolve to AGG's yield if AGG is in `etf_characteristics` (which it
is: AGG yield = 3.86% in the Feb 26 pkl). The hardcoded 4.0 is only a fallback if AGG is
missing. Whether the fallback is actively being used in the live Lambda vs. the pkl-side
ETF lookup requires CloudWatch verification.

### Status: UNRESOLVED

The yield issue is **not fixed**. No changes were made to `yang-generate-positioning` or
`positioning_data.json`. The following items remain open:

1. **PFDE, PFOE (INT, LTA, LTC, ST)** — Missing yield in `etf_characteristics`. Denominator
   exclusion inflates portfolio yield for these four models. Requires Yang to confirm the
   correct yield assumption for PFDE/PFOE, or for the pkl generation process to populate
   these entries.

2. **DFSD (UST)** — Missing yield in `etf_characteristics`. Same denominator inflation
   applies, ~7.3% of UST weight excluded.

3. **UST holdings staleness** — UST latest holdings date in the Feb 26 pkl is 2026-01-07,
   one month behind. Unclear if this reflects a missed rebalance in the pkl or a genuine
   gap in the upload schedule.

4. **Benchmark yield hardcode** — The `lbustruu_yield = 4.0` fallback should be validated
   as either (a) not reached in practice because AGG is always present, or (b) removed and
   replaced with a live lookup that fails loudly rather than silently defaulting.

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/terraform/yang-pipeline/yang-pipeline-definition.json` | Added `GenerateAllocationSummaryAfterAttribution` state in Branch 5; added `processed.$` to `GenerateHoldingsAttribution` params |

## AWS Actions Taken

| Action | Detail |
|--------|--------|
| `terraform apply` | yang-pipeline Step Functions state machine updated |
| Lambda invoked | `yang-generate-allocation-summary` — regenerated `allocation_summary.json` from current holdings data |
| Lambda invoked | `yang-invalidate-cloudfront` — invalidated both CloudFront distributions (`E2LPCXXBLDGWXY`, `EVTSA9VEHNZVH`) |

## Git

| Commit | Author | Description |
|--------|--------|-------------|
| `03cfdd66` | 0.4.0_DT_MarketIntelligence | fix(yang-pipeline): wire GenerateAllocationSummary after GenerateHoldingsAttribution |
| `9b488439` | 0.4.0_DT_MarketIntelligence | fix(yang-pipeline): rename new state to GenerateAllocationSummaryAfterAttribution |

Tag: `yang-v2.1.5`

---

## Open Items

| # | Item | Owner | Priority |
|---|------|-------|----------|
| 1 | Resolve PFDE/PFOE yield — confirm with Yang whether 0% or a data source exists | Yang + CloudOps | High |
| 2 | Resolve DFSD yield — same question for UST | Yang + CloudOps | High |
| 3 | Determine if Yang imputed a yield for these ETFs in his Excel and align pkl to match | Yang | High |
| 4 | UST holdings date stuck at 2026-01-07 in Feb 26 pkl — verify pkl regeneration | Yang | Medium |
| 5 | Validate `lbustruu_yield = 4.0` hardcode is never reached in live Lambda | CloudOps | Low |
