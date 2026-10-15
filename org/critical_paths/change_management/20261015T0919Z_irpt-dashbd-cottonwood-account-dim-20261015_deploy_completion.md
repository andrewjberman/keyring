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
| L1 | verify | gates + BEFORE reads: packet blob, halves, marker scan over every live worktree, bucket fence admits irpt-cot-account-dim-role, layer irpt-performance-native-layer exists, function/roles/schedule absent, account_dim prefix 0 objects, other gold prefixes listed | the printed reads | packet blob ed09e2768fd13983291ceafbed44ddd54ac69e13 equal; both halves SIGNED at it; a4a8375b21 ancestor of HEAD a4dd84c869; marker scan over 23 live worktrees (content grep of .open_deploys for account-dim): 0 hits, 0 ledger files name account-dim; LIVE bucket policy opal-data-cottonwood (4 statements): DenyForeignFirmPrincipals ArnNotLike admits role/*-cot-* which irpt-cot-account-dim-role matches, no statement names account_dim, the 3 restricted denies name only the commonwealth/cottonwood/bronze/crm prefix; layer irpt-performance-native-layer version 1 exists (python3.12, 69899991 bytes); function, role, scheduler role (irpt-cot-account-dim-scheduler-role) and schedule absent (ResourceNotFound/NoSuchEntity); account_dim prefix 0 objects; other gold prefixes (7): account_return_daily 6650, blank_reasons 1, dim_return_method 2, holdings 15, holdings_performance_daily 87, holdings_performance_manifest 174, holdings_qa 5 | CLOSED 20261015T092209Z |
| L2 | s3-prefix | BUILD_ONLY zip + package test rc 0, then upload ONE new object investor-reporting/irpt-cot-account-dim-lambda.zip; new VersionId; built==landed | zip sha256, test rc, VersionId | BUILD_ONLY zip sha256 t+HiXAoUy+8KB+WtLFVT9mlzkVpvHzymxojF7skZyPA= 15 members (lambda_function.py + the 14 staged_from members at their packaged_as paths); package test ADCOT_ZIP_PATH=<built> test_package_resolves.py rc 0 (negative control: the zip without scopes.json FAILS rc 1); real upload 2026-10-15T09:23:04Z ONE new object s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-cot-account-dim-lambda.zip VersionId bwcGdAwAlh.wCPogjrdlllhG1buOm50Q size 143098, content-sha256 metadata equals the built zip (built_equals_landed true), 1 version of the key exists; source map diff = the entry's artifact_sha256 only | CLOSED 20261015T092331Z |
| L3 | verify | fmt -check, init, validate, saved plan: exactly 7 adds all irpt_account_dim, schedule DISABLED, 0 change, 0 destroy | plan line and addresses |  | OPEN |
| L4 | activation | ONE safe-apply on the saved plan; function irpt-cot-account-dim-lambda handler/runtime/role/layer, both roles, schedule DISABLED read back; replan No changes | apply line, read-backs, replan line |  | OPEN |
| L5 | activation | ONE invoke of irpt-cot-account-dim-lambda {date 2026-10-13}, no retry, writes ONE gold key | response and the key |  | OPEN |
| L6 | verify | after-read: exactly one key under account_dim, written in the window; parquet rows and schema hash equal the contract; silver unchanged; no other gold prefix moved by this act | LIST, row count, schema hash |  | OPEN |
| L7 | activation | ENABLE: account-dim schedule.tf one line DISABLED->ENABLED, plan 0/1/0, ONE safe-apply, schedule read back ENABLED cron(45 8 ? * MON-FRI *) America/New_York | plan line, apply line, get-schedule |  | OPEN |
| L8 | verify | FIRST SCHEDULED FIRE after the enable (next 08:45 New York weekday): T-1 key lands or a named hold; read by the issuer 2.0.0_SA_COO~C2 | the issuer's read |  | OPEN |

## Log

- 20261015T091955Z OPENED by 0.7.0_AE_CloudOps~DB2 with 8 leg(s)
- 20261015T092209Z LEG L1 closed: packet blob ed09e2768fd13983291ceafbed44ddd54ac69e13 equal; both halves SIGNED at it; a4a8375b21 ancestor of HEAD a4dd84
- 20261015T092331Z LEG L2 closed: BUILD_ONLY zip sha256 t+HiXAoUy+8KB+WtLFVT9mlzkVpvHzymxojF7skZyPA= 15 members (lambda_function.py + the 14 staged_from m
