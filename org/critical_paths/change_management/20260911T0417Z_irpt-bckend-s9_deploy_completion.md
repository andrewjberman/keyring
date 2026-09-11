# Deploy Completion Record
**Date opened:** 2026-09-11T04:17:28.235510+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-9: upload irpt-ycharts-generate.zip and ADD the generation Lambda and its role to the already-applied investor-reporting/ycharts root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | put-object VersionId plus content-sha256 object metadata equal to the locally built zip |  | OPEN |
| L2 | activation | terraform root infra/aws/terraform/investor-reporting/ycharts -- ADDITIONS ONLY to the root IB-s-8 applied | safe-apply Apply complete line showing only added resources, 0 changed 0 destroyed |  | OPEN |
| L3 | verify | served bytes are the built bytes | get-function-configuration irpt-ycharts-generate CodeSha256 == the built zip base64 sha256 |  | OPEN |
| L4 | verify | the root is CONVERGED after the apply | terraform plan: No changes. Your infrastructure matches the configuration. |  | OPEN |
| L5 | git | the generation package, its fixtures and tests, generate.tf and the registrations on wk-irpt_bckend-1-3 | commit hash |  | OPEN |

## Log

- 20260911T041728Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 5 leg(s)
