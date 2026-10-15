# Deploy Completion Record
**Date opened:** 2026-10-15T04:23:21.768287+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-c-9: APPLY the signed pair DB-c-5 (packet blob ad049d506c, COO half @219d7cb42d, CTO half @80a6ca8dd9): rebuild + upload the SHARED zip investor-reporting/irpt-holdings-performance-lambda.zip (run by irpt-holdings-performance-lambda [49F], irpt-inf-holdings-performance-lambda [INF] and the NEW irpt-cot-holdings-performance-lambda [COT]), ONE safe-apply creating the Cottonwood function, 2 roles, DISABLED schedule irpt-cot-holdings-performance-daily, 12-date catch-up (36 keys, opal-data-cottonwood gold), reader check, then schedule ENABLED
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates + BEFORE reads: packet blob, halves, open-marker scan over every live worktree, role name, listing grants, live CodeSha256 of the 49F and INF functions, COT function and schedule absent, 36 keys absent | the printed reads |  | OPEN |
| L2 | s3-prefix | shared zip investor-reporting/irpt-holdings-performance-lambda.zip: BUILD, member diff vs live is exactly handler.py, then upload; new VersionId; built==landed | built CodeSha256, upload_member_diff, VersionId |  | OPEN |
| L3 | verify | fmt -check (two pre-existing INF hunks only), validate, saved plan: adds only irpt_holdings_performance_cot*, changes exactly the 49F and INF functions, 0 destroy | plan line and addresses |  | OPEN |
| L4 | activation | ONE safe-apply on the saved plan (Cottonwood function, 2 roles + policies, DISABLED schedule; 49F + INF functions take the new code); live CodeSha256 of all THREE equal the built; replan No changes | apply line, three read-backs, replan line |  | OPEN |
| L5 | activation | 12-date catch-up by the Cottonwood handler event only, oldest first (2026-09-28..2026-10-13), 36 keys | 12 return payloads, 36 keys listed |  | OPEN |
| L6 | verify | after-read (36 keys, window writes exactly those, newest 2026-10-13, schema 1.2) + 3 readers clean on one 1.1 and one 1.2 partition + planted listing test | LIST, reader_check, pytest rc |  | OPEN |
| L7 | activation | ENABLE: schedule.tf one line DISABLED->ENABLED, plan 0/1/0, ONE safe-apply, schedule read back ENABLED cron(15 8 ? * MON-FRI *) America/New_York | plan line, apply line, get-schedule |  | OPEN |
| L8 | verify | FIRST SCHEDULED FIRE after the enable (next 08:15 New York weekday): T-1 partition lands or a named hold; read by the issuer 2.0.0_SA_COO~C2 | the issuer's read |  | OPEN |

## Log

- 20261015T042321Z OPENED by 0.7.0_AE_CloudOps~DB2 with 8 leg(s)
