# DEBT_1STRUN Scan -- 0.2.6_RD_Correlation
**Date:** 2026-03-23
**Scope:** portal/src/pages/Correlation/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | constants.ts | 6-20 | C1 Dead | Medium | `ASSET_CLASS_NAMES` is exported but never imported anywhere in the codebase. It is a static list of 13 asset classes superseded by the dynamic `data.tickers` array from the API. Removing it changes zero behavior. |
| 2 | constants.ts | 40-52 | C1 Dead | Medium | `EQUITY_SECTORS` is exported but never imported. Was likely planned for a sector correlation matrix that was never built. Pure dead code. |
| 3 | constants.ts | 55-63 | C1 Dead | Medium | `REGIONS` is exported but never imported. Same story as `EQUITY_SECTORS` -- planned geographic correlation matrix never materialized. |
| 4 | types.ts | 12-17 | C1 Dead | Low | `CorrelationPanelProps` interface is exported but never used by any component. `CorrelationMatrix` defines its own `CorrelationMatrixProps` inline. |
| 5 | types.ts | 19-23 | C1 Dead | Low | `CorrelationCellProps` interface is exported but never referenced. No component consumes it. |
| 6 | types.ts | 16 | C1 Dead | Low | `colorScheme` prop on `CorrelationPanelProps` declares options `'pink' | 'cyan' | 'green'` but no component reads or implements color scheme switching. |
| 7 | types.ts | 29-33 | C1 Dead | Low | `TickerPreset` interface is exported but never imported. `TICKER_PRESETS` in constants.ts uses `as const` and is consumed by its inferred type, not this interface. |
| 8 | hooks/useCorrelationData.ts | 22,54 | C1 Dead | Low | `refetch` is exposed by `useCorrelationData` return type but never destructured or called by any consumer. The hook's only consumer (`Correlation.tsx:32`) destructures `{ data, isLoading, error }`. |
| 9 | components/CorrelationMatrix.tsx | 26,36,55 | C1 Dead | Low | `dataAsOf` prop is declared on `CorrelationMatrixProps` and wired to `DataAsOfCompact`, but the parent (`Correlation.tsx:154`) never passes it. The `DataAsOfCompact` component renders nothing since `dataAsOf` is always `undefined`. |
| 10 | hooks/useCorrelationData.ts | 42 | C2 Deprecated | Low | Comment `// PHASE1_CR_REQ_001: CORRELATION DATA LOADING ENABLED` is a stale tracking comment from the initial build phase. The feature shipped; this marker serves no purpose now. |
| 11 | constants.ts | 67-75 | C4 Hardcoded | Medium | `CORRELATION_COLORS` uses hardcoded RGBA values (`rgba(236, 72, 153, ...)` and `rgba(34, 197, 94, ...)`) instead of referencing the theme's CSS custom properties. If the portal theme changes, these colors will not update. |
| 12 | components/CorrelationMatrix.tsx | 40-41 | C4 Hardcoded | Low | Cell size breakpoints (`56` vs `64` px) and font sizes (`11` vs `12` px) are magic numbers. The threshold `10` for switching sizes is also hardcoded with no documentation of why 10 is the cutoff. |
| 13 | components/CorrelationMatrix.tsx | 62 | C4 Hardcoded | Low | `min-h-[600px]` is an inline magic number for minimum matrix container height. |
| 14 | components/CorrelationMatrix.tsx | 96 | C4 Hardcoded | Low | Null-cell fallback color `rgba(128, 128, 128, 0.2)` is hardcoded inline rather than declared in `CORRELATION_COLORS` alongside the other scale values. |
| 15 | Correlation.tsx | 64,84 | C3 Duplication | Medium | The `PageHeaderCleanBadge` block (icon, title, description JSX) is copy-pasted identically in the loading state (lines 66-70), error state (lines 84-88), and normal render (lines 138-142) -- three copies of the same markup. Extracting the header above the conditional would eliminate all three duplicates. |
| 16 | components/TickerSelector.tsx | 70-74,104-107 | C3 Duplication | Low | Preset-active check logic (`validTickers.length === selectedTickers.length && validTickers.every(...)`) is duplicated: once in `currentPresetName` memo (line 70-74) and again in the render loop (line 105-107). |
| 17 | Correlation.tsx | 89-91 | C6 Stale Error | Medium | Error state shows a generic "Failed to load correlation data" with no detail from the `error` object. The `error.message` is available but discarded, giving the user no actionable information about what went wrong (network, auth, bad data shape, etc.). |

## Summary
- Total findings: 17
- By category: C1: 9, C2: 1, C3: 2, C4: 4, C5: 0 (None found), C6: 1
- High severity: 0
- Medium severity: 5 (#1, #2, #3, #11, #15, #17 -- 6 items)
- Low severity: 11
- Recommended priority fixes:
  1. **#15 (C3 Duplication):** Extract the repeated `PageHeaderCleanBadge` block above the loading/error/data conditionals. Single change, eliminates 3x duplication, reduces Correlation.tsx by ~20 lines.
  2. **#1-3 (C1 Dead):** Remove `ASSET_CLASS_NAMES`, `EQUITY_SECTORS`, and `REGIONS` from constants.ts. They are fully unused and mislead developers into thinking static asset lists drive the page (the API provides tickers dynamically).
  3. **#11 (C4 Hardcoded):** Migrate `CORRELATION_COLORS` to use CSS custom properties from the theme so the matrix respects portal-wide theme changes.

**C5 - Orphaned Infrastructure:** None found. All routes, lazy-loaded chunks, and API hooks in this page directory are actively used.

## Fixes Applied

All 17 findings addressed in same session. Disposition:

| # | Status | Action |
|---|--------|--------|
| 1-3 | FIXED | Removed `ASSET_CLASS_NAMES`, `EQUITY_SECTORS`, `REGIONS` from constants.ts |
| 4-7 | FIXED | Removed `CorrelationPanelProps`, `CorrelationCellProps`, `colorScheme`, `TickerPreset` from types.ts |
| 8 | FIXED | Removed `refetch` from useCorrelationData return type and value |
| 9 | FIXED | Removed `dataAsOf` prop from CorrelationMatrix, removed unused `DataAsOfCompact` import |
| 10 | FIXED | Removed stale `PHASE1_CR_REQ_001` tracking comment |
| 11 | FLAGGED | Added TODO comment for future CSS custom property migration; RGBA values left as-is (functional, theme migration is a separate initiative) |
| 12-13 | DEFERRED | Magic numbers left as-is; extracting to constants for single-use sizing adds indirection without value |
| 14 | FIXED | Moved inline null-cell color to `CORRELATION_COLORS.nullCell` |
| 15 | FIXED | Extracted `PageHeaderCleanBadge` above loading/error/data conditionals (1 render, 0 duplication) |
| 16 | FIXED | Extracted `isPresetActive()` helper, used in both memo and render loop |
| 17 | FIXED | Error state now displays `error.message` for actionable feedback |

Build verified: zero Correlation-related errors (pre-existing Attribution errors unrelated).
