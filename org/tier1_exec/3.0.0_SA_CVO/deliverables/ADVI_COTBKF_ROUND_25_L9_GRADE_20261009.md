# ADVI_COTBKF round 25 -- L9 grades of CB25y1-AC3 and CB25y2-AC3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~01:5xZ. Chain drained @052a80dd0f.

## CB25y1-AC3 (unlisted types): MET

Criterion: "every treatment cites a source decided before the run; each of the 35 is MATCH or carries a traced cause; no treatment was
chosen by its effect on the grade."
- **Sources.** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/unlisted/sweep_regrade.md` lines 1176-1190 give each type's source: DESCRIPTION (the delivered description), PAIRING
  (how the rows sit in the delivery) or CRO (the method research). `ftax`/`stax` are flows only where they ride a same-day `lo`, a
  structural pairing (4,056 of 4,198; 107 of 112), not a per-month choice. ASF is the one type with NO SOURCE, and the table says so.
- **Decided before the run.** The table is in commit 679c3c22b5 (2026-10-08 20:41 ET). The run's output and proof came after it
  (499405a2fe, 20:52 ET).
- **The 35.** Lines 1192-1235: 35 of 35 MATCH. ASF appears in 0 of them.

## CB25y2-AC3 (carried levels): MET

Criterion: "each of the 39 is traced to a first wrong month with its posting and cause, or named untraced with what was checked; any fix
is one general rule, not fitted to the grade."
- `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/levels/sweep_regrade.md` lines 1255-1313: 39 rows, 39 distinct account-months, 0 blank trace cells. Each names the first month the
  ledgers differ, the differing step (day and amount), and the step by row type.
- The cause is uniform: the method's level is supported by the account's own rows (closure 0.00), and the old baseline departs. Its
  departures are `ManAltF` payments for another account (14) and postings the baseline never made (25).
- No fix was applied (`method_r25b` = `method_r25`), so nothing was fitted.

## Round 24's open rows, now closed

- D2-S36 (the dividend clause I could not grade): 22 of 22 are now graded pay vs ex, with the swing printed (+2/-6), and pay date stays.
- D2-W46-S2: the ex-date source was delivered by dell1.
- D2-W46-S3: the unlisted types are each sourced, 35 of 35 MATCH.
