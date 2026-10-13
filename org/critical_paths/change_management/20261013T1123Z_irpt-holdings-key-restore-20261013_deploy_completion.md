# Deploy Completion Record
**Date opened:** 2026-10-13T11:23:30.263849+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T112706Z
**Deploy:** IRPT_ANLREQ TO-RESTORE-R20a: S3 key investor-reporting/irpt-holdings.zip gets one new version copied from live-package version dWoiYeH9; no Lambda update, no Terraform apply, no delete
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | live CodeSha256 SWRfUfHd.. ; key latest QCyspt0v..; source version dWoiYeH9 sha256 equals live CodeSha256; open-entry denominator over every live worktree | the reads and denominator printed | live CodeSha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=; key latest QCyspt0v.. (no newer); source version dWoiYeH9 sha256 equals it (299273 bytes); denominator 40 worktrees 99 entries, 2 exact-name entries both CLOSED on trunk, stale only in old worktree HEADs. Record R1_VERIFY_R20.txt | CLOSED 20261013T112400Z |
| R2 | s3-prefix | copy-object version dWoiYeH9 onto investor-reporting/irpt-holdings.zip, same bucket | new VersionId | copy-object of dWoiYeH9MSXq9yOuQkApr2h_XxwrvVi8 onto investor-reporting/irpt-holdings.zip at 2026-10-13T11:24:26Z: new VersionId hfQkgY1LcwrlvQCRQrJJlUJ2TLeah6op, CopySourceVersionId dWoiYeH9.., SSE AES256; no version deleted | CLOSED 20261013T112456Z |
| R3 | verify | new latest sha256 equals SWRfUfHd.. at 299273 bytes; get-function CodeSha256 unchanged | read-back equality | new latest hfQkgY1LcwrlvQCRQrJJlUJ2TLeah6op sha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0= 299273 bytes; get-function CodeSha256 unchanged SWRfUfHd.. (LastModified 2026-10-12T14:08:33Z); scoped plan: 1 to change, s3_object_version + last_modified only, source_code_hash not in diff. Record R3_READBACK_R20.txt | CLOSED 20261013T112657Z |

## Log

- 20261013T112330Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261013T112400Z LEG R1 closed: live CodeSha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=; key latest QCyspt0v.. (no newer); source version dWoiYeH9 
- 20261013T112456Z LEG R2 closed: copy-object of dWoiYeH9MSXq9yOuQkApr2h_XxwrvVi8 onto investor-reporting/irpt-holdings.zip at 2026-10-13T11:24:26Z: new V
- 20261013T112657Z LEG R3 closed: new latest hfQkgY1LcwrlvQCRQrJJlUJ2TLeah6op sha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0= 299273 bytes; get-functi
- 20261013T112706Z CLOSED -- all 3 legs proven
