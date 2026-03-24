# DEBT_1STRUN Scan -- 0.3.3_RD_DataRefresh
**Date:** 2026-03-23
**Scope:** portal/src/pages/DataRefresh/
**Status:** FIXED -- all 22 findings resolved (see fixes below)

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | constants.ts | 4-50 | C1 Dead | Medium | `PIPELINE_STEPS` array is defined but never imported by any file in DataRefresh or elsewhere in the portal. Removing it changes zero behavior. |
| 2 | constants.ts | 61-92 | C1 Dead | Medium | `STATUS_COLORS` object is defined locally but never imported by any DataRefresh component. PipelineProgress.tsx imports `STATUS_COLORS` from `@/ui/components/statusColors` instead. This entire block is dead code. |
| 3 | constants.ts | 53-58 | C1 Dead | Low | `ACCEPTED_FILE_TYPES` is defined but never imported by any DataRefresh file. FileDropZone.tsx hardcodes its `accept` attribute directly (line 149: `accept=".pkl,.json,.xlsx,.csv"`). |
| 4 | constants.ts | 61-92 | C2 Deprecated | Medium | Local `STATUS_COLORS` is superseded by the shared `@/ui/components/statusColors` module. PipelineProgress.tsx already migrated to the shared version, but this local copy was never cleaned up. |
| 5 | components/FileDropZone.tsx | 44-48 | C3 Duplication | Medium | `formatFileSize()` is duplicated identically in UploadProgress.tsx:21-25. Both have the same B/KB/MB logic. Should be a shared utility. |
| 6 | components/FileDropZone.tsx | 32-37 | C3 Duplication | Low | `FILE_TYPE_ICONS` map is duplicated identically in UploadProgress.tsx:9-14. Same icon mapping in two sibling components. |
| 7 | components/FileDropZone.tsx | 39-42 | C3 Duplication | Low | `getFileIcon()` is duplicated identically in UploadProgress.tsx:16-19. Same extension-lookup logic in two sibling components. |
| 8 | components/FileDropZone.tsx | 13-30 | C3 Duplication | High | Manifest parsing logic (`parseManifestSync`) duplicates the same parsing in useDataRefreshState.ts:210-226. Both parse manifest.json, filter `_pkl`/`_excel`/`_csv` keys, and build the same ManifestFile shape. If the manifest format changes, two locations must be updated. |
| 9 | components/CurrentStatePanel.tsx | 63-75 | C3 Duplication | Low | `FILE_TYPE_LABELS` is redefined with different/extended entries vs constants.ts:95-101. CurrentStatePanel adds `valuation`, `risk_premium`, `correlation`, `macro`, `market_overview`, `positioning` which constants.ts lacks. Two sources of truth for file type display names. |
| 10 | components/CurrentStatePanel.tsx | 29-40 | C3 Duplication | Low | `formatRelativeTime()` is duplicated identically in `components/market-performance/KeywordSentimentModal.tsx:76`. Same time-ago formatting logic in two unrelated components. |
| 11 | tabs/HistoryTab.tsx | 36-42 | C3 Duplication | Low | `formatDuration(seconds)` and PipelineProgress.tsx:116-125 `formatDuration(startedAt, completedAt)` both format m/s durations with different signatures. Same concept, different interfaces -- drift risk if formatting convention changes. |
| 12 | hooks/useDataRefreshState.ts | 198 | C4 Hardcoded | Low | Pipeline polling interval `3000` (3s) is a magic number. Not configurable or named as a constant. |
| 13 | hooks/useDataRefreshState.ts | 418 | C4 Hardcoded | Low | History page size `20` is a magic number passed to `getDataRefreshHistory()`. |
| 14 | hooks/useDataRefreshState.ts | 181 | C4 Hardcoded | Low | Minimum progress floor `Math.max(50, progress)` uses magic number `50`. The `5` on line 175 is also undocumented. |
| 15 | components/CurrentStatePanel.tsx | 18 | C4 Hardcoded | Medium | API path `/api/general/json/latest/manifest.json` is hardcoded inline in `fetchPortalManifest()`. Should come from a route config or API module. |
| 16 | components/CurrentStatePanel.tsx | 53-57 | C4 Hardcoded | Low | Staleness thresholds (7 days = Fresh, 30 days = Aging, else Stale) are magic numbers in `getStalenessStatus()`. |
| 17 | components/PipelineProgress.tsx | 383 | C4 Hardcoded | Medium | AWS Console URL `https://console.aws.amazon.com/states/home?region=us-east-1` has region hardcoded. If the pipeline moves regions, this link breaks silently. |
| 18 | tabs/HistoryTab.tsx | 113 | C4 Hardcoded | Low | `RESTORE_COOLDOWN_MS = 3 * 60 * 1000` is named but its value (3 min) is arbitrary with no documentation of why 3 minutes. |
| 19 | hooks/useDataRefreshState.ts | 345 | C4 Hardcoded | Low | Retry wait estimation `Math.max(1, 3 - ageMinutes)` uses magic number `3` (assumed pipeline duration). |
| 20 | hooks/useDataRefreshState.ts | 460-462 | C6 Stale Error | High | `rollbackToExecution` catch block only calls `console.error`. User gets no toast, no UI feedback that rollback failed. They see "processing" state that never resolves. |
| 21 | hooks/useDataRefreshState.ts | 435-436 | C6 Stale Error | Medium | `refreshHistory` catch block only calls `console.error`. If the history API fails, user sees the loading spinner stop with no explanation. |
| 22 | hooks/useDataRefreshState.ts | 224-226 | C6 Stale Error | Medium | Manifest parse error in `uploadFiles` is caught and logged to console only. User proceeds with `manifest: null` and gets no indication their manifest.json was malformed. |

## Summary
- Total findings: 22
- By category: C1: 3, C2: 1, C3: 7, C4: 8, C5: 0 (C1 findings #1-3 cover orphaned constants; no orphaned routes or lazy chunks found), C6: 3
- High severity: 2
- Recommended priority fixes:
  1. **#8 (C3 High)** -- Deduplicate manifest parsing between FileDropZone and useDataRefreshState. Single parse function prevents format-change bugs.
  2. **#20 (C6 High)** -- Add user-facing error feedback (toast) to `rollbackToExecution` catch. Silent failure on rollback is a critical UX gap.
  3. **#1-3 (C1 Medium)** -- Remove dead exports from constants.ts (`PIPELINE_STEPS`, `STATUS_COLORS`, `ACCEPTED_FILE_TYPES`). These are unused and mislead readers into thinking they are load-bearing.

## Fixes Applied

| Fix | Findings | What Changed |
|-----|----------|--------------|
| Deleted dead code from constants.ts | #1, #2, #3, #4 | Removed `PIPELINE_STEPS`, `STATUS_COLORS`, `ACCEPTED_FILE_TYPES`, type import |
| Created utils.ts with shared functions | #5, #6, #7, #10, #11 | `formatFileSize`, `getFileIcon`, `FILE_TYPE_ICONS`, `formatRelativeTime`, `formatDurationSeconds`, `formatDurationRange` |
| Shared `parseManifest()` in utils.ts | #8 | Single manifest parsing function used by both FileDropZone and useDataRefreshState |
| Merged FILE_TYPE_LABELS in constants.ts | #9 | Consolidated CurrentStatePanel labels into constants.ts; CurrentStatePanel now imports |
| Named constants for magic numbers | #12-19 | `PIPELINE_POLL_INTERVAL_MS`, `HISTORY_PAGE_SIZE`, `UPLOAD_COMPLETE_PROGRESS_FLOOR`, `INITIALIZING_PROGRESS`, `STALENESS_FRESH_DAYS`, `STALENESS_AGING_DAYS`, `ESTIMATED_PIPELINE_DURATION_MIN`, `AWS_CONSOLE_SFN_URL`, `MANIFEST_STALE_TIME_MS`, `RESTORE_COOLDOWN_MS` |
| Added error toasts to silent catch blocks | #20, #21, #22 | `rollbackToExecution`, `refreshHistory`, manifest parse all now show toast errors |
| Replaced manual fetch with publicApiRequest | #15 | CurrentStatePanel uses shared API client instead of hardcoded fetch + localStorage |

**Build status:** Clean (only pre-existing PortfolioManagement errors remain, unrelated to DataRefresh)
