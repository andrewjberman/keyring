# Post-crash assessment: the ~O fabric (SentinelOne reaping, 2026-10-04)

- **Author:** `1.0.0_SA_CTO~O`, session ed538ac8, relaunched about 19:15Z.
- **Asked by:** `0.0.0_AB_MSTR~Z` msg 29192, on record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_191xZ_SENTINELONE_FLEET_CRASH_ASSESS_STATE_BRING_ON_CTO_Z_AND_CTO_O.md` @4f005a07db.
- **Measured at:** 2026-10-04 ~19:20-19:30Z, on site Z, CLOUD @2205340103. Sources: site-Z telemetry
  (`org/mcp/agent_telemetry/*.jsonl`), git (CLOUD and all 28 worktrees from `git worktree list --porcelain`), the
  task-order files (the last `<status>` tag in each), and `project.json`. No AWS or host reads were made.

## 1. Who was online at the reaping (shutdown 18:58:20Z)

Only `1.0.0_SA_CTO~O` was online. The other ~O seats had stopped about 15 hours earlier, at the 03:2xZ fabric stall.

| Seat | Last site-Z tool call (UTC) | Project |
|---|---|---|
| 1.0.0_SA_CTO~O | 2026-10-04 18:52:08 (send_message, msg 29187) | all ~O projects |
| 2.0.0_SA_COO~O | 2026-10-04 03:23:09 | NFRA_OPLGTW (D9) |
| 3.0.0_SA_CVO~O | 2026-10-04 02:58:33 | all ~O projects (L8/L9) |
| 2.0.0_SA_COO~AI | 2026-10-04 02:53:47 | NFRA_OPALAI (D6) |
| 2.0.0_SA_COO~MI | 2026-10-02 04:26:33 | NFRA_MCPINDEX (D9) |
| 4.0.0_SA_CRO~O | 2026-10-02 04:07:55 | none open |
| 2.0.0_SA_COO~MP | 2026-10-01 22:30:17 | NFRA_MCPORTAL (D6), PARKED |
| 0.7.0_AE_CloudOps~OG | 2026-09-29 13:33:46 | none open |
| 2.0.0_SA_COO~MS | no telemetry file on site Z | NFRA_MCPMSP (D6), PARKED |

`1.0.0_SA_CTO~O` at the crash: the 18:4xZ Andrew-direct opal_ai push was routed (record @7c670a9578, msg 29187).
`0.0.0_AB_MSTR~Z` finished it at 19:05Z (msg 29190): opal_ai DEV = PROD = e34ba403c3. This seat had nothing else in
flight. Its `/self-drive` cron was deleted earlier (log @a941eb90bf, Andrew's disk wind-down). No cron is armed now.

## 2. Per project

### NFRA_OPLGTW (D9, opal-gateway). COO `2.0.0_SA_COO~O`. Round 16, L7. GATEWAY WORK IS PENDING.

87 task orders: 77 complete, 7 superseded, 2 cancelled, and 1 open, `OG-rl-5` (pending, worker `~15`).

**A. The OG-gr-3 drain dropped its bytes from CLOUD. The repair is committed but NOT MERGED.**
- Drain `04690bcc28` (01:38Z) kept the first parent's version of 14 of the branch's 15 files. The cause was an
  index.lock collision during `--continue`.
- `2.0.0_SA_COO~O` built the repair on branch `coo-o-gr3-restore` in worktree `C:/tmp/coo-o-gr3fix`: 2 commits,
  `95ac7823d2` and `7bfacc357c` (03:07-03:11Z). They are byte-identical to the worker tip `63203de59f`. The seat
  went quiet 12 minutes later, without merging.
- Measured now:
  - CLOUD holds none of the 14 files at the branch bytes, so the R9 grain and R9a fallback are absent from CLOUD's
    gateway source.
  - No CLOUD commit has touched those 14 paths since the drain, so the merge is conflict-free.
  - The shared tree holds the same 14 files, uncommitted: 11 modified and 3 untracked
    (`tests/test_schwab_grain_r9.py`, plus `GR3_TEST_EDITS.md` and the gr-3 proof JSON under
    `deliverables/0.9.0_WK_NFRA_OPLGTW~22/`). Every `hash-object` equals the branch blob. These are the drain's leftover working-tree bytes.
    They are safe on the branch either way. Merging the branch makes the shared tree clean.
- Owed: `2.0.0_SA_COO~O` merges `coo-o-gr3-restore` through `safe-merge.sh` and confirms the 14 paths at the branch
  bytes on CLOUD.

**B. OG-rl-5 (the r16 gateway release) is BUILT, NOT DEPLOYED.**
- Release branch `rel-nfra-oplgtw-r16` @95a7dccc4d (worktree `C:/tmp/og-rel10`, 02:28Z) carries gr-3's R9 and R9a on
  live `af2d762970`.
- The order's NEVER-2 ledger `nfra-oplgtw-gateway-release-r16` is absent from `.open_deploys/`, both tracked and on
  disk, in all 28 worktrees. Under the ledger-at-start rule, no deploy leg has run.
- The `~15` worker's pre-deploy helpers are uncommitted in `C:/tmp/wk-oplgtw-15-r16`
  (`deliverables/0.9.0_WK_NFRA_OPLGTW~15/rl5_{census_host,host_prelude,paging_host,ssm}.py`, last at 03:16Z). That
  branch has no commits ahead of CLOUD.
- Live host bytes were NOT re-read this session. The last record is af2d762970 at 03:11Z. The order's step 7 ("re-read
  live; if it moved, re-cut") is the first act of whoever resumes it.
- The `~15` worker was a subagent of `2.0.0_SA_COO~O`. It died with that session and cannot be resumed as is: the
  relaunched COO re-hands the order.

**C. Stale gateway release worktrees, all ahead of CLOUD by design (release branches cut on live, not drained):**
`C:/tmp/og-rb9` and `C:/tmp/og-rb10` (detached), and `C:/tmp/og-rel9` (`rel-nfra-oplgtw-r14`, holds the deploy commit
of af2d762970). None of them is dirty. They are cleanup candidates for `2.0.0_SA_COO~O`. Nothing in them is lost work.

### NFRA_OPALAI (D6). COO `2.0.0_SA_COO~AI`. Round 2, L7. Nothing in flight.
- 40 orders: 34 complete, 3 superseded, 3 pending (`OA-e-8`; `OA-t-1` and `OA-t-3` gated on Parts A-B).
- No worktree is held. The last log (@bffa476bb4) says the close run is APPROVED and waiting for Andrew to launch it.
- Open item: opal_ai CI is red on DEV and PROD at e34ba403c3. This predates the push: ruff EXE001 on 2 files needing
  `chmod +x` (msg 29190). It is the lane's fix, and it is not gateway work.

### NFRA_MCPINDEX (D9). COO `2.0.0_SA_COO~MI`. Round 7, L7. UNDRAINED since 2026-10-02 (before the crash).
- 92 orders. 5 are issued and open: `MX-f-1` (`~25`), `MX-m-2` (`~26`), and `MX-s-17`, `s-18`, `s-19` (`~24`).
  `MX-c-1` and `MX-i-5` carry no `<status>` tag.
- Unmerged worker commits, each worktree dirty only in `.scratch/`:
  - `wk-mcpindex-r7-25`: f-1 proof, 2 commits, AC1-AC3 PASS-by-output.
  - `wk-mcpindex-r7-26`: m-2 census, 1 commit.
  - `wk-mcpindex-r7-24`: s-17 and s-18 PHASE A announces, 2 commits.
- Owed: the `2.0.0_SA_COO~MI` drain. This work is not on the gateway.

### NFRA_MCPORTAL (D6). COO `2.0.0_SA_COO~MP`. PARKED since 2026-10-01 (ruling 28068).
- Un-park condition: Andrew sets the Alyssa sitting (G-CLOSE, MP-c-1).
- 2 orders staged (`MP-c-1`, `MP-v-1`). No worktree is held. Nothing in flight.

### NFRA_MCPMSP (D6). COO `2.0.0_SA_COO~MS`. PARKED since 2026-10-01 (ruling 28068).
- Un-park condition: G-MSPID is answered, or Andrew gives the word.
- 3 orders are staged.
- Two worktrees date from 2026-09-30, before the crash:
  - `C:/tmp/ms-5`: 3 commits ahead of CLOUD, plus 2 STAGED gateway files (`deploy-to-ec2.sh`,
    `tests/test_deploy_base_guard.py`). Their content against CLOUD was not resolved this session.
  - `C:/tmp/ms-6`: opal_ai branch `wk-NFRA_MCPMSP-6-opal_ai` @32abfdb, the "5 MCPMSP commits" not in opal_ai DEV.
- Both stay parked with the project.

## 3. Open deploy entries

None for the ~O fabric. The union of `.open_deploys/` across all 28 worktrees (tracked and on disk) holds no
oplgtw, opalai, mcportal or mcpmsp entry. The one MCP-named file, `nfra-mcpindex-bd-playwright-strip.json`, exists only
on three stale branches and is absent from CLOUD, so it is closed on the trunk. The OG-rl-5 ledger has not been opened
(section 2B).

## 4. Relaunch: who the fabric needs

Andrew's test is that the D6/opal_ai COOs come back only if pending opalgateway work needs them. The test is surfaced
here, not adjudicated.

| Seat | Needed? | Why |
|---|---|---|
| 2.0.0_SA_COO~O | YES: gateway work | Holds the unmerged gr-3 repair (CLOUD lacks R9/R9a) and the undeployed r16 release (OG-rl-5). |
| 3.0.0_SA_CVO~O | YES, after COO~O | Writes the L8 slug when round 16 goes terminal. |
| 2.0.0_SA_COO~AI | No (not gateway) | Close run waits on Andrew; the CI chmod fix is a two-file lane item. |
| 2.0.0_SA_COO~MI | No (not gateway) | Round-7 drain owed since 10-02; relaunch is Andrew's call. |
| 2.0.0_SA_COO~MP, ~MS | No | PARKED on Andrew's gates (Alyssa sitting; G-MSPID). |
| 4.0.0_SA_CRO~O, 0.7.0_AE_CloudOps~OG | No | Nothing open. |

No Kimi Teams Agent control-plane gateway change was found pending. The Kimi commits since 10-01 are IRPT_BCKEND IAM
narrowing (`~P`), not gateway work.
