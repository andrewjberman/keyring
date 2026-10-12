# Deploy Completion Record
**Date opened:** 2026-10-12T13:46:52.689160+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T135222Z
**Deploy:** HVST-bx-2 deploy the fenced opal-research-pull-enqueue handler
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | zip built from 824bdb355b lambda_function.py (sha256 c1f8e725...) | zip member sha256 equals git show 824bdb355b:infra/aws/lambda/research/pull_enqueue/lambda_function.py | zip member lambda_function.py sha256 c1f8e725aaa6d3df946fcce6cb66e7044dba30419a2150a77cb3c007aece4ed8 == git show 824bdb355b:infra/aws/lambda/research/pull_enqueue/lambda_function.py (EQUAL True); positive control: <M>~1 file b64c8932... DIFFERS | CLOSED 20261012T134749Z |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | s3 object read back, content-sha256 equals the built zip | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=bSNW5xyLGyzTAHsP2xN.9BfjDIT2SF79 ContentLength=2437 content-sha256(b64)=+e2doUmH+f3S3xWeqbe/XHniGRgzaD8648Pv4eqjh88= read back, matches (upload_verified.sh); object re-downloaded, member hash verified | CLOSED 20261012T134749Z |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 changed from THhzBXqTs1XoNok2IyKS5z+y3RE41aqUMIw4Bno53NM= | plan 0 to add, 1 to change, 0 to destroy (bx2_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (bx2_apply.out); get-function-configuration CodeSha256 THhzBXqTs1XoNok2IyKS5z+y3RE41aqUMIw4Bno53NM= -> +e2doUmH+f3S3xWeqbe/XHniGRgzaD8648Pv4eqjh88= == uploaded object content-sha256, State Active/LastUpdateStatus Successful, LastModified 2026-10-12T13:50:11Z (bx2_after.out CODESHA256 CHANGED: yes); comp-iam service read identical before/after | CLOSED 20261012T135213Z |
| ARMS | verify | opal-research-pull-enqueue deployed function, three no-ticker invokes | non_internal 403, no_context 403, internal_no_ticker 400 | deployed opal-research-pull-enqueue, three invokes, no payload carries ticker/body: ARM non_internal statusCode 403; ARM no_context statusCode 403; ARM internal_no_ticker statusCode 400 (bx2_arms.out; responses arm_*.response.json); invoke StatusCode 200 x3, no FunctionError | CLOSED 20261012T135213Z |

## Log

- 20261012T134652Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)
- 20261012T134749Z LEG BUILD closed: zip member lambda_function.py sha256 c1f8e725aaa6d3df946fcce6cb66e7044dba30419a2150a77cb3c007aece4ed8 == git show 824bdb
- 20261012T134749Z LEG UPLOAD closed: s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=bSNW5xyLGyzTAHsP2xN.9BfjDIT2SF
- 20261012T135213Z LEG APPLY closed: plan 0 to add, 1 to change, 0 to destroy (bx2_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 
- 20261012T135213Z LEG ARMS closed: deployed opal-research-pull-enqueue, three invokes, no payload carries ticker/body: ARM non_internal statusCode 403; ARM
- 20261012T135222Z CLOSED -- all 4 legs proven
