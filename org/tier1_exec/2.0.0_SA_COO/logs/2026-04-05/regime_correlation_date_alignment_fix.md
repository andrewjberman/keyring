# Market Regime SPX:AGG Correlation Date Alignment Fix -- 2.0.0_SA_COO

**Date:** 2026-04-05
**Session:** 14
**Pipeline:** market-overview
**Lambda:** opal-market-regime-classifier

---

## Issue

Andrew reported that the US Regime panel on the Market Overview page showed SPX:AGG
correlation at the 89th percentile while the other three signals (multi-asset momentum,
SPX volatility, yield curve) were all in the bottom decile -- consistent with recent
market stress. The correlation value was suspicious and inconsistent with the regime.

## Investigation

### Data verification

Downloaded the three source time series files from S3:

| Ticker | S3 Key | Entries | Date Range |
|--------|--------|---------|------------|
| SANDP500 | json-tiered/market-overview/timeseries/SANDP500.json | 1095 | 2021-11-19 to 2026-04-02 |
| BloombergAggregate | json-tiered/market-overview/timeseries/BloombergAggregate.json | 1095 | 2021-12-22 to 2026-04-03 |
| SANDPGSCI | json-tiered/market-overview/timeseries/SANDPGSCI.json | 1095 | 2021-11-22 to 2026-04-02 |

Key findings:
- Both SPX and AGG have 1095 entries but **different date ranges** (AGG has 04-03, SPX only to 04-02)
- **25 non-overlapping dates** between SPX and AGG (different trading calendars -- bond market holidays: Presidents' Day, MLK Day, etc.)
- Only **1070 shared dates** out of 1095 entries each

### Root cause

The `generate_historical_time_series` function in the Lambda iterated over equity dates
only and sliced returns by **positional index**:

```python
dates = [p.get('date') for p in reversed(equity_prices)]  # equity dates only
eq_ret = equity_returns[:i+1]   # slice by equity index
bond_ret = bond_returns[:i+1]   # slice by SAME index -- WRONG
corr_raw = calculate_correlation(eq_ret, bond_ret, period)
```

`calculate_correlation` takes `returns[-30:]` from each array with no date awareness.
Because the arrays have different date compositions, every recent position was
misaligned by 1 day:

```
SPX[2026-03-27] correlated with AGG[2026-03-30]  MISALIGNED
SPX[2026-03-30] correlated with AGG[2026-03-31]  MISALIGNED
SPX[2026-03-31] correlated with AGG[2026-04-01]  MISALIGNED
SPX[2026-04-01] correlated with AGG[2026-04-02]  MISALIGNED
SPX[2026-04-02] correlated with AGG[2026-04-03]  MISALIGNED
```

This produced spurious correlation values. The same bug affected `calculate_period_signals`
and `calculate_current_signals`.

### Impact quantified

| Metric | Misaligned (broken) | Date-aligned (correct) |
|--------|-------------------|----------------------|
| 30D raw correlation | -0.231 | +0.511 |
| Correlation score (0-100) | 62 | 24 |
| 90D portal percentile | 89 | 1 |

The correct value (+0.511) indicates stocks and bonds moving together during market
stress -- consistent with the other bottom-decile signals. The broken value (-0.231)
was a complete artifact of correlating returns from different dates.

### Secondary finding: dual percentile calculation

The portal (`MarketRegimeIndicator.tsx:140-227`) ignores the Lambda's pre-computed
`periodStats` percentiles entirely. It fetches the history time series and recalculates
percentiles client-side from raw values. This means both the Lambda output AND the
history file's raw values needed to be correct. The Lambda's `periodStats` are computed
but unused in the display.

## Fix

**File:** `infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-regime-classifier/lambda_function.py`

### New functions added

1. **`calculate_dated_returns(prices)`** -- Returns `{date: return}` dict for date-keyed alignment
2. **`align_returns_by_date(dated_ret1, dated_ret2, up_to_date)`** -- Intersects two date-keyed series by shared dates
3. **`calculate_correlation_aligned(dated_ret1, dated_ret2, period, up_to_date)`** -- Computes correlation on date-aligned returns only

### Call sites updated (4 total)

1. `calculate_period_signals` -- used for periodStats in regime JSON
2. `calculate_current_signals` -- used for current signal values
3. `generate_historical_time_series` main loop -- used for history JSON raw values
4. Rolling percentile loop in `calculate_period_signals` -- historical percentile distribution

All four now use `calculate_correlation_aligned` as primary path with positional
`calculate_correlation` as fallback when dated returns are not available.

### Observability additions

- `data_as_of` now uses the **earliest** ticker latest date (was equity-only, masking AGG having a newer date)
- `tickerDates` dict added to output JSON -- per-ticker latest dates
- `sharedTradingDays` count added to output JSON
- `[Step 7] WARN: Ticker date mismatch` log line when tickers have different as-of dates

## Deployment

| Step | Result |
|------|--------|
| Build zip (PowerShell) | 11.2 KB |
| Upload to S3 with SHA256 metadata | `s3://opal-313476888478-lambda-artifacts/market-overview/opal-market-regime-classifier.zip` |
| Terraform plan (targeted) | 1 change: Lambda source_code_hash update |
| Terraform apply | Applied, 0 added, 1 changed, 0 destroyed |
| 0-diff verification | No changes. Infrastructure matches configuration. |
| Lambda invoke | SUCCESS in 9.4s. Date-aligned: 1069 shared trading days. |
| CloudFront invalidation | Completed (IETRNBCR6DIDY28X4WNM2MPSEP at 16:50:03 UTC) |
| Andrew verification | Confirmed fixed on portal |

**No git tag yet** -- this is a targeted hotfix. The 3 unpushed GLDRST commits are still
on CLOUD. Tag should be created after DT pushes all pending commits together.

## Verified output (post-fix)

```
90D correlation: percentile=18 raw_corr=0.354 (was 89 / -0.127)
History latest:  2026-04-02 raw_corr=0.511 (was -0.231)
```

All four regime signals now consistent in the bottom decile during market stress.

---

## Current State

**Status:** COMPLETE (hotfix deployed and verified)
**Active branch:** CLOUD (uncommitted)

## Next Steps

1. **DT push** -- 3 GLDRST commits + this fix need to be pushed to remote
2. **Git tag** -- `market-overview-v1.6.8` after push
3. **record-terraform-deploy.sh** -- run after tag, update CHANGELOG.json
4. **Source map update** -- `lambda-source-map.json` needs new commit hash + SHA256
5. **Consider**: fix the tiered-generator to ensure all tickers are written atomically or with a manifest, preventing the date skew at the source
