# Deploy Completion Record
**Date opened:** 2026-10-12T13:46:52.689160+00:00
**Status:** OPEN
**Deploy:** HVST-bx-2 deploy the fenced opal-research-pull-enqueue handler
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | zip built from 824bdb355b lambda_function.py (sha256 c1f8e725...) | zip member sha256 equals git show 824bdb355b:infra/aws/lambda/research/pull_enqueue/lambda_function.py |  | OPEN |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | s3 object read back, content-sha256 equals the built zip |  | OPEN |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 changed from THhzBXqTs1XoNok2IyKS5z+y3RE41aqUMIw4Bno53NM= |  | OPEN |
| ARMS | verify | opal-research-pull-enqueue deployed function, three no-ticker invokes | non_internal 403, no_context 403, internal_no_ticker 400 |  | OPEN |

## Log

- 20261012T134652Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)
