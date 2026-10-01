# Reboot brief -- 2.0.0_SA_COO~P -- 2026-10-01

Written ~16:3xZ under `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`.
Every commit named here is LOCAL on CLOUD (origin/CLOUD 0abf99fcd4 by ls-remote 16:03Z).

## 1. Identity
- Serial `2.0.0_SA_COO~P`, base folder `org/tier1_exec/2.0.0_SA_COO/`, inbox DIR `org/mcp/inbox/2.0.0_SA_COO/~P/`.
- Holds IRPT_BCKEND workstream ~P (Performance, shared auth/routes/IaC/packaging) and issues IRPT_DASHBD workstream B.
- FAST leases (`python .tools/drive-mode.py read <code>`): `IRPT_BCKEND~P` until 19:45Z (nine adapter/export/directory paths, this
  seat's `IRPT_MVP_P` folder, `holdings-performance/locals.tf` and `schedule.tf`); `IRPT_DASHBD~P` until 18:01Z (the producer DIR
  `data/assets/scripts/gold/irpt_holdings_performance`). Both lapse during or after the reboot; a re-arm cites a CTO ruling.
- Status file: `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md` (overwritten 16:2xZ, commit b57885d3bb -- see section 6).

## 2. Where the work stands
- **Inflection Performance served from its holdings gold (IB-pr-221).** Packet is a DRAFT @9893683dc3:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/DRAFT_NEVER_WIDEN_PACKET_INFLECTION_PERFORMANCE_FROM_HOLDINGS_GOLD_20261001.md`.
  Done in source: the Terraform root plans again and the Inflection schedule is set to 14:00 UTC @2d74e53d39 (CTO batch 95). Waits on
  ONE thing: Andrew's word on deleting nine stale gap-day objects (packet
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/PACKET_INF_GOLD_STALE_GAP_DAYS_DELETE_FOR_ANDREW_20261001.md` @3cc5b831aa;
  CTO batch 92: no seat runs it until Andrew says so). Next act after his word: run `stale_gap_days_precondition.py` to PASS, build both
  artifacts, fill the hashes, ask both halves (CTO + COO), ledger, apply in the packet's leg order.
- **Mirror release (stray key skip + second schedule)** @2e00498347, source only: its own packet AFTER the serving packet.
- **Directory search with no client firm** answers `UNEXPECTED` (`BucketUnmapped`, `infra/aws/lambda/investor-reporting/_authz/loaders.py`):
  its own packet; not started.
- **IRPT_DASHBD workstream B:** DB-b-1 complete; DB-b-3 complete @38f828d708 (`0.4.0_DS_ClientPlatform~S`; rows S10/S11 recommend
  AGAINST the 3.70 percent tolerance -- judgment for the round analysis). DB-b-2 and DB-b-4 PENDING, issued to worker
  `0.9.0_WK_IRPT_DASHBD~1`. DB-b-2's worker was spawned 16:1xZ and STOPPED by this seat at 16:25Z before its first write, so that it
  would not start a ledger, an S3 write or an artifact upload before the reboot. L10 slug to the CTO when all four are terminal.

## 3. Open acts that must survive the reboot
- Ledger entries open (all author `2.0.0_SA_COO~P`, all with ONLY leg A1 open, the live-walk acceptance read; every apply landed and
  every other leg closed, so nothing is half-landed): `irpt-adapter-holdings-gold-49f-r3-20260929`, `irpt-adapter-render-grant-kms-20260927`,
  `irpt-adapter-render-selection-20260927`, `irpt-export-async-submit-20260927`, `irpt-export-receipt-running-20260928`,
  `irpt-export-reopen-rule-20260927` (sentinels under `org/critical_paths/.open_deploys/`). Safe to hold: each closes on a read.
- Every ledger opened today is CLOSED (49F mint, NNA excusals, coerced admissions, Inflection rebuild).
- Worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275`, branch `coo-p-pr275`, head 2d74e53d39 (merged to CLOUD @40b57f928b).
  Holds two UNCOMMITTED files on purpose (committing either puts a pending plan on a live root): `lambda-source-map.json` (adapter
  `installed.py`/`holdings_gold.py` re-pinned to 89b5a85abe) and `performance/retained.tf` (read grant on the Inflection gold). The
  same diff is saved as `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/HELD_FOR_SERVING_PACKET_adapter_repin_and_inf_gold_read_grant.patch`.
- Worktree DIR `C:\Users\AndrewBerman\Desktop\wk-irpt-dashbd-1`, branch `wk-IRPT_DASHBD-1`, head 8ff819062e: clean (only the
  provisioned `portal` nested worktree shows). Re-use it for the DB-b-2 respawn (`git merge --ff-only CLOUD` first).
- Clocks: 49 Financial producer fires 07:30 America/New_York weekdays (on the OLD artifact, unchanged); the mirror fires 13:05 UTC.
  No Inflection schedule exists (never applied). Cron `1108250c` (`/canonical-drive IRPT_BCKEND`, 10 min) dies with this session.

## 4. Owed
- By this seat: nothing asked of it is unanswered (CTO 103849 answered 16:03Z). The serving packet is owed when Andrew's word comes.
- To this seat: Andrew's word on the nine-object delete (CTO printed the packet path to him 15:2xZ; batch 92 item 6 has the CTO
  reopen the disposition if no word comes).
- Signed halves outstanding: none. The draft packet asks no half yet.

## 5. Relaunch
- RESPAWN: yes -- the serving packet and the DB-b-2/DB-b-4 drain are live work this seat owns.
- First three acts: (1) `/watcher` and read the inbox; (2) read this brief, `STATUS~P.md`, and RULINGS batches 92 and 95 in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`; (3) re-spawn the DB-b-2 worker per
  `.claude/skills/dispatch/SKILL.md` Step 4 in the existing worktree, and check whether Andrew has answered the delete packet.
- `--say` hint: "Read org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_P.md, then the inbox."

## 6. Not done and not known
- STATUS~P commit b57885d3bb carries the WRONG subject (a stale message file from 09:4xZ was reused); its bytes are the 16:2xZ status.
  Not amended (shared branch); this line is the correction.
- The Inflection serving path is exercised only up to a read-only candidate run; no real authorized Inflection request was made.
- The 49 Financial row-compare covered two days (2026-09-25, 2026-09-29), not the history.
- Parked items are listed in STATUS~P.md section Parked.
