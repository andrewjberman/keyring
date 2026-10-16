# Deploy Completion Record
**Date opened:** 2026-10-16T05:00:00.996440+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-612 (AMENDMENT 1): move the THREE holdings-performance functions (49F, INF, COT: one shared artifact key) from CodeSha256 o9UugRAV.. to the signed candidate LiDXhN74.. by one Terraform plan of 3 changes; Branch B = S3 version MP3woT7ipkN4N3hcclPj3.LFigL3MEqO of investor-reporting/irpt-holdings-performance-lambda.zip
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates and BEFORE reads: pair sha256, addenda blobs, three CTO halves, ledgers and markers, live CodeSha256 of all three, reader census, Branch B version | the printed reads |  | OPEN |
| L2 | s3-prefix | source-map rows of irpt-holdings-performance-lambda only (2), BUILD_ONLY digest equals LiDXhN74.. then ONE upload to the shared key, head-object, new VersionId, built==landed | digest, VersionId |  | OPEN |
| L3 | verify | saved plan reads exactly 3 to change, 0 to add, 0 to destroy, only s3_object_version and source_code_hash of the three functions | plan line |  | OPEN |
| irpt-inf-holdings-performance-lambda | tf-lambda | module.irpt_holdings_performance_inf.aws_lambda_function.this | same safe-apply on the same saved plan; live CodeSha256 equals the built digest |  | OPEN |
| irpt-cot-holdings-performance-lambda | tf-lambda | module.irpt_holdings_performance_cot.aws_lambda_function.this | same safe-apply on the same saved plan; live CodeSha256 equals the built digest |  | OPEN |
| L4 | verify | after-read: each CodeSha256 equals built, re-plan 0, exactly the two members differ, deployed handler date line | the reads |  | OPEN |
| L5 | verify | health proof at least 10 minutes after the apply, per function: Invocations, Errors, Throttles, log group Traceback, Task timed out, ERROR | window, counts |  | OPEN |
| L6 | verify | first scheduled runs: 49F split_adjust declared and counts; each sibling DELTA = 0 (non-writing replay, only the split_adjust key added) | per-function reads |  | OPEN |
| irpt-holdings-performance-lambda | tf-lambda | module.irpt_holdings_performance.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T050000Z OPENED by 0.7.0_AE_CloudOps~IB2 with 9 leg(s)
