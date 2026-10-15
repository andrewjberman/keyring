# Deploy Completion Record
**Date opened:** 2026-10-15T17:32:32.671205+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-266: ENABLE the Cottonwood landing schedule irpt-cot-account-return-daily-daily (DISABLED to ENABLED, ONE line of schedule.tf), plan exactly 0/1/0, ONE safe-apply, NO invoke; CTO ruling round-128 addendum 1 @143709c44f; the first scheduled fire stays OPEN for the issuer
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the one-line edit of schedule.tf (state DISABLED to ENABLED) and its commit | git diff shows exactly one changed line; the commit hash |  | OPEN |
| L2 | activation | terraform: fmt, validate, saved plan EXACTLY 0 add 1 change 0 destroy on aws_scheduler_schedule.irpt_account_return_daily, then ONE safe-apply | plan line, apply line |  | OPEN |
| L3 | verify | read-backs: schedule ENABLED at the cron and zone, target the function, flexible window OFF, function unchanged, replan No changes | get-schedule, get-function-configuration, replan line |  | OPEN |
| L4 | verify | the first scheduled fire (2026-10-16 08:15 New York): left OPEN for the issuer 2.0.0_SA_COO~D2 | the issuer's read |  | OPEN |

## Log

- 20261015T173232Z OPENED by 0.7.0_AE_CloudOps~DB2 with 4 leg(s)
