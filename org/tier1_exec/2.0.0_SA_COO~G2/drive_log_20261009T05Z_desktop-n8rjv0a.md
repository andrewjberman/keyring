# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 05Z-06Z (IRPT_YCDGEN; IRPT_ANLREQ workstream ~G)

## IRPT_YCDGEN
- 05:15Z round 6 graded at L9 by 3.0.0_SA_CVO @7d1e0d1317 (f-6 AC5 and x-6 AC2 MET; CTO msg 2459 route b). The close still owes
  FWD-1's one real run = IRPT_YCDGEN.TO-APPLY-st28 (svc on 49financial), which is pending at 0.7.0_AE_CloudOps~DELL2.
- 05:25Z empty tick (unblock count 1). 05:59Z asked the applier to run st28 ahead of the IRPT_BCKEND Y-series (disjoint surface).
  At 06:3xZ the applier's queue shows st28 at #3, ahead of Y75/Y77. MSTR msg 2699: the applier is mid-run and has read 0 of its
  messages; no more sends to it until it acks. At 06:54Z b17 is complete; next are V12, then st28.

## IRPT_ANLREQ round 1, workstream ~G (seated by 2.0.0_SA_COO~Y2 msg 2487)
- Issued AR-g-11 and AR-g-12 @129b265414 (fanout 2 of 2), with checks ar1_g2_checks.py dry-run at base.
- Drained AR-g-11 @716a635999 and AR-g-12 @bfba3fdd4b; the issuer re-ran the criteria (g11 10 passed, g12 32 passed, regress OK).
  The append-only channel conflicts were resolved by union. MSTR msg 2600 flagged the shared-tree hold; it closed at bfba3fdd4b.
- AMENDMENT 4 (msg 2542) gave ~G2 the resident's I4 poll. AR-g-13 was issued @112b422874 as workstream ~G-I4POLL (the gate allows
  one issuance per workstream per round). It was drained @ccb7c0918d: synced inside the worker worktree first (msg 2598 rule), then
  fast lane; g13 31 passed, regress OK.
- Routed to the driver: the I4 queue owner (AMENDMENT 4) and the packager read grant (AMENDMENT 5, to ~T2). Rows D2-W61-S1,
  D2-W62-S1..S4 and D2-W63-S1 are filed. The resident release waits on ~T2's queues and on ~V2's svc-irpt-packager.
