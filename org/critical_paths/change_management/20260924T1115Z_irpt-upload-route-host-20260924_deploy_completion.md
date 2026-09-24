# Deploy Completion Record
**Date opened:** 2026-09-24T11:15:17.006935+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T112429Z
**Deploy:** irpt-ycharts-generate rebuild with the upload POST on its boundary (UploadNotComposed: NOT_READY by name) + the api root's upload route DECLARED against it (CTO batch 28 (iii) / 100535, second act)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload-route | activation | aws_apigatewayv2_route.irpt[POST /api/scoped/investor-reporting/analysis/inputs] on API 7k3ed8px20 -> the analysis integration (irpt-ycharts-generate) | TF apply on the api root (1 add) + 0-diff replan + get-routes readback naming the key with the analysis integration | TF apply on the api root 1 added 0 changed 0 destroyed (upload-route.tfplan); replan rc=0 No changes; get-routes readback: POST /api/scoped/investor-reporting/analysis/inputs -> integrations/wtho3v4 (get-integration: irpt-ycharts-generate/invocations), authorizer naqxlm, route id 0sp6wva | CLOSED 20260924T112429Z |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 0 added 1 changed 0 destroyed (safe-apply, upload-host.tfplan, 11:21:10Z); replan rc=0; get-function-configuration CodeSha256 4fkloyC1HaICo2OboVZgSFSapRJQlM5+ErEKWm0SCnU= == uploaded (S3 version .bbyrCYyj1SSmKOLQ4O_S3XI_wMu8xTr), handler generate_installed.lambda_handler unchanged, Active Successful, IRPT_LIVE_YCHARTS_CALL absent, 0 event source mappings; packaged X10 row ACTIVE (unzipped); verify-on-served: invoke {} -> 200 CONTRACT_VERSION (the container composed, request 76aab1cf-93d5-47a7-870e-a1c3ffd447ec), unsigned upload POST -> 200 operation analysis-input-upload NOT_AUTHORIZED by name (request f8ce6cc8-500f-4630-acf0-7891464c419c) | CLOSED 20260924T112429Z |

## Log

- 20260924T111517Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260924T112429Z LEG irpt-ycharts-generate closed: TF apply 0 added 1 changed 0 destroyed (safe-apply, upload-host.tfplan, 11:21:10Z); replan rc=0; get-function-configurat
- 20260924T112429Z LEG upload-route closed: TF apply on the api root 1 added 0 changed 0 destroyed (upload-route.tfplan); replan rc=0 No changes; get-routes readbac
- 20260924T112429Z CLOSED -- all 2 legs proven
