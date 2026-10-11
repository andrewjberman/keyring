# Deploy Completion Record
**Date opened:** 2026-10-11T13:24:26.552035+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R3-rf-2: opal-ticket-api report route also admits the ticket's CREATOR once (THIS WIDENS A WRITER), CODE ONLY, at box/dell2 pin 8ef21584f8; then the deploy record
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | the ordering condition, the two STOPs and the BEFORE state, before any write | the fourth run's ledger entry reads CLOSED and its row absent (the ordering condition: the two acts never overlap on this function); STOP 1 git diff 8ef21584f8..HEAD over the handler and the tf dir is EMPTY with a live positive control; STOP 2 the deployed lambda_function.py sha256 is cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74; BEFORE CodeSha256 (expect t1EoiJRZ), the env key names and count, opal-tickets ItemCount, and the status/assignee/created_by of TCK-20261009-a1052909 |  | OPEN |
| S1 | s3-prefix | build and upload the opal-ticket-api artifact | the zip content-sha256 recorded AND the zip lambda_function.py hashes to dc0cd973c61f4b037e7181f4675ec8ffe2ec68414cfd9e036c01f4096f386a15 or STOP |  | OPEN |
| S2 | activation | ONE safe-apply in infra/aws/terraform/ticket-center, with NO MSYS_NO_PATHCONV=1 on the wrapper | branch A is exactly 0 to add 1 to change 0 to destroy; anything else is a STOP |  | OPEN |
| S3 | verify | the five after-reads of step 6 | (a) CodeSha256 equals the zip and the deployed file is dc0cd973...; (b) env unchanged, same key names and count; (c) unauthenticated POST to the report route through CloudFront refused 401; (d) ItemCount unchanged and the control ticket reads the same status fields; (e) the replan is 0-diff |  | OPEN |
| S4 | verify | the deploy RECORD and the clamp precheck on the new build | record-terraform-deploy.sh for opal-ticket-api as in TO-RECORD-R3-sm1, with STOP 3: if it lands only one of its two halves (the map entry written and its notice not sent, or the reverse) STOP and report which, and do NOT hand-edit the map (row TCKT_VNEXT-D2-S36); then clamp_precheck.py --out deliverables/r3_rf2/clamp_precheck_table.json reads READ27 27/27 with the opal-ticket-api line CLAMPED on the NEW build, which it can only do if the recorder ran |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261011T132426Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
