# ADVI_49PUSH Phase 2: Master Platinum File Catalog

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-09
**Task Order:** ADVI_49PUSH.007
**Source Audits:** 2.1 (PartnerAnalytics ~B), 2.2 (Distribution ~B), 2.3 (Advisors ~C), 2.4 (Books Remaining ~D), Cross-Surface Matrix (~D), P1 PRD (CTO)
**Status:** Complete

---

## Section 1: Master Platinum File Catalog

### Legend

- **Status:** DELIVERED = written by D_04 as of 2026-04-09 gold run; DESIGNED = specified, pending Phase 3 build
- **Phase:** P1 = delivered in original platinum launch; P2/P3 = subsequent waves

---

### 1A. Firm-Level Files (`platinum/firm/`)

| Path | Count | Est. Size | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|------|-------|-----------|----------|-------------|-----------|---------------|-------|--------|
| `platinum/firm/dashboard.json` | 1 | ~80-150 KB | D_04 | `employee_leaderboard.json` (D_00), `clients_tab.json` (D_00), `advisor_fee_efficiency.json` (C_08), `firm_composition.json` (D_03) | ClientsTab N1 headline + client list + fee scatter | Books N1 | P1 | DELIVERED |
| `platinum/firm/mix_summary.json` | 1 | ~5 KB | D_04 | `firm_mix_views.json` (D_03), `firm_composition.json` (D_03) | ClientsTab N1 mix panel | Books N1 | P1 | DELIVERED |
| `platinum/firm/fee_efficiency.json` | 1 | ~30 KB | D_04 | `advisor_fee_efficiency.json` (C_08) pass-through | FeeEfficiencyPanel (N1 scatter) | Books N1 | P1 | DELIVERED |
| `platinum/firm/timeseries_overview.json` | 1 | ~15-25 KB | D_04 | `timeseries_chart.json` (D_00) [aua/nna/growth_decomposition], `firm_mix_views.json` (D_03) [mix.gran] | PartnerAnalytics header (AUA/NNA/GRO/Mix bar charts) | PartnerAnalytics header | P2 | DELIVERED |
| `platinum/firm/partner_analytics_quarterly.json` | 1 | ~100 KB | D_04 | `partner_analytics/header_metrics_quarterly.json` (D_01) pass-through | DistributionTab snapshot quarterly (donut + bell curve + time machine) | Distribution snapshot | P2 | DELIVERED |
| `platinum/firm/partner_analytics_monthly.json` | 1 | ~100 KB | D_04 | `partner_analytics/header_metrics_monthly.json` (D_01) pass-through | DistributionTab snapshot monthly | Distribution snapshot | P2 | DELIVERED |
| `platinum/firm/partner_analytics_annual.json` | 1 | ~80 KB | D_04 | `partner_analytics/header_metrics_annual.json` (D_01) pass-through | DistributionTab snapshot annual | Distribution snapshot | P2 | DELIVERED |
| `platinum/firm/cumulative_chart.json` | 1 | ~150-250 KB | D_04 | `timeseries_chart.json` (D_00) [geo/adv/nna_geo/nna_adv/drills, weekly-sampled] | DistributionTab continuous mode (stacked area + NNA diverging bar) | Distribution continuous | P2 | DELIVERED |
| `platinum/firm/leaderboard.json` | 1 | ~12-15 KB | D_04 | `employee_leaderboard.json` (D_00) [QTD+YTD only], `entities/advisors/*/book.json` (D_02) [tagged_aua override] | AdvisorsTab (all views: AUA blocks, NNA flows, GRO bars, rank delta) | Advisors tab | P2 | DELIVERED |
| `platinum/firm/header_metrics.json` | 1 | ~5 KB | D_04 | `summary/header_metrics.json` (D_00) pass-through | getHeaderSummary (top-of-page AUA/NNA/client count bar) | PartnerAnalytics + ClientsTab N1 | P3 (.023) | DELIVERED |
| `platinum/firm/timeseries_chart.json` | 1 | ~800 KB | D_04 | `timeseries_chart.json` (D_00) pass-through | getTimeseriesChart (legacy) | PartnerAnalytics + DistributionTab | P3 (.023) | DELIVERED (retirement track) |
| `platinum/firm/employee_leaderboard.json` | 1 | ~681 KB | D_04 | `employee_leaderboard.json` (D_00) pass-through | getEmployeeLeaderboard (legacy) | Books N1 + Advisors tab | P3 (.023) | DELIVERED (retirement track) |

**Note on pass-throughs on retirement track:** `timeseries_chart.json` and `employee_leaderboard.json` are large compliance pass-throughs (P3, .023). They serve legacy endpoints until DE migrates each consumer to the trimmed platinum equivalents (`timeseries_overview.json` and `leaderboard.json`). Once migration is complete, these can be removed from D_04's publishers.

---

### 1B. Advisor-Level Entity Files (`platinum/advisors/{id}/`)

| Path | Count | Est. Size (each) | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|------|-------|-----------------|----------|-------------|-----------|---------------|-------|--------|
| `platinum/advisors/{id}/summary.json` | ~165 | ~20-25 KB | D_04 | `book.json` (D_02): total_aua, tagged_aua, fee_earning_aua, role_breakdown, active_since, nna, growth, clients, fee_summary, tax_exposure; `mix.json` (D_03): mix_periods; `composition.json` (D_03): mix_snapshot, concentration | Books L2 advisor panel; Advisor Drilldown (.041) summary card + role donut | Books L2 + Advisor Drilldown | P1 | DELIVERED |
| `platinum/advisors/{id}/mix.json` | ~165 | ~5 KB | D_04 | `entities/advisors/{id}/mix.json` (D_03) pass-through | Advisor mix Lambda (getAdvisorMixViews) | Books L2 + Advisor Drilldown | P2 (.023) | DELIVERED |
| `platinum/advisors/{id}/timeseries.json` | ~165 | ~30-80 KB | D_04 | `entities/advisors/{id}/timeseries.json` (D_02) pass-through (D_02 adds role AUA fields per .040) | Advisor Drilldown page (.041) stacked area + NNA chart | Advisor Drilldown | P3 (.040) | DELIVERED |

---

### 1C. Client-Level Entity Files (`platinum/clients/{id}/`)

| Path | Count | Est. Size (each) | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|------|-------|-----------------|----------|-------------|-----------|---------------|-------|--------|
| `platinum/clients/{id}/summary.json` | ~600 | ~2-5 KB | D_04 | `detail.json` (D_02): headline, accounts, tax; `_composition.json` (D_03): mix_snapshot, concentration; `_views.json` (C_06): mix_periods; `aua_timeseries.json` (D_02): 90d decomposition; `fee_rate_history.parquet` (A_02): fee_summary | Books L3 inline (client detail, mix, fee, decomposition) | Books L3 | P1 | DELIVERED |
| `platinum/clients/{id}/mix_timeseries.json` | ~600 | ~5-20 KB | D_04 | `{id}.json` (C_06): daily asset-class allocation percentages | ClientDetail page MixTimeseriesPanel | ClientDetail panels | P1 | DELIVERED |
| `platinum/clients/{id}/concentration.json` | ~600 | ~5-15 KB | D_04 | `{id}.json` (C_06): top-N holdings over time | ClientDetail page ConcentrationPanel | ClientDetail panels | P1 | DELIVERED |
| `platinum/clients/{id}/views.json` | ~600 | ~5 KB | D_04 | `entities/clients/{id}_views.json` (C_06/silver) pass-through | getRelationshipMixViews | Books L3 | P3 (.023) | DELIVERED |
| `platinum/clients/{id}/composition.json` | ~600 | ~5 KB | D_04 | `entities/clients/{id}_composition.json` (D_03) pass-through | getRelationshipCompositionStatic | Books L3 | P3 (.023) | DELIVERED |

---

### 1D. Account-Level Entity Files (`platinum/accounts/{id}/`)

| Path | Count | Est. Size (each) | Producer | Gold Sources | Consumers | Shared Across | Phase | Status |
|------|-------|-----------------|----------|-------------|-----------|---------------|-------|--------|
| `platinum/accounts/{id}/summary.json` | ~3,500 | ~1-2 KB | D_04 | `holdings_lots/{date}.parquet` (B_01): asset class mix + top holdings | Books L4 account composition | Books L4 | P1 | DELIVERED |

---

### 1E. File Count Summary

| Category | Pattern | Count | Total Est. Size | Status |
|----------|---------|-------|----------------|--------|
| Firm-level | `platinum/firm/*.json` | 12 files | ~2.1 MB | All DELIVERED |
| Advisor entities | `platinum/advisors/{id}/*.json` | 3 patterns x ~165 = 495 | ~10 MB | All DELIVERED |
| Client entities | `platinum/clients/{id}/*.json` | 5 patterns x ~600 = 3,000 | ~24 MB | All DELIVERED |
| Account entities | `platinum/accounts/{id}/*.json` | ~3,500 | ~5 MB | DELIVERED |
| **Total** | | **~7,007** | **~41 MB** | |

---

## Section 2: Cross-Surface Sharing Annotations

### `platinum/firm/dashboard.json` -- Three disjoint consumers in one file

| Field Group | Books N1 Headline | FeeEfficiencyPanel | Books N1 Client List |
|-------------|------------------|--------------------|---------------------|
| `headline.total_aua` | RENDERS | -- | -- |
| `headline.client_count` | RENDERS | -- | -- |
| `headline.nna_ytd` | RENDERS | -- | -- |
| `fee_efficiency.advisors[].aua` | -- | RENDERS (dot size) | -- |
| `fee_efficiency.advisors[].nna` | -- | RENDERS (x-axis) | -- |
| `fee_efficiency.advisors[].commission` | -- | RENDERS (y-axis) | -- |
| `fee_efficiency.advisors[].efficiency_pctile` | -- | RENDERS (dot color) | -- |
| `clients[].total_aua` | -- | -- | RENDERS |
| `clients[].relationship_id` | -- | -- | RENDERS |

Each consumer reads entirely disjoint fields. Modifying any sub-section does not affect the others.

---

### `platinum/firm/timeseries_*` -- Three files, three consumers

| File | Consumer | Purpose | Key Fields | Est. Size |
|------|----------|---------|------------|-----------|
| `timeseries_overview.json` | PartnerAnalytics header | Pre-aggregated period bars | `aua.{gran}.data[]`, `nna.{gran}[]`, `growth_decomposition.{gran}[]`, `mix.{gran}[]` | ~20 KB |
| `timeseries_chart.json` | getTimeseriesChart (legacy) | Full daily history (retirement track) | All views: aua, nna, geo, adv, drills, growth_decomposition | ~800 KB |
| `cumulative_chart.json` | Distribution continuous | Weekly-sampled geo/adv/NNA stacked area | `geo.data[]`, `adv.data[]`, `nna_geo.data[]`, `nna_adv.data[]`, drills | ~150-250 KB |

`timeseries_overview.json` and `cumulative_chart.json` both source from D_00's `timeseries_chart.json` gold file but extract entirely different slices. Neither overlaps with the other's fields.

---

### `platinum/advisors/{id}/summary.json` -- Books L2 vs Advisor Drilldown

| Field | Books L2 Panel | Advisor Drilldown (.041) |
|-------|--------------|------------------------|
| `book.total_aua` | RENDERS (headline) | RENDERS (summary card) |
| `book.fee_earning_aua` | RENDERS (fee panel) | RENDERS (summary card) |
| `book.nna_qtd`, `nna_ytd` | RENDERS | RENDERS (flows, updated by window) |
| `book.clients[]` | RENDERS (list) | Not used |
| `fee_summary.by_role[]` | RENDERS (donut) | RENDERS (role composition donut) |
| `role_breakdown.{role}.aua` | Available, not rendered | RENDERS (donut segment size) |
| `role_breakdown.{role}.pct_of_tagged` | Available, not rendered | RENDERS (donut legend %) |
| `active_since` | Available, not rendered | RENDERS (summary card "Active Since") |
| `mix`, `mix_periods`, `concentration` | RENDERS | Not used |

**Risk note:** Any change to `fee_summary.by_role[]` or `role_breakdown` shape affects both L2 and Drilldown. Coordinate with DE before modifying these.

---

### `platinum/firm/leaderboard.json` -- Advisors tab field breakdown

| Field | Top 3 Hero Cards | AUA Bar Chart | NNA Bar Chart | GRO Cards | Role Filter |
|-------|-----------------|--------------|--------------|-----------|------------|
| `entries[].name` | RENDERS | RENDERS | RENDERS | RENDERS | -- |
| `entries[].roles` | -- | -- | -- | -- | RENDERS (filter logic) |
| `entries[].total_aua` | AUA mode | RENDERS (bar height) | -- | -- | -- |
| `entries[].nna` | NNA mode | -- | RENDERS | -- | -- |
| `entries[].inflows`, `.outflows` | -- | -- | RENDERS (stacked) | -- | -- |
| `entries[].aua_growth_pct` | GRO mode | -- | -- | RENDERS | -- |
| `entries[].period_start_aua` | -- | -- | -- | -- | DE .043 rank delta |
| `entries[].role_breakdown.*.managed_aua` | -- | -- | -- | -- | RENDERS when role-filtered |
| `entries[].role_breakdown.*.nna` | -- | -- | -- | -- | RENDERS when role-filtered |

---

## Section 3: Divergence Resolution Table

| # | Metric | Divergent Surfaces | Root Cause | Resolution | Status |
|---|--------|-------------------|------------|------------|--------|
| 1 | **Advisor AUA in leaderboard** | Advisors tab showed C_08 `managed_aua` (~$149M for Travis); Books L2 showed D_02 `tagged_aua` (~$427M) | D_00 `_employee_entries_for_window` used split-weighted managed_aua; D_02 used any-role total AUA | RESOLVED: D_04 `build_leaderboard` overrides `total_aua` with D_02 `book_summary.total_aua` (tagged AUA). Window `summary.total_aua` = firm headline from `clients_tab`. | RESOLVED -- commit 10df0f0f (.037) |
| 2 | **Advisor NNA: leaderboard vs Books L2** | Leaderboard: C_08 split-weighted `nna_txn`; L2: D_02 relationship-aggregated `cum_inflows - cum_outflows` | Different aggregation paths, different semantics | SEMANTIC -- NOT A BUG. Leaderboard = fee-weighted attribution (cross-advisor comparison). L2 = book total NNA (advisor detail view). Not unified -- document distinction. | DOCUMENTED. No code change. |
| 3 | **NNA by GEO/ADV: Distribution snapshot vs continuous** | D_01 donut: period-differenced from `canonical_nna + client_performance`; D_00 continuous bar: cumulative daily inflow/outflow series | Two separate NNA computation paths | PENDING: D_04 should read a single canonical NNA source and write to both `partner_analytics_{gran}.json` and `cumulative_chart.json`. Not yet implemented. | PENDING (P3 scope) |
| 4 | **Firm Total AUA: D_01 donut vs D_00 headline** | D_01 sources from `client_performance.parquet` (C_02); D_00 sources from `accounts_dimension_latest` (A_00/B_01). Both apply `aua_certification` override independently. | Different source tables, independent cert application paths | PARTIAL: `timeseries_overview.json` uses D_00's cert-overridden total; partner_analytics files carry D_01's cert-overridden total. Monitor for divergence after each cert update. Flag if >$1M discrepancy. | MONITOR |
| 5 | **Firm client count: N1 headline vs advisor sum** | N1: unique relationship_ids; sum of per-advisor counts overcounts shared clients | Expected mathematical property of multi-advisor accounts | NOT A BUG. Document: firm count = unique (authoritative for capacity); advisor sum = intentional overcount. | DOCUMENTED |

---

## Section 4: Dead Code / Dead Artifact List

| Artifact | Type | Size | Status | Action |
|----------|------|------|--------|--------|
| `gold/artifacts/advisor_rolling_flows.json` | S3 artifact | 52 MB | DEAD -- never fetched by any portal component (confirmed grep across all portal/src/) | AE: `aws s3 rm s3://opal-data-bd/gold/artifacts/advisor_rolling_flows.json`. D_00 producer code already removed. P3/P5 cleanup. |
| `getAdvisorRollingFlows` | API function | -- | REMOVED -- committed prior session | DONE |
| `build_advisor_rolling_flows` | D_00 function | -- | REMOVED -- D_00 producer code gone | DONE |
| `gold/artifacts/architect_leaderboard.json` | S3 artifact | ~15 KB | DEAD -- superseded by employee_leaderboard.json, no consumer | AE: `aws s3 rm s3://opal-data-bd/gold/artifacts/architect_leaderboard.json`. P3/P5 cleanup. |
| `build_architect_leaderboard` | D_00 function | -- | REMOVED | DONE |
| `ADVISOR_ROLLING_FLOWS` constant | s3_layout.py | -- | REMOVED | DONE |
| `ARCHITECT_LEADERBOARD` constant | s3_layout.py | -- | REMOVED | DONE |
| `platinum/firm/timeseries_chart.json` | Platinum pass-through | ~800 KB | TEMPORARY -- retire after DE migrates `getTimeseriesChart` to `timeseries_overview.json` | Retire in Phase 5 after DE .024 migration |
| `platinum/firm/employee_leaderboard.json` | Platinum pass-through | ~681 KB | TEMPORARY -- retire after DE migrates `getEmployeeLeaderboard` to `leaderboard.json` | Retire in Phase 5 after DE .024 migration |

---

## Section 5: Script Architecture Recommendation

### Decision: Option A -- Expand D_04 (already in effect)

**D_04 is the single platinum publisher for ALL platinum files. D_05+ will NOT be created.**

This decision is already reflected in the codebase. D_04 produces all 20 unique platinum path patterns as of 2026-04-09.

**Rationale:**

1. **D_04 already contains all the logic.** Firm, advisor, client, and account publishers are implemented as Steps 1-11. The P2/P3 waves were added as new steps without architectural changes. The pattern scales cleanly.

2. **Single writer prevents S3 key conflicts.** Overlapping publishers would risk partial writes. D_04 is idempotent, runs as a single step after D_03 in the downstream chain, and is safe to re-run.

3. **Runtime is acceptable.** D_04 writes ~14,769 files in a single run on c6i.16xlarge. At current scale (165 advisors, 600 clients, 3,500 accounts), runtime is 3-5 minutes. If future advisor/client count growth pushes past ~30,000 total files, split by entity class: D_04 for firm+advisor, D_04b for client+account. No split needed today.

4. **Single dispatch entry.** Adding D_05+ would require updating `gold_dispatch.sh`, `CHAIN_FULL`, `CHAIN_DOWNSTREAM`, `lambda-source-map.json`, and potentially new Terraform resources. D_04 expansion avoids all of this overhead.

5. **`--dry-run` covers everything.** `D_04 --dry-run` can test all 20 publisher steps without writing to S3.

**Option B (D_05+ for non-Books platinum) -- NOT RECOMMENDED:**

Justified only if D_04 runtime exceeds 10 minutes (making downstream chain a bottleneck) OR if new platinum files require upstream data from a script that runs after D_03 in the chain. Neither condition currently holds.

**Current chain position:**
```
CHAIN_DOWNSTREAM = C_03 C_05 C_07 C_06 C_08 D_00 D_01 D_02 D_03 D_04
```
D_04 is correctly positioned as the final step, after all D_00-D_03 outputs are ready.

---

## Section 6: Remaining Phase 3 Design Items (Not Yet Built)

| Platinum File | Design Brief | Description | Gold Sources | Priority |
|--------------|-------------|-------------|-------------|----------|
| `platinum/clients/{id}/summary.json` + `revenue_and_tax` section | .004 (2.4) | Add cost basis, unrealized gain/loss (ST/LT), tax efficiency ratio, top 3 gain positions, fee yield bps. No new gold computation needed. | `client_tax_liability.parquet` (C_05, already loaded by D_04) | Medium -- extends existing file, no new S3 key |
| `platinum/advisors/{id}/summary.json` + `book.clients[].implied_revenue` + `.fee_yield_bps` | .004 (2.4) | Add 2 revenue fields per client entry in advisor book. ~800 bytes per advisor. | `advisor_fee_detail/{date}.parquet` (C_08) | Low -- DE has not yet requested this |

Neither blocks any current wave of DE task orders.

---

## Section 7: Summary

| Dimension | Value |
|-----------|-------|
| Distinct platinum file patterns | 20 |
| Estimated file count per gold run | ~7,007 |
| All patterns DELIVERED | Yes |
| Phase 3 schema extensions pending | 2 (revenue_and_tax, client implied_revenue) |
| Dead artifacts removed (code) | 5 (rolling_flows fn, architect_leaderboard fn, 2 s3_layout constants, API endpoint) |
| Dead S3 objects for AE cleanup | 2 (advisor_rolling_flows.json, architect_leaderboard.json) |
| Platinum pass-throughs on retirement track | 2 (timeseries_chart.json, employee_leaderboard.json) |
| Divergences resolved | 2 (leaderboard total_aua, dead rolling flows) |
| Divergences pending (P3) | 1 (NNA GEO/ADV canonical source) |
| Divergences documented (semantic, not bugs) | 2 (advisor NNA split, firm client count overcount) |
| Script architecture | D_04 single-publisher (all 20 patterns) |
| Producer runtime estimate | 3-5 min on c6i.16xlarge |
