# Deploy Completion Record
**Date opened:** 2026-10-19T13:36:55.070608+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cn-7 stage 2: build the dossier-refresh container image by CodeBuild from the pinned worktree (build-image.sh --go: source zip upload to s3://opal-313476888478-lambda-artifacts/harvest/build-source/dossier-refresh-source.zip, CodeBuild amgt-dossier-refresh-build, push tag git-e2bd0ba10483 IMMUTABLE into amgt-dossier-refresh-repo); the ONE task family that pulls the repository is amgt-dossier-refresh-task (not yet created; stage 3); digest and size read by two routes; no task definition or schedule exists yet; failure = STOP, nothing retried, nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | task families that pull the repository: live ECS sweep over all families (0 now) and the Terraform config (exactly 1: amgt-dossier-refresh-task) printed; zip file count and zip set equals the pin | count lines + build-image output |  | OPEN |
| B2 | activation | build-image.sh --go: zip uploaded, CodeBuild started and polled to a TERMINAL status SUCCEEDED, smoke step lines printed | build id + status + smoke log lines |  | OPEN |
| B3 | verify | digest and size by two routes (build log IMAGE_DIGEST/IMAGE_SIZE_BYTES and ecr describe-images by tag) agree; size in MB vs cn-4's 287 MB; scan findings counts printed | routes_agree=yes + counts |  | OPEN |
| B4 | git | ledger closed and committed WITH cn7_s2.out | commit hash |  | OPEN |

## Log

- 20261019T133655Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
