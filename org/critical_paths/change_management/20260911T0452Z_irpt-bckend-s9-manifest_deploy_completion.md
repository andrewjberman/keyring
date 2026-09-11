# Deploy Completion Record
**Date opened:** 2026-09-11T04:52:42.206701+00:00
**Status:** OPEN
**Deploy:** IB-s-9 artifact revision: repair the STALE FIXTURE_MANIFEST.json (row W3-S9) and redeploy so served bytes equal committed source
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | head-object Metadata.content-sha256 equals the zip rebuilt from the COMMITTED source |  | OPEN |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/ycharts | 1 to change 0 to add 0 to destroy -- ONLY the function's source_code_hash |  | OPEN |
| L3 | verify | lambda get-function-configuration irpt-ycharts-generate | CodeSha256 equals the built zip and the source-map registration |  | OPEN |
| L4 | verify | terraform plan infra/aws/terraform/investor-reporting/ycharts | No changes. Your infrastructure matches the configuration. |  | OPEN |
| L5 | git | wk-irpt_bckend-1-3 | the repair and the OPEN sentinel committed BEFORE the act |  | OPEN |

## Log

- 20260911T045242Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
