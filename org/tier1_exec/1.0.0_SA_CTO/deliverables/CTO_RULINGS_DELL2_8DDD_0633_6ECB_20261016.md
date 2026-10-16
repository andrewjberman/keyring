# CTO rulings (dell2) -- rows 8ddd, 0633 and 6ecb (2026-10-16 ~07:0xZ)

**Seat:** `1.0.0_SA_CTO~DELL2`.

## 8ddd -- APPROVED (Opal-internal on measured bytes)

`cand/dell2/irpt-series-mirror-contract-031` @a020da0bff, asked by `2.0.0_SA_COO~C2`. Read: the diff from origin/PROD is ONE file,
`seriesContract.ts`, +5/-1, type-only. It adds `income_claim` to the optional names and types `income_claim` and `calendar_source`. The
build-bytes record @6151ed7f01 shows 88 of 88 dist files identical (chunk-set hash 8890552b43cca4fe), and a positive control moved, so the
served page does not change. Class: Opal-internal under this seat's msg-9136 rule. **APPROVED for DEV and PROD at a020da0bff.**

## 0633 -- DECLINED at this head; recut with one fix

`cand/dell2/ticket-hop-failure-read` (4 commits, 3 files), asked by `2.0.0_SA_COO~V2`. The read is right: one status call per shown
analysis ticket with no package, none on a finished request, nothing shown on a failed read, and the words only ever come from the route's
NONE action. **The defect: the page's code set holds only the five silent-hop codes.** The status route (r35L, live) answers a
GENERATOR failure with `DELIVERIES_EXHAUSTED`, `ANALYSIS_FAILED` or `ANALYSIS_REQUIRES_ATTENTION` (`ops/status.py:204`,
`ops/owned_status.py:20-22`), and it carries the words in the same NONE action. So "the generator down", the first failure FWD-4 names,
would show NOTHING on the ticket.

**Fix:** the set gains those three codes, with one test per code. Then re-register at the new head. The row is closed DECLINED, and the recut
is a new row that this seat approves (Opal-internal, the Ticket Center).

## 6ecb -- RULED: Andrew names one notice contact per client firm, with his client-opening word

`2.0.0_SA_COO~V2`'s REC is accepted. The firm registry holds only an email domain, no CRM is catalogued, and the users table holds an admin
at Cottonwood only, so no confirmed recipient exists for all three firms.
- A role mailbox would invent an address nobody confirmed. Picking a user from the table would be this seat choosing a client's contact.
  Both are refused.
- Opening the Ticket Center to clients is already Andrew's word (IRPT_ANLREQ PRD v0.6). The three names (49 Financial, Inflection,
  Cottonwood) come with that word. Until then the map stays empty (row d33f).
- `~V2` writes each firm's row in its own cell, under a pair, once he names them. This adds nothing to his list now: it is part of the
  client-opening act he already holds.

-- `1.0.0_SA_CTO~DELL2`

## ADDENDUM -- d870 (the 0633 recut) APPROVED (2026-10-16 ~07:2xZ)

`cand/dell2/ticket-hop-failure-read` @ac828834: commit `ac828834` adds `ANALYSIS_FAILED`, `ANALYSIS_REQUIRES_ATTENTION` and `DELIVERIES_EXHAUSTED`
to the page set, with tests naming each code (6 references). 3 files, as before. Opal-internal (the Ticket Center). **APPROVED for DEV at ac828834.**

## ADDENDUM -- a06e (the DEV-based re-cut of d870) APPROVED for DEV (2026-10-16 ~07:5xZ)

`cand/dell2/ticket-hop-failure-read-dev` @bdeeaa88f359: 5 commits on DEV 34a6baf8; the diff from origin/DEV is the same 3 files (+410/-9) as the approved
PROD-based head, with all 8 codes in `HOP_FAILURE_CODES`. The dev-overlap waiver of exactly 38 named commits is
`CTO_RULING_DELL2_05CE_DEV_OVERLAP_WAIVER_TICKET_HOP_FAILURE_READ_DEV_20261016.md` (@03159120cf); XA-102b RULED; row 05ce CLOSED.
**APPROVED for DEV only at bdeeaa88f359.** PROD stays with ac828834, after the overlapping features.

## ADDENDUM -- 6099 (series mirror to contract 0.3.3) APPROVED, Opal-internal on measured bytes (2026-10-16 ~11:2xZ)

`cand/dell2/irpt-series-mirror-contract-033` @831f974aa1: ONE file (`seriesContract.ts`, +10/-1) on the PROD tip, type-only (income_claim,
history_scope_claim, history_scope_basis, calendar_source). Build-bytes record `DB_C30_BUILD_BYTES_R150.md`: dist identical to origin/PROD (88/88).
Class Opal-internal under the msg-9136 rule. **APPROVED for DEV and PROD at 831f974aa1.**
