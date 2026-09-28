# Deploy Completion Record
**Date opened:** 2026-09-25T13:23:05.751048+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T132739Z
**Deploy:** Directory refresh fires 09:30 ET, inside the runner host up window (row IRPT_BCKEND-S126)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_scheduler_schedule.irpt_directory_refresh | get-schedule reads cron(30 9 ? * MON-FRI *) America/New_York ENABLED | scheduler get-schedule irpt-directory-refresh 2026-09-25T13:3xZ: cron(30 9 ? * MON-FRI *) America/New_York ENABLED, target irpt-directory-refresh (safe-apply: tagauthz PASSED, 0 added 1 changed 0 destroyed) | CLOSED 20260925T132738Z |
| V1 | verify | 0-diff re-plan of the directory root | terraform plan reads No changes | terraform plan infra/aws/terraform/investor-reporting/directory after apply: No changes. Your infrastructure matches the configuration. | CLOSED 20260925T132739Z |

## Log

- 20260925T132305Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260925T132738Z LEG A1 closed: scheduler get-schedule irpt-directory-refresh 2026-09-25T13:3xZ: cron(30 9 ? * MON-FRI *) America/New_York ENABLED, targ
- 20260925T132739Z LEG V1 closed: terraform plan infra/aws/terraform/investor-reporting/directory after apply: No changes. Your infrastructure matches the
- 20260925T132739Z CLOSED -- all 2 legs proven
