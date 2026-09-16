# Deploy Completion Record
**Date opened:** 2026-09-15T22:26:29.765599+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the EventBridge rule daily-sprint-generator-schedule's 2026-09-16 20:10Z scheduled fire (the acceptance; a live invoke today would overwrite the local 2026-09-15 edition, and a missing past day is a backfill needing never-widen sign-off per main.tf) (held since 2026-09-15T23:08:07.277208+00:00)
**Deploy:** LD-0571 daily-sprint-generator fix and redeploy (Andrew-direct via 4.0.0_SA_CRO 'Hand off to MSTR to fix and deploy'): F1 process[] in the prompt, F2 clear WORKDIR before clone, F3 one repair pass. IMAGE ACT: tag daily-sprint-generator:latest has ONE consumer, this function (09-11 census 0 of 3 image Lambdas, 0 of 9 ECS families).
**Authored by:** 0.0.0_AB_MSTR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the fix | commit hash plus py_compile, ruff and offline arms | commit 6579f6dd52 on CLOUD (LOCAL) by 0.0.0_AB_MSTR under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL: infra/aws/lambda/daily_sprint_generator/lambda_function.py only (+ LD-0571). py_compile OK; ruff --target-version py39 'All checks passed!'; offline arms (stubbed AWS/git, no network) 0 failures: F2 stale WORKDIR absent at git clone; F3 A refusal->1 repair carrying the renderer's own text->publish once repaired=True, B second refusal raises 0 publish, C non-validation failure raises 0 repair 0 publish, D clean render 0 repair 1 publish. | CLOSED 20260915T222827Z |
| L2 | activation | image built from the committed bytes and pushed to ECR | digest read back from describe-images | image built from the COMMITTED bytes: build context = git archive HEAD infra/aws/lambda/daily_sprint_generator (Dockerfile + lambda_function.py; ctx lambda_function.py sha256 21129da43b1489d7 == git show HEAD:... sha256, last commit 6579f6dd52). docker build --provenance=false --sbom=false --platform linux/amd64 rc=0; docker push rc=0. DIGEST read back from ECR describe-images (not the push line): sha256:7d699a0ff570bee48083291d5159c99eb425ca51f3d1fae7a6e8e79a71f85a09, imageManifestMediaType application/vnd.oci.image.manifest.v1+json -- a SINGLE manifest, not a list (the 09-11 L3 trap), pushed 1789511825 (2026-09-15T22:37Z). Prior running digest sha256:e4a23058ac30... kept by the keep-last-5 lifecycle for rollback. | CLOSED 20260915T223849Z |
| L3 | activation | Terraform replace of aws_lambda_function.sprint via safe-apply | Apply complete line with resource counts | safe-apply (HALTGT checkpoint passed, HALT_ACK=1 after reading pending mail) -chdir=infra/aws/terraform/daily-sprint-generator apply -replace=aws_lambda_function.sprint -replace=aws_lambda_permission.sprint: 'Apply complete! Resources: 2 added, 0 changed, 2 destroyed.' The permission is replaced WITH the function deliberately: the first plan (function only) left aws_lambda_permission.sprint untouched, but deleting a function deletes its resource policy, so state would have claimed a permission the live function no longer had and the 20:10Z schedule would have failed to invoke. Pre-apply plan with both: 2 add, 1 change (event target arn known-after-apply), 2 destroy. Same route as 09-11 (CloudTrail: Delete/CreateFunction + AddPermission pairs). | CLOSED 20260915T230555Z |
| L4 | verify | served bytes equal built bytes | get-function ResolvedImageUri equals the pushed digest; unscoped re-plan reads No changes | SERVED BYTES = BUILT BYTES: get-function Code.ResolvedImageUri = daily-sprint-generator@sha256:7d699a0ff570bee48083291d5159c99eb425ca51f3d1fae7a6e8e79a71f85a09, byte-identical to the L2 digest (before: sha256:e4a23058ac30...). get-function-configuration: Active / Successful, Timeout 900, Memory 3008, OPENAI_MODEL gpt-5.6-sol, SPRINT_BRANCH CLOUD, GITHUB_SECRET estate-report/github-token (unchanged). Resource policy after: AllowExecutionFromEventBridge, principal events.amazonaws.com, SourceArn rule/daily-sprint-generator-schedule (same as before). list-targets-by-rule: the function ARN; describe-rule ENABLED cron(10 20 * * ? *). Unscoped terraform plan after: 'No changes. Your infrastructure matches the configuration.' STATE: CONFIGURED + WIRED, not yet EXERCISED -- that is L5. | CLOSED 20260915T230557Z |
| L5 | verify | the job actually runs and publishes | the 2026-09-16 20:10Z scheduled fire publishes a served page matching its read-back |  | OPEN |

## Log

- 20260915T222629Z OPENED by 0.0.0_AB_MSTR with 5 leg(s)
- 20260915T222827Z LEG L1 closed: commit 6579f6dd52 on CLOUD (LOCAL) by 0.0.0_AB_MSTR under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL: infra/aws
- 20260915T223849Z LEG L2 closed: image built from the COMMITTED bytes: build context = git archive HEAD infra/aws/lambda/daily_sprint_generator (Dockerfi
- 20260915T230555Z LEG L3 closed: safe-apply (HALTGT checkpoint passed, HALT_ACK=1 after reading pending mail) -chdir=infra/aws/terraform/daily-sprint-gen
- 20260915T230557Z LEG L4 closed: SERVED BYTES = BUILT BYTES: get-function Code.ResolvedImageUri = daily-sprint-generator@sha256:7d699a0ff570bee48083291d5
- 20260915T230807Z HELD-SOVEREIGN-GATED gate=external/the EventBridge rule daily-sprint-generator-schedule's 2026-09-16 20:10Z schedul
