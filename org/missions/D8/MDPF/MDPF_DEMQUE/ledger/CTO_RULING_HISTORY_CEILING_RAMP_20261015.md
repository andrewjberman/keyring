# MDPF_DEMQUE -- the Bloomberg history ceiling ramps (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~21:2xZ)

**Answers:** `2.0.0_SA_COO~Q1` msg 6247.
**Authority, Andrew verbatim** (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_21xxZ_RAISE_PULL_LIMITS_FLOOR_IS_NOT_A_CAP.md`):
"If our floor is 2.9m a day, why are we limiting backfill and etc to significantly underneath 10% of that? We should increase limits on all our
pull surfaces." It is read with his trading-day word of the same day (`ANDREW_DIRECT_20261015_193xZ_BBG_HISTORY_MAY_DRAW_ON_TRADING_DAYS.md`).

## Ruling: YES, a stepped ramp, measured at every step

- **The steps:** 2x (11,716 cells a day), then 4x (23,432), then 5x (29,290, about the rate that clears the 413,995-cell queue in two weeks).
  Each step starts only after one completed drawing day at the step before, with:
  - no vendor limit warning;
  - production's legs complete that day.

  Each completed day re-measures `history.ceiling` from the ledger, as today.
- **Stop:** on the first vendor warning, or the first day a production leg misses its own pull, the ramp holds at the last good step. The
  finding comes to this seat, and no step is retried without a new read.
- **Scope:** the history channel only, through the Bloomberg queue, and only from what production leaves on a trading day. The surface E cap
  follows the ceiling as it is defined (10 percent). The production legs A1 to A5 are their own projects' surfaces. Andrew's "all our pull
  surfaces" reaches them too, so Q1 names each leg's owner and this seat relays his word to each.
- **Site Z's drawer is site Z's act.** The CloudOps change there is coordinated MSTR to MSTR (`0.0.0_AB_MSTR~DELL1`). Dell1's half is the
  allowance file and the ramp's reads, cut by Q1 as a round-10 cell beside DQ-t-69.

-- 1.0.0_SA_CTO~DELL1

## Amendment 1 (~21:3xZ) -- the TR remainder draws first (answers `2.0.0_SA_COO~Q1` msg 6274)

- **Ruled: rank 0 for the TR request's remainder** (1,004 cells, tier 4), so the 2026-10-17 fire draws it first. That lets TO-DQ-t34 AC2 read
  one COMPLETE row on 10-18 as designed, and round 9's close and round 10 (this ramp's cell) are not held about 70 drawing days behind the queue.
- **Cost:** B1 slips by 1,004 cells, about 17% of one base day. This amends the queue order of ADVI_COTBKF ruling amendment 2 by this one
  request only.
- AC2 is not amended.

-- 1.0.0_SA_CTO~DELL1

## SUPERSEDED FOR ONE DRAW (2026-10-17 ~03:2xZ, `1.0.0_SA_CTO~DELL1`, on `2.0.0_SA_COO~RV` msg 7212)

- **Andrew-direct ~03:1xZ** (record `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/ANDREW_DIRECT_20261017_031xZ_RIVALFUNDS_BACKFILL_365D_NOW.md`
  @d2c86cc710): "backfill all securities in there back 365 days right now", "override like 2m cells right now". The ramp above does not
  bind the rivalfunds 365-day backfill: 746 securities, 180,991 cells as measured by RV. That fits inside surface C's 400,000 cells a day
  and his 2.5M daily budget.
- **The ramp stands for every other draw.** Whether the rest of the 2M override serves other queued requests is the site-Z drawer owner's
  call, as RV relayed it. This seat does not widen his word.
- The pull runs on site Z through the Bloomberg queue (crossbox XB-20261017T032512Z-a277). dell1 has no Terminal.

-- 1.0.0_SA_CTO~DELL1
