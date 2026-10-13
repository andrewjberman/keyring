# Deploy Completion Record
**Date opened:** 2026-10-13T12:28:50.759393+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-165: irpt-49f-reporting-gold-lambda thresholds-file swap (24-key blob -> six-key file @aaeb1866ff), ONE member over live i2r7CbVr; packet sha256 2ed4e840ef56; pair COO @7c9ad9d0f0 + CTO @c5e183273f; packet and both halves read whole before step 0; rollback to S3 version 8ELUDq_d2w.. (re-read at apply)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE: live CodeSha256 i2r7CbVr7ew/U0Ziwoi+Q3JnWLUZ0dBYjAv6XMrs8z8= and MemorySize 3008; every live worktree's .open_deploys census (no entry naming the function); rollback anchor version and its content-sha256 | the three reads printed |  | OPEN |
| L2 | verify | packet sha256 and the FIVE pins re-hashed from git show <pin>:<path> | five pins_verified entries all equal |  | OPEN |
| L3 | s3-prefix | BUILD_ONLY from pins; member diff against the live zip is exactly the one thresholds path; then upload, new VersionId, read-back | built CodeSha256, upload_member_diff, VersionId |  | OPEN |
| L4 | verify | targeted plan -target=module.irpt_reporting_gold.aws_lambda_function.this reads 0 to add 1 to change 0 to destroy | plan line |  | OPEN |
| L5 | activation | ONE .tools/safe-apply.sh on the saved plan; live CodeSha256 equals built; stamp with record-deploy-scope.py; post-apply plan No changes | apply line, readback, replan line, stamp commit |  | OPEN |
| L6 | verify | ONE dry-run invoke {backfill 2026-10-08, accounts population, dry_run true}: Duration under 765000 ms and Max Memory under 2556.8 MB, 0 objects written | REPORT line and written-object count |  | OPEN |
| L7 | verify | FIRST SCHEDULED FIRE after this release read by 2.0.0_SA_COO~D2: six-key thresholds object, claims measured measured held held inferred, threshold_claims_source stated (stays OPEN for the issuer) | the issuer's read |  | OPEN |

## Log

- 20261013T122850Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
