# Deploy Completion Record
**Date opened:** 2026-10-15T17:55:33.789019+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T180418Z
**Deploy:** FWD-5 positive arm: ONE signed change deploys ONE script data/black_diamond/scripts/gold/diag_sleeve_fix.py to s3://opal-data-bd/code/gold/diag_sleeve_fix.py; pin commit 461e3f64ee blob 8d6f273a9e sha256 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7; prior VersionId 3.yZFEuxxfxUOEMd.NRY7bZucaDccGX. (TO NFRA_CTLPLN.TO-CT-ak-3)
**Authored by:** 0.7.0_AE_CloudOps~CT2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit 461e3f64ee blob 8d6f273a9e data/black_diamond/scripts/gold/diag_sleeve_fix.py sha256 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7 | git rev-parse 461e3f64ee:data/black_diamond/scripts/gold/diag_sleeve_fix.py equals 8d6f273a9e and sha256 of the blob equals the pin | git rev-parse 461e3f64ee:data/black_diamond/scripts/gold/diag_sleeve_fix.py = 8d6f273a9e8265fde14717ba9d1fe52fa202efa8; git cat-file blob 461e3f64ee:data/black_diamond/scripts/gold/diag_sleeve_fix.py sha256 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7 equals the pin 971327859b33b43067db744f1a785c08a51b6b75581a1dc8d743ac0a1d83b9b7; 461e3f64ee is an ancestor of HEAD and of origin/box/laptop | CLOSED 20261015T180418Z |
| L2 | s3-prefix | s3://opal-data-bd/code/gold/diag_sleeve_fix.py | s3api head-object ETag equals md5 c204fd9be3bbfc43346a14b4c71051af AND a new VersionId (prior 3.yZFEuxxfxUOEMd.NRY7bZucaDccGX.) | s3api head-object s3://opal-data-bd/code/gold/diag_sleeve_fix.py ETag c204fd9be3bbfc43346a14b4c71051af equals repo md5 c204fd9be3bbfc43346a14b4c71051af, 4251 bytes; new VersionId ceImQVXASssU3IUCRXRjMkoA1XnifTf7 LastModified 2026-10-15T18:02:18Z; prior VersionId 3.yZFEuxxfxUOEMd.NRY7bZucaDccGX. (ETag 56cb170f95c0b112a36a0ee3973d5473) kept as rollback; deployed by the scheduled box-sync push (actor 0.0.0_AB_MSTR) through the hook's pinned-entry step: audit row 2026-10-15T18:01:57Z PINNED-DEPLOY slug=ctlpln-r21-fwd5-one-script-20261015 | CLOSED 20261015T180418Z |
| L3 | verify | audit log plus list-object-versions plus test_round21_fwd5_positive_read.py | 2 versions; no PINNED-DEPLOY row for any other path; other_changed=0 under code/gold/ | test_round21_fwd5_positive_read.py: FWD5-POSITIVE versions=2 etag_equals_repo_md5=True other_changed=0 audit_actor=0.0.0_AB_MSTR ok=True (0 of 190 other keys under code/gold/ modified after 2026-10-15T17:55:33Z); exactly one PINNED-DEPLOY row since the open, for this path; the CloudOps push was REFUSED by the LD-0367 gate (row NFRA_CTLPLN-S9132), so the actor is MSTR not the CloudOps seat | CLOSED 20261015T180418Z |

## Log

- 20261015T175533Z OPENED by 0.7.0_AE_CloudOps~CT2 with 3 leg(s)
- 20261015T180418Z LEG L1 closed: git rev-parse 461e3f64ee:data/black_diamond/scripts/gold/diag_sleeve_fix.py = 8d6f273a9e8265fde14717ba9d1fe52fa202efa8; 
- 20261015T180418Z LEG L2 closed: s3api head-object s3://opal-data-bd/code/gold/diag_sleeve_fix.py ETag c204fd9be3bbfc43346a14b4c71051af equals repo md5 c
- 20261015T180418Z LEG L3 closed: test_round21_fwd5_positive_read.py: FWD5-POSITIVE versions=2 etag_equals_repo_md5=True other_changed=0 audit_actor=0.0.0
- 20261015T180418Z CLOSED -- all 3 legs proven
