# IRPT_BCKEND REBOOT HANDOFF -- 2.0.0_SA_COO~B -- 2026-09-21 ~10:00Z (Andrew reboot)

Andrew is rebooting the box (his word ~09:5xZ; CTO relay 99028). This record survives the reboot; my session context does not. It is the ONE read a successor 2.0.0_SA_COO~B needs to resume BCKEND.

## Andrew's standing directives (verbatim, this session)
1. ~09:3xZ: *"I am getting FNTEND COO~F seated right now. I am also going to bring on CVO~B and CVO~F who are going to be designated to your projects, because we need to drive these forward above all else. They are more important than any other projects. Please review what you can proceed for BCKEND and drive it forward."* -> **IRPT is TOP PRIORITY above all projects; 3.0.0_SA_CVO~B is BCKEND's CVO; 3.0.0_SA_CVO~F is FNTEND's.** (Full record: `ANDREW_DIRECT_20260921_093xZ_IRPT_TOP_PRIORITY_CVO_LANES_DRIVE_BCKEND.md`.)
2. ~09:5xZ: *"wind down your team at the next logical checkpoint and prepare for how you can parallelize the work"* + *"I will reboot this device."*

## Round-8 state at reboot (measured)
- dep_stage EXECUTING, round 8. **2 of 4 cells terminal.** CLOUD HEAD `8e720b7bef` (a CTO log commit on top of my last BCKEND drain `5e2f31a4b4`).
- **rth-3** (status-word hygiene) TERMINAL, drained `4009c22cf5`.
- **rth-4** (110->150-row disposition) TERMINAL, drained `5e2f31a4b4`. Left 150 open rows CARRIED: 108 to COO~B, 37 to CTO, 5 orphaned to worker ~3 (need re-owning to a live seat).
- **rth-1** (inflection serving route, FWD-2 serving, W3-S50) -- worker STOPPED by wind-down at its arm-c STOP (B1-served: investigation done, source edit made, packet written, NOT applied, awaiting CTO+COO halves). **ITS WORK IS UNCOMMITTED IN `/c/tmp/wk-irpt-8-1` on branch `wk-irpt_bckend-8-1`:** modified `infra/aws/lambda/investor-reporting/_authz/loaders.py` (the B1 rectify) + `surprise-channel/investigations/INVESTIGATION_v1.md` (a W1-S row); untracked deliverables under `deliverables/0.9.0_WK_IRPT_BCKEND~1/`: `IB-rth-1_investigation.md`, `NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-1.md`, `battery_ib_rth_1_code_verify.py`, `IB-rth-1_code_verify_output.txt`; `.scratch/` holds `inf_directory_pointer.json`, `scoped_policy.json`. **If the branch WIP commit alongside this record succeeded, it is on `wk-irpt_bckend-8-1`; if not, recover from `/c/tmp/wk-irpt-8-1` (C:\tmp survives reboot) or re-spawn rth-1 with it as a head-start. READ ITS `IB-rth-1_investigation.md` + PACKET FIRST -- it decided the B1/B2/B3 branch on evidence.**
- **rth-2** (export submit-wiring, FWD-2 serving, W1-S43) NOT spawned; order ready at `07faf174d2` (`task-orders/IRPT_BCKEND.TO-IB-rth-2...md`). It is a deploy cell (packet+halves, apply).

## PARALLELIZATION PLAN (prepared per Andrew ~09:5xZ; execute after reboot)
**The ONLY hard serialization is the Terraform apply plane; everything else parallelizes.**
1. **Round 8, finish in parallel:** rth-1 and rth-2 are INDEPENDENT surfaces (rth-1 = `_authz/loaders.py`; rth-2 = `export/`), both FWD-2 serving. Run BOTH as concurrent workers through investigate/build/**packet**. BOTH stop at their never-widen packet before apply, so the applies serialize at MY halves-signing (with CTO), one root at a time -- no concurrent-apply hazard. Recover rth-1's packet (already produced) -> review + sign halves with CTO -> its apply; concurrently spawn rth-2 -> its packet -> halves -> apply. Disk was 37 GB; 2-3 worktrees fine.
2. **CVO~B accelerates the close:** hand the round-8 L8 compile to `3.0.0_SA_CVO~B` (dedicated) rather than base CVO -> L9 not queued behind other projects -> faster round turnover.
3. **Round 9+ parallelizes the owned machinery:** FWD-7 (directory freshness/expiry), FWD-9 (email-intake durability), FWD-10 (firm-binding-at-ingestion) are independent surfaces -> cut as parallel cells (cap 8 per the issuance fanout; realistically 3-4 concurrent). Plus the FWD-2 realization replay once serving routes are live for all 3 firms.
4. **Cross-project seam (with COO~F on FNTEND):** BCKEND is the contract PRODUCER (publish the versioned contract artifact); FNTEND CONFORMS. This is the coordination point for realizing the advisor-facing FWDs (1/3/4/5/8/11). Publish BCKEND's contract -> COO~F conforms FNTEND -> paired producer->consumer test crosses the real client into the real dispatcher. This is what actually moves the 0-realized needle.

## Post-reboot resumption checklist (for 2.0.0_SA_COO~B)
1. `get_live_agents` + `register_agent` (session died -> STALE).
2. Re-arm the inbox Monitor (`/watcher`; prefix `/cygdrive/c`).
3. Re-arm the `/canonical-drive` cron -- session crons die on reboot; re-arm per org/XXX.md Step 1b-F (carrier @c9631a22db).
4. Recover rth-1: check `wk-irpt_bckend-8-1` for the WIP commit; if absent, recover `/c/tmp/wk-irpt-8-1` uncommitted work; read its investigation + packet.
5. Watch for `3.0.0_SA_CVO~B` and `2.0.0_SA_COO~F` coming live.
6. Execute the parallelization plan above.
