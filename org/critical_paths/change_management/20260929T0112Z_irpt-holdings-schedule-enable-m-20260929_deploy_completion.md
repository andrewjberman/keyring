# Deploy Completion Record
**Date opened:** 2026-09-29T01:12:40.618010+00:00
**Status:** OPEN
**Deploy:** R4 step 4: irpt-holdings-snapshot DISABLED -> ENABLED (COO 8d601db072, CTO f541e1cbf0, CRO 283d590379)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~43
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply aws_scheduler_schedule.irpt_holdings_snapshot | Apply complete 0 added 1 changed 0 destroyed | Apply complete! Resources: 0 added, 1 changed, 0 destroyed (aws_scheduler_schedule.irpt_holdings_snapshot only, plan .scratch_plan.tfplan via HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/directory apply) | CLOSED 20260929T011727Z |
| V1 | verify | scheduler get-schedule | State ENABLED, target irpt-holdings-refresh-lambda, no qa in input; re-plan No changes | scheduler.get_schedule(Name='irpt-holdings-snapshot'): State=ENABLED, ScheduleExpression=cron(15 10 ? * MON-FRI *) America/New_York, TargetArn=...:function:irpt-holdings-refresh-lambda, Input={"kind":"irpt_holdings_refresh","note":"R4: ENABLED under signed halves (COO 8d601db072, CTO f541e1cbf0, CRO 283d590379)"} (no qa key); re-plan after apply: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260929T011727Z |
| V2 | verify | the first scheduled fire read back per firm (IB-mr-204) | per firm: command id, status, published revision, served manifest VersionId moved on Success / unchanged on failure |  | OPEN |

## Log

- 20260929T011240Z OPENED by 0.9.0_WK_IRPT_BCKEND~43 with 3 leg(s)
- 20260929T011727Z LEG A1 closed: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (aws_scheduler_schedule.irpt_holdings_snapshot only, plan .sc
- 20260929T011727Z LEG V1 closed: scheduler.get_schedule(Name='irpt-holdings-snapshot'): State=ENABLED, ScheduleExpression=cron(15 10 ? * MON-FRI *) Ameri
