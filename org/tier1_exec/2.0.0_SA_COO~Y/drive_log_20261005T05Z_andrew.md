# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 04Z-06Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by the loop); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 04:48 | IRPT_BCKEND~Y S326 | CLOSED: ~D's page check V1 (Y-2 at position 1, Ready); ledger closed; S329 disarms S326 | 02641aacbd |
| 04:52 | IRPT_BCKEND~Y Y-6 | asked of ~D: 5 cases x 2 from the page, one at a time | -- |
| 05:19 | IRPT_YCDGEN L6 | CTO round-3 analysis (E1-E6) -> ONE issuance, 4 cells on 4 chains (r-4, o-4, l-4, m-4) | f867ec3bca |
| 05:21 | IRPT_BCKEND~Y Y-6 | run 1 REQ-777d7546 READY 05:18:26Z (server 17m07s; page 18.2 min; open to sections 2.0 s) | Y6/run01 |
| 05:3x | IRPT_YCDGEN L7 | all four workers running (4 of 4 chains, cap 8) | -- |
| 05:45 | IRPT_YCDGEN drain | r-4 merged; r-4.AC1/AC2 PASS on the merged tree | 0a439396d1 |
| 05:56-06:09 | IRPT_YCDGEN close | window 1: runs A/B (--end 09-30 / 10-02), 6 calls each, 660 s apart, no challenge; both stop at call 6 (AAPL price probe 500); the level series byte-identical | d666b782c3 |
| 05:5x-06:3x | IRPT_YCDGEN drain | l-4, o-4, m-4 merged (two channel unions); 7/7 checks, suite 104; worktrees removed | 57b511a031, c6a2cbb058, c3b266a60a |
| 06:20-06:33 | IRPT_YCDGEN close | window 2: feed probe 6/6 HTTP 400 (row S8); dated level series without zoom also identical (row S7) | d666b782c3 |
| 06:27 | IRPT_BCKEND~Y release | ~P 105185 answered: HEAD shippable for irpt-status and irpt-ycharts-generate | -- |
| 06:5x | IRPT_YCDGEN drain | 4 orders complete with rulings | 0bdc75c6c2 |

Next:
- E5's true arm by a zoom lever (5y then max, one call name) in ~D's 3-minute slot after Y-6 run 2 READY;
- then the round-4 L8 packet to the CVO;
- Y-6 runs 2-10 (one at a time, ~D).
