# SEAM: market-overview-tiered-generator (producer) -> all-returns.json -> FE TTW render (heatmaps + Top/Bottom)   (scale: MACRO)
**archetype:** VALIDATE
**Run:** 0.1.0_DE_MarketIntelligence, 2026-06-16 ~1831Z, YANG_SITTW.TO-2 (WS-2a)
**Ask:** Andrew /seams "make sure everything is connected correctly"

## Seam definition
The TTW (Trailing Two Weeks = trailing 10 trading sessions) data flow I built for Market Overview, decomposed into constituent seams:
- **S1 DATA leg:** `opal-market-overview-tiered-generator` (Lambda) -> served `s3://opal-data-portal-v2/json-tiered/market-overview/summary/all-returns.json` (`period_returns.TTW`).
- **S2 API contract:** `all-returns.json` -> `getAllReturns()` (market.ts) -> `TickerReturns.returns.TTW`.
- **S3 transform:** `getAllReturns` -> `transformApiToIndexData` (dataLoader.ts) -> `IndexData.periodReturns['TTW']`.
- **S4 heatmap render:** `periodReturns['TTW']` -> `PerformanceHeatMap` (`ALL_PERIODS` col + `PERIOD_NAMES` label).
- **S5 Top/Bottom render:** `periodReturns['TTW']` -> `ExecutiveSummary` (`TIME_PERIODS` selectable -> `getTop/BottomPerformer`).
- **Expected contract:** TTW return = decimal (e.g. 0.05 = 5%), trailing 10 TRADING sessions (`P_latest/P_{10 sessions ago}-1`); additive period key; label+key = `TTW` (Andrew-direct 2026-06-16, formalized binding by COO). FE renders only explicitly-listed periods.
- **Grounding:** served leg vs LIVE S3 object; FE leg vs committed code (portal DEV `27299745`, committed-NOT-promoted — DT gates the prod promote).

## Axis verdicts
| Axis | Seam | Verdict | Evidence |
|---|---|---|---|
| MECHANICAL | S1 producer->TTW key | **UNVERIFIED (by design)** | LIVE all-returns.json (as_of 2026-06-12, 71 indices) period_returns keys = [1D,1W,1M,1Q,1Y,3Y,5Y,WTD,MTD,QTD,YTD] — NO TTW yet. Routed to AE as TO-4; not a defect, the known-open leg. |
| MECHANICAL | S2 API contract | PASS | Primary path builds `returns` via `Object.fromEntries(Object.entries(item.period_returns)...)` -> carries ANY key incl TTW dynamically (market.ts:179-184). Fallback path `returns: item.returns \|\| {}` -> passthrough. `TickerReturns.returns.TTW?` typed. |
| MECHANICAL | S3 transform | PASS | dataLoader.ts: `'TTW': data.returns?.TTW?.return_pct ?? null` reads the exact key; null-coalesces when absent. |
| MECHANICAL | S4 heatmap | PASS | `ALL_PERIODS` includes 'TTW'; cell reads `periodReturns[period]`; `PERIOD_NAMES['TTW']='Trailing Two Weeks'` (header+tooltip); grid `totalColumns = 2 + periodsToShow.length` auto-accounts. tsc -b --noEmit --force exit 0. |
| MECHANICAL | S5 Top/Bottom | PASS | `TIME_PERIODS` includes 'TTW'; `getTop/BottomPerformer(...,'TTW')` reads `periodReturns['TTW']`. tsc clean. |
| MECHANICAL | blast radius | PASS | NO `Object.keys/entries/values(periodReturns)` anywhere in portal/src -> my `TTW:null` injection never surfaces unintentionally. The 5 grep co-matches are INDEPENDENT: BenchmarkHeatmap + ReturnVolatilityScatter define their OWN local `ALL_PERIODS` (`...'SI'`, no 1W); portal-proxy matched a different type (`ETFPeriodReturnsResponse`); Valuation has its own `TIME_PERIODS` shape. Change is isolated to the 2 intended surfaces. |
| DECLARATIVE | types/records vs impl | PASS (1 correction) | `PeriodReturns.TTW?`, `PERIOD_NAMES.TTW`, dataLoader map, served-key-set claim — all verified true. CORRECTION below re: "N/A-graceful". |
| SEMANTIC | units/magnitude | PASS | Served period_returns are DECIMALS (1D range -0.034..+0.051; MSCI S.Korea 1Y=2.58=+258%); FE x100 in both surfaces (`formatReturn` value*100; ExecutiveSummary `*100`). Producer `calculate_period_return` returns `cumulative-1.0` (decimal) -> TTW will match. |
| SEMANTIC | N/A-graceful (S4) | PASS | TTW null -> `formatReturn(null)='N/A'`; absoluteChange guarded -> hidden; no NaN. |
| SEMANTIC | degrade (S5) | **PARTIAL** | When ALL TTW null (missequenced window), `getTopPerformer` reduce (`\|\| -Infinity`) keeps the first element; card shows `(null\|\|0)*100` = **0.00%** (arbitrary ticker), NOT N/A. See residual. |

## Knowledge-parity delta
- **BELIEVED** (my TO-2 session log + COO msgs): "FE renders N/A-graceful until the producer emits TTW." **TRUE for the heatmap (S4)**; **imprecise for Top/Bottom (S5)** — under the missequenced window the selector shows an arbitrary performer at 0.00%, not N/A. Corrected here on the record; the producer-first deploy-sequencing (locked into TO-4 + DT-promote-ordering) is the live mitigation, so the bad window should never reach users.
- **Positive parity confirmations:** producer is a Lambda (AE), not DS; served key-set as claimed; `1W`/`3Y`/`5Y` are emitted-but-not-FE-rendered (precedent proving the FE renders ONLY explicitly-listed periods — so adding a producer key alone is insufficient AND won't leak unlisted keys).

## Verdict
- **FE-internal chain S2->S5: SOUND** — mechanically wired, declaratively consistent, semantically correct (units), isolated blast radius. The chain WILL carry TTW correctly the moment the producer emits the key, riding the identical path the 8 live periods already use (the working siblings ARE the exercise-evidence).
- **End-to-end pipeline: NOT YET SOUND — weakest-seam-binds @ S1 (UNVERIFIED-by-design).** TTW not yet emitted; gated on AE TO-4. This is expected, not a break.
- **1 semantic residual @ S5** (0.00%-not-N/A degradation in the missequenced window) — mitigated by sequencing; optional FE hardening available.

## Residual / unknowns
- **S1 not exercised on a live TTW value** — cannot verify the producer's actual TTW output until AE deploys (TO-4). Phase-3 (TTW vs independent 10-session calc, cross-check vs TO-3) is owed THEN.
- **S5 hardening (optional, my lane):** guard the Top/Bottom selector to render N/A (or hide TTW) when no ticker has a non-null value for the selected period — removes the misleading 0.00% if sequencing is ever violated. NOT done now (avoids scope creep; sequencing already controls the risk). Will add on request.
- FE is committed@DEV `27299745`, NOT promoted — no deployed-vs-committed drift to catch (simply not live yet).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| `aws s3 cp all-returns.json` (LIVE) | period-key set + units/magnitude | PASS — decimals, no TTW key, no historical_prices |
| Grep `Object.keys/entries/values(periodReturns)` | key-iteration blast | PASS — 0 matches (no unintended surfacing) |
| Grep `PeriodReturns\|ALL_PERIODS\|TIME_PERIODS\|periodReturns` repo-wide | consumer blast radius | PASS — 5 co-matches all independent symbols |
| `tsc -b --noEmit --force` (portal) | type/union integrity | PASS (exit 0) |
| Note | `comp-transform schema-check` cannot target shared `src/components/` (page-scoped registry) — tsc is the binding gate | gap (banked in TO-2 log) |
