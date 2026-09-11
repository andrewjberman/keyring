# Deploy Completion Record
**Date opened:** 2026-09-11T01:03:44.231072+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-13 -- the narrative Lambda and its read-only role, first apply of the investor-reporting/narrative root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the narrative package, the terraform root and the source-map entry | commit hash |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | head-object ContentLength + content-sha256 equal to the built zip |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/narrative (aws_iam_role.narrative + two read-only policies + module.irpt_narrative) | safe-apply output |  | OPEN |
| L4 | verify | get-function-configuration irpt-narrative CodeSha256 equals the built zip sha256, the layer is attached, and a 0-diff plan on the root | verbatim CLI output |  | OPEN |

## Log

- 20260911T010344Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
