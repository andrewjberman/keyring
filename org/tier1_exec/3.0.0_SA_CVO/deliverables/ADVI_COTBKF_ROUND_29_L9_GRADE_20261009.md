# ADVI_COTBKF round 29 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~08:4xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_29_DRAIN_END_20261009.md @48715ba8d8`. Rows D2-S44, D2-S45.

| criterion | verdict | evidence |
|---|---|---|
| CB29ac2-AC2: the class of each month is decided by the script's rule from the printed rows, not from the reported return | MET | `div_dating_trace.md`: each month prints its dividend rows, each ex-date source checked (the 39-row EXDATES csv and the 32-CUSIP store listing), the candidates within the 26-day lag, bound_pp from the candidates' amounts over the r28 value, and regression_pp = r28 - r26 computed. The class follows from those; the reported return is printed for context and enters no decision. All 4 are `untraced`, each naming what was checked |

**Two findings (row D2-S45):**
1. **No contradiction of round 28.** The re-count tests continuity on the store's `close_served`, which is split-adjusted by construction.
   Round 28's rule tests the chain's own stored close, the series the repair scales. My round-28 FIX grade stands.
2. **A constant value ratio.** On B3S728504 and B3S728506, r28's day values are 2.43-2.47x r26's on every valued day. Month returns barely move
   under a constant ratio, but the served `account_day_value` carries that level. Which level is right is unmeasured; trace it before those
   values are relied on.
