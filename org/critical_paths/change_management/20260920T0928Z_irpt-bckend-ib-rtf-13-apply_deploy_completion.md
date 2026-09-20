# Deploy Completion Record
**Date opened:** 2026-09-20T09:28:27.643018+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtf-13 -- apply the directory-search contract member + IRPT_CONTRACTS_DIR env line on the directory root. Subtraction gate (CTO compared-object term @ac63a41207) PASS: 58 resource_changes entries compared across 7 roots, 0 paths subtracted (inert on this plan set); directory root's ONLY substantive entry is module.irpt_directory_search.aws_lambda_function.this actions [update] before=PUjH3OjD... after=76LeVyYN...; the other 6 roots (export/holdings/intake/narrative/ops/performance) each show 0 substantive resource_changes. Rollback: re-publish CodeSha256 PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c= via Terraform pinned to build-store VersionId elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk, never update-function-code, and revert the IRPT_CONTRACTS_DIR line.
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260920T092827Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 1 leg(s)
