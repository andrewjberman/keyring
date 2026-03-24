# DEBT_1STRUN Scan -- 0.3.2_RD_TradeSubmission
**Date:** 2026-03-23
**Scope:** portal/src/pages/TradeSubmission/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | types.ts | 4 | C1 Dead | Low | `UserRole` type exported but never imported or used anywhere in the codebase. Removing it changes zero behavior. |
| 2 | hooks/useTradeSubmissionState.ts | 84-91 | C1 Dead | Low | `useExecutedSubmissions` hook exported but never called by any tab or component. Only exists inside unused aggregator. |
| 3 | hooks/useTradeSubmissionState.ts | 32-40 | C1 Dead | Low | `useAllSubmissions` hook exported but never called directly. Only referenced in the unused aggregator hook. |
| 4 | hooks/useTradeSubmissionState.ts | 121-180 | C1 Dead | Medium | `useTradeSubmissionState` aggregator hook combines 7 data sources but is never imported anywhere. All consumers use individual hooks directly. |
| 5 | components/TradeCard.tsx | 7-18 | C2 Deprecated | Medium | `formatET` timezone formatting function duplicated identically in TradeDetailsModal.tsx (lines 8-19). One copy is redundant; should be extracted to services/. |
| 6 | components/FileUploadZone.tsx | 42-48 | C2 Deprecated | Medium | File extension validation `['xlsx', 'xls', 'csv']` duplicated inline here and in fileParser.ts (lines 10-15). Shared constant needed to prevent drift. |
| 7 | components/TradeCard.tsx | 40-46 | C3 Duplication | Medium | `statusMap` converting trade statuses to StatusBadge enums is defined identically in TradeDetailsModal.tsx (lines 35-41). Change to one requires updating both. |
| 8 | components/SecuritiesTable.tsx | 31-43, 140-151 | C3 Duplication | Medium | Empty security row template with all default values repeated in two locations; similar pattern also in SubmitTab.tsx (lines 54-65). Extract to shared factory function. |
| 9 | components/ApproveModal.tsx, ExecuteModal.tsx, RejectModal.tsx | 25-28, 26-29, 31-34 | C3 Duplication | Low | Three modals use identical try/catch pattern logging console.error with generic handler. No recovery or user feedback mechanism. |
| 10 | hooks/useTradeSubmissionState.ts | 37, 50, 63, 76, 88, 100, 112 | C4 Hardcoded | Medium | Poll intervals (30000, 15000, 20000, 60000 ms) hardcoded across 7 locations. Should use named constants. Changing polling strategy requires touching 6+ locations. |
| 11 | tabs/SubmitTab.tsx | 301-314, 356-360 | C4 Hardcoded | High | Fund options (PFDE, PFOE, DIVZ, IDVZ, UST, ST, INT, LTC, LTA) and destinations (vident, trueshares, internal) hardcoded in select dropdowns. No centralized source of truth. Adding/removing a fund requires a code change. |
| 12 | components/TickerAutocompleteInput.tsx | 164-173 | C4 Hardcoded | Medium | 7 specific tickers (AAPL, MSFT, NVDA, GOOGL, AMZN, TSLA, META) hardcoded as mock suggestions. Should be replaced with API lookup or loaded from config. |
| 13 | tabs/HistoryTab.tsx | 17 | C4 Hardcoded | Low | `ITEMS_PER_PAGE = 20` hardcoded. Should be configurable or moved to environment config. |
| 14 | components/ExecuteModal.tsx | 95 | C4 Hardcoded | Low | Brokerage name capitalization computed inline (`charAt(0).toUpperCase() + slice(1)`). Should use utility. |
| 15 | components/TickerAutocompleteInput.tsx | 61 | C4 Hardcoded | Low | `setTimeout(fetchSuggestions, 300)` debounce delay hardcoded. Should use named constant `TICKER_LOOKUP_DEBOUNCE_MS`. |
| 16 | hooks/useTradeSubmissionActions.ts | 33 | C4 Hardcoded | Low | `setTimeout(() => setSelectedSubmission(null), 300)` cleanup delay hardcoded. Should match CSS animation duration from design tokens. |
| 17 | Multiple: fileParser.ts, SubmitTab.tsx, useTradeSubmissionActions.ts, TickerAutocompleteInput.tsx | Various (20+ locations) | C5 Orphaned | Medium | 20+ `console.log`/`console.error`/`console.warn` statements scattered for dev debugging. Should use proper logging service or be removed for production. |
| 18 | components/RejectModal.tsx, SecuritiesTable.tsx, tabs/SubmitTab.tsx | 22, 134, 124+198 | C5 Orphaned | Medium | 4 uses of native `alert()` and `confirm()` browser dialogs instead of toast/modal system. Inconsistent with rest of portal UX. |
| 19 | components/ApproveModal.tsx, ExecuteModal.tsx, RejectModal.tsx | 26, 27, 32 | C6 Stale Error | Medium | Errors logged to console only. No error boundary, retry logic, or structured reporting. Production errors are invisible to user. |
| 20 | tabs/SubmitTab.tsx | 176-206 | C6 Stale Error | Medium | Catch block sets `submitError` state but modal doesn't close automatically on failure. User can be left in loading state if API fails mid-operation. |
| 21 | services/fileParser.ts | 91-94, 151-152 | C6 Stale Error | Medium | File parsing errors wrapped in generic messages; original error context lost. User sees "Failed to parse file" but not root cause (e.g., row 15 has invalid date). |
| 22 | tabs/SubmitTab.tsx | 72-92 | C6 Stale Error | Low | Identifier cache save wrapped in try/catch with comment "Don't block form -- cache is optional" but no user feedback on failure. Silent optimization failure. |
| 23 | hooks/useTradeSubmissionActions.ts | 42-46, 87-98, 138-142 | C6 Stale Error | Low | Error checks cast `selectedSubmission` and user info without null-coalescing guards. Falls back to generic message but doesn't explain what precondition failed. |
| 24 | components/TradeDetailsModal.tsx | 195 | C3 Duplication | Medium | Field named `delta_weight` in form/SecuritiesTable but `delta` in API response read by TradeDetailsModal. Mismatch requires fallback `?? 0` -- drift risk if either side changes. |
| 25 | components/TradeDetailsModal.tsx | 21-22 | C1 Dead | Low | `type TradeSubmissionDetail = TradeSubmission` creates unnecessary type alias. Direct use of imported type is cleaner. |

## Summary
- Total findings: 25
- By category: C1: 5, C2: 2, C3: 4, C4: 7, C5: 2, C6: 5
- High severity: 1
- Medium severity: 14
- Low severity: 10
- Recommended priority fixes:
  1. **#11 (C4, High):** Extract hardcoded fund/destination lists to config or API -- every fund change currently requires a code deploy
  2. **#4 + #2 + #3 (C1, Medium):** Remove unused `useTradeSubmissionState` aggregator and its dead constituent hooks -- 60+ lines of dead code creating false dependency signals
  3. **#10 (C4, Medium):** Extract 7 hardcoded poll intervals to named constants -- current state makes polling strategy changes error-prone across 6+ touch points
