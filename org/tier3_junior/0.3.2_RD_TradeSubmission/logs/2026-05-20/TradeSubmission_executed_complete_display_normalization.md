# TRSB_LEDGER.014 -- EXECUTED/COMPLETE Display Normalization -- 0.3.2_RD_TradeSubmission

**Date:** 2026-05-20
**TO:** org/tier3_junior/0.3.2_RD_TradeSubmission/task_orders/TRSB_LEDGER.014.rd-executed-complete-display-normalization.md
**Issued by:** 2.0.0_SA_COO~B
**Project:** TRSB_LEDGER (PRD v0.1, section 3.5 + section 7 Q2)
**Portal commit (DEV branch):** f9b2d81e

## Objective

Andrew, verifying on :5175, saw "Executed" and "Complete" as two distinct status
labels and read them as different states. They are the same terminal state --
`COMPLETE` is the retired pre-Q2 name; `EXECUTED` is canonical (Andrew Q2 ruling
2026-05-18). Fix: display-normalize so a legacy `COMPLETE` trade renders identically
to `EXECUTED` at every status render site. Display-only -- no DynamoDB migration.

## What changed

### portal/src/pages/TradeSubmission/utils/tradeStatus.ts  (NEW)
Single shared helper module:
- `displayStatus(status)` -- user-facing label; `COMPLETE` folds to the `EXECUTED`
  label, every other status passes through with `_` -> space (matching the page's
  existing uppercase badge-label convention).
- `statusBadgeVariant(status)` -- StatusBadge color variant; `COMPLETE` maps to the
  same variant as `EXECUTED` (`running`) so a legacy COMPLETE row is identical in
  BOTH label and color (pre-fix it was a green "COMPLETE" badge vs EXECUTED's blue
  "EXECUTED" -- folding only the label would have left a color mismatch).

### portal/src/pages/TradeSubmission/components/TradeCard.tsx
- Removed the local `statusMap` block; badge color now via `statusBadgeVariant()`.
- Status label now `displayStatus(submission.status)` instead of the raw
  `submission.status.replace(/_/g, ' ')`.

### portal/src/pages/TradeSubmission/components/TradeDetailsModal.tsx
- Same: removed the copy-pasted `statusMap`; uses `statusBadgeVariant()` +
  `displayStatus()`.

### portal/src/pages/TradeSubmission/tabs/HistoryTab.tsx
- `StatusFilter` type narrowed `'all' | 'EXECUTED' | 'COMPLETE' | 'REJECTED'` ->
  `'all' | 'EXECUTED' | 'REJECTED'`.
- Status-filter dropdown: "Complete Only" option removed; one "Executed Only"
  option remains.
- Filter logic: `statusFilter === 'EXECUTED'` now matches BOTH `status==='EXECUTED'`
  and `status==='COMPLETE'` rows.
- Panel help text reworded ("executed / complete / rejected" -> "executed or
  rejected") so no user-facing prose says "complete" either.

Render-site coverage: the Execution and Approvals tabs render trades via `TradeCard`;
HistoryTab also renders via `TradeCard`. Fixing `TradeCard` + `TradeDetailsModal`
(the only two components that render a status badge) covers every tab. Confirmed by
grep -- no raw `COMPLETE` string reaches a user-facing label anywhere on the page;
the remaining `'COMPLETE'` references are status-logic guards (read-tolerance), not
labels.

## Acceptance criteria

| AC | Result |
|----|--------|
| AC1 -- single displayStatus() helper, applied at every render site; no raw COMPLETE label | PASS -- helper in utils/tradeStatus.ts; TradeCard + TradeDetailsModal both route through it; grep confirms no raw COMPLETE label |
| AC2 -- HistoryTab filter: one "Executed Only" matching EXECUTED+COMPLETE; StatusFilter type narrowed | PASS -- dropdown options ["All Statuses","Executed Only","Rejected Only"]; type is 'all'|'EXECUTED'|'REJECTED' |
| AC3 -- schema-check 0 MISSING; tsc -b 0 errors | PASS -- schema-check "All rendered fields match"; tsc -b --force exit 0 |
| AC4 -- visual smoke: COMPLETE shows "Executed"; filter returns both | PASS -- 5-check smoke, overall PASS |
| AC5 -- no DynamoDB write; COMPLETE stays in TradeSubmissionStatus | PASS -- display-only; TradeSubmissionStatus union untouched |
| AC6 -- no emoji; portal DEV commit; session log; RAVC2 with SHA | PASS -- f9b2d81e; this log; RAVC2 to COO~B cites the SHA |

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `comp-transform schema-check TradeSubmission` | 1 (before write) | "All rendered fields match their response types." 0 MISSING. Display-only mapping -- no schema change expected. |
| `comp-transform schema-check TradeSubmission` | 2 (before commit) | "All rendered fields match their response types." 0 MISSING -- no regression from the helper + StatusFilter narrowing. |
| `bun x tsc -b --force` | 2 (before commit) | Exit 0 -- zero TypeScript errors, including after `StatusFilter` dropped the `'COMPLETE'` member (no dangling reference). |
| `/frontend-dev` visual smoke | 3 (after commit) | PASS -- see below. |

comp-cache: not run -- no new React Query key introduced (this TO adds no data fetch).

## Visual smoke (Phase 3)

Route-mocked Playwright smoke (`trsb014_smoke.py`, workspace root) -- real login,
mocks the trade endpoints to return one `EXECUTED` row + one legacy `COMPLETE` row,
opens the History tab. Screenshots in `.runtmp/trsb014_history_*.png`.

| Check | Result |
|-------|--------|
| Filter dropdown options = [All Statuses, Executed Only, Rejected Only] | PASS -- "Complete Only" gone |
| Legacy COMPLETE row badge label = "EXECUTED" (not "COMPLETE") | PASS |
| EXECUTED row badge label = "EXECUTED" | PASS -- identical label + color to the COMPLETE row |
| "Executed Only" filter returns BOTH the EXECUTED and the COMPLETE row | PASS |
| No page errors | PASS |

`overall: PASS`. Screenshot `trsb014_history_default.png` shows both cards with an
identical blue "EXECUTED" badge -- pre-fix the legacy row was a green "COMPLETE"
badge. Non-fatal `401` console entries are unmocked real-API auth/analytics calls,
not page errors.

## Hand-off

- Portal commit **f9b2d81e** on portal DEV. Per the TO it becomes the 5th commit in
  TRSB_LEDGER.012's portal/PROD cherry-pick set
  (bc5da3d2 + 43b36707 + 00841008 + be5d7631 + f9b2d81e). SHA reported in the RAVC2.
- RD commits, RD does not push -- Pod DT handles the DEV push + PROD promotion (TO-012).
- Andrew's :5175 local-dev re-verify happens after this lands on DEV (DT pulls origin/DEV first).
- RAVC2 to 2.0.0_SA_COO~B citing f9b2d81e.
