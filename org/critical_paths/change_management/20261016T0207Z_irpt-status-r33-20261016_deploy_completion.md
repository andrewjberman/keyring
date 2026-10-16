# Deploy Completion Record
**Date opened:** 2026-10-16T02:07:29.020190+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R33 unit S (AR-g-104): irpt-status code CodeSha256 PcGK+EpS... -> OOez8YSm... (pin 927337a741, status.py only, 49 members): BUILD_ONLY digest check, one upload, scoped plan 0/1/0, safe-apply, V-S reads; applied BEFORE irpt-ycharts-generate (CTO condition 4)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-status.zip one new object version, sha256 38e7b3f1... | the build digest OOez8YSm... equal then the object read-back and VersionId |  | OPEN |
| C | verify | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only) then safe-apply | the plan line and the apply line |  | OPEN |
| V | verify | V-S: G1 CodeSha256, G2 delta exactly status.py of 49, G3 refusal envelope equal | the printed reads |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T020729Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
