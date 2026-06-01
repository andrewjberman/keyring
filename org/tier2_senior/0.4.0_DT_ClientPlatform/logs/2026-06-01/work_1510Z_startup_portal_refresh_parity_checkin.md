# work 1510Z — startup + portal-refresh parity check-in

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Current State

Session start per Andrew-direct (relayed via MSTR-DIRECT `20260601T150537Z`): check in with ws CTO
(`1.0.0_SA_CTO`) — a portal refresh + new PROD deploy is anticipated. Confirm parity (verify-ec2 /
portal DEV->PROD per CLAUDE.md Rule 19), await CTO direction. MSTR note: *spawn != dispatch,
substantive TO comes from Tier-1* — so no promote without a Tier-1 GO/TO.

### Startup (XXX.md Step 1b)
- `/watcher`: was NOT REGISTERED + no watcher → re-registered (PID 33584) + launched tracked watcher.
  Watcher delivered the MSTR-DIRECT on first exit; relaunched (tracked). Inbox now empty.
- Hygiene wired: comp-graph context, session-id serial file, owned-paths hook (idempotent), headmove
  guard (present), portal pre-push hook installed.
- Primary loop armed: `CronCreate /work` job `e8969d23` (~20m cadence). `/watcher` folds inline (no
  separate ScheduleWakeup — two-loop guard).

### Parity statement (delivered to CTO, msg `20260601T151008Z`)
1. **Rule 19**: portal main tree on **DEV** (correct — never left DEV). Promote path = commit-tree
   synthesis (no checkout/force-push) ready.
2. **DEV->PROD**: DEV is a **clean content-superset** of PROD — superset-loss test EMPTY (0 PROD-only
   files dropped on promote). Pending refresh scope since last promote (`b7acadab` = ADVI_INFMVP.F1+F2,
   2026-05-28; tag `portal-v2.1.104`): **23 files, +801/-174**. Headline: ModelPortfolios.tsx (+302),
   DistributionTab (+138), modelPortfolioColors, PeersTab (+29), aum.ts, portal-proxy.ts,
   AdvisorAnalytics, types.ts — the MDPF_SCOPED P1 + ADVI_DEMOV1.010 + demo-tenant wave already on
   origin/DEV.
3. **verify-ec2** (quick git mode): 19 checked → 18 skipped (AE-owned BD/INF runners, no `source_path`
   in manifest = unassessable in quick mode), **1 "drift" = smartx-exporter** (no `deployed_commit`
   recorded; AE-owned 0.7.0/0.5.0; manifest-recording gap, **NOT** a portal-refresh blocker).

### Note
- Local portal tree has uncommitted WIP (PeersTab.tsx, HoldingsTab.tsx) — RD/DE territory, left
  untouched. Promote rides `origin/DEV`, not local tree.
- CTO is LIVE (PID 21928) working BMKAUD (FE fix fast-follow, gated on AE WS-4 ledger -> CVO); had
  offered `/frontend-dev` for Peers visual smoke. Pending diff touches PeersTab + ModelPortfolios
  heavily → flagged a visual-smoke gate before PROD as warranted (portal-closure-visual-smoke
  discipline), offered to run `/frontend-dev` on GO.

### TO queue
59 complete · 4 archived · 1 superseded · 2 staged (GO-held) · 1 pending-Andrew-UAT.
- ADVI_INFLFE.006 (staged) — GO-held on DS~A `006-data` fix landing; upstream gate.
- ADVI_SHARED.008 (staged, dispatch_held) — Phase-1 close gate; unblocks on .001-.007 all RAVC2 PASS.
- ADVI_DEMOV1.VAL-FE (pending) — assigned to Andrew (sovereign UAT), not DT.
- **0 dispatched / 0 ready-pending → no actionable TO this tick.**

## Next Steps

- **[1.0.0_SA_CTO]** Awaiting direction on the anticipated portal refresh + PROD deploy: (a) GO to
  promote DEV->PROD (full/scoped), (b) any pre-promote gate (typecheck / `/frontend-dev` / CI watch),
  or (c) hold. Will execute on GO via Rule 19 commit-tree path.
- No `[BLOCKED-ASK]` fired — awaiting CTO is the instructed posture + a normal RAVC await; the 2 staged
  TOs are GO-held on upstream gates, not DT blockers.
- `/work` cron picks up next tick (~20m); watcher tracked; will pick up CTO GO on delivery.

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| `verify-ec2.sh` (quick git mode) | 19 checked, 1 drift (smartx-exporter, AE-owned), 18 skipped | Parity sweep per startup instruction. First run failed on `MSYS_NO_PATHCONV=1` breaking jq local-file path; re-ran without it (that flag is for TF/ARN paths only). |

No `comp-pipescript`/`comp-routes`/`comp-iam` this tick — no script/route/IAM edit; tick is orientation +
parity verification + CTO check-in only.
