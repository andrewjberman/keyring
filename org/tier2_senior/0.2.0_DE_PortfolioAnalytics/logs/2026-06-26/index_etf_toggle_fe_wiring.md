# Session Log — 0.2.0_DE_PortfolioAnalytics — Index/ETF Benchmark Toggle FE Wiring
**archetype:** IMPLEMENT

**Date:** 2026-06-26
**Agent:** 0.2.0_DE_PortfolioAnalytics (Dashboard Engineer, Portfolio Analytics pod)
**Origin:** DS handoff (0.2.0_DS_PortfolioAnalytics, 20260626T1455Z) — Andrew/Yang-direct.

## Context

Yang Liu flagged (Teams, Andrew-direct 2026-06-26) that on the Model Portfolios
"Benchmark" tab the **Up/Down Capture, Rolling Sharpe, and Max Drawdown** sub-views of
the `ReturnVolatilityScatter` panel do NOT respond to the Index/ETF benchmark toggle —
only Return-vs-Volatility and the Benchmark Comparison heatmap do.

Root cause (DS, source-grounded): those 3 charts read `getModelPortfolioTimeseries()`,
whose rows carried a single `benchmark_return` (== INDEX). The scatter/heatmap read
`benchmarkData`, which already carries both index + etf series. DS shipped the producer
fix (`yang-model-portfolio-benchmarks build_timeseries()`, commit **f3cfe6a4a**) emitting
`index_benchmark_return` + `etf_benchmark_return` per row, retaining `benchmark_return`
as a back-compat alias == index. FE wiring was handed to this DE lane.

## Work done (FE wiring — portal DEV commit e5029515)

| File | Change |
|---|---|
| `src/api/portal-proxy.ts` | `ModelTimeseriesPoint` += `index_benchmark_return` + `etf_benchmark_return` (`number\|null`) |
| `src/components/ReturnVolatilityScatter.tsx` | new `benchmarkType` prop (default `'index'`); threads `benchmarkType` + toggle-resolved `benchmarkCompositions` into all 3 sub-charts |
| `src/pages/ModelPortfolios.tsx` | pass existing `benchmarkType` state (behind `SHOW_BENCHMARK_TOGGLE` gate) into `<ReturnVolatilityScatter>` |
| `src/components/RollingCaptureChart.tsx` | `selectBenchmark()` series selector; null rows excluded by sign-filter; labels mirror compositions |
| `src/components/RollingSharpeChart.tsx` | series selector; BM Sharpe = null for any window containing a null benchmark; labels |
| `src/components/MaxDrawdownChart.tsx` | series selector; cumulative BM NAV pauses on null dates; labels |

**Pre-cutover safety:** the new dual fields are absent in the served JSON until DT
deploys the Lambda + the next yang nightly regenerates the artifact. `selectBenchmark()`
keys on `index_benchmark_return == null` to detect pre-cutover and falls back to the
legacy `benchmark_return` (== index). So nothing breaks now; the ETF toggle on these 3
charts shows index until the data lands, then flips live with no FE redeploy.

## Verification

- `tsc -b --noEmit`: **0 errors**.
- `eslint` (4 touched components): **0 problems**.
- Consumer set of `ModelTimeseriesPoint` traced (Grep) = exactly the 5 touched files —
  the type change is additive and fully contained.
- Visual no-regression / toggle-behavior verify: Playwright browser profile was locked by
  another session; and the real toggle test requires the post-deploy data anyway. Folded
  into the **post-nightly verify** (see Open).

## Open / handoff

- **DT:** deploy `yang-model-portfolio-benchmarks` (Terraform-only, DS commit f3cfe6a4a)
  so the next nightly emits the dual-benchmark fields. Flagged to COO (20260626T1508Z).
- **DE (me), post-nightly:** verify served `model_portfolio_timeseries.json` rows carry
  `index_benchmark_return` (== `benchmark_return` alias) + distinct `etf_benchmark_return`;
  screenshot the 3 charts toggling. Gated on the DT deploy + nightly.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-which "...deps of ModelTimeseriesPoint + 3 charts"` | routed to `pipescript --fe-reachability` / `comp-kuzu` (manifest backstop) |
| `comp-transform schema-check {RollingCaptureChart,RollingSharpeChart,MaxDrawdownChart}` | `Component not found` — these recharts chart components are not in comp-transform's prop-contract registry (gap noted below) |
| `pipescript --fe-reachability` | thread/producer-level reachability (134 threads); not React-component granular — confirmed it operates at pipeline tier, used Grep for the component-level consumer trace |

**Rule 20(b) FE dep-graph check:** satisfied via the consumer-set trace (Grep over
`portal/src` for `ModelTimeseriesPoint` / `getModelPortfolioTimeseries` / the benchmark
fields) — exactly 5 files, all touched, change additive/contained. `comp-transform
schema-check` could not cover these three components (registry gap).

**Gap found:** `comp-transform schema-check` has no entry for `RollingCaptureChart` /
`RollingSharpeChart` / `MaxDrawdownChart` (recharts presentational charts that consume a
typed timeseries prop rather than the tracked data-prop transform surface). Flagging as a
coverage gap for the comp-transform component registry.
