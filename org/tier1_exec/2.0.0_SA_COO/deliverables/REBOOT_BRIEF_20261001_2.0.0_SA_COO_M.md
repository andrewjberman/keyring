# Reboot brief -- 2.0.0_SA_COO~M -- 2026-10-01 (written 16:3xZ)

Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md` (msg 103892).

## 1. Identity
- Serial `2.0.0_SA_COO~M`; base folder `org/tier1_exec/2.0.0_SA_COO/`; inbox `org/mcp/inbox/2.0.0_SA_COO/~M/`.
- Projects: IRPT_BCKEND workstream ~M (Investor Reporting Holdings producer, `data/assets/scripts/gold/investor_reporting/`);
  MDPF_SECCLASS issuer (security classification, `org/missions/D8/MDPF/MDPF_SECCLASS/STATUS.md`); MDPF_HEALGAP cell 1.
- FAST leases: `IRPT_BCKEND~M` and `MDPF_SECCLASS` until 2026-10-02 ~01:4xZ; `MDPF_HEALGAP` until 2026-10-01 19:39Z (re-arm only if needed).

## 2. Where the work stands
- IRPT_BCKEND row S259 (Inflection split accounts list no positions, 91 of 884 accounts, 49.98 M USD): ruled YES by CTO batch 96
  (msg 103859). Build is WORK IN PROGRESS on branch `coo-m-r30` @b26847ea04, NOT merged. Open design point: one producer test
  (`test_l0_categories.py::test_inf_accounts_group_into_categories_present`) requires every account's children to be category
  lines; positions directly under the account break it. Decide where the positions hang, then write the packet (both halves).
  Cause measured: 87 of 89 did not tie on the stale 09-27 assignment snapshot and tie on 10-01 (see the commit message).
- MDPF_SECCLASS Cottonwood seed rows: half `MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_SEED_ROWS_20261001.md`
  @ff4195fccb, COO half signed, CTO half asked (my msg 16:13Z). Code on branch `coo-m-cot-seed-rows` @15a9717715, NOT on CLOUD.
  After signature: merge, pre-run dry run must read 19 of 158 with 0 conflicts, run the seed script, open ledger
  `secclass-cot-seed-rows-m-20261001`.
- Cottonwood re-point: ruled by CTO batch 93 (cash from the feed's flag as class `cash`; a no-ticker CUSIP is a table row;
  no CUSIP is unclassified). Packet not started; it needs the "today's rule by tomorrow's class" table (batch 93 item 4).
- Holdings publication of 14:18Z read: CEMIX ledger CLOSED; model-rows leg H closed; classifier-release leg H5 closed.

## 3. Open acts that must survive the reboot (all safe to hold: each waits on a scheduled run, nothing half-landed)
- `secclass-e18-trigger-dispatcher-m-20261001`: leg A open = tonight's 23:00Z Black Diamond gold fire (PHASE_B3b `E_18 done`,
  chain exit 0). Served since 08:41Z; rollback VersionId in the entry.
- `secclass-bd-thread-r3-m-20261001`: A2 (22:10Z silver `bd_assets_dim` advances), A1 and B4 (23:00Z gold fire, page read).
- `secclass-model-rows-m-20261001`: leg G (23:00Z gold fire reads the six held tickers with class_source etf-classifications).
- `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930` (HELD): only B4 open, read with r3's B4.
- `healgap-cottonwood-catchup-m-20261001`: D1, S on 2026-10-02 13:30Z (mdpf-gold-lambda, deployed by 4.0.0_SA_CRO at 15:00Z),
  D2 the day after. Served-terms values are in `MDPF_HEALGAP_M/NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`.
- Held entries `cot-cash-admission-m-20260925` and `bd-securities-cot-new-p1-m-20260926`:
  HELD-STALE, gated on the Cottonwood re-point; nothing to do before it.
- Worktrees: `C:/Users/AndrewBerman/Desktop/coo_m_r30` (coo-m-r30 @b26847ea04, clean but for an untracked audit log);
  `C:/Users/AndrewBerman/Desktop/coo_m_cot_seed` (coo-m-cot-seed-rows @15a9717715, clean);
  `C:/Users/AndrewBerman/Desktop/wk_irpt_bckend_84` (old worker branch; deleting it waits on Andrew's word).
- Clocks: 22:10Z silver, 23:00Z Black Diamond gold, 2026-10-02 13:30Z mdpf-gold-lambda, 14:15Z irpt-holdings-snapshot.

## 4. Owed
- I owe 1.0.0_SA_CTO: the split-account packet (batch 96); the Cottonwood re-point packet (batch 93 item 4).
- Others owe me: the CTO half on the 19 seed rows (my msg 16:13Z).

## 5. Relaunch
- RESPAWN: yes -- three ledger entries close on tonight's runs and two packets are owed.
- First three things: run /watcher; read this brief and the inbox; read the 22:10Z and 23:00Z runs against the open legs.
- `--say` hint: "read org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md, then your inbox".

## 6. Not done and not known
- The split build's page effect is not walked; the producer was not run locally against live data with the change.
- The iam.tf statement for the Cottonwood host role (`infra/aws/terraform/cot-pipeline/iam.tf` @47e510a186) is on CLOUD and
  NOT applied; an untargeted apply of that root by any seat would carry it.
- Drive-log commits for ticks after 52 were not written this hour.
