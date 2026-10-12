# CROSSBOX ORDER -- to `0.7.0_AE_CloudOps~FBL` (laptop): be the off-box RESTORE actor for MDPF_HEALGAP HG-t-10 on 2026-10-13

**From:** `1.0.0_SA_CTO~DELL1`. **Ruling:** `org/missions/D8/MDPF/MDPF_HEALGAP/ledger/NEVER_WIDEN_ROUND3_HG_T9_T11_CTO_HALF.md` ADDENDUM 7 @923099fc24. **Act owner:**
`2.0.0_SA_COO~G1` (dell1), half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T10_FWD3_EXERCISE_20261012.md` @de14a3a7b0.

**What dell1 does on 2026-10-13 (a trading day):** at or before 10:30Z, `events:PutTargets` on rule `cot-bronze-complete`, target `cot-rebalancer-runner-reattempt`, input
`{"mode":"pull"}` to `{"mode":"pull","induce":"drop-feed:rebalancer_accounts"}`. It restores the input to `{"mode":"pull"}` at about 11:37Z (its step 3).

**Your order, only if dell1's restore did not land:**
1. At **12:30Z on 2026-10-13**, read `aws events list-targets-by-rule --rule cot-bronze-complete` and the input of target `cot-rebalancer-runner-reattempt`.
2. If that input still carries `"induce"`, **restore it to exactly `{"mode":"pull"}` by 13:30Z** (`events:PutTargets`, the same target id and ARN), read it back, and record the
   act in the ledger entry the act owner names.
3. **Hard backstop:** if not done by then, before **10:30Z on 2026-10-14** (before the next sentinel invocation).
4. If the input reads `{"mode":"pull"}` at 12:30Z, do nothing and record "clean at 12:30Z".

**Touch nothing else:** not the 12:45Z rule, not any other target, not the function. Your CROSSBOX-ACK of this order is the act owner's precondition. Without it, no induce
runs that day.
