# YANG_SITTW — TO-3 Phase-0 + seams (chain SOUND) + TO-1 FE leg (b) shipped
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE
**agent:** 0.4.0_DE_ClientPlatform · **2026-06-16** · window: session start (~1809Z) -> ~1900Z

## Current State

Spawned into YANG_SITTW (Andrew-direct "YANG up first"). Startup clean: registered LIVE (PID 30808),
persistent inbox Monitor `bb49ssf73`, 0 crons (event-driven). Two TOs: TO-3 (WS-2b lead) + TO-1 (FE-wiring co-assignee).

### TO-3 (WS-2b) — Phase-0 DONE, FE pre-staged, BLOCKED on AE producer
- **Phase-0 verdict: BOTH surfaces (ReturnVolatilityScatter + BenchmarkHeatmap) = DATA-SIDE.** Both
  consume one `BenchmarkModelData[]` built by ModelPortfolios.tsx (generic over periods) from
  model_portfolio_benchmarks.json (model + index + ETF return/vol/spread per period; default mode ETF).
  Verified vs live data: model_portfolio_timeseries.json has ONE benchmark_return per (date,model) ->
  FE can't serve both index+ETF TTW; scatter vol is producer-computed -> FE-replication inconsistent.
- **Producer = `yang-model-portfolio-benchmarks` Lambda** (ProcessBothPKLs; TF module.model_portfolio_benchmarks),
  AE/Yang-pipeline lane (NOT DS). ~2-line additive change: L191 periods append 'TTW' + `elif period=='TTW': series.tail(10)`.
  Label = `TTW` (Andrew-direct, supersedes "2W"; binding cross-pod w/ TO-2). COO routed TO-4 to 0.7.0_AE_CloudOps.
- FE pre-staged (add TTW to ALL_PERIODS/PERIOD_NAMES/PERIOD_DATA_KEY in both components + FIXED_PERIOD_TRADING_DAYS['TTW']=10
  for net-mode). HOLD commit until producer emits the TTW key, then land + Phase-3 verify. Doc:
  `logs/2026-06-16/yang_to3_phase0_and_fe_staging.md`.

### /seams — TO-3 benchmark chain = SOUND (all 3 axes, ground-truthed)
Record: `logs/2026-06-16/seams_1825Z_model-portfolios-benchmark-pipeline.md` (commit dde8f1259, pushed b2cd5138d).
Producer committed==DEPLOYED (live Lambda pkg byte-faithful; TTW absent); served mpb.json fresh + 0 spread/magnitude
anomalies (45/45 cells); single-benchmark timeseries premise confirmed. Vintage note: data_as_of=2026-06-12
(upload-triggered cadence).

### TO-1 FE leg (b) — COMPLETE (portal DEV a447712b)
Wired vs DEPLOYED DS shape (served aggregate-aua-timeseries.json 2026-06-16 18:37Z: sma_aua ABSENT, floor 2024-11-01).
- **Global since-inception x-axis:** growth-tab rolling-1y filter gated OFF for Global (isGlobalSI); data already
  loaded to 2024-11-01 via globalMdpfData (413 dates). Per-firm rolling-1y UNCHANGED.
- **Estimate-tail demarcation:** ReferenceArea (pre-2026-01-16, MDPF_ESTIMATE_BASIS_END) on BOTH BarChart +
  AreaChart (Global-gated) + disclosure footnote + SI helptip. Estimate never renders as measured.
- **sma_aua cleanup:** optional in 3 portal-proxy types; dropped 2 redundant +sma_aua folds (L831/L893,
  value-preserving — non_model_aua now carries SMA). cohort_class==='sma' by_model filters retained.
- tsc -b --noEmit --force EXIT 0. RAVC2 -> COO; CC DS~A. Joint TO-1 close = DS/COO call.

## Blockers
- **TO-3 FE leg: BLOCKED on AE TO-4** (0.7.0_AE_CloudOps) deploying the additive TTW period key to
  model_portfolio_benchmarks.json. Evidence: deployed Lambda confirmed TTW-absent (0 matches in live pkg);
  FE land+Phase-3-verify fires on AE's deploy signal. Not assumption-blocked — the producer change is GO'd + routed.

## MCP traffic
~12 messages. Significant: COO [GO] TO-3 (181129Z) + [GO] TO-1 FE leg (184355Z); COO routed TO-4 to AE (182503Z);
TO-2 DE (0.1.0) cross-pod TTW-label align (confirmed TTW). RAVC2 TO-1 FE -> COO (185917Z). Phase-0 report + spawn-confirm -> COO.

## Compiler Tools
| Run | Result | Note |
|---|---|---|
| comp-transform schema-check BenchmarkHeatmap / ReturnVolatilityScatter | N/A | "Component not found" — presentational/prop-consuming; redirected to the page |
| comp-transform schema-check ModelPortfolios | WARN | no co-located types.ts (types in portal-proxy.ts) — reconciled type manually; tsc is the binding gate |
| comp-transform ternary-audit ModelPortfolios | PASS | union=TabType only; period switch is in the components, not the page |
| pipescript model-portfolios | PASS | confirmed producer (yang-model-portfolio-benchmarks ProcessBothPKLs) -> 3 served JSON -> getModelPortfolioBenchmarks; reachable |
| comp-pipescript io yang-model-portfolio-benchmarks | N/A | out-of-scope (globgrph/none, not medallion) — expected; used pipescript instead |
| safe-commit surface-check (TO-1 commit) | WARN (advisory) | SEV1 model_portfolios.benchmark + .headline touched; VALUE-SAFE (no computation changed); advisory ramp not flipped |
| tsc -b --noEmit --force (portal) | PASS | exit 0 — the binding type gate for the TO-1 FE change |

**What worked:** pipescript estate trace + deployed-Lambda pull nailed the Phase-0 owner (AE not DS) + committed==deployed.
Ground-truthing the served artifacts (aws s3 pull + python parity) made both Phase-0 and the TO-1 wiring unambiguous.
**What failed:** comp-transform schema-check can't resolve ModelPortfolios types (portal-proxy.ts location) — WARN-only; tsc covers it.
**Gap:** comp-transform schema-check on presentational/prop-consuming components returns "not found" (only fetch-bound
components are in the graph) — a coverage gap for prop-drilled chart components.

## Next Steps
- [0.7.0_AE_CloudOps] deploy TO-4 (additive TTW key) -> signal me; I land TO-3 FE + Phase-3 verify same-turn.
- [2.0.0_SA_COO / 0.4.0_DS_ClientPlatform~A] joint TO-1 close (leg a deployed+co-signed; leg b landed a447712b).
- [0.4.0_DE_ClientPlatform] TO-3 FE land+verify on AE signal. Visual smoke of TO-1 demarcation deferred to DT-promote/Andrew.
