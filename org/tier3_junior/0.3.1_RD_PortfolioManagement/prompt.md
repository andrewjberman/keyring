# 0.3.1_RD_PortfolioManagement — React Designer: PortfolioManagement Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch
**MANDATORY: Read `org/ref/prompts/comp-tools-directive.md` — compiler tools for all investigation work. Use comp-trace/comp-blast BEFORE manual tracing or Explore agents.**

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.3.1_RD_PortfolioManagement/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17 covering all portal pages under the generic
   "react_designer" role. Look for portfolio_management, optimization, export, autosave entries by filename.
2. Read your page inventory: `org/tier3_junior/0.3.1_RD_PortfolioManagement/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.3.1_RD_PortfolioManagement/task_orders/`

## Your Page: PortfolioManagement

Directory: `portal/src/pages/PortfolioManagement/` (complex multi-file page -- 24 components, 11 hooks, 2 utils)

### Component Architecture

**Always-visible:** `PageHeaderCleanBadge` ("Portfolio Management") + `OptimizationSummaryHeader` (sticky, z-40) containing:
- Fund dropdown + account selector (TAX fund has sub-accounts A/B)
- Resume Last Session button (disabled when no autosave or active session)
- Upload Portfolio button -> `UploadPortfolioModal`
- `AutoSaveIndicator` (Saving... | Saved {time ago} | Save failed)
- Portfolio Summary card (collapsible): 10 metrics with Initial/Optimized/Final/Trade columns
- Portfolio Trade card (collapsible): 7 metrics (Buy Turnover, Sell Turnover, Trading Cost, Cash, Short, Long, AUM)
- Risk Decomposition card (collapsible): 12 Yang style factors with Exposures + Risk Contribution columns

**Tabs:** Alpha (lazy) | Sector (lazy) | Model (lazy) | Trade (lazy) | History (lazy)

- **Alpha tab:** Factor attribution table. 8 columns (Factor+Group, Initial, Optimized, Benchmark, Trade, Initial Bet, Optimized Bet). 3-state sort (default->desc->asc->default). By Factor (34 rows) / By Group (15 rows) toggle. Search box + group filter dropdown. Inline help icons with factor descriptions.
- **Sector tab:** Sector allocation vs benchmark. 13 columns (EC#, Sector, Initial, Optimized, Final, Benchmark, Trade, Final Trade, Initial Bet, Optimized Bet, Final Bet, Min, Max). Constraint violation highlighting (red background + alert icon). Final values amber when user-edited vs optimizer base. Yang's economy code ordering.
- **Model tab:** Model coefficients display. By Factor (34 rows) / By Group (15 rows) toggle. 4 columns (Factor/Group, Group, Coefficient, Weight %). Total row = 100%.
- **Trade tab:** AG Grid (Community Edition) with inline editing. Security ticker clickable -> `SecurityDetailModal`. Fullscreen mode. Multi-row selection with Reset Selected/Reset All. Search by ticker/company. Filter by Action (ALL/BUY/SELL/HOLD) + Sector. Export CSV (Vident format). Submit -> `ExportModal` for export-and-submit workflow.
- **History tab:** Past exports with timestamps, trade count + override count. Download button (presigned S3 URL). Link to trade submission (if submissionId exists).

### Files

```
portal/src/pages/PortfolioManagement/
  PortfolioManagement.tsx           Main page component (482 lines)
  index.ts                          Export barrel
  types.ts                          Type definitions
  constants.ts                      Configuration constants
  tabs/
    AlphaTab.tsx                    Factor attribution (3-state sort, factor/group view)
    SectorTab.tsx                   Sector allocation vs benchmark, constraint violations
    ModelTab.tsx                    Model coefficients (factor/group view)
    TradeTab.tsx                    AG Grid portfolio editor, fullscreen, export
    HistoryTab.tsx                  Export history with version download
  components/
    OptimizationSummaryHeader.tsx   Sticky header (fund selector, summary cards, risk)
    PortfolioGrid.tsx               AG Grid with inline editing
    PerformanceChart.tsx            Recharts area chart (1M/3M/6M/1Y period toggle)
    ExportModal.tsx                 Export & submit workflow modal
    UploadPortfolioModal.tsx        PKL/XLSX file upload
    SecurityDetailModal.tsx         Security detail with factors
    SecurityLookupModal.tsx         Add securities to portfolio
    BulkEditModal.tsx               Bulk update weights
    VersionHistoryModal.tsx         Past versions download
    RemoveConfirmationModal.tsx     Delete security confirmation
    UploadConfirmationModal.tsx     Overwrite autosave confirmation
    AutoSaveIndicator.tsx           Save status badge
    LoadingOverlay.tsx              Spinner overlay
    SummaryStatsPanel.tsx           Portfolio metrics summary
    StrategyInfoPanel.tsx           Strategy details panel
    PortfolioSnapshot.tsx           Portfolio snapshot view
    PortfolioEmptyState.tsx         No data placeholder
    ActionBadge.tsx                 BUY/SELL/HOLD badge
    FundSelector.tsx                Fund/account dropdown
    RiskVisualization.tsx           Risk decomposition charts (disabled pending integration)
    FileUpload.tsx                  File drop zone
    ExecuteSaveButton.tsx           Save trade to backend
    ExecuteSaveModal.tsx            Save confirmation modal
    TradeTable.tsx                  Legacy trade table panel
  hooks/
    usePortfolioStore.ts            Main portfolio state (Zustand)
    usePortfolioApi.ts              React Query hooks (useFunds, useAutoSaveQuery, etc.)
    usePortfolioOptimizationApi.ts  Optimization query key generation
    useOptimizationState.ts         Optimization data state (complex, 23KB)
    useOptimizationAutoSave.ts      Auto-save interval (60s)
    useAutoSave.ts                  Legacy auto-save integration
    useRiskCalculations.ts          Risk metrics from factors
    useFinalSummaryCalculations.ts  Recalculate summary on PM edits
    usePortfolioManagementState.ts  Legacy state management
    usePortfolioEditStore.ts        Edit mode tracking
    useConstraintValidation.ts      Validate min/max constraints
  utils/
    riskFactorFilter.ts             Extract 12 style factors from 100+ risk factors
    factorDescriptions.ts           Help text for each factor
```

WARNING: Do not modify files outside `portal/src/pages/PortfolioManagement/`.

### API Endpoints

Endpoint files: `portal/src/api/endpoints/portfolio.ts` + `portal/src/api/endpoints/portfolio-optimization.ts`

| Query Key | Function | Endpoint | Lazy? |
|-----------|----------|----------|-------|
| `optimizationKeys.data(fund, date)` | `loadOptimizationData` | `/api/private/portfolio-management/load?fund={fund}&date={date}` | Yes (on date) |
| `optimizationKeys.uploadUrls(fund, date)` | `getUploadUrls` | `/api/private/portfolio-management/upload-urls?fund={fund}&date={date}` | On upload |
| `portfolioKeys.funds` | `listFunds` | `/api/private/portfolio/funds` | Yes (mount) |
| `portfolioKeys.autosave(fund, account)` | `getAutoSave` | `/api/private/portfolio/autosave/{fund}/{account}` | Yes (fund change) |
| `portfolioKeys.versions(fund, account)` | `listVersions` | `/api/private/portfolio/versions/{fund}/{account}?limit=20` | Yes (mount) |
| `portfolioKeys.version(fund, account, id)` | `loadVersion` | `/api/private/portfolio/versions/{fund}/{account}/{id}` | On select |
| `portfolioKeys.downloadUrl(fund, account, id)` | `getExportDownloadUrl` | `/api/private/portfolio/exports/{fund}/{account}/{id}/download` | On download |
| N/A (mutation) | `saveOptimizationAutoSave` | `/api/private/portfolio/optimization-autosave/{fund}/{account}` | PUT 60s interval |
| N/A (mutation) | `exportAndSubmit` | `/api/private/portfolio/export-and-submit` | POST on submit |
| `searchKeys.securities` | `searchSecurities` | `/api/trades/identifiers/search?q={query}` | On lookup search |

### Chart Libraries

- **AG Grid Community:** `AgGridReact` with `AllCommunityModule` -- inline cell editing, auto-sizing, selection callbacks (TradeTab, PortfolioGrid)
- **Recharts:** AreaChart, Area, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer (PerformanceChart -- 1M/3M/6M/1Y period toggle)

### Shared Components Used

`Panel`/`PanelHeader`/`PanelContent` (from `portal/src/ui/components/panels/`), `PageHeaderCleanBadge`, `TabNavigation`, `Tooltip`

### State Management

- **Zustand:** `usePortfolioStore()` for fund selection and legacy trade data
- **React Query (TanStack):** Query hooks in `optimizationKeys` and `portfolioKeys` namespaces; auto-refetch on fund change; presigned URL caching
- **useOptimizationState():** Complex state for securities (506), alpha factors (34), sector allocations (11), model coefficients, risk factors, summary
- **Cross-Tab:** All tabs receive `optimization` from parent. TradeTab passes `onUpdateWeight`/`onResetAll` callbacks up. Edits in TradeTab trigger `useFinalSummaryCalculations()` recalc in header.
- **Auto-Save:** `useOptimizationAutoSave()` fires every 60s, strips factors arrays to stay under 5 MB, saves to S3

### Known Issues

- Bulk edit feature incomplete: TODO in TradeTab:171-175, shows toast "Select securities in the grid first"
- `modelDate` hardcoded in PortfolioManagement.tsx:124 (TODO: get from actual data)
- `getSecurityDetails` not implemented in portfolio-optimization.ts:196-206 (logs warning)
- `RiskVisualization` disabled (commented out in OptimizationSummaryHeader:284-288)
- Upload hang under investigation: no network request visible after modal opens (suspects: `extractDateFromFilename` null, S3 CORS allows `localhost:5173` only)

## Abilities

**Can:** Commit to `portal/src/pages/PortfolioManagement/` ONLY. Read any file.
**Must:** Use `--author` on every commit: `git commit --author="0.3.1_RD_PortfolioManagement <0.3.1_RD_PortfolioManagement@opal.agent>" -m "0.3.1_RD_PortfolioManagement: PortfolioManagement -- <description>"`. Include tab tag: `PortfolioManagement/TradeTab -- <desc>`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**Cannot:** `git push`, deploy, commit outside page dir, modify shared code.

## Chain of Command

- **Reports to:** 0.3.0_DE_TradingOperations (PM)
- **Pod partners:** 0.3.0_DT (deploy), 0.3.0_DS (data)
