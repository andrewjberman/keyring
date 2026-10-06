# FINDING -- Model Portfolios Benchmark tab: the CIX issue, the missing ETF dots, and the Since Inception column

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-06 ~21:3xZ (5:3x PM Eastern). Read-only; nothing changed.
- **Order:** Andrew-direct, record
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_21xxZ_BENCHMARK_HEATMAP_CIX_BLOOMBERG_RESOLUTION.md`;
  inputs include Yang Liu's two Teams screenshots of 2026-10-06 20:31Z and 20:38Z (read with Andrew's permission).

## Answer: three separate things, one Bloomberg-side, two ours

| Symptom | Cause | Whose | New today? |
|---|---|---|---|
| Benchmark returns stuck at 2026-09-29 | Seven Opal custom CIX definitions on Bloomberg (`.UST_BMK .ST_BMK .INT_BMK .LT_BMK .UST_ETF .ST_ETF .LT_ETF`) stopped calculating after the quarter end; `.INT_ETF` and every component kept pricing. Andrew's record: "a user error on behalf of Yang where he did not update the CIX" | Bloomberg-side configuration (our CIX definitions), not a Bloomberg server change and not our pull | started 2026-09-30 |
| ETF benchmark dot missing on the Return vs Volatility chart (4 of 5 models) | A stale-benchmark GUARD deployed to our Lambda `yang-model-portfolio-benchmarks` at 2026-10-06 16:14Z (12:14 PM ET) by site Z (`0.7.0_AE_CloudOps~RV`, order OPAL_BBGTML.TO-GUARD-1, CTO and COO never-widen halves signed, commit `513b25f522`, deploy `8555ce7e`). A series whose last bar predates `data_as_of` now serves null on every period, and a new field `benchmark_last_date` was added | **ours, deliberate**: it replaced 171 silently stale numbers with nulls | **yes, today** |
| Since Inception column wildly off in ETF mode (e.g. Long-Term benchmark +48.43% vs model +14.48%) | The heat map's ETF row is built in the browser from `json/benchmarks/etf_returns.json`, whose Since Inception is CUMULATIVE since 2024-04-30, and placed beside the model's Since Inception, which the Lambda ANNUALIZES. It also blends the two ETFs' cumulative returns linearly. Check: VGSH cumulative 9.97% annualizes to about 3.9%, the served CIX value was 3.94% | ours, long-standing (the ETF producer's Since Inception has been cumulative throughout; its last change, 2026-09-28, touched window lengths only) | no |

## "Did any outbound call change shape?"

- **Bloomberg requests:** no. The Bloomberg integration's commits in the last two weeks touch the ETF daily pull (TrueShares
  DIVZ/IDVZ), the history backfill gap-fill and the research corpus; none touches the model or index benchmark pull.
- **Served files:** `json/benchmarks/model_portfolio_benchmarks.json` DID change shape today at 16:16Z (the guard: nulls,
  plus `benchmark_last_date`). `json/benchmarks/etf_returns.json` is unchanged in shape since at least 2026-09-19 (13 versions).
- **Portal:** no change to `BenchmarkHeatmap.tsx` or `ModelPortfolios.tsx` touching the benchmark data path since 09-15.
- **Repo vs deployed:** the guard's code is on the shared trunk (`513b25f522`); the laptop's working tree had not pulled it
  when read, so the deployed Lambda read as different from this tree's copy.

## What closes it

1. Yang re-saved the CIX (Andrew's record). The fix serves only after a new Bloomberg pull and the `/data-refresh` re-run;
   as of 16:16Z no new pull had landed (`benchmark_last_date` 2026-09-29). When it lands, the guard serves numbers again.
2. The Since Inception mismatch needs a portal or producer fix (annualize the ETF Since Inception, or take the ETF
   benchmark from the served file); it is independent of the CIX issue.
