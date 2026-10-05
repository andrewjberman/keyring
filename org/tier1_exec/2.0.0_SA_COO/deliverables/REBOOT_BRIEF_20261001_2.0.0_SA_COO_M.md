# Reboot brief -- 2.0.0_SA_COO~M -- rewritten 2026-10-02 04:0xZ at the wind-down; updated 05:2xZ

**UPDATE 2026-10-05 00:3xZ -- multi_asset packet ACTED (supersedes every line below where they differ):**
- Authority: Andrew ~22:1xZ 10-03 "proceed call 2"; ~22:0xZ 10-04 card 4 (49F paired read only, not a general lift of the
  restart hold). Halves: COO @1131610939, CTO batches 240 + 244. Ledger `secclass-multi-asset-rows-and-remint-m-20261004`:
  - M: 7 moves; S: 20 seed rows (module @96f17cdbe9); C: 12 CUSIP rows. Table 2,866.
  - H: hold release @9efbec3c2f / drain e9401c03ff (103971 + 103981 lines gone).
  - R: inf SuRm8tIY.., directory KK09i.JS.., 49f 3Q_W49U7.., cot NZIQjid2.. (prior VersionIds = rollback, in the proof).
  - T: irpt-holdings contract pin 4cc72587d6, CodeSha256 RmruvCeo...
  - OWED: leg V = the first irpt-holdings-snapshot after the act, MONDAY 2026-10-05 10:15Z. Read: packet keys carry
    multi_asset, totals unchanged, readers render it.
- Rows S23 (rows landed before two producers admitted the class; ARMED) -> S24 (disarmed 00:16Z by the re-mints).
- Closed today: S18 cell ledger (CVO leg S PASS), cot seed-rows ledger (leg G read).
- Still owed (reads only; call 3 approved one at a time): BD r4 leg S walk, cot re-point leg S walks. Walker is shared
  with site Z: send ARM / DISARMED to 0.0.0_AB_MSTR, and write 'NEXT RUN FOLLOWS' when re-arming at once.
- Parked on Andrew: the TARGET fold (its contract text rides the bundles, inert), every other data-engineering act.

**UPDATE 2026-10-03 17:5xZ -- ANDREW-DIRECT ~17:3xZ (relayed by 0.0.0_AB_MSTR 104661; record
ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md @4d393e3521, site Z):**
release any quarantine, hold or pause on data collection or pipelines; NO data-engineering change without Andrew's
explicit directive.
- This seat holds NO pause or quarantine on data collection or pipelines, read 17:5xZ:
  - both BD gold rules ENABLED (re-enabled 12:44Z after today's S18 hold);
  - bd-gold-trigger has no reserved concurrency;
  - the five HELD-SOVEREIGN-GATED ledgers each await a verify read only.
  So there was nothing to release.
- Six DEPLOY-SERVE-HELD lines name this seat. Each keeps undeployed CLOUD code at its served bytes:
  `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, `holdings_inf.py`, `build_dim_model_portfolio.py`,
  `build_cottonwood_mdpf_slice.py`, `build_cottonwood_mdpf_pair.py` and `silver/rebalancer_schemas.py`. They pause nothing;
  removing one invites a deploy, which is a data-engineering change, so they stay unless Andrew says otherwise.
- FROM NOW: every pending act is PARKED on Andrew's explicit directive. That covers the multi_asset packet, the TARGET fold,
  the cot seed and re-point acts, and any deploy, row write or watermark move. Reads continue, including the CVO's leg S read.

**UPDATE 2026-10-03 12:5xZ -- S18 DONE except the CVO's leg S (supersedes every line below where they differ):**
- Class cell LIVE: A_03 wTaLoeFXO4.. (scoped liveness: dimension-open AND held on the reference day; output backstop; refusal
  writes nothing and exits 2). Half: COO @56d91fc1ec, CTO batch 224. Ledger `secclass-s18-cell-m-20261003`: P G W Q V R closed
  (QA run exit 0, frontier whole; served mix 10-01 $1,843,207,824.50; 332 of 335 back, 3 traded out; 09-30 content-equal).
  Leg S OWED by 3.0.0_SA_CVO (asked 12:47Z): its read of the first scheduled fire after R = the 12:45:15Z 49F floor boot.
- Restore ledger `secclass-s18-restore-0930-m-20261003` CLOSED. Both gold rules ENABLED 12:44Z.
- Rows S20 (dimension marks dead accounts open), S21 (S3 prices notification boots BD gold), S22 (the runner boots from >= 5
  paths incl. advi-49f-gold-dispatch; it ran the old A_03 at 09:47Z, no write). Next BD hold = hold the host.
- Cosmetic, not done: A_03's log label 'confirmed open by alloc' now counts the scoped carry set's backfill-only members.
- Memory reaper killed the QA waiter (not restarted); one-shot foreground reads only.

**UPDATE 2026-10-03 08:4xZ -- S18 (supersedes every line below where they differ):**
- Row MDPF_SECCLASS-S18 (the 04:00Z BD gold run dropped 335 open accounts, $78.6M, from as_of 10-01); cause row S19 (A_03
  confirms backfill-only accounts open from a WEEKLY allocation file). Ledger `secclass-s18-restore-0930-m-20261003`: legs 0, H
  (both gold rules DISABLED 07:17Z), C (23,542 served keys restored; 1 multipart ETag mismatch content-verified), V (mix 09-30
  $1,843,114,311.70) CLOSED. Leg R OPEN: when the cell lands, C_06 watermarks to 09-30 + rules re-enabled BEFORE MONDAY 04:00Z,
  else report by Sunday 18:00Z.
- Class cell (CTO batch 220; lane batch 221): A_03 liveness from the accounts dimension + a frontier backstop on the built
  partitions + no gate-watermark advance on refusal. CLOUD 564d5bede9 / 5df4c735fa (drains 4f1c1b2b59, dafb13cfb2), 6 + 74 tests,
  NOT deployed. Deployed A_03 = VersionId 1MYNHoSQ.. (md5 6bce3508, rollback). NEXT: delta census
  (R9_CHECKS/s18_cell_delta_census.py), the cell's half to the CTO (signs on receipt), then deploy + watermark reset + one QA
  run + leg R.
- Other owed (unchanged): BD r4 leg S walk; cot re-point leg S; cot seed leg G; multi_asset packet and TARGET-fold 49F QA are
  HEAVY (memory reaper) -- user's word before restarting.

**UPDATE 19:4xZ -- STATE (supersedes every line below where they differ):**
- Portal PROD f76b02acb6 carries eb90f2ad (Andrew's promote; read 13:56:40Z). Both re-land acts RAN.
- BD r3 RE-LAND (ledger `secclass-bd-thread-r4-reland-m-20261002`): P, M (drain ac44b6aaaf, release b3442d6ea1), G (five files
  14:16Z), W (watermarks to 09-29), R (QA run green: unclassified 4.14 pct, every class, identity hops in the log) CLOSED. OWED:
  leg S at tonight's 23:00Z gold fire (firm mix, every class, <= 5.0 pct) + one walked 49F page on PROD readers; and the 22:10Z
  silver read (batch 129). Rollback: copy-object of the prior VersionIds in leg G's proof; watermarks per leg W.
- Cottonwood RE-POINT (ledger `secclass-cot-repoint-m-20261002`): PROD, M (bf165606a2; release 917fd2ff02), I (role +1 statement),
  A + G (17:28-17:30Z), W (CTO addendum 2, batch 179) and R (QA green, 17.37 pct unclassified, 219 of 219 clients sum) CLOSED.
  OWED: leg S at the 2026-10-03 scheduled Cottonwood gold run (~11:35Z) + walks (firm Mix chart, Books donut, one advisor Mix).
- Holdings 14:15Z publication read: three row ledgers CLOSED (7421b39e62). Still open: `irpt-inf-split-positions-m-20261001` leg S
  (branch count read: 71 split / 786 single; the WALK of acc_015d15b45d7a8ac71f951a67 owed) and `secclass-cot-seed-rows-m-20261001`
  leg S (data read 19 of 19; the Cottonwood selection WALK owed) + leg G at 23:00Z. Walker account is shared with 2.0.0_SA_COO~D.
- multi_asset readers packet (batch 164): producer + three schema copies on CLOUD (daaef69b9d, ~P 16a3fcfd6a); Advisor
  Intelligence readers on portal DEV 90a31d7d (CTO PASS 104340, MSTR landed); ~D's colour + IR readers on DEV 7bcedf1b. NEXT: the
  packet's deploy halves (producer deploy, irpt-holdings re-stage) and PROD readers (Andrew's promote); rows only after.
- CTO batch 178: STATUS~M.md current (dbc5e1a5c7); item 2 (after ~D's H-1, landed DEV 16c6690e): 49F largest client
  cli_8499bbbd... expects 17 tiles by the map rule (sent to ~D 104378); bring brief 3 item 1.4(d) TARGET fold back as its own ask.
- Row S15 code half done (writer refuses non-ASCII names, 821bb7b891); the one row's ASCII rewrite rides the next CUSIP-row act.
- Row S16 filed (BD gold deploy re-ships lib/_shared; DISMISSED_WITH_REASON). FAST lease MDPF_SECCLASS LAPSED 13:54Z (not re-armed).
- Push state: every commit of this seat LOCAL; origin CLOUD is the integrator's.

**UPDATE 12:2xZ -- STATE (supersedes the 10:3xZ line where they differ):**
- Table `etf-classifications` 2,841 rows. Written today under both halves: 19 Cottonwood seed (02:12Z), 29 Cottonwood CUSIP CDs
  (03:40Z), 67 bd-mapped (10:26Z), 3 seed ABNFX/LBNYX/NYT (10:30Z), 16 per-ticker first act (11:21Z), 36 residual CUSIP rows (12:18Z).
- BD r3 RE-LAND: branch `coo-m-bd-mix-classes` @29747a2ecb (worktree `coo_m_r30`): fix 1 (eight-class mix) + the identity read (batch
  156). Real run on 09-30: 49F unclassified 4.63 pct (3.99 with the 36 rows). Half `NEVER_WIDEN_HALF_REQUEST_BD_THREAD_R3_RELAND_20261002.md`
  SIGNED both (CTO batch 161) CONDITIONAL on portal PROD carrying eb90f2ad (Andrew's promote). CLOUD's four r3 files are serve-held
  @056e9f0a74 (row S13); the re-land's merge releases them under SERVE-RELEASE-ACK.
- Cottonwood RE-POINT: both halves (CTO conditional, batch 113): legs G, R, S wait on the same PROD promote; leg P (DEV eb90f2ad) closed.
- Open ledgers owing leg S at the 14:15Z Holdings publication: `irpt-inf-split-positions-m-20261001`, `secclass-cot-seed-rows-m-20261001`
  (also G at 23:00Z), `secclass-bd-mapped-rows-m-20261002`, `secclass-cot-name-pattern-rows-m-20261002`, `secclass-bd-first-act-seed-m-20261002`.
- Tonight (batch 129): 22:10Z silver (bd_assets_dim classes as the old library) and 23:00Z gold (49F firm mix 100 pct).
- Next authoring work: the allocation-class proposal (batch 145 C, mine); the residual's later acts and the per-ticker group's rest.
- Surprise rows filed today: S10-S14 (S13 ARMED->disarmed same commit).

**UPDATE 10:3xZ -- BD FORWARD FIX (CTO tick 6, msg 104138):** fix 1 (BD mix carries every class) BUILT on branch
`coo-m-bd-mix-classes` @0ce0ad6efd in worktree `coo_m_r30` (lane grant batch 135; BD tests 72; not merged, no packet yet). Fix 2
(67 bd-mapped rows, batch 139/140) WRITTEN 10:26Z, ledger `secclass-bd-mapped-rows-m-20261002` W closed. Fix 3 (ABNFX, LBNYX,
NYT seed rows; QACDS stays cash) WRITTEN 10:30Z, ledger `secclass-cot-name-pattern-rows-m-20261002` M, W closed. Table 2,789.
The 119 + 30 per-ticker rows (batch 139: by peer, dollar order, first act to 80 pct) NOT started. OPEN RULE ASK 10:32Z: r3 + fix 1
would serve 49F 23.78 pct unclassified (433.1 M = ETFs with a blank ticker on the holdings row) -- may a name resolve a ticker?
(`R8_BD_RELAND_TOMORROW_20261002.md` @3fd8c3688e). Leg S of BOTH new ledgers, the 19 seed rows and the split accounts: the
14:15Z Holdings publication.

**UPDATE 08:4xZ -- INCIDENT CLOSED ROLLED-BACK (CTO batch 129, msg 104131):** V1 green 08:2xZ (49F firm mix 1.000000 at
1,843,114,302.78; z08327149 VXX 1,111,544.96 in alternatives, gap 0.00); restore run exit 0 08:31:13Z; ledger
`secclass-bd-thread-r3-rollback-m-20261002` CLOSED. E_18, silver builder, lib/_shared, SSM v5 STAY on r3 (batch 129). OWED
TONIGHT: read the 22:10Z silver fire (`silver/bd_assets_dim.parquet` classes as the old library) and the 23:00Z gold fire (firm
mix sums to 100 percent); if either moves, roll the r3 silver builder back (its prior VersionId is in r3 leg P). Same 23:00Z fire:
seed-rows leg G. Forward fix for r3: batch 117 item 4 (BD C_06 carries unclassified and the batch 99 classes; the 290 tickers get
rows through a mapped writer under its own half). r3 entry: B4 open, HELD on the CTO.

**UPDATE 06:3xZ -- INCIDENT IN FLIGHT (superseded by the line above):** BD thread r3 failed leg B4 -- the 04:00Z BD gold fire served a 49 Financial
firm mix of 1,397.4 M against 1,843.1 M (290 tickers with no canonical row left the mix; z08327149 lost VXX 1.10 M since 10-01
07:46Z). CTO batches 117-118: ROLL BACK + ONE ad hoc restore run. Done: C_06, D_03, D_04, lib/etf_classifier.py copied back to
their pre-r3 versions 06:19Z (ledger `secclass-bd-thread-r3-rollback-m-20261002`, legs P, C closed); both C_06 watermark keys
restored to 2026-09-29 06:24Z; `bd-gold-trigger {"mode":"incremental"}` fired 06:25:45Z. OWED: V1 on that run's output --
`platinum/firm/mix_summary.json` sums to 100 percent at about 1,843 M and z08327149 carries VXX -- then close leg W and the
ledger ROLLED-BACK. FALLBACK if not green by 11:00Z: restore each overwritten served key to its version just before the 04:00Z
write (batch 117 item 3(b)). E_18, silver, lib/_shared, SSM v5 left in place (E_18 ran rc 0 under the dispatcher; old E_18
never has). r3 re-lands only per batch 117 item 4.

**UPDATE 05:2xZ:** the laptop wind-down was WITHDRAWN (MSTR msg 104038: it was site Z's disk). Work resumed; lease MDPF_SECCLASS
re-armed to 07:09Z. Item 4 below: the merge trap is FIXED (branch `coo-m-cot-carrier` @affbc33e2b, 22 tests, dry merge = the ten
files), the packet is restated and the COO half SIGNED @40cc2e2108 (blob 59c1da5458); CTO half asked 05:19Z. The `coo_m_r30`
worktree is on `coo-m-cot-carrier`.

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
