# 0.7.0_AE_CloudOps -- work tick 2026-06-12 ~1930Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY

## Window

~1855Z tick (080461fbe, planning) -> ~1930Z. Three substantive commits + 1 TF apply +
1 CodeBuild container rebuild. Full D8-AE Part B delivered and deployed.

## Commits this window

- `69055c170` B1+B5: ledger wiring + advisory commit-time surface-check hook
- `3c79b0c5f` B2+B3+B4: SNS TF (item2c_surface_alarm.tf) + derive_runner scan + Lambda marker-advance
- `a34738082` Dockerfile: pyyaml + surface_check_cli + critical-surfaces.yaml for container

## D8-AE Part B -- complete

All 5 sub-deliverables shipped and deployed.

### B1 -- Durable approval ledger (surface_check_cli.py)
- `_audit()` now calls `_write_ledger_approval()` on every SURFACE_ACK bypass.
- Writes `org/critical_paths/change_management/{ts}_{surface}_all_approval.md` with
  class/surfaces/firm/commit/reason fields.
- Best-effort (try/except; never blocks the commit flow).
- File: `org/modules/graph/surface_check_cli.py` (B1 block at `_write_ledger_approval`).

### B5 -- Hook wiring (advisory, non-blocking)
- `safe-commit.sh`: advisory `comp-surface-check check --mode advisory` block inserted
  between contamination-check pass and `git commit --only`. Parses `$IN_SCOPE` newline
  list into `--file` args. Output prefixed `[surface-check]`. Absent binary = silent pass.
  LIVE: the self-test on B1+B5 commit fired: "OK: 2 changed file(s) touch no critical surface."
- `portal/.git/hooks/pre-push`: advisory gate inside `while read` loop, after D-1 check.
  `git diff --name-only base..local_sha | sed s/^/portal\//` -> `--file` args. Non-blocking.

### B2 -- SNS topic + derive_runner scan
- New TF file `infra/aws/terraform/globgrph/item2c_surface_alarm.tf`:
  - `aws_sns_topic.critical_surface_alerts` (opal-critical-surface-alerts)
  - `aws_iam_role_policy.derive_runner_sns` (DeriveRunnerSNS: sns:Publish on topic)
  - `aws_iam_role_policy.incremental_updater_sns` (IncrementalUpdaterSNS: sns:Publish)
- `item2a.tf` + `item2b.tf`: `SNS_TOPIC_ARN` env var injected.
- `derive_runner.py`: `run_critical_surface_scan(graph, date_str, prev_marker_ts)` after
  `stamp_branch_head_marker()` in `main()`. Layer-1 graph-diff vs
  `s3://opal-313476888478-globgrph/critical-surface-baseline.json`; SEV1/SEV2 surface
  attribution via `surface_check_cli.load_surfaces()` + `_file_touches()`; SNS publish
  on findings. Layer-2 (git hash-object) deferred -- Fargate has no git repo.
- Baseline uploaded to S3: `opal-313476888478-globgrph/critical-surface-baseline.json` (1.4MB).

### B3 -- Staleness routing
- `_read_previous_marker_ts()` reads F6 marker `committed_at` BEFORE this run overwrites it.
- In `run_critical_surface_scan()`: if age > 26h, emits STALENESS_WARN to SNS and writes
  S3 ledger entry to `opal-313476888478-globgrph/critical-paths/stale_warning/`.

### B4 -- Incremental_updater real-time marker-advance signal
- `lambda_function.py`: `_publish_marker_advance(written, deleted, batch_ts)` called after
  `stamp_branch_head_marker()` in the handler. Best-effort, logs WARNING on failure.
- `SNS_TOPIC_ARN` env var added to Lambda. New zip rebuilt + uploaded to S3.

## Deployment

### TF apply (globgrph-v0.1.13)
- Plan: 4 add, 3 change, 1 destroy (ECS task def revision replace, expected).
- Apply via `.tools/safe-apply.sh apply tfplan_D8_B2` -- HALT_OVERRIDE used (non-data-loss).
- Post-apply 0-diff: confirmed.
- Resources live:
  - `aws_sns_topic.critical_surface_alerts` ARN: `arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts`
  - `aws_iam_role_policy.derive_runner_sns` (opal-globgrph-derive-runner-task:DeriveRunnerSNS)
  - `aws_iam_role_policy.incremental_updater_sns` (opal-globgrph-incremental-updater:IncrementalUpdaterSNS)
  - ECS task def: `globgrph-derive-runner:2` (now has SNS_TOPIC_ARN env var)
  - Lambda: CodeSha256=`nzkYaTwKZlBob3Gdx3C1xqwD3NYvBvA0YkNjf80xFcQ=` -- verified MATCH.
  - Lambda SNS_TOPIC_ARN env var: `arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts` -- verified.

### Container rebuild (derive_runner:20260612-185544)
- Dockerfile updated: pyyaml==6.0.2 + surface_check_cli.py + critical-surfaces.yaml COPYed.
- Source zip built + uploaded to `opal-data-news-v2/codebuild/derive-runner-build.zip`.
- CodeBuild `semantic-clustering-lambda-build:77dbd2ef` -- SUCCEEDED.
- New image: `313476888478.dkr.ecr.us-east-1.amazonaws.com/opal-globgrph-derive-runner:latest`
  tag `20260612-185544` pushed to ECR.
- ECS task def :2 targets `:latest` -- next nightly run at 02:00 UTC will use new image.

## Compiler Tools

| Tool | Invocation | Result |
|------|-----------|--------|
| comp-blast | comp-blast opal-critical-surface-alerts | No nodes (new resource; 0 blast-radius, safe to create) |
| comp-iam | comp-iam service incremental_updater | Role not mapped (graph pre-apply); 3 ops detected (s3:GetObject, s3:PutObject, sns:Publish) -- IAM verified via TF apply |
| comp-iam | comp-iam service derive_runner | No sns:Publish (pre-apply); confirmed gap filled by item2c_surface_alarm.tf |
| ds-commit-gate | .tools/ds-commit-gate.sh surface_check_cli.py | PASS (B1 edit) |
| ds-commit-gate | .tools/ds-commit-gate.sh derive_runner.py lambda_function.py | PASS (B2+B3+B4 edits) |
| comp-surface-check | safe-commit.sh B5 self-test on B1+B5 commit | PASS: "OK: 2 changed file(s) touch no critical surface." |
| comp-surface-check | 3 subsequent commits | PASS (all reported "touch no critical surface") |
| terraform plan | globgrph 0-diff post-apply | PASS: "No changes. Your infrastructure matches the configuration." |

What worked: B5 self-test fired live on the B1+B5 commit -- proves the advisory hook is wired.
What failed: nothing.
Gap found: comp-iam service for incremental_updater shows role as "not mapped" in the graph (pre-apply vintage). The IAM gap is real (sns:Publish UNKNOWN before apply); filled by item2c_surface_alarm.tf:IncrementalUpdaterSNS. Will auto-resolve on next nightly graph re-derive.

## Deployment Sequence (Rule 2)

| Step | Action | Result |
|------|--------|--------|
| Code | surface_check_cli.py B1, safe-commit.sh B5, portal hook B5 | Committed 69055c170 |
| Code | derive_runner.py B2+B3, lambda_function.py B4, item2c.tf | Committed 3c79b0c5f |
| Code | Dockerfile pyyaml + surface_check_cli + critical-surfaces.yaml | Committed a34738082 |
| S3 upload | Lambda zip -> opal-313476888478-lambda-artifacts/globgrph/incremental_updater.zip | DONE |
| S3 upload | baseline.json -> opal-313476888478-globgrph/critical-surface-baseline.json | DONE |
| terraform plan -out | globgrph tfplan_D8_B2 | 4 add, 3 change, 1 destroy |
| safe-apply.sh | apply tfplan_D8_B2 | Apply complete (HALT_OVERRIDE) |
| 0-diff verify | terraform plan post-apply | No changes |
| git tag | globgrph-v0.1.13 | Tagged + pushed |
| Container rebuild | CodeBuild 77dbd2ef (source zip derive-runner-build.zip) | SUCCEEDED |
| ECR | opal-globgrph-derive-runner:latest + :20260612-185544 | Pushed |
| RAVC2 | 2.0.0_SA_COO | This tick |

## Current State

- D8-AE Part B: ALL 5 sub-deliverables (B1-B5) implemented, deployed, verified.
- Commits: `69055c170` (B1+B5), `3c79b0c5f` (B2+B3+B4), `a34738082` (Dockerfile)
- Lambda: opal-globgrph-incremental-updater at CodeSha256 `nzkYaTwKZlBob3Gdx3C1xqwD3NYvBvA0YkNjf80xFcQ=`
- SNS topic: `arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts`
- Container: ECR `:latest` = `20260612-185544` (pyyaml + surface_check_cli + critical-surfaces.yaml)
- Fargate task def: `globgrph-derive-runner:2` (next nightly: 02:00 UTC 2026-06-13)
- Advisory-mode active: blocking flip awaits COO's 3-condition gate
  (post-resign+CVO / one nightly synthetic-fires+Day-0-suppressed / 0-FP-SEV1-routine).
- OPEN: NFRA_DEBTSCAN TO-D1 (next) -> TO-D2 AE-lane (comp-iam gaps) -> NFRA_OPLMCP.01

## Next Steps

- [2.0.0_SA_COO] RAVC2 D8-AE Part B -- all 5 sub-deliverables delivered.
- [1.0.0_SA_CTO] Advisory->blocking flip -- 3-condition gate tracking.
- [0.7.0_AE_CloudOps] NFRA_DEBTSCAN TO-D1 reachability sweeps (next task order).
