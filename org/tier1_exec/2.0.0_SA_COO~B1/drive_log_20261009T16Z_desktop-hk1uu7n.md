# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), LGIC_ENFORCE, 2026-10-09 16Z-17Z

Loop: cron 444d0b5d, every 10m. Round 20 issued @8d27dd6749.

| UTC | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| 15:4xZ | L6->L7 | 20 | 0/5 | issuance after the CTO's PRD header fabric bump @81cdaa2be3; worktrees ~1..~3; workers on EN-z-1, EN-z-4, EN-z-3 |
| 15:5xZ | L7 drain | 20 | 1/5 | EN-z-3 re-proved (PASS-R20-STOP) and merged @6440817b97; slot ~3 torn down. MSTR msg 2712 (client data, W73 evidence) acked; no order names the path |
| 16:0xZ-16:1xZ | L7 drain | 20 | 3/5 | EN-z-1 (PASS-R20-LIVE; live 2457 nodes, 16 new cards) @bd7a7bd351; EN-z-4 (PASS-R20-S9; self-test PASS; pytest 193/1) @17c2c1c34f; the scope test is red on the trunk too (row D1-S2); rows D1-S1, D1-S2 @290fd5e697. MSTR msgs 2739/2758/2796 (wider client-data scope, scoped search only) acked and carried to both running workers |
| 16:2xZ | L7 drain + close run | 20 | 4/5 | EN-z-2 (PASS-R20-COMPARE 143/117/26) @1ca0ddb4fd. Row D1-W1-S1 ARMED (121 carried cards now read) disarmed by the owner's close run @119661e0fc: CENSUS COMPLETE 3701 judged + 359 carded |
| 16:3xZ | rule | 20 | 4/5 | EN-z-5 FAIL on the issuer's arm (row D1-W2-S153: the row_id regex admitted no worker id) -> AMENDMENT 1 @6dcca1e14f; slot ~2 merged open @d7324d9449, fast-forwarded, fresh worker |
| 16:4xZ | L7 drain -> L8 | 20 | 5/5 | EN-z-5 (PASS-R20-S12) @df856a79b1; drain end @5587cd04fb; round-close-check REFUSED only on Z2R20-AC2 ungraded; L8 packet msg 2842 to `3.0.0_SA_CVO`, READ 16:42:04Z |
