# IRPT_DASHBD round 107 -- L9 grade of DB107-1-J1

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~15:5xZ. **Asked by:** msg 7720 (packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND107_B_DRAIN_END_20261014.md`, blob 78683c7421 @2458825ec5).
**Criterion:** a re-grade of round 106's FAIL, in three parts:
- page 5's chart pointer sends a client to the page that prints the household's period totals;
- page 6's foot note no longer contradicts the Allocation column;
- nothing else the fix moves misinforms.

**Read by this seat:** pages 2, 4, 5 and 6 of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r107/pages/final/`, as images.
- Pages 5 and 6 carry the fix.
- Page 4 is the target of the new pointer.
- Page 2 holds the only other page pointer (to page 6), and it would move if the pagination moved.

The document is still 14 pages. Re-run on HEAD: DB107-1-AC1 PASS, and the five earlier live criteria (DB105-1..3-AC1, DB106-1..2-AC1)
PASS. No client figure is copied here.

**Result: PASS.**

- **Page 5.** "Ending value and net additions, last 12 months (household)" now reads "Chart not drawn in this report; the period totals
  are in the table on page 4". Page 4 prints the household's Net Additions, Net Gain and Ending Value for all four windows. The
  allocation-by-account note still points to page 5, which prints each account's ending value.
- **The split-column line** now prints once, followed by "The same applies to each account.". This resolves the repetition reading of
  round 106.
- **Page 6.** The foot note reads "Ending value, net gain and return for each asset class: not available yet." Each class row prints
  only its allocation share or the dash, so the note matches the cells under it. The household-allocation clause is gone, and the
  household row's Allocation cell stays blank by the CTO's ruling.
- **Page 2.** "the values are in the table on page 6" still lands on the holdings table: the pagination did not move.
- **Unchanged and still met:** the dash only in the three unheld class cells; the household Net Gain filled on page 6; no slot name;
  no asterisk.

**Accepted with it (for the next render round, not this grade):**
- Row W170-S1, ruled in D2-S33: the issuer's note-level rule does not key the three per-account "...chart: not available yet."
  sentences. No account-level chart value prints anywhere, so nothing is contradicted today. The rule should key them or fail.
- The narrow holdings columns wrap "Not available yet". This is cosmetic.
- **The disclosure page** stays "Not available yet". The release gate on Andrew's call a252 holds every client render; this criterion
  does not grade it.

-- 3.0.0_SA_CVO~DELL2
