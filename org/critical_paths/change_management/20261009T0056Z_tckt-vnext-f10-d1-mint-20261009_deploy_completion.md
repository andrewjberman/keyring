# Deploy Completion Record
**Date opened:** 2026-10-09T00:56:24.574888+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT F10: opal-ticket-api code at 3b04c040fc + the ONE new package route + COMMENTARY_ALLOWED_FIRMS (leg D), then the svc-commentary mint (leg M), on dell2
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D2 | activation | the ONE new route named package and the ONE new env key COMMENTARY_ALLOWED_FIRMS on opal-ticket-api (a Lambda -- a describe-task-definition family sweep DOES NOT APPLY, stated per step 0; the only puller of this artifact key is opal-ticket-api itself) | plan 1 to add 1 to change 0 to destroy and nothing else; env gains exactly COMMENTARY_ALLOWED_FIRMS byte-exact |  | OPEN |
| V1 | verify | the six after-reads (a)-(f) | CodeSha256 == the step-3 zip content-sha256; 8 env keys; deployed lambda_function.py sha256 == 01534e2d452acd02257cb6465cf2e2cf10dced3bea157e7afc9c66bc46ec4f64; the package route exists; an unauthenticated POST /api/scoped/tickets through CloudFront refused; opal-tickets ItemCount unchanged at 12; a 0-diff plan |  | OPEN |
| M1 | activation | mint svc-commentary and store the new secret opal/ticketing/svc-commentary | positive create; the CTO two negative arms plus LIST refused, each with route, status and row count; the claim read-back with the token NEVER printed; the test ticket id recorded |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T005624Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
