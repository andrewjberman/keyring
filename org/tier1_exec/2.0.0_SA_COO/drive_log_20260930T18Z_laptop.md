# 2.0.0_SA_COO~M drive log -- 2026-09-30 17Z-18Z (IRPT_BCKEND ~M + MDPF_SECCLASS; host derived: laptop)

- 17:0xZ-17:3xZ ticks 7-10: NO-OP beyond reads. B3 exercise run in flight on runner i-01003b035d2988dfb; served keys
  unchanged; CVO READ the r4 + r5 L8 packets at 17:00:31Z. Re-login at ~17:3xZ: registration LIVE (PID 17668), one
  watcher script row.
- 17:49:03Z the exercise run COMPLETED with exit 1 (s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-09-30_20260930_174903.log):
  C_06 crashed at import 17:47:29Z -- /tmp/gold_layer_scripts/lib/etf_classifier.py:19 `parents[5] / infra/...`
  -> IndexError: 5. D_03/D_04 never ran. Served keys changed 0 of 4.
- 18:16:09Z ROLLBACK (NEVER-2: finish or roll back): copy-object of the five BD code objects from their pre-window
  VersionIds, ETags verified: lib/etf_classifier.py 884889c0, silver/build_bd_assets_dim.py 662ef035, D_03 346e7b0f,
  D_04 a4b867d4, C_06 8b1f012c -- the bytes the 04:00Z run executed. Row MDPF_SECCLASS-S5 (BLOCKING; the gate refused
  class DEFECT, not in the enum). Ledger: B3 closed as ROLLED BACK, entry HELD (external: new CTO half; H5 stands).
  Commit df545deda5 (its subject still says DEFECT; the row reads BLOCKING). E_18: same hop class (parents[4], :54),
  0 occurrences in the cumulative gold log -- it has never run in the gold chain.
- 18:31Z ESCALATION to 1.0.0_SA_CTO (fix-forward as round 6 cell 1). 18:33Z CTO RULING 103369: rollback accepted as
  the half's own branch (half spent); round 6 cell 1 decomposed now; E_18 stays deployed, 10-01 04:00Z is the expected
  negative control, its acceptance moves to the first run after the fix-forward; IRPT legs and H5 stand.
  CTO DECISION 103371 (all laptop issuers): a cell changing a runner-deployed script's imports proves the import in
  the deployed layout.
- 18:3xZ /next-calls rendered for Andrew: one open call (may a per-firm value FILL an absent instrument_kind on an
  existing row; CTO 103218 routed it to him), five options; CloudOps relaunch excluded as answered.
- 18:4xZ E_18 ledger HELD on the fix-forward (reread-event: the round-6 cell-1 redeploy). Round 6 DECOMPOSED, NOT
  ISSUED @81244a2bf3: SC-e-13 (ship the one client in the gold code, remove the hops, measure the silver layout, new
  BD_THREAD_R3 half, deployed-layout import criterion from the deploy tool's own output) and SC-e-14 (find_by_* CUSIP
  filter + seed PRE-READ count, CUSIP_ROWS condition 5). Issuance waits on the CTO's round-5 analysis after the CVO slug.
- Carried: the BD half of bd-securities-cot-new-p1 R1 (its re-read condition is met: the served mix summary carries
  2026-09-28); the leg cannot close until the COT half's S173 re-point, so the read runs with the next substantive tick.
- Push state: origin/CLOUD 410818259a (MSTR ls-remote 14:5xZ); this seat's commits LOCAL.
