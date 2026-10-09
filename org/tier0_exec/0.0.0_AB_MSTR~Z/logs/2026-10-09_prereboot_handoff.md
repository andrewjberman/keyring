# 0.0.0_AB_MSTR~Z -- pre-reboot handoff, 2026-10-09 ~06:5xZ

Andrew-direct ~06:1xZ: site Z winds down for a reboot. Andrew sets the reboot time; it was unnamed at writing.

## First acts after the reboot, in order

1. Arm `/watcher`, `/agentbus`, `/integrate` (assess) and `/govern 30m` on `6,36 * * * *`.
2. **Relaunch the four Codex CloudOps lanes by hand.** They are NOT on the autolaunch roster, which runs only Claude seats
   through the repo engine. Launch `.tools/ajb2.ps1` for `0.7.0_AE_CloudOps~ZV`, `~ZQ`, `~ZC` and `~ZW`. Each holds crossbox
   ORDERs already delivered to its inbox:
   - `~ZV` (dell1 V1, ETFS_RIVALS): `XB-...-eb6d` (Terminal sign-in pre-flight, 10:20-10:45Z) and `XB-...-897f` (tw1
     vehicle-log relay, after the 11:00Z run).
   - `~ZQ` (dell1 Q1, MDPF_DEMQUE): `XB-...-fbb0` (TO-DQ-t14) and `XB-...-fda4` (the mission-tree order is the authority).
   - `~ZC` (dell1 C1, AMGT_CORPUS): `XB-...-aff1` (13:00Z fire read, 13:20-14:30Z) and `XB-...-7b40` (re-pin, 11:15-12:45Z;
     it SUPERSEDES f12c).
   - `~ZW` (dell1 W1, AMGT_HARVST): `XB-...-3bf7` (bs-4) and `XB-...-99e4` (bs-3).
   Their ACKs to dell1 COOs land only in site Z's local broker, so carry each ACK to dell1 over the bus yourself.
3. Check that the autolaunch roster brought every Claude seat back:
   `C:\opal-elev\autolaunch-agents.ps1`, a wrapper over the repo engine with COOs as `serial=PROJECT_CODE`. Backup
   `.bak-20261009T0525Z`. `2.0.0_SA_COO~SW` was removed because NFRA_SPRINTWIN is closed.
   `3.0.0_SA_CVO~Z` was down before the reboot. 1.0.0_SA_CTO~Z needs it for L8/L9.
4. Tell dell1 (`0.0.0_AB_MSTR~DELL1`) the box is back, and give the time. Tell dell2 too: it parked the data_refresh
   admission ask (~O to CloudOps~Z) and the MCPINDEX readers ask until the reboot.
5. **dell1 relay, after 13:20Z** (bus a4a1a08f, 1.0.0_SA_CTO~DELL1 msg 1930). Copy
   `%LOCALAPPDATA%/opal_bbg_budget/bbg_budget_2026-10-09.jsonl` and the 13:00Z amgt-induction-daily fire's stdout log,
   unchanged, to `s3://opal-data-assets/bloomberg/global/bronze/demand_ledger/dt=2026-10-09/`. Send back both keys and
   their sizes. (A session cron, 96d6aa93, was set for 13:25Z; it dies with the reboot.)
6. NFRA_OPALAI unblock `UB-20261009T054344Z-1afa` is SIGNED. `2.0.0_SA_COO~AI` drives on the fold and resumes it after
   r29 serves. Under /govern after r29: the Analyst relaunch (CTO~Z ruling, step 4).
7. COO~O: close ledger `nfra-oplgtw-og-bf-1-phase-d` with its recorded figures. Its world act is COMPLETE (256/256,
   wk-NFRA_OPLGTW-32-41 @8756eab844). NEVER re-execute it.

## State at writing

- **Branch:** box/sitez is 0 behind CLOUD and on origin.
- **Tree:** cleaned by 1.0.0_SA_CTO~Z (@5392a8f055, @c65797c5cb). Left on purpose: `etf_daily_pull.py`, whose
  uncommitted deletion task OPAL_restore_etf_daily_pull_20261009 restores at 12:00Z, so do not touch it; the
  spawn-audit appends; and the portal gitlink (checkout a3ab197f vs recorded 2d42e9b733, for a box pass).
- **Choke brief for laptop 4.0.0_SA_CRO~A:** `deliverables/BRIEF_20261009_061xZ_SITEZ_FABRIC_CHOKE_GITOPS_GATES.md`
  @19a44d57c0, delivered and acked (laptop bus 4e5868e4).
