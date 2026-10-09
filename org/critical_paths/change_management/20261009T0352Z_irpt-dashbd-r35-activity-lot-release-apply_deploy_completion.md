# Deploy Completion Record
**Date opened:** 2026-10-09T03:52:19.900727+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-70: apply the R35 activity-and-lot release to irpt-49f-reporting-gold-lambda (class + activity + realized + unrealized tables; targeted plan 0/3/0)
**Authored by:** 0.9.0_WK_IRPT_DASHBD~47
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pins 0-4 + artifact rebuild + targeted plan | Plan: 0 to add, 3 to change, 0 to destroy |  | OPEN |
| D1 | activation | safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 3 changed |  | OPEN |
| V1 | verify | readback CodeSha256 + source map record + dry_run | CodeSha256 = source map, dry_run under 85% of 900 s / 2048 MB, 0 objects written |  | OPEN |
| A1 | verify | first fire A1-A6 incl A4 DELTA=0 | fire request id + A1..A6 read |  | OPEN |

## Log

- 20261009T035219Z OPENED by 0.9.0_WK_IRPT_DASHBD~47 with 4 leg(s)
