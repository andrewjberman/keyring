# Deploy Completion Record
**Date opened:** 2026-09-11T15:35:37.190901+00:00
**Status:** OPEN
**Deploy:** IB-rt-4 (export root): the ONE error envelope on IB-rt-8's controller, and the import closure download.py has needed since round 1
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object Metadata.content-sha256 equals the zip rebuilt from COMMITTED source; import closure verified in the /var/task + /opt/python layout BEFORE registration |  | OPEN |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/export | the plan shows ONLY this cell's code change -- 0 to add, 0 to destroy, source_code_hash and s3_object_version the only differing attributes |  | OPEN |
| L3 | verify | lambda get-function-configuration irpt-export-render | CodeSha256 equals the built zip and the source-map registration; the triple equality reads 6 of 6 across every impacted function |  | OPEN |
| L4 | verify | terraform plan infra/aws/terraform/investor-reporting/export | No changes. Your infrastructure matches the configuration. |  | OPEN |
| L5 | git | wk-irpt_bckend-2-3 | the code, the source map and the OPEN sentinel committed BEFORE the act |  | OPEN |

## Log

- 20260911T153537Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
