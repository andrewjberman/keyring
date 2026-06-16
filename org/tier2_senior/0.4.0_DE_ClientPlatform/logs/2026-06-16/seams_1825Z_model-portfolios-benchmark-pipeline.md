# SEAM: yang-model-portfolio-benchmarks pipeline -> Model Portfolios Performance tab (BenchmarkHeatmap + ReturnVolatilityScatter)  (scale: MACRO)
**archetype:** VALIDATE
**by:** 0.4.0_DE_ClientPlatform | **2026-06-16 ~1825Z** | context: YANG_SITTW.TO-3 pre-flight ("make sure everything is connected correctly")

## Seam definition
The data flow feeding TO-3's two surfaces, decomposed into constituent seams and ground-truthed against
DEPLOYED/SERVED artifacts (not source/self-report):
- **A (producer):** `yang-model-portfolio-benchmarks` Lambda (ProcessBothPKLs branch, YangDataPipeline SFN); TF `module.model_portfolio_benchmarks`.
- **served:** `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` (+ daily `model_portfolio_timeseries.json`).
- **route:** CloudFront `/api/general/benchmarks/model_portfolio_benchmarks.json` -> `getModelPortfolioBenchmarks`.
- **B (consumers):** `ModelPortfolios.tsx` page transform (L694-732) -> `<BenchmarkHeatmap>` + `<ReturnVolatilityScatter>`.
- **expected contract:** per-period `model.returns[p] = {model, index_benchmark, etf_benchmark, index_spread, etf_spread, model_volatility, index_benchmark_volatility, etf_benchmark_volatility}`; periods 1D/WTD/MTD/1M/QTD/1Q/YTD/1Y/Since Inception; values in %, spread = model - benchmark.

## Constituent seams + axis verdicts

### Seam 1 — Producer -> Served S3
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | Served object exists + FRESH: `head-object` LastModified 2026-06-15 13:20:51Z, 17481B. The fresh, correctly-shaped artifact IS the evidence the deployed producer fired + wrote. |
| DECLARATIVE | PASS | Deployed Lambda package (downloaded via `get-function` Code.Location) is byte-faithful to repo source: `periods` list L191 identical (9 periods), `calculate_period_returns` branch structure line-for-line (1D early-return + WTD/MTD/1M/QTD/1Q/YTD/1Y/SI). Committed==deployed -> my AE spec keyed to real deployed code. TTW genuinely absent (0 matches for TTW/2W/tail(10)). |
| SEMANTIC | PASS (vintage note) | 5 models x 9 periods = 45 cells; ALL have model_volatility; **0 spread-identity anomalies** (index_spread==model-index, etf_spread==model-etf, tol 0.02); **0 magnitude anomalies**. UST YTD sane (model 1.25%, idx 0.68%, etf 0.57%, vols ~1%). **VINTAGE:** data_as_of=2026-06-12 (last trading day in Yang's uploaded PKL; end_date=term_returns.index.max()), regenerated 06-15. Upload-triggered cadence (~D-1/D-2), NOT a defect — every period (and future TTW) is as-of the last Yang upload. |

### Seam 2 — Served S3 -> CloudFront/API -> Page
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | S3 key exists at the path the route maps to; object 17KB << CloudFront 10MB auto-compress cap (ContentEncoding null but size-safe -> no raw-transfer degradation). Route in live production use (existing 9-period heatmap/scatter render today) = evidence the CF edge resolves. RESIDUAL: did not curl the CF edge URL this session (origin pulled directly). |
| DECLARATIVE | PASS | Route mapping `getModelPortfolioBenchmarks -> /api/general/benchmarks/model_portfolio_benchmarks.json` confirmed (pipescript estate trace + portal-proxy.ts L804). TS `ModelPortfolioBenchmarksResponse` top-level keys match served (benign: type names `notes`, served has `model_source_note`; FE reads neither -> no break). |
| SEMANTIC | PASS | Same payload as Seam 1. |

### Seam 3 — Page transform -> BenchmarkHeatmap + ReturnVolatilityScatter
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | Transform (ModelPortfolios.tsx L700-724) reads exactly the fields present in the served data (all 45 cells populated); selects index-vs-etf by `benchmarkType` (default 'etf'); is generic over periods (`Object.entries(model.returns)`). Both components read resolved `data.returns[PERIOD_DATA_KEY].{model,benchmark,spread,model_volatility,benchmark_volatility}`. |
| DECLARATIVE | PASS | Component `BenchmarkModelData` type matches transform output; every PERIOD_DATA_KEY the components map (SI->'Since Inception', rest identity) exists in the served period set. |
| SEMANTIC | PASS | index/etf selection correct (spread identities hold for BOTH benchmark modes in served data); volatility carried through for the scatter. |

## Phase-0 load-bearing premise — VERIFIED against live data
`model_portfolio_timeseries.json` (daily) carries **exactly ONE** `benchmark_return` per (date, model_code) — fields {date, model_code, model_return, benchmark_return, rfr}; 2770 pts = 554 dates (2024-04-30 -> 2026-06-12) x 5 models. => FE can compute at most ONE benchmark mode's TTW; the heatmap/scatter need BOTH index + ETF -> **data-side verdict holds.** TTW `tail(10)` dry-run sound (INT 06-01->06-12 compounds to -0.21%).

## Knowledge-parity delta
None found — believed chain == true chain on all axes. Producer committed==deployed (no source-vs-deployed drift). One property made explicit (not previously recorded at the seam): the served data is **as-of the last Yang upload (06-12), upload-triggered**, not same-day — so TTW, like every period, ends at data_as_of.

## Verdict
**SOUND** (all 3 axes PASS on every constituent seam). The existing Model-Portfolios benchmark chain carries the right shape + correct, fresh-to-upload values from deployed Lambda through to both TO-3 components. The TTW work is cleanly ADDITIVE onto a sound chain; the one coordination risk (producer-emitted key name) is closed — binding key = `'TTW'` in AE TO-4 + FE PERIOD_DATA_KEY['TTW']='TTW'.

## Residual / unknowns
- CF edge URL not curled this session (origin pulled directly; route evidenced by live prod render). Low risk.
- TTW seam itself is FORWARD-LOOKING: will be re-verified (Seam 1 SEMANTIC = independent tail(10) parity; Seam 3 = schema-check) when AE TO-4 deploys the TTW key — the Phase-3 acceptance.

## Compiler Tools
| Run | Result |
|---|---|
| `comp-transform schema-check BenchmarkHeatmap / ReturnVolatilityScatter` | Component not found (presentational/prop-consuming, not fetch-bound) -> redirected to `ModelPortfolios` |
| `comp-transform schema-check ModelPortfolios` | WARN no co-located types.ts (types in @/api/portal-proxy.ts) — non-blocking |
| `comp-transform ternary-audit ModelPortfolios` | union=TabType only; the period switch lives in the components, not the page |
| `pipescript model-portfolios` | confirmed producer (yang-model-portfolio-benchmarks ProcessBothPKLs) -> 3 served JSON -> getModelPortfolioBenchmarks; reachable [CVO ground-truth] |
| `aws s3api head-object` / `s3 cp` (x2) | served artifacts fresh 2026-06-15 13:20:51Z; pulled for content checks |
| `aws lambda get-function` + unzip + grep | deployed==committed; TTW absent (0 matches) |
| python parity/structure/magnitude scan | 45/45 cells; 0 spread anomalies; 0 magnitude anomalies; single benchmark_return premise confirmed |
