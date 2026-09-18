# Deploy Completion Record
**Date opened:** 2026-09-18T15:47:15.110747+00:00
**Status:** OPEN
**Deploy:** IB-rtd-2 round 2: the missed-fire date is a different question from previous -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-refresh.zip | build-and-upload.sh write-VERIFIED line, sha256 metadata match |  | OPEN |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | plan shows ONLY source_code_hash + s3_object_version changed on module.irpt_directory_refresh.aws_lambda_function.this, 0 to add, 0 to destroy |  | OPEN |
| L3 | verify | lambda get-function-configuration irpt-directory-refresh | CodeSha256 == built zip == source-map registration |  | OPEN |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. |  | OPEN |
| L5 | git | wk-irpt_bckend-4-2b | the code, the tests and the source map, committed BEFORE the apply |  | OPEN |

## Log

- 20260918T154715Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
