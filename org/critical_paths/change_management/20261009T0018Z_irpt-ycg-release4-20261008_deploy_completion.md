# Deploy Completion Record
**Date opened:** 2026-10-09T00:18:37.900929+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND APPLY-Y70: irpt-ycharts-generate release 4 on dell2 -- E11 (custody_submission.py) then the X-1 actor read-back
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks at pin e94a64b0f6 | pin an ancestor of origin/box/dell2 (rc 0); census changed_members=1 custody_submission.py; live CodeSha256 Un0wVZqj..; rollback S3 version recorded | git fetch origin then git merge-base --is-ancestor e94a64b0f6 origin/box/dell2 -> rc 0 (the CTO half's condition: no apply until the pin reads on origin); release-census irpt-ycharts-generate --pin HEAD (a79efe066f) -> changed custody_submission.py built=420ccd097831 live=e347d1d198d0, changed_members=1; live CodeSha256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= == the declared live and rollback target; rollback S3 object version recorded NqbpRnnx5METt43XaI_4nmk5fZDRTQpk | CLOSED 20261009T001904Z |
| L2 | s3-prefix | the built artifact on the lambda-artifacts prefix | build-and-upload SHA256 equals emzWWzrR0TUf7sHDbEeDeedc1EnTeaXAMl5kSHYLU7E= with write VERIFIED |  | OPEN |
| L3 | activation | irpt-ycharts-generate code (targeted apply of the ycharts root) | plan 0/1/0 on s3_object_version + source_code_hash only; live CodeSha256 re-read == built; re-plan 0 |  | OPEN |
| L4 | verify | E11 offline suites + the X-1 actor read-back | pytest 3 passed on test_custody_submission_revision.py and 66 passed 2 skipped across the three custody suites; import census failed:{}; X-1 graded on all THREE read-back booleans taken BEFORE any delete |  | OPEN |

## Log

- 20261009T001837Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261009T001904Z LEG L1 closed: git fetch origin then git merge-base --is-ancestor e94a64b0f6 origin/box/dell2 -> rc 0 (the CTO half's condition: no app
