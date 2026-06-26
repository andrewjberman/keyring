# DevOps + Data-Contract Brief — model_portfolio_timeseries dual benchmark (Index/ETF toggle)

**Author:** 0.2.0_DS_PortfolioAnalytics
**Date:** 2026-06-26
**For:** Pod2 DE (frontend wiring) + Pod2 DT (portal/Lambda deploy)
**Origin:** Andrew direct (Teams w/ Yang Liu 2026-06-26) — the Up/Down Capture, Rolling
Sharpe, and Max Drawdown views on the Model Portfolios "Benchmark" tab do NOT respond to
the Index/ETF benchmark toggle; only Return vs Volatility (and the Benchmark Comparison
heatmap) do. Andrew: "all of those charts are not toggling aside from return vs volatility,
all of them need to be linked to the toggle."

---

## Root cause (source-grounded)

Two data paths feed the `ReturnVolatilityScatter` panel (`portal/src/components/ReturnVolatilityScatter.tsx`):

| View | Data source | Toggles? |
|---|---|---|
| Return vs Volatility (scatter) | `benchmarkData` (period returns carry both `index_benchmark` + `etf_benchmark`) | YES |
| Benchmark Comparison (heatmap) | `benchmarkData` + `benchmarkType` prop | YES |
| **Up/Down Capture** (`RollingCaptureChart`) | `getModelPortfolioTimeseries()` → single `benchmark_return` | **NO** |
| **Rolling Sharpe** (`RollingSharpeChart`) | same timeseries | **NO** |
| **Max Drawdown** (`MaxDrawdownChart`) | same timeseries | **NO** |

`model_portfolio_timeseries.json` only carried ONE `benchmark_return` per row, which was the
**INDEX** benchmark (producer `build_timeseries()` pulled `mapping['index_benchmark']` only).
**This answers Yang's question: the May upside/downside capture was computed vs INDEX.**

---

## What I changed (DS scope — Lambda only)

**File:** `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`
**Function:** `build_timeseries()`

- Added `etf_series = term_returns.get(mapping['etf_benchmark'])` (the ETF-blend daily series
  was already loaded in `term_returns` — same source the period/scatter path uses).
- Each timeseries row now emits **both**:
  - `index_benchmark_return` (daily decimal)
  - `etf_benchmark_return` (daily decimal)
- `benchmark_return` **RETAINED** as a back-compat alias == `index_benchmark_return` (prior
  behavior) so the current FE keeps working until DE threads the toggle. No breaking change.
- Updated the output `series_note`/log + my `data_contract.xml`.

**New row shape** (`json/benchmarks/model_portfolio_timeseries.json`, served at
`/api/general/benchmarks/model_portfolio_timeseries.json`):
```
{ date, model_code, model_return, benchmark_return, index_benchmark_return, etf_benchmark_return, rfr }
```
All return fields = daily decimal fractions (e.g. -0.009261 = -0.93%). `etf_benchmark_return`
is `null` for any (model, date) where the ETF series has no value (e.g. pre-ETF-inception dates).

Verification: `python -m py_compile` clean; `comp-pipescript io` confirms the producer writes
`json/benchmarks/model_portfolio_timeseries.json`.

---

## Pod2 DT — deploy (Lambda)

1. Deploy `yang-model-portfolio-benchmarks` via **Terraform only** (Rule 1; no console / no
   `update-function-code`). Standard build-and-upload + `safe-apply` cycle.
2. The new fields appear after the **next yang-pipeline run** regenerates the timeseries
   artifact. Do NOT trigger an ad-hoc gold run to validate (Rule); verify on the scheduled
   nightly's served artifact.
3. Verify served shape: `GET /api/general/benchmarks/model_portfolio_timeseries.json` →
   each row has `index_benchmark_return` + `etf_benchmark_return`. Spot-check a recent date
   where `index_benchmark_return == benchmark_return` (alias invariant) and
   `etf_benchmark_return != index_benchmark_return` (distinct series).

## Pod2 DE — frontend wiring (3 charts → toggle)

The producer now supplies both series; FE just needs to select by `benchmarkType`:

1. **Type** — `portal/src/api/portal-proxy.ts` `ModelTimeseriesPoint` (~line 816): add
   `index_benchmark_return: number | null` and `etf_benchmark_return: number | null`
   (keep `benchmark_return` for now).
2. **Thread the prop** — `ModelPortfolios.tsx` already owns `benchmarkType` ('index'|'etf',
   line ~406). Pass it into `<ReturnVolatilityScatter ... benchmarkType={benchmarkType} />`
   (line ~1906), then down into `RollingCaptureChart` / `RollingSharpeChart` /
   `MaxDrawdownChart`.
3. **Select the field** — in `computeRollingCapture` (`RollingCaptureChart.tsx:101-107`) and
   the Sharpe/drawdown equivalents, read
   `benchmarkType === 'etf' ? p.etf_benchmark_return : p.index_benchmark_return`
   instead of `p.benchmark_return`. Guard nulls (ETF series may be null on early dates).
4. **Benchmark labels** — the `MODEL_BENCHMARKS` map in `RollingCaptureChart.tsx:37-43` shows
   index composition names ("85% Agg / 15% ACWI"); when `benchmarkType==='etf'` these should
   show the ETF-blend labels (mirror the scatter/heatmap `benchmarkCompositions` /
   `etf_compositions` already in `comprehensiveBenchmarkData`).
5. Per Rule 20(b) run the FE dependency-graph check before commit; `comp-transform schema-check`
   on the 3 chart components after the type change.

Gate note: only show ETF/Index toggle wiring behind the existing `SHOW_BENCHMARK_TOGGLE`
(internal/Opal-Capital) gate — external/partner users stay on the ETF default (Andrew 2026-06-01).

---

## Handoff status

- [x] Lambda change committed (DS) — see commit in handoff message.
- [ ] Lambda deployed (DT).
- [ ] FE threading (DE).
- [ ] Served-artifact verify post-nightly (DT/DE).
