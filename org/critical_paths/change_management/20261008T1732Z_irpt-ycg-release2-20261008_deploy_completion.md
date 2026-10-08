# Deploy Completion Record
**Date opened:** 2026-10-08T17:32:30.825199+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate release 2: TCKT_VNEXT X-1 on-behalf upload by listed OPAL_GLOBAL filer (uploads.py, interactive_access.py, generate_installed.py); pin f7a9d0b34f; built 798Lgqw2..; rollback ZspX0qD2.. / S3 objver 4Pvl.mN3tY9bIQDDVVnGYFiNoKbrUSTh; CTO half 6d24511482
**Authored by:** 0.9.0_WK_IRPT_BCKEND~156
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks: pin ancestor, census=3 members, live CodeSha256 == ZspX0qD2.. | ancestor rc0 + changed_members=3 + live hash read + rollback objver |  | OPEN |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == 798Lgqw2.. + new versionId |  | OPEN |
| L3 | activation | safe-apply of ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this; 0 add 1 change 0 destroy | apply output + live CodeSha256 == 798Lgqw2.. |  | OPEN |
| L4 | verify | after-reads 1-7 + test row and every upload key deleted and read NOT FOUND | after-reads file + NOT FOUND reads |  | OPEN |

## Log

- 20261008T173230Z OPENED by 0.9.0_WK_IRPT_BCKEND~156 with 4 leg(s)
