# The device-death scan: Windows Terminal crashed under a leaking endpoint-protection service and took every Claude seat -- 0.0.0_AB_MSTR

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE

**Date:** 2026-09-07 (window 02:11Z -> 02:50Z; 2026-09-06 22:11 -> 22:50 US Eastern)
**Task Order:** ad-hoc; Andrew-direct at this terminal ~02:3xZ: *"My device died at some point and took down all running
agents, I need you to scan device logs and see where we left off"*. Standing seat charter (device/fabric infra manager).
**Status:** SCAN COMPLETE, reported to Andrew. No seat relaunched, no fabric act taken -- the default-OFF rule stands and the
relaunch is his call because the memory condition that killed the fabric is STILL PRESENT.

---

## Objective

Determine from device-side evidence WHEN and WHY the fabric died, and WHERE every seat left off, so Andrew can decide the
relaunch. Deliverable = the assessment; no repair unless asked.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| Windows System log (PowerShell `Get-WinEvent`) | ids 41/1074/6005/6006/6008/12/13, 7 days | PASS | NO reboot, NO power event since the 2026-09-02 21:54 boot -- the machine never died; the terminal did |
| Windows Application log | ids 1000/1001, 3 days | PASS | dwm.exe fault 23:58:36 (dwmcore.dll, 0xc00001ad) then WindowsTerminal.exe APPCRASH 23:59:00 (0xc0000005), 2026-09-05 local |
| Resource-Exhaustion-Detector (System 2004) | 3 days | PASS | 22 low-virtual-memory diagnoses 12:19 -> 23:57 on 09-05; top consumer EVERY time `EPProtectedService.exe` pid 6444, 21.4 GB -> 23.4 GB |
| `Win32_OperatingSystem` / `Get-Process` | memory now | WARN | 93% physical used, commit 51.9 of 62.3 GB; pid 6444 working set 8.6 GB -- the condition is LIVE at scan time |
| `Win32_Process` | claude/codex/python/bash start times | PASS | one claude.exe (this session, 22:11); Codex runtimes from 09-04 and 09-05 survived; CTO~Y relaunched 22:13 |
| `Get-NetTCPConnection` | ports 7800/53041/58294/58660 | PASS | broker pid 28260 (09-04) alive on 7800; CRO~Y app-server 53041 NOT listening -- HOLLOW seat (heartbeat LIVE, runtime dead); ~Q and CTO~Y listening |
| telemetry last-row census | `org/mcp/agent_telemetry/*.jsonl`, 11 files touched since 09-04 | PASS | last rows: CloudOps~W 03:59:02Z, WK_CLDGRPH~2 03:58Z, CTO 03:56Z, CVO 03:56Z, COO 03:41Z (09-06) -- the death instant per seat |
| git | last commit per author since 09-03 (1,360 commits); `fetch`; `rev-list --left-right`; worktree status x3 | PASS | HEAD 7d81a9c25f 31 ahead / 0 behind origin/CLOUD @58adeff90c; origin/SITEZ @14a7c793e2 3 ahead / 256 behind; merge-base ea1835863e |
| `.tools/to-check.py --all` | | PASS | 86 active TOs / 42 projects; the two mid-execution projects: NFRA_OUTSET OS-s-18/19 -> CloudOps~W; NFRA_CLDGRPH D-7/D-8 -> WK~2 |
| `.tools/fabric-projects.py` / `fabric-check.py --agents` | | PASS | 17 HOT; 1 live agent (this seat) |
| `.tools/deploy_ledger.py list` | | PASS | 4 OPEN PAST-WINDOW + 2 HELD-STALE + 1 unindexed BYPASS, all pre-dating the crash by 69-138 h |
| `.tools/aws iam get-role-policy` (rail-checked: resource-level question comp-iam cannot model) | estate-report-runner-role / estate-report-runner | PASS | APPLIED policy: 11 resources, `outset/*` 0 hits; positive control `kuzu_nessie_db` present -> the uncommitted iam.tf grant is DESIRED-NOT-APPLIED, nothing half-landed |
| `get_delivery_state` / `ack_messages` | since 09-04T20:00Z | PASS | 23 rows, 22 READ, 1 OFFER-EXHAUSTED (94433) opened and acked |
| `agentbus-sqs.sh` | device, peek x2, watch (Monitor blc7ia2tc), send x2 | PASS | 2 site-Z messages consumed at arm, both acked (438c9186, 27636412) |
| audit-archive-invoker | startup A.2 | 3 findings | the known STALE-BASELINE plus 2x `INTEGRITY/ERROR-FAILCLOSED` baseline-missing on the two override audit logs -- surfaced, not chased |

**What worked:** asking the Application log and the Resource-Exhaustion-Detector after the System log said "no reboot" --
"device died" was the symptom Andrew saw; the device never went down. The telemetry last-row census gave a per-seat death
instant that no log file could (the seats died mid-turn and wrote no log). **What failed:** the first seat-log extraction
sorted by mtime and picked site-Z lane files that the reconcile merge had re-stamped, and printed through cp1252 -- replaced by
the telemetry census and by reading the commit bodies. `check-inbox` is not on the harness PATH (the `.tools` PATH entry is
Windows-form); invoked by path. **Gap found:** the inbox-watch and agent-poller both heartbeat a seat whose Codex runtime is
dead (CRO~Y), and CTO~Y's every-5-minute sends to it land as `IDENTITY_SEND_UNVERIFIED` rows -- a hollow seat reads LIVE on
every producer-side probe, exactly the memory entry's shape.

---

## Work Completed

1. **Startup A-E, `/watcher`, `/agentbus`, `/integrate` assess-only** -- registered PID 26616; inbox Monitor `b9ec1y9mb`
   (parent-tied pid 2021); bus consumer `blc7ia2tc` (device laptop, both queues depth 0 after drain); divergence measured above.
2. **The death, dated and caused.** 2026-09-05 23:59:00 local (2026-09-06 03:59Z): WindowsTerminal.exe access violation one
   second after a dwm.exe fault, both under a low-virtual-memory condition Windows had been diagnosing every few minutes since
   12:19 that day, with `EPProtectedService.exe` (pid 6444) the top consumer at 21.4 -> 23.4 GB virtual. Every Claude seat was a
   tab of that terminal. The Codex seats (separate console hosts) and the broker (detached python, pid 28260) survived. Last
   fabric commit 23:54; the D-7 hand-off merge in the worker worktree 23:55:56; dark until this launch 22:11 on 09-06.
   **CORRECTION (02:5xZ, same session, on the HUD log line at 03:55:56Z):** that hand-off merge `c8d93dddfd` was run by
   `2.0.0_SA_COO~A` (`export OPAL_AGENT_SERIAL=2.0.0_SA_COO~A; git -C $W merge CLOUD -m ...`), a bare `git merge` that git
   stamped with the default author "Andrew Berman". The first draft of this log and of the Desktop report called it Andrew's
   own commit; both are corrected. Also measured after the first draft: `/tmp/os18plan.out` (42,141 B, written 23:59:00 ET)
   opens with `fatal error: runtime: cannot allocate memory` -- the Terraform plan CloudOps~W was running died of the same
   exhaustion in the same second as the Terminal.
3. **Where each seat left off** (from commits + telemetry, since no seat logged the death):
   - `2.0.0_SA_COO~A` (NFRA_CLDGRPH): L6 amendment of TO-CG-D-7 for PASS 4 @7d81a9c25f (23:54) -- D7-AC1 passes, D7-AC2 fails on
     the world (3 of 30 consumers open a local DB; `kuzu_cost_enrich.py` has no repoint target), order cannot go terminal until
     the CTO's disposition ruling. Worker `0.9.0_WK_NFRA_CLDGRPH~2` died at 03:58Z on `/c/tmp/wk-cldgrph-2-d7` @c8d93dddfd
     (the COO~A lane's hand-off merge, see CORRECTION above; nothing committed after; untracked `tsgraph_detect_ledger.json`
     + a gate audit log). D-8 queued behind.
   - `2.0.0_SA_COO` (NFRA_OUTSET): round-2 issuance @37b2a19129 (23:40) -- OS-s-18 (the publish) and OS-s-19 (the S3 deploy,
     NEVER-2 cell) seated in order on `0.7.0_AE_CloudOps~W`; dep_stage EXECUTING.
   - `0.7.0_AE_CloudOps~W`: mid-OS-s-18 at 03:59Z -- the `infra/aws/terraform/estate-report/iam.tf` `outset/*` GetObject grant
     is edited and UNCOMMITTED in the main tree, and NOT applied (measured). `docs/briefs/cmpaws-iam-census-20260906.json`
     (23:45) is its comp-iam refresh, untracked.
   - `1.0.0_SA_CTO`: adjudication CG-s-8 scope @622ffb9631 (22:56); owes NFRA_OUTSET's L10 read of the CVO slug and the D-7
     disposition ruling (delete vs declare-dead for `kuzu_cost_enrich.py`).
   - `3.0.0_SA_CVO`: C-S18 @a51c092fa2 (23:08); waiting to grade D-7/D-8 at their drains and the CTO's OUTSET L10.
   - `4.0.0_SA_CRO`: last act 15:00 local (brief amendment @fd9b987a87); idle at death. `2.0.0_SA_COO~B`: ETFS_GUARDRAIL at
     ROUND_CLOSE, nothing to fire until the 2026-10-01 read.
   - Codex: `1.0.0_SA_CTO~Y` relaunched 22:13 tonight and sent the dead COO two orders-wanted messages on PREQ-04 (22:24,
     22:35); `4.0.0_SA_CRO~Y` is HOLLOW (heartbeat pid 47132 live, app-server 53041 dead -- CTO~Y's own message cites its
     memory-allocation failure); `0.8.0_AE_CloudComp~Q` alive since 09-04.
4. **Andrew's relayed question answered** (bus 04f103bd from `0.0.0_AB_MSTR~Z`): the laptop CLI is authenticated as
   `andrew@goldengate.dev` by OAuth subscription login, no API key, no Bedrock/Vertex -- sent as the ack (27636412), no credential.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Report, do not relaunch | Andrew asked for a scan; the memory condition that killed the fabric is still live (93% used, 8.6 GB in one service), so a fleet relaunch now would re-run the failure; the reboot or service restart is his call |
| Treat the `iam.tf` edit as DESIRED-NOT-APPLIED, not half-landed | measured on the applied plane with a positive control; nothing to roll back |
| Ack the two bus messages and answer the relay in the ack | RAVC on consumed messages; the question was Andrew's own and the answer carries no secret |
| Leave the D-7 worker worktree and the reconcile worktree in place | both hold state their owners will read at relaunch; removal is a recursive delete and not this seat's without a word |

---

## Files Modified

This log only (this commit). Bus: two acks sent. Broker: 94433 acked.

---

## Blockers

- **AT ANDREW:** the relaunch, and the memory condition beneath it (`EPProtectedService.exe` at 23 GB virtual / 8.6 GB working
  set; the leak recurs from a 09-02 boot inside ~2.5 days). Nothing at this seat is blocked by another seat.

---

## Current State

Live on this device: this seat, the broker (pid 28260), `1.0.0_SA_CTO~Y`, `0.8.0_AE_CloudComp~Q`; `4.0.0_SA_CRO~Y` hollow. Dead:
every Claude seat (CTO, COO, COO~A, COO~B, CVO, CRO, CloudOps~W, the CLDGRPH workers). Local CLOUD @7d81a9c25f, 31 ahead of
origin (LD-0522 hold), 0 behind; the uncommitted `iam.tf` grant and the two worker worktrees are the only in-flight artifacts.
Site Z @14a7c793e2 is 3 log commits ahead, 256 behind, idle by its own word.

---

## Next Steps

1. **[Andrew]** Clear the memory condition (restart the endpoint-protection service or reboot), then say the word on the relaunch
   order. Recommended order: `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `2.0.0_SA_COO~A`, `3.0.0_SA_CVO`, `0.7.0_AE_CloudOps~W`, `4.0.0_SA_CRO`;
   relaunch `4.0.0_SA_CRO~Y` via `ajb2` (its runtime is dead); COO~B only when the October read is due.
2. **[`2.0.0_SA_COO~A`]** Re-spawn the D-7 pass-4 worker on `wk-cldgrph-2-d7` @c8d93dddfd; the CTO's disposition ruling on
   `kuzu_cost_enrich.py` gates the order's close.
3. **[`0.7.0_AE_CloudOps~W`]** Resume OS-s-18 from the uncommitted `iam.tf` edit (commit, `safe-apply`, prove the RED arm), then OS-s-19 under its NEVER-2 ledger.
4. **[`2.0.0_SA_COO`]** The two PREQ-04 messages from `1.0.0_SA_CTO~Y` (22:24, 22:35) want a bounded writer-of-record order or a hold.
5. **[`0.0.0_AB_MSTR`]** The push window on Andrew's word (31 ahead); the D-7 worker worktree and `C:/tmp/mstr-reconcile-20260904` cleanup on his word.

---

## What is UNVERIFIED, stated because a uniformly clean log is the one to distrust

- The causal chain memory-exhaustion -> dwm fault -> terminal crash is the ordering of three logs on one clock, not a debugger
  trace; the correlation is exact to the minute and repeated by CTO~Y's independent read, but it is a chain of timestamps.
- CRO~Y's app-server death is read from a closed port and CTO~Y's message, not from its own stderr.
- Whether the D-7 pass-4 worker had begun any act before dying is unknowable: its worktree carries only untracked scratch and
  its telemetry ends at 03:58Z.
