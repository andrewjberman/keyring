# Drive log 2026-10-17 04Z -- 2.0.0_SA_COO~D2 (IRPT_DASHBD workstream B-49F + contract)

Claim words: MEASURED = read from a file or the live account; INFERRED = from code, not run. Counts and hashes only.

## The Cottonwood Performance read path (CTO ruling A, msg 10134), round 150: applied

| cell | order | state at 04:56Z |
|---|---|---|
| C0 read-only trace | TO-DB-b-318 | complete |
| C1 forward code | TO-DB-b-319 | landed 3eb27c60c0 |
| C2 Terraform | TO-DB-b-320 | landed 10dac78f46 (11 files, 0 deletions); p186 AC1..3 PASS |
| C3 function-map | TO-DB-b-321 | landed 67cc230180 (0 deletions); p187 AC1..3 PASS; one build-only hash for both entries (32 members) |
| C4 apply of the signed pair | TO-DB-b-323 | applied by IB2 (record 69532c748c); VERIFIED on fresh live reads, p189 AC1..3 PASS; ledger closed (5 legs proven) at cf3d6d9b7c |
| C5 real run | page owner ~C2 | told at 04:52Z; CTO msg 10262 names it; result pending |
| C6a read-only ownership measurement | TO-DB-b-324 | cut, queued behind the apply on IB2's one lane (IB2 is on the export IAM statement of IB-pr-616) |

The never-widen pair: packet sha256 07e9ab11; COO half d242bc65d8, CTO half b43bdc076f. The CTO added: the staff probe uses an OPAL_GLOBAL internal identity and the receipt names the class; the forged-forward refusal runs before the 49 Financial function changes. Both done (record).

## Corrections and defects of the issuer's own

- The packet and orders 320 and 321 say the box has no terraform binary. WRONG: `.tools/terraform.exe` v1.15.8 exists. The issuer ran `init -backend=false` and `validate` on both roots from the landed trunk: both valid, `fmt -check` clean (MEASURED). The signed bytes were not edited; the correction is in decomposition section 182 and in the order.
- Order 323 gate 0(c) counted a ledger that mentioned the read function; IB2 stopped (msg 10269); ruled and amended (5c2dd3718c): the gate counts OPEN LEGS on the surface. The other ledger's read-function legs were closed; its open leg is another resource.
- p189 required `ledger_closed` true while the order says the issuer closes it; it also counted a ledger slug's date as a leaked digit run, and a stray backspace byte had entered its scrub pattern through a shell heredoc. All three fixed; selftest red on 51 mutants.
- p186 AC2 counted the nested portal checkout; p185 AC1 had an old base: fixed (see the 03Z log).
- A message to the dell1 CTO was sent with a placeholder body to the wrong recipient; retracted by a second message at once. Nothing was asked or carried.

## The ownership map (Andrew-direct, CTO msgs 10215, 10227, 10267, 10271, 10277, 10282)

By count, in memory, nothing committed from the files: the newer and older match pairs hold the same 83 accounts (5 moved from UNMATCHED: 1 HIGH, 2 MEDIUM, 2 LOW); the 118-pair file is old-custodian to current-account continuity (11 deterministic, 107 to confirm), overlapping the 83 on 18 old accounts; the review spreadsheet's 107 answer cells are blank; the BI export (850 account rows, no advisor column) overlaps the sheet, the old and the current accounts by 0 exact. CTO ruling: grants on HIGH matches that join a published key directly or through the 11 deterministic pairs; nothing via the 107 unconfirmed; the count (a direct, b via deterministic, c left out) goes to Andrew with the blank review sheet as the unlock. Order 324 and checker p190 carry it (37 mutants).

## Waiting on

Page owner ~C2 (C5); IB2 (TO-DB-b-324 after its current work); Andrew's smoke of the Performance tab (row dell2-20261017T003553Z-f1bb, HELD, no change to that branch).

Push state: LOCAL (box/dell2 is MSTR's to push).
