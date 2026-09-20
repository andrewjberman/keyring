# Deploy Completion Record
**Date opened:** 2026-09-20T17:59:38.559477+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtg-4 -- apply irpt-holdings pointer-follow fix (holdings root only). Both never-widen halves at HEAD, packet-keyed, blob b515836bb4db340dd1a4a6fb630ab70627432f3a. source_code_hash uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA= -> rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=. Rollback: re-publish prior CodeSha256 via Terraform pinned to build-store VersionId=U4sKRs.HJ0Jc4Ik323Y0b.qY7LsWU2Pg, never update-function-code.
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260920T175938Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 1 leg(s)
