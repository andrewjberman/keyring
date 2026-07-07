# PRD CANDIDATE — Source published Bloomberg TR indices for Market Overview benchmarks

- **Date:** 2026-07-07
- **Author:** 0.2.0_DS_PortfolioAnalytics (SME; Market Overview is Pod 1 MarketIntelligence territory)
- **Requested by:** 2.0.0_SA_COO (out of MKOV_RETFIX.TO-2)
- **PRD owner (to adopt):** 1.0.0_SA_CTO
- **Relates to:** the MKOV_RETFIX frontend fix (TO-1) — INDEPENDENT of this; the modal TR/annualized/anchor fix is needed regardless.

## Problem
Market Overview index returns are computed from a **price index + a smoothed continuous daily dividend add-back** (source-confirmed from the raw PKL). Two consequences vs Bloomberg's published benchmarks:
1. **Residual ~10–30 bps** (yield-scaled: S&P +18, R2000 +32, Agg +6) — smoothed-continuous vs Bloomberg's discrete ex-date reinvestment.
2. **EAFE +0.85%** — `MXEA` gross-dividend synthesis vs the street-standard NET benchmark.

## Proposal
Change Yang's PKL to carry the **published Bloomberg total-return index** for each benchmark instead of a price ticker + computed dividend. Candidate tickers (Yang to confirm exact terminal symbols):

| Index | Current (price) | Proposed (published TR) |
|---|---|---|
| S&P 500 | `SPX Index` | `SPXT Index` (S&P 500 Total Return) |
| Russell 2000 | `RTY Index` | `RU20INTR Index` (Russell 2000 TR) |
| MSCI EAFE | `MXEA Index` | `NDDUEAFE Index` (MSCI EAFE **Net** TR USD) — resolves gross/net |
| Bloomberg Agg | `LBUSTRUU Index` | no change (already TR) |

(Same treatment extends to the other equity benchmarks in the feed as a follow-on; scope the four headline benchmarks first.)

## Benefits
- Equities tie to Bloomberg's published TR **to the basis point** — removes the smoothed-dividend approximation.
- EAFE quotes the **standard net benchmark** — closes Wayne's discrepancy at the source.
- Eliminates a whole class of "why doesn't the dashboard match Bloomberg" questions.

## Impacts / considerations
- **Field semantics:** with a published TR ticker, `return` derives directly from the TR level. Decide whether to keep a **separate price series** for the chart's price display (the modal charts price levels) vs charting the TR level. Recommend keeping both: TR for the return stat, price for the visual line.
- **Historical continuity (the real work):** switching tickers changes the level series. Yang's PKL build must pull the **full history** of the new TR tickers, and the DDB + served `period_returns` + any cached history must be **backfilled** so 1Y/3Y/5Y stay continuous. No silent splice.
- **Blast radius:** every consumer of the `return` field shifts to published-TR basis — model-portfolio benchmarks, peer performance, and any return display. Generally *more* correct, but it is a values change on served numbers → needs a never-widen-style review + re-verify against served artifacts.
- **Independent of TO-1:** the frontend modal fix (read TR `period_returns`, annualize, anchor to data date) is still required regardless of this change.

## Validation
- One-time **Bloomberg terminal diff** (Yang): published TR series vs current computed `return` over the identical window → confirms the residual closes.
- Post-change served parity check: recompute 3Y annualized from the new served `period_returns` == published Bloomberg TR to the bp.

## Owners (proposed)
- **Yang** — PKL ticker swap + full-history pull (human/terminal).
- **Pod 1 DS/AE (MarketIntelligence)** — ingest + tiered-generator adjustments, backfill.
- **0.2.0_DS_PortfolioAnalytics** — SME / reconciliation validation.

## Decision (Andrew-direct, 2026-07-07): NET EAFE confirmed
Andrew confirmed: **use the standard (NET) benchmark going forward** — `MXEA` (gross-synthesized) → **`NDDUEAFE`** (MSCI EAFE Net TR USD). This resolves the EAFE gross/net question and is folded into this ticker swap. Directive: "make sure that gets implemented" → this candidate is now decision-complete; CTO to formalize as the MKOV_RETFIX follow-on PRD and drive to a deployed change.

## Consumer-audit seed (first pass — CTO requires full column-level enumeration before locking)
Confirmed consumers of `return`/`period_returns`/`daily_return` (NOT exhaustive; comp-grep first pass):
- `portal/src/api/endpoints/market.ts` — `getMarketOverviewSummary`/`Details`, maps `period_returns`.
- `portal/src/components/PerformanceHeatMap.tsx`, `market-performance/ExecutiveSummary.tsx` — read `periodReturns`.
- `portal/src/components/market-performance/IndexPerformanceModal.tsx` — the TO-1 target (currently price-derived).
- **`portal/lambda/precompute-market-metrics.ts` — SECOND consumer that independently compounds `daily_return`** (separate surface that also shifts on cutover).
- **`etf_period_returns.json` / `yang-generate-etf-period-returns`** — related ETF-returns artifact; scope whether in/out.
- Still to enumerate: model-portfolio benchmarks, peer performance (flagged, not yet cited), any DDB-stored/cached historical `return`.
- **Cache/stale-value question (CTO-mandated):** determine whether any consumer STORES a historical `return` (vs recomputing from the live series each run) — those are stale-cache-on-cutover risks, not just going-forward changes. Needs a queryKey/TTL + DDB-materialization check.
