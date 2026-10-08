# ADVI_COTBKF round 21 -- L9 grade of CB21u1-AC3 (the mover cause classes)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~19:0xZ. **Order:** `ADVI_COTBKF.TO-CB-u-1` (drained @0aefdc2e8e).
**Criterion (verbatim):** "each class's traced month shows its named mechanism in the printed day values, and the rule, not the
result, decided the class."

## Verdict: MET

1. **The rule decided.** `deliverables/0.9.0_WK_ADVI_COTBKF~42/mover_causes.md` lines 5-33 print the rule before any count:
   - the constants are fixed (OFFSET_MIN_PCT 0.05, OFFSET_RATIO 0.5, sweep-trade-day threshold 0.005);
   - the classes are tried in a fixed order, first fit wins;
   - a tie goes to `other:unexplained` and is never forced;
   - the other tests are printed as flags (offsetting 0, balance-dominant 72, trade-dominant 75, overlap 0).

   The packet's two trunk runs also show the guard refusing rather than forcing. Before the arms were rebuilt, all 147 read unexplained.
2. **The traces show their mechanisms.**
   - **sweep_balance, D49141714 2019-02.** D = -4,010.86 on every day and no sweep-trade day, so s_trade 0 and s_bal -3.2159. The move
     comes from the base the after arm carries in.
   - **other:sweep_trade_day, RGY005018 2024-12.** D steps on the two flagged days (-199.98, then -188.14) and is flat after. s_trade
     0.8647 exceeds s_bal 0.0348.
   - This seat re-derived four printed returns from the printed values:
     - D49141714 02-28: after 52.73/51.04-1 = 0.033111; before 4,063.59/4,061.90-1 = 0.000416.
     - RGY005018 12-10: after 21,808.25/21,852.77-1 = -0.002037; before 22,008.23/21,852.77-1 = 0.007114.

## Finding beyond the criterion (row D2-S32)

Both traces show one mechanism, W42-S1's: the after arm's value steps down by a sweep buy and never steps back up, because the
funding sale credits no cash. The 72/75 split records WHERE that debit moves the month, not two causes. So the W42-S1 cash-leg repair
is one fix for all 147, and its re-grade is the test: both classes should collapse together.
