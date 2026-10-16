# FWD-9 served reads, round 6 (2.0.0_SA_COO~H1) -- appended one entry per run

Instruments: `R5_CHECKS/r5_fwd9_read.py filled 2026-10-12` (the organic blank-then-fill pair) and `R6_CHECKS/r6_week_read.py <as_of ...>` (SALXX and FXFXX read each trading day
from the gold partition the run wrote). The DONE WHEN (CTO round-5 ADDENDUM 1): no BLANK across a week that includes a Monday. Read only; no ad-hoc run was taken.

## Entry 1 -- the 2026-10-16 13:00Z scheduled run (serves as_of 2026-10-15), read 13:07Z-13:15Z

**The organic fill (FXFXX 2026-10-12): `FWD9-FILLED-OK D=2026-10-12 E=2026-10-15 filled=FXFXX`.**
- served `data_as_of` 2026-10-15, LastModified 2026-10-16T13:01:47Z; FXFXX was null on 2026-10-12 in the bbg/2026-10-12 pull; `bbg/2026-10-15` history carries `FXFXX 0.0` on D; FXFXX served WTD is a number for PFDE and PFOE (0.0315).
- Discrimination: the same instrument read `FWD9-FILLED-BAD not-re-requested` on 2026-10-16 ~01:3xZ (the pre-flight at that tick) against the page then served (`data_as_of` 2026-10-13), so it separates the two states.

**The served-week read for as_of 2026-10-15: `WEEK-READ 1 as_of day(s): VALUE=2 CARRIED=2 BLANK=0 ABSENT=0`** (after the instrument fix below).
- FXFXX in PFDE and PFOE: VALUE, 1D 0.0105, all eight windows numbers, frontier 2026-10-15 (a reading on the day).
- SALXX in DIVZ and IDVZ: CARRIED, 1D 0.0098, all eight windows numbers, frontier 2026-10-14 (labelled).
- Arms exercised in this read: VALUE (FXFXX), CARRIED (SALXX), ABSENT (the gold partition for 2026-10-12 does not exist, read as ABSENT); BLANK not met.

**Instrument defect found and fixed in this read (mine).** `r6_week_read.py` labelled a holding CARRIED whenever `return_frontier` was set, so FXFXX (frontier equal to the as_of, a reading on the day)
printed CARRIED and the first run of the tool said `VALUE=0 CARRIED=4`. The pair's own rule says frontier = as_of when there is a reading on as_of. The classification now reads CARRIED only when the frontier
differs from the as_of; the first (wrong) print is not used as evidence. A prior read with the old classification (the SH-t-27 L2 read) used `r6_l2_read.py`, a different script, and is not affected.

## Still owed (the served week must include a Monday)

- as_of 2026-10-16 (Fri), served by the Mon 2026-10-19 13:00Z run; as_of 2026-10-19 (Mon), served by the Tue 2026-10-20 run: the DONE WHEN's Monday.
- Then the FINAL L8 packet to the CVO; the INTERIM packet @11e48d7278 carries the four graded judgment criteria.
