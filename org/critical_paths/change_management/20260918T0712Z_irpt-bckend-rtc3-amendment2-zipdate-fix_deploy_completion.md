# Deploy Completion Record
**Date opened:** 2026-09-18T07:12:25.643174+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T071610Z
**Deploy:** IRPT_BCKEND IB-rtc-3 AMENDMENT 2: correct the zip's fixed timestamp to the canonical 2020-01-01 (battery b.2 caught the mismatch)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | content-sha256 metadata match + head-object size | content-sha256=E7TMbaF9NBPm7rFIDkk7y22gNQiPRAGr9m9BqcpnkGM= verified via head-object (size 38745==38745); VersionId=xuF53Ar4NioCglz2tn5dkFmA6JLIUZo. | CLOSED 20260918T071609Z |
| L2 | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + served CodeSha256 matches battery's independent re-derivation | terraform apply: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 destroyed; served CodeSha256 E7TMbaF9NBPm7rFIDkk7y22gNQiPRAGr9m9BqcpnkGM= matches battery arm b.1/b.2 (independent re-derivation, 2020-01-01 canonical timestamp); post-apply re-plan No changes | CLOSED 20260918T071610Z |

## Log

- 20260918T071225Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
- 20260918T071609Z LEG L1 closed: content-sha256=E7TMbaF9NBPm7rFIDkk7y22gNQiPRAGr9m9BqcpnkGM= verified via head-object (size 38745==38745); VersionId=xuF5
- 20260918T071610Z LEG L2 closed: terraform apply: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 destroyed; served CodeSha256
- 20260918T071610Z CLOSED -- all 2 legs proven
