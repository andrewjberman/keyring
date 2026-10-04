# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-04 21Z-23Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by the loop); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 20:5x | IRPT_BCKEND~Y S318 | cause measured offline: the template's 7 text cells outside A/B fail the XLSX proof by contract; row S321; CTO ruling asked | 07bb047d22 |
| 21:1x | IRPT_BCKEND~Y S320 | recorder for irpt-ycharts-generate; reconcile parity; CHANGELOG entry handed to ~P (committed by ~P) | 40417a1b8c |
| 21:3x | IRPT_YCDGEN L10 | CTO round-1 analysis E1-E5 read; S318 ruled (b), batch 243 | -- |
| 22:0x | IRPT_YCDGEN L5/L6 | round 2 ONE issuance: 3 cells on 3 chains (r-2, m-2, c-2), 7 checks dry-run at the base | 4182c82353 |
| 22:1x | IRPT_YCDGEN E1 | a fresh signed link to the run-3 report printed to Andrew (not stored; his open not yet confirmed) | -- |
| 22:2x | IRPT_YCDGEN L7 | three workers spawned, one worktree each | -- |
| 22:4x-23:0x | IRPT_YCDGEN drain | r-2 merged 988a62c350, c-2 merged 14254f9b70, m-2 merged 9cfc9da211; all checks re-run on the merged tree; suite 56 passed | 6c252f2efe, 5539fdb825, 36ba75f699 |
| 23:16 | IRPT_YCDGEN close | live: YCD-R2-20261004T2315Z-A (index bootstrapped) and -B: FWD-2 reads false/false; both OTHER_ENDPOINT routes answer 200 | fda2a4e8c7 |
| 23:23 | IRPT_YCDGEN L8 | round-2 drain-end packet to 3.0.0_SA_CVO (blob 196b77774e) | fda2a4e8c7 |
| 23:2x-23:5x | IRPT_BCKEND~Y S318 | fix 780c86d763 (pinned boilerplate); ledger opened; irpt-status zip built and uploaded (U1 closed); census and smoke; packet to the CTO (blob e5b5abfa45) | e29f4a47aa, 615ee9b611, 64f30ab5a3 |

Next:
- the CTO half for S318, then D1 (one targeted apply), then V1 (Y-5 reads READY with its date basis);
- the CVO's L9 on IRPT_YCDGEN round 2;
- Andrew's confirmation that he opened the report (E1);
- Y-2 (a Comparison with the easy file) and Y-6 on the session, one at a time.
