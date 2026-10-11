# IRPT_ANLREQ round 10, workstream Y -- L8 COMPILE: the Open read's fallback on DEV, the composition-read entry builds live with its check on, the census and pair for release 5's return

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Input: the CTO's round-10 analysis @57cdd1cdde. Decomposition:
`decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md`. Issuance @487f73663e, fanout 3 of 3.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 10` at this compile: 12 orders in scope, complete 11, proof_ok 11,
proof_bad 0, judgment 3, graded 2, ungraded 1, verdict REFUSED -- the one ungraded judgment is `AR103-y-AC2`, section 4, yours.

Claim words: MEASURED = this seat ran or read it; RECORD = a worker's committed record this seat opened.

## 1. AR-y-101 -- the Open read's one fallback (row `IRPT_ANLREQ-D2-S51`). ON portal DEV.

- Built twice. The first build keyed on `UNEXPECTED_OWNED_READ_QUERY`, the code the analysis and my face named. The CTO refused it
  (msg 5465): that string is an exception MESSAGE and is never served. MEASURED by this seat in the LIVE `irpt-status` package (the
  downloaded zip, digest `6idtFvAm`, 49 members): the reasons map at `entry.py:252` serves class `RequestReadRefused` as
  `INVALID_INPUT`. AMENDMENT 1 @9a9dc17b61 re-opened the order; the check now refuses the unserved string.
- As landed: `readTicketReport` in `src/pages/TicketCenter/analysisRequest.ts`, used by both call sites; one second read without the
  ticket id only on `publicReasonCode` `INVALID_INPUT`; `REPORT_TICKET_MISMATCH` and every other reason never retried.
- MEASURED: 4 fallback tests pass; TicketCenter 53 pass, 0 fail; tsc OK; eslint 0 errors, 6 warnings. CTO approved (msg 5487);
  `0.0.0_AB_MSTR~DELL2` landed DEV `3ebc35ebf2`, CI success (its receipt, msg 5505; DEV hash MEASURED by ls-remote).
- NOT MEASURED by anyone: a live refused read arriving at the page as `INVALID_INPUT`. No live call was made.
- `INVALID_INPUT` is broad (about 25 raise sites on the report read). The CTO accepted the breadth and ruled the fallback
  TRANSITIONAL: the release that makes the binding live removes it (section 3).
- THIS SEAT'S DEFECT: I merged the first build before re-reading a proof check that had printed INVALID (I had pointed it at the
  worker's path from the shared tree); the re-read on the merged copy was VALID.

## 2. AR-y-102 -- the composition-read entry builds the live digest with its parity check ON (row `IRPT_ANLREQ-D2-S34`). Merged @908c44ed5e.

- Seven other files of `reports/` declared `outside_package`; the four unpinned members pinned at `35044a21aa` by the sha256 of the
  pinned bytes; 33 lines added to one map entry. MEASURED: `Y102-BUILD-OK` on the worker's tree and on the shared tree after the
  merge: 16 of 16 pinned, a build with NO skip prints `DbvBUxTG...`, the live digest.
- The negative control I ordered could not be read as written: with one byte of a pinned member changed and uncommitted, the build
  REFUSES and prints no digest (row `IRPT_ANLREQ-D2-W53-S1`). That is a stronger guard than a pin that silently wins; my face did not
  know it existed.
- I corrected the entry's stale note that said the skip was needed (@fde5036262) and re-ran the check.
- Not done, stated: `irpt-intake-poller`, the other function row S34 names (a missing member file; stays on that row).

## 3. AR-y-103 -- the census for release 5's return, and the pair. Merged @1b10155228. WRITTEN AND HELD.

- RECORD: a proposed `irpt-status` entry with all 49 members at ONE pin (`487f73663e`), built twice to `EXu+Izn1...` with no skip; the
  map itself untouched (MEASURED by the check: the map is clean and still records the live digest). 16 members differ from live; 5
  change a served answer; 11 read INERT (10 measured by calling both packages, 1 inferred).
- The half this morning's record lacked: each served change names its portal reader on PROD and on DEV. ONE reader on PROD does not
  admit the new answer: the history reader (`owned-requests.ts`), fixed on DEV by `cbd5cc66` with `a3f99d6e`.
- A correction to my own packet: the reason set in `Page.tsx` is NOT a PROD precondition (PROD admits any upper-case reason; no PROD
  caller sends `ticket_id`).
- Row `IRPT_ANLREQ-D2-W52-S8`: five members of the entry had no `staged_from` row at all.
- The pair: `deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_RETURN_IRPT_STATUS.md`. Its precondition is the
  history reader on portal PROD. By CTO msg 5511 that candidate (Investor Reporting only, outside the print route) is cut by
  `2.0.0_SA_COO~D2` and waits on no word. The pair names the fallback's removal as a step after the after-reads.

## 4. For L9

`AR103-y-AC2` (judgment): every `CHANGES_SERVED_ANSWER` row names the portal reader that actually decides whether PROD admits the new
answer, and no member read `INERT` changes what a caller is served. Artifact: the census,
`deliverables/0.9.0_WK_IRPT_ANLREQ~52/r10/RETURN_CENSUS_IRPT_STATUS.json` (blob `83fe9f0ab6`). What I could not check: readers
outside the portal repository; `acceptance.py`'s INERT is inferred.

## 5. Rows

| row | state |
|---|---|
| IRPT_ANLREQ-D2-S51 | ARMED until the landing; the landing is done (DEV `3ebc35ebf2`); the close is its disarm owner's (the CTO) |
| IRPT_ANLREQ-D2-S34 | the composition-read half is fixed; the intake-poller half stays open |
| IRPT_ANLREQ-D2-W53-S1, -W52-S8 | observations, filed by the workers |
| IRPT_ANLREQ-D2-S26 | ARMED, unchanged (one test message on the commentary-ready queue until about 2026-10-15T06:10Z) |
