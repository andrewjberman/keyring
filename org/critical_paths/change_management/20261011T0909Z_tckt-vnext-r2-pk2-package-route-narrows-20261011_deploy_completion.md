# Deploy Completion Record
**Date opened:** 2026-10-11T09:09:40.624063+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R2-pk-2: opal-ticket-api package route narrows (no ticket on 200 and on the changed-under-write 409; five 409s gain a code), CODE ONLY, at box/dell2 pin be67d1fd38
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | the three STOPs and the BEFORE state, before any write | STOP 1 git diff pin..HEAD over the handler and the tf dir is EMPTY with a live positive control; STOP 2 the deployed lambda_function.py sha256 is ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade; STOP 3 the Lambda running opal_packager.py is NAMED with its live CodeSha256, its live package downloaded, and its attach call shown to discard the answer as the tree does (call at :269, discarded result at :183); AC1 r2_checks.py pk-200 reads PK-200-OK; BEFORE CodeSha256 (expect W03VREoM), the 8 env key names, opal-tickets ItemCount, and the status/assignee/created_by of TCK-20261009-a1052909 |  | OPEN |
| S1 | s3-prefix | build and upload the opal-ticket-api artifact | the zip content-sha256 recorded AND the zip lambda_function.py hashes to cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74 or STOP |  | OPEN |
| S2 | activation | ONE safe-apply in infra/aws/terraform/ticket-center, with NO MSYS_NO_PATHCONV=1 on the wrapper | branch A is exactly 0 to add 1 to change 0 to destroy; anything else is a STOP |  | OPEN |
| S3 | verify | the five after-reads of step 7 | (a) CodeSha256 equals the zip and the deployed file is cf10e19e...; (b) env unchanged at 8 keys; (c) unauthenticated POST to /api/scoped/tickets/TCK-20261009-a1052909/package through CloudFront refused 401; (d) ItemCount unchanged and the control ticket reads the same status fields; (e) the replan is 0-diff |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T090940Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
