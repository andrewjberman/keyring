# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 03Z-04Z -- ETFS_RIVALS (lease FULL)

| time | limb | round | TOs | act |
|---|---|---|---|---|
| ~03:2xZ | L6 | 14 | 0/2 | ONE issuance @7667270270: RIV-ab-1 (Z-S54 A + C, Andrew-direct @3e040ecbf2), RIV-as-1 (audit size rule, ruling 4). fanout 1 of 1 chains. 3 checks FAIL at base as designed, controls PASS. The gate's first run was exempted by a peer's open merge; re-run graded both orders rc=0. |
| 03:36Z | L7 | 14 | 0/2 | worker ~1 executing ab-1; tick NO-OP. |
| ~03:5xZ | L7 | 14 | 2/2 | ab-1 then as-1 reported; issuer re-run 3 of 3 PASS, proofs VALID, suite 795 passed; orders flipped on the branch; drained @22844f744f; worktree removed. |
| ~04:0xZ | close | 14 | 2/2 | real run on 2026-10-06: 24 PASS badges all "earlier", index 1,279,784 B, audit unchanged. COO half @c80640b1d4; CTO half @2420f346aa. |
| ~04:2xZ | close | 14 | 2/2 | deploy: ledger etfs-rivalfunds-r14 opened @fe1b3fbb78, apply 0/5/0, 5 of 5 hashes, one republish rv-publish-1006r14, served equals prediction, ledger CLOSED 4/4 @cc02eeac7d. Sent to CVO~RV and CTO~Z (30569, 30570). |

Open: J1 of ab-1 and CTO condition 4 wait on the 13:00Z sweep; row Z-W1-S49 (a refresh that uses up the invocation) is unexercised; ledger etfs-rivalfunds-pk1-al1 stays OPEN for the 11:00Z vehicle run and the morning pass. Rows Z-W1-S49 and Z-W1-S50 are INERT observations owned by this seat.
