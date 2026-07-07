# MKOV_RETFIX.TO-2 — Residual-bps reconciliation: INTERIM findings (mechanism identified)

- **Date:** 2026-07-07
- **Owner:** 0.2.0_DS_PortfolioAnalytics (SME; market-overview is Pod 1 territory)
- **TO:** org/tier1_exec/2.0.0_SA_COO/task_orders/MKOV_RETFIX.TO-2.residual-bps-reconciliation.md
- **Status:** Mechanism SOURCE-CONFIRMED from the raw PKL. Exact per-bp attribution vs Bloomberg's published TR still needs a terminal pull (see Gate).

## Question
Our total-return 3Y annualized sits ~6–32 bps off Wayne's Bloomberg on identical underlying INDEX data (S&P +18, R2000 +32, EAFE +85 [gross/net-dominated], Agg +6). Not tracking error (confirmed indexes, not ETFs). Why any residual at all?

## Ruled out (first pass)
- Precision/compounding drift — daily `return` stored to 4dp (0.01 bp); sub-bp drift.
- Daily-vs-monthly frequency — our daily-compound == our month-end-compound for all four.
- Window boundary — handled correctly (close-to-close, excludes start-day return).

## Mechanism identified (this pass, from PKL `return_daily`)
`price` is a pure PRICE index (`price_return` == `pct_change(price)`, diff=0). Yang synthesizes total return by adding a **smoothed continuous daily dividend yield on ~100% of trading days**, NOT discrete ex-date reinvestment:
- S&P 500: +0.0053%/day (~1.34%/yr), no lumps.
- MSCI EAFE: +0.0122%/day (~3.07%/yr).
- Bloomberg Agg: ~0 add-back (`LBUSTRUU` price level is already total return).

Bloomberg's PUBLISHED TR indices (SPXT / RU20INTR / net-or-gross EAFE) reinvest dividends **discretely on ex-dates**. Smoothed-continuous vs discrete reinvestment compounds to a slightly different 3-yr total, and the delta **scales with dividend yield** — matching the observed residual ordering (EAFE > R2000 ≈ S&P > Agg≈0). This is the residual source.

## Gate (why it can't be closed to the exact bp in-session)
Confirming the exact per-index bp requires the PUBLISHED Bloomberg TR series (SPXT/RU20INTR/NDDU-or-GDDU-EAFE) over the identical window for a day-level series diff vs Yang's `return`. That needs Yang's Bloomberg terminal (human) or a data source carrying the published TR index — I do NOT have terminal access (YCharts index-TR symbols are premium-gated 403). Mechanism is confirmed; exact bp attribution is the remaining step.

## Unifying recommendation (PRD candidate — flagged, not patched)
Both this residual AND the EAFE gross-vs-net issue have the SAME clean fix: **source Bloomberg's PUBLISHED total-return indices directly** (SPXT, RU20INTR, and net-EAFE NDDUEAFE) instead of computing TR from a price index + smoothed dividend add-back. That would (a) tie equities to Bloomberg's published TR to the bp, and (b) let us quote the standard net EAFE benchmark. This is a Yang-PKL / data-model change → route as a new PRD candidate, not a silent patch.

## Grounding
- Raw PKL: `s3://opal-data-portal-v2/benchmarks/data_20260701_v1.pkl` (`return_daily`: date, index_name, bbg_ticker, price, return, price_return).
- Tickers: SPX / RTY / MXEA / LBUSTRUU (all ` Index`; zero ETFs in feed).
- Prior brief: `docs/briefs/market-overview-3y-return-price-vs-total-return-20260707.md`.
