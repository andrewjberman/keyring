# Deploy Completion Record
**Date opened:** 2026-10-05T03:48:21.310013+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T134429Z
**Deploy:** S323: restart EC2 i-02448edb624a7a7cf (mdpf-daily-runner, stopped User initiated 2026-10-04 16:41:18 GMT) on Andrew card 2 @c9c8e0c191 -- one start only
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | activation | ec2 start-instances i-02448edb624a7a7cf | state running | start-instances: stopped -> pending; waiter: running, LaunchTime 2026-10-05T03:49:32Z (one start, Andrew card 2 @c9c8e0c191) | CLOSED 20261005T035104Z |
| V1 | verify | SSM agent Online on the instance | describe-instance-information PingStatus | ssm describe-instance-information PingStatus Online, LastPing 2026-10-05T03:50:05Z | CLOSED 20261005T035104Z |
| V2 | verify | the next directory refresh manifest read at all three firms | manifest keys + timestamps | READ 2026-10-05 ~13:4xZ, NEGATIVE: the 13:30Z refresh manifests at opal-data-bd/inf/cot all read HAND_OVER_RUNNER_OFFLINE ('start issued, no build sent'); the runner was started again at 13:30:36Z by the dispatcher, so the one-time 03:49Z start did not carry through. The start was the act this ledger covers; the remedy is not complete, new row S336 (dispatcher start races the SSM hand-over) | CLOSED 20261005T134428Z |

## Log

- 20261005T034821Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20261005T035104Z LEG S1 closed: start-instances: stopped -> pending; waiter: running, LaunchTime 2026-10-05T03:49:32Z (one start, Andrew card 2 @c9c8e0c
- 20261005T035104Z LEG V1 closed: ssm describe-instance-information PingStatus Online, LastPing 2026-10-05T03:50:05Z
- 20261005T134428Z LEG V2 closed: READ 2026-10-05 ~13:4xZ, NEGATIVE: the 13:30Z refresh manifests at opal-data-bd/inf/cot all read HAND_OVER_RUNNER_OFFLIN
- 20261005T134429Z CLOSED -- all 3 legs proven

## Correction (2026-10-05 ~13:4xZ)

Leg V2's proof names the new row "S336"; the row filed is IRPT_BCKEND-S335.
