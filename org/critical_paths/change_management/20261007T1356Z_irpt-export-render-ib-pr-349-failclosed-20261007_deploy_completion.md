# Deploy Completion Record
**Date opened:** 2026-10-07T13:56:07.983471+00:00
**Status:** OPEN
**Deploy:** EMERGENCY IB-pr-343 release: irpt-export-render export reads fail closed, pin b921635dad, 9 members, laptop applier by hash
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-release baseline: live CodeSha256 exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg= == S3 objver MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3 == tfstate source_code_hash; ROLLBACK SOURCE = s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip?versionId=MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3 | three-plane read printed |  | OPEN |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-export-render -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | built sha256 + new versionId |  | OPEN |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/export from saved planfile; only code + object version, 0 to destroy | apply output + 0-diff re-plan |  | OPEN |
| L4 | verify | after-reads IB68-1: deployed sha==built, replan 0, live entry.py fc241d806ecc, existing export refused, new/performance/analysis READY, admitted-read log line, outside path refused, Opal caller served | IB68-1_release_after_reads.json + IB68-1-AC1 PASS |  | OPEN |

## Log

- 20261007T135607Z OPENED by 0.7.0_AE_CloudOps~I with 4 leg(s)
