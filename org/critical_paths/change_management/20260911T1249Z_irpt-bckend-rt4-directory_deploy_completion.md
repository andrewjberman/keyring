# Deploy Completion Record
**Date opened:** 2026-09-11T12:49:26.860969+00:00
**Status:** OPEN
**Deploy:** IB-rt-4 (directory root): typed ids at every key boundary and the ONE error envelope -- code change only
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/ | head-object Metadata.content-sha256 equals the zip rebuilt from COMMITTED source, per function in this root |  | OPEN |
| L2 | activation | terraform apply infra/aws/terraform/investor-reporting/directory | the plan shows ONLY the code change (source_code_hash + s3_object_version); 0 to add, 0 to destroy |  | OPEN |
| L3 | verify | lambda get-function-configuration | CodeSha256 equals the built zip and the source-map registration, per function in this root |  | OPEN |
| L4 | verify | terraform plan | No changes. Your infrastructure matches the configuration. |  | OPEN |
| L5 | git | wk-irpt_bckend-2-3 | the code, the source map and the OPEN sentinel committed BEFORE the act |  | OPEN |

## Log

- 20260911T124926Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
