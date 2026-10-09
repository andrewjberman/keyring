# ADVI_COTBKF round 32 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~09:5xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_32_DRAIN_END_20261009.md`. Row D2-S47.

| criterion | verdict | evidence |
|---|---|---|
| CB32af1-AC2: the class follows from the printed per-day rows by the pre-written rule, and the named source is the one the chain actually reads | MET | `base_close_trace.md` prints, per sampled day, the chain price, Yahoo Close and Adj Close, and both ratios. chain/AdjClose is a constant 1.0054 (SCHB) and 1.0216 (SCHZ), so by the rule (TOL 0.5%, SHARE 80%) both are `other_source`. Source: `commonwealth_daily_valuation.py:48` imports `commonwealth_price_census`, whose `STORES[0]` is `cottonwood-silver-canonical-prices`, column `price`, same-day only. This seat read both |

**Notes (no grade change):**
1. The rule and its output landed in one commit (0af60ccd42). "Written before the first run" is the worker's statement, not an order git
   can show. The only post-run edit disclosed is a ruff rename, with the output re-run byte-identical.
2. SCHB's 1.0054 sits 0.04 points over the 0.5% tolerance, so its class turns on that constant. Either class gives the same reading (an
   earlier dividend-adjusted vintage), so no decision rides on it.
