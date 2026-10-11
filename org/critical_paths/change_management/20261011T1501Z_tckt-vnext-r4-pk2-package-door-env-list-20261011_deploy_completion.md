# Deploy Completion Record
**Date opened:** 2026-10-11T15:01:44.171913+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R4-pk-2: opal-ticket-api code at f239b06ad8 PLUS one new EMPTY env key PACKAGE_ALLOWED_FIRMS (BRANCH E -- the door admits nobody), ONE safe-apply, then the deploy record
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | the two STOPs and the BEFORE state, before any write | STOP 1 git diff f239b06ad8..HEAD over the handler and the tf dir is EMPTY before my own step-3 edit, with a live positive control; STOP 2 the deployed lambda_function.py sha256 is dc0cd973c61f4b037e7181f4675ec8ffe2ec68414cfd9e036c01f4096f386a15; BEFORE CodeSha256 (expect 20v0+vfe), the env key NAMES and count (expect 8) with a sha256 of EACH value and NO contents printed for TICKET_DL_MAP or CLIENT_LINK_MAP, opal-tickets ItemCount, and the status/assignee/created_by of TCK-20261009-a1052909 |  | OPEN |
| S1 | git | THE ONE EDIT: add the comment line and PACKAGE_ALLOWED_FIRMS = "" to main.tf beside COMMENTARY_ALLOWED_FIRMS, and commit that file ALONE | the committed diff touches exactly one file and adds exactly the comment plus one key with an EMPTY value, per CTO half BRANCH E; no firm is added, since a list with a firm in it is outside this order |  | OPEN |
| S2 | s3-prefix | build and upload the opal-ticket-api artifact | the zip content-sha256 recorded AND the zip lambda_function.py hashes to c40036677aae180cb362f89f2c2aecb62ef53fd0b1a285bb3bd2c813176c1026 or STOP |  | OPEN |
| S3 | activation | ONE safe-apply in infra/aws/terraform/ticket-center, with NO MSYS_NO_PATHCONV=1 | branch A is 0 to add 1 to change 0 to destroy, carrying the function's source_code_hash AND exactly ONE env key added with an empty value; any other resource, or any other env key in the diff, is a STOP |  | OPEN |
| S4 | verify | the five after-reads of step 6 | (a) CodeSha256 equals the zip and the deployed file is c4003667...; (b) the env has 9 key names, the 8 old values hash the same as in step 2, and PACKAGE_ALLOWED_FIRMS is present with its value length printed as 0; (c) unauthenticated POSTs to BOTH /package and /report refused 401; (d) ItemCount unchanged and the control ticket reads the same status fields; (e) the replan is 0-diff |  | OPEN |
| S5 | verify | the deploy RECORD and the clamp precheck on the new build | record-terraform-deploy.sh for opal-ticket-api with STOP 3 (if it lands only one of its two halves, STOP and report which; do NOT hand-edit the map, row TCKT_VNEXT-D2-S36); then clamp_precheck.py --out deliverables/r4_pk2/clamp_precheck_table.json reads READ27 27/27 with the opal-ticket-api line CLAMPED on the NEW build |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T150144Z OPENED by 0.7.0_AE_CloudOps~TV2 with 7 leg(s)
