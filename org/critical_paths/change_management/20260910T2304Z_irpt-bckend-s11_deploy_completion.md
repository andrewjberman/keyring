# Deploy Completion Record
**Date opened:** 2026-09-10T23:04:21.488222+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-11 -- performance adapter Lambda + role, first apply of the investor-reporting/performance root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the adapter package, terraform root and source-map entry | commit hash |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | head-object ContentLength + content-sha256 equal to the built zip |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (aws_iam_role.performance_adapter + module.irpt_performance_adapter) | safe-apply output |  | OPEN |
| L4 | verify | get-function-configuration CodeSha256 equals the built zip sha256, and a 0-diff plan on the root | verbatim CLI output |  | OPEN |

## Log

- 20260910T230421Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
