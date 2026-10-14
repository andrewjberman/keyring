# IRPT_DASHBD round 105 -- L9 grade of DB105-2-J1

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~14:1xZ. **Asked by:** msg 7679. Packet:
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND105_B_DRAIN_END_20261014.md`, blob 94d5e1d21e
(@220bdbd631).
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-203.*.md:39`): a re-grade of round 104's J1.
- Every client-facing line that says a figure is unavailable or not held reads as plain words and cannot misinform. That means: no
  note claims a reason for a figure the report prints, no note contradicts the table under it, and no template slot name or dangling
  asterisk prints.
- The holdings table stays in the baseline's orientation.

**Read by this seat:** all 15 pages of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r105/pages/r105_3/`, as images.
DB105-1-AC1, DB105-2-AC1 and DB105-3-AC1 re-run on HEAD: 3 of 3 PASS. No client figure is copied here; only page numbers, row labels
and counts.

**Result: FAIL, on one remaining instance of round 104's first count, plus one instance that round 104 should have caught. Orientation
is met. Round 104's counts 2 and 3 are fixed.**

## Fixed since round 104 (met)

- **Count 1 on the Activity Summary.** On p.5-6, Beginning Value, Net Gain and Ending Value now print for the household and all three
  accounts. They reconcile: the household's last-12-month Beginning Value equals p.3, its Net Gain equals p.4, and the three accounts
  sum to the household. Only the split columns (Contributions, Withdrawals, Income) stay absent, each under its own note.
- **Count 2.** Notes name their account: p.9 "Account ending 9269, Return (Cumulative) since 2024-07-08: is not available while its
  source is being repaired." sits above the one cell it explains, and p.11 does the same for its two cells.
- **Count 3.**
  - "Inception date" and "Sub-class rows: Not split into sub-classes in this report." replace the slot names.
  - The registration-name row is gone.
  - No asterisk prints.
- **The disclosure pointer** still prints on every page, and p.15 reads "Not available yet". The CTO made this a release gate (Andrew's
  call a252), so it is held there and not graded here.
- **Orientation.** On p.7, classes are rows and the baseline's columns are in order. The three unheld classes print the dash (3 of 3).

## NOT MET

1. **P.7 Holdings Overview: a note claims a reason for figures the report prints.** The household row reads "Not available yet" for Net
   Gain in all four windows (Last 12 Months, Year To Date, Quarter To Date, since 2024-07-08). The note above it says "Household, Net Gain
   for Last 12 Months, ... and Net Gain since 2024-07-08: needs more history than is available yet."
   - P.4 prints the household's Net Gain for those four windows.
   - P.5 prints the last-12-month figure, and it equals p.4.

   This is round 104's count 1 on the holdings page. The issuer's cross-table rule checks 6 pairs and found 0 conflicts. The household
   row of the Holdings Overview against the Portfolio Value Summary is not one of the 6.
2. **P.2 and p.5: chart notes give a reason that is not the true one.**
   - P.2 says "Allocation by asset class (household): needs more history than is available yet."
   - P.5 says "Allocation by account (household): needs more history than is available yet."

   A current allocation needs only today's values, and the report prints both sets: the class allocation on p.7 (four classes with
   percentages, three with the dash) and each account's ending value on p.5. The figures exist; only the chart is not drawn. Saying it
   "needs more history" misinforms. **This seat missed the same two notes in round 104.**

## Readings (not the FAIL, for the remedy cell)

- **The split columns' reason.** On p.5-6, Contributions, Withdrawals and Income read "needs more history". Their sum, Net Additions,
  prints on p.4 and pp.9-11, so the truer words are that Opal does not split it yet. This is a reading, not a count, because no printed
  figure equals the absent one.
- **A dash with no footnote.** Row W167-S6: a window the account did not span prints the baseline's dash with no footnote, and a client
  reads a dash as "not held". I did not find such a cell on these 15 pages. It is held for the remedy cell.
- **Long notes.** The p.2 and p.7 notes are long single sentences. They read stiffly, but they are plain.

## Remedy (one render cell)

- The cross-table rule covers every printed figure that a note can name. At least: the Holdings Overview household row against the
  Portfolio Value Summary, and every allocation chart against the table that prints its values.
- An absent chart whose values print elsewhere says so ("Chart not drawn in this report; the values are in the table on page N"), or
  is dropped, and never claims "needs more history".

-- 3.0.0_SA_CVO~DELL2
