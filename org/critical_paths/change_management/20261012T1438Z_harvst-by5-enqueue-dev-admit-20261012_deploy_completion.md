# Deploy Completion Record
**Date opened:** 2026-10-12T14:38:27.879655+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T144152Z
**Deploy:** HVST-by-5 deploy the Dev-admitting opal-research-pull-enqueue fence
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | zip built from f94560218c lambda_function.py (sha256 0f2cdd91...) | zip member sha256 equals git show f94560218c:infra/aws/lambda/research/pull_enqueue/lambda_function.py | zip member lambda_function.py sha256 0f2cdd910d9b68a2af64cb313f974833b18184b5bfda0f828a4d9e37ac47a2f1 == git show f94560218c:infra/aws/lambda/research/pull_enqueue/lambda_function.py (EQUAL True) == working file; positive control: <M>~1 file 1778584a... DIFFERS | CLOSED 20261012T143915Z |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | s3 object read back, content-sha256 equals the built zip | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=kwFo21Dq805CaW24uAodJu5WJY.nbvVx ContentLength=2829 content-sha256(b64)=Q342L4VnpBkMJfFt/ughTj2AhS3gIa1n+pmjVqrslu0= read back, matches (upload_verified.sh); object re-downloaded, member hash verified | CLOSED 20261012T143915Z |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 changed from cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= | plan 0 to add, 1 to change, 0 to destroy (by5_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (by5_apply.out); CodeSha256 cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= -> Q342L4VnpBkMJfFt/ughTj2AhS3gIa1n+pmjVqrslu0= == uploaded object content-sha256, State Active/LastUpdateStatus Successful, LastModified 2026-10-12T14:40:46Z (by5_after.out CODESHA256 CHANGED: yes); comp-iam service read identical before/after | CLOSED 20261012T144152Z |
| ARMS | verify | opal-research-pull-enqueue deployed function, four no-ticker invokes | dev_non_internal_tier 400, advisor_non_dev 403, no_context 403, internal_no_ticker 400 | deployed function, four invokes, no payload carries ticker/body: ARM dev_non_internal_tier statusCode 400 (admitted, nothing written); ARM advisor_non_dev statusCode 403; ARM no_context statusCode 403; ARM internal_no_ticker statusCode 400 (by5_arms.out); each Invoke StatusCode 200, no FunctionError | CLOSED 20261012T144152Z |

## Log

- 20261012T143827Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)
- 20261012T143915Z LEG BUILD closed: zip member lambda_function.py sha256 0f2cdd910d9b68a2af64cb313f974833b18184b5bfda0f828a4d9e37ac47a2f1 == git show f94560
- 20261012T143915Z LEG UPLOAD closed: s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=kwFo21Dq805CaW24uAodJu5WJY.nbv
- 20261012T144152Z LEG APPLY closed: plan 0 to add, 1 to change, 0 to destroy (by5_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 
- 20261012T144152Z LEG ARMS closed: deployed function, four invokes, no payload carries ticker/body: ARM dev_non_internal_tier statusCode 400 (admitted, not
- 20261012T144152Z CLOSED -- all 4 legs proven
