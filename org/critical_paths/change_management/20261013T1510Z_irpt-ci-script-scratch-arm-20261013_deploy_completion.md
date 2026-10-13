# Deploy Completion Record
**Date opened:** 2026-10-13T15:10:58.267458+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-SCRATCH-R21: live arm of the AR-y-222 fix (build-and-upload.sh at 9ffca59db9, blob 372c3240fb): real run through a temp map with the upload landing on investor-reporting/_ar222_scratch/ only; no function key, Lambda, Terraform or repository map moves
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | detached worktree at trunk head containing 9ffca59db9; script blob equals 372c3240fb; BEFORE reads of irpt-status key, repository map row and CodeSha256; temp map key read back; open-entry denominator | reads printed |  | OPEN |
| S2 | s3-prefix | real run of build-and-upload.sh investor-reporting irpt-status via BAU_SOURCE_MAP_OVERRIDE, no BUILD_ONLY, upload to the scratch key | exit code, SHA256 line, size, verify line |  | OPEN |
| S3 | verify | scratch object head-object size and content-sha256 equal the run; scratch prefix version count; real map row, irpt-status.zip latest and CodeSha256 unchanged | equalities printed |  | OPEN |

## Log

- 20261013T151058Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
