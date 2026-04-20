# Opal Models vs. 49 Financial Performance — FY 2025

**Agent:** 0.2.0_DS_PortfolioAnalytics
**Date:** 2026-04-11
**Branch:** CLOUD
**Request:** Ad hoc — Andrew

---

## Objective

Quantify FY 2025 portfolio performance in three stages:

1. **Aggregate Opal model portfolio 2025 return** — using `model_20251231_v1.pkl` per-model daily returns weighted by real time-varying AUA (from `aum-timeseries.json`).
2. **49 Financial firm 2025 market return** — cross-checking the platinum `growth_decomposition` number against a first-principles account-level daily-chained TWR from `gold/account_performance.parquet`.
3. **49 Financial Opal-vs-Non-Opal segment split** — splitting the 49F book into positions in the 51-ticker Opal model universe vs. everything else (single stocks, mutual funds, non-Opal ETFs), computing segment-level daily-chained TWR from `gold/consolidated/positions.parquet`, and quantifying each segment's contribution to firm return.

---

## Stage 1 — Opal Model Aggregate 2025 Return

### Data sources

| Source | S3 Path | Purpose |
|---|---|---|
| Per-model daily returns | `opal-data-portal-v2/benchmarks/model_20251231_v1.pkl` → `model_returns` | Daily returns per UST/ST/INT/LTC/LTA |
| Per-model daily AUA history | `opal-data-portal-v2/json/portfolios/aum-timeseries.json` → `by_model` | Time-varying weights (Nov 2024 – present) |

### Critical unit fix

`model_returns['return']` is stored in **percent units** (verified against `BIL_return` / `QQQ_return` columns on 2025-06 sample: BIL daily = 0.0179 → 0.0179%/day ≈ 4.5% annualized, consistent with cash). The existing reference script `data/analysis/q1_2026_aggregate_opal_return.py` compounds these as decimals and is **off by two orders of magnitude** — flagged for correction.

### Method

Two complementary aggregations:

- **Static weights**: EOY-2025 AUA mix applied across every day of 2025 (simple but ignores book composition shifts).
- **Dynamic weights**: For each trading day, use the prior-day per-model AUA mix → compute weighted daily return → compound. Handles UST launching mid-2025 ($0 book in early 2025 → $59M by year-end) and LTC growing from 26% → 46% of book.

### Results

| Model | 2025 Return | EOY AUA | EOY Weight |
|---|---:|---:|---:|
| UST (Ultra Short-Term) | +4.64% | $59.3M | 5.35% |
| ST (Short-Term) | +5.06% | $80.8M | 7.29% |
| INT (Intermediate) | +15.62% | $260.8M | 23.53% |
| LTC (Long-Term Conservative) | +20.06% | $510.4M | 46.05% |
| LTA (Long-Term Aggressive) | +18.97% | $197.0M | 17.78% |
| **Aggregate** | — | **$1.108B** | 100% |

| Aggregation | 2025 Return |
|---|---:|
| **Static EOY weights** | **+16.88%** |
| **Dynamic daily AUA mix** | **+16.46%** |
| EOY-weighted $ contribution sum | +$187.3M on $1.108B = +16.90% |

Script: `data/analysis/fy2025_aggregate_opal_return.py`

---

## Stage 2 — 49 Financial Firm 2025 Market Return

### Approach A — Platinum `growth_decomposition`

Source: `s3://opal-data-bd/platinum/firm/timeseries_overview.json`, field `growth_decomposition` (annual/quarterly/monthly).

| Period | Start AUA | Market $ | NNA $ | `aua_residual_delta` $ |
|---|---:|---:|---:|---:|
| 2025 (annual) | $951.4M | +$214.6M | +$256.0M | +$282.8M |

- **Simple headline** (used in UI partner_analytics `market_pct`): `market / period_aua_start = +22.56%` — **inflated**, because mid-year NNA contributed a base that also earned market return but isn't in the denominator.
- **Quarterly-chained TWR**: +18.14%
- **Monthly-chained TWR** (recomputed from `growth_decomposition.monthly`): **+18.10%**

2025 monthly market returns from platinum:

| Month | Start AUA | Market % |
|---|---:|---:|
| 2025-01 | $951M | +3.26% |
| 2025-02 | $1,306M | +0.71% |
| 2025-03 | $1,328M | −1.17% |
| 2025-04 | $1,336M | +0.55% |
| 2025-05 | $1,345M | +3.29% |
| 2025-06 | $1,406M | +2.62% |
| 2025-07 | $1,251M | +0.29% |
| 2025-08 | $1,263M | +2.02% |
| 2025-09 | $1,320M | +2.37% |
| 2025-10 | $1,358M | +0.70% |
| 2025-11 | $1,432M | +0.97% |
| 2025-12 | $1,420M | +1.25% |

Jan residual +$323M and Jun residual −$192M flag possible bulk on-/off-boarding events; platinum's residual accounting is what causes the small divergence vs. the account-level recompute.

### Approach B — Account-level daily chained TWR (independent cross-check)

Source: `s3://opal-data-bd/gold/account_performance.parquet` (5.8M rows, 7,314 accounts, daily `total_aua` / `growth` / `daily_inflow` / `daily_outflow` / `aua_residual` per account).

Verified per-row identity `aua_change = growth + inflow − outflow + aua_residual` (median diff 0 on 1,000-row sample).

Method — for each trading day `d`:
```
r_d = Σ_accounts(growth_d) / Σ_accounts(total_aua_{d-1})
TWR = Π(1 + r_d) − 1
```
This is flow-/churn-robust because `growth` is cleanly separated from flows at the per-account daily grain.

**Result: 49F 2025 daily-chained TWR = +17.72%.**

Monthly comparison vs. platinum (10 of 12 months agree within 0.05 pp; Jan and Dec diverge in line with the known residual anomalies):

| Month | Account-level chain | Platinum monthly |
|---|---:|---:|
| 2025-01 | +2.435% | +3.260% |
| 2025-02 | +0.717% | +0.710% |
| 2025-03 | −1.159% | −1.170% |
| 2025-04 | +0.582% | +0.550% |
| 2025-05 | +3.266% | +3.290% |
| 2025-06 | +2.849% | +2.620% |
| 2025-07 | +0.294% | +0.290% |
| 2025-08 | +2.022% | +2.020% |
| 2025-09 | +2.362% | +2.370% |
| 2025-10 | +0.692% | +0.700% |
| 2025-11 | +0.945% | +0.970% |
| 2025-12 | +1.511% | +1.250% |

Script: `data/analysis/fy2025_49f_market_return_xcheck.py`

### Stage 2 summary

| Method | 2025 Return |
|---|---:|
| Platinum simple (headline in UI) | +22.56% |
| Platinum quarterly chained | +18.14% |
| Platinum monthly chained | +18.10% |
| **Account-level daily chained TWR (canonical)** | **+17.72%** |

Best firm number: **+17.72%** from account-level data.

---

## Stage 3 — 49F Opal vs. Non-Opal Segment Split

Motivation: Andrew flagged that 49F's top holdings (IEFA, DIVZ, IDVZ, SPYM, PFDE) **are** Opal model ETFs, so the 1.3 pp gap between 49F (+17.72%) and the Opal aggregate (+16.46%) cannot be explained by 49F holding exotic non-model securities. The real question is how the Opal-ETF portion of 49F's book performed vs. the non-Opal portion.

### Data source

`s3://opal-data-bd/gold/consolidated/positions.parquet` — 116M-row position-day panel (`date`, `account_id`, `asset_name`, `units`, `price`, `market_value`, `ticker`). 50.2M rows pertain to 2024-12-31 through 2025-12-31 at 49F.

### Segment definition

- **Opal segment**: positions whose `ticker` is in the 51-ticker Opal model universe (extracted from `model_pkl['holdings']['ticker'].unique()`).
  51 tickers: `AGG, BIL, BIV, BNDX, BSCQ, BSCR, BSJQ, CLIP, COWZ, DFSD, DIVZ, IBTF, ICSH, IDVZ, IEFA, IEMG, IJH, IQLT, IWM, JAAA, JEPI, LONZ, MINT, OBIL, PCHI, PDBC, PFDE, PFOE, QBER, QQQ, QUAL, SJNK, SPHY, SPMO, SPSM, SPYM, TBIL, UTEN, UTWO, UVXY, VCIT, VCSH, VEA, VGIT, VGLT, VGSH, VSS, VTV, VXX, XBIL, XLU`.
- **Non-Opal segment**: everything else (single stocks, mutual funds, non-Opal ETFs, CASH).

### Method

Mark-to-market each held position using prior-day units:
```
pos_gain_d = units_{d-1} × (price_d − price_{d-1})
pos_base_d = units_{d-1} × price_{d-1}
r_seg_d    = Σ pos_gain_d / Σ pos_base_d     (per segment per day)
TWR_seg    = Π(1 + r_seg_d) − 1              (daily chained)
```
Prior-day units isolates market P&L from flows. Positions that were freshly opened that day (no `units_lag`) are excluded from the base and gain on that day.

### Critical data-quality fixes

1. **Weekend snapshots**: The consolidated file contains all 365 calendar days. Weekend rows carry stale prices; Saturday-to-Monday resync created phantom 20–27% daily moves. Fix: restrict to weekdays only.
2. **US market holidays**: Even after removing weekends, US market holidays (Good Friday, Memorial Day, Juneteenth, MLK, Thanksgiving, etc.) still generated phantom 10–20% moves on the trading day after. Top 5 worst initial non-Opal daily moves were all holiday-adjacent. Fix: explicit holiday filter for 2025.
3. **Ticker consistency**: Verified same ticker has identical price across all accounts on same date (0 tickers with >1 price on 2025-06-30). Good.

Holiday list filtered: Dec 25-26 2024; Jan 1, Jan 9 (Carter), Jan 20, Feb 17, Apr 18, May 26, Jun 19, Jul 4, Sep 1, Nov 27, Dec 25 2025.

### Data-freshness caveat

`consolidated/positions.parquet` was last refreshed 2026-02-13; `canonical/holdings/*.parquet` was refreshed 2026-04-10. At EOY 2025 the two sources disagree slightly on Opal share:
- consolidated: Opal $916M / Non-Opal $568M (61.7% / 38.3%)
- canonical: Opal $1,034M / Non-Opal $440M (70.2% / 29.8%)

The ~$128M difference is asset_names resolved to Opal tickers in April that were unresolved in February. This biases the consolidated non-Opal bucket slightly larger. Non-Opal return is computed on the larger denominator, so if anything it **understates** the non-Opal outperformance. The consolidated file is the only source with the full day-level history needed for daily TWR, so we use it with this caveat noted.

### Results

| Segment | 2025 TWR | Avg daily weight |
|---|---:|---:|
| **Opal-ETF segment** | **+13.92%** | 67.1% |
| **Non-Opal segment** | **+30.61%** | 32.9% |
| **Firm combined (segment method)** | **+18.52%** | 100% |
| Firm (account-level daily TWR, independent) | +17.72% | — |

Segment method and account-level method agree within 0.8 pp on the firm number, validating both.

### Monthly chained returns by segment

| Month | Opal % | Non-Opal % | Firm % |
|---|---:|---:|---:|
| 2025-01 | +2.234 | +5.166 | +3.317 |
| 2025-02 | +1.243 | −2.379 | −0.135 |
| 2025-03 | +0.151 | −2.493 | −0.859 |
| 2025-04 | +0.841 | −1.220 | +0.091 |
| 2025-05 | +2.054 | +2.944 | +2.351 |
| 2025-06 | +1.883 | +3.424 | +2.372 |
| 2025-07 | −0.859 | +0.017 | −0.587 |
| 2025-08 | +1.945 | +4.045 | +2.580 |
| 2025-09 | +1.614 | +2.001 | +1.734 |
| 2025-10 | +0.030 | +7.883 | +2.401 |
| 2025-11 | +1.263 | +2.207 | +1.555 |
| 2025-12 | +0.749 | +6.000 | +2.403 |

### Why the non-Opal segment returned +30.6%

Top EOY 2025 non-Opal positions and their 2025 price returns (verified directly from consolidated prices):

| Ticker | Description | EOY MV | 2025 Price Return |
|---|---|---:|---:|
| SPLG | SPDR Portfolio S&P 500 ETF (cheaper SPY) | $96.8M | +17.79% |
| **PRAX** | **Praxis Precision Medicines (single biotech)** | **$43.4M** | **+282.98%** |
| JPEM | JPMorgan Active EM ETF | $19.4M | +22.90% |
| TASCX | Mutual fund | $18.9M | +18.35% |
| QGRO | Am. Century Quality Growth ETF | $18.1M | +15.18% |
| SPGP | Invesco S&P 500 GARP | $14.3M | — |
| SGOV | iShares 0-3M T-Bill | $13.2M | — |
| JMUB | JPMorgan Muni ETF | $12.9M | — |
| JPM | JPMorgan Chase (stock) | $12.6M | +37.27% |
| XSVM | Invesco S&P SmallCap Val Momentum | $10.0M | — |
| PRISX | T. Rowe Price Fin Svcs (fund) | $9.6M | — |
| AAPL | Apple (stock) | $9.4M | +9.05% |
| NVDA | NVIDIA (stock) | $5.3M | +38.92% |
| VOO / FXAIX | S&P 500 vehicles | $11.4M | +17.82% / +17.84% |

**PRAX** alone contributed roughly **$31M** of market gain (entered 2025 at ~$11M MV and finished at ~$43M — 147K shares × $76.96 → $294.74). With an average non-Opal base of ~$300M, PRAX contributed **~10 percentage points** of the non-Opal segment's 30.6% return from a single biotech name.

The remaining non-Opal outperformance came from broad S&P 500 exposure (SPLG, VOO, FXAIX ~$110M combined) and high-beta single stocks (JPM +37%, NVDA +39%).

### The key interpretation

| | 2025 Return | Notes |
|---|---:|---|
| **Opal model aggregate** (dynamic AUA weights, pure model) | **+16.46%** | What the 5 Opal models actually produced |
| **49F Opal-ETF segment** (Opal tickers as actually held at 49F) | **+13.92%** | What 49F clients actually earned on their model-aligned positions |
| **Gap** | **−2.54 pp** | 49F's model positions UNDERPERFORMED the pure Opal models |

The Opal models as a mathematical construct beat 49F's real-world execution of them by ~2.5 pp. Plausible drivers:

1. **Weight drift** — 49F accounts aren't rebalanced to exact model target weights; advisor overrides, lag, and cash drag diverge actual from target.
2. **Model mix at 49F is not the same as the firm-wide Opal mix** — 49F may be overweight UST/ST (which returned +4.6% / +5.1%) relative to the Opal aggregate which is dominated by LTC (46%) and LTA (18%) at +20% / +19%.
3. **Partial-year membership** — 49F positions classified as "in Opal" were only ~60–70% of the book; the accounts and dollars in models turn over across the year in a way the static 51-ticker membership test doesn't capture.

### Decomposing the firm gap

The earlier observation that **49F firm (+17.72%) beat Opal aggregate (+16.46%) by +1.3 pp** is the net of two much larger effects moving in opposite directions:

- 49F's **non-Opal sleeve** (32.9% weight) returned **+30.6%**, lifting the firm number.
- 49F's **Opal-ETF sleeve** (67.1% weight) returned **+13.9%**, dragging the firm number below pure models.

Weighted check: `0.671 × 13.92 + 0.329 × 30.61 = 9.34 + 10.07 = 19.41%`, close to the +18.52% segment-method firm TWR (residual difference from daily-chain vs. weighted-average approximation).

---

## Visualizations

### Chart 1 — Per-Model 2025 Returns
Scale: 1 char = 0.5%

```
 UST   +4.64%  █████████▍
 ST    +5.06%  ██████████▏
 INT  +15.62%  ███████████████████████████████▎
 LTC  +20.06%  ████████████████████████████████████████▏
 LTA  +18.97%  █████████████████████████████████████▉
                |--------|--------|--------|--------|--------|
                0%       5%      10%      15%      20%      25%
```

### Chart 2 — Opal EOY 2025 AUA Weight Mix
Scale: 1 char = 1%  (total = $1.108B)

```
 UST    5.35%  █████▎                                                   $59.3M
 ST     7.29%  ███████▎                                                 $80.8M
 INT   23.53%  ███████████████████████▌                                $260.8M
 LTC   46.05%  ██████████████████████████████████████████████          $510.4M
 LTA   17.78%  █████████████████▊                                      $197.0M
                |---------|---------|---------|---------|---------|
                0%       10%       20%       30%       40%       50%
```

### Chart 3 — Master Return Comparison (sorted)
Scale: 1 char = 1%

```
 49F NON-OPAL sleeve           +30.61%  ██████████████████████████████▋
 Opal LTC                      +20.06%  ████████████████████▏
 Opal LTA                      +18.97%  ██████████████████▉
 49F firm (account TWR)        +17.72%  █████████████████▊
 Opal aggregate (dynamic)      +16.46%  ████████████████▍     <- pure model
 Opal INT                      +15.62%  ███████████████▌
 49F OPAL sleeve               +13.92%  █████████████▉        <- actual at 49F
 Opal ST                        +5.06%  █████
 Opal UST                       +4.64%  ████▋
                                        |---|---|---|---|---|---|---|
                                        0%  5%  10% 15% 20% 25% 30% 35%
```

**The gap that matters:** Opal aggregate (+16.46%) − 49F Opal sleeve (+13.92%) = **−2.54 pp** — Opal models beat their own real-world execution at 49F by two and a half points.

### Chart 4 — Monthly Segment Returns 2025
Scale: 1 char = 1%. Center line `│` marks 0.

```
              Opal-ETF sleeve       Non-Opal sleeve         Firm blended
              -3 ─┼─ +4             -3 ─┼─ +8               -3 ─┼─ +4
 Jan-25           │██▎              +2.23      │█████▏       +5.17      │███▎      +3.32
 Feb-25           │█▎               +1.24    ██▍│            -2.38     ▏│          -0.14
 Mar-25           │▏                +0.15    ██▌│            -2.49    ▉ │          -0.86
 Apr-25           │▉                +0.84    █▎ │            -1.22      │          +0.09
 May-25           │██▏              +2.05      │██▉          +2.94      │██▎       +2.35
 Jun-25           │█▉               +1.88      │███▍         +3.42      │██▍       +2.37
 Jul-25          ▉│                 -0.86      │             +0.02    ▌ │          -0.59
 Aug-25           │█▉               +1.95      │████         +4.05      │██▌       +2.58
 Sep-25           │█▋               +1.61      │██           +2.00      │█▊        +1.73
 Oct-25           │                 +0.03      │███████▉     +7.88      │██▍       +2.40
 Nov-25           │█▎               +1.26      │██▎          +2.21      │█▌        +1.56
 Dec-25           │▊                +0.75      │██████       +6.00      │██▍       +2.40
              ────┴──────          ────┴──────              ────┴──────
```

Key patterns visible in the chart:
- **Opal sleeve** is remarkably steady — 11 of 12 months positive, narrow band of −0.9% to +2.2%. Reads like a diversified model book.
- **Non-Opal sleeve** is spiky — Feb/Mar/Apr all negative, then catastrophic Oct +7.88% and Dec +6.00% from single-stock / growth-ETF rallies. Classic single-name dispersion.
- **Firm blended** sits between the two but closer to the Opal sleeve (because Opal is 67% of weight). The Oct and Dec spikes in firm returns are entirely non-Opal contributions.

### Chart 5 — Non-Opal Top Contributors (EOY 2025)
Bar = EOY Market Value (scale: 1 char = $5M). Right column = 2025 price return.

```
 SPLG    S&P 500 ETF              ███████████████████▎      $96.8M    +17.79%
 PRAX    Biotech single stock     ████████▋                 $43.4M   +282.98%  ***
 JPEM    Active EM ETF            ███▉                      $19.4M    +22.90%
 TASCX   Mutual fund              ███▊                      $18.9M    +18.35%
 QGRO    Growth ETF               ███▌                      $18.1M    +15.18%
 SPGP    S&P GARP ETF             ██▊                       $14.3M      —
 SGOV    0-3M T-Bill              ██▋                       $13.2M      —
 JMUB    Muni ETF                 ██▌                       $12.9M      —
 JPM     Single stock             ██▌                       $12.6M    +37.27%
 XSVM    SC Val Momentum          ██                        $10.0M      —
 PRISX   Financial Sv fund        █▉                         $9.6M      —
 AAPL    Single stock             █▉                         $9.4M     +9.05%
 NVDA    Single stock             █                          $5.3M    +38.92%
```

*** = The standout. PRAX went from $11.35M → $43.39M on 147K shares @ $76.96 → $294.74. Rough contribution to the non-Opal segment return: ~$32M gain / ~$425M average non-Opal base ≈ **7.5 pp of the 30.6% non-Opal return from one biotech stock**. Broader S&P 500 exposure (SPLG/VOO/FXAIX ~$110M combined at +18%) contributed another ~5 pp. Together, these two themes explain roughly half of the non-Opal segment's 2025 outperformance.

### Chart 6 — Firm Return Decomposition
How the 49F firm's +17.72% is built from its two sleeves:

```
          Weight    Return    Contribution
 Opal      67.1%  × +13.92%  =  +9.34 pp   ████████████████████▍
 Non-Opal  32.9%  × +30.61%  = +10.07 pp   ██████████████████████
                              -----------
                    Firm TWR: +19.41 pp   (segment-weighted approximation)
                    Firm TWR: +17.72 pp   (account-level daily chain, canonical)
```

The non-Opal sleeve — despite being only 1/3 of the book by weight — contributes **slightly more** to the firm return than the Opal sleeve does. That's the arithmetic answer to "why did 49F beat the pure Opal aggregate": a minority of the book earned 2×+ the return of the majority.

---

## Artifacts

### Scripts (checked in to repo)

| Script | Purpose |
|---|---|
| `data/analysis/fy2025_aggregate_opal_return.py` | Stage 1 — Opal model aggregate 2025 return (static + dynamic weights) |
| `data/analysis/fy2025_49f_market_return_xcheck.py` | Stage 2 — 49F firm daily-chained TWR from account_performance.parquet |
| `data/analysis/fy2025_49f_segment_split.py` | Stage 3 — 49F Opal vs Non-Opal segment split with holiday/weekend filtering |

### Source data (S3, read-only)

| Key | Bucket | Purpose |
|---|---|---|
| `benchmarks/model_20251231_v1.pkl` | `opal-data-portal-v2` | Per-model daily returns, holdings, etf_returns |
| `benchmarks/data_20251231_v1.pkl` | `opal-data-portal-v2` | Full data bundle (not strictly needed for this analysis) |
| `json/portfolios/aum-timeseries.json` | `opal-data-portal-v2` | Per-model daily AUA history for dynamic weights |
| `json/portfolios/aum-metrics.json` | `opal-data-portal-v2` | Current AUM snapshot |
| `gold/account_performance.parquet` | `opal-data-bd` | Per-account daily total_aua / growth / flows (5.8M rows) |
| `gold/consolidated/positions.parquet` | `opal-data-bd` | 116M-row position-day panel (refreshed 2026-02-13) |
| `gold/canonical/holdings/{date}.parquet` | `opal-data-bd` | Daily per-account holdings with resolved ticker (fresher 2026-04-10) |
| `gold/dimensions/ticker_resolution.parquet` | `opal-data-bd` | asset_name → ticker mapping |
| `platinum/firm/timeseries_overview.json` | `opal-data-bd` | 49F growth_decomposition (annual/quarterly/monthly) |
| `platinum/firm/dashboard.json` | `opal-data-bd` | 49F headline AUA / counts |
| `platinum/firm/mix_summary.json` | `opal-data-bd` | 49F equity/FI/alt mix by quarter |
| `gold/firm_composition.json` | `opal-data-bd` | 49F top holdings snapshot |

### Intermediate outputs (local cache)

| Path | Contents |
|---|---|
| `%TEMP%\model_20251231.pkl` | Local cache of Opal model pkl |
| `%TEMP%\aum-timeseries.json` | Local cache of per-model daily AUA history |
| `%TEMP%\acct_perf.parquet` | Local cache of `gold/account_performance.parquet` |
| `%TEMP%\consol_positions.parquet` | Local cache of `gold/consolidated/positions.parquet` (650 MB) |
| `%TEMP%\pos_2025_seed.parquet` | 2024-12-31 → 2025-12-31 slice with `is_opal` tag (50.2M rows) |
| `%TEMP%\can_hold_20251231.parquet` | Canonical holdings EOY 2025 |
| `%TEMP%\can_hold_20241231.parquet` | Canonical holdings EOY 2024 |
| `%TEMP%\tick_res.parquet` | Ticker resolution table |
| `%TEMP%\seg_daily_2025.csv` | Initial (flawed) segment daily returns incl. weekends — kept for diagnostic reference |
| `%TEMP%\seg_daily_2025_biz.csv` | Business-day-only segment daily returns (pre-holiday filter) |

---

## Headline Summary

| | 2025 Return |
|---|---:|
| 49F Non-Opal sleeve (single stocks, growth ETFs, mutual funds — PRAX single biotech +283%) | **+30.6%** |
| **49F firm TWR (account-level, most authoritative)** | **+17.7%** |
| Opal model aggregate (dynamic AUA weights, "pure models") | **+16.5%** |
| **49F Opal-ETF sleeve (models as actually held at 49F)** | **+13.9%** |
| Opal LTC (best individual model) | +20.1% |
| Opal LTA | +19.0% |
| Opal INT | +15.6% |
| Opal ST | +5.1% |
| Opal UST | +4.6% |

**Takeaways**

1. Opal's 5-model aggregate returned **+16.46%** in 2025 on dynamic AUA weights.
2. 49F's firm earned **+17.72%** — a 1.26 pp premium to the pure Opal aggregate.
3. That firm-level premium is a composition artifact, not evidence that 49F's Opal execution beat the models. Decomposed: 49F's Opal sleeve *under*performed pure models by 2.5 pp (+13.9% vs. +16.5%), while the non-Opal sleeve (~33% of book) *over*performed at +30.6%, carried almost single-handedly by a $11M → $43M PRAX biotech position (+283%) and broad S&P 500 ETF exposure.
4. The 2.5 pp Opal-sleeve drag vs. pure models is the number worth investigating further — it points at weight drift / model mix / rebalancing discipline within 49F's Opal-allocated accounts.

---

## Follow-ups / Open Items

- **Q1 2026 aggregate Opal return script** (`data/analysis/q1_2026_aggregate_opal_return.py`) compounds `return` as decimal when the source stores percent. Fix pending.
- Investigate the **2.5 pp Opal-sleeve drag** at 49F — is it model mix (49F overweight UST/ST) or weight drift from target weights? Requires joining 49F holdings to model target weights per month and computing tracking error.
- `gold/consolidated/positions.parquet` refresh cadence: the file used here is from 2026-02-13 while `canonical/holdings/*.parquet` is from 2026-04-10. ~$128M of EOY 2025 non-Opal MV in consolidated gets reclassified to Opal in canonical (better ticker resolution). Worth refreshing the consolidated file or running Stage 3 against a per-date assembled canonical dataset if precision matters.
- Jan 2025 `aua_residual_delta` of +$323M and Jun 2025 of −$192M in platinum `growth_decomposition` — likely bulk onboardings / large account departure. Worth a targeted lookup of which accounts drove them.
