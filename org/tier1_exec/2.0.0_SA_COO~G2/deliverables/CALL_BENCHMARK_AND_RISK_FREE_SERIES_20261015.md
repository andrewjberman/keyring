# Call: which series are the Opal Overview's benchmark and risk-free rate? (2.0.0_SA_COO~G2, IRPT_ANLREQ workstream ~G, 2026-10-15)

**Asked by:** `2.0.0_SA_COO~G2`. **Gates:** the Overview's beta, alpha, Sharpe and Sortino elements (map ids `p7.e02`, `p7.e03`, `p7.e05`, `p7.e06`) and the benchmark chart `p7.e15`. **Does not gate:** the priced return, drawdown and risk figures that need no benchmark (they print once the release carries the price stage), the resident release r32, or FWD-1.

## What exists

- The priced Opal producer (`AR-g-86`, merged) values every element that needs only the portfolio's own series. The four statistics above also read a BENCHMARK level series and a RISK-FREE level series (`layout_overview._risk_stat`: monthly returns of each). With neither given they read `INPUT_MISSING:benchmark` or `INPUT_MISSING:risk_free`, which is true and printed in words.
- The map names the benchmark as `^SPXTR`, YCharts' own id for the S&P 500 total-return index (`benchmark_level_series`, from the YCharts report the Overview mirrors). No tracked line says which risk-free series the YCharts report used.
- PRD C-PRICES (v0.15) fixes the order for a SECURITY'S price (estate stores, Yahoo, YCharts one symbol per call, replacement, else omit). It says nothing about a benchmark or a risk-free rate.

## The decision

Which two series does the Opal Overview use, and where do they come from?

- **A. Two ETFs through the same chain (REC).** Benchmark `SPY`, risk-free `BIL` (SPDR Bloomberg 1-3 Month T-Bill ETF), each priced as any holding is: the estate's Bloomberg history first (it holds the Opal ETFs; whether it holds SPY and BIL is not yet read), then Yahoo, then YCharts. One mechanism, every price carries its source, no new vendor call, no rate-to-level conversion. Cost: SPY is a close stand-in for the total-return index, not the index (its fee is a few basis points), and BIL's return is a T-bill ETF's, not a bare rate.
- **B. A house benchmark and risk-free rate Andrew names.** If Opal already reports against a specific benchmark or rate, name it and where it is read from; the cell reads that instead.
- **C. Leave them NOT_AVAILABLE for now.** The four statistics keep saying `INPUT_MISSING` in words; nothing else changes. Cheapest; the Overview has four unfilled figures.

## What the answer releases

A or B: one cell in the ENGINE lane (the benchmark and risk-free series are resolved through the price chain and handed to the layout as its `benchmark` and `risk_free` arguments; about a day with its checks). C: nothing.
