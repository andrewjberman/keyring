# ADVI_COTBKF round 23 -- L9 grade of CB23w1-AC3

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~22:0xZ. **Order:** `ADVI_COTBKF.TO-CB-w-1` (chain drained @e0326895c4).
**Criterion (verbatim, unamended):** "the 23 are classed with evidence rows and sum to 23; the rule is one general condition; round 22's
25 recovered movers are still MATCH and the non-sweep control is unchanged."

## Verdict: NOT MET (one clause of four)

| clause | result | evidence |
|---|---|---|
| 23 classed with evidence rows, sum 23 | MET | `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/sweep_regrade.md` lines 1210-1282: vendor_cfncash_leg_of_sweep_sale 13, unvalued_funding_sale 9, credit_kept_by_every_condition 1; each row lists its credit days and the reason each was dropped |
| one general condition | MET | the rule names no account; a comp-find of the three named accounts over `data/assets/scripts/silver` hits one comment (`commonwealth_sweeps.py:35`) and no condition |
| round 22's 25 still MATCH | **NOT MET** | AMENDMENT 3 section: MATCH 0, DIFF 25 |
| non-sweep control unchanged | MET | control_same=True, 642 of 642 |

AMENDMENT 3 (CTO msg 1618) accepted one named regression and moved AC2's expectation. It did not amend AC3. The packet's "recorded as the
CTO ruled" describes the issuer's record, not a change to this clause, so the clause is graded as written. The issuer's diagnosis points
at the cure: the carried cash level, which round 24 takes up. The closing read is that re-grade with the 25 named.
