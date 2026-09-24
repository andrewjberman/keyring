# Deploy Completion Record
**Date opened:** 2026-09-24T10:20:23.171889+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T102741Z
**Deploy:** irpt-ycharts-generate: installed handler generate_installed.lambda_handler + sqs:SendMessage on irpt-generation (CTO 100497 (a); no ESM, IRPT_LIVE_YCHARTS_CALL unset)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 0 added 2 changed 0 destroyed (safe-apply, generate-installed.tfplan, 10:24:09Z); replan rc=0 No changes; get-function-configuration CodeSha256 uHfng41l/agHCG5OHldwqi2r+NUZKfu7DqmWvbqNhTc= == uploaded sha (builder metadata, S3 version .YnkMmwAKJumsmFjRgQm_9W0TQxdyhZB), handler generate_installed.lambda_handler, 0 event source mappings, IRPT_LIVE_YCHARTS_CALL absent; verify-on-served: invoke {} -> 200, no FunctionError, named refusal CONTRACT_VERSION (request 4d0c23f9-ac15-4e39-a21d-48f7e6e660d8); recorder 281f54f157; receipt GENERATE_INSTALLED_APPLY_20260924.json | CLOSED 20260924T102741Z |

## Log

- 20260924T102023Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260924T102741Z LEG irpt-ycharts-generate closed: TF apply 0 added 2 changed 0 destroyed (safe-apply, generate-installed.tfplan, 10:24:09Z); replan rc=0 No changes; get-f
- 20260924T102741Z CLOSED -- all 1 legs proven
