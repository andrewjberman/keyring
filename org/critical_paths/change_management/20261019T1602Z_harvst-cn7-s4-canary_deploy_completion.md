# Deploy Completion Record
**Date opened:** 2026-10-19T16:02:50.616264+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cn-7 stage 4: ONE manual DRY canary of the standing dossier-refresh task: aws ecs run-task on amgt-dossier-refresh-cluster, task definition amgt-dossier-refresh-task:1 (image by digest sha256:ceac4ad0..), Fargate, subnet subnet-023db8cbfd99ffff2, security group sg-0e3918ef300c9f5e4 (amgt-dossier-refresh-sg), public IP, container command override [--only, UNH_US_Equity] with NO --write and NO --require-trading-day; expected exit 0 and REFRESH-CENSUS names=1 ... errors=0 mode=dry-run; a written count above 0, a non-zero exit, errors, AccessDenied, image-pull failure or missing log is a STOP (and a disable); the schedule stays DISABLED; nothing is written to the gold prefix; nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | run-task issued once with the override; task ARN printed; the schedule read DISABLED before and after | run-task output + schedule reads |  | OPEN |
| F2 | verify | task STOPPED; container exit code 0; startedAt/stoppedAt and wall seconds; the CloudWatch log has REFRESH-CENSUS names=1 errors=0 mode=dry-run and written 0 | task describe + log lines |  | OPEN |
| F3 | git | ledger closed and committed with cn7_s4.out | commit hash |  | OPEN |

## Log

- 20261019T160250Z OPENED by 0.7.0_AE_CloudOps~SC1 with 3 leg(s)
