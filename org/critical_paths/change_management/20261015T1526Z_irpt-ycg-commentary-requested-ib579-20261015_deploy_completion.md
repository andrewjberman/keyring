# Deploy Completion Record
**Date opened:** 2026-10-15T15:26:00.800783+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-579: move irpt-ycharts-generate from CodeSha256 5TRFZf6G.. to the signed candidate 3+fMEJhQ8.. (the commentary_requested release) by its Terraform path; Branch B = S3 version sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C of investor-reporting/irpt-ycharts-generate.zip
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates and BEFORE reads: packet sha256, both halves, ledgers and markers, live CodeSha256, Branch B version, live zip commentary_requested count 0 in the three ENDPOINT members, accepted request item sha256 | the printed reads |  | OPEN |
| L2 | s3-prefix | source-map rows of this function only, BUILD_ONLY digest equals 3+fMEJhQ8.. then upload, head-object, new VersionId, built==landed | digest, VersionId |  | OPEN |
| L3 | verify | saved plan reads 1 to change, 0 to add, 0 to destroy, only s3_object_version and source_code_hash of the one function | plan line |  | OPEN |
| L4 | verify | after-read: CodeSha256 equals built, re-plan 0, exactly the four members differ, import census failed empty, offline replay at the pin, item hash unchanged, composition test | the reads |  | OPEN |
| L5 | verify | health proof at least 10 minutes after the apply: Invocations and Errors, log group Traceback TypeError Task timed out ERROR | window, count, errors |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261015T152600Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
