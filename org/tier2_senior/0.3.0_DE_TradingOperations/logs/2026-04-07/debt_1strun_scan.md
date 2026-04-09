# DEBT_1STRUN Scan -- Pod 3 (TradingOperations) Shared Infrastructure

**Agent:** 0.2.3_RD_FactorTilts (covering 0.3.0_DE_TradingOperations)
**Date:** 2026-04-07
**Scope:** Shared API endpoints, types, hooks, and utilities used by Pod 3 pages (PortfolioManagement, TradeSubmission, DataRefresh, SecurityScanner)

---

## C1 - DEAD CODE

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C1-1 | HIGH | api/endpoints/portfolio.ts:315-338 | `transformToEditableTrade()` -- exported function, never imported by any page. Backend now returns `EditableTrade` directly via `UploadResponse.data.trades`. This was the original client-side transform for v1 `TradeRecord` -> `EditableTrade`. |
| C1-2 | HIGH | api/endpoints/portfolio.ts:343-356 | `transformToExportTrade()` -- exported function, never imported by any page. The `exportAndSubmit()` endpoint (line 457) handles server-side export now. |
| C1-3 | HIGH | api/endpoints/portfolio.ts:7-56 | `ImportData`, `TradeRecord`, `PortfolioMetrics` (original types) -- `ImportData` is re-declared in `pages/PortfolioManagement/types.ts:24` and imported from there. The api/endpoints versions are only used by the dead transform functions above. `TradeRecord` with its `Symbol`/`Name` API-case fields is never imported by any page. |
| C1-4 | HIGH | api/endpoints/portfolio.ts:85-124 | `ExportRequest`, `ExportResponse`, `ExportHistoryItem` types -- only used by `exportToVidentTemplate()` and `getExportHistory()` in the same file. These functions are only called from `usePortfolioApi.ts` hooks that appear to be legacy (v1 export flow, pre-`exportAndSubmit`). Needs verification whether `usePortfolioApi` export mutations are still active in the UI. |
| C1-5 | MEDIUM | api/endpoints/portfolio-optimization.ts:218+ | `getMockOptimizationData()` -- exported mock data generator, never imported by any page. Comment says "Remove this once backend is ready." Backend is ready. |
| C1-6 | MEDIUM | pages/PortfolioManagement/utils/mockData.ts (entire file) | `MOCK_TRADES`, `MOCK_PERFORMANCE`, `MOCK_IMPORT_DATA`, `MOCK_PORTFOLIO_METRICS` -- only imported by mockData.ts itself and potentially legacy test paths. No page component imports from this file. |
| C1-7 | LOW | pages/PortfolioManagement/components/SecurityLookupModal.tsx:31-54 | `MOCK_SECURITIES` array -- hardcoded mock data inside a production component. Used as search results when no API is connected. Should be replaced with actual API call or removed. |

---

## C2 - DEPRECATED / SUPERSEDED

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C2-1 | HIGH | api/endpoints/portfolio.ts:270-290 | `uploadPickleFile()` (standalone) -- superseded by `uploadPickleFileWithFund()` (line 367) which adds fund/account context. The standalone version is still imported in `usePortfolioManagementState.ts:16` via `@/api/portal-proxy` (a re-export). Also imported from `@/api/endpoints/portfolio` in `usePortfolioApi.ts:3`. Two different code paths for the same operation. |
| C2-2 | HIGH | api/endpoints/portfolio.ts:295-310 | `exportToVidentTemplate()` and `getExportHistory()` -- superseded by `exportAndSubmit()` (line 457). The old export flow used `publicApiRequest` (no JWT); the new flow uses `apiRequest` (JWT). Old functions still wired in `usePortfolioApi.ts:74,99`. |
| C2-3 | MEDIUM | api/endpoints/portfolio-optimization.ts:197-208 | `getSecurityDetails()` -- has `TODO: Implement backend endpoint` comment and `console.warn` noting "backend pending". If backend is now implemented, remove the warning. If not, this is dead code that will 404. |
| C2-4 | MEDIUM | pages/PortfolioManagement/DESIGN_SPEC.md | Design spec from initial build. References mock data patterns and checkbox items (`- [ ]`). Likely outdated now that the page is live. |
| C2-5 | LOW | pages/TradeSubmission/FUNCTIONALITY_IMPLEMENTATION_SUMMARY.md, QUICK_STATUS_CHECK.md, CANONICAL_COLORS_COMPLETE.md | Implementation artifacts left in source tree. Not harmful but add noise. |

---

## C3 - DUPLICATION / DRIFT RISK

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C3-1 | HIGH | api/endpoints/portfolio.ts:270 vs api/portal-proxy.ts:1753 | `uploadPickleFile` defined in BOTH files with different return types (`ImportData` vs `PortfolioImportData`). `usePortfolioManagementState.ts:16` imports from `portal-proxy`; `usePortfolioApi.ts:3` imports from `endpoints/portfolio`. Two implementations, two types, same Lambda endpoint. |
| C3-2 | HIGH | api/endpoints/portfolio.ts:7-56 vs pages/PortfolioManagement/types.ts:24+ | `ImportData`, `TradeRecord`, `PortfolioMetrics` defined in both locations with slightly different field sets. The page-local types add fields like `PerformanceDataPoint` not present in the API types. No single source of truth. |
| C3-3 | MEDIUM | pages/PortfolioManagement/utils/factorDescriptions.ts vs pages/SecurityScanner/utils/factorDescriptions.ts | Two files with same filename but different factor sets (Yang alpha factors vs SSCN scanner factors). Not actual duplicates but the naming creates confusion. Both are local to their pages, so low risk, but any shared factor work would miss one. |
| C3-4 | MEDIUM | api/endpoints/portfolio.ts uses `apiRequest` (JWT) for most new endpoints but `publicApiRequest` (no JWT) for legacy `exportToVidentTemplate` and `getExportHistory`. Mixed auth patterns in the same file. |

---

## C4 - HARDCODED CONFIGURATION

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C4-1 | HIGH | api/endpoints/trade-submission.ts (entire file) | ALL trade submission API functions use `publicApiRequest` instead of `apiRequest`. This means workflow actions (approve, reject, execute) do NOT include JWT auth headers. These are sensitive operations that should require authentication. The security-scanner and data-refresh endpoints correctly use `apiRequest`. |
| C4-2 | MEDIUM | api/endpoints/portfolio.ts:433-439 | `saveOptimizationAutoSave()` parameter types use `any[]` for 7 fields (securities, alphaFactors, sectorAllocations, modelCoefficients, modelGroups, riskFactors, summary). Proper types exist in `@/types/portfolio-optimization`. |
| C4-3 | LOW | api/endpoints/portfolio.ts:347 | `TODO: Lookup from raw DataFrame` comment in `transformToExportTrade()` -- permanent TODO in dead code. |
| C4-4 | LOW | pages/DataRefresh/hooks/useDataRefreshState.ts:355 | Error message string parsing with regex (`errorMessage.match(/\{.*\}/)`). Fragile -- depends on backend error format. |

---

## C5 - ORPHANED INFRASTRUCTURE

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C5-1 | MEDIUM | pages/PortfolioManagement/DESIGN_SPEC.md | 347-line design spec with unchecked implementation checkboxes. Not code, but adds to `portal/src/pages` directory size and creates confusion about what's implemented vs planned. |
| C5-2 | MEDIUM | pages/TradeSubmission/FUNCTIONALITY_IMPLEMENTATION_SUMMARY.md | 200+ line implementation summary left in production source. References `publicApiRequest` import patterns. |
| C5-3 | LOW | pages/DataRefresh/AWS_ENGINEER_BRIEF.md | Engineering brief in page source directory. Should be in `docs/` or `org/`. |
| C5-4 | LOW | pages/SecurityScanner/DESIGN_SPEC.md | Design spec in page source directory. |

---

## C6 - STALE ERROR HANDLING

| # | Severity | File:Line | Description |
|---|----------|-----------|-------------|
| C6-1 | HIGH | api/endpoints/portfolio-optimization.ts:202-208 | `getSecurityDetails()` -- calls `apiRequest` to an unimplemented endpoint. Will throw a 404 error with no meaningful error message. The `console.warn` fires but the function still makes the request. |
| C6-2 | MEDIUM | pages/DataRefresh/components/CurrentStatePanel.tsx:4 | Imports `publicApiRequest` directly from `@/api/api-client` instead of using the typed endpoint functions in `@/api/endpoints/data-refresh.ts`. Likely makes raw fetch calls without proper error typing. |
| C6-3 | LOW | api/endpoints/portfolio.ts:270-290 | `uploadPickleFile()` returns raw `ImportData` without validating the response shape matches the interface. If the Lambda response format changes, the TypeScript types won't catch it at runtime. |

---

## Summary

| Category | High | Medium | Low | Total |
|----------|------|--------|-----|-------|
| C1 Dead Code | 4 | 2 | 1 | 7 |
| C2 Deprecated | 2 | 2 | 1 | 5 |
| C3 Duplication | 2 | 2 | 0 | 4 |
| C4 Hardcoded | 1 | 1 | 2 | 4 |
| C5 Orphaned | 0 | 2 | 2 | 4 |
| C6 Stale Error | 1 | 1 | 1 | 3 |
| **Total** | **10** | **10** | **7** | **27** |

---

## RD/DS Pod Scan Status

| Agent | Scan Log | Status |
|-------|----------|--------|
| 0.3.0_DS_TradingOperations | logs/2026-03-23/debt_1strun_scan.md | NOT FOUND |
| 0.3.1_RD_PortfolioManagement | logs/2026-03-23/debt_1strun_scan.md | NOT FOUND |
| 0.3.2_RD_TradeSubmission | logs/2026-03-23/debt_1strun_scan.md | NOT FOUND |
| 0.3.3_RD_DataRefresh | logs/2026-03-23/debt_1strun_scan.md | NOT FOUND |
| 0.3.4_RD_SecurityScanner | logs/2026-03-23/debt_1strun_scan.md | NOT FOUND |

All DS/RD scan logs are PENDING. Pod aggregate report cannot include their findings.

---

## Top 10 Pod Debt Items (DE scan only)

| Rank | Finding | Severity | Effort | Why |
|------|---------|----------|--------|-----|
| 1 | C4-1: trade-submission.ts uses publicApiRequest for all endpoints | HIGH | MODERATE | Sensitive workflow actions (approve/reject/execute trades) lack JWT auth. Security risk. |
| 2 | C3-1: uploadPickleFile defined in two files with different types | HIGH | MODERATE | Two code paths, two return types for same Lambda. Drift risk on any API change. |
| 3 | C2-1: standalone uploadPickleFile superseded by uploadPickleFileWithFund | HIGH | MODERATE | Legacy function still wired in usePortfolioManagementState. Should be consolidated. |
| 4 | C1-1/C1-2: transformToEditableTrade/transformToExportTrade dead | HIGH | QUICK WIN | Delete 2 functions (40 lines). Zero consumers. |
| 5 | C2-2: exportToVidentTemplate/getExportHistory superseded | HIGH | MODERATE | Old export flow uses wrong auth pattern. Need to verify usePortfolioApi references and remove. |
| 6 | C3-2: ImportData/TradeRecord types duplicated in api vs page | HIGH | MODERATE | Single source of truth needed. Consolidate to api/endpoints/portfolio.ts or shared types. |
| 7 | C1-3: Original TradeRecord/ImportData/PortfolioMetrics types dead in api | HIGH | QUICK WIN | Delete once C3-2 consolidation happens. ~50 lines. |
| 8 | C6-1: getSecurityDetails calls unimplemented endpoint | HIGH | QUICK WIN | Either implement the endpoint or remove the function. Currently silently 404s. |
| 9 | C4-2: saveOptimizationAutoSave uses any[] for 7 params | MEDIUM | MODERATE | Replace with proper types from @/types/portfolio-optimization. |
| 10 | C1-5/C1-6: Mock data generators never used | MEDIUM | QUICK WIN | Delete getMockOptimizationData + entire mockData.ts. ~230 lines. |
