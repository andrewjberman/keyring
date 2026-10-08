# ADVI_COTBKF round 22 -- L9 grade of CB22v1-AC3 (one general cash-leg rule)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~19:4xZ. **Order:** `ADVI_COTBKF.TO-CB-v-1` (drained @4839b6f2d2).
**Criterion (verbatim):** "the repair is one general cash-leg rule (no account special-cased), the 72 and the 75 are counted back to
MATCH from the persisted grades, and every month still DIFF is named, not forced."

## Verdict: MET

1. **One general rule.** `commonwealth_sweeps.py` `funding_credit_rows`:
   - It applies per (account, trade date) that has a listed-sweep buy.
   - It credits CFNCASH with min(S, B). S is the day's non-sweep, non-CFNCASH sale proceeds, with a null Amount counting nothing.
     B is the day's sweep buy quantity.
   - A missing Amount column is refused.
   - No account appears in the code. A comp-find of the traced and regressed account ids over `data/assets/scripts/silver` finds one
     hit, in a crosswalk test, and none in the rule.
2. **Counted from the persisted grades.** `deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md` lines 711-1063 read the 163 from
   `mover_classes.parquet`. The BEFORE arm reproduces the unrepaired verdict on 163 of 163, and the counts back to MATCH are 25 of 72
   `sweep_balance`, 0 of 75 `sweep_trade_day` and 0 of 16 core.
3. **Named, not forced.** Lines 1064ff name 138 movers still DIFF. I counted 138 distinct account-months, which equals 163 - 25. The
   23 MATCH -> DIFF regressions are named separately (line 683).

## What the round falsified

My round-21 finding (D2-S32) read the 72/75 split as WHERE one missing credit lands, and predicted that the classes would collapse
together. They did not. The funding-sale credit returned only carried-balance months: the issuer finds no non-sweep sale on a
sweep-trade day inside any of the 147 `neither` months. The trade-day months carry a different leg, the dividend and fee rows of
W43-S1. D2-S32 stays OPEN, falsified as stated.

## Lead for the 23 regressions (row D2-S34, unmeasured)

The rule credits cash whenever a non-sweep sale and a sweep buy share a day. If the vendor already posts a cash leg for some of
those sales, the credit counts it twice. 19 of the 23 sit in two accounts (0QF879130, 0QF879352), which fits an account-pattern cause.
Check each credited day for an existing CFNCASH row before W43-S1's legs are layered on top.
