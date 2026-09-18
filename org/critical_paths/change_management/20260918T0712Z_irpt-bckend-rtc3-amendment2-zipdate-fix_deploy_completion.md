# Deploy Completion Record
**Date opened:** 2026-09-18T07:12:25.643174+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtc-3 AMENDMENT 2: correct the zip's fixed timestamp to the canonical 2020-01-01 (battery b.2 caught the mismatch)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | content-sha256 metadata match + head-object size |  | OPEN |
| L2 | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + served CodeSha256 matches battery's independent re-derivation |  | OPEN |

## Log

- 20260918T071225Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
