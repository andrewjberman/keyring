# IRPT_DASHBD PRD v0.17 -- L4-R review, ratified-text half (the last fallback wording)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~00:3xZ. **Delivery:** msg 8813. **PRD:**
`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @4fd78cac82. **Compared against:** v0.16 @00d3dc2c91, signed with C-GUARD owed
(`IRPT_DASHBD_PRD_v0.16_RATIFIED_TEXT_REVIEW_20261016.md`).

**Verdict: SIGN.** Only the C-METHOD and C-GUARD rows moved in this half.

- **C-GUARD.** "Falls back to price return plus income with `return_basis = HOLDINGS_INCOME_FALLBACK`" is removed. A breach of the
  tolerance MARKS the day `FLOW_UNRECONCILED` and never substitutes. `total_return_daily` keeps the flow-adjusted figure, or, where that
  cannot stand, the day is `NOT_MEASURABLE` with a stated gap. This matches ruling 17 ("C-GUARD never substitutes; the emitted value is the
  value graded", ADDENDUM v0.4).
- **C-METHOD.** Modified Dietz is the window cross-check, "a window figure, never a day state and never a substitute for a daily return".
- **Agreement.** FWD-10's ACCEPT, C-HONESTY, C-GUARD and C-METHOD now agree: no fallback state exists at day grain. This seat's sweep of
  the ENDPOINT and CONTRACTS for "fallback" finds only C-METHOD's restated window wording.

**Not graded here (outside the half).** ADDENDUM v0.16 item 4 assigns two owners. The unreported-days fields in the series contract go to
`~D2`, the sole writer. The first Cottonwood series publish goes to `~S2`, under its own never-widen pair. That is new served output, and
this seat signs or grades it when its pair is delivered.

-- 3.0.0_SA_CVO~DELL2
