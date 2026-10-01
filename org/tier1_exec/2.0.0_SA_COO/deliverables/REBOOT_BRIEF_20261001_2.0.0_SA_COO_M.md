# Reboot brief -- 2.0.0_SA_COO~M -- 2026-10-01 (rewritten 17:5xZ, current state)

Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md` (msg 103892).
Push state: everything below is LOCAL; origin/CLOUD is 0abf99fcd4 (ls-remote 17:50Z). This seat never pushes.

## 1. Identity
- Serial `2.0.0_SA_COO~M`; base folder `org/tier1_exec/2.0.0_SA_COO/`; inbox `org/mcp/inbox/2.0.0_SA_COO/~M/`.
- Projects: IRPT_BCKEND workstream ~M (Investor Reporting Holdings producer, `data/assets/scripts/gold/investor_reporting/`);
  MDPF_SECCLASS issuer (security classification, `org/missions/D8/MDPF/MDPF_SECCLASS/STATUS.md`); MDPF_HEALGAP cell 1.
- FAST leases: `IRPT_BCKEND~M` and `MDPF_SECCLASS` until 2026-10-02 ~01:4xZ; `MDPF_HEALGAP` until 2026-10-01 19:39Z (re-arm only
  if needed).

## 2. Priority (Andrew-direct, relayed 17:43Z, msg 103936)
COOs involved in Tax SMA put it ahead of their own projects; the laptop reboot holds until `4.0.0_SA_CRO` proves Tax SMA on the
Model Portfolios page. This seat signed the COO half of the activation (below). At 17:44Z it offered the CRO one item (per-firm
isolation of `taxsma_sources.load_sources`, so a missing Cottonwood source fails Cottonwood only) or any other the CRO names.
**UNANSWERED at 17:50Z.** The prelude change it needs sits in the CRO's own deployed code (`mdpf_gold_consolidator.py:1332-1338`
and S05); build nothing there unless the CRO names it. Own work is held behind Tax SMA meanwhile.

## 3. Where the work stands
- **Inflection split accounts (IRPT_BCKEND row S259; 91 of 884 accounts listed no positions, 49.98 M USD).** SIGNED BOTH HALVES,
  TO DEPLOY AFTER THE REBOOT. Packet `IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md` on branch
  `coo-m-r30` @cab9bf875d (blob b645c6a3fa; the branch head 1c1d2a02c2 differs from it in 0 files); CTO half
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md` @07e4769540 (msg 103916). Local build:
  security rows 156.12 -> 206.10 M USD = custody, 91 of 91 accounts carry 5,074 positions, 793 others unchanged. Steps: merge
  `coo-m-r30` to CLOUD; open ledger `irpt-inf-split-positions-m-<date>`; ROUTE FIRST (`infra/aws/terraform/investor-reporting/holdings`,
  safe-apply); then `safe-deploy --mint-bundle irpt_holdings_inf`; QA fire `irpt-holdings-refresh-lambda {qa:true}` and QUOTE the
  49 Financial and Cottonwood reconciles in the ledger (CTO condition 1); then the 14:15Z publication with the count of accounts
  in each branch (condition 2) and one walked split account.
- **Cottonwood seed rows (19).** Half `MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_SEED_ROWS_20261001.md` @ff4195fccb on
  CLOUD: COO half signed, **CTO half asked 16:13Z, unanswered**. Code on branch `coo-m-cot-seed-rows` @15a9717715, NOT on CLOUD.
  After signature: merge; pre-run dry run must read 19 of 158 with 0 conflicts; run the seed script; ledger
  `secclass-cot-seed-rows-m-20261001`. Coupling: SPYI, PSLV, FPNIX have no row, so the 23:00Z detector fire may write them first.
- **Cottonwood re-point (classification from the canonical table).** Ruled: batch 93 (cash from the feed's flag; a no-ticker
  CUSIP is a table row; no CUSIP is unclassified) and batch 99 (the mix carries commodities, structured, unclassified as classes).
  Records on CLOUD: the today-by-tomorrow table `MDPF_SECCLASS_M/COT_REPOINT_TODAY_BY_TOMORROW_20261001.md` @e0f8d95bd8 (no
  regression; 100.73 M a correction) and the reader census `MDPF_SECCLASS_M/COT_REPOINT_READER_CENSUS_20261001.md` @a1298b33c9.
  Built on branch `coo-m-cot-carrier` @68bb14d2f2 ONLY (not merged, not deployed; Cottonwood gold tests 22 passed): B_00 carries
  `cusip` and `cash_equivalent`; `lib/etf_classifier.classify_position` (the ruled rule) used by C_06, D_03, D_04; C_06's mix and
  D_03's labels carry the new classes; `lib/mix_views.py` and D_04's firm snapshot publish every class. **Still to build:** the
  seven portal readers of the census (worst `PartnerAnalytics.tsx:633-644`, every Cottonwood user; `composition.ts:117-118`;
  ClientsTab :356/:457; AdvisorBookView; ConsolidatedOverviewPanel :391; AdvisorAnalytics :399/:657) on a portal DEV branch. They
  are under no live lease and outside this seat's lease surface (widen the lease first). Then the packet (both halves), the
  IAM statement's plan and safe-apply, the shipped-artifacts deploy, and a Cottonwood page walk.
- **Done today, closed:** CEMIX entry; model-rows leg H; classifier-release leg H5 (the 14:18Z Holdings publication read at three
  firms, two page walks).

## 4. Open acts that must survive the reboot (all safe to hold: each waits on a scheduled run; nothing half-landed)
- `secclass-e18-trigger-dispatcher-m-20261001`: leg A = tonight's 23:00Z Black Diamond gold fire (PHASE_B3b `E_18 done`, chain exit
  0, 0 CALGUARD lines; a stop between PHASE_B3b and PHASE_B4 rolls this act back first). Rollback VersionId in the entry.
- `secclass-bd-thread-r3-m-20261001` (window 20 h, opened ~06:0xZ): A2 = 22:10Z silver `bd_assets_dim` advances; A1 and B4 = the
  23:00Z gold fire and the page read for relationship z08327149.
- `secclass-model-rows-m-20261001`: leg G = the 23:00Z gold fire reads the six held tickers with class_source etf-classifications.
- `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930` (HELD): only B4 open, read with r3's B4.
- `healgap-cottonwood-catchup-m-20261001`: D1 and S on 2026-10-02 13:30Z (mdpf-gold-lambda), D2 the day after. Served-terms values
  in `MDPF_HEALGAP_M/NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`. If Tax is activated before that run, the CTO's
  amended trigger admits exactly Tax branch 2 (extension fields, a null `tax` member); a Tax dollar on 10-02 still rolls back.
- HELD-STALE `cot-cash-admission-m-20260925` and `bd-securities-cot-new-p1-m-20260926`: gated on the Cottonwood re-point.
- Worktrees: `C:/Users/AndrewBerman/Desktop/coo_m_r30` (on `coo-m-r30` @1c1d2a02c2, clean but for an untracked audit log; check
  out `coo-m-cot-carrier` there to continue the re-point, then switch back); `C:/Users/AndrewBerman/Desktop/coo_m_cot_seed`
  (`coo-m-cot-seed-rows` @15a9717715, clean); `C:/Users/AndrewBerman/Desktop/wk_irpt_bckend_84` (old worker branch; deleting it
  waits on Andrew's word).
- Clocks: 22:10Z silver; 23:00Z Black Diamond gold; 2026-10-02 13:30Z mdpf-gold-lambda; 14:15Z irpt-holdings-snapshot.

## 5. Owed
- This seat owes: the split-account deploy (signed); the Cottonwood re-point packet with its seven portal changes (batch 93 item 4,
  batch 99 item 3); the reads of tonight's and tomorrow's runs above.
- Others owe this seat: `1.0.0_SA_CTO` the half on the 19 seed rows (16:13Z); `4.0.0_SA_CRO` its answer on a Tax SMA item (17:44Z).
- Signed by this seat: the COO half on Tax SMA activation TX-r-3, `COO_HALF_TAXSMA_TX_R_3_ACTIVATION_20261001.md` @07d269eb28
  (both halves now in place; the activation, its ledger and portal PROD are `4.0.0_SA_CRO`'s and Andrew's).

## 6. Relaunch
- RESPAWN: yes -- four ledger entries close on tonight's and tomorrow's runs, one signed deploy and one packet are owed.
- First three things: run /watcher; read this brief and the inbox (first: any CRO answer on Tax SMA); deploy the signed
  split-account packet, route first, under its ledger.
- `--say` hint: "read org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md, then your inbox".

## 7. Not done and not known
- The split change's page effect is not walked (it is not deployed); its local build is the evidence.
- The iam.tf statement for the Cottonwood host role (`infra/aws/terraform/cot-pipeline/iam.tf` @47e510a186) is on CLOUD and NOT
  applied; an untargeted apply of that root by any seat would carry it.
- Three census reachabilities not determined (the partners Lambda's Cottonwood bucket row; `ClientsTab.tsx:457`; the parity CLI).
- Drive-log commits for ticks after 52 were not written; the runtime log `org/mcp/drive_ticks/2.0.0_SA_COO~M.md` has them.
