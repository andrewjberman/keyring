# Deploy Completion Record
**Date opened:** 2026-10-15T15:26:00.800783+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-579: move irpt-ycharts-generate from CodeSha256 5TRFZf6G.. to the signed candidate 3+fMEJhQ8.. (the commentary_requested release) by its Terraform path; Branch B = S3 version sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C of investor-reporting/irpt-ycharts-generate.zip
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates and BEFORE reads: packet sha256, both halves, ledgers and markers, live CodeSha256, Branch B version, live zip commentary_requested count 0 in the three ENDPOINT members, accepted request item sha256 | the printed reads | packet sha256 2920ef90fa06.. equal; addendum COO blob f848de8d6a equal, CTO half SIGNED on it, ruling @7f7acb0e42 and msg 8364 amendment read; ledgers read 1936, 0 non-closed name the function; markers 27 worktrees 432 files, 0 naming it with an open trunk ledger, 2 stale CLOSED views named (wt-base-a4b7, rel-resident-r5); live CodeSha256 5TRFZf6G.. at 15:23Z; Branch B S3 version sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C (55 versions listed, one content match, bytes equal the live zip); live zip commentary_requested 0/0/0 in submission.py, acceptance.py, schema; accepted request item sha256 1e07ec8ee152.. (get-item, GetItem simulated allowed on the table ARN) | CLOSED 20261015T153219Z |
| L2 | s3-prefix | source-map rows of this function only, BUILD_ONLY digest equals 3+fMEJhQ8.. then upload, head-object, new VersionId, built==landed | digest, VersionId | 3 re-pinned rows of this function in the real map (7 changed lines incl artifact_sha256); BUILD_ONLY 3+fMEJhQ8enneLH30XiiV5VYEC4kk0+hZl0SFFsyM4k= equals the signed digest; four members differ from the live zip with the signed sha256; uploaded VersionId wJDd4Tr_Ya8CWi2CSPqgVqci4riH04lh size 635697 content-sha256 metadata = built (head-object) | CLOSED 20261015T153219Z |
| L3 | verify | saved plan reads 1 to change, 0 to add, 0 to destroy, only s3_object_version and source_code_hash of the one function | plan line | saved plan 15:31Z: Plan: 0 to add, 1 to change, 0 to destroy; module.irpt_ycharts_generate.aws_lambda_function.this s3_object_version sf9zrBd..->wJDd4Tr.. and source_code_hash 5TRFZf6G..->3+fMEJhQ8.. only | CLOSED 20261015T153219Z |
| L4 | verify | after-read: CodeSha256 equals built, re-plan 0, exactly the four members differ, import census failed empty, offline replay at the pin, item hash unchanged, composition test | the reads | re-plan No changes rc=0; deployed zip sha256 = 3+fMEJhQ8..; vs pre-apply zip exactly 4 members differ (acceptance.py abbdab493509, composition_admission.py 8d9b7aadc7c4, schema 1052343f111b, submission.py 18aba4f0792f) 106 of 106; ONE invoke (census) StatusCode 200 modules 68 failed {}; accepted request item sha256 1e07ec8ee152.. equal before and after; composition test 6 passed 0 failed; offline replay of the released function 17 arms, 3 differ from the recorded verdicts (the pre-apply live package already carries release 29's acting_principal_id pairing) -- stated in the record | CLOSED 20261015T153840Z |
| L5 | verify | health proof at least 10 minutes after the apply: Invocations and Errors, log group Traceback TypeError Task timed out ERROR | window, count, errors |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | ONE safe-apply (HALT checkpoint and comp-tagauthz passed; inbox 8 of 8 READ) on the saved plan 15:32:31Z-15:34:14Z: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' rc=0; LastModified 2026-10-15T15:34:08Z; live CodeSha256 3+fMEJhQ8enneLH30XiiV5VYEC4kk0+hZl0SFFsyM4k= equals the built digest | CLOSED 20261015T153839Z |

## Log

- 20261015T152600Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261015T153219Z LEG L1 closed: packet sha256 2920ef90fa06.. equal; addendum COO blob f848de8d6a equal, CTO half SIGNED on it, ruling @7f7acb0e42 and ms
- 20261015T153219Z LEG L2 closed: 3 re-pinned rows of this function in the real map (7 changed lines incl artifact_sha256); BUILD_ONLY 3+fMEJhQ8enneLH30Xi
- 20261015T153219Z LEG L3 closed: saved plan 15:31Z: Plan: 0 to add, 1 to change, 0 to destroy; module.irpt_ycharts_generate.aws_lambda_function.this s3_o
- 20261015T153839Z LEG irpt-ycharts-generate closed: ONE safe-apply (HALT checkpoint and comp-tagauthz passed; inbox 8 of 8 READ) on the saved plan 15:32:31Z-15:34:14Z: 'App
- 20261015T153840Z LEG L4 closed: re-plan No changes rc=0; deployed zip sha256 = 3+fMEJhQ8..; vs pre-apply zip exactly 4 members differ (acceptance.py abb
