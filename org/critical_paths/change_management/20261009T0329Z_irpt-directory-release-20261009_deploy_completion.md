# Deploy Completion Record
**Date opened:** 2026-10-09T03:29:15.013335+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-383: the ONE directory release at pin 7f31bbfa4e -- refresh function + runner bundle, then the per-firm seeding run and the driven after-read
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | tf-lambda | irpt-directory-refresh code at pin 7f31bbfa4e via safe-apply in infra/aws/terraform/investor-reporting/directory/ | live CodeSha256 equals the built 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= AND a re-plan shows 0 changes |  | OPEN |
| B1 | s3-prefix | the investor-reporting runner bundle via safe-deploy.sh on directory_runner.py | ETag equals md5 b0356a757b1ae92e3a4b46a847378315 AND bundle sha256 equals 2e3e6648312f5daad1da91f0c3aaeb4736a81b16cc9bb0dd4f43e5e93886b968, with the live bundle version recorded BEFORE and AFTER |  | OPEN |
| S1 | s3-prefix | inflection seeding, packet Branch A step 2, previous-key investor-reporting/directory/2026-09-25/directory.json | the landed dated key read back for the carried TERMINATED entry; sub-branch (same-date overwrite or new-date key) and the S3 versions written both recorded |  | OPEN |
| S2 | s3-prefix | cottonwood seeding, packet Branch A step 2, previous-key investor-reporting/directory/2026-10-05/directory.json | same read-back, sub-branch and S3 versions recorded |  | OPEN |
| V1 | verify | one driven refresh per firm, then each _refresh/<date>/manifest.json at the manifest own as_of | per firm reason_code, manifest_as_of, terminated_count and carried_in_served from the served directory.json; for 49financial also source_client_ids_present from its first landing with the new bundle |  | OPEN |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T032915Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)
