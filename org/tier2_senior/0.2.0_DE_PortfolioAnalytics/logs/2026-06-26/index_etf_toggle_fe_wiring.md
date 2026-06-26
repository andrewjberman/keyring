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

## Fast-track verification (gate cleared same session)

DT fast-tracked the data (Andrew-direct ASAP): deployed `yang-v2.4.12` AND manually
reran the producer, so the served artifact carried the new fields within the session
(no wait for the PM upload). DS data-verify PASSED (2790 rows, alias holds, etf distinct
2767/2790, **zero nulls** — etf full history from inception, magnitudes sane).

**Behavior verify (DE):** pulled the LIVE served artifact (`s3://opal-data-portal-v2/
json/benchmarks/model_portfolio_timeseries.json`, generated_at 2026-06-26T15:18:08Z) and
ran my exact chart math for INT under both toggles:

| metric | INDEX | ETF | differ |
|---|---|---|---|
| Up Capture 1Y | 92.12 | 82.32 | YES |
| Down Capture 1Y | 99.07 | 90.09 | YES |
| Rolling Sharpe BM 1Y | 1.927 | 1.62 | YES |
| Benchmark Max Drawdown | -9.086% | -9.74% | YES |
| **Model** Max Drawdown (control) | -6.599% | -6.599% | toggle-invariant OK |

=> all 3 charts demonstrably respond to the toggle on live data; the model-only control
is invariant (selector doesn't leak into model math). Spot INT 2026-06-18 ties to DS
exactly (model 0.005449 / idx 0.004437 / etf 0.008608).

**GO given to DT** (20260626T1524Z) to run the DEV->PROD promote of e5029515.

**Residual (one, low-risk):** the PIXEL screenshot leg was NOT run — the shared Playwright
browser profile was hard-locked by another agent's session all session. The change is a
data-source field swap inside already-rendering recharts components (no render-structure
change), so render-regression risk is low; flagged to DT as a fast post-promote spot-check,
NOT a gate. Did not hold Andrew's ASAP promote on an unacquirable browser.

## Outcome — LIVE on PROD

DT ran the canonical promote: **PROD `bee2842f`, tag `portal-v2.1.126`** (peeled-verified),
CI run 28248041838 conclusion=success, parity-gate empty, workspace pointer bumped
`46248a804` on CLOUD, main tree back on DEV. Validated DT's evidence; GO closed both sides.

**The Index/ETF toggle on Up/Down Capture + Rolling Sharpe + Max Drawdown is LIVE for
internal/Opal users** (behind `SHOW_BENCHMARK_TOGGLE`; external stays ETF default).
Andrew's ASAP delivered end-to-end in-session.

## Residual (non-gating)

- Pixel screenshot of the 3 charts toggling on PROD — deferred the whole session because the
  shared Playwright browser profile was hard-locked by another agent. Functional behavior was
  proven on live data (compute-equivalence above), so this is a spot-check, not a gate;
  owner = whoever frees the browser first (DT or DE).

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
