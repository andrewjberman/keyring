# Deploy Completion Record
**Date opened:** 2026-10-13T11:23:30.263849+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RESTORE-R20a: S3 key investor-reporting/irpt-holdings.zip gets one new version copied from live-package version dWoiYeH9; no Lambda update, no Terraform apply, no delete
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | live CodeSha256 SWRfUfHd.. ; key latest QCyspt0v..; source version dWoiYeH9 sha256 equals live CodeSha256; open-entry denominator over every live worktree | the reads and denominator printed |  | OPEN |
| R2 | s3-prefix | copy-object version dWoiYeH9 onto investor-reporting/irpt-holdings.zip, same bucket | new VersionId |  | OPEN |
| R3 | verify | new latest sha256 equals SWRfUfHd.. at 299273 bytes; get-function CodeSha256 unchanged | read-back equality |  | OPEN |

## Log

- 20261013T112330Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
