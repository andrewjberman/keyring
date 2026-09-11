# Deploy Completion Record
**Date opened:** 2026-09-11T20:02:55.862829+00:00
**Status:** OPEN
**Deploy:** LD-0547 daily-sprint-generator: first apply of the scheduled cloud /daily-sprint -- ECR repo, container image, image Lambda, execution role and the 21:30 Eastern EventBridge schedule. Andrew-direct 2026-09-10 'This needs to be an automatic run. Please build it now.'; credential resolved Andrew-direct 2026-09-11 'just use the one that is already there' (estate-report/github-token), relayed 1.0.0_SA_CTO msg 95850. IMAGE-ACT BLAST RADIUS (NEVER-2), measured by this seat not taken from the handoff: the tag 313476888478.dkr.ecr.us-east-1.amazonaws.com/daily-sprint-generator:latest has ZERO existing consumers -- 0 of 3 image-package Lambdas and 0 of 9 active ECS task families reference it; the repository did not exist before this deploy, so the tag reaches exactly one family, the function created here. A future second consumer makes this a shared tag and pinning moves to digest-per-family.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the remote-state backend fix on the component | commit hash, terraform fmt and validate clean |  | OPEN |
| L2 | activation | ECR repository daily-sprint-generator created via targeted safe-apply | the apply resource count plus describe-repositories returning the repositoryUri |  | OPEN |
| L3 | activation | container image built from the committed Dockerfile and pushed to that repository | the image DIGEST from describe-images, not a tag name and not the build rc |  | OPEN |
| L4 | activation | full safe-apply of the remaining resources | Apply complete line with resource counts covering all 9 planned resources |  | OPEN |
| L5 | verify | unscoped re-plan on the applied root | terraform plan reading No changes |  | OPEN |
| L6 | verify | live state of the function and its schedule | get-function-configuration returning the function plus describe-rule showing the schedule ENABLED -- proves CONFIGURED only, never that the job works |  | OPEN |
| L7 | verify | the job actually RUNS -- the only oracle the handoff accepts | a served page under s3://opal-data-portal-v2/daily-reports/ matching its own read-back, from a real execution |  | OPEN |

## Log

- 20260911T200255Z OPENED by 0.7.0_AE_CloudOps with 7 leg(s)
