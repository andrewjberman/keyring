# Deploy Completion Record
**Date opened:** 2026-09-23T21:54:17.181755+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260923T221609Z
**Deploy:** IRPT native Holdings selected-account reader package and least-privilege cutover
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | activation | Canonical package upload | S3 artifact digest and version; pinned maintained source31f9422dea | Canonical build-and-upload 1 of1 success;33members pinned with M5c277 repaired manifests. S3Version e7XAGneq1_KKe2tnBVK45FsEFNItS2NF SHA bcb3fb71937ad4958e3a68821a60a39ce338df6f7a8bca83b7584bd5913cc94b; source mapc17e1d819a. Backend .runtime/holdings-reader-cutover/upload-receipt.json | CLOSED 20260923T220131Z |
| A1 | activation | Saved plan function environment and reader role | Reviewed exact plan safe-apply receipt | Saved ca2a9077 applied 1add3change0destroy; CodeSha vLP7cZN61JWOOmiCGmCjnOM43296i8qDt1hL1ZE8yUs=; exact S3 e7XAGneq1_KKe2tnBVK45FsEFNItS2NF retained; HOLDINGS_READER_APPLY_20260923.json | CLOSED 20260923T221609Z |
| V1 | verify | Readback code configuration IAM and parity | Exact package hash role grants environment and zero-diff; M API/browser handoff | Actual Lambda Active/Successful exact reviewed CodeSha and env/IAM; refreshed postplan no changes; corrected recorder2d6b5881e5 exact one function; reconcile1already-in-parity0HELD; HOLDINGS_READER_APPLY_20260923.json | CLOSED 20260923T221609Z |

## Log

- 20260923T215417Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260923T220131Z LEG P1 closed: Canonical build-and-upload 1 of1 success;33members pinned with M5c277 repaired manifests. S3Version e7XAGneq1_KKe2tnBVK4
- 20260923T221609Z LEG A1 closed: Saved ca2a9077 applied 1add3change0destroy; CodeSha vLP7cZN61JWOOmiCGmCjnOM43296i8qDt1hL1ZE8yUs=; exact S3 e7XAGneq1_KKe
- 20260923T221609Z LEG V1 closed: Actual Lambda Active/Successful exact reviewed CodeSha and env/IAM; refreshed postplan no changes; corrected recorder2d6
- 20260923T221609Z CLOSED -- all 3 legs proven
