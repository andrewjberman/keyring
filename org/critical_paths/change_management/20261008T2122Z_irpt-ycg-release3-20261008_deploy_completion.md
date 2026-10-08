# Deploy Completion Record
**Date opened:** 2026-10-08T21:22:24.415763+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate release 3: the E6 build (pin 1b94d50b8c, built Un0wVZqj) proven on the TEMPLATE lane (file_base64); no new grant; rollback ZspX0qD2 / S3 objver LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v; pair NEVER_WIDEN_PAIR_RELEASE3_A1 + CTO half AMENDMENT 1
**Authored by:** 0.9.0_WK_IRPT_BCKEND~159
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks: pin ancestor, census=4 members, live CodeSha256 == ZspX0qD2, grant read-back, rollback objver | ancestor rc0 + changed_members=4 + live hash + grant statements + rollback objver | pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_access.py, served.py, uploads.py); live CodeSha256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= LastModified 2026-10-08T20:44:41Z; role policy irpt-ycharts-generate holds 16 Sids incl ReadPartnerProfileRowForOnBehalfAdvisor (GetItem on exactly opal-partner-49financial/-inflection/-cottonwood) and RetainOriginalHoldingsUploadsOnly (original_holdings, 3 firms), and does NOT hold RetainOriginalCsvUploadsOnly; ROLLBACK SOURCE S3 current versionId LF5iMV9_9RtJ6z.v.SOW7iGLD2j8JN0v content-sha256 ZspX0qD2..; shared ycharts tf dir diff HEAD empty | CLOSED 20261008T212240Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == Un0wVZqj.. + new versionId |  | OPEN |
| L3 | activation | safe-apply of ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this 0 add 1 change 0 destroy | apply output + live CodeSha256 == Un0wVZqj.. |  | OPEN |
| L4 | verify | after-reads 1-7, test row deleted NOT FOUND, admit keys handed to laptop | after-reads file + NOT FOUND read + admit_keys file |  | OPEN |

## Log

- 20261008T212224Z OPENED by 0.9.0_WK_IRPT_BCKEND~159 with 4 leg(s)
- 20261008T212240Z LEG L1 closed: pin 1b94d50b8c ancestor of worktree HEAD rc0; release-census changed_members=4 (generate_installed.py, interactive_acces
