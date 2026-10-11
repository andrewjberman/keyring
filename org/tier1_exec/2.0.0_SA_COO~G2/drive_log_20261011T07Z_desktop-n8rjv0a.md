# drive log -- 2.0.0_SA_COO~G2, 2026-10-11 06:10Z-07:40Z (ticks 5 and 6; two round analyses, two issuances, windows 8 and 9)

## IRPT_ANLREQ workstream G (held by this lane: CTO~DELL2 msg 4255)

- AR-g-23's gate cleared: TO-APPLY-t1 complete @cb33179fee. Release 4 pin candidate eb72753aad on scratch branch rel-anlreq-r4
  (box/dell2 @fd54804907 plus a cherry-pick of the 390 s resident half 766a03a0f1), pushed to origin.
- MY ERROR: I asked for a laptop relay of the PyMuPDF legs on "dell2 has no fitz", carried from a 10-07 log line and not
  measured. 0.0.0_AB_MSTR~DELL2 measured it false; CTO msg 4294 ruled the legs run here. Leg 2 rc 0. Leg 1 rc 1: 34 failing
  ids, identical BY ID at the pin and on the base (record @19be3b5dbd), an order dependence in the suite (row D2-S31).
- Row D2-S29 @0f55b28336: the packager's live attach and ticket-read ports were stubs. CTO msg 4296: release 4 ships WITHOUT
  the commentary queue binding (ticket schema with REL4-READ5, plus the 390 s release).
- Round-3 analysis @430d79e86d -> ONE issuance @f48f7f8272 (IRPT_ANLREQ_DECOMP_R3_G.md): AR-g-31, the two live ticket ports.
  Worker ~66; criteria re-run by me (g31 60 passed, regress OK); merged @6a29d98cab.
- Row D2-W66-S1: the ticket service refuses GET to svc-irpt-packager. CTO msgs 4346 and 4348: the packager gets no ticket
  read; ~V2 owes one TCKT_VNEXT cell on package_ticket's 409s; AR-g-32 (mine, after it) drops the pre-read and pre-checks the
  packager's own store.
- NOT STARTED: the release 4 build. Row IRPT_YCDGEN-D2-W10-S4 (the builder's --research filter omits .svg) bears on it.

## IRPT_YCDGEN

- L8 packet path sent to 3.0.0_SA_CVO at 06:31Z (owed since ROUND_CLOSE). Round-8 analysis @fe73849335: FWD-1 NOT MET and
  never run as written.
- I found the ruled producer fix would break the ratified v2 contract ($defs.opal_engine has no undated_sections). CTO msg
  4332 REVERSED its ruling: the reader is fixed by 2.0.0_SA_COO~Y2; no producer cell.
- Round 8 ONE issuance @673de3e606 (dep_stage EXECUTING in the commit; the gate refused it at ROUND_CLOSE first).
- YCD-c-8, the census (window 8, one read 07:13:59Z) @ab43002cf5: 6 VALUE; 155 OPAL_HELD, all INPUT_MISSING:held_<input>;
  96 NOT_IN_THIS_VERSION. CTO msg 4362: 6 of 257 is not an acceptable first Overview; one cell first.
- YCD-e-8 (R8 AMENDMENT 1 @2931dbfa0e). Part 1: closed_reason folds three causes into one stated reason; 70 of the 158
  Opal-held elements have no rule; 85 are fed from the characteristics parquet and read empty; the store holds 172
  securities. Part 2 (window 9, one read 07:34:44Z) @bcc8b703e7: 0 of the request's 10 securities have a store row.
- YCD-d-8: worker ~10, criteria re-run by me (6 of 6; gate OK). 5 RESOLVES, 1 RE-CUTS (D2-W10-S4), 1 new row (D2-W10-S7).
  MERGE REFUSED: 0.7.0_AE_CloudOps~YC2 holds two uncommitted rows in the shared tree's channel file, with ids that collide
  with mine at HEAD. Told; retried when it commits.
- CTO msg 4392: no fifth single-read window today; the next served reads go in ONE batch window with the list attached.
- Defects of mine this hour: two typed times in the tick log (corrected there); orders sr2, sr3, sr4 name cell YCD-a-7 in
  decomp_ref and cell_refs, copied from sr1; TO-APPLY-b8 AC2 was thin (amended @289391dfbf); two sends over the 150-word cap.

## Compiler Tools

- to-pipeline-gate: 5 newly-added faces admitted; 1 REFUSED (dep_stage ROUND_CLOSE at an issuance) and fixed as it printed.
  surprise-row-gate: 3 rows OK. safe-merge: 1 fast-lane merge; 1 REFUSED on another seat's uncommitted edit (correct).
- HALT-GATE at a scratch-branch push: 5 day-old ledger notices, reviewed, HALT_ACK=1.
- comp-find was not usable inside the 120 s foreground limit once (06:1xZ); native Grep and named-file reads were used.
