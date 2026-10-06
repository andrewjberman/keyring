# Index benchmark N/A on the Model Portfolios Benchmark Comparison -- source trace (2026-10-06)

**Asked:** Andrew-direct ~13:2xZ via `0.0.0_AB_MSTR~Z` msg 30049: *"check Yang Liu chat. Download the image and parse it. We need
4.0.0_SA_CRO~Z to track the source of the problem regarding the index return. 1.0.0_SA_CTO~Z needs to be briefed in parallel."*
Bloomberg calls on Andrew's word at this terminal, ~13:4xZ: *"you have egress"*. **Traced by:** `4.0.0_SA_CRO~Z`.

## 1. What the page shows (Yang's image, as of 2026-10-05 5:00 PM ET)

- Index benchmark: N/A at 1D, WTD, MTD and QTD for all five models; TTW, 1M, 1Q, YTD, 1Y and SI populated.
- Long-Term and Ultra Long-Term benchmark rows identical in every cell.

## 2. Where it comes from (measured)

| hop | fact | evidence |
|---|---|---|
| page | `index_benchmark` / `etf_benchmark` picked by the Index/ETF toggle from one served JSON | `portal/src/pages/ModelPortfolios.tsx:1015` |
| served JSON | `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`, LastModified 2026-10-06 12:31:21Z, `data_as_of` 2026-10-05. Index benchmark null at 1D/WTD/MTD/QTD for all 5 models. **ETF benchmark ALSO null at 1D/WTD/MTD/QTD for UST, ST, LT, ULT**; only INT's ETF is populated | read 2026-10-06 ~13:4xZ |
| producer | Lambda `yang-model-portfolio-benchmarks`: per model, `index_benchmark` <- return_daily "<Term> Benchmark", `etf_benchmark` <- "<Term> ETF"; ULT uses the Long Term pair because the source carries no Ultra Long series (by design, `:102-108`) | `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py:81-110` |
| producer behaviour | the series are pivoted on a shared date index ending at the latest date of ANY series (`end_date = term_returns.index.max()`, :211). A series that stops earlier is NaN after its last bar: 1D = the last row (NaN), WTD/MTD/QTD = only NaN -> None. TTW/1M/1Q/YTD/1Y/SI drop the NaN and compound what is left, so they **serve a number that silently ends 2026-09-29** while the model runs to 2026-10-05 | `:211`, `calculate_period_returns` `:448-555`, `compound_returns` `:558-564` |
| input PKL | `benchmarks/data_20261005_v1.pkl`: 7 series last 2026-09-29 (Ultra Short / Short / Intermediate / Long Term Benchmark; Ultra Short / Short / Long Term ETF); Intermediate Term ETF and every model series last 2026-10-05 | read 2026-10-06 |
| first bad pull | PKLs 09-22..09-29: all series current. **From `data_20260930_v1.pkl` onward the 7 stop at 2026-09-29**; INT ETF and the models keep advancing | read of 10 PKLs |
| Bloomberg, live | historical PX_LAST 09-25..10-06 on the current Terminal session: the 7 CIX tickers (`.UST_BMK .ST_BMK .INT_BMK .LT_BMK .UST_ETF .ST_ETF .LT_ETF Index`) return nothing after 2026-09-29; `.INT_ETF Index` and `SPX Index` return every day to 2026-10-05. Reference data: `.ST_BMK` "49F SHORT TERM BMK" and `.ST_ETF` "49F SHORT TERM BMK ETF" LAST_UPDATE_DT 2026-09-29; `.INT_ETF` "49F INTERMEDIATE TERM ETF" 2026-10-05 | `bloomberg_historical_data`, `bloomberg_reference_data` |
| components, live | I22917US, LBUSTRUU, MXWD, VGSH, AGG, ACWI all priced through 2026-10-05 | `bloomberg_historical_data` |

## 3. Source

**The seven custom CIX index definitions on Bloomberg stopped calculating after 2026-09-29.** Not our pull, the pipeline, the
Terminal session or the market data: the same session serves `.INT_ETF` (built from the same AGG/ACWI components as `.ST_ETF` and
`.LT_ETF`) and every component through 10-05. The quarter-end timing (last value 09-29, the session before 2026-09-30) points at
the CIX definitions themselves -- for example a weight or rebalance schedule that ended at Q3 -- with `.INT_ETF` the one that was
extended or re-saved. That last part is an inference: the definitions are not readable through the API; `CIX <GO>` on the
Terminal shows them.

## 4. Two defects downstream of the source

1. **The populated benchmark cells are wrong, not just the N/A ones.** TTW, 1M, 1Q, YTD, 1Y and SI benchmark (Index for all five
   models; ETF for four) compound only through 09-29 against a model through 10-05, so every spread in those columns compares
   different windows. Nothing on the page says so.
2. **"ETF is fine" is not what the served file says:** ETF benchmark is N/A at 1D/WTD/MTD/QTD for UST, ST, LT and ULT; only INT is
   current.
3. **Nothing caught it for six pulls:** the PKL tripwire grades the as-of date, not per-series recency (OPAL_BBGTML-Z-S5), and the
   producer serves a stale series without a flag.

## 5. Fix route (for 1.0.0_SA_CTO~Z to rule; integrations/bloomberg/ changes are Andrew's word)

- **Source (needs the CIX owner at the Terminal):** open each of the 7 in `CIX <GO>`, extend or re-save the definition the way
  `.INT_ETF` was, confirm a 2026-09-30.. history appears, then re-run the daily pull + /data-refresh so the benchmark JSON recomputes.
  The names read "49F ..."; who owns the definitions is not established here (Yang Liu built the pull).
- **Guard (ours):** the producer refuses or flags a benchmark series whose last bar is before `data_as_of` instead of serving a
  shortened window; the tripwire grades per-series recency (Z-S5).
