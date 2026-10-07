# ADVI_COTBKF round 8 -- L9 grade: FWD-6 and CB8h1-AC3 (the coverage page, second cut)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~11:2xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_8_DRAIN_END_20261007.md` @3d0eb94919 (msg 404); the page
`deliverables/0.9.0_WK_ADVI_COTBKF~24/COVERAGE_STATEMENT.md`; the round-7 grade `ADVI_COTBKF_ROUND_7_L9_GRADE_20261007.md` @cfd9d3c4f4.

**Grade: NOT MET, narrowly.** The page now leads with one line per kind of record, as round 7's grade asked. Every date span on those lines
matches the applied tables (re-read by this seat). One of the record kinds FWD-6 names is missing from the lead lines, so the second half
of its ACCEPT ("nobody mistakes one for another") still fails for that kind.

## What now holds

- The page opens "What the backfill covers, by kind of record. Each kind has its OWN date span; no one range covers them all." The single
  2016-2026 documents range that misled in round 7 no longer leads.
- Transactions 2013-04-03 to 2026-06-22; positions one day, 2026-06-23; statements 2025-06-30 to 2026-05-31 (twelve months); tax forms
  2025-02-09 to 2026-06-06. All four equal this seat's reads of the applied tables. The tax forms' issue dates fall in two seasons
  (2025-02..06: 485; 2026-02..06: 549), which is two tax years.
- CRM and prices are stated as NOT COVERED, each with its reason. W23-S1 is answered: 1,360 exact repeats, kept by C-SILVER.

## What does not

- **Returns are not among the lead lines.** FWD-6's ACCEPT names "thirteen years of transactions and returns". The six lead lines are
  transactions, positions, statements, tax forms, CRM and prices. Returns appear only in the storage section below (`silver /
  performance`, 2013-04-04 to 2026-06-23). A reader who stops at the by-kind list, which is what it is for, will take returns to be
  either uncovered or part of transactions.
- **Two smaller items, not by themselves a fail:**
  - The tax-form line gives a file-date span. "Two tax years (2024 and 2025)" would say what FWD-6 says.
  - FWD-6's "ten years of activity" has no line of its own. If activity is the CRM record, the CRM line should say so in a word.

## What clears it

Add one lead line: "RETURNS: monthly, yearly and since-inception returns, 2013-04-04 to 2026-06-23, for 1,519 of 1,533 accounts (14
have none in the delivery)". Optionally, name the tax years and say which line is "activity". The criterion is then re-graded on the page.

## CB4d1-AC3 -- re-grade on row S19: still NOT MET, on one prefix

Row S19 (2.0.0_SA_COO~C2, 11:15Z): the laptop ran the round-7 scanner (`commonwealth_price_store_scan.py` @d97b008a7c) on
`opal-data-cottonwood/irpt/cottonwood/` to its leaves: 725 objects, 205 prefixes, 0 candidate price stores (status LISTED; the dell2 run
of the same script reads DENIED, which the scanner never reads as empty). That clears the half of this seat's round-6 condition that
named `irpt/cottonwood/`. The other half, `mdpf/cottonwood/` (model portfolios), was not listed. Run the same scanner on that prefix from
a permitted principal; with 0 candidates there, CB4d1-AC3 is MET.

-- 3.0.0_SA_CVO
