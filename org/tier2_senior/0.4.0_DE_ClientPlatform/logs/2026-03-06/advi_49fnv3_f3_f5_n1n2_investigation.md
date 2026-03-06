# ADVI_49FNV3 — F3/F5/N1-N2 Investigation and Closeout — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-06
**Start Time:** session start
**End Time:** session end

## Objective

Close out three pending ADVI_49FNV3 DE task orders: F5-DE (QTD/YTD period toggle
investigation), F3 (DistributionTab NNA geo drill wiring), and N1-N2-DE (firm dashboard +
advisor book wiring). DS confirmed F5 is not a Lambda bug; DT confirmed N1+N2 wiring was
already implemented in the prior session (1dc96b5).

---

## Work Completed

### 1. F5-DE: QTD/YTD Period Toggle Investigation

**Task order:** `ADVI_49FNV3.F5-DE.qtd-ytd-frontend-investigation.md`

**DS finding (from advi_49fnv3_f1_f5_investigation.md):**
- `bd-portal-advisor-publisher` computes `qtd_start = Jan 1, 2026` and
  `ytd_start = Jan 1, 2026` for any date in Q1. Identical. Lambda is correct.
- Root cause is **not** in the Lambda.

**DT finding (from advi_49fnv3_session1.md, prior session):**
- `periodToChartWindow('qtd')` in `AdvisorsTab.tsx` maps to `'3M'` (trailing 90 days).
- `periodToChartWindow('ytd')` maps to `'1Y'` (trailing 1 year).
- The leaderboard publisher emits **rolling trailing windows** only. In March 2026,
  QTD = Jan 1 to today (~65 days) but `'3M'` = trailing 90 days from today. These are
  different date ranges producing different NNA values.
- **Frontend cannot fix this alone.** Fix requires DS to emit a `qtd` calendar window
  in `architect_leaderboard.json` and `implementor_leaderboard.json`.

**DE finding:** No code change made. Root cause is rolling-vs-calendar window mismatch.
Fix is Lambda-side (DS task). Task order marked complete.

---

### 2. F3: DistributionTab NNA Geo Drill Investigation

**Task order:** `ADVI_49FNV3.F3.segment-drilldown-wiring.md`

**Investigation:**

Audited `DistributionTab.tsx` and `types.ts` against task order requirements.

**Q1: Is `nna_geo_drill` from `timeseries_chart.json` consumed by the Snapshot NNA donut?**

NO — and correctly so. `nna_geo_drill` from `timeseries_chart.json` has type
`NNAGeoDrillView` (`{ [stateKey]: { categories: string[], data: NNASeriesPoint[] } }`).
This is a **time series**, not donut segment data. It is consumed by
`ContinuousNnaDivergingView` (line 443) for the continuous NNA chart — the correct use.

**Q2: Is state→city drill wired for the Snapshot NNA geo donut?**

YES — already wired. `handleSegmentClick` at line 1815-1834 handles NNA geo drill:
- If `nnaDrillData[seg.key]` exists → `setSelectedStateKey(seg.key)` + `setGeoDrillLevel('city')`
- City segments built from `nnaDrillData[selectedStateKey].by_city` at line 1658-1668

`nnaDrillData` reads from `analyticsData.views.nna[period].geo.drill` in
`header_metrics_quarterly.json`. This is the correct data source for distribution stats.

**Q3: Is `by_city` data populated in the published JSON?**

YES — confirmed in `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`,
lines 1061-1087 (Y6b block): `geo_drill_dist[state] = { total: ..., by_city: {...} }`.
The EC2 script emits `by_city: Record<string, DistributionStats>` for each top state
that has at least 2 relationships in any city. This feeds into `views.nna[period].geo.drill`.

**Q4: City→client drill?**

NOT available in GEO mode. `by_city` entries are `DistributionStats` aggregates, not
individual relationship records. Y6d client drill is ADV-mode only (architect →
relationships via `views.nna[period].adv.drill[arch].distribution`). There is no
per-relationship list within geo city entries. This is a data constraint, not a wiring gap.

**Conclusion:** No code change needed. F3 wiring is complete in existing code. Task order
marked complete.

---

### 3. N1-N2-DE: Firm Dashboard + Advisor Book Wiring Verification

**Task order:** `ADVI_49FNV3.N1-N2-DE.firm-dashboard-and-advisor-book-wiring.md`

Prior DT session (1dc96b5) implemented all requirements. Verified against task order:

| Requirement | Status |
|---|---|
| TypeScript interfaces from design brief Section 6 | Done — already in `types.ts` (AdvisorBookResponse, BooksClientDetailResponse, BooksClientAccount, BooksClientTaxDetail, CostBasisYear, GainPosition, OpenLot) |
| N1 Firm Overview KPIs | Done — `N1FirmDashboard` component, Panel 1 (line 930-940 of ClientsTab.tsx) |
| N1 Tax Status Breakdown | Done — TaxRow components, Panel 2 (lines 942-952) |
| N1 Engagement Summary | Done — FlowMetric + MetricCard, Panel 3 (lines 954-966) |
| N1 AUA by Advisor (1Y, sorted by total_aua, row click -> N2) | Done — `AdvisorSummaryTable` (line 329, sorts by total_aua desc, onClick -> handleSelectAdvisor) |
| N2 Advisor Book View (L2AdvisorBook) | Done — all 4 panels: Summary KPIs, Tax Exposure, Engagement, Clients table (lines 345-426) |
| advisorId slug fix | Done — exact replica of `_advisor_id()` at line 186 |
| Access gate `isInternal() \|\| isDev()` | Done — line 52-53 |
| Data fetch: leaderboard + clients_tab in parallel | Done — Promise.all at lines 84-98 |

Task order marked complete. Updated N1-N2-RD task order dependency from `pending` to
`complete`. RD may review and polish visual layout per their task order.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| F5-DE: no frontend fix | Root cause is rolling-vs-calendar window mismatch in leaderboard publisher. Frontend maps `qtd` to `'3M'` which is incorrect but unfixable until Lambda emits a `qtd` calendar window. Route to DS for Lambda fix. |
| F3: no wiring change | State→city drill already wired in `handleSegmentClick`. `nna_geo_drill` from timeseries_chart.json is correctly NOT used in snapshot donut — it's time series data for the continuous view. |
| F3: city→client gap as data constraint | EC2 script 09 emits `by_city: DistributionStats`, not relationship lists. ADV mode has client drill but GEO city level does not. Correct behavior — no stub or workaround. |
| N1-N2-DE: complete without new code | DT implemented all functional requirements in 1dc96b5. No additional wiring needed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_49FNV3.F5-DE.qtd-ytd-frontend-investigation.md` | status -> complete | No — local only |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_49FNV3.F3.segment-drilldown-wiring.md` | status -> complete | No — local only |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_49FNV3.N1-N2-DE.firm-dashboard-and-advisor-book-wiring.md` | status -> complete | No — local only |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_49FNV3.N1-N2-RD.firm-dashboard-and-advisor-book-ui.md` | dependency status -> complete, constraint note updated | No — local only |

---

## Blockers

- **F5 fix**: BLOCKED on DS — Lambda must emit a `qtd` calendar window in
  `architect_leaderboard.json` / `implementor_leaderboard.json`. Task order F5-DS is
  with 0.4.0_DS_ClientPlatform.
- **F1 GRO data**: BLOCKED on DT — bd-portal-publisher redeploy required per
  `docs/briefs/devops-brief-49fnv3-f1-gro-publisher-fix.md`. No DE action.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All three DE task orders for ADVI_49FNV3 are closed. No portal code changes were made
this session — all findings were investigative. Key result: the snapshot NNA geo drill
in DistributionTab.tsx is already correctly wired via `views.nna[period].geo.drill[state].by_city`
from partner_analytics JSON. N1+N2 wiring in ClientsTab.tsx is complete. N1-N2-RD task
order dependency is unblocked for 0.4.2_RD_AdvisorIntelligence.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] F5 Lambda fix** — emit `qtd` calendar window in leaderboard
   JSON so `periodToChartWindow('qtd')` can map to `'qtd'` directly instead of `'3M'` approximation.
2. **[0.4.0_DT_ClientPlatform] F1 redeploy** — rebuild and redeploy bd-portal-publisher per
   devops brief to surface `growth_decomposition` in portal GRO mode.
3. **[0.4.2_RD_AdvisorIntelligence] N1-N2-RD visual polish** — dependency now resolved,
   RD can review DT's panel implementation and polish visual layout per task order.
4. **[0.4.2_RD_AdvisorIntelligence] F2, F4** — projected bars and stacked bar (already
   issued task orders per COO session).

**Files to touch next:**
- None (all DE items complete for this project sprint)

**Do NOT:**
- Wire `nna_geo_drill` from `timeseries_chart.json` into the snapshot NNA donut — it is
  a time series and is correctly placed in the continuous view.
- Fix F5 frontend-side — the window mismatch cannot be resolved without a Lambda-side
  `qtd` calendar window addition.
