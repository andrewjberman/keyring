# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 08Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by presence); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 08:1x | IRPT_BCKEND~Y Y-6 | run 3's page miss traced: server-side REQ-724a493e is position 0 of 33 firm rows; irpt-status not redeployed, no error -> page-side (to ~D) | -- |
| 08:1x | IRPT_BCKEND~Y Y-6 | backend states for runs 1-3; the join's journal limb by window; 900 s release = 15m07s of each job | 0d980ceca5 |
| 08:2x | IRPT_BCKEND~Y | drive log 07Z + STATUS~Y (release finding on the next-list) | e72373dd77 |
| 08:41 | IRPT_BCKEND~Y Y-6 | run 4 REQ-1352d8c1 READY 08:41:43Z (18m07s) | Y6/run04 |
| 08:4x | IRPT_BCKEND~Y | firewall-window probe staged for after Y-6 (12 public-ticker reads, 2 windows of 6, W=330 s, own index key) | 08fc07bd3f |
| 08:56 | IRPT_BCKEND~Y Y-6 | ~D: the miss is a slow page load (list skeleton 30 s after reload); answered with Lambda latencies (irpt-status max 7.1 s, directory 0.5 s) -> page-side or transit | -- |
| 08:59 | IRPT_YCDGEN L9 | NO-OP: the CVO's (packet READ 07:15:38Z) | -- |

Next:
- Y-6 runs 5-10 (~D, after its driver fix), with backend states per run;
- the firewall-window probe after Y-6's last run;
- IRPT_YCDGEN: the CVO's L9 and slug, then the CTO's round-4 analysis, then ONE issuance.
