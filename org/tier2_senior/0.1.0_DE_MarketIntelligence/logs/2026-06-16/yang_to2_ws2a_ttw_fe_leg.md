# YANG_SITTW TO-2 (WS-2a) — Phase-0 + TTW FE leg + AE producer escalation

**archetype:** MIXED
**secondary_archetypes:** TRACE, IMPLEMENT, COORDINATE

**Serial:** 0.1.0_DE_MarketIntelligence
**Date:** 2026-06-16 (~18:08-18:26Z)
**TO:** YANG_SITTW.TO-2 (status: pending; FE leg DONE, data leg BLOCKED on AE TO-4)

## Summary

Spawned as one of the 3 YANG_SITTW TO-leads (Andrew-direct "YANG up first"). Confirmed spawn ->
COO GO'd TO-2. Ran per-surface Phase-0, authored the additive TTW FE leg, committed to portal DEV,
and escalated the data-side producer change (AE lane) to COO, who routed it as TO-4.

**Andrew-direct mid-session (sovereign):** "I would call it TTW, not 2W." Binding label change ->
applied TTW as both user-facing label AND internal period key across both surfaces; relayed cross-pod
to TO-3 (0.4.0_DE, confirmed) + COO (formalized as binding in both TOs).

## Work done

### Phase-0 (per-surface data-vs-FE-compute fork) — BOTH surfaces = DATA-PROVIDED
- Both Market-Overview surfaces read the SAME `periodReturns` map: the 4 tab heatmaps via the shared
  `PerformanceHeatMap` (`ALL_PERIODS` columns), and Top/Bottom Performers via `ExecutiveSummary`
  (`getTop/BottomPerformer` over the same `IndexData`).
- Data path: `useMarketData -> loadMarketData -> getAllReturns()` -> tiered
  `/api/general/json-tiered/market-overview/summary/all-returns.json`.
- Served artifact inspected (`aws s3 cp s3://opal-data-portal-v2/json-tiered/market-overview/summary/all-returns.json`):
  as_of 2026-06-12, 71 indices, `period_returns` keys = `[1D,1W,1M,1Q,1Y,3Y,5Y,WTD,MTD,QTD,YTD]` —
  has a `1W` (5-session) key, NO TTW, and NO `historical_prices` in the summary payload.
- => FE-compute NOT viable (no daily series in-payload; per-ticker `timeseries/{ticker}.json` would be
  71 extra requests to build one grid column). TTW must be an ADDITIVE producer key. **Classification:
  DATA-PROVIDED, both surfaces.**

### Producer owner + the load-bearing methodology catch
- Producer = `opal-market-overview-tiered-generator` (a Lambda, python3.11) at
  `infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py`
  (identified via `pipescript market-overview`). Reads price history from DynamoDB
  `opal-portal-market-data`. **AE lane, not DS, not my DE lane (can't touch infra/aws).**
- **§5 CONFLICT:** the Lambda computes ALL period returns by CALENDAR-day arithmetic ("Yang's method";
  `PERIOD_CALENDAR_DAYS = {1W:7, 1M:30, ...}`, `calculate_period_return()` compounds over a calendar
  window). A native `TTW:14` calendar entry would VIOLATE the §5 binding (10 TRADING days). Correct =
  trading-day-counted last-10-rows path (`calculate_all_returns` L135-189). For market-overview indices
  the series is trading-days-only, so last-10-rows = 10 sessions (clean). Escalated to COO as the exact
  scoped AE ask; COO baked the trap into TO-4 verbatim and called it "the load-bearing one."

### FE leg (my lane) — committed portal DEV `27299745`
Additive TTW (label+key=TTW), slotted after WTD by horizon, renders N/A until the producer emits TTW:
- `src/lib/performanceUtils.ts` — `PeriodReturns` += optional `'TTW'`
- `src/api/endpoints/market.ts` — `TickerReturns.returns` += `TTW?`
- `src/lib/dataLoader.ts` — `transformApiToIndexData` periodReturns map += `'TTW'`
- `src/components/PerformanceHeatMap.tsx` — `ALL_PERIODS` + `PERIOD_NAMES` += TTW
- `src/components/market-performance/ExecutiveSummary.tsx` — `TIME_PERIODS` += TTW

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `pipescript market-overview` | producer/estate trace | PASS | ID'd `opal-market-overview-tiered-generator` (Lambda) + served all-returns.json path |
| `comp-transform schema-check ExecutiveSummary` | pre-change | PASS | resolved -> ExecutiveSummaryPanel: "All rendered fields match" |
| `comp-transform schema-check MarketPerformance` | pre-change | PASS | "All rendered fields match" |
| `comp-transform schema-check PerformanceHeatMap` | pre-change | N/A | "Component not found" — shared `src/components/` node not in page-scoped registry |
| `comp-transform ternary-audit ExecutiveSummary` | pre-change | PASS | "No string-literal union types... Nothing to audit" (no period ternary) |
| `comp-transform ternary-audit PerformanceHeatMap` | pre-change | N/A | "Component not found" (as above) |
| `tsc -b --noEmit --force` (portal) | post-change | PASS (exit 0) | authoritative union/Record-completeness gate: `PERIOD_NAMES` is `Record<ALL_PERIODS[number],string>` so TTW key forced; no orphan, no runtime-undefined |
| `eslint` (5 touched files) | post-change | PASS (exit 0) | only the benign pre-existing baseline-browser-mapping note |

**What worked:** `pipescript market-overview` pinned the producer + served path in one shot, exposing
that "data-side" = a Lambda (AE), not DS. The served-artifact inspection was decisive for the
data-vs-FE fork. `tsc --force` is the real union-orphan gate for the shared component.
**What failed:** nothing blocked.
**Gap found:** `comp-transform schema-check` / `ternary-audit` cannot target a shared `src/components/`
component fed via props (page-scoped registry only) — a DE editing the shared `PerformanceHeatMap` gets
no schema-check coverage; `tsc` is the fallback. Worth surfacing to compiler-tooling R&D.

## Blockers

- **BLOCKED (evidence-cited):** data leg + Phase-3 verify of TO-2 depend on
  `opal-market-overview-tiered-generator` emitting the additive TTW key — an infra/Lambda change outside
  my DE lane. Routed to AE (0.7.0_AE_CloudOps) as **TO-4** by COO (msg 182456Z). Event-driven: AE MCPs
  me when `all-returns.json` carries TTW; I then run Phase-3 + RAVC2. Not assumption-blocked — the
  served artifact proves no TTW key + no in-payload daily series.

## Current State

- **FE:** portal DEV `27299745` (on branch DEV, NOT pushed/promoted — DT is the QA gate). TTW column in
  all 4 heatmaps + TTW selectable in Top/Bottom Performers; renders "N/A" until data lands. Label+key=TTW.
- **Data:** TO-4 with 0.7.0_AE_CloudOps — producer must emit `TTW` = trailing 10 TRADING sessions
  (`latest/price_{10 rows back} - 1`), trading-day-counted (NOT `PERIOD_CALENDAR_DAYS`). Deploy-sequencing
  locked in TO-4: producer key lands before/with the FE promote (so no all-N/A column ships).
- **Cross-pod:** TO-3 (0.4.0_DE, Model Portfolios) confirmed — no shared producer/util with me; shared
  TTW definition only, formalized by COO as binding in both TOs.
- **TTW def (binding, Andrew-direct):** trailing 10 trading days, `P_latest / P_{10 sessions ago} - 1`.

## Next Steps

- [0.7.0_AE_CloudOps] TO-4: emit additive TTW key in all-returns.json (trading-day-counted); MCP me on deploy.
- [0.1.0_DE_MarketIntelligence] on AE ping: Phase-3 verify (TTW vs independent 10-session calc, cross-check vs TO-3) -> RAVC2 to COO.
- [0.1.0_DT_MarketIntelligence] (later) TO-2 FE promote `27299745` — sequence AFTER the producer TTW key is live.
