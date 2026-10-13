# Deploy Completion Record
**Date opened:** 2026-10-13T16:01:44.445985+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-SCRATCH-R21b: second live arm of the AR-y-229 fix (build-and-upload.sh at 25e92d4daa, blob eba6dc3da9): real run through a temp map, upload on investor-reporting/_ar222_scratch/ only; no function key, Lambda, Terraform or repository map moves
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | detached worktree at trunk head containing 25e92d4daa (same sparse cone, no .tools); script blob equals eba6dc3da9; BEFORE reads; temp map key read back; open-entry denominator | reads printed |  | OPEN |
| S2 | s3-prefix | real run of build-and-upload.sh investor-reporting irpt-status via BAU_SOURCE_MAP_OVERRIDE, no BUILD_ONLY, to the scratch key | exit code, SHA256 line, size, verify line |  | OPEN |
| S3 | verify | scratch object head-object size and content-sha256 equal the run; scratch prefix version count; real map row, irpt-status.zip latest and CodeSha256 unchanged | equalities printed |  | OPEN |

## Log

- 20261013T160144Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
