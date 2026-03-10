# ADVI_49FNV3 — F2, F4, F6, F7, N1-N2-RD Complete — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-09
**Portal DEV commit:** `594c3f6`

## Objective

Execute all 5 pending ADVI_49FNV3 task orders: F2 (projected ghost bars), F4 (stacked bar top 10),
F6 (unassigned sorting), F7 (zebra striping), N1-N2-RD (firm dashboard + advisor book visual polish).

---

## Work Completed

### 1. F6 + F7 — Pre-Applied (DT commit `1dc96b5`)

Both were already implemented by DT in portal DEV commit `1dc96b5`:
- **F6:** `PINNED_BOTTOM_NAMES = new Set([FIRM_ACCOUNT_NAME, 'Unassigned'])` at AdvisorsTab.tsx:80.
  Leaderboard separates pinned entries (lines 688-698), renders them in a dimmed "Unranked" section.
- **F7:** `bg-white/[0.025]` on odd leaderboard rows at line 771. Matches SecurityScanner pattern.

Marked both task orders as `complete`. No code changes needed.

### 2. F4 — Top Ten Advisors Stacked Bar (New Component)

Added `TopTenStackedBar` component to AdvisorsTab.tsx. Renders inside Panel 1 (Top Performers)
when `flowsData?.stacked_bar?.[period]?.[role]` data is available. Falls back to Top3Highlights
cards when stacked_bar data absent.

| Property | Value |
|----------|-------|
| Chart type | Recharts ComposedChart with stackOffset="sign" |
| Data source | `flowsData.stacked_bar[period][role]` (AdvisorBarEntry[]) |
| Sort | nna_net descending, tie-break: advisor_name ascending, top 10 |
| Inflows bar | stackId="flows", fill #2563EB, opacity 0.8 |
| Outflows bar | stackId="flows", fill #DC2626, dataKey outflowsNeg (negated client-side) |
| NNA dash | RechartsLine with custom dot — gold (#F59E0B) horizontal dash at y=nna_net |
| X-axis | advisor_name truncated at 12 chars, -45 degree angle |
| Tooltip | advisor_name, inflows, outflows, NNA (signed + colored) |

### 3. N1-N2-RD — Visual Polish

DT commit `1dc96b5` implemented functional N1 (firm dashboard) and N2 (advisor book) panels.
RD polish applied:

| Change | File | Line |
|--------|------|------|
| Back button: "All Advisors" -> "Back to Firm Overview" | ClientsTab.tsx | L2 back button |
| Zebra striping on AdvisorSummaryTable rows | ClientsTab.tsx | `bg-white/[0.025]` on odd rows |
| Zebra striping on L2 ClientsTable rows | ClientsTab.tsx | same pattern |

### 4. F2 — Projected Ghost Bars (PartnerAnalytics.tsx)

Added projection computation for the current incomplete period across all three panel views.

**Helper functions added:**
- `computePeriodDays(granularity, periodKey)` — returns totalDays + elapsedDays for monthly/quarterly/annually
- `currentPeriodKey` memo — identifies today's period

**AUA view ghost bars:**
- `augmentedAuaData` memo adds `{cat}_ghost` fields (e.g., `NMNC_ghost`, `NMEC_ghost`)
- Formula: `projected = actual * (totalDays / elapsedDays)`, capped at `max(actual, prior * 1.5)`
- Ghost rendered as additional stacked Bars with fillOpacity 0.25
- Only non-zero for the current incomplete period

**NNA view ghost bars:**
- `augmentedNnaData` memo adds `inflow_ghost` and `outflow_ghost` fields
- Inflow ghost extends upward (blue, 25% opacity)
- Outflow ghost extends downward (red, 25% opacity)
- Net line does NOT get a ghost (per task order)

**GRO view dashed extensions:**
- `augmentedGroData` memo adds a projected data point after the last actual point
- Three additional Line components with `strokeDasharray="6 3"` for market_proj, nna_proj, total_proj
- Dashed segments connect last actual to projected value using `connectNulls={false}`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| F6/F7: mark complete without changes | DT already implemented in `1dc96b5`; code verified correct |
| F4: ComposedChart (not BarChart) | Needed for NNA dash overlay (Line component) alongside stacked bars |
| F4: NNA dash via Line + custom dot | Cleanest Recharts pattern for per-bar markers without Scatter complexity |
| F2: Cap formula `max(actual, prior * 1.5)` | Prevents ghost from being negative if actual already exceeds 1.5x prior |
| F2: `any` type for augmented AUA data | Dynamic ghost key generation (`${cat}_ghost`) not expressible in static type; `any` cast avoids TS errors on downstream consumers |
| N1-N2: "Back to Firm Overview" | Task order explicitly requested this text over the DT's "All Advisors" |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | F4: TopTenStackedBar component + Panel 1 conditional rendering | Yes -- portal DEV `594c3f6` |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | N1-N2: back button text + zebra striping | Yes -- portal DEV `594c3f6` |
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | F2: projection helpers + augmented data memos + ghost bars + GRO dashed lines | Yes -- portal DEV `594c3f6` |
| Task orders (5 files) | All marked complete | Local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

All 5 ADVI_49FNV3 task orders are complete. Portal DEV commit `594c3f6` contains F4 stacked bar,
F2 projected ghost bars (AUA + NNA + GRO), and N1-N2 visual polish. `bunx tsc -b` clean.
F6 and F7 were pre-applied by DT. DE review needed before DT pushes.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Review commit `594c3f6`** -- F2 projection logic, F4 stacked bar visual, N1-N2 polish.
2. **[0.4.0_DT_ClientPlatform] Push portal DEV after DE review** -- QA gate.
3. **[0.4.2_RD_AdvisorIntelligence] No further ADVI_49FNV3 task orders pending** -- await next assignment.

**Do NOT:**
- Push portal DEV -- DT is the push gate after DE reviews
- Implement L3/L4 visual panels for N1-N2 -- Phase 2a only per task order constraint
