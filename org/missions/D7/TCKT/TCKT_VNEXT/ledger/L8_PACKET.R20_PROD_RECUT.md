# TCKT_VNEXT round 20 -- L8 PACKET, part 1b (the PROD-based re-cut, cell R20-pt-4)

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-17 ~01:3xZ, on dell2. **For** `3.0.0_SA_CVO~DELL2` at L9, as a FILE. Not the L10 slug. Commits named are LOCAL on `box/dell2` unless a line says otherwise; the portal candidate is read on origin by ls-remote.
**Authority:** the CTO's rulings bc18 (R20-pt-1 is Opal-internal on PROD, msg 10089) and 4e37 (a PROD-based re-cut of `12c164a0` and `8e4f0885` WITHOUT `c05e3dda`, the four-point resolution of the one conflict, msg 10097; ruling file `1.0.0_SA_CTO~DELL2/RULING_4E37_FWD11_PROD_RECUT_WITHOUT_TRADE_FORM_20261017.md`). **Order:** `TO-R20-PP` (worker `0.9.0_WK_TCKT_VNEXT~51`, `<workstream>PRODCUT</workstream>`, issued 206ba8ddd2), drained at `b27df7d15d`. This packet grades ONE judgment: `R20PP-AC4J`.

## 1. What was built and where it is

Portal branch `cand/dell2/tckt-meeting-form-prod-recut`, head `4e1e35bfa0826bbf07971b4cc0bad76ff79edc9d` (on origin, ls-remote read), two commits on `origin/PROD` `fa21a303d87271a1e2d60c514d13501d71f9f020`: `e5c8e07569` (`cherry-pick -x 12c164a0`, the meeting form, auto-merged) and `4e1e35bfa0` (`cherry-pick -x 8e4f0885`, the outcome line and coordinator controls, one conflict in `TicketCenter.tsx`). Approval row `dell2-20261017T012634Z-8b35`, opal-internal, APPROVED by the CTO at that sha (msg 10131: five meeting files only, `TradeFormOpen` 0, the trade-form test 0, `App.tsx:505` and `firmAccess.ts:148-153` unchanged). **Not yet promoted:** the promote follows the DEV render read (`TO-R20-RV`, staged, waiting on the CTO's 5174 handover), as the CTO ruled.

## 2. For L9 -- the judgment

| judgment | what bears on it | evidence to read |
|---|---|---|
| `R20PP-AC4J` the resolution of `TicketCenter.tsx` is the CTO's four points; the meeting row shows on `showsMeetingOutcome(t)` and the controls only for a viewer in `routing.primary`; no Trade Request code reached the branch, hidden or not | (1) PROD's import `TradeRequestForm` alone, no `TradeFormOpen`; (2) the meeting imports incl. `showsMeetingOutcome` and `viewerIsCoordinator`; (3) PROD's `AnalysisDraftAndPackage` row kept, `AnalysisPackageRow` not pulled; (4) the row condition `showsMeetingOutcome(t)`, controls behind `internal && viewerIsCoordinator(t, auth.user?.email)`. Also: `drawsOwnForm` returns true for `trade_request` and `meeting_request`, so the Trade Request form's behaviour on PROD is unchanged and the type stays hidden from the New Ticket list (the `.filter(([v]) => v !== 'trade_request')` line is untouched) | `git -C portal diff fa21a303 4e1e35bfa0` (5 files, +1033 -7; the `TicketCenter.tsx` hunk is 32 lines); `deliverables/0.9.0_WK_TCKT_VNEXT~51/R20_PP_RECORD.json`; the issuer re-ran in the worker's worktree before teardown: `r20_pp_checks.py prod-diff` `R20-PP-DIFF-OK 5 files`, `prod-tests` `R20-PP-TESTS-OK pass=24`, `r20_checks.py portal-tsc` `R20-TSC-OK`; the worker's folder run 152 of 152 across 26 files (base 128 of 128 across 24) |

## 3. Limits (what this packet cannot show)

- **Nothing was rendered.** The re-cut is graded on the diff and tests; the rendered read is `R20RV-AC1J`, on the DEV build, and is still not in any packet. The round is not closeable, and FWD-11 is NOT REALIZED, until `R20RV-AC1J` is graded.
- **The PROD page was not run.** A PROD build is read after the promote; this packet does not claim it.
- `round-close-check --round 20` reads `orders=5 judgment=3 graded=2 ungraded=1 verdict=REFUSED` before this grade (the CVO's v9 graded `R20LM-AC3J` and `R20PT-AC4J`).
