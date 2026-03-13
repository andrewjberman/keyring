# ADVI_MVPLVL 2i: Time Window State Lift — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-13
**Portal DEV commit:** `2639c7d`
**Workspace CLOUD commit:** pending (DT)

## Objective

Execute PRD item 2i: remove Distribution Tab's independent time window toggle and
inherit the time window from the Assets Overview header panel (PartnerAnalytics).

---

## Work Completed

### 1. State Lift to AdvisorIntelligence.tsx

Added `timeWindow` + `setTimeWindow` state to `AdvisorIntelligence.tsx` alongside
existing `granularity`. Threaded as props:
- `timeWindow` + `onTimeWindowChange` to `PartnerAnalytics`
- `timeWindow` to `DistributionTab`

### 2. PartnerAnalytics.tsx — Use Props Instead of Local State

- Removed `const [timeWindow, setTimeWindow] = useState<TimeWindow>('1Y')`
- Added `timeWindow: TimeWindow` and `onTimeWindowChange: (w: TimeWindow) => void` to `PartnerAnalyticsProps`
- Replaced `setTimeWindow(opt)` with `onTimeWindowChange(opt)` in the toggle click handler

### 3. DistributionTab.tsx — Remove Independent Toggle, Use Inherited Value

- Removed `const [window, setWindow] = useState<ChartWindowOption>('1Y')`
- Added `const window: ChartWindowOption = timeWindow` (maps inherited prop to existing local variable name for minimal downstream changes)
- Removed the entire `{/* Window Toggle -- continuous mode only */}` JSX block (22 lines of toggle UI)
- Added `timeWindow: TimeWindow` to `DistributionTabProps`
- `WINDOW_OPTIONS` const retained (still used by sub-components for day-count lookups)

### 4. TypeScript Verification

`bunx tsc -b --noEmit` — clean, zero errors.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Map `TimeWindow` to `ChartWindowOption` via alias, not type change | `TimeWindow` ('1Y'\|'3Y'\|'Max') is a subset of `ChartWindowOption` ('3M'\|'6M'\|...\|'Max'). Sub-components use `ChartWindowOption` for window config lookups. Aliasing avoids touching 10+ internal function signatures. |
| Keep `WINDOW_OPTIONS` array in DistributionTab | Still used by `ContinuousChartView`, `ContinuousNnaChartView`, `ContinuousNnaDivergingView`, `ClaContinuousView` for day-count filtering. |
| Default `'1Y'` set in AdvisorIntelligence.tsx | Matches PRD 1a-i requirement (was previously `'3Y'` in PartnerAnalytics). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx` | Add `timeWindow` state, thread to PartnerAnalytics + DistributionTab | Yes — portal DEV `2639c7d` |
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | Remove local `timeWindow` state, use `timeWindow`/`onTimeWindowChange` props | Yes — portal DEV `2639c7d` |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Remove local `window` state + toggle UI, use `timeWindow` prop | Yes — portal DEV `2639c7d` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`

ADVI_MVPLVL 2i is fully delivered. The time window is now a single source of truth
in `AdvisorIntelligence.tsx`. Changing the Window toggle in the Assets Overview header
(1Y/3Y/Max) immediately updates both the PartnerAnalytics chart and the Distribution
Tab continuous view. The Distribution Tab no longer has its own window toggle.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commit `2639c7d` queued
2. **[0.4.0_DT_ClientPlatform] Commit this log to CLOUD**
