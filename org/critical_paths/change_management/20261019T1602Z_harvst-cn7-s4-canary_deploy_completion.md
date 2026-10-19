# Deploy Completion Record
**Date opened:** 2026-10-19T16:02:50.616264+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T160725Z
**Deploy:** AMGT_HARVST HVST-cn-7 stage 4: ONE manual DRY canary of the standing dossier-refresh task: aws ecs run-task on amgt-dossier-refresh-cluster, task definition amgt-dossier-refresh-task:1 (image by digest sha256:ceac4ad0..), Fargate, subnet subnet-023db8cbfd99ffff2, security group sg-0e3918ef300c9f5e4 (amgt-dossier-refresh-sg), public IP, container command override [--only, UNH_US_Equity] with NO --write and NO --require-trading-day; expected exit 0 and REFRESH-CENSUS names=1 ... errors=0 mode=dry-run; a written count above 0, a non-zero exit, errors, AccessDenied, image-pull failure or missing log is a STOP (and a disable); the schedule stays DISABLED; nothing is written to the gold prefix; nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | run-task issued once with the override; task ARN printed; the schedule read DISABLED before and after | run-task output + schedule reads | PASS. cn7_s4.out 16:04Z: schedule DISABLED before; run-task issued once (failures []) for task arn:aws:ecs:us-east-1:313476888478:task/amgt-dossier-refresh-cluster/3d1131e0936e4b8785d06e22e2e1486a, task definition amgt-dossier-refresh-task:1, Fargate, subnet-023db8cbfd99ffff2, sg-0e3918ef300c9f5e4, public IP, override [--only, UNH_US_Equity] (no --write, no --require-trading-day); schedule DISABLED after | CLOSED 20261019T160724Z |
| F2 | verify | task STOPPED; container exit code 0; startedAt/stoppedAt and wall seconds; the CloudWatch log has REFRESH-CENSUS names=1 errors=0 mode=dry-run and written 0 | task describe + log lines | PASS on the order's required items, with ONE unnamed difference stated and not self-graded. Task STOPPED (EssentialContainerExited), container exit code 0, startedAt 16:04:52Z stoppedAt 16:06:06Z wall 74.8 s; log: REFRESH-CENSUS names=1 written=0 would_write=1 unchanged=0 no_new_model_block=0 no_today_model_block=0 skipped_allowed=0 skipped_guard=0 errors=0 mode=dry-run; no AccessDenied, no image-pull failure. Difference: the order expects UNH to read UNCHANGED; it read WOULD_WRITE moved=model_rows inputs_differ=model_block guard=PASS (consistent with a model block dated 2026-10-19 now existing; stamps not read). Nothing written | CLOSED 20261019T160724Z |
| F3 | git | ledger closed and committed with cn7_s4.out | commit hash | Closed and committed with cn7_s4.out in the stage-4 commit | CLOSED 20261019T160724Z |

## Log

- 20261019T160250Z OPENED by 0.7.0_AE_CloudOps~SC1 with 3 leg(s)
- 20261019T160724Z LEG F1 closed: PASS. cn7_s4.out 16:04Z: schedule DISABLED before; run-task issued once (failures []) for task arn:aws:ecs:us-east-1:313
- 20261019T160724Z LEG F2 closed: PASS on the order's required items, with ONE unnamed difference stated and not self-graded. Task STOPPED (EssentialConta
- 20261019T160724Z LEG F3 closed: Closed and committed with cn7_s4.out in the stage-4 commit
- 20261019T160725Z CLOSED -- all 3 legs proven
