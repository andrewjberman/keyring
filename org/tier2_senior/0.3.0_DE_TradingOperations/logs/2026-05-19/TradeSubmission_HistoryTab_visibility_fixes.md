# TradeSubmission HistoryTab — Trade Visibility Fixes (catch-up log)

**Agent:** 0.3.0_DE_TradingOperations
**Date:** 2026-05-19
**TO:** None — Andrew-direct empirical bug fixes (no task order). Catch-up log per README launch protocol (commits not covered by an existing session log).
**Portal DEV commits:** `bc5da3d2` -> `43b36707` -> `00841008`
**Workspace CLOUD commit:** see commit landing this log (catch-up + SSCN_DIVDEF TO closes)

---

## Why this log exists

Session-start launch protocol: three portal commits authored by `0.3.0_DE_TradingOperations`
on 2026-05-19 (13:21-13:33 EDT) post-dated the SSCN_DIVDEF.005 session log (written 13:05)
and were not covered by any session log. This is the catch-up log rectifying that gap
before other work.

---

## Objective

A real trade — Lauren-initiated `TRADE-20260518-181840-2E31B0`, approved + executed by
Andrew, DynamoDB `status=EXECUTED`, `brokerage_email_sent=true` — was invisible to the
user in the TradeSubmission History tab. Three iterative fixes to
`portal/src/pages/TradeSubmission/tabs/HistoryTab.tsx` closed the visibility gap.

---

## Work Completed (3 commits, 1 file)

### 1. `bc5da3d2` — surface EXECUTED trades alongside COMPLETE + REJECTED

The workflow does NOT auto-transition `EXECUTED -> COMPLETE` (`completeSubmission` is a
separate API action with no UI trigger). A just-executed trade was therefore in a limbo
state: gone from the Execution tab (no longer `APPROVED`) and not yet visible in History
(filter was `COMPLETE | REJECTED` only).

Fix: added a `useExecutedSubmissions` fetch, merged `EXECUTED` into `allCompletedTrades`,
extended the `mySubmissions` filter to post-approval states, added `'EXECUTED'` to the
`StatusFilter` type + dropdown, and updated panel title / help / empty-state copy.
Type union: `'all' | 'EXECUTED' | 'COMPLETE' | 'REJECTED'`.

### 2. `43b36707` — My Submissions view includes approved/executed trades, not just initiated

The "My Submissions" filter matched `initiator_email === userEmail` only, so a trade
Andrew approved + executed but did not initiate (Lauren initiated it) never appeared in
his "My Submissions" — only the "All Trades" view showed it.

Fix: union of (a) initiator-side trades via `getMySubmissions`; (b) trades where
`approver_email` / `executor_email` matches the user, resolved against the
`allCompletedTrades` pool. Dedupe by `submission_id`; sort newest-first. Renamed the view
"My Submissions" -> "My Trade History" to reflect the broader semantic. Loading / error
states updated to factor all 4 fetches.

### 3. `00841008` — USER view no longer hard-blocks on augmentation queries

`43b36707` made the USER view's `isLoading` / `error` depend on all 4 queries
(`myData` + `executed` + `completed` + `rejected`). If any one by-status augmentation
query was slow or errored, the USER view rendered "Failed to load submissions" instead
of any trades.

Fix: USER view now blocks only on `myData` (the initiator-side primary fetch). The
`executed` / `completed` / `rejected` augmentation queries degrade gracefully — the
involvement-based merge still runs from whatever data is available, and an empty
augmentation pool is harmless. AGG view behavior unchanged.

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| (none logged) | — | — | These were tight iterative single-file FE bug fixes to `HistoryTab.tsx` with no data-prop schema change, no new endpoint, no new React Query key shape (the new `useExecutedSubmissions` reuses the existing by-status fetch pattern). `comp-transform schema-check` / `comp-blast` were not run in-session; the change is render-logic-only within one tab component. Flagged here for transparency rather than left blank. |

`bun typecheck` reported `exit 0` on each of the three commits (per commit messages).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/TradeSubmission/tabs/HistoryTab.tsx` | Surface EXECUTED trades; union My-Trade-History over initiator + approver + executor involvement; graceful augmentation-query degradation | Yes — DEV `bc5da3d2` -> `43b36707` -> `00841008` |

---

## Current State

Three fixes committed to portal DEV. `HistoryTab.tsx` now surfaces a trade to a user
whenever they are involved as initiator, approver, or executor, and across the full
post-approval status set (`EXECUTED` / `COMPLETE` / `REJECTED`). USER view renders
available data rather than hard-failing on a slow augmentation query.

Not pushed — DE cannot push; portal DEV push is DT's gate.

## Next Steps

- [DevOps 0.3.0_DT] These 3 commits join the push-ready portal DEV stack. Not gated by
  SSCN_DIVDEF TO-4 — they are independent TradeSubmission bug fixes; safe to push to
  remote DEV on the next DT push cycle.
- [Dashboard Engineer] No further DE action; verify against the live `TRADE-20260518-181840-2E31B0`
  record after DT pushes and DEV redeploys.
