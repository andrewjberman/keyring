# Deploy Completion Record
**Date opened:** 2026-10-02T13:26:37.447215+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-8: apply the reporting-publish root (publisher function + 08:15 ET weekday schedule); packet blob 38a6eb19a1, COO half + CTO half (c272931fcf, batch 168)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | terraform plan of infra/aws/terraform/investor-reporting/reporting-publish | 7 to add, 0 to change, 0 to destroy |  | OPEN |
| D1 | activation | targeted safe-apply of the saved plan | Apply complete 7/0/0 |  | OPEN |
| V1 | verify | get-function-configuration irpt-49f-reporting-publish-lambda + get-schedule + re-plan | CodeSha256 = gZM/pg..., schedule ENABLED cron(15 8 ? * MON-FRI *) America/New_York, re-plan No changes |  | OPEN |
| Q1 | verify | ONE ad hoc QA invoke, no arguments (CTO half, batch 168) | 12 new versions as_of 2026-10-01; page Data through moves 09-28 -> 10-01 |  | OPEN |
| A1 | verify | first scheduled fire Monday 2026-10-05 08:15 ET, no seat starting it | 12 keys as_of T-1 (2026-10-02 by branch A); page Data through that date |  | OPEN |

## Log

- 20261002T132637Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
