# ADVI_49PUSH Phase 2: Master Platinum File Catalog

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-08
**Task Order:** ADVI_49PUSH.007
**Status:** Complete
**Sources:** P1 PRD, P2 briefs 2.1/2.2 (~B), 2.3 (~C), 2.4 (~D), cross-surface matrix (~D)

---

## 1. Master Catalog

### Firm-Level Files (`platinum/firm/`)

| # | Path | Count | Est. Size | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|---|------|-------|-----------|----------|-------------|-----------|--------------|-------|--------|
| F1 | `platinum/firm/dashboard.json` | 1 | ~80-150KB | D_04 | D_00 `clients_tab.json` (headline), D_00 `employee_leaderboard.json` (entries), C_08 `advisor_fee_efficiency.json` (scatter) | Books N1: headline metrics, clients dropdown, fee efficiency scatter | Books N1 | P1 | DELIVERED |
| F2 | `platinum/firm/mix_summary.json` | 1 | ~5KB | D_04 | D_03 `firm_mix_views.json` (quarterly/monthly bars), D_03 composition (mix pie + concentration) | Books N1: mix pie, quarterly bars, concentration panel | Books N1 | P1 | DELIVERED |
| F3 | `platinum/firm/timeseries_overview.json` | 1 | ~20KB | D_04+ | D_00 `timeseries_chart.json` (aua, nna, growth_decomposition -- pre-aggregated by period), D_03 `firm_mix_views.json` (mix bars) | PartnerAnalytics header: AUA/NNA/GRO/Mix bar charts | PartnerAnalytics header | P3 | DESIGNED |
| F4a | `platinum/firm/partner_analytics_quarterly.json` | 1 | ~100KB | D_04+ | D_01 `header_metrics_quarterly.json` (5 views x 4 periods: donut + distribution + metrics) | DistributionTab snapshot mode (quarterly granularity) | DistributionTab + PartnerAnalytics (pass-through) | P3 | DESIGNED |
| F4b | `platinum/firm/partner_analytics_monthly.json` | 1 | ~100KB | D_04+ | D_01 `header_metrics_monthly.json` | DistributionTab snapshot mode (monthly granularity) | DistributionTab + PartnerAnalytics (pass-through) | P3 | DESIGNED |
| F4c | `platinum/firm/partner_analytics_annual.json` | 1 | ~80KB | D_04+ | D_01 `header_metrics_annual.json` | DistributionTab snapshot mode (annual granularity) | DistributionTab + PartnerAnalytics (pass-through) | P3 | DESIGNED |
| F5 | `platinum/firm/cumulative_chart.json` | 1 | ~150-250KB | D_04+ | D_00 `timeseries_chart.json` (geo, adv, nna_geo, nna_adv, geo_drill, adv_drill, nna_geo_drill -- weekly-sampled) | DistributionTab continuous mode: stacked area, NNA diverging bar | DistributionTab | P3 | DESIGNED |
| F6 | `platinum/firm/leaderboard.json` | 1 | ~12-15KB | D_04+ | D_00 `employee_leaderboard.json` (entries -- QTD/YTD windows only, stripped of fee/efficiency fields) | Advisors tab: top 3 hero, bar charts, card list, role filter | Advisors tab | P3 | DESIGNED |

### Advisor-Level Files (`platinum/advisors/{id}/`)

| # | Path | Count | Est. Size | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|---|------|-------|-----------|----------|-------------|-----------|--------------|-------|--------|
| A1 | `platinum/advisors/{id}/summary.json` | ~20 | ~10-20KB ea | D_04 | D_02 `book.json` (clients, AUA, NNA, fee_summary.by_role), D_03 (mix snapshot, quarterly bars, composition), C_08 (fee role breakdown) | Books L2: advisor book detail, mix, composition, fee role donut, client drilldown | Books L2 | P1 | DELIVERED |

**P3 extension:** Add `implied_revenue` + `fee_yield_bps` to each client entry in `book.clients[]` (~D finding, ~800 bytes per advisor).

### Client-Level Files (`platinum/clients/{rel_id}/`)

| # | Path | Count | Est. Size | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|---|------|-------|-----------|----------|-------------|-----------|--------------|-------|--------|
| C1 | `platinum/clients/{rel_id}/summary.json` | ~600 | ~2-5KB ea | D_04 | D_02 `detail.json` (accounts, AUA, tax, engagement), D_03 (mix snapshot, quarterly bars, composition), C_06 (90d decomposition), A_02 (fee_summary) | Books L3: client detail, mix, composition, fee summary, tax | Books L3 | P1 | DELIVERED |
| C2 | `platinum/clients/{rel_id}/mix_timeseries.json` | ~600 | ~5-20KB ea | D_04 | C_06 `{rel_id}.json` (mix[] daily) | Books L3 detail: MixTimeseriesPanel | Books L3 detail | P1 | DELIVERED |
| C3 | `platinum/clients/{rel_id}/concentration.json` | ~600 | ~5-15KB ea | D_04 | C_06 `{rel_id}.json` (concentration) | Books L3 detail: ConcentrationPanel | Books L3 detail | P1 | DELIVERED |

**P3 extension:** Add `revenue_and_tax` section to C1 (~D finding). Fields: `annual_implied_revenue`, `fee_yield_bps`, `cost_basis.{total_cost_basis, total_market_value, total_unrealized_gain, short_term.*, long_term.*, tax_efficiency_ratio}`, `top_positions[]`. Gold sources: C_05 `client_tax_liability.parquet`, D_02 `detail.json` fee_summary. ~200-300 bytes per client.

### Account-Level Files (`platinum/accounts/{acct_id}/`)

| # | Path | Count | Est. Size | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|---|------|-------|-----------|----------|-------------|-----------|--------------|-------|--------|
| X1 | `platinum/accounts/{acct_id}/summary.json` | ~3,500 | ~1-2KB ea | D_04 | B_01 `holdings_lots/{date}.parquet` (composition), accounts_dimension (metadata) | Books L4: account composition | Books L4 | P1 | DELIVERED |

---

## 2. Catalog Summary

| Category | File Count | Total Size | Phase |
|----------|-----------|-----------|-------|
| **Firm-level (DELIVERED)** | 2 | ~85-155KB | P1 |
| **Firm-level (DESIGNED)** | 6 | ~462-565KB | P3 |
| **Advisor-level** | ~20 | ~200-400KB | P1 (+ P3 extension) |
| **Client-level** | ~1,800 | ~7-24MB | P1 (+ P3 extension) |
| **Account-level** | ~3,500 | ~3.5-7MB | P1 |
| **TOTAL** | **~5,328** | **~11-32MB** | |

### New P3 Firm Files

| File | Replaces Gold Artifact | Size Reduction |
|------|----------------------|----------------|
| `timeseries_overview.json` (20KB) | Partial replacement of `timeseries_chart.json` (~800KB-1MB) + eliminates `firm_mix_views.json` Lambda hop | ~98% for this slice |
| `partner_analytics_{gran}.json` (3 x ~100KB) | Direct replacement of `header_metrics_{gran}.json` (3 x ~120KB) | ~17% (waste stripping) |
| `cumulative_chart.json` (~200KB) | Partial replacement of `timeseries_chart.json` (weekly-sampled vs daily) | ~75% for this slice |
| `leaderboard.json` (~15KB) | Replacement of `employee_leaderboard.json` (681KB) for Advisors tab | ~98% |

**Net gold-to-platinum reduction for P3 firm files:** ~1.95MB gold -> ~535KB platinum (**~73% reduction**)

---

## 3. Cross-Surface Sharing Annotations

### F1: `platinum/firm/dashboard.json` (P1)

| Section | Fields Used | Consumer Surface |
|---------|------------|-----------------|
| `headline.total_aua` | Firm AUA headline | Books N1 |
| `headline.client_count` | Client count | Books N1 |
| `headline.account_count` | Account count | Books N1 |
| `employee_leaderboard[]` | All entries (full windows) | Books N1 (if leaderboard shown at N1) |
| `fee_efficiency.advisors[]` | Scatter dots: aua, nna, commission, efficiency_pctile | Books N1 FeeEfficiencyPanel |
| `fee_efficiency.regression` | NOT used (client-side regression) | -- |

**NOT consumed by:** Advisors tab (uses separate leaderboard.json), PartnerAnalytics header (uses timeseries_overview.json), Distribution tab.

### F3: `platinum/firm/timeseries_overview.json` (P3)

| Section | Fields Used | Consumer Surface |
|---------|------------|-----------------|
| `aua.{gran}.data[].NMNC/NMEC` | Stacked bar chart (AUA Clients sub-mode) | PartnerAnalytics header |
| `nna.{gran}[].inflow/outflow/net` | Diverging bar chart (NNA mode) | PartnerAnalytics header |
| `growth_decomposition.{gran}[]` | Stacked bar chart (GRO mode) | PartnerAnalytics header |
| `mix.{gran}[]` | Stacked bar chart (AUA Mix sub-mode) | PartnerAnalytics header |

**NOT consumed by:** Distribution tab (uses F4/F5), Advisors tab, Books tab.

### F4a-c: `platinum/firm/partner_analytics_{gran}.json` (P3)

| Section | Fields Used | Consumer Surface |
|---------|------------|-----------------|
| `views.{aua\|nna\|geo\|adv}.current.donut` | ApexCharts donut + legend | DistributionTab snapshot |
| `views.{geo\|adv}.current.distribution` | Bell curve histogram + P10-P90 markers | DistributionTab snapshot |
| `views.*.{current\|q1\|q2\|q3}.donut/distribution` | Time machine period comparison | DistributionTab snapshot |
| `views.{geo\|adv}.current.donut.segments[].cities/clients` | Drill-down nested segments | DistributionTab snapshot drill |
| `views.*.metrics.client_count` | Passed to continuous view as totalClients | DistributionTab continuous |

**NOT consumed by:** PartnerAnalytics header (does NOT render D_01 data -- key ~B finding).

### F5: `platinum/firm/cumulative_chart.json` (P3)

| Section | Fields Used | Consumer Surface |
|---------|------------|-----------------|
| `geo.data[]` | Stacked area chart (AUA by state) | DistributionTab continuous |
| `adv.data[]` | Stacked area chart (AUA by architect) | DistributionTab continuous |
| `nna_geo.data[]` | NNA diverging bar (by state) | DistributionTab continuous NNA |
| `nna_adv.data[]` | NNA diverging bar (by architect) | DistributionTab continuous NNA |
| `geo_drill.{state}` | City-level drill | DistributionTab continuous drill |
| `adv_drill.{adv}` | Client-level drill | DistributionTab continuous drill |
| `nna_geo_drill.{state}` | City-level NNA drill | DistributionTab continuous NNA drill |

**NOT consumed by:** PartnerAnalytics header (uses F3), Advisors tab, Books tab.

### F6: `platinum/firm/leaderboard.json` (P3)

| Section | Fields Used | Consumer Surface |
|---------|------------|-----------------|
| `windows.{QTD\|YTD}.entries[]` | Top 3 hero, bar charts (top 10), card list (paginated) | Advisors tab |
| `windows.{w}.entries[].role_breakdown` | Role filter checkbox logic | Advisors tab |
| `windows.{w}.entries[].inflows/outflows` | NNA diverging bar | Advisors tab NNA mode |
| `windows.{w}.summary` | Aggregate totals | Advisors tab |

**NOT consumed by:** Books N1 (uses dashboard.json), PartnerAnalytics, Distribution tab.

---

## 4. Divergence Resolution Table

| # | Metric | Surfaces Affected | Current Gold Sources (Divergent) | Canonical Platinum Source (Resolved) | Resolution Mechanism |
|---|--------|-------------------|--------------------------------|-------------------------------------|---------------------|
| D1 | **Advisor AUA (managed vs book)** | Advisors leaderboard vs Books L2 | D_00: `advisor_fee_detail` split-weighted `managed_aua`; D_02: `accounts_dimension` total_aua; D_01: `nna_aua_by_advisor` total_aua | **Semantic split -- both valid:** `leaderboard.json` uses split-weighted (C_08); `advisors/{id}/summary.json` uses total (D_02) | D_04 documents distinction. Cross-advisor comparison always uses split-weighted. Book detail uses total. NEVER mixed in same view. |
| D2 | **Advisor NNA YTD** | Advisors leaderboard vs PartnerAnalytics ADV donut vs Books L2 | D_00: C_08 split-weighted `nna_txn`; D_01: canonical_nna period-differenced; D_02: relationship-level cum_flows diff | **Single: C_08 `advisor_fee_detail` nna_txn** for cross-advisor comparison. D_01's canonical_nna for firm-level NNA (not per-advisor). | D_04 reads C_08 for leaderboard. D_04 reads canonical_nna for partner_analytics donut NNA. Both are valid at their grain. |
| D3 | **NNA by GEO/ADV (snapshot vs continuous)** | DistributionTab snapshot donut vs continuous bar | D_01: period-differenced from `canonical_nna` + `client_performance`; D_00: cumulative daily inflow/outflow series | **Single: canonical_nna (C_01)** aggregated consistently by D_04 for both snapshot and continuous. Period-level flows derived from same cumulative series. | D_04 computes NNA-by-state from canonical_nna once, publishes to both `partner_analytics_{gran}.json` donut and `cumulative_chart.json` series. |
| D4 | **Firm Total AUA** | PartnerAnalytics header vs Books N1 vs Distribution donut | D_00: `aua.{gran}` (from `_build_static_aua_periods`); D_01: `views.*.donut.total`; D_00: `clients_tab.headline.total_aua` | **Single: `clients_tab.headline.total_aua`** (D_00, from accounts_dimension). All platinum files use this value with cert override applied once. | D_04 loads canonical AUA once, applies cert, propagates to all firm-level files. |
| D5 | **Firm Client Count** | Books N1 vs Advisors leaderboard sum | D_00: unique relationship_ids with AUA > 0; D_00: sum of per-advisor client counts (overcounts shared clients) | **Firm count = unique relationships** (from `clients_tab.json`). Per-advisor counts are correct at their level. | NOT a bug. Both preserved as-is. Dashboard uses firm count; leaderboard shows per-advisor count. |

---

## 5. Dead Code / Dead Artifact List

| # | Artifact | Size | Producer | Why Dead | Recommendation |
|---|----------|------|----------|----------|----------------|
| DC1 | `gold/artifacts/advisor_rolling_flows.json` | **52 MB** | D_00 `build_advisor_rolling_flows()` | No consumer. `getAdvisorRollingFlows()` exists in API layer but is never imported or called by any portal component. Replaced by inflows/outflows fields in employee_leaderboard entries (commit 235d3278). | **Phase 3:** Remove from D_00. Remove `getAdvisorRollingFlows` from `advisor-intelligence.ts`. Remove `AdvisorRollingFlowsResponse` type. |
| DC2 | `gold/artifacts/architect_leaderboard.json` | ~50KB est | D_00 `build_architect_leaderboard()` | Legacy dual-write. Replaced by `employee_leaderboard.json` which includes all roles. D_00 comments note "dual-write until portal migrates." | **Phase 3:** Remove after confirming no consumers. |
| DC3 | `gold/artifacts/summary/header_metrics.json` | ~30KB est | D_00 `build_header_metrics()` | Superseded by D_01's multi-view `partner_analytics/header_metrics_{gran}.json`. `getHeaderMetrics()` API function exists but portal uses `getPartnerAnalytics()` instead. | **Phase 5:** Verify no external consumers, then remove. |
| DC4 | 5 unused leaderboard windows | N/A (within file) | D_00 `build_employee_leaderboard()` | Windows 3M/6M/1Y/2Y/3Y/MTD in employee_leaderboard.json. AdvisorsTab uses only QTD/YTD. FeeEfficiencyPanel uses separate C_08 windows. | **Phase 3:** Trim to QTD/YTD in platinum leaderboard.json. Keep in gold for any future analytics use. |
| DC5 | Server-side `regression` in employee_leaderboard | N/A (within file) | D_00 | FeeEfficiencyPanel computes regression client-side, ignoring the server-side regression object. | **Phase 3:** Exclude from platinum leaderboard.json. Keep in dashboard.json fee_efficiency if needed. |

**Total dead data eliminated:** ~52.08 MB per gold run (dominated by advisor_rolling_flows.json).

---

## 6. Script Architecture Recommendation

### Question: Expand D_04 or create D_05+?

### Recommendation: **Option A -- Expand D_04**

**Rationale:**

1. **D_04 already reads the gold tables** that feed the P3 platinum files. It loads D_00 outputs (employee_leaderboard, clients_tab, timeseries_chart), D_01 outputs (header_metrics), D_02 outputs (book, detail), D_03 outputs (mix views), and C_08 outputs (fee efficiency). Adding new platinum file writes to D_04 requires no new data loading.

2. **Cross-surface consistency** is enforced by a single script. D_04 reads canonical AUA once, applies cert once, and propagates to all firm-level files. A D_05 would need to independently load the same tables and apply the same cert, creating a new divergence risk.

3. **Dispatch chain simplicity.** D_04 runs last in the chain (after D_03). Adding D_05 requires chain extension and ordering logic.

4. **The P3 additions are all firm-level.** The 6 new files (F3, F4a-c, F5, F6) are all under `platinum/firm/`. No new entity-level iteration (no per-advisor or per-client loops). This is 6 additional `_save_json()` calls, not 6,000.

### D_04 Expansion Plan

```
D_04.client_portal_summary.py (expanded)

Phase 1 (DELIVERED):
  publish_firm_dashboard()     -> platinum/firm/dashboard.json
  publish_firm_mix_summary()   -> platinum/firm/mix_summary.json
  publish_advisor_summaries()  -> platinum/advisors/{id}/summary.json (~20 files)
  publish_client_summaries()   -> platinum/clients/{rel_id}/summary.json (~600 files)
  publish_client_timeseries()  -> platinum/clients/{rel_id}/mix_timeseries.json (~600 files)
  publish_client_concentration() -> platinum/clients/{rel_id}/concentration.json (~600 files)
  publish_account_summaries()  -> platinum/accounts/{acct_id}/summary.json (~3,500 files)

Phase 3 (NEW):
  publish_timeseries_overview()    -> platinum/firm/timeseries_overview.json
  publish_partner_analytics()      -> platinum/firm/partner_analytics_{gran}.json (x3)
  publish_cumulative_chart()       -> platinum/firm/cumulative_chart.json
  publish_leaderboard()            -> platinum/firm/leaderboard.json

Phase 3 (EXTENSIONS):
  publish_client_summaries()  -- add revenue_and_tax section (reads C_05)
  publish_advisor_summaries() -- add implied_revenue + fee_yield_bps to clients[]
```

### Runtime Estimate

| Operation | Items | Est. Time |
|-----------|-------|-----------|
| Load gold tables (already done for P1) | 0 new loads | +0s |
| `publish_timeseries_overview()` | 1 file, pre-aggregate from timeseries_chart.json | +2s |
| `publish_partner_analytics()` x3 | 3 files, pass-through from D_01 with waste stripping | +3s |
| `publish_cumulative_chart()` | 1 file, weekly-sample from timeseries_chart.json | +5s |
| `publish_leaderboard()` | 1 file, trim windows/fields from employee_leaderboard.json | +1s |
| `revenue_and_tax` extension | ~600 files, read C_05 parquet once + aggregate | +10s |
| `advisor client revenue` extension | ~20 files, read C_08 detail once | +2s |
| **Total P3 addition** | | **~+23s** |

Current D_04 runtime is dominated by entity-level file writes (~5,300 files). P3 adds 6 firm-level files + minor extensions to existing entity loops. Negligible runtime impact.

### Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| D_04 script grows too large | LOW | P3 adds ~200 lines. D_04 is already modular with per-publish functions. |
| timeseries_chart.json changes break P3 | LOW | D_00 output is stable. D_04 reads and transforms, does not assume internal structure beyond documented keys. |
| cumulative_chart.json exceeds 200KB | MEDIUM | Monitor after first run. If >200KB, split drill data into lazy-loaded files (see brief 2.2 alternative). |
| NNA divergence not fully resolved | MEDIUM | D_04 must compute NNA-by-state/advisor from canonical_nna for BOTH partner_analytics and cumulative_chart. Verify with integration test comparing donut total vs bar chart total for same period. |

---

## 7. Complete File Tree

```
platinum/
  firm/
    dashboard.json                          [P1 DELIVERED]    ~100KB
    mix_summary.json                        [P1 DELIVERED]    ~5KB
    timeseries_overview.json                [P3 DESIGNED]     ~20KB
    partner_analytics_quarterly.json        [P3 DESIGNED]     ~100KB
    partner_analytics_monthly.json          [P3 DESIGNED]     ~100KB
    partner_analytics_annual.json           [P3 DESIGNED]     ~80KB
    cumulative_chart.json                   [P3 DESIGNED]     ~200KB
    leaderboard.json                        [P3 DESIGNED]     ~15KB
  advisors/
    {id}/
      summary.json                          [P1 DELIVERED]    ~15KB ea  (x~20)
  clients/
    {rel_id}/
      summary.json                          [P1 DELIVERED]    ~3KB ea   (x~600)
      mix_timeseries.json                   [P1 DELIVERED]    ~10KB ea  (x~600)
      concentration.json                    [P1 DELIVERED]    ~10KB ea  (x~600)
  accounts/
    {acct_id}/
      summary.json                          [P1 DELIVERED]    ~1.5KB ea (x~3,500)
```

**Firm-level total (P1 + P3):** 8 files, ~620KB
**Entity-level total (P1):** ~5,320 files, ~25MB
**Grand total:** ~5,328 files, ~26MB

---

## 8. Phase 3 Execution Order

| Step | Action | Dependencies | Deliverable |
|------|--------|-------------|-------------|
| 1 | Add `publish_timeseries_overview()` to D_04 | None | F3 in S3 |
| 2 | Add `publish_partner_analytics()` to D_04 | None | F4a-c in S3 |
| 3 | Add `publish_cumulative_chart()` to D_04 | None | F5 in S3 |
| 4 | Add `publish_leaderboard()` to D_04 | None | F6 in S3 |
| 5 | Extend `publish_client_summaries()` with revenue_and_tax | C_05 read added | C1 extended |
| 6 | Extend `publish_advisor_summaries()` with client revenue fields | C_08 read added | A1 extended |
| 7 | Deploy D_04 to gold runner, verify all files | Steps 1-6 | All platinum/ files in S3 |
| 8 | Remove `build_advisor_rolling_flows()` from D_00 | None | DC1 eliminated |
| 9 | Remove `build_architect_leaderboard()` from D_00 | None | DC2 eliminated |
| 10 | Update serving layer (shared-advisor-router + opal-partners-data) | Step 7 | New CF/Lambda rules for P3 files |
| 11 | Update frontend API calls for P3 platinum paths | Step 10 | Portal reads P3 files |
| 12 | Integration test: numbers-tie validation across all surfaces | Step 11 | QA pass |
