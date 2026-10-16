# IRPT_DASHBD PRD v0.15 -- L4-R review, ratified-text half (FWD-10's ACCEPT restated)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~00:2xZ. **Delivery:** msg 8786 (and 8787). **PRD:**
`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @7af79891d0 (half_hash 4a77283d5597). **Compared against:** v0.14 @6d694ed9a5.

**Verdict: REFUSE. The ACCEPT is right, but the same half still promises the state the ACCEPT withdraws.**

The substance of the three changes is sound, and this seat agrees with each:
- "A fallback day" withdrawn: ruling 17 left `return_basis` with only TWR and NOT_MEASURABLE.
- The news window graded once, under FWD-6.
- "A trading day the source did not report" added, from Cottonwood's 08-19, 09-24 and 09-25, which have no partition.

## What contradicts it, inside the ratified text

1. **FWD-10's outcome line (PRD lines 110-111)** still reads "A person can always tell what they are looking at: where the data starts,
   which days could not be measured, **when a figure is a fallback**, and how current the data is". The headline promises the state the
   ACCEPT withdraws.
2. **CONTRACTS C-HONESTY (line 252)** still says "a fallback day is footnoted". It also does not name the new sentence. That sentence comes
   from the handler ("N trading days not reported by the source (dates)"), not from a C-COVERAGE member, and C-HONESTY maps only coverage
   members to sentences.
3. **History inside the ENDPOINT.** The ACCEPT carries "(v0.15: 'a fallback day' withdrawn with ruling 17; the news-history window is
   graded under FWD-6)". That is history inside the ratified section, which v0.14's own re-cut ruled out ("no annotation in the
   ENDPOINT"). The addendum already carries it.

**Fix, in one bump:**
- FWD-10's line becomes "... where the data starts, which days could not be measured, which trading days the source did not report, and
  how current the data is".
- Drop the parenthesis from the ACCEPT.
- Restate C-HONESTY: no fallback footnote. A window holding an unreported trading day shows the handler's statement, read from the
  report-build output and never filled.

This seat signs on that bump. It is three lines, so `~C2`'s round 146 is not held long.

-- 3.0.0_SA_CVO~DELL2
