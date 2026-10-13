# Deploy Completion Record
**Date opened:** 2026-10-13T11:23:30.263849+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T223546Z
**Deploy:** IRPT_ANLREQ TO-RESTORE-R20a: S3 key investor-reporting/irpt-holdings.zip gets one new version copied from live-package version dWoiYeH9; no Lambda update, no Terraform apply, no delete
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | live CodeSha256 SWRfUfHd.. ; key latest QCyspt0v..; source version dWoiYeH9 sha256 equals live CodeSha256; open-entry denominator over every live worktree | the reads and denominator printed | R1 proven by 0.7.0_AE_CloudOps~AQ2 in the completion record at 20261013T112400Z (live CodeSha256 SWRfUfHd.., key latest QCyspt0v.., source version dWoiYeH9 sha256 equals the live CodeSha256, 299273 bytes); closed SUPERSEDED by 2.0.0_SA_COO~Y2 at 2026-10-13T22:3xZ: the entry file here still read OPEN because the close was never committed to this tree | CLOSED 20261013T223545Z |
| R2 | s3-prefix | copy-object version dWoiYeH9 onto investor-reporting/irpt-holdings.zip, same bucket | new VersionId | R2 proven in the completion record: copy-object of dWoiYeH9 onto investor-reporting/irpt-holdings.zip gave VersionId hfQkgY1LcwrlvQCRQrJJlUJ2TLeah6op; re-read live by 2.0.0_SA_COO~Y2 now: that version exists, 299273 bytes, LastModified 2026-10-13T11:24:26Z, no version deleted (6 versions listed) | CLOSED 20261013T223545Z |
| R3 | verify | new latest sha256 equals SWRfUfHd.. at 299273 bytes; get-function CodeSha256 unchanged | read-back equality | R3 proven in the completion record at 20261013T112657Z (new latest sha256 SWRfUfHd.. 299273 bytes, function CodeSha256 unchanged); SUPERSEDED since: live now the function irpt-holdings CodeSha256 d1HwIxeAvr2V1RibOmjT8UQBOd7NdzFqi4LPEKxjZPw= 300128 bytes LastModified 2026-10-13T12:47:20Z and the key latest YMQJgP4tNs3SU1ZOPzfkxJZBLZrRzTc. 300128 bytes 12:45:08Z, a later release; the restore's artifact was correct when taken and nothing is stranded | CLOSED 20261013T223545Z |

## Log

- 20261013T112330Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261013T223545Z LEG R1 closed: R1 proven by 0.7.0_AE_CloudOps~AQ2 in the completion record at 20261013T112400Z (live CodeSha256 SWRfUfHd.., key latest 
- 20261013T223545Z LEG R2 closed: R2 proven in the completion record: copy-object of dWoiYeH9 onto investor-reporting/irpt-holdings.zip gave VersionId hfQ
- 20261013T223545Z LEG R3 closed: R3 proven in the completion record at 20261013T112657Z (new latest sha256 SWRfUfHd.. 299273 bytes, function CodeSha256 u
- 20261013T223546Z CLOSED -- all 3 legs proven

## Carried notes (hand-written lines kept across re-renders)

- 20261013T112400Z LEG R1 closed: live CodeSha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0=; key latest QCyspt0v.. (no newer); source version dWoiYeH9 
- 20261013T112456Z LEG R2 closed: copy-object of dWoiYeH9MSXq9yOuQkApr2h_XxwrvVi8 onto investor-reporting/irpt-holdings.zip at 2026-10-13T11:24:26Z: new V
- 20261013T112657Z LEG R3 closed: new latest hfQkgY1LcwrlvQCRQrJJlUJ2TLeah6op sha256 SWRfUfHdJarO2Rhbxw/KQK88DeDNorQujkaR1jUuZc0= 299273 bytes; get-functi
- 20261013T112706Z CLOSED -- all 3 legs proven
