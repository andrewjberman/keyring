# Deploy Completion Record
**Date opened:** 2026-10-02T02:23:10.198433+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T031148Z
**Deploy:** IRPT_DASHBD DB-b-2: platinum series + manifest publisher, SERIES contract verified, first local run for the newest-partition accounts, plan of the reporting-publish root
**Authored by:** 0.9.0_WK_IRPT_DASHBD~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | SERIES contract | file written, required/optional lists | org/standards/IRPT_DASHBD_SERIES_CONTRACT.json contract_version 0.1.0 (landed @b80543a03c by the issuer): series.required 13 keys, series.optional [class_value,class_weight,class_names], manifest.required 10 keys; publisher emits exactly the required keys (tests/test_publisher.py test_required_keys_exactly_and_optional_absent, 13 of 13 OK) | CLOSED 20261002T023045Z |
| W1 | activation | series + manifest for the 5 sample accounts | keys, gz sizes, build seconds | local --upload run 6 accounts (every account_id in newest partition 2026-09-28; 559 gold partitions): gz_bytes 0010783709=17665 0027265115=4705 0035940058=4518 0076459710=2195 0084073310=4447 0091939812=3384; build_seconds 0.0056 0.0000 0.0000 0.0000 0.0005 0.0020; keys irpt/49financial/platinum/reporting/account=<id>/{series.json.gz,manifest.json} in opal-data-49financial; rc=0 | CLOSED 20261002T023045Z |
| P1 | verify | plan of the reporting-publish root | 0 destroy; lambda, role, schedule created; artifact uploaded | terraform init + plan -no-color on infra/aws/terraform/investor-reporting/reporting-publish rc=0: 'Plan: 7 to add, 0 to change, 0 to destroy.' creates aws_lambda_function (module.irpt_reporting_publish), aws_iam_role x2 (execution + scheduler), aws_scheduler_schedule irpt-49f-reporting-publish-daily; saved verbatim to org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/reporting-publish.plan.txt; artifact s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-reporting-publish-lambda.zip uploaded, write VERIFIED size=108492 sha256 gZM/pgyLqFICfadTwYF5VkNQDwhoFJbR2YGmjsmbzis=; NO apply | CLOSED 20261002T031126Z |

## Log

- 20261002T022310Z OPENED by 0.9.0_WK_IRPT_DASHBD~1 with 3 leg(s)
- 20261002T023045Z LEG C1 closed: org/standards/IRPT_DASHBD_SERIES_CONTRACT.json contract_version 0.1.0 (landed @b80543a03c by the issuer): series.require
- 20261002T023045Z LEG W1 closed: local --upload run 6 accounts (every account_id in newest partition 2026-09-28; 559 gold partitions): gz_bytes 001078370
- 20261002T031126Z LEG P1 closed: terraform init + plan -no-color on infra/aws/terraform/investor-reporting/reporting-publish rc=0: 'Plan: 7 to add, 0 to 
- 20261002T031148Z CLOSED -- all 3 legs proven
