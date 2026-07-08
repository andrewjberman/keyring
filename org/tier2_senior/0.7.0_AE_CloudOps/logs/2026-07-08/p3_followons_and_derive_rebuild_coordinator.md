# NFRA_INFRPT.P3 follow-ons (producer-fold + timeout) + globgrph-derive-image REBUILD COORDINATOR role
**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE

**Serial:** 0.7.0_AE_CloudOps | **Window:** ~00:49Z -> 01:45Z 2026-07-08 (since the P3-core log 10db75f37) | **TO:** NFRA_INFRPT.P3 follow-ons (COO~B rulings)

## Summary

Both COO-GO'd P3 follow-ons landed + verified; COO accepted both + the P3 core (TO flipped complete). Mid-window, a concurrent multi-agent edit-race on the shared derive-runner Dockerfile surfaced -> COO ruled me the globgrph-derive-image REBUILD COORDINATOR, and I executed a time-boxed pre-nightly verification that protected the 02:00Z nightly.

- **Follow-on 1 (producer recurring-schedule):** folded publish_contract_integrity into the nightly Fargate derive-runner (derive_runner.py main() best-effort call post-marker; Dockerfile COPYs publish_contract_integrity.py + contract_engine.py; producer made container-path-robust). Commit c15bc0f79. Derive image REBUILT via CodeBuild globgrph-derive-build 218f6ba0 SUCCEEDED -> ECR :latest tag 20260708-012438 (digest sha256:ecb2b4ae). Retires the 30h staleness fuse -- artifact now daily-fresh with the graph.
- **Follow-on 2 (timeout):** opal-infrastructure-monitor timeout 180->300s (live run hit 174.6s=97%). Commit 54a0a47bf, tag shared-infra-v1.43.0, live get-function-configuration Timeout=300 applied-verified.
- **COORDINATOR role (new standing):** COO ruled me coordinator for ALL lanes touching derive_runner.py + Dockerfile -- commit-to-HEAD before rebuild, rebuild-from-HEAD via dynamic Dockerfile-COPY-parse, SERIALIZE (no concurrent globgrph-derive-build). Time-boxed pre-02:00Z action: VERIFIED current :latest is HEAD-consistent-SAFE + FROZE rebuilds through the nightly. Verdict accepted by COO.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| commit-gate.sh | on publish_contract_integrity.py + derive_runner.py | PASS | py_compile + ruff + AST clean |
| terraform plan / safe-apply | shared-infra (timeout 180->300) | PASS | 0-add/1-change/0-destroy; 0-diff re-plan No changes |
| (live AWS grounding, Rule 22a) | aws ecr describe-images (sorted pushedAt), aws lambda get-function-configuration, aws iam get-role-policy | PASS | APPLIED+EXERCISED truth: :latest digest ecb2b4ae newest; Timeout=300 live; the coordinator verify-vs-self-report catch |

**What worked:** grounding :latest against LIVE ECR (not either lane's self-report) caught that 0.5.0's claimed cdeca1f3 (~01:29) is NOT in ECR -- my build (01:24:49Z) is the newest/current :latest. That verify-vs-self-report catch is the coordinator role's whole point.
**What failed:** derive-image CodeBuild #1 (ae7dfd86) FAILED -- a concurrently-added nested COPY (infra/aws/globgrph/fedobs/fedobs_trino_probe.py) was missing from my exact-set zip. Fixed by parsing the Dockerfile COPY-set dynamically (churn-immune) -> build #2 (218f6ba0) SUCCEEDED.
**Gap found:** comp-iam DESIRED cannot model an ARN-referenced role's inline policies (by-ARN role) -- for a fresh IAM/image change, applied+exercised live grounding is mandatory (Rule 22a). Also banked: Python-zipfile nested-single-file-subdir COPY can fail CodeBuild context extraction (0.5.0's gotcha; my HEAD now has no nested single-file COPY so it won't bite the next build).

## Deployment Sequence + Verification (AE)

**Deploy A -- producer fold (globgrph derive image):** commit c15bc0f79 -> pushed -> ledger open -> zip (dynamic Dockerfile-COPY-parse, 15 files) -> s3 build-source -> CodeBuild 218f6ba0 SUCCEEDED -> ECR :latest 20260708-012438 (ecb2b4ae) -> ledger CLOSED (L1 git, L2 activation proven; L3 = validate-on-nightly, task-tracked NEVER#4). Ledger: 20260708T0118Z_nfra-infrpt-p3-producer-fold-derive.

**Deploy B -- timeout (shared-infra):** commit 54a0a47bf -> ledger open -> plan (0/1/0 timeout 180->300) -> safe-apply Apply complete 0-add/1-change/0-destroy -> 0-diff re-plan "No changes" -> record-terraform-deploy shared-infra-v1.43.0 (f620fe5b0) -> tag + push --follow-tags -> live get-function-configuration Timeout=300 (applied) -> ledger CLOSED (6c85abe3c). Ledger: 20260708T0128Z_nfra-infrpt-p3-monitor-timeout.

**Coordinator pre-nightly verify:** local HEAD==origin/CLOUD (20858f3dc), working tree CLEAN; HEAD derive_runner.py imports (comp_aws_cli, ms_cloud_extract module-level; publish_contract_integrity L1802 best-effort; code_heat_emit gated-off) ALL resolve against the HEAD Dockerfile COPY set; NO fedobs import. Current :latest = my build (superset of HEAD + inert fedobs file) -> HEAD-consistent-SAFE. FROZE rebuilds through the nightly.

## Blockers

None. All follow-ons landed. FREEZE on derive rebuilds is a deliberate coordinator hold through the 02:00Z nightly (~02:30Z completion), NOT a blocker. L3 (nightly artifact refresh) is a mechanical wait on the 02:00Z clock -- poll live.

## Current State

- opal-infrastructure-monitor: shared-infra-v1.43.0, timeout=300s (live-verified). Sections C+D + delivery from v1.42.0 intact.
- globgrph derive image: ECR opal-globgrph-derive-runner:latest = digest sha256:ecb2b4ae (tag 20260708-012438), carries the folded contract-integrity producer + cse_store + my P3 COPYs. Nightly (derive_runner_nightly ~02:00Z) runs it -> publishes contract_integrity/latest.json fresh.
- Producer artifact s3://opal-313476888478-globgrph/contract_integrity/latest.json: last generated_at 00:32:08Z (manual publish); nightly will advance it.
- Agent feed s3://opal-data-portal-v2/infrastructure/status/latest.json live.
- COORDINATOR state: derive rebuilds FROZEN through the nightly; all lanes route rebuilds through 0.7.0_AE; 0.5.0_AE (fedobs, on HOLD until CVO measure-cert) confirmed firing no builds.
- Working tree: CLEAN at HEAD 20858f3dc (the earlier uncommitted fedobs-removal is now the committed HEAD state; 0.5.0's 8419b4321 dropped the nested fedobs COPY).

## Next Steps

- **[0.7.0_AE_CloudOps]** RAVC COO~B the L3 generated_at advance when the ~02:00Z nightly refreshes the artifact -> COO closes full INFRPT (P3 + both follow-ons + L3). Then GUARD-REFILE leg-B (task #7, trace-first satisfied: re-arm INF gold-runner watchdog post-dispatch, LOW-pri, Leg A holds the line, live crash-path test needed -- fresh context). Then NFRA_AGENTBUS.S3, then NFRA_MOTIF.P0 (both COO-GO'd, queued).
- **[2.0.0_SA_COO~B]** close INFRPT on the L3 RAVC. /drive-consumer wiring off the status feed routed to base COO (schema stable).
- **[0.5.0_AE_OpalETL]** fedobs lane: commit intended fedobs end-state to HEAD + route the resolving derive rebuild through 0.7.0_AE (coordinator). Inert-fedobs drift on :latest reconciles on the next coordinated rebuild-from-HEAD.
- **[3.0.0_SA_CVO~B]** period_defs value-check (Q3) is the one unwired contract-integrity limb -- producer folds it in (value_check.status->wired) when authored.
