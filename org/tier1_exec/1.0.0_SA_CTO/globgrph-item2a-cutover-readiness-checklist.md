# GLOBGRPH Item-2a First-Cron — CTO Cutover-Readiness Checklist

**For:** NFRA_GLOBGRPH first nightly derive-runner cron, **06-10 02:00Z**.
**My role:** architecture reviewer (GLOBGRPH pod) — AE_CloudOps runs the cron + RAVC2s; I give the instant endorse/reject against this checklist.
**Pre-staged:** 2026-06-09 (COO drive request).

## What fires at 02:00Z

Item-2a = ECS **Fargate** task (`globgrph-derive-runner`, 1 vCPU / 2 GB), triggered by EventBridge rule `opal-globgrph-derive-runner-nightly` (`cron(0 2 * * ? *)`, ENABLED). Flow: pull ECR `opal-globgrph-derive-runner:latest` → **full account-wide `comp-aws derive`** (read-only describe across all resource classes) → write Iceberg tables to S3 warehouse `opal-313476888478-globgrph` → **one atomic Nessie commit on `main`** + **`audit-baseline-{date}` tag**. Logs → `/ecs/globgrph/derive-runner`.

## Which ACs apply to a FIRST run (vs later)

This is the **establishing baseline (commit N)** — so apply the AC subset that doesn't require an N-1:
- **APPLIES:** AC2 (atomic versioning), AC4 (0-untyped, absolute bar), AC1 (deterministic snapshot — at least no nondeterminism red flags), AC6 (cost/runtime discipline).
- **DEFERRED to 2nd cron / later phase:** AC3 (diff N→N+1 — needs a prior baseline; verifiable 06-11), AC5/AC7/AC8/AC9 (Kuzu/Cypher cross-layer traversal — Item-3, post-Item-1; not this run's bar).
- **Framing for COO/Andrew:** a clean first cron = **Wave-2 Item-2a landed + baseline established**, NOT GLOBGRPH closeout (AC7 closeout bar explicitly requires demonstrated versioning + Cypher on real unioned data — a later milestone).

## Verification checklist (run against AE's RAVC2 evidence)

1. **[Task ran to success]** ECS task for the 02:00Z run reached `STOPPED` with **exit 0** (container `derive-runner`), not a `*Failed`/timeout/OOM stop reason. — `ecs describe-tasks` stoppedReason + container exitCode; or AE's cited task ARN.
2. **[No OOM / time blowout]** Task ran in **minutes**, well under any cap, peak memory < 2 GB (the 1vCPU/2GB sizing held for a full account-wide derive). If it brushed 2 GB or ran long → flag a sizing-headroom note even on success (the account grows).
3. **[Logs clean]** `/ecs/globgrph/derive-runner` for the run: **no `Traceback`, no `AccessDenied`/permission errors, no throttle/`Rate exceeded`, no partial-derive warnings.** A permission-denied on any describe call = an incomplete graph even if the task exits 0 → REJECT (the account-wide describe IAM in item2a.tf must cover every class touched).
4. **[Nessie commit — atomic, on main]** Exactly **one** new commit on `main` for the run; it is **atomic across all Iceberg tables** (no half-written graph readable on `main`) — AC2. Verify the commit hash + that all expected tables advanced together.
5. **[Baseline tag]** `audit-baseline-{2026-06-10}` (or run-date) **tag created** and pins the commit from (4). The tag is the source-of-truth baseline pointer.
6. **[AC4 — 0 untyped, ABSOLUTE]** `graph_metrics.untyped == 0` for the commit. **Any** untyped node or edge = run FAILS (hard bar, carried from CMPAWS §4). Confirm the metric is emitted and is exactly 0 — not absent (absence ≠ pass).
7. **[Counts plausible]** Node/edge counts are non-zero and in the expected order of magnitude for a full account-wide derive (sanity vs the CMPAWS Wave-1 census — not 0, not absurdly low = silent partial; not wildly high = double-count). Ask AE for the node/edge totals by class.
8. **[Warehouse written coherently]** S3 `opal-313476888478-globgrph` has the Iceberg metadata + data files for the commit; the Nessie ref resolves to a coherent table set (ties to AC2).
9. **[AC6 — cost/footprint]** Idle footprint unchanged (warm Nessie Fargate + DynamoDB + S3 only); the derive task is ephemeral (stops after the run, no lingering task). Register the run cost/runtime in the NFRA scorecard (§5a) if AE hasn't.

## Endorse / reject rule

- **ENDORSE (P1/Wave-2 Item-2a complete):** 1-9 green, with AC4 untyped==0 and AC2 single-atomic-commit+tag as the two hard gates. Note explicitly that AC3/AC5/AC7 remain for later milestones — this endorsement is "first baseline landed correctly," not closeout.
- **REJECT (specific gap):** any of — task failed/OOM/timeout; any AccessDenied in logs (incomplete derive); >1 or non-atomic commit; missing/!=0 untyped; missing baseline tag; implausible counts. Tie the gap to the AC + the exact evidence line.

## Notes
- First-run-specific watch: the **IAM describe coverage** (item2a.tf `DeriveRunnerAccountDescribe`) is the most likely first-run failure — a class the derive touches but the policy doesn't grant returns AccessDenied → silent partial graph that still exits 0. Item 3 (logs) is the catch; do not endorse on exit-0 alone.
- Reconciliation discipline (PRD §3): once Item-2b incremental is live, a nightly-2a baseline that diverges from accumulated-2b commits is a **2b-correctness signal** — not in scope for this first 2a run, but the baseline this run establishes is what that future check measures against.
