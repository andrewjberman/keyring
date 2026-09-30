# 2.0.0_SA_COO~M drive log -- 2026-09-30 15Z-16Z (IRPT_BCKEND ~M + MDPF_SECCLASS; host derived: laptop)

- 15:0xZ tick 2 | CTO signed both ONE-WINDOW halves @b4cd4a46ba (seven conditions each; IRPT legs before BD legs; H4 3 of 3
  Success before B1 copies a byte). Ledger secclass-bd-thread-r2-and-irpt-narrowed-m-20260930 OPENED (9 legs, 24 h).
- 15:1xZ H1 plan (init -reconfigure) 0 add / 3 change / 0 destroy: aws_iam_role_policy.irpt_holdings x3. H2 safe-apply
  15:13:15Z (HALT_ACK=1; naming plan gate WARN 29) 0/3/0; re-plan 0; read-back Sid CanonicalClassifierLookup
  (Query+GetItem on the table + two GSIs) on irpt-49f/inf/cot-holdings-role.
- 15:18Z-15:33Z H3 mints: 49f 17ad3ea043 (members-sha256 6db48725..., 44 members); inf/cot FAILED 15:20-15:22Z on a
  transient SyntaxError in lib/opal_naming.py (a peer's mid-edit, HEAD compiled again by 15:3xZ); re-run inf 743d611217
  (3cf01e2f...), cot 24fdc82554 (2c95e1aa...). Closure diff EMPTY across the three HEADs.
- 15:2xZ-15:3xZ mail: ~Y STUCK (staged sentinels; mine committed @3042725dba, MSTR also landed it @24fdc82554 under the
  audited override), ~T restamp notice (12 generated naming targets move at TR-g-1's drain), CRO IRPT_TAX_MEMBER columns
  7 -> 9. Note: deploy_ledger.py stages on every open/close-leg; commit follows each ledger act from now on.
- 15:41:57Z H4 QA fire DISPATCHED (156a0153 / d3a9537b / edbf7720); Success/0 x3 by 15:47:44Z. Reader
  R29_CHECKS/r29_qa_after_read.py (node_kind + display.symbol): holdings_qa vs served holdings -- unclassified 65/4/179
  identical (to_unclassified 0); PHYS/GLD alternatives/Gold -> commodities/Metals, VXX alternatives/Volatility ->
  structured/Hedge, basis TABLE; served manifests (.e0bQWBR.. / 2lvMn_5S.. / yPNnC6xy.., 14:16-14:23Z) unchanged by the
  QA fire. H4 CLOSED. NOTE: the morning scheduled publication landed 14:16-14:23Z from the OLD bundles; H5 = the next.
- 15:4xZ-16:0xZ MDPF_SECCLASS r5 chain A: WK~9 built @8368a9a396, blocked by a base INDEX-DRIFT (NFRA_TRNSPT) -> issuer
  cherry-picked 17ad3ea043 (b622e6a245), fresh continuation committed @661f1e74d9 (W9-S3 DISMISSED_WITH_REASON: the
  schema has no RESOLVED value); drained @716f6f883a; issuer re-run 4 passed / CUSIP-GUARD 0 / HALF-READY / VALID;
  worktree 9 removed. COO half on CUSIP_ROWS signed @5cc84b40f6 (two of three reader guards NOT built, stated); CTO
  half SIGNED @1f4792c45a (6 conditions; round 6 carries the two guards). r5 chain-A packet @1fb1c96bf6 after the CTO
  fixed IRPT_DASHBD's index drift @e8d1c25288.
- 16:29Z B1: five BD files DEPLOYED + VERIFY OK (gold lib/etf_classifier.py, D_03, D_04, C_06; silver
  build_bd_assets_dim.py) from b6cfb3316e. B2 CLOSED (live IAM read: bd-securities-access grants GetItem; 0 inline added).
  Prior served VersionIds recorded: firm_composition AUXYImvT.. (05:16Z), mix_daily_summary oIyAV02C.., z08327149
  summary RMmQy.i3.., firm mix_summary 4iHMfpRA.., bd_assets_dim gY8SA9ru.. (09-29 22:11Z).
- 16:36:55Z B3 exercise: bd-gold-trigger {mode incremental} -> runner i-01003b035d2988dfb started (was stopped); the
  23:00Z bd-gold-nightly-fallback fire is the acceptance. Served-key VersionId watch armed (background).
- 16:41Z-16:46Z CUSIP_ROWS act (ledger secclass-cusip-rows-m-20260930): G1 guard 0/0 at 16:41 and again at 16:44:40Z;
  P1 PRE-READ present=0 of 349; W1 written=348 refused=1 of 349, overwrites 0 -- the refusal is the census's own
  duplicate key CUSIP:786514AS8 (Safeway 7.45% 2027, held by 49financial and cottonwood; 349 rows = 348 unique keys);
  R1 read-back equal=348 missing=0 differ=1 (the duplicate's High Yield sub-class vs the landed row's absent one, a
  seed-path correction never this act's overwrite). CLOSED @8b03d64dcc. Act script R5_CHECKS/r5_cusip_rows_act.py
  (repo-root hop parents[6]).
- Open at 17:00Z: H5 (next scheduled Holdings fire, read on the page), B3 acceptance (23:00Z fire) + B4 (page read for
  z08327149), E18 ledger A1 (10-01 04:00Z), MODEL_ROWS halves (after the CVO's r4 compile), SC-e-12 parked (placement
  asked of the CTO), round 6 (two reader guards + W5-S2 citation) after the round-5 analysis.
- Push state: origin/CLOUD 410818259a (MSTR ls-remote 14:5xZ); local commits LOCAL.
