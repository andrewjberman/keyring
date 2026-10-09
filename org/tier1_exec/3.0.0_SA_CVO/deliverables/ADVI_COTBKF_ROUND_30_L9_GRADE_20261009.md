# ADVI_COTBKF round 30 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~09:0xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_30_DRAIN_END_20261009.md @6a163e8b24`. Row D2-S46.

| criterion | verdict | evidence |
|---|---|---|
| CB30ad1-AC2: each account's class follows from the printed per-CUSIP rows by the script's pre-written rule, and the "which level is right" statement rests on an outside value where one exists | MET | The rule was committed @3d3ddbceb5 before the first run. The only later change (@816400901c) is a one-line date-type conversion, not a rule. `scale_trace.md` prints, per sample day, each CUSIP's quantity, both closes and their ratio (808524102 3.0000, 808524839 2.0000), the split the plan applied (x3, x2 on 2024-10-11, from the rows), identical cash under both methods, and "none within 5 days" for an outside trade price. Both accounts are `untraced` by the rule. No level is asserted as measured: "r28 is right" is labelled an inference (W57-S1) |

**Note:** an outside value does exist, but outside the delivery: an as-traded close from MDPF_DEMQUE or Yahoo. This read-only cell did not
fetch it. The packet proposes it for round 31, and D2-S45 stays open until it is read.
