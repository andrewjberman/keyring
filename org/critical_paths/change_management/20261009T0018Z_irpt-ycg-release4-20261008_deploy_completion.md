# Deploy Completion Record
**Date opened:** 2026-10-09T00:18:37.900929+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T003255Z
**Deploy:** IRPT_BCKEND APPLY-Y70: irpt-ycharts-generate release 4 on dell2 -- E11 (custody_submission.py) then the X-1 actor read-back
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks at pin e94a64b0f6 | pin an ancestor of origin/box/dell2 (rc 0); census changed_members=1 custody_submission.py; live CodeSha256 Un0wVZqj..; rollback S3 version recorded | git fetch origin then git merge-base --is-ancestor e94a64b0f6 origin/box/dell2 -> rc 0 (the CTO half's condition: no apply until the pin reads on origin); release-census irpt-ycharts-generate --pin HEAD (a79efe066f) -> changed custody_submission.py built=420ccd097831 live=e347d1d198d0, changed_members=1; live CodeSha256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= == the declared live and rollback target; rollback S3 object version recorded NqbpRnnx5METt43XaI_4nmk5fZDRTQpk | CLOSED 20261009T001904Z |
| L2 | s3-prefix | the built artifact on the lambda-artifacts prefix | build-and-upload SHA256 equals emzWWzrR0TUf7sHDbEeDeedc1EnTeaXAMl5kSHYLU7E= with write VERIFIED | build-and-upload.sh investor-reporting irpt-ycharts-generate: SHA256 emzWWzrR0TUf7sHDbEeDeedc1EnTeaXAMl5kSHYLU7E= == the order's declared built sha; s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip write VERIFIED (size=591317, sha256 metadata match) | CLOSED 20261009T002012Z |
| L3 | activation | irpt-ycharts-generate code (targeted apply of the ycharts root) | plan 0/1/0 on s3_object_version + source_code_hash only; live CodeSha256 re-read == built; re-plan 0 | targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this from the COMMITTED planfile (plan text 43e2dfdb10); plan changed ONLY s3_object_version NqbpRnnx5METt43XaI_4nmk5fZDRTQpk -> YDb8Vrk.YuU6A3d7poxncrnoSCxit7K3 and source_code_hash (plus the computed last_modified); Apply complete 0 added 1 changed 0 destroyed; live CodeSha256 RE-READ = emzWWzrR0TUf7sHDbEeDeedc1EnTeaXAMl5kSHYLU7E= = built; re-plan of the same target 'No changes' | CLOSED 20261009T002550Z |
| L4 | verify | E11 offline suites + the X-1 actor read-back | pytest 3 passed on test_custody_submission_revision.py and 66 passed 2 skipped across the three custody suites; import census failed:{}; X-1 graded on all THREE read-back booleans taken BEFORE any delete | BRANCH B. Read 2 (the import census) FAILED on the release-4 bytes: direct invoke {irpt_import_census:true} -> modules 62, failed {custody_submission: ImportError cannot import name CUSTODY_POLICY_REVISION from composition}. custody_submission.py is the ONE changed member. POSITIVE CONTROL: the identical invoke on the rolled-back bytes reads modules 62, failed {} -- the instrument reads clean when the code is clean. The E11 offline suites DID pass (3 passed; 66 passed 2 skipped) and could not see this: CUSTODY_POLICY_REVISION is defined only in reports/composition.py while the zip packages the generate tree's composition.py, so pytest resolved a same-name shadow. Rolled back the same session to Un0wVZqj.. (live re-read, Active/Successful); reads 3-7 never reached, so no test filer, no upload, no records, no resolve_upload, no YCharts resolution; test filer key NOT FOUND on a consistent get-item. Row IRPT_BCKEND-D2-S15 | CLOSED 20261009T003255Z |

## Log

- 20261009T001837Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261009T001904Z LEG L1 closed: git fetch origin then git merge-base --is-ancestor e94a64b0f6 origin/box/dell2 -> rc 0 (the CTO half's condition: no app
- 20261009T002012Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-ycharts-generate: SHA256 emzWWzrR0TUf7sHDbEeDeedc1EnTeaXAMl5kSHYLU7E= == the
- 20261009T002550Z LEG L3 closed: targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this from the COMMITTED planfile (plan text 43e2
- 20261009T003255Z LEG L4 closed: BRANCH B. Read 2 (the import census) FAILED on the release-4 bytes: direct invoke {irpt_import_census:true} -> modules 6
- 20261009T003255Z CLOSED -- all 4 legs proven
