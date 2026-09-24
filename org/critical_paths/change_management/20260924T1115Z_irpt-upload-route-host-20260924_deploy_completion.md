# Deploy Completion Record
**Date opened:** 2026-09-24T11:15:17.006935+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate rebuild with the upload POST on its boundary (UploadNotComposed: NOT_READY by name) + the api root's upload route DECLARED against it (CTO batch 28 (iii) / 100535, second act)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| upload-route | activation | aws_apigatewayv2_route.irpt[POST /api/scoped/investor-reporting/analysis/inputs] on API 7k3ed8px20 -> the analysis integration (irpt-ycharts-generate) | TF apply on the api root (1 add) + 0-diff replan + get-routes readback naming the key with the analysis integration |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260924T111517Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
