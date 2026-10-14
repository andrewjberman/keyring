# IRPT_DASHBD round 106 -- L9 grade of DB106-2-J1

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~15:0xZ. **Asked by:** msg 7696. Packet:
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND106_B_DRAIN_END_20261014.md`, blob 11c4a27f31
(@b46887a9a7).
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-207.*.md:39`): a re-grade of round 105's J1.
- No note or chart note claims a reason for a figure the report prints.
- No note contradicts the table under it.
- No template slot name or dangling asterisk prints.
- The dash means only "not held".
- The holdings table stays in the baseline's orientation.

**Read by this seat:** all 14 pages of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r106/pages/r106_1/`, as images.
DB106-1-AC1 and DB106-2-AC1 re-run on HEAD: 2 of 2 PASS. No client figure is copied here.

**Result: FAIL on two single lines. Both fixes are one line each. Everything round 105 failed is fixed.**

## Fixed since round 105 (met)

- **P.6 Holdings Overview.** The household row now prints Net Gain for Last 12 Months, Year To Date, Quarter To Date and since
  2024-07-08. These are p.4's figures. The note above names only the absent figures: the household's returns and the month-to-date
  columns.
- **Chart notes no longer claim "needs more history".**
  - P.2: "Chart not drawn in this report; the values are in the table on page 6". P.6 prints the class allocation.
  - P.5: the allocation-by-account note points to page 5, which prints each account's ending value.
- **The split columns state their true reason.** "Opal does not split net additions into contributions, withdrawals and income yet."
  prints once for the household and once per account.
- **The dash means only "not held".** It prints in the three unheld class cells and nowhere else on the 14 pages.
- **Orientation is met.** No slot name and no asterisk prints. Every account note names its account (pp.8, 10, 11-13).

## NOT MET

1. **P.5, the chart note "Ending value and net additions, last 12 months (household)" says "the values are in the tables on pages 5
   and 8".**
   - Page 8 is account 9269's overview. It is not the household's.
   - The household's last-12-month net additions print on p.4 and nowhere on p.5 or p.8.

   The note sends a client to the wrong page for the household's figures. Also, a 12-month line chart's values are a series, and no
   table prints the series. The truer words are "Chart not drawn in this report; the period totals are in the table on page 4".
2. **P.6, the foot note "Ending value, net gain and return for each asset class, and the household allocation: not available yet."**
   - It sits under a table whose Allocation column prints the household's split across classes: four shares, and the dash for three
     unheld classes.
   - The issuer flagged this as reading (1). It is a count under the criterion's "no note contradicts the table under it".
   - The class half of the sentence is true. The "household allocation" half is either dropped, or the household row prints 100%.

## Readings (not counts)

- **Wrapping.** "Not available yet" wraps over two or three lines in p.6's narrow columns (the issuer's reading 2). This is cosmetic.
- **Repetition.** P.5's split-column sentence prints four times, word for word. It is accurate; a single household-level line would
  read better.
- **Account chart notes.** On pp.8-10, "Account allocation chart: not available yet." and "Account performance chart, last 12 months:
  not available yet." claim no reason and contradict nothing. They are accepted.

## Remedy

Two one-line wording fixes in the render cell: the p.5 chart pointer, and the "household allocation" clause on p.6. This seat re-reads
p.5 and p.6 only, unless the fix moves other pages.

-- 3.0.0_SA_CVO~DELL2
