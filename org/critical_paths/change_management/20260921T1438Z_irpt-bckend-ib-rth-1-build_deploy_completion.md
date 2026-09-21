# Deploy Completion Record
**Date opened:** 2026-09-21T14:38:35.108904+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rth-1 arm (c): K-CODE build -- all 7 serving functions rebuilt by build-and-upload.sh from HEAD 031d98c51d (source-map loaders.py pin now 385aff4646, the signed AccessDenied-as-absent fix; packet blob 19389dc50b, COO half @6298e74db4, CTO half @5fce993215). Build store only, never a function. Rollback sources = the current latest versions, each == live CodeSha256 == packet s4 table: directory-search GcjdIsAVfsJXvzGwuySEofStO3gVoEG8, status 2ER4lGvdlY7ftm5mPgEYt6pnXbozOeIG, holdings UUJ.iaufP39ypd8gq2NeSYyQewqgNizF, narrative jM9scOJ005ovgidfDS3DBRHRmjvLzUwn, export-render bEdwSqXfY99WaJSKeLwPkLuBPySCmI39, performance-adapter M0E32HJhwg54I6jcU4g2e58Ktthey_51, ycharts-generate D6hl_ey9azxF8RJRQ01YkDlO.axHKuHw
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L4 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L5 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L6 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |
| L7 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | new VersionId latest + content-sha256 == built + re-download sha256(b64) == built + zip members vs prior live: EXACTLY loaders.py differs and == 0c086052e6e6 (fix blob 3ea6b1cc4a) + prior version kept + function CodeSha256 unchanged (not applied) |  | OPEN |

## Log

- 20260921T143835Z OPENED by 0.7.0_AE_CloudOps~V with 7 leg(s)
