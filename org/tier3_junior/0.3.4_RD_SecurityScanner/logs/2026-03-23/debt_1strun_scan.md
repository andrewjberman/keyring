# DEBT_1STRUN Scan — 0.3.4_RD_SecurityScanner
**Date:** 2026-03-23
**Scope:** portal/src/pages/SecurityScanner/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | utils/quintileUtils.ts | 48-65 | C1 Dead | Medium | `formatPercentileCell` is exported but never imported anywhere in the codebase. The function wraps `getPercentileBackground` + `NULL_DISPLAY` + `NULL_TEXT_CLASS` into a combined return object, but all three AG Grid tabs use the individual helpers directly instead. |
| 2 | utils/quintileUtils.ts | 20 | C1 Dead | Low | `NULL_TEXT_CLASS` is exported but never imported by any file. Only `NULL_DISPLAY` from the same module is consumed (by UniverseScannerTab). |
| 3 | components/FactorChip.tsx | 23 | C2 Deprecated | Low | Uses native `title` attribute for tooltip (`title={\`${name} (${category})\``). ScannerHeaderPanel was migrated to the canonical `<Tooltip>` component (commit `8c1ab08`, 2026-03-06). FactorChip was not updated to match, leaving an inconsistent tooltip pattern. |
| 4 | tabs/UniverseDataTab.tsx, tabs/UniverseScannerTab.tsx | 24-28, 36-40 | C3 Duplication | Medium | `US_ONLY_UNIVERSES` (`Set(['sp500', 'r1000', 'r1000v'])`) is defined identically in both tab files. If the universe list changes, both must be updated in lockstep or they will drift. Should be a single export in `types.ts` or a shared util. |
| 5 | tabs/UniverseDataTab.tsx, tabs/UniverseScannerTab.tsx | 171-181, 333-343 | C3 Duplication | Medium | The `.scanner-grid` AG Grid zebra-stripe `<style>` block (3 CSS rules for even/odd/hover row backgrounds) is copy-pasted identically in both tabs. A shared CSS class or a single injected stylesheet would eliminate the duplication. |
| 6 | tabs/UniverseDataTab.tsx, tabs/UniverseScannerTab.tsx | 21, 34 | C3 Duplication | Low | `ModuleRegistry.registerModules([AllCommunityModule])` is called at module scope in both files. AG Grid tolerates double registration, but it is unnecessary — a single registration in the page orchestrator or a shared init module would be cleaner. |
| 7 | components/ScannerHeaderPanel.tsx, tabs/FactorBankTab.tsx | 56-63, 50-57 | C3 Duplication | Low | Factor sort logic (canonical category index primary, coverage descending secondary) is duplicated in both components. Same comparator function written twice. |
| 8 | hooks/useScannerState.ts | 71-81, 88-99 | C3 Duplication | Low | `setEqualWeight` and `initializeDefaults` contain nearly identical weight distribution logic (`Math.floor(100/n)` + remainder to first item). Only difference is `initializeDefaults` also sets `selectedFactors`. |
| 9 | hooks/useScannerApi.ts | 31, 42, 51 | C4 Hardcoded | Low | `staleTime: 5 * 60 * 1000` is repeated in all three React Query hooks with no shared constant. If the refresh policy changes (e.g., the factor metadata endpoint moves to daily updates), three call sites must be found and updated. |
| 10 | tabs/UniverseDataTab.tsx | 158 | C4 Hardcoded | Low | AG Grid container height hardcoded to `600px`. UniverseScannerTab uses `700px` (line 320). Neither adapts to viewport height, and the difference between tabs is unexplained. |
| 11 | tabs/UniverseScannerTab.tsx | 320 | C4 Hardcoded | Low | AG Grid container height hardcoded to `700px`. See finding #10. |
| 12 | SecurityScanner.tsx | 31 | C4 Hardcoded | Low | `DEFAULT_CATEGORIES` array hardcodes 5 category strings (`value`, `growth`, `quality`, `momentum`, `size`). These seed the initial factor selection but are not derived from any config or the factor metadata response. If categories are renamed server-side, the defaults silently fail (no factors match). |
| 13 | utils/quintileUtils.ts | 20, 48-65 | C5 Orphaned | Medium | Two exported symbols (`NULL_TEXT_CLASS`, `formatPercentileCell`) have no consumers. They appear to be infrastructure prepared for a rendering pattern that was never adopted — the AG Grid tabs use inline `cellStyle` functions with the lower-level helpers instead. |
| 14 | tabs/UniverseDataTab.tsx | 128-138 | C6 Stale Error | Medium | Error state shows "Failed to load universe data. Please refresh." with no error details, no retry button, and no console logging. The `error` object from React Query is available but unused, so users and developers get zero diagnostic signal on failure. |
| 15 | tabs/UniverseScannerTab.tsx | 270-280 | C6 Stale Error | Medium | Same generic error message pattern as finding #14. "Failed to load scanner data. Please refresh." — no error details exposed. |
| 16 | tabs/FactorBankTab.tsx | 152-162 | C6 Stale Error | Medium | Same generic error message pattern. "Failed to load factor metadata. Please refresh." — no actionable feedback. |
| 17 | hooks/useScannerApi.ts | 27-33 vs 37-44 vs 46-53 | C6 Stale Error | Low | `useFactorMetadata` sets `retry: 2` but `useUniverseData` and `useUniverseScanner` omit `retry`, falling back to React Query default (3). The inconsistency is undocumented — either all three should share a policy or the divergence should be intentional and commented. |

## Summary
- Total findings: 17
- By category: C1: 2, C2: 1, C3: 5, C4: 4, C5: 1, C6: 4
- High severity: 0
- Recommended priority fixes:
  1. **Finding #4 — `US_ONLY_UNIVERSES` duplication**: Extract to a single shared constant. Highest drift risk because changes to supported universes would silently break one tab if only the other is updated.
  2. **Finding #5 — duplicated AG Grid `<style>` block**: Extract to a shared CSS file or component. Both tabs render these styles at runtime; a mismatch would cause visual inconsistency between tabs.
  3. **Findings #14-16 — generic error states**: Surface the error message from React Query and add a retry button. Three tabs all swallow errors identically — users currently have no way to self-diagnose or recover without a full page refresh.
