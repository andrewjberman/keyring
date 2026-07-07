# Brief — Market Overview index returns read low: modal shows PRICE return, plus EAFE gross-vs-net

- **Date:** 2026-07-07
- **From:** 0.2.0_DS_PortfolioAnalytics
- **To:** 1.0.0_SA_CTO
- **Trigger:** Wayne Wicker (advisory board) fact-checked 3-year annualized index returns on the dashboard against Bloomberg; reported all four came out lower.
- **Status:** Diagnosis SOURCE-CONFIRMED (raw PKL -> DDB -> served, all traced). Fix requires a CTO-lane decision because it touches the display and possibly the ingest/upstream feed.

## What Wayne reported (3Y annualized, period ending 2026-06-30)

| Index | Wayne / Bloomberg |
|---|---|
| S&P 500 | 20.4% |
| Russell 2000 | 18.3% |
| MSCI EAFE | 16.3% |
| US Agg (Bloomberg Agg) | 4.1% |

## Lineage (comp-tool traced)

`json-tiered/market-overview/summary+details+timeseries`
  <- `opal-market-overview-tiered-generator` (compounds DDB `daily_return`)
  <- DynamoDB `opal-portal-market-data`
  <- `yang-ingest-dynamodb` (batch-writes the raw PKL)
  <- `data_pkl` = `s3://opal-data-portal-v2/benchmarks/data_20260701_v1.pkl` (Yang's weekly Bloomberg upload, data_as_of 2026-06-30).

## Ground truth (all compounded on the exact 3-yr window 2023-07-03 -> 2026-06-30)

The PKL `return_daily` frame carries: `date, index_name, bbg_ticker, price, return, price_return`.
`return` = gross-dividend total return; `price_return` = price only. Ingest stores `price` and `daily_return`(=`return`); it does NOT store `price_return`.

| Index | bbg_ticker | `return` (total) | `price_return` | Served card field | Bloomberg |
|---|---|---|---|---|---|
| S&P 500 | **SPX** (price idx) | 20.58% | 18.99% | 20.59% | 20.4% |
| Russell 2000 | **RTY** (price idx) | 18.62% | 16.99% | 18.62% | 18.3% |
| MSCI EAFE | **MXEA** (price idx) | 17.15% | 13.49% | 17.16% | 16.3% |
| Bloomberg Agg | **LBUSTRUU** (TR idx) | 4.16% | 4.16% | 4.16% | 4.1% |

**Pipeline is faithful:** raw PKL `return` compounds to the served card field to the basis point. No corruption.

## Two distinct problems

### 1. The chart modal displays PRICE return, not total return (frontend; this is what Wayne saw)
`portal/src/components/market-performance/IndexPerformanceModal.tsx:185` computes its "3Y Return" stat as `(last.price - first.price)/first.price` off the `historical_prices` (price level) series. That is a **price return** — ex-dividend — so it reads 1.4 pt (S&P) to 2.8 pt (EAFE) below Bloomberg's total return. The bond Agg matches because its price level already IS a total-return index.
- The total-return numbers are ALREADY computed and served (the summary/detail `period_returns`, from `daily_return`). The modal just doesn't use them.
- Secondary display defects in the same modal: it shows **cumulative** (~+70%) labeled "3Y Return" (no annualized option), and its window is a rolling `today - 1095 days` count (`CHART_PERIODS['3Y'].days = 1095`) rather than a clean 3-calendar-year window ending on the data's as-of date — a ~0.5 pt second-order error and a source of "2.97y not 3.0y" drift.

### 2. EAFE uses a GROSS-dividend series vs the standard NET benchmark (data/source decision)
Our MSCI EAFE is `MXEA` with the **gross-dividend** total return (`return` = 17.15%). Wayne's Bloomberg 16.3% is **MSCI EAFE Net** (standard benchmark, dividends net of foreign withholding tax). Gross exceeds net by ~0.85 pt/yr for EAFE. S&P and Russell show no such gap (US, no dividend withholding), which is why only EAFE is off. This is a convention choice, not a bug — but if we want to quote the street benchmark, Yang's PKL would need to send the net EAFE series (e.g. `NDDUEAFE`) instead of / alongside `MXEA`.

## Why this needs the CTO lane ("what's being sent over and/or frontend")

- **Frontend-only path (fast):** point the modal's period-return stat at the served `period_returns` (total return) instead of diffing `price`. Fixes the headline number Wayne hit. The chart LINE would still be a price series unless we also feed it total return.
- **Cloud/feed path (fuller):** to make the chart itself total-return, the `timeseries/{ticker}.json` feed (and possibly the DDB ingest) must carry a total-return LEVEL series (the `price_return` column is already in the PKL but is dropped at ingest; a TR level would need building). Touches `yang-ingest-dynamodb` and the tiered/timeseries generator.
- **Upstream/data-governance path (separate):** EAFE gross-vs-net is a decision for Yang / the investment team, not a code fix.

## Recommendation

1. Assign an agent to scope the **frontend stat fix** (modal reads served total-return period_returns) + the cumulative->annualized label + the window anchoring. Low risk, high visibility (advisory-board-facing).
2. Decide whether the modal's **chart line** must also be total return (drives whether we build a TR level series in the feed — cloud work).
3. Route **EAFE gross-vs-net** convention to Yang / investment committee as a data-source decision; if net is desired, Yang adds the net EAFE series to the PKL.

## Addendum (2026-07-07) — index-not-ETF confirmation + first-pass residual-bps forensic

**Confirmed: indexes, not ETFs (no tracking error possible).** Every series in the PKL uses a Bloomberg ` Index` ticker — Wayne's four are `SPX`, `RTY`, `MXEA`, `LBUSTRUU` (all ` Index`). Whole-feed suffix census (84 series): 76 ` Index`, 4 ` Curncy` (crypto/metals), 4 ` Comdty`. **Zero ` Equity` tickers** and zero ETF roots (SPY/IWM/EFA/AGG). So residuals are NOT tracking error / expense drag.

**Residual-bps first pass (why our TR sits ~6–32 bps off Wayne's Bloomberg on identical underlying):**
- RULED OUT — precision/compounding drift: daily `return` stored to 4dp (0.01 bp granularity); compounding ~754 obs drifts sub-bp.
- RULED OUT — daily-vs-monthly frequency: our daily-compound == our month-end-compound to 2dp for all four (S&P 20.58==20.58; R2000 18.62==18.62; EAFE 17.15≈17.16; Agg 4.16==4.16). Series is internally self-consistent.
- CONFIRMED SENSITIVE but handled correctly — window boundary: including vs excluding the 2023-06-30 close swings S&P 47 bps; our canonical figure correctly EXCLUDES the start-day return (close-to-close 6/30/23→6/30/26).
- LEADING REMAINING CAUSES: (1) Wayne's 1-decimal rounding (~up to 10 bps); (2) **methodology delta** between Yang's computed gross-dividend daily TR on the price tickers (SPX/RTY/MXEA) and Bloomberg's PUBLISHED total-return index (SPXT / RU20INTR / net-vs-gross EAFE). Agg (`LBUSTRUU`, already a TR index) should tie exactly — its +6 bps is pure rounding.
- DECISIVE EXPERIMENT (needs Yang's Bloomberg terminal): pull the published TR index for each name over the identical window and diff series-vs-series against Yang's `return`. Not reproducible from served data alone — a Yang/terminal task, external gate.

## Grounding
- Raw PKL: `s3://opal-data-portal-v2/benchmarks/data_20260701_v1.pkl` (`return_daily` frame; bbg_ticker column).
- Served: `s3://opal-data-portal-v2/json-tiered/market-overview/summary/all-returns.json` (data_as_of 2026-06-30).
- Generator: `infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py` (`calculate_period_return` compounds `daily_return`; `get_time_series` stores `price`+`daily_return`).
- Modal: `portal/src/components/market-performance/IndexPerformanceModal.tsx:45-52,175-185`.
- Ingest: `yang-ingest-dynamodb` (model-portfolios thread; DDB `opal-portal-market-data`).
