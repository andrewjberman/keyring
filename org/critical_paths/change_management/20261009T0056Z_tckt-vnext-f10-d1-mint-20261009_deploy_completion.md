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
| D2 | activation | the ONE new route named package and the ONE new env key COMMENTARY_ALLOWED_FIRMS on opal-ticket-api (a Lambda -- a describe-task-definition family sweep DOES NOT APPLY, stated per step 0; the only puller of this artifact key is opal-ticket-api itself) | plan 1 to add 1 to change 0 to destroy and nothing else; env gains exactly COMMENTARY_ALLOWED_FIRMS byte-exact | route aws_apigatewayv2_route.tickets["package"] Creation complete id=qx3kow0, route_key POST /api/scoped/tickets/{ticketId}/package, target integrations/vgix3jf, AuthorizationType CUSTOM, AuthorizerId naqxlm (both pre-existing); env gained EXACTLY COMMENTARY_ALLOWED_FIRMS="49financial,cottonwood,inflection" byte-exact, 7 keys -> 8, no other key added removed or changed; plan was 1 to add 1 to change 0 to destroy and nothing else | CLOSED 20261009T010645Z |
| V1 | verify | the six after-reads (a)-(f) | CodeSha256 == the step-3 zip content-sha256; 8 env keys; deployed lambda_function.py sha256 == 01534e2d452acd02257cb6465cf2e2cf10dced3bea157e7afc9c66bc46ec4f64; the package route exists; an unauthenticated POST /api/scoped/tickets through CloudFront refused; opal-tickets ItemCount unchanged at 12; a 0-diff plan | (a) CodeSha256 RFRuryx.. == step-3 zip content-sha256 PASS. (b) 8 env keys, COMMENTARY_ALLOWED_FIRMS byte-exact PASS. (c) the DEPLOYED zip (downloaded via lambda get-function Code.Location) lambda_function.py sha256 = 01534e2d452acd02257cb6465cf2e2cf10dced3bea157e7afc9c66bc46ec4f64 = the order value = git show 3b04c040fc:infra/aws/lambda/ticket_center/lambda_function.py -- three-way; the package route exists, 1 exact match of a PRINTED 117-route denominator, auto-paginated PASS. (d) unauthenticated POST https://opalinvest.dev/api/scoped/tickets -> HTTP 401 {"error":"Missing or invalid Authorization header"}; the NEW package route unauthenticated also 401, so it landed behind the same auth boundary PASS. (e) opal-tickets ItemCount 12 before and 12 after PASS. (f) 0-diff plan PASS | CLOSED 20261009T010645Z |
| M1 | activation | mint svc-commentary and store the new secret opal/ticketing/svc-commentary | positive create; the CTO two negative arms plus LIST refused, each with route, status and row count; the claim read-back with the token NEVER printed; the test ticket id recorded |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply from the COMMITTED planfile (plan text c46b7d6b9a); Apply complete 1 added 1 changed 0 destroyed; live CodeSha256 RE-READ = RFRuryxKnuGVum/K3YP7MGnR5B2S4rFZfc4MX9k+gMQ= = the step-3 zip content-sha256; s3_object_version -> zgYaW.Ue4hoNgwQ4q5ODivIfJgLDcxGE; 0-diff re-plan of the whole ticket-center root | CLOSED 20261009T010644Z |

## Log

- 20261009T005624Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261009T010644Z LEG opal-ticket-api closed: safe-apply from the COMMITTED planfile (plan text c46b7d6b9a); Apply complete 1 added 1 changed 0 destroyed; live CodeSh
- 20261009T010645Z LEG D2 closed: route aws_apigatewayv2_route.tickets["package"] Creation complete id=qx3kow0, route_key POST /api/scoped/tickets/{ticket
- 20261009T010645Z LEG V1 closed: (a) CodeSha256 RFRuryx.. == step-3 zip content-sha256 PASS. (b) 8 env keys, COMMENTARY_ALLOWED_FIRMS byte-exact PASS. (c
