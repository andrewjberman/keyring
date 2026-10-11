# 1.0.0_SA_CTO -- post-restart: state compile, half-done deploys, residue (2026-10-10 20:15Z -> 20:40Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DEPLOY

Order: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_201xZ_RESTART_COMPILE_STATE_DEPLOYS_THEN_RESIDUE_THEN_INFORM.md
(committed @5404f51097). Restart point read: logs/2026-10-10/session_close_1800-2007Z.md @1d57c009f2.

## 1. Laptop state

- Seat: registered LIVE (PID 18680), inbox watcher armed (script pid 2692), inbox empty, delivery ledger 0 rows since 20:00Z.
- Live seats on the laptop: 0.0.0_AB_MSTR and 1.0.0_SA_CTO only. Two Codex shells (PIDs 15472, 22712) are running with no
  serial bound. They are session shells and were not touched.
- Crons in this session: none. /self-drive is NOT re-armed. The session-close note said a successor may re-arm it; Andrew's
  order puts state, deploys and residue first. It stays off until he says otherwise.
- Worktrees: 1 (the shared checkout). No linked worktrees, so there is no worker-branch ledger to union.
- Open deploy ledgers in the tree: 28, of which 1 is laptop-device (nfra-trnspt-a18, HELD-SOVEREIGN-GATED: apply SUCCESS
  2026-10-09, gate = the two status-only probes, one of them dell2's). Nothing laptop-owned is half-landed.

## 2. Half-done deploys and risky work (all 12 OPEN ledgers read, the artifact measured where the risk was live)

| Ledger (device) | Measured | Verdict / act |
|---|---|---|
| healgap-r2-act3-induced-partial-repair-20261010 (dell1, 2.0.0_SA_COO~G1) | EventBridge target `cot-rebalancer-runner-daily` STILL had `induce: drop-feed:rebalancer_accounts`; 06:00Z Oct 10 bucket 4 invocations / 3 errors | **ROLLED BACK by this seat at 20:28:38Z**: PutTargets `{"mode":"pull"}` (the ledger's own rollback, byte-equal to TF `cot_rebalancer_runner.tf:194`), read back, FailedEntryCount 0. Leg L3 closed @5404f51097. The 12:00Z restore deadline (MSTR~DELL1) had been missed because dell1 was down. L2/L4/L5 (PARTIAL read, FWD-3 repair, satellites) stay with G1. The Oct 10 run is failed/partial and its repair is G1's. |
| amgt-resapp-r88-mm4-scoped-api-dell1 (dell1, ~RA1) | live CodeSha256 `KlosR/ap8O...` (LastModified 2026-10-09 22:55:03Z), not the rollback b7Lj1J; 334 invocations / 0 errors / 0 throttles since | LANDED, not rolled back. Record commit 4607adbfcd (`ci: record deploy harvest`), served read daaa6f76d8 (C1, /10 SERVED). Only the 12 ledger legs are unclosed. RA1 closes them on dell1's return. |
| irpt-ycdgen-served-read-20261009 (dell2) | W2 restored svc to cottonwood (independent read in ledger). Secret `irpt/svc-irpt-analysis/password` resource policy LIVE == BEFORE (2/2 statements set-equal), != ADD | No open grant. S+/S- legs are a records gap: the laptop CTL windows (TO-APPLY-30) opened and closed, and the sr1 ADD never landed in time (G2 drive log). dell2 closes the ledger. |
| irpt-anlreq-r1-irpt-status-rev5-20261009 (dell2) | R1 failed pre-apply; live = rev 3; irpt-status Errors 0 since Oct 9 18Z | Safe: nothing applied. Close as STOPPED on return. |
| irpt-anlreq-t1-commentary-store-and-lambda (dell2) | Step A applied (5 added, 0 changed); A2/B not run | Dormant infrastructure, nothing serving it. Owner on return. |
| irpt-anlreq-r1 (first apply), irpt-fwd14, tckt-vnext hop-e, nfra-mcpindex r8 (site Z) | Only prechecks or nothing logged; fwd14 states nothing was written | No live act; owner on return. |
| harvst-bs3 / harvst-bw1 (site Z) | runner armed/re-pinned; verify legs open | Intended continuous runner; owner on return. |
| mdpf-demque-zq-t24, mdpf-sechist x2 (site Z / dell1) | scheduled one-shot / verify-only legs | Intended; owner on return. |

## 3. Residue on this box

- Terraform provider temp files: 6 removed, 0.88 GB freed (23.23 -> 24.10 GB free). Merged/orphan worktree pools: 0.
- Orphan processes (`kill-maint.ps1 -Mode scripts`): 0 kill targets.
- 10 open-deploy ledgers on REMOTE boxes carried only this device's 07:24Z red-scan stamps (`last_red_at`, and on 2 of them
  `last_held_nudge_at`; every other diff line was checked as 0). They were restored to HEAD so they cannot conflict with the
  owners' writes at integrate. The diff is kept at `archive/root_residue_20261010/laptop_red_stamps_20261010T0724Z.patch`
  (7,389 bytes). `git stash` was refused by the shared-worktree gate, so a patch file was used instead.
- Root-level untracked scratch (Sep 9 -> Oct 9, no owner in git) MOVED, not deleted, to `archive/root_residue_20261010/`:
  `--help`, `.runtmp_os20_wait.sh`, `TX-p-1.baseline.txt`, `TX-v-1.expected-cases.txt`, `x.json`, `y75_evidence.json`,
  `.scratch_sprint/`, `.scratch_m84_bk/`.
- Left as found (other lanes' files): the append-only audit logs (MSTR/integrate), LGIC_BLANKFIX worker round-5 files,
  the CVO NFRA_CTLPLN grades deliverable, the portal submodule pointer, and ~280 other untracked files under org/, infra/,
  docs/, data/ and deck_generation/.

## Next Steps

1. [2.0.0_SA_COO~G1, dell1] HEALGAP R2 act 3: L2 PARTIAL read of 2026-10-10, L4 FWD-3 repair, L5 satellites; the daily
   input is already back on pull.
2. [0.7.0_AE_CloudOps~RA1, dell1] close amgt-resapp-r88 legs citing 4607adbfcd and the live KlosR hash.
3. [dell2 owners] close irpt-ycdgen (S+/S- records gap), irpt-anlreq rev5 (STOPPED), and decide on t1 step A.
4. [Andrew] /self-drive re-arm is held for his word.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| audit-archive-invoker.py | WARN | 2 findings: agent-spawn-audit.log non-append (pinned/adjudicated), stale baseline (advanced now) |
| comp-find | PASS | `last_red_at` writer = .tools/deploy_ledger.py; `laptop secret` 5/47,831; cot target TF 5 hits |
| comp-rail | WARN | 1 denial (census piped to tail); re-run with --limit |
| deploy_ledger.py close-leg | PASS | HEALGAP L3 |
| kill-maint.ps1 / cleanup-disk.ps1 | PASS | 0 orphan processes; 0.88 GB freed |
| aws events / lambda / cloudwatch / secretsmanager reads | PASS | one resource each, read back after the one write |
