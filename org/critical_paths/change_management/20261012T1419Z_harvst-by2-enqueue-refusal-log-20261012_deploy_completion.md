# Deploy Completion Record
**Date opened:** 2026-10-12T14:19:33.211692+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T142432Z
**Deploy:** HVST-by-2 deploy the refusal-logging opal-research-pull-enqueue handler
**Authored by:** 0.7.0_AE_CloudOps~HV1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| BUILD | verify | zip built from 31590746f1 lambda_function.py (sha256 1778584a...) | zip member sha256 equals git show 31590746f1:infra/aws/lambda/research/pull_enqueue/lambda_function.py | zip member lambda_function.py sha256 1778584aa7309505cc3c2252dd863cd21d405f074be6b0f57d25fa96ed33f484 == git show 31590746f1:infra/aws/lambda/research/pull_enqueue/lambda_function.py (EQUAL True) == working file; positive control: <M>~1 file c1f8e725... DIFFERS | CLOSED 20261012T142026Z |
| UPLOAD | activation | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip | s3 object read back, content-sha256 equals the built zip | s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=S9217s5ck1gZJvwSC.Ayeg4vFAkV063z ContentLength=2690 content-sha256(b64)=cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= read back, matches (upload_verified.sh); object re-downloaded, member hash verified | CLOSED 20261012T142026Z |
| APPLY | activation | module.harvest_enqueue in infra/aws/terraform/harvest (targeted, safe-apply) | plan 0 add 1 change 0 destroy; CodeSha256 changed from +e2doUmH+f3S3xWeqbe/XHniGRgzaD8648Pv4eqjh88= | plan 0 to add, 1 to change, 0 to destroy (by2_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (by2_apply.out); CodeSha256 +e2doUmH+f3S3xWeqbe/XHniGRgzaD8648Pv4eqjh88= -> cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo= == uploaded object content-sha256, State Active/LastUpdateStatus Successful, LastModified 2026-10-12T14:22:19Z (by2_after.out CODESHA256 CHANGED: yes); comp-iam service read identical before/after | CLOSED 20261012T142431Z |
| ARMS | verify | opal-research-pull-enqueue deployed function, three no-ticker invokes, then the log read | non_internal 403, no_context 403, internal_no_ticker 400; DENIED lines tier=partner and tier=NONE, 0 for internal | deployed function, three invokes, no payload carries ticker/body: ARM non_internal statusCode 403; ARM no_context statusCode 403; ARM internal_no_ticker statusCode 400 (by2_arms.out); log read since T0=14:19:03Z: exactly 2 DENIED events, DENIED: tier=partner and DENIED: tier=NONE, both inside this seat's arm window; DENIED LINES FOR internal: 0 (by2_log.out) | CLOSED 20261012T142431Z |

## Log

- 20261012T141933Z OPENED by 0.7.0_AE_CloudOps~HV1 with 4 leg(s)
- 20261012T142026Z LEG BUILD closed: zip member lambda_function.py sha256 1778584aa7309505cc3c2252dd863cd21d405f074be6b0f57d25fa96ed33f484 == git show 315907
- 20261012T142026Z LEG UPLOAD closed: s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip VersionId=S9217s5ck1gZJvwSC.Ayeg4vFAkV06
- 20261012T142431Z LEG APPLY closed: plan 0 to add, 1 to change, 0 to destroy (by2_plan.out); safe-apply of the saved planfile: Apply complete! Resources: 0 
- 20261012T142431Z LEG ARMS closed: deployed function, three invokes, no payload carries ticker/body: ARM non_internal statusCode 403; ARM no_context status
- 20261012T142432Z CLOSED -- all 4 legs proven
