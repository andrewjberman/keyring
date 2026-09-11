# Deploy Completion Record
**Date opened:** 2026-09-11T01:03:19.410256+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-13 -- the shared irpt-common layer: build, upload, publish and attach to irpt-performance-adapter (surprise row IRPT_BCKEND-W4-S3)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the layer source, the performance root layers.tf and env pins, and the CI map registrations | commit hash |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-layers/irpt-common.zip | head-object ContentLength + content-sha256 equal to the built zip |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (aws_lambda_layer_version.irpt_common + the attach on module.irpt_performance_adapter) | safe-apply output |  | OPEN |
| L4 | verify | get-function-configuration irpt-performance-adapter shows a Layers[].Arn containing irpt-common, an invoke returns contract_validated true, and the root re-plans 0-diff | verbatim CLI output |  | OPEN |

## Log

- 20260911T010319Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
