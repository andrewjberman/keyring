# DEBT_1STRUN Scan -- 0.3.1_RD_PortfolioManagement
**Date:** 2026-03-23
**Scope:** portal/src/pages/PortfolioManagement/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | hooks/useOptimizationAutoSave.ts | 120-127 | C6 Stale Error | High | Retry branch logs retry count but does nothing ("Will retry on next interval"). Error state persists and interval fires unchanged, creating false impression of retry behavior and potential infinite retry loop. |
| 2 | hooks/useAutoSave.ts | 86-103 | C6 Stale Error | High | `setTimeout(async () => {...}, RETRY_DELAY)` returns a promise that is never awaited. If retry mutation throws, the error is swallowed. Floating promise violation. |
| 3 | hooks/usePortfolioStore.ts + usePortfolioEditStore.ts + usePortfolioManagementState.ts | 15-18 / 19-22 / 44-47 | C3 Duplication | High | `deriveAction()` duplicated 3 times with identical logic but different threshold sources (0.01 literal vs WEIGHT_THRESHOLD constant). If threshold logic changes, all three must update. Extract to shared utility. |
| 4 | hooks/usePortfolioManagementState.ts + usePortfolioStore.ts | 51-87 / 369-433 | C3 Duplication | High | `calculateSummaryStats()` duplicated with slightly different netTurnover formula (one divides by 2, one doesn't). Risk of inconsistent reporting. |
| 5 | hooks/useRiskCalculations.ts + useFinalSummaryCalculations.ts | 36-81 / 44-75 | C3 Duplication | High | Near-identical `computeExposureVector()` / `computeActiveExposures()` compute same 12-factor exposure vector with different naming. Could drift under separate maintenance. |
| 6 | tabs/LookupTab.tsx | 1-31 | C1 Dead / C5 Orphaned | High | Entire component is a non-functional stub -- renders only placeholder text, accepts `onAddToTrade` callback but never calls it. Registered as tab but provides zero functionality. |
| 7 | components/ExecuteSaveButton.tsx | 32 | C1 Dead | High | Emoji character U+26A0 in badge text violates CLAUDE.md rule #13 (no emojis in production code). Breaks CloudWatch log queries on Windows. |
| 8 | components/UploadPortfolioModal.tsx | 194-276 | C6 Stale Error | High | Complex timeout/retry logic with silent exception suppression. Nested try-catch at lines 253-258 swallows actual error; if cache load fails, toast.error shows generic message without original error details. |
| 9 | tabs/RebalanceTab.tsx + TradeTab.tsx | 42-61 / 104-122 | C3 Duplication | Medium | `handleLoadVersion()` duplicated -- both call `loadVersionMutation.mutateAsync()`, then `store.loadVersion()`, then close modal and show toast. Extract to shared hook. |
| 10 | tabs/RebalanceTab.tsx + TradeTab.tsx | 63-97 / 124-157 | C3 Duplication | Medium | File upload + confirmation logic (`handleFileSelect`, `handleUpload`, `handleConfirmUpload`) duplicated with identical patterns across both tabs. |
| 11 | tabs/RebalanceTab.tsx + TradeTab.tsx | 100-109 / 274-297 | C3 Duplication | Medium | Filter + sort logic for securities/trades duplicated (search ticker/name, action filter, sector filter). Should share a single memoized hook. |
| 12 | tabs/AlphaTab.tsx + SectorTab.tsx + ModelTab.tsx | 114-127 / 71-82 / 81-93 | C3 Duplication | Medium | Identical 3-state sort logic (click desc -> asc -> default) duplicated across all three tabs. Extract to `use3StateSort()` hook. |
| 13 | hooks/usePortfolioStore.ts | 148-236 | C3 Duplication | Medium | Three nearly identical normalization blocks (loadAutoSave, loadVersion, loadUploadData) compute finalWeight, tradeWeight, action, isOverridden independently. If normalization changes, all three must update. |
| 14 | PortfolioManagement.tsx | 163-252 | C2 Deprecated | Medium | `handleResumeSession()` implements dual-format logic (hasFullData branches NEW vs OLD format). Legacy autosave migration path that should be deprecated once old sessions expire. |
| 15 | PortfolioManagement.tsx | 124 | C2 Deprecated | Medium | TODO comment `// TODO: Get from actual data` -- `modelDate` hardcoded to match `optimizationDate` with no resolution path or issue reference. |
| 16 | hooks/useOptimizationCalculations.ts | 61-72 | C2 Deprecated | Medium | Five TODO comments for unimplemented calculations (predictedBeta, totalRisk, assetSelection, commonFactor, aum) that return hardcoded 0 to consumers. Superseded by useFinalSummaryCalculations and useRiskCalculations hooks. |
| 17 | tabs/RebalanceTab.tsx | 236-241 | C2 Deprecated | Medium | Disabled button labeled "Export (deprecated)" with no onClick handler. Export moved to TradeTab via ExportModal. Dead UI element should be removed. |
| 18 | utils/mockData.ts | 1-6 | C2 Deprecated | Medium | Header comment describes mock data as transient placeholder "until real data is imported" but file is still heavily used. Stale framing. |
| 19 | hooks/usePortfolioOptimizationApi.ts | 35-54 | C5 Orphaned | Medium | `handleAuthError()` function handles 401/403 and redirects to login but is defined and never invoked anywhere. Dead code or incomplete integration. |
| 20 | hooks/usePortfolioOptimizationApi.ts | 85-234 | C5 Orphaned | Medium | `useNavigate()` called in 5 mutation hooks (usePortfolioData, useSavePortfolio, useSnapshots, useDeleteSnapshot, useUploadPortfolioFiles) but `navigate` variable never used. Leftover from incomplete error-handling refactor. |
| 21 | utils/riskFactorFilter.ts | 1-74 | C5 Orphaned | Low | Exports `filterToStyleFactors()`, `isSummaryRow()`, `excludeSummaryRows()` but no file in the scanned set imports from this module. Possibly orphaned from removed Risk Decomposition feature. |
| 22 | hooks/usePortfolioEditStore.ts | 140-175 | C1 Dead | Medium | `useSummaryStats()` hook exported but never imported. Summary stats calculated inline in usePortfolioStore and usePortfolioManagementState instead. |
| 23 | hooks/useOptimizationState.ts | 429-636 | C1 Dead | Low | Six mock data generator functions (getMockSecurities, getMockAlphaFactors, etc.) defined but never called. Should be removed or moved to dedicated mock file. |
| 24 | tabs/TradeTab.tsx | 172-180 | C1 Dead | Medium | `handleBulkEditClick()` shows toast "Bulk edit will be available after grid selection is implemented" with commented-out code. Partially implemented then abandoned. |
| 25 | components/UploadPortfolioModal.tsx | 325-335 | C1 Dead | Medium | 11 lines of console.log debug statements fire on every render. No production purpose; should be removed or gated behind dev check. |
| 26 | components/RiskVisualization.tsx | 20-37 | C2 Deprecated | Medium | Heavy console.log debug output embedded in production component (lines 20-23, 30, 34, 37, 71-72). Operational knowledge in logs should be in docs or types. |
| 27 | components/OptimizationSummaryHeader.tsx | 284-288 | C2 Deprecated | Low | Commented-out RiskVisualization component with no FIXME or issue reference. Incomplete refactoring artifact. |
| 28 | components/ExecuteSaveButton.tsx + ExecuteSaveModal.tsx | multiple | C3 Duplication | Medium | Identical hardcoded HSL CSS variable references scattered across className strings. No centralized color token; if design system changes, both files must update independently. |
| 29 | components/PortfolioGrid.tsx | 229-305 | C3 Duplication | Medium | Trade column and Final Trade column share nearly identical formatting/color logic with minor differences. Color calculation `val > 0.005 ? '#15803d' : val < -0.005 ? 'hsl(var(--danger))'` duplicated. |
| 30 | components/PerformanceChart.tsx | 32-33, 93-94 | C3 Duplication | Medium | Timezone correction logic and comment duplicated in two functions (chartData memo and tooltip formatter). Extract to utility. |
| 31 | PortfolioManagement.tsx | 51 | C4 Hardcoded | Low | Fund code 'PFDE' hardcoded as sort priority. Should be in constants.ts or config. |
| 32 | PortfolioManagement.tsx | 370 | C4 Hardcoded | Low | Session ID prefix 'opt_' hardcoded. Should be named constant. |
| 33 | PortfolioManagement.tsx | 211 | C4 Hardcoded | Low | React Query staleTime hardcoded to 10 * 60 * 1000. Should be extracted constant. |
| 34 | hooks/useAutoSave.ts + useOptimizationAutoSave.ts | 5-7 / 23-25 | C4 Hardcoded | Low | AUTO_SAVE_INTERVAL=60000 and RETRY_DELAY=2000 duplicated in two files with same values. No centralized config. |
| 35 | hooks/useOptimizationCalculations.ts + useFinalSummaryCalculations.ts | 26 / 145 | C4 Hardcoded | Low | Trading cost rate (0.00035 = 3.5 bps) hardcoded in two places. Should be configurable or from backend. |
| 36 | hooks/useConstraintValidation.ts | 41 | C4 Hardcoded | Low | Portfolio weight tolerance hardcoded as 0.01. No per-portfolio or validator-specific configuration. |
| 37 | tabs/RebalanceTab.tsx + TradeTab.tsx | 81 / 140 | C4 Hardcoded | Medium | Strategy hardcoded as 'PFDE' in upload handlers in both tabs. Should derive from store state or selected fund. |
| 38 | tabs/TradeTab.tsx | 251 | C4 Hardcoded | Low | Canonical sector order hardcoded as array [25, 45, 40, ...]. Should reference centralized enum. |
| 39 | components/ExportModal.tsx | 22-33 | C4 Hardcoded | Medium | Destination options and attestation labels hardcoded as constants. Business rules that should come from backend or centralized config. |
| 40 | components/PortfolioGrid.tsx | 150-155 | C4 Hardcoded | Medium | Size colors (`sizeColors: Record<string, string>`) with inline RGB values and no design token reference. |
| 41 | components/LoadingOverlay.tsx | 12 | C4 Hardcoded | Medium | Hardcoded `text-[#1e3a5f]` color conflicts with dark theme. Should use HSL variable. |
| 42 | tabs/SectorTab.tsx | 254, 272 | C4 Hardcoded | Low | Inline hex colors (#f59e0b, #818cf8) for cell styling should use Tailwind classes or centralized constants. |
| 43 | tabs/AlphaTab.tsx + SectorTab.tsx | 499-501 / 338-347 | C4 Hardcoded | Low | Trade color thresholds hardcoded locally in each tab with different values (0.1 vs 0.5 vs 2). Should be centralized. |
| 44 | hooks/usePortfolioApi.ts | 59-61, 84-86, 162-164, 202-204, 224-226, 267-269 | C6 Stale Error | Medium | Six mutation hooks have onError callbacks that only console.log. No user-facing toast, no error state capture, no recovery. Errors are silent from UI perspective. |
| 45 | hooks/useAutoSave.ts | 79, 98 | C6 Stale Error | Medium | Error extraction converts all errors to generic 'Auto-save failed', losing HTTP status codes and backend error messages. |
| 46 | PortfolioManagement.tsx | 223-225 | C6 Stale Error | Medium | Background factor fetch catches all errors and logs only `err?.message`, then silently continues. 500s, timeouts, network failures all swallowed with only a warn log. |
| 47 | PortfolioManagement.tsx | 208-226 | C6 Stale Error | Medium | `queryClient.fetchQuery()` handler does not validate that data was fetched. If fetch returns undefined or empty array, condition on line 213 silently exits without logging. |
| 48 | tabs/RebalanceTab.tsx | 57-60 | C6 Stale Error | Medium | handleLoadVersion catch: generic toast 'Failed to load version' with no error details passed to user. Swallows specific API error messages. |
| 49 | tabs/TradeTab.tsx | 118-120 | C6 Stale Error | Medium | Same generic handleLoadVersion catch as RebalanceTab. Duplicated stale pattern. |
| 50 | tabs/HistoryTab.tsx | 106-107 | C6 Stale Error | Medium | handleDownload catch block does not capture or log error object at all. Silent catch with no diagnostic info. |
| 51 | components/UploadPortfolioModal.tsx | 293-300 | C6 Stale Error | Medium | Error discrimination via string matching on `error.message`. Brittle -- if backend messages change, checks break silently. No structured error codes. |
| 52 | components/PortfolioGrid.tsx | 393 | C6 Stale Error | Medium | Cell edit validation uses browser `alert()` instead of toast or modal. Blocks UI thread. |
| 53 | components/VersionHistoryModal.tsx | 166 | C6 Stale Error | Medium | "Load more versions" button rendered when `hasMore && !isLoading` but onClick handler is missing. Dead UI element. |
| 54 | hooks/usePortfolioEditStore.ts | 143 | C2 Deprecated | Low | Hardcoded `aum = 100000000` with TODO "get from main store". Placeholder value never replaced. |
| 55 | hooks/useOptimizationState.ts | 268, 124 | C2 Deprecated | Low | Two stale TODOs: "Fetch security details from backend" and "Get modelDate from actual data". Partially implemented features. |
| 56 | components/EmptyGridTemplate.tsx | 26 | C4 Hardcoded | Low | Magic number 10 for skeleton rows with no constant or explanation. |

## Summary

- **Total findings:** 56
- **By category:** C1: 7, C2: 9, C3: 12, C4: 14, C5: 4, C6: 10
- **High severity:** 8
- **Medium severity:** 32
- **Low severity:** 16

## Recommended Priority Fixes (Top 3 by Impact)

1. **Extract shared utilities for duplicated logic (C3 findings #3, #4, #5, #9-#13):** The `deriveAction()`, `calculateSummaryStats()`, `computeExposureVector()`, version loading, file upload, and filter/sort logic are each duplicated 2-3 times with subtle differences. This is the highest-impact structural debt -- one drift-prone change in any of these will produce inconsistent behavior. Extract to shared hooks/utils: `useFilteredTrades()`, `use3StateSort()`, `deriveAction.ts`, `normalizePortfolio.ts`, `riskMath.ts`.

2. **Fix broken retry/error handling in autosave hooks (C6 findings #1, #2, #8):** useOptimizationAutoSave has a fake retry loop that never actually retries (finding #1), useAutoSave has a floating promise that swallows errors (finding #2), and UploadPortfolioModal silently suppresses exceptions in nested try-catch (finding #8). These are the only findings that could cause silent data loss in production.

3. **Remove dead stubs and unused code (C1 findings #6, #7, #22-#25):** LookupTab is a non-functional stub registered as a real tab, useSummaryStats is exported but never imported, 6 mock generators are never called, handleBulkEditClick shows a "not yet implemented" toast, and debug console.logs fire in production. The emoji in ExecuteSaveButton (#7) specifically violates CLAUDE.md rule #13 and will break CloudWatch on Windows.
