# Deploy Completion Record
**Date opened:** 2026-10-11T04:03:20.053228+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R2-rr-2: opal-ticket-api report-id shape check, CODE ONLY, at box/dell2 pin a366ce52ec
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | the pre-checks at the pin before any write | STOP 1 git diff pin..HEAD over infra/aws/lambda/ticket_center and infra/aws/terraform/ticket-center is EMPTY with a live positive control; STOP 2 the deployed lambda_function.py sha256 is 670686262068808fcf1d3e0c05ce8e92e32441f9382efeb9361c789ab19457a8; AC1 r2_checks.py rr-shape reads RR-SHAPE-OK; BEFORE CodeSha256 (expect HK82TEd0SQWe...), 8 env key names, opal-tickets ItemCount, and the status/assignee/created_by of TCK-20261009-a1052909 |  | OPEN |
| S1 | s3-prefix | build and upload the opal-ticket-api artifact | the zip content-sha256 recorded AND the zip lambda_function.py hashes to ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade or STOP; say so if the zip carries tests/ |  | OPEN |
| S2 | activation | ONE safe-apply in infra/aws/terraform/ticket-center | branch A is exactly 0 to add 1 to change 0 to destroy; anything else is branch B and a STOP |  | OPEN |
| S3 | verify | the five after-reads of step 6 | (a) CodeSha256 equals the zip and the deployed file is ca3be343...; (b) env unchanged at 8 keys; (c) unauthenticated POST to /api/scoped/tickets/TCK-20261009-a1052909/report through CloudFront refused 401; (d) ItemCount unchanged and TCK-20261009-a1052909 reads the same status fields; (e) the replan is 0-diff |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T040320Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
