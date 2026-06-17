# NFRA_INFRPT.P1 increment-2b -- DRIFT producer DEPLOYED + render verified (0.7.0_AE_CloudOps~B)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, COORDINATE, DIAGNOSE

Window: since the inc-2a log. Lane: 0.7.0_AE_CloudOps~B.

## Current State

NFRA_INFRPT.P1 increment-2b (the producer-backed DRIFT legs) is DEPLOYED end-to-end + render-verified in-Lambda. The infra report's DRIFT section is now complete: deploy-drift (2a, in-Lambda) + producer comp/terraform (2b), all with staleness/coverage meta-guards. Tag `shared-infra-v1.25.0`.

ARCHITECTURE (forced hybrid -- two CI walls, CTO-ruled): GH-Action push leg (`.github/workflows/drift-producer-push.yml`, BASE_EXEC-committed by CTO 1594218) on push:CLOUD -> OIDC `opal-drift-producer-gha-role` (branch-pinned ref:refs/heads/CLOUD, PR-excluded) runs `drift_producer.py --mode comp` -> `s3://opal-data-portal-v2/infrastructure/drift_state_comp.json` + re-zips the terraform source subset -> `s3://opal-313476888478-lambda-artifacts/drift-producer/source.zip`. EventBridge nightly (06:30 UTC) -> CodeBuild `opal-drift-producer` (read-only service role `opal-drift-producer-codebuild-role`, S3-ZIP source) runs `drift_producer.py --mode terraform` -> `drift_state_tf.json`. Lambda `check_producer_drift` renders both legs + staleness (generated_at/terraform_checked_at/source_zip_age, 26h/50h) + the coverage guard.

DEPLOYED (TF `infra/aws/terraform/shared-infra/drift-producer.tf`, 9 resources, safe-apply 0-destroy; comp-iam 0 missing). Read-only role = ZERO mutate verbs (CTO-signed-off; DescribeSecret not GetSecretValue, no Decrypt). Lambda render sha `udV+iYte...`.

VERIFIED IN-LAMBDA (archive `infrastructure/reports/2026-06-17/17-31-22.json`): comp leg [OK] 0 findings (2 tools clean); terraform leg renders all 3 staleness lines + `coverage 6/29 (RED)` -- the coverage guard WORKING (the leg goes RED on honest low coverage; NO false-clean). deploy_drift WATCH (volatility-fetcher NEW->standing). data_freshness RED (inc-1 persists).

## Run-to-verify / iterate-on-the-run findings (CTO-anticipated)

- terraform coverage 6/29: `terraform plan` fails on the FIRST refresh error per module, so each read-perm wave reveals only the NEXT per-module error (data-refresh: S3-bucket-read [wave-1] -> S3-object-tags [wave-2] -> CW-Logs-tags [next]). An estate-wide terraform-plan READ role needs the full per-service read surface. Waves 1-2 done (S3 read+tagging, ELBv2, CloudFront-list, CUR, ECR, StepFns, CW-alarms). PERM-BREADTH DECISION routed to CTO: hand-scope the tail (least-priv, many waves) vs a broad read-only managed policy (fast, broader than the signed-off least-priv).
- Config tail (not perms): bd/cot/inf/mdpf `ec2.tf` + globgrph terraform-function errors (per-module) + 2 var-requiring modules (need tfvars).
- comp-surface-check `scan` SILENT-NO-OP in CI: `.comp-graph` is gitignored -> no baseline -> rc=0 + 0-findings, which the rc-based could-not-assess MISSES. Needs a hardening (detect rc-0-but-no-baseline). The comp leg reported "2 tools ran clean" -- the surface tool ran but didn't actually assess.

## Deployment Sequence (AE)

[CTO commits BASE_EXEC workflow 1594218] -> (workflow first run FAILED: role not yet applied) -> safe-apply drift-producer.tf (9 add) -> gh run rerun (role now exists) GREEN: source.zip + drift_state_comp -> aws codebuild start-build (terraform leg) SUCCEEDED: drift_state_tf (6/29) -> role-perm iterate wave-1 (artifact/layer read) commit+apply+rerun -> wave-2 (tags + service Describe verbs) commit+apply+rerun -> build-and-upload Lambda render + safe-apply (render live) -> record-terraform-deploy shared-infra-v1.25.0 + tag + push -> async invoke (Event) -> archive 17-31-22.json render-verified.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-iam | gaps (x3, after each iam.tf change) | PASS | 0 missing each time (drift roles are CodeBuild/GHA, not in the Lambda/EC2 model) |
| ds-commit-gate.sh | drift_producer.py + lambda_function.py (xN) | PASS | py_compile + AST + ruff clean each edit |
| safe-apply.sh | -chdir=shared-infra apply (x3) | PASS | 9 add then 2 change then 1 change; 0-destroy throughout |
| build-and-upload.sh | shared-infra opal-infrastructure-monitor | PASS | render artifact udV+iYte |
| record-terraform-deploy.sh | shared-infra --version shared-infra-v1.25.0 | PASS | CHANGELOG + source-map |

**What worked:** the coverage guard (CTO refinement) validated live -- it correctly screams 6/29 RED rather than false-cleaning a 21%-coverage run; the per-module degrade-to-WATCH made every cannot-assess VISIBLE; the iterate-on-the-run advanced module errors wave-by-wave (visible, not silent); async-invoke + archive-read verify (no retry-storm). **What failed:** the first GH-Action run (role not yet applied -- expected ordering; fixed by apply-then-rerun). **Gap:** the terraform-plan read tail (perm-breadth decision) + the comp-surface-scan CI-baseline no-op (could-not-assess hardening).

## Blockers

None. The inc-2b SYSTEM is done + verified. Coverage-to->=80% is iterate-on-the-run, gated on CTO's perm-breadth decision (not a blocker -- the guard reports honest coverage meanwhile).

## Next Steps

- **[1.0.0_SA_CTO]** Perm-breadth decision: hand-scope the terraform-plan read tail (least-priv) vs broad read-only managed policy (coverage-velocity).
- **[0.7.0_AE_CloudOps~B]** Per CTO's call: continue the read-perm iterate OR swap to the managed policy; harden the comp-surface-scan could-not-assess (rc-0-no-baseline); investigate the ec2.tf/globgrph terraform-function errors + the 2 var-requiring modules.
- **[0.7.0_AE_CloudOps~B]** Deliberate-queued (after inc-2b, per COO): volatility-fetcher stranded-deploy adjudication + stale source-map fix; deploy-role OIDC trust hardening (which-refs-check first).

## Files Modified

See commit messages: `562de2df7` (drift-producer.tf + drift_producer.py), `fa3823be5` + the wave-2 commit (role-perm iterate), `c49f36d4f` (record deploy v1.25.0). GH-Action `.github/workflows/drift-producer-push.yml` committed by CTO (BASE_EXEC, 1594218).
