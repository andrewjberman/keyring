# Deploy Completion Record
**Date opened:** 2026-09-26T13:18:05.160890+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate carries interactive_access / template_reader / security_resolution (publish 45d905110c; ~Y 101116/101125) -- build, apply, verify
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | new zip + served function | generate_package_closure.py exit 0 on the new zip (was 1 on LdjdnnLh); CodeSha256 == built artifact; invoke {} named CONTRACT_VERSION refusal before and after, cold start clean; replan No changes |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260926T131805Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
