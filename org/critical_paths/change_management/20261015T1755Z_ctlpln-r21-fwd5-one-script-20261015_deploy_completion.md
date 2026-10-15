# Deploy Completion Record
**Date opened:** 2026-10-15T17:55:33.789019+00:00
**Status:** OPEN
**Deploy:** FWD-5 positive arm: ONE signed change deploys ONE script data/black_diamond/scripts/gold/diag_sleeve_fix.py to s3://opal-data-bd/code/gold/diag_sleeve_fix.py; pin commit 461e3f64ee blob 8d6f273a9e sha256 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7; prior VersionId 3.yZFEuxxfxUOEMd.NRY7bZucaDccGX. (TO NFRA_CTLPLN.TO-CT-ak-3)
**Authored by:** 0.7.0_AE_CloudOps~CT2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit 461e3f64ee blob 8d6f273a9e data/black_diamond/scripts/gold/diag_sleeve_fix.py sha256 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7 | git rev-parse 461e3f64ee:data/black_diamond/scripts/gold/diag_sleeve_fix.py equals 8d6f273a9e and sha256 of the blob equals the pin |  | OPEN |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/diag_sleeve_fix.py | s3api head-object ETag equals md5 c204fd9be3bbfc43346a14b4c71051af AND a new VersionId (prior 3.yZFEuxxfxUOEMd.NRY7bZucaDccGX.) |  | OPEN |
| L3 | verify | audit log plus list-object-versions plus test_round21_fwd5_positive_read.py | 2 versions; no PINNED-DEPLOY row for any other path; other_changed=0 under code/gold/ |  | OPEN |

## Log

- 20261015T175533Z OPENED by 0.7.0_AE_CloudOps~CT2 with 3 leg(s)
