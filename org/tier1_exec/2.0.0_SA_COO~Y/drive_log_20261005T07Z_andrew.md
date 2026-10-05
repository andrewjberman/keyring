# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 07Z-08Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by presence); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 07:00 | IRPT_BCKEND~Y Y-6 | run 2 REQ-14fe69cf READY by 07:00:01Z (page 06:58:51Z, 17.9 min, sections 1.4 s) | Y6/run02 |
| 07:07 | IRPT_YCDGEN close | window 3 in ~D's freed slot: F zoom=5y, G zoom=max (one call name); G reads changed TRUE on the level series, false on portfolio_info (FWD-2's true arm) | 742b4665df |
| 07:13 | IRPT_YCDGEN L8 | round-4 packet to the CVO (READ 07:15:38Z) | 742b4665df |
| 07:1x | IRPT_BCKEND~Y | STATUS~Y refreshed | bd24826521 |
| 07:38 | IRPT_BCKEND~Y Y-6 | run 3 REQ-724a493e READY 07:38:14Z (18m40s); the page lost the row from 07:27Z, server-side it is position 0 of 33 (page-side, to ~D) | Y6/run03 |
| 08:0x | IRPT_BCKEND~Y Y-6 | backend_join's journal limb joins by window (0 -> 16 lines); runs 1-2 joined: 15m07s of each job is the 900 s read-back release | 0d980ceca5 |

Next:
- Y-6 runs 4-10 (~D), with backend states per run;
- after Y-6, measure the firewall window in (122, 660] s, then a packet to cut `READ_BACK_LEASE_TTL_S`;
- IRPT_YCDGEN: the CVO's L9 (m-4.AC3), the CTO's round-4 analysis, then ONE issuance.
