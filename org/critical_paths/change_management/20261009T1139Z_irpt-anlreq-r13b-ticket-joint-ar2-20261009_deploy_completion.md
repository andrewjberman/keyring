# Deploy Completion Record
**Date opened:** 2026-10-09T11:39:00.469721+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ R13b joint opal-ticket-api CODE-ONLY release: pin ba6fcb1c14, lambda_function.py sha256 670686262068808fcf1d3e0c05ce8e92e32441f9382efeb9361c789ab19457a8. Substitute applier 0.7.0_AE_CloudOps~AR2 under CTO standing ruling @5ff94852a6 item 2 and CTO half @11a11e67e2 (half names ~DELL2; R13 withdrawn from it @4f6b1b8d57). One family on the artifact key = opal-ticket-api itself (a Lambda: describe-task-definition family sweep DOES NOT APPLY). No env, IAM, route or permission change. Rollback: re-apply V12 build pin 86454002bf, file 04f5727b.
**Authored by:** 0.7.0_AE_CloudOps~AR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | the step-5 after-reads (a)-(e) | (a) deployed lambda_function.py sha256 == 67068626...; (b) the 8 env key names and values unchanged; (c) an unauthenticated POST refused; (d) opal-tickets ItemCount unchanged at 13; (e) replan 0-diff |  | OPEN |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T113900Z OPENED by 0.7.0_AE_CloudOps~AR2 with 2 leg(s)
