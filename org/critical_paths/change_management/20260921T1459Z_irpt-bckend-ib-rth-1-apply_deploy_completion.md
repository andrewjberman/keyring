# Deploy Completion Record
**Date opened:** 2026-09-21T14:59:21.625405+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rth-1 arm (d): APPLY the signed loaders.py fix (AccessDenied-as-absent) to the 6 serving functions whose build landed (ledger irpt-bckend-ib-rth-1-build, commit 2c7cff46b0); packet blob 19389dc50b, COO half @6298e74db4, CTO half @5fce993215. Subtraction gate (apply_ib_rth_1.py --plan, 10 roots): each of the 6 roots EXACTLY one aws_lambda_function update, s3_object_version + source_code_hash only, pre-change -> built; api/core/intake EMPTY; ycharts EMPTY apart from the known pre-existing EC2 state drift (runner i-0167fd745ad906a66 running->stopped, 2.0.0_SA_COO~B's host, a stop needs Andrew's word) -- the ycharts root is NOT applied. irpt-ycharts-generate stays at its pre-change bytes (builder refusal, row S111). 0 destroy. Rollback per packet s4: re-publish each function's pre-change CodeSha256 via Terraform pinned to the prior build-store version, never update-function-code.
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/directory (module.irpt_directory_search.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L2 | activation | infra/aws/terraform/investor-reporting/ops (module.irpt_status.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L3 | activation | infra/aws/terraform/investor-reporting/holdings (module.irpt_holdings.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L4 | activation | infra/aws/terraform/investor-reporting/narrative (module.irpt_narrative.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L5 | activation | infra/aws/terraform/investor-reporting/export (module.irpt_export_render.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L6 | activation | infra/aws/terraform/investor-reporting/performance (module.irpt_performance_adapter.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' |  | OPEN |
| L7 | verify | the 10 investor-reporting roots post-apply + served CodeSha256 | fresh plan per root 'No changes.' 10 of 10 (ycharts: only the known EC2 drift) + served CodeSha256 == built 6 of 6 + irpt-ycharts-generate unchanged |  | OPEN |

## Log

- 20260921T145921Z OPENED by 0.7.0_AE_CloudOps~V with 7 leg(s)
