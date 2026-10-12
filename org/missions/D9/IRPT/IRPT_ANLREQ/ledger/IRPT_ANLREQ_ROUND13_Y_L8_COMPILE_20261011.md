# IRPT_ANLREQ round 13, workstream Y -- L8 COMPILE: the queue age's two corrections on portal DEV; and the read of the one-account check, which moves the check to another file

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Input: the CTO's round-13 analysis @7542d8555c. Decomposition:
`decompositions/IRPT_ANLREQ_DECOMP_R13_Y.md`. Issuance @56d7070068, fanout 2 of 2. Both orders complete.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 13` at this compile: 11 orders in scope, judgment 4, graded 2,
ungraded 2, verdict REFUSED -- the two ungraded judgments are section 3's, yours.

Claim words: MEASURED = this seat ran or read it; RECORD = a worker's committed record this seat opened.

## 1. AR-y-131 -- the queue age: hours up to 72, and only for a closed list of waiting statuses. ON portal DEV.

- Merged @c5974bde4b; portal candidate `d3ef4a5d88` approved by the CTO (msg 5805) and landed by `0.0.0_AB_MSTR~DELL2` with CI success
  (its receipt, msg 5820; DEV hash MEASURED by ls-remote at 20:51Z).
- The rule as built: `under a minute`; minutes below one hour; HOURS from one hour up to but not including 72 (`47 hours`,
  `71 hours`); whole days from 72 hours (`3 days`; 95 hours reads `3 days`, 96 hours `4 days`). One earlier expectation changed:
  24 hours now reads `24 hours`, not `1 day`.
- `WAITING_STATUSES` is `readonly TicketStatus[]` = `open`, `in_progress`; the cell decides by membership.
- RECORD, the statuses read: the portal's type (`src/api/endpoints/tickets.ts:13`) and the service's list
  (`infra/aws/lambda/ticket_center/lambda_function.py:155`) both hold exactly `open`, `in_progress`, `completed`. The worker found NO
  per-type status definition on the service side, only that shared list. So the closed list equals "not completed" today and
  differs only for a status added later.
- MEASURED on the head: `Y131-AGE-OK` (9 tests), `Y131-KEEP-OK` (TicketCenter 62 pass, 0 fail), `PORTAL-TSC-OK`, eslint 0 errors and
  1 warning, proof VALID. The whole suite, run before the last DEV merge: 1373 pass, 3 fail, 1 error, 0 under TicketCenter
  (placed as this worktree's by `2.0.0_SA_COO~D2`'s run of the Investor Reporting suite on DEV, msg 5756; INHERITED).
- NOT LOOKED AT as a page this round (round 12's look stands for the layout; this round changed the unit rule and a list).

## 2. AR-y-132 -- the READ of the one-account check (TCKT_VNEXT FWD-3). Merged @aae18dd730. No product file changed.

RECORD: `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (blob `5ea3c6b4d4`); rows `IRPT_ANLREQ-D2-W52-S9`, `-S10`,
`-S11`. MEASURED by this seat: `Y132-READ-OK` on both trees (7 signals, 4 of 4 kinds, 5 proposed cells), proof VALID. The readings
below are the worker's; this seat did not re-run the door.

- **The door the form reaches is NOT `parse.py`.** The deployed service refuses that lane by name (`CSV_LANE_NOT_COMPOSED`); the
  form always sends the file itself, and the lane that takes it (`template_reader.py`) reads only columns A and B of the first
  sheet. My order, the ruling it followed and the earlier read all named `parse.py`: a check built there would never run (row S9).
- **What the door does today**, run in process on four synthetic sheets with an offline provider stub:

  | kind | result | turned back | says what to fix |
  |---|---|---|---|
  | several accounts (a third column naming the account) | accepted; the account column is dropped and rows for the same ticker merge | no | no |
  | a totals row labelled "Total" | accepted, the total counted as a holding (twice the sheet's real sum) | no | no |
  | a holding that cannot be priced (a shares sheet) | turned back with a code | yes | no |
  | a known-good sheet | accepted | no | n/a |

  Limits, the worker's: the stub admits any symbol-shaped word, so whether the LIVE provider refuses the symbol `TOTAL` was not run;
  no live provider, resident or real sheet was used.
- **Recognition of several accounts:** seven signals weighed. Two are offered as rules (an account-named column holding two or more
  distinct values; a repeated header row), both INFERRED: the repository holds no example of either. Three are rejected for a high
  false-positive risk (the same ticker on several rows is tax lots; subtotal rows and label-only lines are asset-class groupings
  in the repository's own fixtures).
- **What cannot be turned back at the door at all:** stacked tables with no account column, no repeated header and one worksheet
  look like one account; a total with no recognisable label; and pricing, which is decided later in the resident, not at the POST.
- **The form:** shows a refusal as "Review required" with one line per finding; a finding has words only for 4 codes, otherwise the
  raw code and row. And the first answer is always RESOLVING, so a person sees a refusal only on a second press (row S11).
- **Five proposed cells** (census in the reader; error findings; words for the codes; the release; optionally the form re-posting),
  with four questions a ruling must settle first: what counts as several accounts; whether a totals row is turned back or dropped
  and compared with the sum; whether a words-only edit to `ops/status.py` is in this project's grant; whether two presses are
  acceptable for FWD-3.

## 3. For L9 -- two judgments

- `AR131-y-AC3`: the statuses named as waiting are the ones in which a ticket is waiting on Opal, read from the ticket type's
  definition, and a person ranking the queue is not misled by the unit. Note for the grade: no per-type definition exists to read.
- `AR132-y-AC2`: the record is enough to cut the build, and no signal is offered that a one-account sheet would commonly trip.

## 4. Unchanged

Release 5's return, then the fallback's removal: HELD after the PROD push of portal `fc876722`, which waits on Andrew. MEASURED
20:51Z: the history reader is not on portal PROD `37aa1247ee`.
