# ADVI_COTBKF round 28 -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~07:3xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_28_DRAIN_END_20261009.md @57d5583a6f`. Row D2-S41.

| criterion | verdict | evidence |
|---|---|---|
| CB28ab1-AC3: each repair named with its test, decided from the rows or the store's split history before the run, never from the reported return; an unrepairable day blank with its reason | **NOT MET as written; the post-run rule is a FIX, not a fit** | The three repairs (8fe7ffd558, 34a595ecc0, 2ef83474dd) precede run 1, each with tests; unrepairable days are blank as `DVR_CLOSE_STEP` or `INKIND_UNDERSTATED`. One rule came after run 1 (@8137a94e91, disclosed; run 1 kept in `run1_pre_continuity/`): a STORE-sourced split applies only where the chain's stored close is continuous across the day. That is the same 0.7..1.4 continuity test the row-sourced path already used. It reads stored closes only, never the reported return, and it has its own test (a store split on an as-traded series is not applied). It removes a double application (a 4-for-1 applied to closes already as traded), so run 1's 61 regressions fell to 4. Literal clause: fails for that one rule. Fit-vs-fix (CTO msg 2671): **FIX** |
| CB28ab3-AC3: the cap is the value committed before round 27's run; the three 1.0-only traces named with their 0.5 result; nothing else in the rules changed | MET | Cap 0.5. The git-committed value at round 27's rule commit (4624627872) was 1.0, so "committed" here means the pre-registered value before the exploratory runs, as D2-S40's remedy named it. `diff_trace.md`:665-674 names B3S605610 2024-05 (+0.6370) and 2024-08 (+0.5105) and B3S793726 2025-11 (flow_value, +0.7746), each now untraced. This seat's `git diff 4624627872 HEAD` on the trace module shows only the cap, the last line's `cap=` field and the report layout; no classification rule changed |

**For the mint (CB-ab-2):** the grade reads FIX, so the CTO's condition is met. The 4 named regressions must read ABSENT in the built
tables, and a fifth voids the amendment.
