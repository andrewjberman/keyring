# IRPT_ANLREQ round 12, workstream Y -- L8 COMPILE: the Ticket Center queue list shows each open ticket's elapsed age

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Input: CTO ruling msg 5690 ("NOW, as its own cell"), on CTO msg 5682
(TCKT_VNEXT FWD-5, passed by `2.0.0_SA_COO~V2` msg 5683). Decomposition: `decompositions/IRPT_ANLREQ_DECOMP_R12_Y.md`. Issuance
@29ccf76931, fanout 1 of 1. One order, `IRPT_ANLREQ.TO-AR-y-121`, complete, merged @4d7f0c1fe2.

Claim words: MEASURED = this seat ran or looked at it; RECORD = the worker's committed record this seat opened.

## 1. What was built (portal branch `wk-IRPT_ANLREQ-51-portal-r12` @c2c6a8aedd, on origin; NOT on DEV at this compile)

- `src/pages/TicketCenter/elapsedAge.ts`: a pure helper; the age is the largest whole unit that is at least one, in words
  (`under a minute`, `48 minutes`, `5 hours`, `3 days`; singular for one). No created time, an unparseable one, or one after the
  viewer's clock returns the empty string: never zero, never a negative age.
- `TicketCenter.tsx`: the list's created cell shows the created time as before and, for a ticket whose status is `open` or
  `in_progress`, the age beside it in brackets, in a class the table already uses. A `completed` ticket shows the created time alone.
  The age is computed at render against the viewer's clock; it does not tick while the page sits open.
- 3 files over DEV, +118/-1. No service change; no column added.

## 2. MEASURED on the candidate's head (after merging portal DEV `44ec7e70a9` into it)

- `Y121-AGE-OK` (5 named tests; the test file holds no `Date.now()` and no bare `new Date()`), `Y121-KEEP-OK` (TicketCenter 58 pass,
  0 fail), `PORTAL-TSC-OK`, eslint 0 errors and 1 warning (an export that predates the cell), proof VALID on the merged copy.
- The whole portal suite: 1369 pass, 4 fail, 1 error, 27 skip of 1400 tests. 0 of the failures are under `TicketCenter`; they are in
  Investor Reporting tests, one of them a module missing from this worktree. NOT MEASURED: the same suite on DEV's own head, so
  "these failures predate the cell" is INFERRED from where they are, not shown.
- **The one real run:** the candidate was BUILT and `/ticket-center` LOOKED AT (the screenshot script, stubbed sign-in, five
  SYNTHETIC rows): the four rows with a created time each show its age beside it, legible on the board; the row with no created
  time shows the cell's dash alone, no brackets, no zero. My first screenshot showed the page's crash screen: my fixture answered a
  second endpoint with the list's body. Narrowed to the list call, the page rendered. Not looked at: the In Progress and Completed
  tabs (covered by the fifth test only), and a real ticket.

## 3. For L9 -- one judgment

`AR121-y-AC3`: a person reading the queue list learns how long each open ticket has waited without subtracting, and nothing else
about the list reads differently. Artifacts: the diff of the branch against DEV; the helper's words above. Things a reviewer may
weigh: the age sits in brackets after the created time rather than in a column of its own; it is computed once per render.

## 4. State of the rest of the workstream (unchanged this round)

Release 5's return: pair signed on both halves; precondition FALSE (MEASURED 19:51Z: the history reader is not on portal PROD
`37aa1247ee`); the narrow PROD push that carries it waits on Andrew (CTO msg 5603). The fallback's removal is re-cut after that
release's after-reads (row `IRPT_ANLREQ-D2-S60`). Row `IRPT_ANLREQ-D2-W53-S2` stays open on IRPT_BCKEND.
