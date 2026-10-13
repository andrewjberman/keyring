# TCKT_VNEXT decomposition -- ROUND 16, 2026-10-13, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** Andrew, 2026-10-13 ~12:23Z, card 7 "Yes do it" (close `TCK-20261009-a1052909` and `TCK-20261012-13cd3a1d`), record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`; the CTO's relay msg 6909; the
never-widen pair `deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_CW1_CRAWL_PAIR.md` with COO-half AMENDMENT 1 (this seat) and CTO-half
AMENDMENT 1 @4fea908a37 (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R2_CW1_ONE_TICKET_CRAWL_CTO_HALF.md`), both SIGNED. No PRD
addendum; PRD v0.4 stands. FWD-1 is NOT REALIZED and was not run. Not a thread round: it closes two test tickets Andrew asked to be
closed, and grades no FWD of this project. `TCK-20261012-c546fead` is NOT a target (card 1 still needs it).

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `R16-cw-2` | ONE crawl sitting: one synthetic internal identity (LIST `["cottonwood"]`, one token of at most 20 minutes), the board's own claim then complete controls pressed for each of the two test tickets, the mail branch read after each claim, the identity removed after `exp`. A result file | support to Andrew's card 7 (open calls `fbb1`, `5cb1`); no FWD of this project | cut | applier seat | WORLD | -- | none |
| carried | everything in round 14's carried row, unchanged; the staff request (card 1) and TR-dp-24 are other seats' | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 1):** {`R16-cw-2`}. **Fan-out: 0 workers; one applier order.** The act mints a signed token from a secret and drives a
signed-in browser; a worker subagent holds neither.

## Rule 24 record

- **MECE over the pair's amended text.** Domain: its numbered steps 0 to 7 and AMENDMENT 1's six points. By subtraction: the identity
  and token (steps 2, 3), the two writes (step 4 per ticket), the board and item reads (step 5), the zero-call read (step 6), the
  removal (step 7), the mail branch (CTO condition 2) are each a numbered step of the order; nothing is uncovered, and the ledger is
  step 0.
- **Same grain:** one sitting, one identity, two tickets. **One axis:** the two tickets read `completed` and the identity is gone.
- **A name this cell does not choose:** the identity's address is fixed by the pair (AMENDMENT 1 point 4), and the ticket ids are the
  two targets; no id is typed from memory.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule). comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; the key read and the row
write are grants this box's agent user already holds, reported after the fact through `0.0.0_AB_MSTR~DELL2` as the pair says).
comp-adversary: the control is the check's independent live re-read of both tickets, the identity row and the card-1 ticket.

Dry-run at the base (box/dell2, 2026-10-13): `r16_cw2_close.py` FAIL (no result file), as expected. The identity's row key reads
ABSENT now and the walker row's key shape reads PRESENT (positive control).
