# /self-drive dell2 projects -- tick 6 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 5 (@5c93cbb6c9), plus tick 6 (11:45Z). **state: ARMED**

## Scope state (11:45Z)

All 5 are `active` / `EXECUTING`. Inbox: 0 unread. Read and acked since tick 5: 366, 378, 381, 384, 387, 390, 392, 395, 398, 399, 402,
406, 408, 416, 420, 422, 426 and 433.

## Outcomes

- **ADVI_COTBKF FWD-8 REALIZED**: 4 of 9.
- IRPT_DASHBD FWD-8: HELD on Andrew's split-pull word. Two no-vendor methods failed to discriminate (E1': 0 of 2,299; Dietz: the
  control fits 19 against 22, with 3 overlapping). UNEXPLAINED is 3,279 of 9,078.
- IRPT_CUSTDY FWD-1: NOT LIVE. Hop 5 waits on IRPT_BCKEND E-P9's release and the portal kit.

## Driver acts (dell2 LOCAL)

| act | hash |
|---|---|
| IRPT_CUSTDY round 3 L10 (SI anchor rules 1-3) | ec25e39844 |
| ADVI_COTBKF round 7 L10 | 625987b867 |
| **ADVI_COTBKF round 7 CORRECTION**: this seat read the 1,360 gap against a row that predates PRD v0.4 C-SILVER. The repeats are kept by design, and E3 is struck (`~C2` msg 390) | 20b2b40d99 |
| IRPT_DASHBD round 19 L10 (the split BD pull listed for Andrew, with expected outcomes on both branches) | b402b7b2e3 |
| IRPT_DASHBD round 20 L10 (FWD-8 held on Andrew's word; six-class landed, so account_class_daily is cut) | 58f3ed0501 |
| ADVI_COTBKF CB-d-4 CTO half AMENDMENT 1 (the update carries CT-d-2's dell2 principal; the after-read denies dell2 on the crm prefix) | b4073b7bf2 |

## Rulings by message

- 384 (`~P2`, S364, no terraform on dell2): (b), the kit carries terraform. No laptop apply. The laptop took the REC (106173).
- 399 (`~D2`): the E1 method is Modified Dietz over BD's own totals, with a midpoint control and a netAdditions-equality guard. The
  control then showed the method does not discriminate (msg 416).
- 402 (`~P2`): PrintEntry.tsx @cdda4378 LAND-WITH-NOTE, after a typecheck, lint and one test where a toolchain exists. Next round,
  `readReportKind` refuses unknown kinds.
- 406: the Cottonwood price-store scan found 0 candidates in 725 objects, a measured absence. FWD-3's next step is sizing the gap.
- 422 (`~K2`, W9-S2): SI is "since inception (first funded <date>)" where Opal holds the open date and zero holdings to funding (12
  accounts); rule 2 where the open date precedes Opal's data (2).
- 426 (laptop 106191): `holdings_snapshot.py` is dell1's worker's while SC-e-56 is open. Its release takes dell2's halves.
- 433 (`~P2`): no /closer for IRPT_BCKEND. FWD-1's block is Andrew's own PROD gate, not a missing hop.

## Self-findings (one line each)

- Round 7: this seat graded a count against a superseded row instead of the PRD it governs under. Corrected the same tick on the
  COO's citation. The guard for next time: read the PRD's CONTRACTS row before ruling a count wrong.
- A shell command left `cat > /dev/null` waiting on stdin and moved to the background. It was stopped with TaskStop; no file was
  affected.

## Acts only Andrew can do

1. The IRPT_YCDGEN F1 retry (his login): the only open leg of `irpt-ycdgen-r6-branch-b2`.
2. One IRPT_BCKEND export (his per-use vendor word).
3. Opening PROD `/investor-reporting` to an advisor, or naming an advisor test principal (a gate he set by name, 2026-09-22).
4. **NEW:** the IRPT_DASHBD split Black Diamond pull: 2,299 accounts, 2,299 calls, 4,598 ranges split at 2025-01-09, landing in a
   new `pull=` prefix (his per-use vendor word). Either branch moves FWD-8's grade.
5. Handing IRPT_CUSTDY reports to the chosen advisor (egress), when hop 5 serves.
6. Offered: confirming IRPT_YCDGEN FWD-17 to FWD-23.

## Completion test

NOT DONE: 0 of 5 complete. 5 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- Reads only (git, `opal_naming`, PRD lines). Every commit waited out MSTR's merges on `.git/MERGE_HEAD`.
