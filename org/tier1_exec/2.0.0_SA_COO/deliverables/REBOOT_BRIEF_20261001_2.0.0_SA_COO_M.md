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
**ANSWERED 18:06Z (msg 103941): no build item.** The one item, event-triggered: when `4.0.0_SA_CRO`
says Tax is served (after site Z's Gateway release, the activation and two ad-hoc runs), read the Model Portfolios page on DEV for
49 Financial and Global -- the totals, the caption, the SMA > ALT Strategies Tax leaf -- and report it against
`org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md`. Per-firm isolation of `load_sources` stays parked. The first-day rule Andrew ruled
is deployed (18:03Z). Own work resumes until that word arrives.

## 3. Where the work stands
- **Inflection split accounts -- DEPLOYED 2026-10-01; only leg S open.** Ledger `irpt-inf-split-positions-m-20261001`: M (merge
  @b4d4548d5a), R (route irpt-holdings CodeSha256 tS/APci3.. at 20:13:14Z, lane grant CTO batch 101), P (three irpt_holdings_*
  bundles minted 20:39Z-20:41Z from each firm's OWN live members with only the two signed files swapped, worktree
  `C:/Users/AndrewBerman/Desktop/coo_m_mint`, branch `coo-m-split-mint`, scratch, removable), Q (QA fire Success x3; Inflection
  QA = the packet's build; 49 Financial 7,570/7,570 and Cottonwood 851/851 unchanged; live route reconciles 884/884, prior
  route 793/884) all CLOSED. LEG S, 2026-10-02 after the 14:15Z irpt-holdings-snapshot fire: run
  `IRPT_MVP_M/R30_CHECKS/split_qa_read.py` adapted to the served namespace, state the count of accounts in each branch (CTO
  condition 2: the stale-assignment swing can send them back to `client_values_do_not_tie`), walk one split account on the
  page, close S. The push of 21:3xZ: this seat answered HOLD for holdings_snapshot.py/holdings_inf.py (msg 103971) -- the
  directory runner's commit-routed bundle `investor-reporting.tar.gz` holds holdings_snapshot.py and no half covers it.
  Packet `IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md` (on CLOUD, addendum 1 @5d4a1b60fe);
  CTO half @07e4769540.
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
  D_03's labels carry the new classes; `lib/mix_views.py` and D_04's firm snapshot publish every class. **Portal readers BUILT, not pushed:** portal branch `coo-m-cot-mix-readers` @35cd4be5 in worktree
  `C:/Users/AndrewBerman/Desktop/portal_coo_m` (from origin/DEV 2bb367ef): PartnerAnalytics maps every served class,
  composition.ts keeps `unclassified`, ClientsTab passes includeOther, the donut legend and AdvisorAnalytics carry every class,
  Cottonwood's layout lists `unclassified`. tsc clean, eslint 0 errors, new test fails on the old helper, class-reader census OK;
  IVE49-AC1 (colour distance) fails identically on DEV (not this change). chartColors.ts is 2.0.0_SA_COO~D's, not changed.
  HELD, NOT PUSHED, by decision 18:2xZ: the page look needs a dev server on 5174 (portal law: 5174 only), which serves the
  shared checkout, and the served data carries none of the new classes until the gold side ships -- so the branch ships WITH
  the re-point packet, its acceptance being a Cottonwood page walk after the gold deploy. Before the push:
  `git -C <worktree> log origin/DEV..HEAD` lists only this seat's commit; merge DEV forward first. Lease
  MDPF_SECCLASS re-armed 18:1xZ to cover these files (same expiry). PACKET DRAFTED (unsigned): `MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md` @1ffbf6a639
  -- legs M, I, A, G, P, R, S. Open before signing: the 19 seed rows' CTO half; the CUSIP rows' own half -- DRAFTED
  `MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_COT_CUSIP_ROWS_20261001.md` @17744bb533: 29 bank CDs (3.01 M USD) follow the table's 8
  bank-CD `CUSIP:` rows; 4.47 M USD of the 7.49 M gap is 8-character Black Diamond identifiers, NOT CUSIPs (stay unclassified;
  a vendor namespace is a four-postulate proposal); 2 mortgage-backed bonds have no peer. Its writer (the conditional put
  Black Diamond's E_18 uses, on the write-model-rows.py pattern) is NOT BUILT; the writer count per served key. Then the packet (both halves), the
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
- `healgap-cottonwood-catchup-m-20261001`: CLOSED 22:1xZ, all four legs. D2 read on the CRO's 22:08Z Gold run (manifest
  `_manifests/2026-09-30/20261001T220850Z.json`: catchup 0 planned, 0 built, 0 failed). Nothing owed on it.
- HELD-STALE `cot-cash-admission-m-20260925` and `bd-securities-cot-new-p1-m-20260926`: gated on the Cottonwood re-point.
- Worktrees: `C:/Users/AndrewBerman/Desktop/coo_m_r30` (on `coo-m-r30` @1c1d2a02c2, clean but for an untracked audit log; check
  out `coo-m-cot-carrier` there to continue the re-point, then switch back); `C:/Users/AndrewBerman/Desktop/coo_m_cot_seed`
  (`coo-m-cot-seed-rows` @15a9717715, clean); `C:/Users/AndrewBerman/Desktop/wk_irpt_bckend_84` (old worker branch; deleting it
  waits on Andrew's word).
- Clocks: 22:10Z silver; 23:00Z Black Diamond gold; 2026-10-02 13:30Z mdpf-gold-lambda; 14:15Z irpt-holdings-snapshot.

## 5. Owed
- This seat owes: the split-account leg S read (2026-10-02 after 14:15Z; deploy done 2026-10-01); the Cottonwood re-point packet with its seven portal changes (batch 93 item 4,
  batch 99 item 3); the reads of tonight's and tomorrow's runs above.
- Others owe this seat: `1.0.0_SA_CTO` the half on the 19 seed rows (16:13Z); `4.0.0_SA_CRO` the word that Tax is served (then
  this seat reads the Model Portfolios page, section 2).
- Signed by this seat: the COO half on Tax SMA activation TX-r-3, `COO_HALF_TAXSMA_TX_R_3_ACTIVATION_20261001.md` @07d269eb28
  (both halves now in place; the activation, its ledger and portal PROD are `4.0.0_SA_CRO`'s and Andrew's).

## 6. Relaunch
- RESPAWN: yes -- four ledger entries close on tonight's and tomorrow's runs, one signed deploy and one packet are owed.
- First three things: run /watcher; read this brief and the inbox (first: has the CRO said Tax is served? then the page read); deploy the signed
  split-account packet, route first, under its ledger.
- `--say` hint: "read org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md, then your inbox".

## 7. Not done and not known
- The split change's page effect is not walked (it is not deployed); its local build is the evidence.
- `etf_classifier.py` serve-hold, three release conditions: (3) the shared client at `s3://opal-data-cot/code/gold/lib/_shared/`
  is MET -- first-minted by the laptop push a3866c3dfb at 22:26Z-22:27Z (msg 103988), inert: the served `etf_classifier.py`
  (2026-06-10) never reads `_shared/`. Still open: (1) the re-point packet's two halves, (2) the host role's read of
  etf-classifications (the iam.tf statement below, not applied).
- The iam.tf statement for the Cottonwood host role (`infra/aws/terraform/cot-pipeline/iam.tf` @47e510a186) is on CLOUD and NOT
  applied; an untargeted apply of that root by any seat would carry it.
- Three census reachabilities not determined (the partners Lambda's Cottonwood bucket row; `ClientsTab.tsx:457`; the parity CLI).
- Drive-log commits for ticks after 52 were not written; the runtime log `org/mcp/drive_ticks/2.0.0_SA_COO~M.md` has them.
