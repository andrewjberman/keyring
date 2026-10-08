# Deploy Completion Record
**Date opened:** 2026-10-08T21:22:24.415763+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T213418Z
**Deploy:** irpt-ycharts-generate release 3: the E6 build (pin 1b94d50b8c, built Un0wVZqj) proven on the TEMPLATE lane (file_base64); no new grant; rollback ZspX0qD2 / S3 objver LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v; pair NEVER_WIDEN_PAIR_RELEASE3_A1 + CTO half AMENDMENT 1
**Authored by:** 0.9.0_WK_IRPT_BCKEND~159
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks: pin ancestor, census=4 members, live CodeSha256 == ZspX0qD2, grant read-back, rollback objver | ancestor rc0 + changed_members=4 + live hash + grant statements + rollback objver | pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_access.py, served.py, uploads.py); live CodeSha256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= LastModified 2026-10-08T20:44:41Z; role policy irpt-ycharts-generate holds 16 Sids incl ReadPartnerProfileRowForOnBehalfAdvisor (GetItem on exactly opal-partner-49financial/-inflection/-cottonwood) and RetainOriginalHoldingsUploadsOnly (original_holdings, 3 firms), and does NOT hold RetainOriginalCsvUploadsOnly; ROLLBACK SOURCE S3 current versionId LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v content-sha256 ZspX0qD2..; shared ycharts tf dir diff HEAD empty | CLOSED 20261008T212240Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == Un0wVZqj.. + new versionId | build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: SHA256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= (== signed), s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip size=591141, new versionId NqbpRnnx5METt43XaI_4nmk5fZDRTQpk, content-sha256 metadata Un0wVZqj.. (head-object). Running code unchanged by this leg. | CLOSED 20261008T212414Z |
| L3 | activation | safe-apply of ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this 0 add 1 change 0 destroy | apply output + live CodeSha256 == Un0wVZqj.. | dell2 apply from shared initialized ycharts root: saved plan (Y68-1_plan.txt, committed 16f4e4ac90) 0 add / 1 change / 0 destroy (s3_object_version LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v -> NqbpRnnx5METt43XaI_4nmk5fZDRTQpk, source_code_hash ZspX0qD2.. -> Un0wVZqj..); .tools/safe-apply.sh apply of the saved plan; live after: CodeSha256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= LastModified 2026-10-08T21:26:18Z Active/Successful; targeted re-plan No changes rc0; census invoke modules 62 failed={} | CLOSED 20261008T212722Z |
| L4 | verify | after-reads 1-7, test row deleted NOT FOUND, admit keys handed to laptop | after-reads file + NOT FOUND read + admit_keys file | BRANCH A (all reads pass): reads 0-3 PASS, read 4 STORED-NEXT-STATE (template-lane on-behalf admit by test filer for advisor adv-04b85b8aefda at 49financial: RESOLVING then NORMALIZED, upload_id UP-a5f12db5..., 1 resolve_upload), read 5 NOT_AUTHORIZED (adv-27637b75127c), read 6 FIRM_BINDING, read 7 NOT_AUTHORIZED, no write on 5-7. Test filer row deleted, consistent get-item no Item. 9 admit keys (7 ddb derived, 2 s3 confirmed by list) handed to the laptop in Y68-1_admit_keys.json. After-reads file Y68-1_release3_after_reads.json. Live == Un0wVZqj.., rolled_back false. | CLOSED 20261008T213418Z |

## Log

- 20261008T212224Z OPENED by 0.9.0_WK_IRPT_BCKEND~159 with 4 leg(s)
- 20261008T212240Z LEG L1 closed: pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_acces
- 20261008T212414Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: SHA256 Un0wVZqjqpwKhpYyFeBRW3fVFddrlHR0BtHjYuP5eNY= (=
- 20261008T212722Z LEG L3 closed: dell2 apply from shared initialized ycharts root: saved plan (Y68-1_plan.txt, committed 16f4e4ac90) 0 add / 1 change / 0
- 20261008T213418Z LEG L4 closed: BRANCH A (all reads pass): reads 0-3 PASS, read 4 STORED-NEXT-STATE (template-lane on-behalf admit by test filer for adv
- 20261008T213418Z CLOSED -- all 4 legs proven
