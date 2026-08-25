# DEPLOY-COMPLETION LEDGER -- portal DEV->PROD promote: Submit-a-Request FULL REMOVAL (D7_TICKETING)

**Opened:** 2026-08-25T17:02:59Z by 0.3.0_DT_TradingOperations (DT lane, /prod-deploy) -- AT DEPLOY-START
**Status:** OPEN -- promote in flight
**Authority:** Andrew-direct 2026-08-25 ~16:2xZ (relayed 1.0.0_SA_CTO msg 70751) and ~16:4xZ
(scope widened to full removal, relayed 0.0.0_AB_MSTR msg 70772). PROD clearance: MSTR msg 70796
[CLEARED-PROD] after site Z's promote concluded SUCCESS on two instruments.

## ANDREW VERBATIM
16:2xZ: "D7 is effectively on hold, however with that said, I want the 'Submit a Ticket' sidebar
item pulled off dashboard. That whole functionality is broken and shouldnt even be on the
dashboard. Mention this to MSTR and have them bring out an 0.3.0_DT_TradingOperations to go get
rid of it and /prod-deploy"

16:4xZ: "some agent at some point some agent thought it would be a good idea to make a separate
page/function from Ticket Center rather than repurposing a client-facing version of Ticket Center
(which was the wrong direction) and this page has existed ever since and I do not want it"

## THE ACT
Promote portal DEV -> PROD carrying commit `18fd5b38` (FULL frontend removal of the
Submit-a-Request page) + merge `4ac152f8`. Landed on origin/DEV at 4ac152f8 (VALGATE PASS).

SCOPE -- WIDER THAN THE NAV ENTRY, STATED EXPLICITLY:
  src/App.tsx                        nav entry, orphaned Send import, lazy import, the route
  src/lib/firmAccess.ts              3 partner allowlist entries (49financial, cottonwood, demo)
  src/pages/SubmitRequest/           the page
  src/api/endpoints/ticket-intake.ts the submit-path client (removed only after a reference
                                     search proved no other importer)
  TOTAL: 5 files, 363 deletions, 0 insertions.

TICKET CENTER SURVIVES: /ticket-center, pages/TicketCenter/, api/endpoints/tickets.ts untouched.
Backend /api/scoped/tickets/submit and opal-ticket-api NOT in this change -- frontend only.
Disjoint from the live AGG/Factor Tilts sovereign scope (verified: 0 Factor Tilts files in diff).

## PRE-FLIGHT (before the act)
  bun run build  rc=0   |  bun run lint  rc=0 (0 errors)  |  residue scan CLEAN
  RENDERED ACCEPTANCE (merged tree, ui-smoke /market, sidebar expanded, PNG read):
    "Submit a Request" ABSENT **and** Security Scanner + Portfolio Management + Trade Submission
    + Ticket Center ALL RENDER in the same read, same Tools section; all four nav sections paint.
    The surviving siblings are the positive control -- an absence with no positive control beside
    it is not a measurement.

## PRE-REGISTERED READINGS
- CI conclusion != success on the PROD headSha -> ROLLBACK to the recorded PROD base, close the
  ledger ROLLBACK, escalate loud to MSTR. Do not leave a half-landed promote.
- Parity gate `git diff origin/DEV HEAD` non-empty in the worktree -> ABORT before pushing PROD.
- If MSTR reports site Z's L7 rendered verification RED mid-flight -> STOP and report rather than
  completing onto a base under investigation (MSTR 70796 condition).

## CLOSURE
(pending)
