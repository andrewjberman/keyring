# Deploy Completion Record
**Date opened:** 2026-10-08T20:34:02.663045+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T204751Z
**Deploy:** irpt-ycharts-generate release 2 (E6): X-1 on-behalf upload with E5 guard; pin 1b94d50b8c built Un0wVZqj; rollback ZspX0qD2 / S3 objver QBeNB.XXjTccRAbSADmCh_Wv7R0brx6q; pair @8c11ac4ff1 + CTO half @2df0aa0c99
**Authored by:** 0.9.0_WK_IRPT_BCKEND~158
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks: pin ancestor, census=4 members, live CodeSha256 == ZspX0qD2, grant read-back, rollback objver | ancestor rc0 + changed_members=4 + live hash + grant statement + rollback objver | pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_access.py, served.py, uploads.py); live CodeSha256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= LastModified 2026-10-08T17:44:54Z; grant Sid ReadPartnerProfileRowForOnBehalfAdvisor GetItem on exactly opal-partner-49financial/-inflection/-cottonwood (after-read 0); ROLLBACK SOURCE S3 current versionId QBeNB.XXjTccRAbSADmCh_Wv7R0brx6q content-sha256 ZspX0qD2..; shared ycharts tf dir diff HEAD empty | CLOSED 20261008T203418Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == Un0wVZqj.. + new versionId | build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: import-closure OK (63 .py), SHA256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= (== signed), s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip write VERIFIED size=591141, new versionId CRj5yeTuBVUDiflaLEpoSX5wIfDKBd4e, content-sha256 metadata Un0wVZqj.. (head-object). Running code unchanged by this leg. | CLOSED 20261008T203530Z |
| L3 | activation | safe-apply of ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this 0 add 1 change 0 destroy | apply output + live CodeSha256 == Un0wVZqj.. | dell2 apply from shared initialized ycharts root: saved plan (Y67-1_plan.txt, committed 0b21388d51) 0 add / 1 change / 0 destroy (s3_object_version QBeNB.XXjTccRAbSADmCh_Wv7R0brx6q -> CRj5yeTuBVUDiflaLEpoSX5wIfDKBd4e, source_code_hash ZspX0qD2.. -> Un0wVZqj..); .tools/safe-apply.sh: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-tagauthz gate PASSED, no override. Live after: CodeSha256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= LastModified 2026-10-08T20:37:56Z Active/Successful; targeted re-plan: No changes (rc0); census invoke modules 62 failed={}. | CLOSED 20261008T203907Z |
| L4 | verify | after-reads 1-7, test row deleted NOT FOUND, admit keys handed to laptop | after-reads file + NOT FOUND read + admit_keys file | BRANCH B (stopped, rolled back): reads 0-3, 5, 6 passed on release 2; read 4 FAIL (guard admitted, stored write AccessDenied s3:PutObject on opal-data-irpt state/prospect_inputs/, row IRPT_BCKEND-D2-W158-S1 BLOCKING); read 7 FAIL (refusal code NOT_AUTHORIZED vs release-1 UNEXPECTED, row -S2). Rolled back 20:44:41Z via s3 copy-object of QBeNB.XXjTccRAbSADmCh_Wv7R0brx6q (new versionId LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v, content ZspX0qD2..) + targeted safe-apply 0/1/0; live CodeSha256 ZspX0qD2.., re-plan No changes, census failed={}. Test filer row deleted, consistent get-item no Item. Admit keys (4, derived; RETENTION# row may exist) handed to the laptop in Y67-1_admit_keys.json. After-reads file Y67-1_release2_after_reads.json. | CLOSED 20261008T204751Z |

## Log

- 20261008T203402Z OPENED by 0.9.0_WK_IRPT_BCKEND~158 with 4 leg(s)
- 20261008T203418Z LEG L1 closed: pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_acces
- 20261008T203530Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: import-closure OK (63 .py), SHA256 Un0wVZqjqpwKhpYyFeB
- 20261008T203907Z LEG L3 closed: dell2 apply from shared initialized ycharts root: saved plan (Y67-1_plan.txt, committed 0b21388d51) 0 add / 1 change / 0
- 20261008T204751Z LEG L4 closed: BRANCH B (stopped, rolled back): reads 0-3, 5, 6 passed on release 2; read 4 FAIL (guard admitted, stored write AccessDe
- 20261008T204751Z CLOSED -- all 4 legs proven
