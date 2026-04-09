# ADVI_49PUSH P2 2.3 -- Advisors Tab Design Audit

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-08
**Task Order:** ADVI_49PUSH.003
**Status:** Complete

---

## 1. Fetch Trace Table

| # | Trigger | API Function | URL | Serving Path | S3 Key | Gold Script | Gold Function |
|---|---------|-------------|-----|-------------|--------|-------------|---------------|
| 1 | `useEffect` on firmId mount | `getEmployeeLeaderboard(firmOverride)` | `/api/scoped/advisor-intelligence/artifacts/employee_leaderboard.json` | CloudFront -> shared-advisor-router -> S3 direct | `gold/artifacts/employee_leaderboard.json` | D_00.portal_aggregates.py | `build_employee_leaderboard` |

**Only one fetch.** The PRD assumed two fetches (`employee_leaderboard.json` + `advisor_rolling_flows.json`). In reality, AdvisorsTab imports only `getEmployeeLeaderboard`. The `getAdvisorRollingFlows` function exists in the API layer but is **never imported or called** by any component in the portal. The 52 MB `advisor_rolling_flows.json` artifact is **dead data** -- produced by D_00 and served by CloudFront, but never consumed.

### Serving Layer Detail (from comp-routes)

```
ROUTE: getEmployeeLeaderboard
  URL:        /api/scoped/advisor-intelligence/artifacts/employee_leaderboard.json
  CloudFront: behavior /api/scoped/advisor-intelligence/artifacts/*
              origin   S3-opal-data-bd (s3)
  Auth:       edge JWT (yes), API GW (no)
  Router:     shared-advisor-router
  S3 key:     gold/artifacts/employee_leaderboard.json
  Consumers:  AdvisorsTab, ClientsTab
```

No Lambda transformation. The browser receives the raw JSON from S3 with JWT auth at the edge.

---

## 2. Render Field Inventory

### Fields Actually Rendered

| Field | Used In | Chart/Card | Notes |
|-------|---------|------------|-------|
| `name` | Top3, NNA bar, AUA bar, Growth bar, Cards | All | Advisor display name |
| `roles` | Role filter, Cards | Filter logic | Array of role strings; drives checkbox filtering |
| `total_aua` | Top3 hero (AUA mode), AUA bar chart, Cards | AUA column | Ranked, top 10 charted |
| `nna` | Top3 hero (NNA mode), NNA bar chart, Cards | NNA column | Ranked, top 10 charted |
| `inflows` | NNA bar chart tooltip, NNA stacked bar | NNA view | Stacked positive bar |
| `outflows` | NNA bar chart tooltip, NNA stacked bar | NNA view | Stacked negative bar |
| `aua_growth_pct` | Top3 hero (GRO mode), Growth bar chart, Cards | GRO column | Diverging horizontal bars |
| `new_clients` | Cards | New Clients column | Displayed in all 3 card views |
| `client_count` | `getDisplayMetrics` role-filtering | Internal | Summed from role_breakdown when filtered |
| `account_count` | `getDisplayMetrics` role-filtering | Internal | Summed from role_breakdown when filtered |
| `role_breakdown.*` | Role-filtered metrics | Internal | When role checkboxes are partially checked, AUA/NNA/inflows/outflows are re-summed from checked roles only |

### Fields Fetched but NOT Rendered

| Field | In JSON | In TypeScript | Notes |
|-------|---------|---------------|-------|
| `implied_revenue` | Yes | Yes (`EmployeeLeaderboardEntry`) | Not displayed anywhere in AdvisorsTab |
| `fee_yield_bps` | Yes | Yes | Not rendered; used by FeeEfficiencyPanel (separate component) |
| `efficiency_ratio` | Yes | Yes | Not rendered |
| `regression_residual` | Yes | Yes | Not rendered |
| `rank_nna` | Yes | No type def | Pre-computed rank, not used (component re-ranks client-side) |
| `rank_aua` | Yes | No type def | Not used |
| `rank_efficiency` | Yes | No type def | Not used |
| `regression` (per-window) | Yes | Yes | Not rendered in AdvisorsTab (used by FeeEfficiencyPanel) |
| `role_breakdown.*.implied_revenue` | Yes | Yes | Not rendered |
| `role_breakdown.*.avg_split_pct` | Yes | Yes | Not rendered |
| `role_breakdown.*.aua_growth_pct` | Yes | No | Not in type, not rendered |
| `role_breakdown.*.new_clients` | Yes | No | Not in type, not rendered |

### Constants

| Constant | Value | Usage |
|----------|-------|-------|
| `TOP_N_CHART` | 10 | Bar charts show only top 10 advisors |
| `TOP_N_HIGHLIGHTS` | 3 | Hero cards show top 3 |
| `LEADERBOARD_PAGE_SIZE` | 10 | Paginated card list, 10 per page |
| `PINNED_BOTTOM_NAMES` | `{"49F House", "Unassigned"}` | Excluded from rankings, pinned to bottom |
| `ADVISOR_ROLES` | `["architect", "implementor", "consultant", "local_ops"]` | Checkbox filter options |

### Windows Used

The component maps `PeriodKey` to window keys:
- `qtd` -> `"QTD"` (default)
- `ytd` -> `"YTD"`
- `mtd` -> `"QTD"` (fallback, no MTD toggle exposed)

The JSON contains windows: `3M`, `6M`, `1Y`, `2Y`, `3Y`, `MTD`, `QTD`, `YTD`. The component uses **only QTD and YTD**. The 5 trailing windows (`3M`/`6M`/`1Y`/`2Y`/`3Y`) and `MTD` are never accessed by AdvisorsTab.

---

## 3. Waste Analysis

### 3a. File Size

| Artifact | Size | Status |
|----------|------|--------|
| `employee_leaderboard.json` | 681 KB | Active -- single fetch, entire file used |
| `advisor_rolling_flows.json` | 52.4 MB | **DEAD** -- produced but never fetched by any component |

### 3b. Structural Waste in employee_leaderboard.json

1. **5 unused windows**: The file contains 8 windows (3M, 6M, 1Y, 2Y, 3Y, MTD, QTD, YTD). AdvisorsTab uses only QTD + YTD. However, FeeEfficiencyPanel and Books N1 may use trailing windows -- this needs cross-reference before trimming.

2. **Per-entry waste**: Each entry carries `implied_revenue`, `fee_yield_bps`, `efficiency_ratio`, `regression_residual`, 3 rank fields, and nested `role_breakdown` with `implied_revenue` and `avg_split_pct`. Of these, AdvisorsTab uses only: `name`, `roles`, `total_aua`, `nna`, `inflows`, `outflows`, `aua_growth_pct`, `new_clients`, `client_count`, `account_count`, and the core `role_breakdown` fields (`managed_aua`, `nna`, `inflows`, `outflows`, `account_count`, `client_count`).

3. **Approximate waste fraction**: ~30-35% of per-entry payload is fee/efficiency data not rendered by AdvisorsTab. Acceptable for now since the file is shared with FeeEfficiencyPanel.

4. **advisor_rolling_flows.json (52 MB)**: 100% waste. No consumer exists. Recommendation: **stop producing this artifact** in D_00. It was replaced by the inflows/outflows fields added to employee_leaderboard entries (commit 235d3278).

### 3c. Advisor Count / Zero-AUA Filtering

All advisors are included in every window, including those with zero AUA in some trailing windows. For a firm with ~15 advisors, this is negligible. For larger firms, zero-AUA filtering could reduce entry count, but is unnecessary at current scale.

---

## 4. Cross-Surface Number Tie Analysis

### 4a. Data Source Divergence Map

| Metric | Advisors Tab (D_00) | PartnerAnalytics ADV Donut (D_01) | Books L2 Summary (D_02) | Divergent? |
|--------|--------------------|------------------------------------|------------------------|------------|
| **Advisor AUA** | `advisor_fee_detail` (08c canonical) -> `managed_aua` summed by advisor | `nna_aua_by_advisor.parquet` (pre-aggregated silver view) -> `total_aua` | `accounts_dimension` (A_00/B_01) -> `total_aua` summed by architect | **YES -- 3 different sources** |
| **Advisor NNA YTD** | `advisor_fee_detail` -> `nna_daily` summed over YTD window | `canonical_nna` + `client_perf` -> period-differenced NNA by architect | `accounts_dimension` -> `cum_inflows - cum_outflows` differenced over YTD | **YES -- 3 different sources** |
| **Advisor Growth %** | `(current_aua - start_aua) / start_aua` from `advisor_fee_detail` | Not shown per-advisor (only shown as AUA donut share change) | `(total_aua - aua_start) / aua_start` from `accounts_dimension` | **YES -- 2 different sources** |
| **Advisor Client Count** | `cdim.groupby('primary_architect').size()` | `num_relationships` from `nna_aua_by_advisor` view | `relationship_id.nunique()` from `accounts_dimension` filtered to architect | **YES -- potentially different counts** |

### 4b. Root Cause of Divergence

The three scripts compute "advisor AUA" from **three fundamentally different grain levels**:

1. **D_00 (employee_leaderboard)**: Uses `advisor_fee_detail` from 08c canonical, which is a daily partition by `(advisor, role, date)`. AUA is `managed_aua` -- the portion of account AUA assigned to each advisor role weighted by `split_pct`. This is **role-weighted AUA**.

2. **D_01 (PartnerAnalytics ADV donut)**: Uses `nna_aua_by_advisor.parquet`, a pre-aggregated silver view that groups by `architect` (primary architect only). This is **architect-attributed AUA** (no role split).

3. **D_02 (Books L2 advisor book)**: Uses `accounts_dimension` filtered to `architect == X`, summing `total_aua` per account. This is **account-level AUA attributed to primary architect**.

The NNA divergence follows the same pattern: D_00 sums daily `nna_daily` from fee detail (role-weighted), D_01 differences cumulative NNA from `canonical_nna` (transaction-based), D_02 differences `cum_inflows - cum_outflows` from account snapshots (position-based).

### 4c. Resolution Recommendation

**Single source of truth: `advisor_fee_detail` (08c canonical)**

Rationale:
- It is the only source that correctly handles role splits (an account can have architect + implementor, each with a split_pct)
- It already produces the most granular data (daily × advisor × role)
- The employee_leaderboard already aggregates from it, and the role_breakdown allows filtering by any combination of roles
- D_01's `nna_aua_by_advisor` and D_02's account-level groupby are simplified approximations

**Platinum design must derive all advisor-level AUA, NNA, and growth from `advisor_fee_detail`** so that the number on the Advisors tab leaderboard exactly equals the number on the Books L2 summary and the PartnerAnalytics ADV donut.

---

## 5. Platinum File Specification

### 5a. Recommendation: Separate `platinum/firm/leaderboard.json`

**Do NOT embed in `dashboard.json`.** Rationale:

1. `dashboard.json` (Phase 1) serves Books N1 headline + fee efficiency. It's a different rendering surface with different field needs.
2. The leaderboard has windowed data (QTD/YTD at minimum). dashboard.json's leaderboard section would need to carry the same window structure, bloating a file designed for a single-view dashboard.
3. FeeEfficiencyPanel already reads `advisor_fee_efficiency.json` (C_08) -- it doesn't need leaderboard data duplicated into dashboard.json.

**Decision: `platinum/firm/leaderboard.json`** -- standalone file serving AdvisorsTab, shared with any surface that needs windowed per-advisor rankings.

### 5b. `platinum/firm/leaderboard.json` Schema

```json
{
  "generated_at": "2026-04-08T...",
  "data_as_of": "2026-04-07",
  "firm_id": "49financial",
  "available_windows": ["QTD", "YTD"],
  "windows": {
    "QTD": {
      "entry_count": 15,
      "summary": {
        "total_aua": 1234567890.12,
        "total_nna": 12345678.90
      },
      "entries": [
        {
          "name": "Travis Penfield",
          "advisor_id": "travis_penfield",
          "roles": ["architect"],
          "total_aua": 123456789.01,
          "nna": 1234567.89,
          "inflows": 2345678.90,
          "outflows": 1111111.01,
          "aua_growth_pct": 5.2,
          "new_clients": 3,
          "client_count": 42,
          "account_count": 87,
          "role_breakdown": {
            "architect": {
              "managed_aua": 100000000.00,
              "nna": 1000000.00,
              "inflows": 2000000.00,
              "outflows": 1000000.00,
              "account_count": 70,
              "client_count": 35
            },
            "implementor": {
              "managed_aua": 23456789.01,
              "nna": 234567.89,
              "inflows": 345678.90,
              "outflows": 111111.01,
              "account_count": 17,
              "client_count": 7
            }
          }
        }
      ]
    },
    "YTD": { "...same structure..." }
  }
}
```

**Provenance map:**

| Platinum Field | Gold Source | Gold File | Notes |
|---------------|------------|-----------|-------|
| `entry.total_aua` | `managed_aua` summed across roles | `advisor_fee_detail` (08c) | Latest-day snapshot |
| `entry.nna` | `nna_daily` summed over window | `advisor_fee_detail` (08c) | Transaction-based |
| `entry.inflows` | `inflow_daily` summed over window | `advisor_fee_detail` (08c) | |
| `entry.outflows` | `outflow_daily` summed over window | `advisor_fee_detail` (08c) | |
| `entry.aua_growth_pct` | `(current - start) / start * 100` | `advisor_fee_detail` (08c) | Window-relative |
| `entry.new_clients` | `cdim.first_seen_date >= window_start` | `client_dimension` (A_04) | Grouped by primary_architect |
| `entry.client_count` | `cdim.groupby(primary_architect).size` | `client_dimension` (A_04) | |
| `entry.account_count` | Sum of role_breakdown account_counts | `advisor_fee_detail` (08c) | |
| `entry.role_breakdown.*` | Per-role aggregation | `advisor_fee_detail` (08c) | Key for role-filter |

**Fields removed vs current employee_leaderboard.json:**

- `implied_revenue` -- moved to `platinum/firm/fee_efficiency.json` (separate surface)
- `fee_yield_bps` -- same
- `efficiency_ratio` -- same
- `regression_residual` -- same
- `rank_nna`, `rank_aua`, `rank_efficiency` -- client-side ranking; not needed in platinum
- `regression` (per-window) -- moved to fee_efficiency platinum
- `role_breakdown.implied_revenue` -- not rendered by leaderboard
- `role_breakdown.avg_split_pct` -- not rendered by leaderboard

**Windows trimmed:** Only `QTD` and `YTD` (the only windows AdvisorsTab accesses). If Books N1 or FeeEfficiency needs trailing windows (1Y/3Y), those go in their own platinum file.

**Estimated size:** ~15 advisors x 2 windows x ~400 bytes/entry = ~12-15 KB (down from 681 KB).

### 5c. `platinum/firm/rolling_flows.json` -- NOT NEEDED

The original `advisor_rolling_flows.json` (52 MB) is dead data. No component fetches it. The NNA flows visualization in AdvisorsTab uses `inflows`/`outflows` from the employee_leaderboard entries. **Do not create a platinum rolling_flows file.** Instead:

- Stop producing `advisor_rolling_flows.json` in D_00
- The inflows/outflows per entry in `platinum/firm/leaderboard.json` serve the NNA bar chart

---

## 6. Cross-Surface Consistency Matrix

| Metric | Advisors Tab | Books L2 Summary | PartnerAnalytics ADV Donut | Current Gold Source | Platinum Source (Design) |
|--------|-------------|-----------------|---------------------------|--------------------|-----------------------|
| Advisor AUA | leaderboard.json `total_aua` | `advisors/{id}/summary.json` `total_aua` | `partner_analytics/header_metrics_*.json` `views.adv.*.donut.segments[].aua` | D_00: fee_detail, D_02: acct_dim, D_01: adv_ts | **Single: advisor_fee_detail (08c)** -> D_04 computes once, publishes to leaderboard + advisor summary + partner_analytics |
| Advisor NNA YTD | leaderboard.json `nna` (YTD window) | `advisors/{id}/summary.json` `nna.ytd` | `partner_analytics/header_metrics_*.json` `views.nna.*.adv` | D_00: fee_detail nna_daily, D_02: cum_flows diff, D_01: canonical_nna diff | **Single: advisor_fee_detail (08c)** -> nna_daily summed |
| Advisor Growth % | leaderboard.json `aua_growth_pct` | `advisors/{id}/summary.json` `growth.ytd_growth_pct` | N/A (not per-advisor in donut) | D_00: fee_detail, D_02: acct_dim aua diff | **Single: advisor_fee_detail (08c)** -> consistent growth calc |
| Advisor Client Count | leaderboard.json `client_count` | `advisors/{id}/summary.json` `client_count` | `views.adv.*.donut.segments[].client_count` | D_00: cdim primary_architect, D_02: rel_id.nunique, D_01: adv_ts.num_relationships | **Single: client_dimension primary_architect count** |

**All four metrics currently diverge across 2-3 scripts.** The platinum design resolves this by mandating that D_04 (the platinum publisher) reads `advisor_fee_detail` once and writes all advisor-level metrics to every platinum file that needs them.

---

## 7. Answers to PRD Audit Questions

### Q1: How large is employee_leaderboard.json? Can it be trimmed?

**681 KB.** Yes, it can be significantly trimmed:
- Remove 5 unused windows (3M/6M/1Y/2Y/3Y) and MTD -> saves ~75% of file
- Remove fee/efficiency fields not rendered by leaderboard -> saves ~30% per entry
- Remove pre-computed ranks (client re-ranks) -> saves ~5% per entry
- Platinum estimate: **~12-15 KB** (from 681 KB)

Zero-AUA filtering is unnecessary at current advisor count (~15).

### Q2: advisor_rolling_flows.json -- how much does the chart render?

**The chart does not render advisor_rolling_flows.json at all.** The function `getAdvisorRollingFlows` is defined but never called by any component. The NNA bar chart in AdvisorsTab uses `inflows`/`outflows` fields from `employee_leaderboard.json` entries. The 52 MB artifact is dead. `TOP_N_CHART = 10` applies to the bar chart built from leaderboard entries, not rolling flows.

### Q3: Should Advisors tab share `platinum/firm/dashboard.json` or get its own file?

**Own file: `platinum/firm/leaderboard.json`.** Reasons:
1. Different windowing needs (QTD/YTD vs single-period dashboard)
2. Different field sets (leaderboard needs role_breakdown; dashboard needs fee_efficiency)
3. Cleaner separation of concerns -- each platinum file serves one rendering surface

### Q4: Are both architects[] and implementors[] splits rendered?

**Not applicable.** The component never fetches `advisor_rolling_flows.json` (which contains the `architects[]`/`implementors[]` split). Instead, it uses `role_breakdown` from the employee_leaderboard, which already provides per-role metrics. The role filter checkboxes in AdvisorsTab toggle which roles are summed from `role_breakdown`, not which time series are displayed.

---

## 8. Compiler Tool Traces (Session Log)

### Commands Run

| # | Command | Key Finding |
|---|---------|-------------|
| 1 | `comp-trace AdvisorsTab --direction both` | Single downstream edge: -> getEmployeeLeaderboard |
| 2 | `comp-trace employee_leaderboard --all --direction both` | Upstream: D_00:build_employee_leaderboard -> S3 artifact. Downstream: 14 endpoints (graph over-counts; many are other endpoints in same API file) |
| 3 | `comp-trace advisor_rolling_flows --direction both` | No upstream or downstream connections for the function node |
| 4 | `comp-blast build_employee_leaderboard` | 28 downstream nodes (14 endpoints + 13 Lambda refs + 1 S3 artifact) |
| 5 | `comp-blast advisor_rolling_flows` | No downstream consumers |
| 6 | `comp-pipescript io D_00` | Reads 17 sources, writes 8 artifacts. employee_leaderboard + advisor_rolling_flows both terminal |
| 7 | `comp-pipescript consumers D_00` | Only D_01 consumes D_00 output (via aua_certification_key) |
| 8 | `comp-routes trace AdvisorsTab` | Confirmed: only getEmployeeLeaderboard call, S3 direct via shared-advisor-router |
| 9 | `comp-routes trace getEmployeeLeaderboard` | CF -> S3-opal-data-bd, JWT edge auth, no Lambda transform |
| 10 | `comp-routes trace getAdvisorRollingFlows` | CF -> S3-opal-data-bd, same pattern (but no consumer) |
| 11 | `comp-trace getAdvisorRollingFlows --direction up` | Upstream shows employee_leaderboard.json (graph link may be stale) |

### Key Decisions

1. **advisor_rolling_flows.json is dead** -- confirmed by grep across all portal/src: `getAdvisorRollingFlows` is defined in API layer but never imported
2. **Single-file fetch** -- AdvisorsTab is simpler than expected: one fetch, one file, no Lambda
3. **Cross-surface divergence confirmed** -- 3 different gold sources produce "advisor AUA" for 3 different surfaces
4. **Resolution: advisor_fee_detail (08c) as single source** -- most granular, handles role splits correctly

---

## 9. Summary of Recommendations

| # | Action | Impact |
|---|--------|--------|
| 1 | Create `platinum/firm/leaderboard.json` with QTD + YTD windows only | 681 KB -> ~15 KB |
| 2 | Stop producing `advisor_rolling_flows.json` in D_00 | Eliminate 52 MB dead artifact |
| 3 | Remove `getAdvisorRollingFlows` from API layer (dead code) | Code cleanup |
| 4 | Unify all advisor AUA/NNA/growth on `advisor_fee_detail` (08c) | Eliminate cross-surface divergence |
| 5 | Strip fee/efficiency fields from leaderboard platinum (move to fee_efficiency platinum) | Smaller payload, cleaner separation |
| 6 | Do NOT create `platinum/firm/rolling_flows.json` | No consumer exists |
