# ADVI-005 4C — Stacked Bar Primary + Rolling 1Y Secondary — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-03-04
**Portal DEV commit:** `0bceb64`

## Objective

Implement Advisors tab rolling flows redesign (Stream 4C):
- Primary view: stacked bar chart (inflows up / outflows down) per advisor per period
- Secondary view: rolling 1Y line chart sliced by period toggle
- Legacy fallback preserved when stacked_bar or rolling_1y keys absent

Gate status was CLEARED (bd-v2.15.1). Types added by DE at portal DEV `5125eb9`.

---

## Work Completed

### Imports

- Recharts: added `BarChart as RechartsBarChart`, `Bar`, `ReferenceLine`
- Types: replaced `AdvisorRollingFlowsResponse` with `AdvisorRollingFlowsResponseV2`;
  added `AdvisorBarEntry`, `AdvisorRolling1YSeries`, `StackedBarPeriodKey`

### New types + constants

- `type FlowsViewMode = 'primary' | 'secondary'`
- `STACKED_BAR_PERIOD_OPTIONS` — qtd/ytd/1y/3y/max with labels QTD/YTD/1Y/3Y/Max
- `FLOWS_VIEW_OPTIONS` — Stacked / 1Y Rolling

### New state

- `flowsView: FlowsViewMode` — defaults to `'primary'`
- `stackedBarPeriod: StackedBarPeriodKey` — defaults to `'ytd'`
- `flowsData` type upgraded from `AdvisorRollingFlowsResponse | null` to `AdvisorRollingFlowsResponseV2 | null`

### Rolling Flows panel

Header now shows view toggle (Stacked / 1Y Rolling) + period toggle (QTD/YTD/1Y/3Y/Max).
Content conditionally renders:
- `StackedBarChart` when `flowsView === 'primary' && flowsData?.stacked_bar`
- `Rolling1YChart` when `flowsView === 'secondary' && flowsData?.rolling_1y`
- Legacy `RollingFlowsChart` as fallback when new keys absent

### StackedBarChart (new component)

| Property | Value |
|----------|-------|
| Chart type | Recharts BarChart |
| Data source | `data.stacked_bar[period][role]` (AdvisorBarEntry[]) |
| Sort order | nna_net ascending (lowest leftmost, highest rightmost) |
| Inflows bar | `stackId="flows"`, fill: hsl(var(--success)), opacity 0.75 |
| Outflows bar | `stackId="flows"`, fill: hsl(var(--destructive)), opacity 0.75, dataKey="outflowsNeg" |
| Outflows encoding | Positive in JSON; negated client-side: `outflowsNeg = -e.outflows` |
| Reference line | y=0 at rgba(255,255,255,0.2) |
| X-axis | advisor_name, angle -45, 12-char truncation |
| Tooltip | Custom content showing advisor_name + inflows/outflows/nna_net |

Waterfall style: inflows segment 0→inflows, outflows segment inflows→(inflows + outflowsNeg).
Net position of bar = nna_net.

### Rolling1YChart (new component)

| Property | Value |
|----------|-------|
| Chart type | Recharts LineChart (same pattern as legacy RollingFlowsChart) |
| Data source | `data.rolling_1y[role]` (AdvisorRolling1YSeries[]) |
| Period slicing | `period` toggle controls x-axis cutoff date (rolling window stays 1Y) |
| Selection | Same `selectedAdvisorIds` set as leaderboard row clicks |
| Metric plotted | nna (per contract: NNA-only primary; inflows/outflows in series for future) |
| Tooltip | advisor_name + formatted NNA per date |

Period → startDate mapping:
- qtd: start of current calendar quarter
- ytd: Jan 1 of current year
- 1y: 365 days ago
- 3y: 3 years ago
- max: no cutoff (full history)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| stackId="flows" on both bars | Waterfall: inflows up from 0, outflows pull back from inflows top |
| flowsData typed as V2 (not V1) | Gate cleared; V2 extends V1 so backward compat holds |
| Legacy fallback path kept | Guard on stacked_bar/rolling_1y keys per 4C.5 requirement |
| Period toggle shared between primary and secondary | PRD: both views show period toggle; secondary uses it to slice x-axis |
| Default period: ytd | Most relevant business view; qtd too short, max too wide |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | 4C stacked bar + rolling 1Y | Yes — portal DEV `0bceb64` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

Portal DEV is 7 commits ahead of origin: `3dc9dc5`, `7df26bb`, `5125eb9`, `ed832db`, `5f42dc6`, `bdcd00c`, `0bceb64`.
`bunx tsc -b` clean.

---

## Next Steps

1. **[DE] Review 4C visual design** before DT pushes portal DEV.
2. **[RD 0.4.2] Task 6 — advi_c3_cla_snapshot** — CLA snapshot view fix in DistributionTab.
3. **[RD 0.4.2] Task 7 — advi_c1_geo_continuous** — GEO continuous NNA view.
4. **[RD 0.4.2] Task 9 — ADVI-004 C2+C4** — ADV continuous + CLA continuous (gated).
