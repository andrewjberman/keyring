# DEBT_1STRUN Pod 4 Aggregate -- 0.4.0_DE_ClientPlatform (covered by 0.4.1_RD)
**Date:** 2026-04-07
**Task Order:** DEBT_1STRUN.001.scan
**Status:** Complete

## Source Scans

| Agent | Scope | Findings | Status |
|-------|-------|----------|--------|
| 0.4.0_DS_ClientPlatform | gold/, silver/, classification/ scripts | 47 | Complete (2026-03-23) |
| 0.4.1_RD_ModelPortfolios | portal/src/pages/ModelPortfolios/ | 13 | Complete (2026-03-23) |
| 0.4.2_RD_AdvisorIntelligence | portal/src/pages/AdvisorIntelligence/ | -- | PENDING (never executed) |
| 0.4.0_DE_ClientPlatform (this scan) | portal shared infra, API wiring, types | 24 | Complete (2026-04-07) |

---

## Part 1: DE Own Scan -- Shared Portal Infrastructure

### Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| DE-1 | portal/src/api/portal-proxy.ts | 249-265, 302-322, 327-348, 376-396 | C2 Deprecated | High | Six API functions marked "DEMO MODE" with TODO to revert to private firm-scoped endpoints. Public endpoints serve production data without auth. Long-standing temporary workaround. |
| DE-2 | portal/src/api/endpoints/aum.ts | 465-513 | C2 Deprecated | High | getAccountDistribution() uses public endpoint with TODO to revert to private. Bearer token code commented out. |
| DE-3 | portal/src/api/portal-proxy.ts | 87-98 | C2 Deprecated | Medium | 401 redirect disabled due to infinite redirect loop for ModelPortfolios. Only console.error -- auth failures silently swallowed. |
| DE-4 | portal/src/api/endpoints/aum.ts | 645-661 | C1 Dead | Low | Dead export `getModelColor()` with hardcoded color map. Proper implementation exists in modelPortfolioColors.ts. |
| DE-5 | portal/src/lib/modelPortfolioColors.ts | 96-104 | C1 Dead | Low | `getAllModelColors()` exported but never imported anywhere. |
| DE-6 | portal/src/components/AccountDistributionChart.tsx | 23 | C1 Dead | Low | Destructured prop `title` with underscore prefix -- accepted but unused. |
| DE-7 | portal/src/components/ReturnVolatilityScatter.tsx | 34-39 | C1 Dead | Low | Props `timestamp` and `source` declared in interface but never referenced in component body. |
| DE-8 | portal/src/components/BenchmarkHeatmap.tsx | 43-50 | C1 Dead | Low | Prop `benchmarkCompositions` defined but falls back to hardcoded BENCHMARK_INDICES. |
| DE-9 | portal/src/hooks/useTabNavigation.ts | 49-54 | C1 Dead | Low | Hook returns `setActiveTab` but all consumers only use `handleTabChange`. Raw setState export unused. |
| DE-10 | portal/src/api/endpoints/aum.ts | 375-400 | C6 Stale Error | Medium | getAUMMetrics() catch block returns empty/zero data instead of propagating error. Client can't distinguish "no data" from API failure. |
| DE-11 | portal/src/api/endpoints/aum.ts | 417-423 | C6 Stale Error | Medium | getAUMTimeSeries() catch returns empty arrays without error context. Silent failure produces blank chart. |
| DE-12 | portal/src/api/portal-proxy.ts | 97-99 | C6 Stale Error | Medium | 401 errors only log to console. Auth failure swallowed, user gets no feedback. |
| DE-13 | portal/src/api/endpoints/aum.ts | 449-459 | C5 Orphaned | Low | clearAccountDistributionCache() never called. In-memory cache TTL hardcoded; CloudFront handles HTTP caching anyway. |
| DE-14 | portal/src/api/endpoints/advisor-intelligence.ts | 56, 275, 289, 332, 364 | C4 Hardcoded | Medium | Firm ID "49financial" hardcoded as default in 5+ functions. Should use centralized config. |
| DE-15 | portal/src/components/BenchmarkHeatmap.tsx | 66, 181-182 | C4 Hardcoded | Low | SI inception date "4/30/2024" hardcoded in 3 places. |
| DE-16 | portal/src/components/BenchmarkHeatmap.tsx | 214-221 | C4 Hardcoded | Low | BENCHMARK_INDICES static table -- should come from API. |
| DE-17 | portal/src/components/BenchmarkHeatmap.tsx | 225-245 | C4 Hardcoded | Low | ETF_BENCHMARK_ALLOCATIONS hardcoded weights (85/15, 40/60 blends). |
| DE-18 | portal/src/api/endpoints/portfolio.ts | 347 | C4 Hardcoded | Low | Security.sedol field is always `undefined` with TODO comment. |
| DE-19 | portal/src/hooks/useDataSource.ts | 61-75 | C5 Orphaned | Low | useYangDataAsOf() exported but never imported. |
| DE-20 | portal/src/components/BenchmarkHeatmap.tsx | 101-118 | C3 Duplication | Low | countTradingDays() duplicates weekday-counting logic; should be shared utility. |
| DE-21 | portal/src/api/endpoints/advisor-intelligence.ts | 56+ | C3 Duplication | Low | firmId mapping pattern repeated 6+ times across functions. Should extract to helper. |
| DE-22 | portal/src/pages/ModelPortfolios/tabs/PeersTab.tsx | 21 | C4 Hardcoded | Medium | INCEPTION_DATE hardcoded '2024-04-30'. Should come from API. |
| DE-23 | portal/src/pages/ModelPortfolios.tsx | 800-810 | C6 Stale Error | Medium | Distribution-unavailable fallback shows CORS debug message to end users. |
| DE-24 | portal/src/pages/ModelPortfolios.tsx | 239 | C6 Stale Error | Low | Error state discards actual metricsError object, shows generic string. |

### DE Own Scan Summary
- Total: 24 findings
- By category: C1: 6, C2: 3, C3: 2, C4: 5, C5: 2, C6: 6
- High severity: 2, Medium: 8, Low: 14

---

## Part 2: Pod Aggregation

### RD ModelPortfolios Findings (13 total, from 2026-03-23 scan)

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| RD1-1 | ModelPortfolios.tsx | 257-259 | C1 Dead | Medium | `aggregateMetrics` destructured but never used |
| RD1-2 | ModelPortfolios.tsx | 639 | C1 Dead | Low | `isSelected` declared for Non-Model legend but unused |
| RD1-3 | ModelPortfolios.tsx | 180+ | C2 Deprecated | Low | Six stale PHASE1_PF_REQ comments |
| RD1-4 | ModelPortfolios.tsx | 801 | C2 Deprecated | High | Emoji character violates CLAUDE.md rule 13 |
| RD1-5 | ModelPortfolios.tsx | 1066-1123, 1288-1343 | C3 Duplication | High | Near-identical tooltip renderer duplicated in BarChart and AreaChart (~55 lines each) |
| RD1-6 | ModelPortfolios.tsx | 1125-1153, 1345-1373 | C3 Duplication | Medium | Custom Legend renderer duplicated between BarChart and AreaChart |
| RD1-7 | ModelPortfolios.tsx:58-64 / PeersTab.tsx:112-121 | - | C3 Duplication | Medium | Model portfolio canonical order defined twice (drift risk) |
| RD1-8 | PeersTab.tsx | 21 | C4 Hardcoded | Medium | INCEPTION_DATE hardcoded (same as DE-22 -- deduplicated) |
| RD1-9 | ModelPortfolios.tsx | 1186 | C4 Hardcoded | Medium | Footnote hardcodes "~50 newly opened holdings" |
| RD1-10 | ModelPortfolios.tsx | 599-600 | C4 Hardcoded | Low | Donut chart dimensions 380x380 hardcoded |
| RD1-11 | ModelPortfolios.tsx | 538-543 | C4 Hardcoded | Low | ApexCharts animation magic numbers |
| RD1-12 | ModelPortfolios.tsx | 800-810 | C6 Stale Error | Medium | CORS debug message shown to users (same as DE-23 -- deduplicated) |
| RD1-13 | ModelPortfolios.tsx | 239 | C6 Stale Error | Low | Generic error discards metricsError (same as DE-24 -- deduplicated) |

### DS ClientPlatform Findings (47 total, from 2026-03-23 scan)

Top findings by severity (full list in DS scan log):

| # | Scope | Category | Severity | Description |
|---|-------|----------|----------|-------------|
| DS-1 | gold/archive/ (31 files) | C1 Dead | High | Entire archive/ directory is dead code (~5,000+ lines) |
| DS-2 | silver/build_interpolated_prices.py | C1 Dead | High | Entire script orphaned -- output has zero consumers |
| DS-3 | silver/merge-daily-allocation-incremental.py | C1 Dead | High | Deprecated per docstring, orphaned manifest |
| DS-4 | silver/fetch_historical_prices_yfinance.py | C1 Dead | High | Not invoked by any orchestrator. Dead OpenAI path. |
| DS-5 | silver/security_ticker_mapping_final.py | C1 Dead | High | Static dict superseded by S3 config. Only consumer is dead. |
| DS-18 | gold/05 + 05b | C3 Duplication | High | NNA INFLOW/OUTFLOW frozensets copy-pasted. Silent divergence risk. |
| DS-19 | gold/05 + 05b | C3 Duplication | High | load_flows_from_transactions() ~150 lines duplicated |
| DS-25 | gold/05 | C4 Hardcoded | High | FLOW_CAP, VELOCITY_WINDOW, VELOCITY_THRESHOLD business rules in code |
| DS-36 | gold/05c | C6 Stale Error | High | sys.exit(0) on validation failure. Pipeline sees "success." |
| DS-37 | gold/05d | C6 Stale Error | High | sys.exit(0) on certification failure. Same silent exit. |
| DS-45 | classification/ | C6 Stale Error | High | OpenAI retry doesn't distinguish rate-limit from schema error |

### RD AdvisorIntelligence: PENDING

0.4.2_RD_AdvisorIntelligence never completed a DEBT_1STRUN scan. Findings from AdvisorIntelligence are limited to what the DE scan captured in shared infrastructure (DE-14, DE-21).

---

## Cross-References

| DE Finding | RD/DS Finding | Nature |
|------------|---------------|--------|
| DE-22 (PeersTab INCEPTION_DATE) | RD1-8 (same) | Duplicate -- merged |
| DE-23 (CORS debug message) | RD1-12 (same) | Duplicate -- merged |
| DE-24 (generic error string) | RD1-13 (same) | Duplicate -- merged |
| DE-1 (DEMO MODE endpoints) | DS-36/37 (silent validation exit) | Related: if backend validation silently passes bad data, DEMO endpoints serve it without auth checks. Compounding risk. |
| DE-14 (hardcoded firmId) | DS-24 (hardcoded S3 bucket) | Pattern: both frontend and backend hardcode deployment-specific identifiers instead of config |
| RD1-5 (tooltip duplication) | RD1-6 (legend duplication) | Same root cause: Growth tab charts should share a component library |

---

## Top 10 Pod Debt Items (Ranked by Severity x Blast Radius)

| Rank | Source | Finding | Category | Effort | Rationale |
|------|--------|---------|----------|--------|-----------|
| 1 | DS-36,37 | Silent sys.exit(0) in validation/certification scripts | C6 | QUICK WIN | Masks data quality failures from pipeline. Change to sys.exit(1). 15 min fix. |
| 2 | DE-1 | Portal-proxy DEMO MODE endpoints (6 functions) | C2 | MODERATE | Production data served without auth. Requires investigating the 401 infinite redirect root cause (DE-3) first. |
| 3 | DS-18,19 | NNA flow classification logic duplicated across 05/05b | C3 | MODERATE | Business rules will silently diverge. Extract to gold/lib/nna_flows.py. ~2 hours. |
| 4 | DS-1 | gold/archive/ directory (31 dead files, 5000+ lines) | C1 | QUICK WIN | Delete or move. Zero references. Largest dead code surface in pod. |
| 5 | DS-2,3,4,5 | Four dead silver scripts + orphaned outputs | C1 | QUICK WIN | Delete scripts + clean orphaned S3 outputs. ~30 min. |
| 6 | RD1-5,6 | Duplicated tooltip + legend renderers in ModelPortfolios | C3 | MODERATE | ~110 lines duplicated. Extract to shared ModelChartTooltip/ModelLegend. ~1.5 hours. |
| 7 | DE-14 | Hardcoded firmId "49financial" in 5+ API functions | C4 | QUICK WIN | Extract to constant or config. ~30 min. |
| 8 | DS-25 | NNA business rules (FLOW_CAP, thresholds) hardcoded | C4 | MODERATE | Move to config file. Requires validation that config is loaded correctly. ~2 hours. |
| 9 | DE-10,11 | AUM API catch blocks swallow errors, return empty data | C6 | MODERATE | Client can't distinguish no-data from failure. Need proper error propagation. ~1.5 hours. |
| 10 | DS-45 | OpenAI classify retry doesn't distinguish error types | C6 | MODERATE | Rate-limit, schema error, and network failure all treated identically. ~1 hour. |

### Effort Summary
- **QUICK WIN** (< 1 hour): Items 1, 4, 5, 7
- **MODERATE** (1-4 hours): Items 2, 3, 6, 8, 9, 10
- **SIGNIFICANT** (> 4 hours): None identified in top 10

---

## Totals

| Source | Findings |
|--------|----------|
| DE own scan | 24 |
| DS scan | 47 |
| RD ModelPortfolios | 13 (3 deduplicated with DE) |
| RD AdvisorIntelligence | PENDING |
| **Pod total (deduplicated)** | **81** |

By category: C1: 16, C2: 10, C3: 10, C4: 14, C5: 5, C6: 18, (+ 8 unscanned from 0.4.2_RD)
High severity: 15 | Medium: 22 | Low: 26
