# ADVI_MVPLVL-004 P4 Books Tab Views — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-16
**Portal DEV commit:** `478baea`
**Task Order:** `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_MVPLVL.004.p4-books-tab-views.md`
**Thread:** `org/threads/ADVI_MVPLVL-004-p4-books-tab-alignment/`

## Objective

Implement Books Tab L3/L4 view enhancements: paired Mix + Concentration pie panels with linked
selection, compact AUA/NNA time series charts, and advisor listing UI consistency (4h). All
inline in ClientsTab.tsx.

---

## Work Completed

### 1. Mix + Concentration Snapshot Pies (4e/4f)

New inline `CompositionPies` component renders side-by-side donut charts from `BooksCompositionResponse`:

| Feature | Implementation |
|---------|---------------|
| Mix pie | Recharts PieChart with Cell per asset class, donut style (innerRadius/outerRadius) |
| Color mapping | `MIX_PIE_COLORS` — equity=#6366F1, fixed_income=#10B981, structured_notes=#F59E0B, cash=white/35, other=#EF4444 |
| Click-to-filter | Click Mix slice toggles `selectedAssetClass`; same click deselects |
| Opacity dimming | Non-selected slices render at fillOpacity 0.3 |
| Concentration pie | Filters `items[]` by `selectedAssetClass` when set; shows all when null |
| Other bucket | Shown in concentration pie only when no filter is active |
| Legend | Clickable legend rows with color dots, labels, and pct values |
| Compact mode | `compact` prop for L4 (smaller pie radius, single-column layout) |

**Wired at:**
- L3: After Accounts Table, before Mix Timeseries panels
- L4: Inside account detail section, after metrics grid

**Data fetching:**
- L3: `getBooksRelationshipComposition(clientKey)` in `useEffect` on `[clientKey]`
- L4: `getBooksAccountComposition(selectedAccountId)` in `useEffect` on `[selectedAccountId]`

### 2. Compact AUA/NNA Time Series (4g)

New inline `CompactTimeSeriesChart` component renders composed chart:

| Feature | Implementation |
|---------|---------------|
| AUA | Recharts Area with gradient fill, left Y-axis |
| NNA | Recharts Bar, right Y-axis, green (#10B981) at 60% opacity |
| Window toggle | Local state `1Y/3Y/Max`, client-side filtering of daily data |
| X-axis | Date labels formatted as "MMM 'YY", ~6 ticks |
| Tooltip | Standard chart tooltip with formatted currency values |
| Compact mode | `compact` prop for L4 (200px vs 280px height) |

**Wired at:**
- L3: After Concentration Timeseries panel, before L4 drill
- L4: Inside account detail section, after composition pies

**Data fetching:**
- L3: `getBooksRelationshipTimeseries(clientKey)` in `useEffect` on `[clientKey]`
- L4: `getBooksAccountTimeseries(selectedAccountId)` in `useEffect` on `[selectedAccountId]`

### 3. Advisor Listing N1 Redesign (4h)

Rewrote `AdvisorSummaryTable` to match 3d leaderboard (AdvisorsTab.tsx) visual design:

| Before | After |
|--------|-------|
| HTML table with alternating rows | Flex card-like rows with generous padding |
| Plain rank number | Rank badges (gold/silver/bronze for top 3) |
| Plain NNA text | Bold NNA with `hsl(var(--success))` / `text-red-400` coloring |
| Plain growth % | Gradient pills: `bg-emerald-500/15` + ArrowUpRight / `bg-red-500/15` + ArrowDownRight |
| Table header row | Sort header bar ("Ranked by AUA") matching 3d style |
| `formatCurrency` for NNA | `formatNumberTo3Digits` for compact NNA display |

Columns: Rank, Name, AUA, Clients, NNA, Growth % — matches 3d leaderboard column structure.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Shared `selectedAssetClass` between Mix pies and Mix timeseries at L3 | Clicking equity in the pie should filter both the concentration pie and the timeseries panels |
| Separate `selectedAssetClassL4` state for L4 | L4 is independent of L3 selection — account-level filter shouldn't affect relationship-level |
| Client-side window filtering for timeseries | Fetch full history once, filter locally for 1Y/3Y/Max — avoids redundant API calls |
| No sort interactivity on advisor table | 3d leaderboard has sort buttons, but Books tab advisor table is always sorted by AUA desc; keeping it simple |
| `compact` prop on both components | L4 space is constrained inside the account detail panel; smaller charts avoid scroll fatigue |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Add imports (recharts, lucide, API fns), L3/L4 data fetching, CompositionPies + CompactTimeSeriesChart components, AdvisorSummaryTable redesign | Yes — portal DEV `478baea` |

---

## Blockers

None. Lambda endpoints (partners-api-v1.1.0) not yet deployed for composition/timeseries, but
endpoints are already registered in advisor-intelligence.ts from prior DE work. Panels will show
loading state until data is available.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`
**TypeScript:** `bunx tsc -b --noEmit` — zero errors

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] QA gate** — verify L3/L4 composition pies render correctly with live data once Lambda deployed
2. **[0.4.0_DS_ClientPlatform] Lambda deploy** — partners-api-v1.1.0 for composition + timeseries endpoints
3. **[0.4.2_RD_AdvisorIntelligence] Post-deploy** — visual QA, verify linked selection works end-to-end

**Do NOT:**
- Modify L2 (advisor-level) composition — deferred per task order constraint
- Add sort interactivity to advisor table — not in scope for 4h
