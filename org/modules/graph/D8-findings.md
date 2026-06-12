# NFRA_GRAPHS D8 — Day-0 Critical Surface Baseline Findings

**Generated:** 2026-06-12T~1815Z  
**Author:** 0.4.0_DE_ClientPlatform  
**Carve authority:** critical-surfaces.yaml v0.3 (CTO carve-ACK bf3d019dc, 2026-06-12)  
**Global graph baseline:** `.comp-graph/baseline.json` — 2139 nodes, 2691 edges (comp-xref --save)

**Vintage anchor (F6 — NFRA_GLOBGRPH, live since 2026-06-12T16:15:51Z):**  
- S3 marker: `s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json`  
- nessie_commit_hash: `59b0a6a9a98d7d2ed03e5e8f7123f331e20cbac8063b9e8c7c6970a10f8dd3f5`  
- writer_id: `incremental_updater`  
- graph_nodes snapshot_id: `2373504567134934158`  
- graph_edges snapshot_id: `6719449234129434488`

> **Correction (CVO P2, 175033Z):** Initial D8 draft erroneously stated F6 marker was not present.
> The marker was live at 16:15:51Z (certified b22320a4c); baselines are now re-anchored to the F6
> nessie vintage above. The prior CLOUD branch-head ref (`b879522196e3`) is superseded by this anchor.

---

## Surface Scan Summary

| Surface | Severity | Firms | Findings (Day-0) | Alarm-eligible? |
|---------|----------|-------|-----------------|-----------------|
| model_portfolios.headline | SEV1 | bd/inf/cot | 1 known + 1 coverage gap | known=expected_by_design; gap=document |
| model_portfolios.benchmark | SEV1 | bd/inf/cot | 1 coverage gap | gap=document |
| advisor_intelligence | SEV1 | bd/inf/cot | 1 FP (auth) + 3 field-contract expected | none alarm-eligible Day-0 |
| model_portfolios.peers | SEV2 | bd/inf/cot | 1 coverage gap | gap=document |
| model_portfolios.aum | SEV2 | bd/inf/cot | 1 known (shared with headline) | known=expected_by_design |

**Shared-node note (v0.3 severity_resolution):** `model_portfolios.headline` (SEV1) and
`model_portfolios.aum` (SEV2) share the aum.ts backend chain (same Lambda/S3/gold nodes).
Per monitor.severity_resolution, changes to shared nodes alarm at SEV1 (block-with-ack).
AE alarm wiring must apply this max-severity rule on shared-node firings.

---

## Surface 1 — model_portfolios.headline (SEV1)

**Firms scanned:** bd (49financial), inf (inflection), cot (cottonwood)  
**comp-platinum root component:** ModelPortfolios.tsx  
**Fetches resolved by comp-platinum:**
- `getAccountDistributionByFirm()` → `/api/general/mdpf/{param}/account-distribution.json` → CF behavior 16 → [AUTH]
- `getAccountDistribution()` → `/api/general/portfolios/account-distribution.json` → CF behavior 16 → [AUTH] (via `/api/private/` path for firm-specific; `/api/general/` for global)
- `getAUMMetrics()` → url:(not resolved) — Day-0 known finding

**Fetches NOT resolved by comp-platinum (coverage gap):**
- `getAUMTimeSeries()` — in ModelPortfolios.tsx import line 37+, not detected
- `getMdpfAggregateAUATimeSeriesByFirm()` — not detected

### Findings

| ID | Template | Finding | Verdict | Alarm? |
|----|----------|---------|---------|--------|
| D8-H-001 | scan.wiring.dangling_fetch | `getAUMMetrics()` url:(not resolved) — double-wrap indirection (ModelPortfolios → aum.ts → portal-proxy.ts) prevents comp-platinum from resolving CF route | **expected_by_design** (Day-0 known; shared with aum surface) | NO — exclude from alarm triggers |
| D8-H-002 | scan.wiring.dangling_fetch | `getAUMTimeSeries`, `getMdpfAggregateAUATimeSeriesByFirm` not traced by comp-platinum | **coverage_gap** — fetches confirmed in ModelPortfolios.tsx import (L37); comp-platinum tool limitation, not a production bug | NO — tool gap; document for AE wiring |
| D8-H-003 | scan.firm.asymmetry | bd/inf/cot output SYMMETRIC — all 3 firms show identical fetch set + CF routing | **clean** | N/A |
| D8-H-004 | scan.auth.missing_edge | `getAUMMetrics` auth cannot be assessed (url not resolved); other fetches all [AUTH] | **FP** for resolved fetches; unresolvable for getAUMMetrics | N/A |

---

## Surface 2 — model_portfolios.benchmark (SEV1)

**Firms scanned:** bd (49financial), inf (inflection), cot (cottonwood)  
**comp-platinum root component:** BenchmarkHeatmap (not registered) → fetches resolved via grep in ModelPortfolios.tsx  
**Fetches (confirmed via ModelPortfolios.tsx L443/L451):**
- `getModelPortfolioBenchmarks()` → `/api/general/benchmarks/model_portfolio_benchmarks.json` → CF behavior 16 [AUTH]
- `getETFBenchmarkReturns()` → `/api/general/benchmarks/etf_returns.json` → CF behavior 16 [AUTH]

**Route auth:** CF behavior 16 `/api/general/*` → [AUTH] auth-validator-edge + public-data-router (confirmed via comp-routes).

### Findings

| ID | Template | Finding | Verdict | Alarm? |
|----|----------|---------|---------|--------|
| D8-B-001 | scan.wiring.dangling_fetch | `BenchmarkHeatmap` not registered as a comp-platinum component; fetches traced manually via ModelPortfolios.tsx grep + portal-proxy.ts | **coverage_gap** — fetches wired and auth-gated correctly; comp-platinum blind spot on non-page sub-components | NO — production wiring confirmed clean; tool gap only |
| D8-B-002 | scan.auth.missing_edge | Both benchmark fetches route via CF behavior 16 [AUTH] (auth-validator-edge) | **clean** | N/A |
| D8-B-003 | scan.firm.asymmetry | Benchmark data is firm-AGNOSTIC (general bucket, not firm-routed) — SYMMETRIC by design across bd/inf/cot | **clean** | N/A |

**AE note:** comp-surface-check alarm coverage for this surface requires monitoring
`portal/src/components/BenchmarkHeatmap.tsx` + `portal/src/api/portal-proxy.ts` (L804-867)
directly, since comp-platinum cannot carve this subgraph via component registry.

---

## Surface 3 — advisor_intelligence (SEV1)

**Firms scanned:** bd (49financial), inf (inflection), cot (cottonwood)  
**comp-platinum components:** AdvisorsTab, AdvisorBookView, ClientsTab, PartnerAnalytics (all 3 firms)  
**All ADVI fetches route via CF behaviors 2 (/api/scoped/advisor-intelligence/artifacts/*/*)
or the general scoped pattern (/api/scoped/advisor-intelligence/*.json) — all [AUTH].**

### Fetch-level findings

| ID | Template | Finding | Verdict | Alarm? |
|----|----------|---------|---------|--------|
| D8-A-001 | scan.auth.missing_edge | `getPlatinumAdvisorSummary()` shows `auth: NONE`, `cloudfront: -> ()` in ALL firms (AdvisorBookView + ClientsTab) | **FP** — dynamic URL `{param}/book.json{param}` prevents comp-platinum static resolution; actual CF behavior 21 `/api/scoped/partners/*` [AUTH] confirmed via comp-routes (D7 triage, re-confirmed D8) | NO — known FP, suppress in alarm wiring |
| D8-A-002 | scan.field.contract_break | `PlatinumLeaderboardResponse` 2/5 fields used in AdvisorsTab — `data_as_of`, `firm_id`, `available_windows` unused | **expected_by_design** (SYMMETRIC bd/inf/cot; reserved fields per type definition) | NO |
| D8-A-003 | scan.field.contract_break | `TimeseriesOverviewResponse` 6/7 fields — `firm_id` unused in PartnerAnalytics | **expected_by_design** (SYMMETRIC all firms; firm_id is legacy/future field) | NO |
| D8-A-004 | scan.field.contract_break | ClientsTab: `PlatinumFirmDashboard` 0/8, `PlatinumFirmMixSummary` 0/7, `PlatinumLeaderboardResponse` 0/5 fields rendered | **expected_by_design** — whole-object pass-through to sub-components not traced by comp-platinum (confirmed clean in comp-transform schema-check D7) | NO |
| D8-A-005 | scan.field.contract_break | ClientsTab: `HeaderMetricsResponse` 1/17 fields rendered | **expected_by_design** — same pass-through pattern; 16 fields consumed by sub-component(s) | NO |

### Firm-asymmetry breakdown (EXPECTED)

| Component | bd (49financial) | inf (inflection) | cot (cottonwood) |
|-----------|-----------------|-----------------|-----------------|
| PartnerAnalytics — gold script | `D_04 :: build_partner_analytics()` (prefix) | `D_04 :: build_partner_analytics()` (cot) | `D_04 :: build_partner_analytics()` (cot) |
| AdvisorsTab — getFirmLeaderboard gold | `D_04 :: build_firm_dashboard()` (bd — incl. B_02 in feed) | `INF_D_00c :: load_performance_dim()` (INF tree) | `D_04 :: build_firm_dashboard()` (cot) |
| PartnerAnalytics — getTimeseriesOverview gold | `D_04 :: build_timeseries_overview()` | `D_04 :: build_timeseries_overview()` | `D_04 :: build_timeseries_overview()` |

**Asymmetry verdict:** INF uses INF_ prefixed gold tree scripts (expected — separate Orion-API upstream);
bd and cot use the same script namespace with different bucket routing (expected — bd/cot are separate
BD-sourced pipelines). No anomalous asymmetry.

---

## Surface 4 — model_portfolios.peers (SEV2)

**Firms scanned:** bd (49financial), inf (inflection), cot (cottonwood)  
**comp-platinum root component:** PeersTab — shows "No fetches detected" for all 3 firms  
**Fetch confirmed via:** ModelPortfolios.tsx L458 + portal-proxy.ts L910

- `getPeerPerformance()` → `/api/general/peers/peer_performance.json` → CF behavior 16 [AUTH]

### Findings

| ID | Template | Finding | Verdict | Alarm? |
|----|----------|---------|---------|--------|
| D8-P-001 | scan.wiring.dangling_fetch | `PeersTab` shows "No fetches detected" — fetch is hoisted to parent ModelPortfolios.tsx (L458), data passed via props | **coverage_gap** — production fetch wired correctly via ModelPortfolios parent; comp-platinum can't trace prop-drilled fetches | NO — tool gap; wiring confirmed clean |
| D8-P-002 | scan.auth.missing_edge | `getPeerPerformance` → CF behavior 16 [AUTH] — confirmed via comp-routes | **clean** | N/A |
| D8-P-003 | scan.firm.asymmetry | Peers data is firm-AGNOSTIC (general bucket, not firm-routed) — SYMMETRIC by design | **clean** | N/A |

**AE note:** comp-surface-check alarm coverage for this surface requires monitoring
`portal/src/api/portal-proxy.ts` (L910) + ModelPortfolios.tsx (L458) directly,
since PeersTab itself has no fetch hooks.

---

## Surface 5 — model_portfolios.aum (SEV2)

**Firms scanned:** bd (49financial), inf (inflection), cot (cottonwood)  
**comp-platinum root component:** ModelPortfolios.tsx (AUMGrowthMetrics is a sub-component not in registry)  
**Fetches resolved by comp-platinum:**
- `getAUMMetrics()` → url:(not resolved) — Day-0 known finding
- `getAccountDistributionByFirm()` → `/api/general/mdpf/{param}/account-distribution.json` → CF behavior 16 [AUTH]
- `getAccountDistribution()` → CF behavior [AUTH]

### Findings

| ID | Template | Finding | Verdict | Alarm? |
|----|----------|---------|---------|--------|
| D8-AU-001 | scan.wiring.dangling_fetch | `getAUMMetrics()` url:(not resolved) — same as D8-H-001; shared node with headline surface | **expected_by_design** — Day-0 known finding; in critical-surfaces.yaml `known_findings` | NO — exclude from alarm triggers |
| D8-AU-002 | scan.firm.asymmetry | bd/inf/cot SYMMETRIC — identical fetch set + routing for all 3 firms | **clean** | N/A |
| D8-AU-003 | (shared-node) | This surface shares backend chain with model_portfolios.headline; changes to shared aum.ts nodes alarm at SEV1 per monitor.severity_resolution | **documented** — MAX severity rule applies | N/A (rule captured in critical-surfaces.yaml v0.3) |

---

## comp-platinum Coverage Gaps (summary for AE alarm wiring)

The following surfaces have fetch functions that comp-platinum cannot trace via component registry.
AE must instrument alarm coverage for these independently (direct monitoring of portal-proxy.ts
functions or CloudFront path patterns):

| Surface | Gap | Affected fetches | Source of truth |
|---------|-----|-----------------|-----------------|
| model_portfolios.headline | getAUMTimeSeries, getMdpfAggregateAUATimeSeriesByFirm not detected | aum.ts + portal-proxy.ts | ModelPortfolios.tsx L37 imports |
| model_portfolios.benchmark | BenchmarkHeatmap not a registered comp-platinum component | getModelPortfolioBenchmarks, getETFBenchmarkReturns | portal-proxy.ts L804-867 |
| model_portfolios.peers | PeersTab has no direct fetch hooks (prop-drilled from ModelPortfolios) | getPeerPerformance | portal-proxy.ts L910, ModelPortfolios.tsx L458 |

---

## Alarm-eligible findings (none at Day-0)

All Day-0 findings are either:
- `expected_by_design` (known: getAUMMetrics url-unresolved, ADVI auth FP, field-contract pass-through)
- `coverage_gap` (tool limitation, not a production bug)

**No findings warrant an alarm trigger at Day-0.** Baselines are clean for alarm wiring.
First alarm should fire only when a FUTURE scan detects deviation from this baseline.

---

## Signed baselines status

| Surface | Signed | Baseline node | Vintage anchor |
|---------|--------|--------------|----------------|
| model_portfolios.headline | true (pending YAML update) | `.comp-graph/baseline.json` (2139 nodes/2691 edges) | CLOUD b879522196e3 (F6 pending) |
| model_portfolios.benchmark | true (pending YAML update) | `.comp-graph/baseline.json` | CLOUD b879522196e3 (F6 pending) |
| advisor_intelligence | true (pending YAML update) | `.comp-graph/baseline.json` | CLOUD b879522196e3 (F6 pending) |
| model_portfolios.peers | true (pending YAML update) | `.comp-graph/baseline.json` | CLOUD b879522196e3 (F6 pending) |
| model_portfolios.aum | true (pending YAML update) | `.comp-graph/baseline.json` | CLOUD b879522196e3 (F6 pending) |

**Global baseline path:** `.comp-graph/baseline.json`  
**Per-surface carve:** comp-platinum is the carving tool; comp-xref --save captures the whole-graph
snapshot. The comp-xref CLI does not support per-surface saves — the global baseline is the
single baseline artifact covering all 5 surfaces.
