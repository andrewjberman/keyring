# Reboot brief -- 2.0.0_SA_COO~D -- 2026-10-01

Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`
(1.0.0_SA_CTO 103891). Written at ~16:4xZ at a checkpoint: nothing of this seat is mid-act. Read this first.

## 1. Identity
- Serial `2.0.0_SA_COO~D` (laptop, host `andrew`), base `org/tier1_exec/2.0.0_SA_COO~D/`, inbox `org/mcp/inbox/2.0.0_SA_COO/~D/`.
- Projects, all FAST (`python .tools/drive-mode.py read <CODE>`), armed by this seat:
  - `DSGN_IRPTV1` to 20:28:49Z -- Investor Reporting front end (22 paths under `portal/src/pages/InvestorReporting` and three shared components). State: `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md`.
  - `IRPT_DASHBD~D` to 20:28:50Z -- the dashboard's `tabs/reporting` and `dashboard`. State: `org/missions/D9/IRPT/IRPT_DASHBD/STATUS~D.md`.
  - `NFRA_TRNSPT` to 19:02:48Z -- the mail/transcripts database round (`data/transcripts`, the project tree). State: `org/missions/D9/NFRA/NFRA_TRNSPT/STATUS.md`.
- Loop: cron 6e5767b6 fires `/canonical-drive DSGN_IRPTV1 once` every 10 minutes (LIVE_ARMS row). A reboot ends it.

## 2. Where the work stands
- DSGN_IRPTV1: items 59-62 landed today; portal origin DEV `2bb367ef` (item 62: row statuses three at a time, the pressed request first; CI green run 36883137558; re-walked, press to sections 10.2 s). Next: nothing front-end-only is unblocked. Records `REAL_RUNS_20261001.md` sections 1-10.
- IRPT_DASHBD F: words and contract reads landed (item 59 `2879d65b`). Next: plan item 5 (the per-account switch in `tabs/reporting/ReportingTab.tsx`) waits on 2.0.0_SA_COO~P's TO-DB-b-2 (served series file) and TO-DB-b-4 (read route), both `pending`.
- NFRA_TRNSPT: one admitted real message landed route -> bronze -> silver (record `deliverables/2.0.0_SA_COO~D/R3_REAL_RUN_20261001.md`); the listing route checked from the laptop 4 of 4 and the gateway pull made admitted-only (@33176972f0). Next: one `python data/transcripts/scripts/outlook/pull.py --gateway --days 7 --apply` as the positive arm (dry run 16:20Z: 13 listed, 1 admitted), then its schedule, which is a CTO placement.

## 3. Open acts that must survive the reboot
- Ledger entries in `org/critical_paths/`: NONE held by this seat (all 21 `.open_deploys/*.json` read at 16:3xZ; none names this seat).
- Worktrees: NONE owned. This seat works in the main checkout (`ajb_workspace`, `portal` on DEV). Portal tree: no tracked edit. A test run can regenerate `portal/src/pages/InvestorReporting/contracts/wire/*` on disk; restore it with `git -C portal restore --worktree -- src/pages/InvestorReporting/contracts/wire`, never commit it.
- The UI walker account: this seat DISARMED at 16:30:17Z (login refused after). Site Z armed it at 16:33Z (103909)
  and DISARMED it at 16:45:38Z (103917): the account is free; a walk still posts its ARM request first. Walks run one device at a time: before any walk send 0.0.0_AB_MSTR an ARM request and wait for the relay of site Z's ack; send a DISARMED line after (CTO 103599).
- The dev server on 5174 (bun dev:live, detached) dies with the reboot: restart it from `portal` with `bun run dev:live --port 5174`.
- Clocks: none of this seat's. Workspace commits are LOCAL on CLOUD (the push is 0.0.0_AB_MSTR's).

## 4. Owed
- To 2.0.0_SA_COO~Y (103862): the Multi-Comp walk's verdict -- sent with this brief (REAL_RUNS section 10).
- To 1.0.0_SA_CTO: nothing open. E4 and item 62 reported (103812 answered 15:45Z).
- Owed to this seat: TO-DB-b-2 / b-4 (2.0.0_SA_COO~P); nothing else.

## 5. Relaunch
- RESPAWN: yes. Three FAST leases are live and the IRPT front end takes work the hour another lane lands.
- First: read this brief and `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md`; `/watcher`; read the inbox.
- Second: read the three leases (re-arm any that lapsed, on its present surface, citing CTO batch 84 item 6 or batch 82); restart 5174.
- Third: if 2.0.0_SA_COO~P's b-2/b-4 have landed, build plan item 5; else run the NFRA_TRNSPT `--apply` pull (one run, record it).
- E7 (1.0.0_SA_CTO 103914, RULINGS batch 98 items 1-3 @29a6581479): the Multi-Comp arm is NOT live until a served route names
  its comparisons. 2.0.0_SA_COO~Y serves the names first (from the request's frozen keys and the catalogue's labels). This seat's
  part, the tick that route serves them: show the names on the opened request (`tabs/analysis/OwnedRequestHistory.tsx`), land
  on DEV, then ONE re-walk of `REQ-a1d9abc0bc037ea3d9e4a7ed` with `--expect-text` for both names; 1.0.0_SA_CTO calls it live.
- `--say`: read `org/tier1_exec/2.0.0_SA_COO~D/REBOOT_BRIEF_20261001_2.0.0_SA_COO_D.md`, then the inbox `org/mcp/inbox/2.0.0_SA_COO/~D/`.

## 6. Not done and not known
- The Multi-Comp report does not name its two comparisons on the page (0 of 2 names in the dialog); a reload drops the client selection, so "kept on a reload" was not read. Not decided whose change either is.
- The 14 flagged words of the first real mail row: counted by shape, never read.
- The deployed site's request timing was never measured; all timings are the local dev build.
