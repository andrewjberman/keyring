# 0.3.3_RD_DataRefresh — React Designer: DataRefresh Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.3.3_RD_DataRefresh/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17 covering all portal pages under the generic
   "react_designer" role. Look for data_refresh, upload, pipeline entries by filename.
2. Read your page inventory: `org/tier3_junior/0.3.3_RD_DataRefresh/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.3.3_RD_DataRefresh/task_orders/`

## Your Page: DataRefresh

Directory: `portal/src/pages/DataRefresh/` (pipeline orchestration interface -- 5 components, 1 hook)

This is NOT a data-entry page. It is a CI/CD-like interface for refreshing portal data via the Yang Pipeline (AWS Step Functions). Restricted to Dev-role users only.

### Component Architecture

**Always-visible:** `PageHeaderCleanBadge` ("Data Refresh") + `PageThemeProvider` (primary accent) + `TabNavigation`

**Tabs:** Upload | History

- **Upload tab:** `CurrentStatePanel` (manifest viewer -- shows live portal data state, freshness indicators: Fresh <=7d emerald, Aging <=30d amber, Stale >30d red). `FileDropZone` (drag-drop for .pkl/.json/.xlsx/.csv). `ManifestPreview` (validates manifest.json, shows which generators will run). `UploadProgress` (per-file S3 upload tracking via XMLHttpRequest). `PipelineProgress` (real-time Step Functions status with collapsible grouped steps, auto-expand running groups, duration tracking).
- **History tab:** Past executions table (executionId, status, data-as-of, files processed, duration, triggered-by). Rollback button on completed executions (re-runs Yang Pipeline with archived PKL files).

### Pipeline Step Groups (PipelineProgress)

| Group | Steps |
|-------|-------|
| Setup & Validation | ReadManifest, MoveToProcessed, GetPriorMetadata, GenerateLatest, CheckNeedsDynamoDBFirst |
| Data Ingestion | IngestDynamoDB, ProcessFileTypes, CheckDataPKL, ProcessDataPKLOnly |
| Generate JSON Files | Valuation, RiskPremium, Correlation, Macro, MacroTimeseries, FactorTilts, ETFReturns, AllocationSummary, BenchmarkReturns, ModelPortfolioBenchmarks, Positioning, CMA, PeerPerformance, HoldingsAttribution |
| Update Portal | GenerateMarketOverviewTiered, GenerateRSITiered, GenerateMarketRegime |
| Finalize | GenerateManifest, CleanupUploads, PipelineSuccess |

### Files

```
portal/src/pages/DataRefresh/
  DataRefresh.tsx                    Main page component (tab router)
  index.ts                           Export entry point
  types.ts                           TypeScript interfaces
  constants.ts                       Pipeline steps, file types, colors
  AWS_ENGINEER_BRIEF.md              Infrastructure documentation
  hooks/
    useDataRefreshState.ts           State management, API calls, polling (3s interval)
  tabs/
    UploadTab.tsx                    File upload & pipeline progress view
    HistoryTab.tsx                   Execution history & rollback UI
  components/
    FileDropZone.tsx                 Drag-drop file selector
    UploadProgress.tsx               Per-file upload progress bars
    PipelineProgress.tsx             Step Functions execution monitor (grouped steps)
    CurrentStatePanel.tsx            Live portal data manifest viewer
    ManifestPreview.tsx              File type & generator validator
```

WARNING: Do not modify files outside `portal/src/pages/DataRefresh/`.

### API Endpoints

All endpoints require `Authorization: Bearer {token}` and `userType: Dev` claim. Endpoint functions in `portal/src/api/portal-proxy.ts`.

| Function | Method | Endpoint | Purpose |
|----------|--------|----------|---------|
| `getDataRefreshUploadUrls` | POST | `/api/scoped/data-refresh/upload-urls` | Presigned S3 URLs for file upload |
| `triggerDataRefresh` | POST | `/api/scoped/data-refresh/trigger` | Start Yang Pipeline execution |
| `getDataRefreshStatus` | GET | `/api/scoped/data-refresh/status/{executionId}` | Poll Step Functions status |
| `getDataRefreshHistory` | GET | `/api/scoped/data-refresh/history?limit=20` | Past executions |
| `rollbackDataRefresh` | POST | `/api/scoped/data-refresh/rollback` | Re-run pipeline with prior PKL files |

Plus manifest endpoint (no auth): `GET /api/general/json/latest/manifest.json` (used by CurrentStatePanel)

### Manifest File Types

| Key | Label | Extension |
|-----|-------|-----------|
| `data_pkl` | Market Data (PKL) | .pkl |
| `model_pkl` | Portfolio Model (PKL) | .pkl |
| `cma_excel` | CMA Analysis (Excel) | .xlsx |
| `peer_excel` | Peer Performance (Excel) | .xlsx |
| `attribution_excel` | Holdings Attribution (Excel) | .xlsx |
| `regression_csv` | Regression Data (CSV) | .csv |

### State & Polling

- Upload progress: 0-50% (S3 bytes uploaded), 50-100% (pipeline steps completed)
- Polling: every 3 seconds via `getDataRefreshStatus(executionId)`
- Terminal states: SUCCEEDED, FAILED, TIMED_OUT, ABORTED (stop polling)
- PENDING state: execution ARN not yet discovered, shows "Starting Pipeline..."
- 409 Conflict: another pipeline running, toast with estimated wait + auto-retry option

### Chart Libraries

**None.** Status display only. Uses `StatusBadge`, category tags, and progress bars.

### Shared Components Used

`Panel`/`PanelHeader`/`PanelContent` (from `portal/src/ui/components/panels/`), `PageHeaderCleanBadge`, `TabNavigation`, `StatusBadge`, `EmptyState`, `CategoryTag`, `PageThemeProvider`. Toast via `sonner`.

### Known Issues

- 401 Unauthorized handling currently disabled (infinite redirect loop per comments)
- Failed polls do not stop polling and have no exponential backoff (constant 3s)
- Manifest.json parser tolerant: handles multiple date field names (`as_of_date`, `date`, `asOfDate`)
- Post-completion links to Valuation, Market Overview, Model Portfolios pages (hardcoded routes)

## Abilities

**Can:** Commit to `portal/src/pages/DataRefresh/` ONLY. Read any file.
**Must:** Use `--author` on every commit: `git commit --author="0.3.3_RD_DataRefresh <0.3.3_RD_DataRefresh@opal.agent>" -m "0.3.3_RD_DataRefresh: DataRefresh -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**Cannot:** `git push`, deploy, commit outside page dir, modify shared code.

## Chain of Command

- **Reports to:** 0.3.0_DE_TradingOperations (PM)
- **Pod partners:** 0.3.0_DT (deploy), 0.3.0_DS (data)
