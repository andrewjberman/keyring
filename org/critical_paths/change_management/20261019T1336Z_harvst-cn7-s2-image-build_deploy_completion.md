# Deploy Completion Record
**Date opened:** 2026-10-19T13:36:55.070608+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T134137Z
**Deploy:** AMGT_HARVST HVST-cn-7 stage 2: build the dossier-refresh container image by CodeBuild from the pinned worktree (build-image.sh --go: source zip upload to s3://opal-313476888478-lambda-artifacts/harvest/build-source/dossier-refresh-source.zip, CodeBuild amgt-dossier-refresh-build, push tag git-e2bd0ba10483 IMMUTABLE into amgt-dossier-refresh-repo); the ONE task family that pulls the repository is amgt-dossier-refresh-task (not yet created; stage 3); digest and size read by two routes; no task definition or schedule exists yet; failure = STOP, nothing retried, nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | task families that pull the repository: live ECS sweep over all families (0 now) and the Terraform config (exactly 1: amgt-dossier-refresh-task) printed; zip file count and zip set equals the pin | count lines + build-image output | PASS (count read). Config: exactly 1 aws_ecs_task_definition in dossier-refresh.tf (family amgt-dossier-refresh-task, created at stage 3); live ECS: 10 ACTIVE families swept, 0 name amgt-dossier-refresh-repo (the first sweep script failed on a path error and was re-run read-only); zip 767 entries from 19 COPY lines, zip set equals HEAD e2bd0ba104 | CLOSED 20261019T134136Z |
| B2 | activation | build-image.sh --go: zip uploaded, CodeBuild started and polled to a TERMINAL status SUCCEEDED, smoke step lines printed | build id + status + smoke log lines | STOP, NOT A PASS. build-image.sh --go uploaded the source zip (4032386 B, VersionId CEDJquKeV6S7d98aoOBHfjm_T828Qywb) and started CodeBuild build a8b1605f-e707-4c69-81f8-945ac366a6eb, which reached terminal status FAILED at 13:37:46Z in DOWNLOAD_SOURCE: YAML_FILE_ERROR 'Expected Commands[7] to be of string type: found subkeys instead at line 43'. Cause: buildspec.yml phases.build[2] and phases.post_build[7] are unquoted plain scalars with a colon-space. No Docker step, no smoke step. Nothing retried, recipe not edited. Row AMGT_HARVST-D1-S65. Closed as a STOP so the entry is not left open: nothing half-landed (0 images, no task definition/schedule); the S3 source zip stays | CLOSED 20261019T134136Z |
| B3 | verify | digest and size by two routes (build log IMAGE_DIGEST/IMAGE_SIZE_BYTES and ecr describe-images by tag) agree; size in MB vs cn-4's 287 MB; scan findings counts printed | routes_agree=yes + counts | NOT OBTAINED, STOP. No image was built, so no IMAGE_DIGEST/IMAGE_SIZE_BYTES, no two-route agreement (routes_agree not computed), no scan counts. ECR repository amgt-dossier-refresh-repo holds 0 images (list-images length 0). Closed as part of the STOP, not a pass | CLOSED 20261019T134137Z |
| B4 | git | ledger closed and committed WITH cn7_s2.out | commit hash | Closed with the STOP: this close commits with cn7_s2.out (the full transcript and failure read) and surprise row AMGT_HARVST-D1-S65 | CLOSED 20261019T134137Z |

## Log

- 20261019T133655Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
- 20261019T134136Z LEG B1 closed: PASS (count read). Config: exactly 1 aws_ecs_task_definition in dossier-refresh.tf (family amgt-dossier-refresh-task, cr
- 20261019T134136Z LEG B2 closed: STOP, NOT A PASS. build-image.sh --go uploaded the source zip (4032386 B, VersionId CEDJquKeV6S7d98aoOBHfjm_T828Qywb) an
- 20261019T134137Z LEG B3 closed: NOT OBTAINED, STOP. No image was built, so no IMAGE_DIGEST/IMAGE_SIZE_BYTES, no two-route agreement (routes_agree not co
- 20261019T134137Z LEG B4 closed: Closed with the STOP: this close commits with cn7_s2.out (the full transcript and failure read) and surprise row AMGT_HA
- 20261019T134137Z CLOSED -- all 4 legs proven
