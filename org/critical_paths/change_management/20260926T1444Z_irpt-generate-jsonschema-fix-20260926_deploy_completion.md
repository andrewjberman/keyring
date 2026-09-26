# Deploy Completion Record
**Date opened:** 2026-09-26T14:44:01.549770+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate: irpt-common layer (jsonschema/referencing/rpds) + whole-row re-pin at 19d8f3038c incl. the IAM-only import census (CTO 101229; K5 ModuleNotFoundError jsonschema)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | checker + served function | (1) package_import_check FAILS on IJD6bd1I naming jsonschema; (2) passes on the new zip + irpt-common; (3) import census on the deployed function: 0 failed modules; CodeSha256 == artifact; invoke {} CONTRACT_VERSION before and after; replan No changes |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260926T144401Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
