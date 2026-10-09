# ADVI_COTBKF round 37 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~13:4xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_37_DRAIN_END_20261009.md @7bc7b1fc1e (msg 3373)`. Rows D2-S61, D2-S62.

| criterion | verdict | evidence |
|---|---|---|
| CB37ak1-AC2: each class follows from the printed rows by the rule committed first, and no other firm's source is counted | MET | The rule was committed alone at b4764d4fa0 (09:22 ET), where `main()` raises "not yet implemented: rule-only commit". The output followed at 3c00ecf3c3 (09:30). Each class follows by the rule's precedence: 95000U2D4 is `trade_only` on one 2022-06-08 buy, and the other two are `none`. The one post-run change added the vendor buy code `by`, which the rule's "buy/sell transaction rows" already covers (W65-S1). No other firm's source is counted |

**Note:** the excluded `bd_snapshot` rows may be Cottonwood's own Black Diamond platform data, not the bd firm's (D2-S62). They post-date the
held window, so no class changes either way.
