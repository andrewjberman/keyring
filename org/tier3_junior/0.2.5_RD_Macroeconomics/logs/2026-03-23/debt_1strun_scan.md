# DEBT_1STRUN Scan — 0.2.5_RD_Macroeconomics
**Date:** 2026-03-23
**Scope:** portal/src/pages/Macroeconomics/
**Status:** ALL 31 FINDINGS FIXED (build verified, 0 new errors)

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | constants.ts | 8-53 | C1 Dead | High | `MONTHS`, `QUARTERS`, `MONTHLY_INDICATORS`, `QUARTERLY_INDICATORS` exported but never imported by any file. Heatmap uses Yang API data dynamically and defines its own local `MONTHS`. ~45 lines of dead exports. |
| 2 | constants.ts | 56-62 | C1 Dead | Medium | `STATUS_COLORS` exported but never imported. Qualitative status system (Tame/Hot/Mixed) fully replaced by percentile-based color system in `utils/percentileColor.ts`. |
| 3 | constants.ts | 100-113 | C1 Dead | Medium | `YIELD_CURVE_TENORS` exported but never imported. `YieldCurveTab` defines its own `TENOR_ORDER` + `TENOR_TO_YEARS` inline. |
| 4 | constants.ts | 116-142 | C1 Dead | Medium | `ASSESSMENT_COLORS` record exported but never imported by any component. 27 lines of dead code. |
| 5 | types.ts | 6-13 | C1 Dead | Medium | `IndicatorStatus` and `EconomicIndicatorCell` types only referenced by dead `STATUS_COLORS` in constants.ts. Transitive dead code. |
| 6 | types.ts | 16-19 | C1 Dead | Medium | `EconomicIndicatorRow` interface exported but never imported anywhere. |
| 7 | types.ts | 22-30 | C1 Dead | Medium | `MacroSummary` interface exported but never imported. Old executive summary type with no consumers. |
| 8 | types.ts | 42-63 | C1 Dead | Medium | `VIXData`, `VIXTermStructurePoint`, `VIXHistoricalPoint` — three interfaces superseded by types in `@/api/portal-proxy`. `VolatilityTab` imports from the API module, not from local types. |
| 9 | tabs/VolatilityTab.tsx | 413 | C1 Dead | Low | `_regimeColors` parameter renamed with underscore prefix to suppress unused warning. Parameter is received but never used in `HistoricalChartTooltip`. |
| 10 | tabs/VolatilityTab.tsx | 495 | C1 Dead | Low | `_config = VOLATILITY_INDEX_CONFIG[indexType]` assigned in `HistoricalChart` but never referenced. Dead variable. |
| 11 | tabs/YieldCurveTab.tsx | 319 | C1 Dead | Low | `void (thirtyYear && tenYear ? thirtyYear.current - tenYear.current : 0)` — spread calculation explicitly voided. Dead computation with no consumer. |
| 12 | components/MacroTimeSeriesModal.tsx | 143-153 | C3 Duplication | High | Local `formatValueWithUnit` duplicates `utils/percentileColor.ts:110-126` with different formatting logic (modal uses `.toFixed(2)` for %, percentileColor uses `.toFixed(1)`). Active drift between two formatters producing different output for same inputs. |
| 13 | components/MacroTimeSeriesModal.tsx | 159-203 | C3 Duplication | High | Local `getPercentileColor` and `getPercentileLabel` duplicate `utils/percentileColor.ts:20-105` but add sign-awareness (positive vs negative indicators). The shared utility lacks this, so the modal cannot use it — but the duplication means color logic lives in two places with different return values. |
| 14 | panels/MacroHeatmap.tsx | 33 | C3 Duplication | Medium | Local `const MONTHS = [...]` duplicates `constants.ts:8`. If month names ever change (localization), two copies must be updated. |
| 15 | panels/MacroHeatmap.tsx | 553 | C3 Duplication | Low | `monthOrder` array inside `IndicatorRowPosition` is a third copy of the months list (also in MacroHeatmap line 33 and constants.ts line 8). |
| 16 | tabs/YieldCurveTab.tsx | 92-106 | C3 Duplication | Medium | `TENOR_ORDER` and `TENOR_TO_YEARS` duplicate the information in `YIELD_CURVE_TENORS` from constants.ts. Two representations of the same tenor data in two files. |
| 17 | tabs/YieldCurveTab.tsx | 245-246 | C4 Hardcoded | High | `currentMonthIdx = months.length - 1` hardcodes the "current" month to December. `oneMonthAgoIdx = currentMonthIdx - 1` hardcodes to November. Should dynamically detect the latest month with data from Yang's API. Yields stale current/1M-ago curves for 11 months of the year. |
| 18 | tabs/VolatilityTab.tsx | 512 | C4 Hardcoded | Low | Magic number `3` in data sampling filter (`idx % 3 === 0`). Sampling ratio is not configurable and not documented as to why 3 was chosen. |
| 19 | tabs/VolatilityTab.tsx | 517-518 | C4 Hardcoded | Low | Magic numbers `compressionThreshold = 25` and `compressionStrength = 0.3` for VIX asymmetric scale compression. Should be named constants or derived from percentile data. |
| 20 | tabs/YieldCurveTab.tsx | 120 | C4 Hardcoded | Low | Tooltip background `#1e1e2d` is a hardcoded hex color. Other tooltips use `hsl(var(--bg-header))` CSS variable. Inconsistent with theme system. |
| 21 | tabs/YieldCurveTab.tsx | 533 | C4 Hardcoded | Low | `maxChange = 30` bps used to scale yield change bar heights. No documentation on why 30, and extreme moves would clip silently. |
| 22 | tabs/VolatilityTab.tsx | 714-715 | C4 Hardcoded | Medium | `T17:00:00-05:00` hardcoded Eastern Standard Time offset for footer timestamp. Does not account for EDT (-04:00) during daylight saving, producing incorrect timestamps ~7 months/year. |
| 23 | utils/percentileColor.ts | 71-105 | C5 Orphaned | Medium | `getPercentileRange` and `getPercentileLabel` are exported but never imported by any consumer. MacroTimeSeriesModal defines its own sign-aware versions instead of extending these. |
| 24 | panels/MacroHeatmap.tsx | 77-83 | C6 Stale Error | Medium | `getMacroData()` error is caught and logged to console only (`console.error`). No error state is set. Component falls through to "No data available" which does not distinguish load failure from genuinely empty data. User cannot know the API call failed. |
| 25 | tabs/YieldCurveTab.tsx | 221-223 | C6 Stale Error | Medium | FRED `getYieldCurveData()` error silently swallowed via `.catch(err => { console.warn(...); return null })`. User never knows 1Y historical curve failed to load; checkbox appears disabled with "(N/A)" but no explanation. |
| 26 | panels/MacroHeatmap.tsx | 77 | C2 Deprecated | Low | `console.log('[MacroHeatmap] Macro data loaded:', data)` — debug logging left in production code. Logs full data payload to console on every page load. |
| 27 | tabs/YieldCurveTab.tsx | 238-240 | C2 Deprecated | Low | Debug `console.log`/`console.warn` statements with emoji characters (`\u2705`, `\u26A0\uFE0F`). Violates CLAUDE.md rule #13 (no emojis in code that runs on AWS or production). |
| 28 | components/MacroTimeSeriesModal.tsx | 305, 357 | C2 Deprecated | Low | Debug `console.log` with emoji checkmarks (`\u2705`) in production code. Same CLAUDE.md rule #13 violation. |
| 29 | Macroeconomics.tsx | 26 | C2 Deprecated | Low | Stale phase-tracking comment `// \u2705 PHASE1_MC_REQ_002: VOLATILITY DATA LOADING ENABLED`. Phase is long complete; comment is outdated and uses emoji. |
| 30 | panels/MacroHeatmap.tsx | 71 | C2 Deprecated | Low | Stale phase-tracking comment `// \u2705 PHASE1_MC_REQ_001: MACRO DATA LOADING ENABLED`. Same issue as #29. |
| 31 | tabs/YieldCurveTab.tsx | 216 | C2 Deprecated | Low | Stale phase-tracking comment `// \u2705 PHASE1_MC_REQ_001: MACRO DATA LOADING ENABLED`. Same issue as #29. |

## Summary
- Total findings: 31
- By category: C1: 11, C2: 6, C3: 5, C4: 6, C5: 1, C6: 2
- High severity: 4
- Medium severity: 13
- Low severity: 14
- Recommended priority fixes:
  1. **#17 — YieldCurveTab hardcoded month index** (C4 High): Causes the yield curve to show stale Dec/Nov data for 11 months of the year. Should dynamically find the latest month with data from the API response.
  2. **#12 + #13 — MacroTimeSeriesModal duplicated utilities** (C3 High): Two independent implementations of `formatValueWithUnit` and `getPercentileColor` with different output for the same inputs. Consolidate sign-awareness into `utils/percentileColor.ts` and delete the modal's local copies.
  3. **#1-8 — Dead types and constants** (C1 Medium, aggregate): ~150 lines of dead exports across `constants.ts` and `types.ts` from the old qualitative-label system. Safe to remove in a single cleanup pass since no file imports them.
