# YANG_SITTW.TO-3 (WS-2b) — Phase-0 classification + FE pre-stage

**TO:** YANG_SITTW.TO-3.ws2b-ttw-model-portfolios | **DE:** 0.4.0_DE_ClientPlatform | **2026-06-16**
**Label (Andrew-direct, binding):** `TTW` (NOT 2W). Def (§5, binding cross-pod): TTW = trailing **10 trading days**, return = `P_latest / P_{10 sessions ago} - 1`, spread = `model_TTW - benchmark_TTW` same window.

## Phase-0 classification (per surface) — DECISIVE: BOTH = DATA-SIDE

Both TO-3 surfaces consume one `BenchmarkModelData[]` built by `ModelPortfolios.tsx` page transform (L694-732,
generic over periods via `Object.entries(model.returns)`) from `model_portfolio_benchmarks.json`
(`getModelPortfolioBenchmarks`). That file carries per-period model + index_benchmark + etf_benchmark
returns/spreads/volatilities. Default `benchmarkType='etf'`.

| Surface | File | Source of TTW | Classification |
|---|---|---|---|
| Return-vs-vol scatter | `ReturnVolatilityScatter.tsx` | needs `returns['TTW'].{model,benchmark,model_volatility,benchmark_volatility}` | **DATA-SIDE** |
| BenchmarkHeatmap | `BenchmarkHeatmap.tsx` | needs `returns['TTW'].{model,benchmark,spread}` for BOTH index + ETF modes | **DATA-SIDE** |

**Why not FE-compute:** the only served daily series (`model_portfolio_timeseries.json`) has a SINGLE
`benchmark_return` per model -> FE can cover at most one benchmark mode, leaving the OTHER (incl. the ETF
default) N/A. Scatter per-period volatility is producer-computed (`std(ddof=1) x sqrt(252)`); FE-replicated
TTW vol would be methodologically inconsistent on a cross-period vol chart. => data-side.

## Producer (data-side leg — AE/Yang-pipeline lane, NOT DS)
- Lambda `yang-model-portfolio-benchmarks` (ProcessBothPKLs); `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`; TF `module.model_portfolio_benchmarks`.
- Owner recommendation: **0.7.0_AE_CloudOps** (Yang-pipeline lineage map + bmkaud benchmark-writer census authored by them). COO routing the spawn.
- Change (~2 lines, additive, never-widen-safe): (1) L191 append `'TTW'` to `periods`; (2) `calculate_period_returns()` add `elif period == 'TTW': period_data = series.tail(10)` (among window branches, NOT the 1D early-return). Emits model+index+ETF TTW into model_portfolio_benchmarks.json + benchmark_returns.json. etf_returns.json NOT touched (heatmap ETF mode reads etf_benchmark from comprehensive file; etf_returns is fallback only).
- **Binding producer key = `'TTW'`** (FE PERIOD_DATA_KEY must match). Deploy = Terraform + YangDataPipeline re-run.

## FE pre-stage (my lane; HOLD commit until producer TTW deployed, then land + Phase-3 verify)

### `portal/src/components/BenchmarkHeatmap.tsx`
- `ALL_PERIODS` (L53): insert `'TTW'` after `'WTD'` -> `['1D','WTD','TTW','MTD','1M','QTD','1Q','YTD','1Y','SI']`.
- `PERIOD_NAMES` (Record<Period> — TS-enforced): add `TTW: 'Trailing Two Weeks'`.
- `PERIOD_DATA_KEY` (Record<Period>): add `TTW: 'TTW'`.
- `FIXED_PERIOD_TRADING_DAYS` (L90): add `TTW: 10` — REQUIRED so NET-mode fee proration uses 10 trading days (else falls to `default: return 1` -> wrong net return). This is the subtle net-mode correctness item.

### `portal/src/components/ReturnVolatilityScatter.tsx`
- `ALL_PERIODS` (L48): insert `'TTW'` after `'WTD'`.
- `PERIOD_DATA_KEY` (Record<Period>, L52): add `TTW: 'TTW'`.
- Update stale header comment L8 ("8-period toggle") -> reflects added TTW.

### Page (`ModelPortfolios.tsx`)
- NO change — transform is generic over periods; TTW flows through automatically.

## Phase-3 verify (on producer deploy)
TTW cell (model/benchmark/spread) = independent `tail(10)` compound on the served daily series; spread =
model_TTW - benchmark_TTW same window; cross-check vs TO-2 surfaces; `comp-transform schema-check` clean.

## Status
Phase-0 DONE + producer spec/owner -> COO. FE leg pre-staged, **BLOCKED on AE producer TTW deploy**.
TO-1 FE-wiring leg separately HELD on DS deploy.
