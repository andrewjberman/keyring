# Deploy Completion Record
**Date opened:** 2026-10-09T17:27:53.106116+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 REVISION 5 (AMENDMENT 6 @1de19fec83): the FOURTH apply, fixing the rev-4 TypeError that 500'd every caller. PINNED to 54ed3aa8f6 (on origin, control origin/CLOUD discriminates), built DZOdwUOG, rollback rev 3 t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI= which is the CURRENT live state after 0.7.0_AE_CloudOps~AR2 completed Branch B. R0: the member diff must be EXACTLY status_installed.py, composition.py and repository.py. R1: signature_closure.py on the UPLOADED zip. R3: 5xx and TypeError both 0 over 5 minutes PLUS 2.0.0_SA_COO~G2's authorized 200 -- the live-call arm the CTO made standard for every served Lambda release after rev 4 passed its own acceptance while broken. Either R3 limb failing means Branch B. THE LEDGER STAYS OPEN UNTIL R3
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | the uploaded-zip member diff against the LIVE function artifact | EXACTLY status_installed.py, composition.py and repository.py changed, nothing added or removed, or STOP. The live side is read from get_function, never from the S3 key the upload has just overwritten |  | OPEN |
| R1 | verify | signature_closure.py on the UPLOADED zip | it grades the bytes the Lambda will load, not a local rebuild |  | OPEN |
| L1 | s3-prefix | build and upload from a detached worktree at the pin | uploaded sha256 equals DZOdwUOG or STOP |  | OPEN |
| L2 | activation | ONE ops safe-apply from the repo root with -chdir | code-only; any other line is a STOP |  | OPEN |
| R3 | verify | the LIVE arm: 5xx and TypeError 0 over 5 minutes, plus G2 authorized 200 | either limb failing is Branch B back to t6OJTCcm. This is the arm rev 4 lacked, which is why a release that 500d on every call passed its own acceptance |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T172753Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)
