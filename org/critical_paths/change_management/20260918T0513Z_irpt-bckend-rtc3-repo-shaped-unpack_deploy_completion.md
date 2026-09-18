# Deploy Completion Record
**Date opened:** 2026-09-18T05:13:33.518473+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtc-3: repo-shaped unpack recipe deployed and the directory root re-applied
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L3 | verify | served CodeSha256 == built zip sha256, host import check re-run for inf/cot | CodeSha256 match + SSM import-check stdout |  | OPEN |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260918T051333Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
