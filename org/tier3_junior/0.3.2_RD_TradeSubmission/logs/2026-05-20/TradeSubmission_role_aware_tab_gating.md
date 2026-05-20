# TRSB_LEDGER.008b -- Portal Role-Aware Tab Gating (A4 fix) -- 0.3.2_RD_TradeSubmission

**Date:** 2026-05-20
**TO:** org/tier3_junior/0.3.2_RD_TradeSubmission/task_orders/TRSB_LEDGER.008b.rd-portal-role-aware-gating.md
**Issued by:** 2.0.0_SA_COO~B
**Project:** TRSB_LEDGER (PRD v0.1, section 2.A A4 + section 7 Q2)
**Portal commit (DEV branch):** see hand-off section

## Objective

Gate the TradeSubmission portal's privileged tabs on actual trade-group membership
instead of firm identity (closes hole A4: "portal gates on firm, not role"), and
remove the orphaned `completeSubmission` FE function (FE side of the Q2 COMPLETE
retirement -- Andrew 2026-05-18: COMPLETE retired, EXECUTED is the terminal state).

## Gate / dispatch

TO was `staged` + `dispatch_held` on TRSB_LEDGER.008. On boot, confirmed the gate
cleared: AE 0.7.0 delivered the `/api/general/trades/users/me` endpoint contract
(2026-05-18 18:37Z). COO~B fired the GO 2026-05-20 ~14:20Z; TO flipped to `pending`.

Endpoint contract (from AE 0.7.0 / TRSB_LEDGER.008):
- `GET /api/general/trades/users/me` -- behind the portal JWT authorizer, no params,
  caller resolved server-side from the JWT principal.
- Response 200: `{ email, name, groups: string[], role }`.
- Fail-closed: a caller with no trade-users row returns 200 with `groups: []` (NOT an
  error). `[]` means "show no privileged tabs".

## What changed

### portal/src/api/endpoints/trade-submission.ts
- Added `TradeUserMe` interface (`{ email, name, groups: string[], role }`) and
  `getTradeUserMe()` -- `GET /api/general/trades/users/me`.
- Removed the orphaned `completeSubmission()` function (no call sites existed --
  verified via repo-wide grep; only the definition was present).
- Removed `'complete'` from the `WorkflowActionRequest.action` union (orphaned
  write-path; `WorkflowActionRequest` is referenced only within this file).
- Kept `'COMPLETE'` in the `TradeSubmissionStatus` union with a comment: it is
  READ-tolerance only. TRSB_LEDGER.004 does not migrate historical rows, so legacy
  `COMPLETE` records still exist and must render without error.

### portal/src/pages/TradeSubmission/hooks/useTradeSubmissionState.ts
- Added `useTradeUserMe()` React Query hook + the `tradeUserMeKey` (`['trade-user-me']`),
  `staleTime: 5min`, `refetchOnWindowFocus: false` (permissions change rarely).

### portal/src/pages/TradeSubmission/TradeSubmission.tsx
- Replaced `isInternal = claims?.firmId === 'opal-capital'` with group-based gating:
  `canApprove = groups.includes('approvers')`, `canExecute = groups.includes('executors')`,
  where `groups = tradeUser?.groups ?? []` from `useTradeUserMe()`.
- Removed `claims` from the `useAuth()` destructure (no longer referenced here).
- The Approvals tab + content render only when `canApprove`; the Execution tab +
  content render only when `canExecute`. Submit + History remain visible to every
  authenticated user. `allowedTabs` clamps a stale `initialTab` / `activeTab` to Submit.
- The Execute button (inside ExecutionTab) and approve/reject controls (inside
  ApprovalsTab) are transitively gated -- those tabs only mount when the group grants
  them, and the tab-content render is independently gated as belt-and-suspenders.

Note: HistoryTab's separate use of `claims.firmId` for firm-scoping the "All Trades"
view is a data-visibility scope, not an A4 privilege gate -- left untouched (out of scope).

## Acceptance criteria

| AC | Result |
|----|--------|
| AC1 -- privileged tabs gate on `groups`, firm gate removed | PASS -- `isInternal` firm gate replaced by `canApprove`/`canExecute` from /users/me |
| AC2 -- React Query hook for /users/me, zero key collisions | PASS -- key `['trade-user-me']`; `comp-cache collisions` shows 0 collisions involving it |
| AC3 -- completeSubmission + call sites removed; EXECUTED terminal; legacy COMPLETE renders | PASS -- function removed (0 call sites); COMPLETE kept read-only; smoke `history_legacy_complete` PASS |
| AC4 -- schema-check 0 MISSING, `tsc -b` 0 errors | PASS -- schema-check "All rendered fields match"; `tsc -b --force` exit 0 |
| AC5 -- visual smoke: Execution hidden for non-executor, visible for executor | PASS -- 4-state route-mocked smoke, all PASS |
| AC6 -- no emoji; committed to portal DEV; session log + RAVC2 | PASS -- no emoji in changes; committed; this log; RAVC2 to COO~B |

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `comp-transform schema-check TradeSubmission` | 1 (before write) | "All rendered fields match their response types." 0 MISSING. `groups` not yet wired -- expected. |
| `comp-cache collisions` | 1 (before write) | 4 collisions, ALL in AdvisorIntelligence; none involve any trade key. New key `['trade-user-me']` is collision-free. |
| `comp-transform schema-check TradeSubmission` | 2 (before commit) | "All rendered fields match their response types." 0 MISSING after wiring. |
| `bun x tsc -b --force` | 2 (before commit) | Exit 0 -- zero TypeScript errors across the portal, including after the `completeSubmission` removal. |
| `/frontend-dev` visual smoke | 3 (after wire) | PASS -- see below. |

## Visual smoke (Phase 3)

Route-mocked Playwright smoke (`trsb008b_smoke.py`, workspace root) -- mocks
`GET /api/general/trades/users/me` with four group states, real login
(michael@opalinvest.com, an `opal-capital` internal user -- pre-fix the firm gate
would have shown all 4 tabs), navigates to `/trade-submission`, asserts the tab set.
Screenshots in `.runtmp/trsb008b_*.png`.

| State | groups | Tabs seen | Result |
|-------|--------|-----------|--------|
| both | `[approvers, executors]` | Submit, Approvals, Execution, History | PASS |
| exec_only | `[executors]` | Submit, Execution, History (Approvals absent) | PASS |
| approv_only | `[approvers]` | Submit, Approvals, History (Execution absent) | PASS |
| none | `[]` | Submit, History (both privileged tabs absent) | PASS |
| history_legacy_complete | n/a | legacy `COMPLETE` row renders in History, no page errors | PASS |

`overall: PASS`. The `none` state is the decisive A4 proof: an `opal-capital` internal
user with `groups: []` sees only Submit + History -- the firm-identity gate no longer
governs the privileged surfaces. Non-fatal `401` console entries in every state are
real-API calls for endpoints not route-mocked (auth/analytics) -- not page errors, not
introduced by this change.

## Hand-off

- Portal code committed to the portal submodule **DEV** branch (RD commits, RD does
  not push). Pod DT (0.3.0_DT_TradingOperations) handles the DEV push + gitlink bump
  per the standard portal flow. PROD promotion is a separate DT-lane TO
  (TRSB_LEDGER.013, authored by COO~B after this TO).
- RAVC2 to 2.0.0_SA_COO~B.
