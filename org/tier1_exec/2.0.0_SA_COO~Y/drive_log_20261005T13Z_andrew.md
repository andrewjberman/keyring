# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 12:4xZ-14:1xZ (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by presence); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 12:54-13:01 | IRPT_BCKEND~Y | firewall-window probe in site Z's hold (~D told): 12/12 200, a 7th 373 s after the first answered; window in (122, 373] s | bb1b59c3f6 |
| 13:11 | IRPT_BCKEND~Y | [DECISION] to the CTO: release at 390 s -> batch 262 YES (after-read: the first two live jobs, no challenge; revert on challenge) | msg 105274 |
| 13:2x-13:4x | IRPT_BCKEND~Y | the 390 s ReadBackPending release built and tested on y-release-390 (generate 403 passed, 30 skipped; offline suite 0); deploys after Y-6 | f1e101d19c |
| 13:43 | fabric | ~D's two staged paths held the shared index >20 min; [ASK] ~D; cleared 13:55Z | msg 105277 |
| 13:5x | IRPT_YCDGEN drain | w-5 merged; all 12 round-5 checks PASS on CLOUD (134 tests); w-5 closed (W2-S10 ruled); round 5 all terminal | ff51386f38 |
| 14:0x | IRPT_YCDGEN E6 | staged: bundle ycdgen-e6-bundle-fb6c0f63feb7 (8 requests, 6 + 2, 660 s), host script, e6_render_store.py; slot asked of ~D | (w-5 close commit) |

Next:
- E6 live in ~D's slot after Y-6 run 7 reads READY; render, store, link to Andrew;
- E4 leg 2 after today's close reaches YCharts;
- the round-5 packet to the CVO;
- Y-6 runs 8-10; then the 390 s release deploy (packet with the CTO's half).
