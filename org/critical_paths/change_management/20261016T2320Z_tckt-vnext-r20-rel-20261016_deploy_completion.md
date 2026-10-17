# Deploy Completion Record
**Date opened:** 2026-10-16T23:20:53.684788+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T233151Z
**Deploy:** TCKT_VNEXT TO-R20-REL (AMENDMENTS 1 and 2): opal-ticket-api CODE-ONLY release for the open route's same-member fence (row C-S11); pair COO blob 2ceb3a22fe, CTO half blob 9597009c5e, built_from_sha 44933b266b, lambda_function.py blob 5968534813, check d300cf7316; one hunk in attachment_open_ticket; one in-place code update, no environment, route or IAM change
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs, CTO count, start condition and live baseline read by the applier | all true and printed | pair blob 2ceb3a22fe, CTO half 9597009c5e (the GO's AMENDMENT 2 correction; file unchanged since its only commit 545bfe0af8), check d300cf7316, lambda_function.py 5968534813 at 44933b266b and HEAD all equal; CTO count scanned=33 with_attachment=19 differ=0 (read twice, last at the apply); census 99 trees read, 0 live open entries naming opal-ticket-api, opal-tickets or opal-users-v2, shared tree none besides this ledger; asked CTO (msg 10013) and IB2 (msg 10014): none open; live CodeSha256 JwdnACONAnxwqzhsVgqgU+nRoLdmS7MyLmzXmZuXsR4= LastModified 19:27:55Z = the pair's baseline | CLOSED 20261016T232427Z |
| B1 | verify | package built from 44933b266b with BUILD_ONLY; member diff against the live member | exactly ONE hunk, one member | built at 44933b266b with BUILD_ONLY=1 (guard 8), one member lambda_function.py git blob 5968534813, 40379 bytes, sha256 hex 891c49658a7a21712d8970d1313e11fc43b02afb2a87921de4d3603dca72dd13, b64 iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM=; diff against the live member (live zip downloaded, its b64 equals CodeSha256): exactly 1 hunk, 6 added 1 removed, in attachment_open_ticket at line 2118 | CLOSED 20261016T232427Z |
| U1 | activation | package uploaded to s3://opal-313476888478-lambda-artifacts/ticket-center/opal-ticket-api.zip with content-sha256 metadata, previous S3 VersionId saved as the rollback | metadata equals the zip sha256 base64 | package iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= (hex 891c49658a7a2171..., 40379 bytes) uploaded, new S3 VersionId 9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK; head-object metadata and round-trip read equal; rollback = S3 VersionId 0iVZCJN6gNZGepFpC3Fw2__53OnCuXja (holds the live code JwdnACON..., copy saved) | CLOSED 20261016T232516Z |
| P1 | verify | terraform plan of infra/aws/terraform/ticket-center saved to a planfile | ONE in-place update, the function code only | plan saved C:/dev/tv2-rel-r20-out/tf.plan from the stack dir (main.tf blob 748e680fd7f8, clean): Plan: 0 to add, 1 to change, 0 to destroy; ONE resource module.opal_ticket_api.aws_lambda_function.this updated in place; changed: s3_object_version 0iVZCJN6gNZGepFpC3Fw2__53OnCuXja -> 9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK, source_code_hash JwdnACON... -> iRxJZYp6..., last_modified (computed); no environment, route, role or policy change; equals the pair section 3 | CLOSED 20261016T232625Z |
| A1 | activation | safe-apply of the saved planfile, function Active and Successful | CodeSha256 equals the package base64 sha256 | safe-apply of the saved planfile rc=0 at 2026-10-16T23:28:32Z: Apply complete! Resources: 0 added, 1 changed, 0 destroyed; live opal-ticket-api State=Active LastUpdateStatus=Successful CodeSha256=iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= (equals the package), 14 environment keys unchanged; post-apply plan: No changes | CLOSED 20261016T233151Z |
| V1 | verify | r20_rel_check.py | REL-OK | r20_rel_check.py (blob d300cf7316): REL-OK code_sha256=iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= fence=present env=unchanged | CLOSED 20261016T233151Z |

## Log

- 20261016T232053Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261016T232427Z LEG S1 closed: pair blob 2ceb3a22fe, CTO half 9597009c5e (the GO's AMENDMENT 2 correction; file unchanged since its only commit 545bfe0
- 20261016T232427Z LEG B1 closed: built at 44933b266b with BUILD_ONLY=1 (guard 8), one member lambda_function.py git blob 5968534813, 40379 bytes, sha256 
- 20261016T232516Z LEG U1 closed: package iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= (hex 891c49658a7a2171..., 40379 bytes) uploaded, new S3 VersionId 9
- 20261016T232625Z LEG P1 closed: plan saved C:/dev/tv2-rel-r20-out/tf.plan from the stack dir (main.tf blob 748e680fd7f8, clean): Plan: 0 to add, 1 to ch
- 20261016T233151Z LEG A1 closed: safe-apply of the saved planfile rc=0 at 2026-10-16T23:28:32Z: Apply complete! Resources: 0 added, 1 changed, 0 destroye
- 20261016T233151Z LEG V1 closed: r20_rel_check.py (blob d300cf7316): REL-OK code_sha256=iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= fence=present env=un
- 20261016T233151Z CLOSED -- all 6 legs proven
