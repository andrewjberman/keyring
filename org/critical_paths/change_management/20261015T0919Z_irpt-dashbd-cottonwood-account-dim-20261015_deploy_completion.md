# Deploy Completion Record
**Date opened:** 2026-10-15T09:19:55.932178+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-c-20: APPLY the signed pair DB-c-19 (packet blob ed09e2768f, COO half @d405648eff, CTO half @055825367e): upload ONE artifact object investor-reporting/irpt-cot-account-dim-lambda.zip, ONE safe-apply creating 7 resources (function irpt-cot-account-dim-lambda, role irpt-cot-account-dim-role, its scheduler role, 2 policies, log group, schedule irpt-cot-account-dim-daily DISABLED), ONE invoke for 2026-10-13 writing ONE gold key irpt/cottonwood/gold/account_dim/date=2026-10-13/data.parquet in opal-data-cottonwood, after-read, then schedule ENABLED cron(45 8 ? * MON-FRI *) America/New_York
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates + BEFORE reads: packet blob, halves, marker scan over every live worktree, bucket fence admits irpt-cot-account-dim-role, layer irpt-performance-native-layer exists, function/roles/schedule absent, account_dim prefix 0 objects, other gold prefixes listed | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip + package test rc 0, then upload ONE new object investor-reporting/irpt-cot-account-dim-lambda.zip; new VersionId; built==landed | zip sha256, test rc, VersionId |  | OPEN |
| L3 | verify | fmt -check, init, validate, saved plan: exactly 7 adds all irpt_account_dim, schedule DISABLED, 0 change, 0 destroy | plan line and addresses |  | OPEN |
| L4 | activation | ONE safe-apply on the saved plan; function irpt-cot-account-dim-lambda handler/runtime/role/layer, both roles, schedule DISABLED read back; replan No changes | apply line, read-backs, replan line |  | OPEN |
| L5 | activation | ONE invoke of irpt-cot-account-dim-lambda {date 2026-10-13}, no retry, writes ONE gold key | response and the key |  | OPEN |
| L6 | verify | after-read: exactly one key under account_dim, written in the window; parquet rows and schema hash equal the contract; silver unchanged; no other gold prefix moved by this act | LIST, row count, schema hash |  | OPEN |
| L7 | activation | ENABLE: account-dim schedule.tf one line DISABLED->ENABLED, plan 0/1/0, ONE safe-apply, schedule read back ENABLED cron(45 8 ? * MON-FRI *) America/New_York | plan line, apply line, get-schedule |  | OPEN |
| L8 | verify | FIRST SCHEDULED FIRE after the enable (next 08:45 New York weekday): T-1 key lands or a named hold; read by the issuer 2.0.0_SA_COO~C2 | the issuer's read |  | OPEN |

## Log

- 20261015T091955Z OPENED by 0.7.0_AE_CloudOps~DB2 with 8 leg(s)
