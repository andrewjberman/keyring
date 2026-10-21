# TCKT_VNEXT round 23 -- FWD-5 exercised once on DEV (`2.0.0_SA_COO~V2`, dell2, 2026-10-21)

**Authority:** the CVO's `ADJUDICATION_v21` (`3.0.0_SA_CVO~DELL2`, 2026-10-21T02:45Z, signed at PRD v0.8): FWD-2 ticket arm REALIZED, FWD-4 REALIZED (the R20 DEV run: one filer filed, claimed and completed `TCK-20261017-da2a1987`), **FWD-5 NOT REALIZED on the evidence on file -- one live arm**; relayed by the CTO's msg 11772, which SUPERSEDES his msg 11766 (the FWD-4 arm). **No PRD change.** FWD-5's DONE WHEN: "EXERCISED -- an Opal person picks the next request to work from the queue alone"; ACCEPT: an Opal person reads each request's type and how long it has waited from the queue itself, and opens only the ones that are theirs.

**Withdrawn:** cell `R23-f4-1` (FWD-4 on DEV) and its order `TO-R23-F41`, committed @552a013e46 and cancelled before TV2 was told of it; `R20_CHECKS/r23_fwd4_check.py` stays in the tree as a record and is not graded.

## Enrichment list and what each item becomes
| # | item | cell | kind | write surface | risk |
|---|---|---|---|---|---|
| 1 | on DEV, two open tickets of different types on the board; an Opal person reads the board unclipped and claims one from the board without opening either; the full-board shot saved; which ticket was chosen and from what the person read, recorded; the synthetic tickets removed | `R23-fv-1` | RUN (the applier `0.7.0_AE_CloudOps~TV2`) | two `opal-tickets` items (created, one claimed, then deleted by key); two `opal-users-v2` rows (a filer and a picker, created then deleted) | WORLD |

## What the cell does
`R23-fv-1`: on the portal DEV served at `http://localhost:5174` (the one DEV origin; the pattern of `TO-R18-RUN`), a synthetic filer files one Service Request and one Other ticket; a SECOND synthetic internal identity, the picker, opens the board (the Ticket Center's queue page), takes a FULL-PAGE shot with both rows' type and age readable, chooses one by what it reads, and presses Claim on that row in the board without opening either ticket; a second full-page shot after the claim; both tickets are saved whole, then deleted by key after the tokens' `exp`, and both identity rows are deleted. The picker is a second identity so the claim is the queue's act and not FWD-4's self-claim. The DEV board reads the live tickets table, so it shows other open tickets too: the shot is the board as the page renders it, reviewed by TV2 for client account ids before it is saved (if any is visible, TV2 reports instead of saving). The check `R20_CHECKS/r23_fwd5_check.py` holds the record's side; the shots are the CVO's judgment.

## Chains and fan-out
**M = 1 chain:** {`R23-fv-1`}. **Fan-out: 1 of 1 chain, cap 4, reason:** one applier order (it holds the credentials a worker does not), no worker.

## Rule 24 record
The run's states: (the board shows both rows with type and age / one or neither) x (the Claim control is on the board row / only inside the ticket) x (the claim lands on the chosen ticket only / on both or the other) x (everything removed / left). The check admits only (both rows with type and age, the claim made from the board, the chosen ticket in_progress under the picker and the other still open and unassigned, all removed). A board with no Claim control on its rows is FWD-5 failing as the PRD words it ("opens only the ones that are theirs"): a STOP reported with the shot, never worked around by a claim made from inside a ticket.
