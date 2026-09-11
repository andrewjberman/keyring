# Deploy Completion Record
**Date opened:** 2026-09-11T07:29:06.413492+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-16: apply the ops Terraform root (irpt-status Lambda + role); build-and-upload the irpt-status artifact; wire the seven-arm cross-firm recovery proof
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of ops/ deliverables, lambda-source-map.json, terraform | hash pushed |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-status.zip | build-and-upload.sh output line |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/ops (state key investor-reporting/ops/tfstate) | safe-apply Apply complete line with resource count |  | OPEN |
| L4 | verify | post-apply live-state read: get-function-configuration irpt-status CodeSha256 vs built zip; 0-diff plan | the read output |  | OPEN |

## Log

- 20260911T072906Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
