# 0.3.2_RD_TradeSubmission — React Designer: TradeSubmission Page

Base persona: `org/ref/prompts/react_designer.md`.

## On Launch
**MANDATORY: Read `org/ref/prompts/comp-tools-directive.md` — compiler tools for all investigation work. Use comp-trace/comp-blast BEFORE manual tracing or Explore agents.**

1. Read your most recent session log:
   - v2 (org): `org/tier3_junior/0.3.2_RD_TradeSubmission/logs/` (latest date)
   - v1 (legacy): `logs/sessions/` -> latest date -> `react_designer/`
   v1 has 93 logs dating to 2025-11-17 covering all portal pages under the generic
   "react_designer" role. Look for trade, submission entries by filename.
2. Read your page inventory: `org/tier3_junior/0.3.2_RD_TradeSubmission/deliverables/page_inventory.xml`
3. Check for task orders: `org/tier3_junior/0.3.2_RD_TradeSubmission/task_orders/`

## Your Page: TradeSubmission

Directory: `portal/src/pages/TradeSubmission/` (multi-step trade approval workflow -- 8 components, 2 hooks, 1 service)

### Component Architecture

**Always-visible:** `PageHeaderCleanBadge` ("Trade Submission") with auth guard (`useAuth()`). User email/name passed as props to all tabs. Notification badges on Approvals and Execution tabs showing pending counts.

**Tabs:** Submit (Upload icon) | Approvals (CheckCircle icon) | Execution (PlayCircle icon) | History (History icon)

- **Submit tab:** File upload via `FileUploadZone` (drag-drop .xlsx/.csv). `fileParser.ts` (SheetJS/xlsx library) parses trade template: 5-row metadata header (Fund, Weights As Of, Trades As Of, Comments x2) + row 7 headers + securities data. `SecuritiesTable` with 10 columns + inline `TickerAutocompleteInput` (300ms debounce, ghosted overlay, Tab/RightArrow accept). Form: fund (PFDE/PFOE/DIVZ/IDVZ/UST/ST/INT/LTC/LTA), destination (vident/trueshares/internal), dates, comments. 4 required attestation checkboxes. POST `/submit` on form submit.
- **Approvals tab:** `TradeCard` grid showing pending submissions (15s auto-refetch). Action buttons: Approve, Reject, View Details, Download Excel. `ApproveModal` (yes/no confirmation). `RejectModal` (required reason textarea). `TradeDetailsModal` with 4 sections: Trade Details, Workflow Timeline, Securities, Attestations.
- **Execution tab:** `TradeCard` grid of approved submissions (20s auto-refetch). `ExecuteModal` (yes/no + brokerage name). Execute -> POST `/workflow` action:execute -> brokerage email sent.
- **History tab:** Dual view modes: My Submissions (user's own) / All Trades (org-wide). Status filter: All / Complete / Rejected. Pagination: 20/page with prev/next. Combines completed + rejected submissions sorted by submitted_at DESC.

### Files

```
portal/src/pages/TradeSubmission/
  TradeSubmission.tsx               Page component (auth guard, tab routing)
  types.ts                          Type re-exports
  index.ts                          Module export barrel
  tabs/
    SubmitTab.tsx                   File upload, form entry, attestations
    ApprovalsTab.tsx                Pending approvals queue, modal actions
    ExecutionTab.tsx                Ready-to-execute trades, brokerage send
    HistoryTab.tsx                  Completed/rejected, pagination, dual view
  components/
    TradeCard.tsx                   Reusable submission card (status badge, timeline)
    TradeDetailsModal.tsx           Full submission details (securities table, timeline)
    SecuritiesTable.tsx             10-column data grid (HTML table + controlled inputs)
    TickerAutocompleteInput.tsx     Inline ticker suggestion (debounce, cache-hit indicator)
    FileUploadZone.tsx              Drag-drop Excel/CSV parser wrapper
    ApproveModal.tsx                Approval confirmation dialog
    RejectModal.tsx                 Rejection reason (required textarea)
    ExecuteModal.tsx                Execution confirmation before brokerage send
  hooks/
    useTradeSubmissionState.ts      React Query hooks (7 query hooks + 1 combined)
    useTradeSubmissionActions.ts    Modal state, workflow actions (approve/reject/execute)
  services/
    fileParser.ts                   Excel/CSV parser (SheetJS), date/weight format handlers
```

WARNING: Do not modify files outside `portal/src/pages/TradeSubmission/`.

### API Endpoints

Endpoint file: `portal/src/api/endpoints/trade-submission.ts` (15 functions)

| Function | Method | Endpoint | Purpose |
|----------|--------|----------|---------|
| `submitTrade` | POST | `/api/general/trades/submit` | Create new submission |
| `approveSubmission` | POST | `/api/general/trades/workflow` | PENDING_APPROVAL -> APPROVED |
| `rejectSubmission` | POST | `/api/general/trades/workflow` | PENDING_APPROVAL -> REJECTED (with reason) |
| `executeSubmission` | POST | `/api/general/trades/workflow` | APPROVED -> EXECUTED (emails brokerage) |
| `completeSubmission` | POST | `/api/general/trades/workflow` | EXECUTED -> COMPLETE |
| `getAllSubmissions` | GET | `/api/general/trades/submissions` | All submissions (recent first) |
| `getPendingApprovals` | GET | `/api/general/trades/submissions/pending` | Filter: PENDING_APPROVAL |
| `getMySubmissions` | GET | `/api/general/trades/submissions/by-initiator?email=...` | Filter by initiator |
| `getSubmissionsApprovedBy` | GET | `/api/general/trades/submissions/by-approver?email=...` | Filter by approver |
| `getSubmissionsByStatus` | GET | `/api/general/trades/submissions/by-status?status=...` | Filter by status |
| `getSubmission` | GET | `/api/general/trades/submissions/{id}` | Single submission detail |
| `downloadExcelFile` | GET | `/api/general/trades/submissions/{id}/excel` | S3 presigned URL download |
| `getTradeUsers` | GET | `/api/general/trades/users` | All trade users (for dropdowns) |
| `searchIdentifierCache` | GET | `/api/general/trades/identifiers/search?q=...` | Ticker autocomplete (max 10) |
| `batchSaveIdentifiers` | POST | `/api/general/trades/identifiers/batch` | Cache new tickers after upload |

### Key Data Types

```
TradeSubmissionStatus = 'PENDING_APPROVAL' | 'APPROVED' | 'REJECTED' | 'EXECUTED' | 'COMPLETE'
submission_id format: "TRADE-YYYYMMDD-HHMMSS-XXXXXX"
fund: 'PFDE' | 'PFOE' | 'PFIA' | 'PFDX' | 'PFTX'
brokerage: 'vident' | 'schwab' | 'fidelity' | 'other'
TradeSecurity: ticker, sedol?, isin?, figi?, current_weight?, proposed_weight?, delta?, trade_instruction?
```

### React Query Polling

| Hook | Refetch Interval | Purpose |
|------|-----------------|---------|
| `usePendingApprovals()` | 15s | High-priority: approvals queue |
| `useApprovedSubmissions()` | 20s | Execution-ready queue |
| `useMySubmissions(email)` | 30s | User's own submissions |
| `useAllSubmissions()` | 30s | All submissions |
| `useExecutedSubmissions()` | 30s | Executed trades |
| `useCompletedSubmissions()` | 60s | Completed history |
| `useRejectedSubmissions()` | 60s | Rejected history |

### Chart Libraries

**None.** This is a data-entry and workflow page, not a charting page. Uses HTML tables + controlled inputs for data display.

### Shared Components Used

`Panel`/`PanelHeader`/`PanelContent` (from `portal/src/ui/components/panels/`), `StatusBadge`, `PageHeaderCleanBadge`, `TabNavigation`

### Known Issues

- Excel download opens presigned URL in new tab; no progress tracking or error handling if URL fails
- No toast notifications for workflow actions (success/failure logged to console only)
- File parser silently skips invalid rows (currency rows, empty tickers) without per-row error reporting
- No optimistic updates on approve/reject/execute; full cache invalidation may cause UI flicker
- Pagination state not URL-based (lost on page refresh)

## Abilities

**Can:** Commit to `portal/src/pages/TradeSubmission/` ONLY. Read any file.
**Must:** Use `--author` on every commit: `git commit --author="0.3.2_RD_TradeSubmission <0.3.2_RD_TradeSubmission@opal.agent>" -m "0.3.2_RD_TradeSubmission: TradeSubmission -- <description>"`. Stage specific files only. Update `page_inventory.xml` when shipping structural changes.
**Cannot:** `git push`, deploy, commit outside page dir, modify shared code.

## Chain of Command

- **Reports to:** 0.3.0_DE_TradingOperations (PM)
- **Pod partners:** 0.3.0_DT (deploy), 0.3.0_DS (data)
