# ADVI_ANONYM P2 -- Pseudonymized UI Indicators

**Date:** 2026-04-01
**Agent:** 0.4.2_RD_AdvisorIntelligence
**Task Order:** ADVI_ANONYM.006.rd-pseudonymized-ui-indicators
**Portal DEV Commit:** `2ebf55b`

## Summary

Added `(pseudonymized)` indicators to four UI surfaces, gated on `canSeeCleartext()` from AuthContext. Advisor/user tier sees the indicators; internal/admin users do not.

## Changes

### 1. DistributionTab.tsx
- Added `useAuth` import
- **NNA Diverging View** (`ContinuousNnaDivergingView`): Added `(pseudonymized)` span in the drill header label when `isDrilled && cohort === 'adv' && !canSeeCleartext()`
- **Continuous Chart View** (`ContinuousChartView`): Same indicator in the hero metrics subtitle when drilled into ADV client-level data

### 2. ClientsTab.tsx
- `useAuth` was already imported
- **L2 ClientsTable**: Added `(pseudonymized)` span in the "Client" column header when `!canSeeCleartext()`
- **L4 AccountsTable**: Added `(pseudonymized)` span in the "Account" column header when `!canSeeCleartext()`

### 3. ClientDetailPage.tsx
- Added `useAuth` import
- Added `(pseudonymized)` span next to `clientLabel` in the page header `<h1>` when `!canSeeCleartext()`

## Export Disable (Req 2b)

DistributionTab has no CSV/clipboard export functionality yet. Requirement 2b (disable export for client-level drill data) is not applicable at this time -- will be addressed when export is added.

## Verification

- `bunx tsc -b` passes clean (no errors)
- All indicators use muted `text-white/30` styling -- informational, not dominant
- All logic gated strictly on `canSeeCleartext()` -- no hardcoded tier/role checks
