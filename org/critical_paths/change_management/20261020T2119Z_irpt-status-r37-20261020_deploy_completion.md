# Deploy Completion Record
**Date opened:** 2026-10-20T21:19:50.218569+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T214940Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R37 (two PDF routes): release r37 of the irpt-status Lambda, owned_report.py moves, pin 474f174e89
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | new latest version of investor-reporting/irpt-status.zip in opal-313476888478-lambda-artifacts, object sha256 078474759a81... | object read back equal | U digest build at the pin 474f174e89 BUILD_ONLY printed CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= (git status clean, MSYS_NO_PATHCONV unset, private TMPDIR); real upload 2026-10-20T21:30:20Z one new object version GQvcCsg_FTPeOh.4GRZNiCLF3mxgJKk4 (70 -> 71 versions); object read back sha256 078474759a81...f1321, 369411 bytes, 49 members | CLOSED 20261020T213426Z |
| C | activation | terraform scoped apply of module.irpt_status.aws_lambda_function.this at CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= | Apply complete 0 added 1 changed 0 destroyed | C scoped plan 0 to add 1 to change 0 to destroy at trunk HEAD 30f47b4167 (fmt -check whole root rc 0, init), attributes last_modified, s3_object_version, source_code_hash only; safe-apply 2026-10-20T21:33:16Z..21:33:55Z rc 0 (first attempt 21:32:43Z blocked by the halt gate on 9 already-READ routine messages, none STOP-class, broker 0 not-READ; nothing applied; re-run with HALT_ACK=1): Apply complete! Resources: 0 added, 1 changed, 0 destroyed | CLOSED 20261020T213426Z |
| V | verify | after-reads G1 to G6 | G1 to G6 lines | G1 live CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= (equals expected); G2 49 of 49 members compared with the R0 pre-window zip: exactly owned_report.py differs, 0 added, 0 removed; G3 credential-less envelope status 401 sha256 equal before and after; G4 READY report read of REQ-d47252fe... status 200 body sha256 equal (byte-identical, 60114 bytes); G5 MADE for the Overview route (NOT_FOUND before, a download link after; commentary route unchanged NOT_FOUND for that older request); G6 census changed_members 0 at the pin; viewer row removed after exp and read ABSENT (index and consistent); uploaded VersionId GQvcCsg_FTPeOh.4GRZNiCLF3mxgJKk4, rollback 5Uqt.3DqL8QHzaOKv0clIZ14XADNH7ZD | CLOSED 20261020T214940Z |

## Log

- 20261020T211950Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261020T213426Z LEG U closed: U digest build at the pin 474f174e89 BUILD_ONLY printed CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= (git sta
- 20261020T213426Z LEG C closed: C scoped plan 0 to add 1 to change 0 to destroy at trunk HEAD 30f47b4167 (fmt -check whole root rc 0, init), attributes 
- 20261020T214940Z LEG V closed: G1 live CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= (equals expected); G2 49 of 49 members compared with the
- 20261020T214940Z CLOSED -- all 3 legs proven
