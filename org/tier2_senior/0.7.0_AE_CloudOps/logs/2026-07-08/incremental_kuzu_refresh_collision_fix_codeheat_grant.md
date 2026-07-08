# Incremental kuzu-projection refresh (92x, Andrew-directed) + collision-fix re-derive + code_heat grounding + leg-5 grant

**archetype:** MIXED (primary IMPLEMENT; secondary DEPLOY, DIAGNOSE)
**agent:** 0.7.0_AE_CloudOps · **date:** 2026-07-08 · **window:** since coupled_04_pass_c3_materialize_promote_emit.md (~1845Z) -> ~2030Z

## Summary

Five threads delivered + closed. Headline: Andrew observed the graph was being re-processed too heavily; grounded it to TWO layers (Fargate full-derive + the LOCAL kuzu projection full-rebuild-on-every-HEAD-advance) and fixed both -- the local one via an incremental delta-refresh (92x), the durable-discipline one via a "batch non-urgent graph changes onto the nightly" rule (memory saved).

## Work delivered

- **Incremental local kuzu-projection refresh (Andrew "go now"; the local analog of the cloud incremental_updater).** `kuzu_incremental_refresh.py` (f8e7f6aab): diff HEAD-Iceberg vs the live kuzu DB (key + snapshot_ts) -> MERGE changed/added nodes + DETACH-DELETE removed nodes + edge add/del, on a file-copy + _canonical atomic-swap; large-delta/error/cold-start fallback to full; count-guard; subprocess-isolated (Arrow-S3 finalize). Wired into _canonical (rebuild_fn prefers it), flag-flipped ON in the comp-kuzu wrapper (3d98c9ca4). MEASURED 92x: incremental 3.9s vs full 356.7s (~6min) on the live canonical DB. CTO arch-gate GO 195732Z + RAVC ACCEPTED (content-exact adversarial proof "the standout").
- **Drift-vector hardening (CVO~B code-review).** Vector 1 (node ts-inequality) CLOSED by producer guarantee -- source-confirmed both writers stamp snapshot_ts=batch_ts=int(time.time()*1000) fresh per run (incremental_updater :470/:683, derive_runner :1815). Vector 2 (edge SET-field drift) ELIMINATED (3496e6e8e): edge diff now detects layer/snapshot_ts changes. Reconcile-oracle CAPABILITY built (aebe0d0a6): content-exact all-fields diff. CVO~B CERT: TIER-1 (correctness+drift-safety) CERTED; Tier-2 (standing-oracle wiring) = closing condition.
- **Collision-fix re-derive (task #9, CTO-gated prereq to N>1 C3).** DS~B regenerated the C3 node_id (system:firm-conditional-display -> :25558d98, f875bc854). Rebuilt derive image + re-derived (ledger motif-c3-collision-fix-rederive CLOSED 3/3): C3 id :25558d98 live, old bare id ABSENT (no orphan), 36 CONTAINS resolve. CVO~B re-cert PASS.
- **code_heat ~9d staleness (COO~B Class-2 route) -- MECHANISM grounded.** NOT a stopped refresh: parquet re-emits daily (S3 14:45Z) but from a git checkout frozen at 06-29 (repo_head_sha=15e3a25b9c9a). Stale-checkout live-read. 0.5.0's hypothesis disproven. Emitter-fix routed to 0.8.0~B; FRESHGUARD-coverage gap handed to 0.7.0~B (leg-5).
- **github-token IAM grant (unblocks 0.7.0~B leg-5 v2).** Same-region GetSecretValue on github-token-6FYoJ6 for opal-globgrph-freshness-alarm (5b25baebf, ledger CLOSED 3/3, live get-role-policy verified). 0.7.0~B's design-doc us-east-2 was a stale grep -> no replica needed (caught by asking for live ARNs).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-kuzu` | baseline + exercise-confirm + live BEHIND->incremental verify + reconcile checks | PASS (also the surface being optimized) |
| `comp-glob`/`comp-grep` | locate ingest producer, freshness-alarm role TF, code_heat producer/schedule | PASS |
| `commit-gate.sh` | every .py edit (kuzu_incremental_refresh, _canonical, tests) | PASS (caught unused s3 var + test E401/E70x) |
| `safe-commit.sh` | f8e7f6aab / 3496e6e8e / aebe0d0a6 / 3d98c9ca4 / 5b25baebf | PASS |
| `deploy_ledger.py` | collision-fix (3/3) + github-token grant (3/3) | PASS |
| `terraform plan` / `safe-apply.sh` | targeted github-token grant (1-add, 0-diff re-plan) | PASS |
| live-AWS (Rule 22a) | codebuild/ecr/ecs/cloudwatch (collision re-derive) + iam get-role-policy (grant, rail-marked -- Rule 22a fresh-IAM exception) | PASS |

**What worked:** the adversarial content-exact exercise-confirm (corrupt-behind-DB -> byte-exact vs full-load) proved self-heal, not just delta-apply -- CTO called it the standout. Asking 0.7.0~B for live ARNs caught a stale-grep us-east-2 before building a needless cross-region replica. **What failed:** MSYS mangled the leading-`/` CloudWatch log-group (fixed via PowerShell); safe-apply needs the explicit `apply` subcommand. **Gap:** comp-which routes a code-LOCATION question to a graph tool (minor).

## Deployment Sequence + Verification (AE)

- **Incremental-refresh flip:** commits f8e7f6aab (module) -> 3496e6e8e (Vector-2) -> aebe0d0a6 (reconcile) -> 3d98c9ca4 (flag-on comp-kuzu wrapper). Verified: 92x measured, content-exact adversarial + live BEHIND->incremental catch-up (pin re-stamped), self-test 34/34.
- **Collision-fix re-derive:** CodeBuild c6d83dc7 -> ECR :latest c98f48bf -> ecs run-task efb3a9f0 exit=0 (C2C3_MOTIF_INGEST 7n/36e/0-unresolved, marker f647120374) -> comp-kuzu :25558d98 present + old absent.
- **github-token grant:** commit 5b25baebf -> safe-apply 1-add -> 0-diff re-plan -> live get-role-policy GithubTokenRead=GetSecretValue on github-token-6FYoJ6.

## Blockers

None. Remaining work is coordination-gated or non-urgent (see Next Steps).

## Current State (handoff)

- **comp-kuzu is now RELIABLE (FinalizeS3 fix, prior) AND FAST (incremental refresh, 92x, flag-on).** Every agent's BEHIND query stitches the delta instead of a ~6-min full rebuild. Flag: GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1 in .tools/comp-kuzu; unset reverts to full-only.
- **Nightly full-derive overwrite trips the large-delta fallback -> full local rebuild = daily ground-truth reset** (no separate mechanism).
- **C3 layer LIVE at :25558d98** (collision-safe). N>1 C3 materialize GATED on this scheme (CTO).
- **leg-5 freshness-alarm role** can now read github-token (parity-drift v2 unblocked for 0.7.0~B).

## Next Steps

- **[0.7.0_AE_CloudOps]** the coherent host-side cadence + alarm-wiring cluster: (1) /log-tied Q4 emit build (#12, DESIGN-to-CTO first) -- couples 0.8.0~B emitter git-sync + 0.5.0 producer contract; (2) reconcile-oracle Tier-2 wiring (#13) rides the same cadence + the opal-critical-surface-alerts SNS + item2c email sub + auto-fallback -> then ping CVO~B to close Tier-2; (3) land item2c critical-surface email sub (needed by leg-5 + reconcile alarms); (4) 0.5.0's nightly EventBridge TF (+ portal-checkout-in-image HARD REQ). Batched: FRESHGUARD leg-4 (nightly), kuzu_cli multi-query (#10, non-urgent).
- **[0.7.0_AE_CloudOps~B]** build leg-5 v2 (grant landed, CTO arch-gated).
- **[0.8.0_AE_CloudComp~B]** code_heat_emit.py git-sync-before-compute (emitter half).
- **[3.0.0_SA_CVO~B]** exercise-verify Tier-2 standing oracle on landing (planted real-delta drift -> alarm + fallback).
