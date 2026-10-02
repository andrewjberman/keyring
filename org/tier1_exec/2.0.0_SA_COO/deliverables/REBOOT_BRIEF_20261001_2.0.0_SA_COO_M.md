# Reboot brief -- 2.0.0_SA_COO~M -- rewritten 2026-10-02 04:0xZ at the wind-down

Wind-down order: Andrew-direct ~03:4xZ relayed by `0.0.0_AB_MSTR` msg 104030 (disk near full). Push state: everything is LOCAL;
this seat never pushes. FAST leases ENDED at the wind-down (MDPF_SECCLASS, IRPT_BCKEND~M, MDPF_HEALGAP all FULL).

## 1. Identity
- Serial `2.0.0_SA_COO~M`; base folder `org/tier1_exec/2.0.0_SA_COO/`; inbox `org/mcp/inbox/2.0.0_SA_COO/~M/`.
- Projects: IRPT_BCKEND workstream ~M (Holdings producer); MDPF_SECCLASS issuer; MDPF_HEALGAP cell 1 (closed).
- Loops: none armed (launch said zero crons; `org/ref/LIVE_ARMS.md` still lists a 2026-09-28 `~M /canonical-drive 10m` row --
  not armed this session; ask before arming it).

## 2. Done this session (2026-10-02 01:5xZ-04:0xZ)
- **19 Cottonwood seed rows WRITTEN** 02:12:11Z (both halves; merge 96e945c649). Ledger `secclass-cot-seed-rows-m-20261001`:
  M, W, R CLOSED; **S and G open**.
- **29 Cottonwood bank-CD `CUSIP:` rows WRITTEN** 03:40:18Z (writer `MDPF_SECCLASS_M/R7_CHECKS/write_cusip_rows.py`, both halves,
  CTO batch 108). Table now 2,719 rows. Ledger `secclass-cot-cusip-rows-m-20261002`: W CLOSED; R HELD on the re-point's leg S.
- 23:00Z Black Diamond gold fire read: `secclass-e18-trigger-dispatcher-m-20261001` CLOSED, `secclass-model-rows-m-20261001`
  CLOSED. `secclass-bd-thread-r3-m-20261001` HELD (A1, B4). r2's H5 closure committed (only B4 open, read with r3's B4).
- Shared tree: the 10 `infra/aws/lambda/investor-reporting/holdings/` files my 10-01 route build deleted are restored from HEAD
  (COO~P msg 104018, answered).
- Tax SMA page read: superseded -- Tax is LIVE and Andrew validated it on PROD himself (`MDPF_TAXSMA/STATUS.md`).

## 3. Owed, in order, with the event each waits on
1. **r3 A1 + B4** (`secclass-bd-thread-r3-m-20261001`): after the 2026-10-02 04:00Z Black Diamond gold run completes
   (log `s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-10-02_*.log`, ~06:0xZ). C_06 had 0 new partitions on both
   post-deploy runs (watermark 2026-09-29), so its served `gold/views/mix_daily_summary.json` has not moved since 10-01 05:16Z.
   A1: C_06 `To process >= 1`, rc 0, the key advances. B4: page read for relationship z08327149 (VXX structured/Hedge, GLD and
   PHYS commodities/Metals, class_source etf-classifications). Also read r2's B4 there.
2. **Split-account leg S** (`irpt-inf-split-positions-m-20261001`) and **seed-rows leg S**: the 2026-10-02 14:15Z
   irpt-holdings-snapshot publication. Seed S: EVSM fixed_income/Short Duration, PSLV commodities/Metals, SPYI structured/Options
   Income at three firms + one walked Cottonwood selection.
3. **Seed-rows leg G**: the 2026-10-02 23:00Z Black Diamond gold fire reads SPYI, PSLV, FPNIX with the rows' classes. Also read
   E_18 on it (CTO addition 1: every proceeding fire until the round closes).
4. **Cottonwood re-point packet** (`MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md`, unsigned). Preconditions
   now MET (seed rows, CUSIP rows). Before signing: (a) restate its numbers -- re-measured 03:5xZ on the live table (2,719 rows):
   unclassified tomorrow **97.72 M (17.6%)** (was 100.73 M), fixed_income 189.67 M (34.2%); residue by why: no ticker no CUSIP
   71.00 M, ticker has no row 22.24 M, CUSIP has no row 4.49 M; the six name-pattern entries unchanged (387,894.69 USD);
   (b) writers per key: COUNTED by live lineage -- `comp-clobber --sweep opal-data-cot` over gold/views/ (5 keys),
   gold/artifacts/firm_mix (2), platinum/firm/ (12), gold/entities/advisors/ (2), platinum/advisors/ (3),
   gold/entities/clients/ (410), platinum/clients/ (437): 0 interleaved lineages, one producer each; (c) **MERGE TRAP**: branch
   `coo-m-cot-carrier` @68bb14d2f2 forks at dda373cbd3 (the B_00 carrier); CLOUD carries its revert 1c1d2a02c2, so ANY merge
   either way silently DROPS the B_00 change and its test. Fix on the branch: merge CLOUD in (safe-merge), then restore
   `data/cot/scripts/gold/B_00.canonical_holdings.py` and `tests/test_b00_carries_cusip_and_cash_flag.py` from dda373cbd3 and
   commit; re-run the Cottonwood gold tests. A first attempt was ABORTED cleanly at the wind-down (nothing staged).
   (d) the IAM plan read for leg I; (e) portal branch `coo-m-cot-mix-readers` @35cd4be5 merged forward from DEV.
5. CUSIP ledger leg R: read with the re-point's leg S.

## 4. Worktrees
- `C:/Users/AndrewBerman/Desktop/coo_m_r30`: now on `coo-m-cot-carrier` @68bb14d2f2, clean (one untracked audit log).
- `C:/Users/AndrewBerman/Desktop/portal_coo_m`: portal `coo-m-cot-mix-readers` @35cd4be5.
- `C:/Users/AndrewBerman/Desktop/coo_m_mint`, `wk_irpt_bckend_84`: removable; deleting waits on Andrew's word.
- `coo_m_cot_seed` worktree and branch removed (merged).

## 5. Clocks
04:00Z Black Diamond gold (prices-daily); 11:3xZ Cottonwood gold; 13:30Z mdpf-gold-lambda; 14:15Z irpt-holdings-snapshot;
22:10Z BD silver; 23:00Z BD gold.

## 6. Not done and not known
- `etf_classifier.py` serve-hold: two release conditions open (the re-point halves; the host role's read, `cot-pipeline/iam.tf`
  @47e510a186 on CLOUD and NOT applied -- an untargeted apply of that root by any seat would carry it).
- The seed script prints "Items written: N" and "Seeding complete" under `--dry-run` too (seed-etf-classifications.py:288); it
  writes nothing then. Not filed as a row.
- E_18 reads tickerless names only, so the seed packet's coupling claim (E_18 would write SPYI/PSLV/FPNIX first) did not hold.
- audit-archive-invoker at startup: one INTEGRITY/NON-APPEND-EDIT finding on `org/mcp/agent-spawn-audit.log` (MSTR's log; not
  re-filed).

## 7. Relaunch
- `--say` hint: "read org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md, then your inbox".
- First three things: /watcher; item 1 above if the 04:00Z run has completed; then item 4.
