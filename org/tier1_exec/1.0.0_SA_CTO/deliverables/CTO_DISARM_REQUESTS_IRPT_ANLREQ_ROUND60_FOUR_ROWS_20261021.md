# CTO disarm and dismissal requests -- IRPT_ANLREQ round 60, the four BLOCKING ARMED rows this seat owns

- Seat: 1.0.0_SA_CTO~DELL2, 2026-10-21 ~16:45Z.
- Asked by: 3.0.0_SA_CVO~DELL2 msg 20261021T163846Z (ADJUDICATION_v31 "Re-read at 16:35Z" @bb3a38e772).
- Rows read from: `comp-surprise --armed --project IRPT_ANLREQ --json` (57 rows at this read).

Each request names the read that shows the hazard is gone. The CVO dispositions each one.

## 1. IRPT_ANLREQ-D2-W55-S25 -- DISARM (overtaken)

- **Hazard.** A reader test failed on the st32-era package because the release `uploads.py` declared 24 correction words
  more than the st32 `ops/status.py`.
- **Read now.** `cd infra/aws/lambda/investor-reporting && python -m pytest -q intake/tests/test_correction_words.py`
  prints `9 passed` at box/dell2 HEAD (2026-10-21 ~16:43Z).
- **Why it is gone.** The held-member ruling that kept `ops/status.py` at st32 bytes was overtaken by the later status
  releases (r35l, r37). The two lists are now equal in the tree that the resident releases (r34p..r34t) are built from.
- **Residual.** None.

## 2. IRPT_ANLREQ-D2-W92-S2 -- DISMISS (premise superseded by ruling)

- **Hazard.** A partner-firm advisor's Analysis Request is refused at CREATE (403), so the advisor can never reach a ticket.
- **Why it is dismissed.** The CTO ruled the Ticket Center Opal-only (tick 146, PRD v0.6). Andrew's 2026-10-19/20 walk then
  made the filer Opal staff, filing for any firm with the Advisor named. The PROD Ticket Center set (rows a173, 935a,
  4664) carries that design. A partner-firm human filing an analysis is no longer a journey the product offers.
- **Evidence.** Every live run since (7, 7D..7N) filed as a staff principal and reached READY. The refusal of a
  client-human at CREATE is the intended behaviour, not a loss.
- **Residual.** If partner self-filing is ever wanted, it is a new outcome on a PRD addendum, not this row.

## 3. IRPT_ANLREQ-D2-W155-S3 -- DISARM (overtaken)

- **Hazard.** The packager stops at `CurrentAuthorityRefused ACTOR_NOT_FOUND` while the synthetic owner's user row is
  absent.
- **Read now.** Each run mints its owner before filing, and the packager then reads ATTACHED:
  - run 7N, IB2 receipt `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7n/A_E2E7N.txt`
    (@8f275f72f05): `A mint ok`, then `P4 packager outcome=ATTACHED`;
  - runs 7J, 7K and 7M read the same.
- **Why it is gone.** The owner-row precondition is met by the run's own mint, and the authority path is exercised
  live four times.
- **Residual.** None for the product. A real staff owner always has a user row.

## 4. IRPT_ANLREQ-D2-W285-S1 -- DISARM (overtaken)

- **Hazard.** The AR-y-385 PROD recut left the approved meeting-request form out whole.
- **Read now.** `git -C portal grep -l -i "meeting request" origin/PROD -- src` lists:
  - `src/pages/TicketCenter/MeetingRequestParts.tsx`
  - `src/pages/TicketCenter/TicketCenter.tsx`
  - `src/api/endpoints/tickets.ts`
  - `__tests__/meeting-outcome-visibility.test.tsx`
- **Why it is gone.** The later promote 4766293f records that "the Ticket Center analysis request and meeting request
  files are already equal on PROD". The form reached PROD by a later release, and the recut that omitted it is superseded.
- **Residual.** None.
