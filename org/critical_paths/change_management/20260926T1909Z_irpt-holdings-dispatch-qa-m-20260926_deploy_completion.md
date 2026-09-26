# Deploy Completion Record
**Date opened:** 2026-09-26T19:09:05.324487+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T191503Z
**Deploy:** R4 step 3 prep: redeploy irpt-holdings-refresh-lambda with the QA fire (145c5e6494); schedule stays DISABLED, no served output
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-holdings-refresh-lambda.zip | build-and-upload OK + head-object sha256 metadata == source-map artifact_sha256 | build-and-upload.sh investor-reporting irpt-holdings-refresh-lambda OK; head-object investor-reporting/irpt-holdings-refresh-lambda.zip 3,507 bytes 2026-09-26T19:09:14Z, metadata content-sha256 SGwrvwLH8fhriLW03s/oXMPE1Whjhix8pwKJYHhWKwI= == lambda-source-map artifact_sha256 | CLOSED 20260926T191058Z |
| T1 | tf-lambda | aws_lambda_function irpt-holdings-refresh-lambda (directory root, -target) | safe-apply 0 add / 1 change / 0 destroy | HALT_ACK=1 safe-apply (terraform 1.14.5) -chdir=investor-reporting/directory -target=module.irpt_holdings_refresh.aws_lambda_function.this: Apply complete 0 added, 1 changed, 0 destroyed (s3_object_version UPPT76... -> 8bREa5Al..., source_code_hash -> SGwrvwLH...) | CLOSED 20260926T191503Z |
| V1 | verify | the deployed function | get-function CodeSha256 == artifact sha256; schedule State DISABLED; targeted re-plan No changes | get-function-configuration CodeSha256 SGwrvwLH8fhriLW03s/oXMPE1Whjhix8pwKJYHhWKwI= (== artifact), LastModified 2026-09-26T19:13:41Z, Active/Successful; scheduler irpt-holdings-snapshot DISABLED; targeted re-plan: No changes | CLOSED 20260926T191503Z |

## Log

- 20260926T190905Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20260926T191058Z LEG A1 closed: build-and-upload.sh investor-reporting irpt-holdings-refresh-lambda OK; head-object investor-reporting/irpt-holdings-ref
- 20260926T191503Z LEG T1 closed: HALT_ACK=1 safe-apply (terraform 1.14.5) -chdir=investor-reporting/directory -target=module.irpt_holdings_refresh.aws_la
- 20260926T191503Z LEG V1 closed: get-function-configuration CodeSha256 SGwrvwLH8fhriLW03s/oXMPE1Whjhix8pwKJYHhWKwI= (== artifact), LastModified 2026-09-2
- 20260926T191503Z CLOSED -- all 3 legs proven
