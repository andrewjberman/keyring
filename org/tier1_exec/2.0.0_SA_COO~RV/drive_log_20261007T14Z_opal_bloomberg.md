# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 14Z-17Z (host opal_bloomberg)

Continues `drive_log_20261007T13Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 14:0xZ-15:5xZ -- round 21 drained, round 22 cut, built, drained

`ETFS_RIVALS | L7 -> L8 (FULL) | rounds 21, 22 | thread y | DRIVE FORWARD`

- Round 21 (RIV-pl-1) merged e3ea0014bc; packet sent; CVO: pl-1 J1 MET (@37c17c640c).
- Gateway release r26 live 14:03:49Z (2.0.0_SA_COO~O msg 31038). Order of acts: the Lambda deploy is next.
- Round 22 (RIV-pm-1) issued 96792f2f46; amended before any spawn with the marker repair of row C-S64 (CTO ruling msg
  31031, amendment 6ce602bd1e, no gate limb graded the amendment). Built 1a829c5a1f; two strip display faults seen on
  the first real-run look and fixed by the issuer on the branch (ef6dbb5eee); merged c6ac7335a5. Suite 876 passed, 2
  skipped, 0 failed; 26 of 26 check files PASS at 23d65887ca. Packet @a8e3357abc.
- Andrew read the served page ~15:4xZ and saw no dialog and no period switch: that is the undeployed rounds.
- Andrew-direct ~15:1xZ by relay (msgs 31130, 31132): no download on site Z. This deploy builds no wheel and fetches
  nothing (source-only packages, an existing layer ARN, providers on disk); CTO~Z agreed (msg 31137).

## 15:5xZ-17:0xZ -- the deploy prepared; two rows; the COO half signed

`ETFS_RIVALS | L8 -> deploy prep (SERVED) | round 22 | thread y (local) | DRIVE FORWARD`

- Packet sent to 3.0.0_SA_CVO~RV and 1.0.0_SA_CTO~Z (msgs 31135, 31136). CVO slug @8ee36f16f5: pm-1 J1 MET, C-S64
  REMEDIATED. CTO~Z (msg 31137) accepted "11 equal, 2 gained" on one more read: markers against the trade schedule.
- That read (`round22/markers_vs_trade_schedule.py`): 11 of 13 funds equal outright; BASG +10 and GQGU +2 are trades
  recorded under a CUSIP or raw ticker string, each traced to its row; 43 gained markers named.
- **Row Z-S63 (BLOCKING for the deploy at 1,024 MB):** the deployed daily Lambda used 864 MB of 1,024 MB and 440 s of
  900 s today; the new stages peak at 1,552 MB on site Z. RULED by 1.0.0_SA_CTO~Z (msg 31149): memory_size 3008 for the
  five in the same apply; first-run Max Memory Used and Duration are ledger legs; Duration above 720 s blocks backfill
  day 1. Edit @beb13d39ff, committed under the audited lane override (the stack's paths are the cloud-ops lane).
- Plan at pin beb13d39ff: 0 add, 5 change, 0 destroy; memory_size, source_code_hash, last_modified only.
- **Row Z-S65:** the new page has 4 GQGU mentions (META, ASML) that open a dialog holding only a name; the served page
  has 0. The count stood in the real-run records since round 17 and this seat had not reported it.
- COO never-widen half SIGNED `round22/NEVER_WIDEN_HALF_COO_R22_DEPLOY.md` @b2ed0588f4, sent to 1.0.0_SA_CTO~Z 16:58Z.
- 2.0.0_SA_COO~Z msg 31142 (three ETFS_RIVALS files staged in the shared index): they were 3.0.0_SA_CVO~RV's and had
  landed @8ee36f16f5 by the time of the read; answered.
- Andrew-direct ~16:3xZ by relay (msg 31186, fabric roles; record on origin @df6d1ad20b): read; it changes no act here.

Blocked on: the CTO half. Then, in one sitting: ledger open, `safe-apply`, one republish of 2026-10-07 with `refresh_a1`
true, the served grade, the REPORT lines, ledger legs.
