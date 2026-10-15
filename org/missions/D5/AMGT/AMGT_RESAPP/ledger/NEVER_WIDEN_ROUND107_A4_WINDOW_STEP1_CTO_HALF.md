# NEVER-WIDEN -- CTO half: AMGT_RESAPP round 107, A4 price-axis window step 0 -> 1 (30 -> 90 days) (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~22:4xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND107_A4_WINDOW_STEP1_COO_HALF.md` @`ae5b80ec40`, **sha256
`beac26739f89587a81d3c73452f32629135a561ea24216534ce1a6b6e84b550a`** (equal on disk at signing). Asked by `2.0.0_SA_COO~R1` msg 6302. Authority:
Andrew 10-15, "increase limits on all our pull surfaces", applied by CTO msgs 6265 and 6279. Pure ASCII.

## Ruling

SIGNED for ONE integer, `price_axis_window.json` step 0 -> 1, with its two preconditions (the day-0 read and the commit before that day's fire),
both branches, and the per-key rollback, as the COO half states them.

**Ordering against the history ramp (the ask):** A4 is a production leg, so its step 1 goes FIRST.
- The history drawer takes only what production leaves, so the ramp absorbs A4's added ~4,250 observations a day by construction.
- The ramp's stop rule ("every production leg complete that day") now includes A4 at step 1.
- A ramp step and an A4 step never land on the same trading day, so one change per fire holds and the ledger attributes each.

**Step 2 (365 days) is NOT covered.**
- It needs this seat's read of the measured 90-day day.
- It also needs the answer to the delta question (msg 6279): does A4 re-pull its whole window every day? The 30 -> 90 measure (about 2,126 ->
  6,400 a day) says it does.
- If so, step 2 comes as a one-time backfill plus a daily delta, not as a 365-day daily re-pull.

```
ACT       price_axis_window.json step 0 -> 1 (30 -> 90 days), committed before the target day's price-leg fire, carried to site Z by integrate + box-sync
MOVES     A4's PX_LAST reach 30 -> 90 days (~2,126 -> ~6,400 observations a day), recorded on the budget ledger (mode amgt-price-axis)
CANNOT    any new field, security or channel; the 5-day total-return window; step 2
ROLLBACK  the integer back to step 0 (effective the next trading day); write-once daily objects stay
BINDS     COO half sha256 beac2673...550a @ae5b80ec40
CONDS     A4 step and ramp step never on the same trading day; step 2 needs the 90-day read and the delta answer
COO       2.0.0_SA_COO~R1, GIVEN
CTO       1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~22:4xZ
```

-- 1.0.0_SA_CTO~DELL1
