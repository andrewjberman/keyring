# Q1 2026 Aggregate Opal Return Analysis -- 0.2.0_DS_PortfolioAnalytics

**Agent:** 0.2.0_DS_PortfolioAnalytics
**Date:** 2026-04-09
**Branch:** CLOUD
**Request:** Ad hoc -- Andrew

---

## Objective

Compute Q1 2026 aggregate Opal model portfolio return using:
1. Per-model Q1 returns from Yang's price index (data.pkl / model.pkl in S3)
2. AUM weights from the Model Portfolios page (aum-metrics.json)

---

## Data Sources

| Source | S3 Path | As-Of |
|--------|---------|-------|
| Model returns (price index) | `opal-data-portal-v2/benchmarks/data_20260401_v1.pkl` → `return_daily` | 2026-04-01 upload |
| AUM weights (current) | `opal-data-portal-v2/json/portfolios/aum-metrics.json` | 2026-04-08 |
| AUM weights (historical) | `opal-data-portal-v2/json/portfolios/aum-timeseries.json` | 2026-04-09 |

Used the `2026-04-01` pkl (not the `2026-03-31` one) because the March 31 pkl's `model_returns`
data cut off at March 27. The April 1 pkl contains the complete March 30 and March 31 rows.

Q1 window: Dec 31, 2025 close → Mar 31, 2026 close (61 calendar days, 61 rows per model including weekends with zero returns; 47 trading days with non-zero returns).

---

## Method

Used the `price` column in `return_daily` (long-form per `index_name`) to compute:

```
Q1 return = price[last trading day <= 2026-03-31] / price[last trading day <= 2025-12-31] - 1
```

This avoids the compounding noise from zero-return weekend rows in the `return` column,
and also avoids the `total` column which resets to 1.0 periodically within each pkl window
(confirmed: LTA total showed 1.000000 on both 2026-01-08 and 2026-03-30, not a continuous index).

---

## Q1 2026 Per-Model Returns

| Model | Dec 31 Price | Mar 31 Price | Q1 Return |
|-------|-------------|-------------|-----------|
| UST (Ultra Short Term) | -- | -- | **+0.44%** |
| ST (Short Term) | -- | -- | **+0.14%** |
| INT (Intermediate Term) | -- | -- | **-0.01%** |
| LTC (Long Term Conservative) | 127.5501 | 127.4804 | **-0.05%** |
| LTA (Long Term Aggressive) | -- | -- | **-0.12%** |

All returns sourced from Bloomberg `.{MODEL} Index` series tracked by Yang.

---

## AUM Weights

| Model | Q1-Start AUM (Dec 31, 2025) | Q1-Start Wt | Current AUM (Apr 8, 2026) | Current Wt |
|-------|----------------------------|-------------|--------------------------|------------|
| UST | $59,313,279 | 5.35% | $59,062,061 | 4.65% |
| ST | $80,844,301 | 7.29% | $98,764,311 | 7.78% |
| INT | $260,783,867 | 23.53% | $272,754,825 | 21.48% |
| LTC | $510,387,041 | 46.05% | $637,610,303 | 50.22% |
| LTA | $197,048,474 | 17.78% | $201,536,671 | 15.87% |
| **Total** | **$1,108,376,963** | | **$1,269,728,171** | |

---

## Aggregate Q1 2026 Opal Return

| Weighting Basis | Aggregate Return |
|----------------|-----------------|
| Q1-start AUM weights (Dec 31, 2025) | **-0.015%** |
| Current AUM weights (Model Portfolios page) | **-0.017%** |

Both converge to approximately **flat (-0.02%)** for Q1 2026.
The mix shift over the quarter was not large enough to meaningfully change the result.

---

## Benchmark Context

| Index / Portfolio | Q1 2026 Return |
|-------------------|---------------|
| S&P 500 | -4.63% |
| MSCI ACWI | -3.52% |
| Long-Term Benchmark (15% Agg / 85% ACWI blend) | -2.63% |
| Bloomberg Aggregate | -0.05% |
| **Opal Aggregate (AUM-weighted)** | **-0.02%** |

The aggregate model portfolio return was essentially flat, tracking closely to
Bloomberg Aggregate rather than the equity-tilted benchmark blends. Significant
relative outperformance vs. all benchmark comparisons.

---

## Script

Analysis script written to: `data/analysis/q1_2026_aggregate_opal_return.py`
(uses boto3 + pickle; runs locally against S3)
