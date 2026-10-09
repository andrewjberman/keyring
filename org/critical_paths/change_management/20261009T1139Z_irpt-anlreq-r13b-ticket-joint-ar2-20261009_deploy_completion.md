# Deploy Completion Record
**Date opened:** 2026-10-09T11:39:00.469721+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T114610Z
**Deploy:** IRPT_ANLREQ R13b joint opal-ticket-api CODE-ONLY release: pin ba6fcb1c14, lambda_function.py sha256 670686262068808fcf1d3e0c05ce8e92e32441f9382efeb9361c789ab19457a8. Substitute applier 0.7.0_AE_CloudOps~AR2 under CTO standing ruling @5ff94852a6 item 2 and CTO half @11a11e67e2 (half names ~DELL2; R13 withdrawn from it @4f6b1b8d57). One family on the artifact key = opal-ticket-api itself (a Lambda: describe-task-definition family sweep DOES NOT APPLY). No env, IAM, route or permission change. Rollback: re-apply V12 build pin 86454002bf, file 04f5727b.
**Authored by:** 0.7.0_AE_CloudOps~AR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | the step-5 after-reads (a)-(e) | (a) deployed lambda_function.py sha256 == 67068626...; (b) the 8 env key names and values unchanged; (c) an unauthenticated POST refused; (d) opal-tickets ItemCount unchanged at 13; (e) replan 0-diff | (a) PASS three-way: git show ba6fcb1c14:infra/aws/lambda/ticket_center/lambda_function.py = 670686262068808fcf1d3e0c05ce8e92e32441f9382efeb9361c789ab19457a8 = the built zip entry = the DEPLOYED zip entry (downloaded via lambda get-function Code.Location, 1 entry). (b) PASS 8 env key names identical before and after (CLIENT_LINK_MAP COMMENTARY_ALLOWED_FIRMS CUTOFF_ET ROUTING_MATRIX TABLE_NAME TICKET_DEEP_LINK_BASE TICKET_DL_MAP USERS_TABLE), COMMENTARY_ALLOWED_FIRMS byte-exact 49financial,cottonwood,inflection; the plan hid env in an unchanged block and the apply ran that exact saved planfile. (c) PASS unauthenticated POST https://opalinvest.dev/api/scoped/tickets -> HTTP 401 Missing or invalid Authorization header, and the new package route POST .../TEST-NONE/package -> HTTP 401 likewise; positive control GET https://opalinvest.dev/ -> HTTP 200, so the 401 is a refusal and not an unreachable host. (d) PASS opal-tickets ItemCount 13 before and 13 after. (e) PASS replan of the whole ticket-center root with -detailed-exitcode rc=0, No changes. Your infrastructure matches the configuration. | CLOSED 20261009T114600Z |
| opal-ticket-api | tf-lambda | module.opal_ticket_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply from the SAVED planfile tfplan.r13b in detached worktree /c/dev/wk-ar2-r13 at pin ba6fcb1c14. Plan was branch A exactly: 0 to add, 1 to change, 0 to destroy, the one change module.opal_ticket_api.aws_lambda_function.this updated in-place, three attributes only -- source_code_hash IMJsVN6U8F730Z9Typ1AuG2bRUunlFYJ5it+jkirlWM= -> HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA=, s3_object_version vTaikElcFfkLXSqEOKZhg_iH1_FViE37 -> TNDfJSNhCarmtqRmFU.jsPUaiO7BLSsK, last_modified known-after-apply; 28 unchanged attributes and 4 unchanged blocks hidden, so no env, IAM, route or permission change. Apply complete: 0 added, 1 changed, 0 destroyed. Live CodeSha256 RE-READ = HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA= = the uploaded zip content-sha256. LastModified 2026-10-09T11:43:28Z. | CLOSED 20261009T114543Z |

## Log

- 20261009T113900Z OPENED by 0.7.0_AE_CloudOps~AR2 with 2 leg(s)
- 20261009T114543Z LEG opal-ticket-api closed: safe-apply from the SAVED planfile tfplan.r13b in detached worktree /c/dev/wk-ar2-r13 at pin ba6fcb1c14. Plan was branch
- 20261009T114600Z LEG V1 closed: (a) PASS three-way: git show ba6fcb1c14:infra/aws/lambda/ticket_center/lambda_function.py = 670686262068808fcf1d3e0c05ce
- 20261009T114610Z CLOSED -- all 2 legs proven
