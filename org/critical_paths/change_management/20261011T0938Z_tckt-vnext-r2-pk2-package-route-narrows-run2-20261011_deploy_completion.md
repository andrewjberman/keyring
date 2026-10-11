# Deploy Completion Record
**Date opened:** 2026-10-11T09:38:50.879382+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R2-pk-2 SECOND GO (AMENDMENT 1 @c492e616f6): opal-ticket-api package route narrows, CODE ONLY, at box/dell2 pin be67d1fd38; STOP 3 met by the record, not a function digest
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | STOPs 1 and 2 re-read LIVE, STOP 3 as the restated record, and the BEFORE state | STOP 1 git diff be67d1fd38..HEAD over the handler and the tf dir is EMPTY with a live positive control; STOP 2 the deployed lambda_function.py sha256 is ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade; STOP 3 is the record, written with BOTH reads beside each other and claiming NO deployed caller was read -- (i) N=17 Lambdas swept by content, 0 carry opal_packager.py (my read, whose population was Lambdas and so could neither find nor rule out a non-Lambda host) and (ii) running resident root e606008994-st27: opal_packager.py absent, no packager binding, build input and host bytes not listed (2.0.0_SA_COO~G2 msg 4594); AC1 r2_checks.py pk-200 reads PK-200-OK; BEFORE CodeSha256, the 8 env key names, opal-tickets ItemCount and the control ticket's status fields |  | OPEN |
| S1 | s3-prefix | build and upload the opal-ticket-api artifact | the zip content-sha256 recorded AND the zip lambda_function.py hashes to cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74 or STOP |  | OPEN |
| S2 | activation | ONE safe-apply in infra/aws/terraform/ticket-center, with NO MSYS_NO_PATHCONV=1 on the wrapper | branch A is exactly 0 to add 1 to change 0 to destroy; anything else is a STOP |  | OPEN |
| S3 | verify | the five after-reads of step 7 | (a) CodeSha256 equals the zip and the deployed file is cf10e19e...; (b) env unchanged at 8 keys; (c) unauthenticated POST to the package route through CloudFront refused 401; (d) ItemCount unchanged and the control ticket reads the same status fields; (e) the replan is 0-diff |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T093850Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
