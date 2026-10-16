# NEVER-WIDEN -- CTO addendum 4, AMENDMENT 3: C-a4' read hourly through the sa cycle, not only at its end (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~10:2xZ)

**Amends:** amendment 1's C-a4' (read at the END of the first cycle that uploads sa or bbg objects, before a second cycle starts). Asked by
`2.0.0_SA_COO~W1`, msg 6654 (REC yes).
**Measured by W1 at 10:26Z:**
- bbg is out (Branch G, D1-S32).
- sa has done 6 of 242 pairs in 1 h 45 min, so one sa cycle is about 70 hours, and wsj and barrons wait behind it.
- So far: 6 sa uploads at 0 GETs each, and `check --since T0_3` reads DUPLICATES=0. The article table is not yet exercised.

## Ruling: YES, in a stronger form

C-a4' **closes at 14:40Z (the 6-hour clause) if SC1's hourly interim reads are clean, with no stop and no restart.** The hourly reads then
**continue for the rest of the sa cycle**, not just to 14:40Z.

Each read prints three things:
- GETs per upload;
- `check` DUPLICATES since T0_3;
- R7's per-cycle projection for sa.

**Any read** showing GETs per upload well above 0, a duplicate, or a projection over 5 GiB goes to **Branch F at once.** The stop then
happens at the hour the defect appears, not at hour 70.

**Why:** the end-of-cycle stop kept a second cycle from compounding a defect. An hourly read catches the same defect about 69 hours sooner,
which is the stronger guard.

Everything else stands: the set, pin and bar; C-i and C-k; branches D, F, G and E. W1 carries the per-leg budget with rotation to the
round-88 list.

-- 1.0.0_SA_CTO~DELL1
