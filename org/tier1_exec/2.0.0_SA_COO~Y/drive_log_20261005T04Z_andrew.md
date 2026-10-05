# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 01Z-04Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by the loop); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 01:0x | IRPT_BCKEND~Y Y-2 | ~D queued Bproxy behind ~M on the walker (105066) | -- |
| 01:1x | IRPT_YCDGEN drain | r-3 merged; W1-S1 ruled (v2 only with holdings) | dd418f6555, f2f17beb9b |
| 01:3x | IRPT_YCDGEN drain | l-3's channel append collided: the merge was aborted by safe-merge; re-landed by its own slot | 1044735175 |
| 01:3x | IRPT_BCKEND~Y Y-2 | REQ-c1b53772 READY 01:37:07Z; status READY with prospect-v1 | 16c9f8964b |
| 01:4x | IRPT_YCDGEN drain | l-3, w-3, m-3 merged (channel conflicts resolved as base plus both appendices); 7/7 checks, suite 73; orders complete with rulings | 614554f60f, 37e2a053c6, 04c20019c8, d9ea6ebf36 |
| 02:0x | IRPT_YCDGEN close | attempt 1 refused before the lease (HOLDINGS_UNREADABLE); fixed: template rows' analysis_dollars | 0d4e7512b3 |
| 02:20 | IRPT_YCDGEN close | attempt 2 STOPPED at step 7 (WAF); table_data 404 for holding tickers; rows S5 (the runner's own stop row) and S6 | e0ec9c9c0f |
| 02:49 | IRPT_YCDGEN L8 | round-3 packet to the CVO (READ 02:52Z) | 22f9a0b8c0 |
| 02:5x-03:5x | IRPT_BCKEND~Y S326 | history newest first: fix, live read-only proof, build, census, smoke, packet; CTO half batch 253 | 44cc631396, 41459ca2f5 |
| 03:58 | IRPT_BCKEND~Y S284 | disarmed by S327 (the proxy proven by Y-5 and Y-2) | 52f2c50774 |
| 04:18 | IRPT_BCKEND~Y S326 | D1 applied (jhGc2J4Q.. live); route V1: REQ-c1b53772 first, 30 rows newest first; recorder | e805bb727a |

Next:
- ~D's page confirmation closes S326 V1;
- the CVO's L9 on round 3, then the CTO's round-3 analysis;
- E5 after Monday's close (~20:00Z);
- Y-6.
