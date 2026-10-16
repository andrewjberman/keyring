# Deploy Completion Record
**Date opened:** 2026-10-16T05:54:23.480165+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R35L (AR-g-117): irpt-status code CodeSha256 OOez8YSm... -> +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A= (pin 90b69dcb12, 3 of 49 members: durable_job.py owned_status.py status.py; the closed failure code and its words): BUILD_ONLY digest check, one upload, scoped plan 0/1/0, safe-apply, V reads; COO half blob 3092cf2a13, CTO half msg 9106
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-status.zip one new object version, sha256 f937190d... | the build digest +TcZDWmwE... equal then the object read-back and VersionId |  | OPEN |
| C | verify | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only) then safe-apply | the plan line and the apply line |  | OPEN |
| V | verify | V: G1 CodeSha256, G2 delta exactly 3 of 49, G3 refusal envelope equal, G4 READY report read byte-identical, G5 census 0 | the printed reads |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T055423Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
