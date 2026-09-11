# Deploy Completion Record
**Date opened:** 2026-09-11T05:52:02.615760+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-14 -- the export worker and its role, first apply of the investor-reporting/export root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the export package, the terraform root and the source-map entry | commit hash |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object ContentLength + content-sha256 equal to the built zip |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/export (aws_iam_role.export_render + its logs policy + module.irpt_export_render) | safe-apply output |  | OPEN |
| L4 | verify | get-function-configuration irpt-export-render CodeSha256 equals the built zip sha256, the irpt-common layer is attached, an invoke reports its renderer absence, and a 0-diff plan on the root | verbatim CLI output |  | OPEN |

## Log

- 20260911T055202Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
