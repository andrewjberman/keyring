# Deploy Completion Record
**Date opened:** 2026-09-05T08:11:22.166386+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260905T083055Z
**Deploy:** EG-s-9: JOIN both recipients (aj@ + andrew@) on etfs-reports-orchestrator (targeted: aws_lambda_function.orchestrator only)
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| code | activation | etfs-reports-orchestrator | get-function-configuration Environment.Variables.EMAIL_RECIPIENT reads aj@opalinvest.com,andrew@opalinvest.com and CodeSha256 matches the built zip's base64 sha256 (applied BY TARGET: -target=aws_lambda_function.orchestrator) | get-function-configuration Environment.Variables.EMAIL_RECIPIENT=aj@opalinvest.com,andrew@opalinvest.com; CodeSha256=AVvA9lPQAj3tns5JSJ7Awg+crucGgIAfr5dHtScATXw= matches the built zip's base64 sha256 exactly (orchestrator_served_vs_built.py VERDICT: MATCH); applied BY TARGET -target=aws_lambda_function.orchestrator, targeted 0-diff plan -detailed-exitcode rc=0 | CLOSED 20260905T083017Z |

## Log

- 20260905T081122Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~1 with 1 leg(s)
- 20260905T083017Z LEG code closed: get-function-configuration Environment.Variables.EMAIL_RECIPIENT=aj@opalinvest.com,andrew@opalinvest.com; CodeSha256=AVv
- 20260905T083055Z CLOSED -- all 1 legs proven
