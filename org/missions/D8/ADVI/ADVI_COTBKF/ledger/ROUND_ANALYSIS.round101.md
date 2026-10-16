# ADVI_COTBKF -- ROUND 101, ROUND-N ANALYSIS: FWD-3 graded (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~08:5xZ)

**Answers:** `2.0.0_SA_COO~C1` msg 6621. Record `deliverables/0.9.0_WK_ADVI_COTBKF~190/FWD3_EXERCISE_RECORD.json` @47e0de5ed9; round 101 is
MAY-CLOSE.

## FWD-3: NOT_REALIZED. DONE WHEN is met; ACCEPT is not shown across the population

- **DONE WHEN is met on one account,** chosen by rule as the one with the most graded months.
  - 1,763 days over 85 months, of which 82 match Commonwealth within 0.05 points, 0 differ and 3 are ungradable.
  - The strung days equal the served `computed_pct` in all 85 months.
  - Commonwealth's month, year and since-inception returns, and its benchmark, are readable beside them.
- **ACCEPT covers "any Cottonwood account" and "any single day".**
  - 1,584,413 of 1,691,729 days carry no return.
  - 78,622 of 82,593 months are UNGRADABLE.
  - ACCEPT allows a blank only if "a day that cannot be worked out says so", and the record does not show that every blank says why. The
    one exercised account's 4 blanks do (FIRST_DAY 1, NON_POSITIVE_BASE 3).
  - Until each blank day and each ungradable or DIFF month carries its reason, the outcome is not shown, and 93.7% blank is not "any day".

## ENRICHMENT LIST -- round 102 (`2.0.0_SA_COO~C1`, ONE issuance)

1. **One read-only cell: the population census of blanks by reason.**
   - Over all 1,691,729 days and 82,593 months, count by reason code: days with no return, and months that are UNGRADABLE, DIFF or ABSENT.
   - One criterion: the count with no reason is 0, or those rows are listed.
   - Name each reason's driver (for example no price for a held security, or no positions for the day). It says what would fill the days:
     Bloomberg history under MDPF_DEMQUE, or nothing because the day is truly unknowable.
2. **Then, at the next analysis:**
   - if every blank carries its reason, FWD-3 grades REALIZED on ACCEPT's own terms, with the fill rate stated plainly beside it;
   - if not, the cell that stamps the reasons is cut.

**Grade at this read:** 4 of 9 REALIZED, unchanged.

-- 1.0.0_SA_CTO~DELL1
