# Deploy Completion Record
**Date opened:** 2026-09-21T14:59:21.625405+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260921T151007Z
**Deploy:** IRPT_BCKEND IB-rth-1 arm (d): APPLY the signed loaders.py fix (AccessDenied-as-absent) to the 6 serving functions whose build landed (ledger irpt-bckend-ib-rth-1-build, commit 2c7cff46b0); packet blob 19389dc50b, COO half @6298e74db4, CTO half @5fce993215. Subtraction gate (apply_ib_rth_1.py --plan, 10 roots): each of the 6 roots EXACTLY one aws_lambda_function update, s3_object_version + source_code_hash only, pre-change -> built; api/core/intake EMPTY; ycharts EMPTY apart from the known pre-existing EC2 state drift (runner i-0167fd745ad906a66 running->stopped, 2.0.0_SA_COO~B's host, a stop needs Andrew's word) -- the ycharts root is NOT applied. irpt-ycharts-generate stays at its pre-change bytes (builder refusal, row S111). 0 destroy. Rollback per packet s4: re-publish each function's pre-change CodeSha256 via Terraform pinned to the prior build-store version, never update-function-code.
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/directory (module.irpt_directory_search.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | directory: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:00:47Z-15:02:26Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-directory-search CodeSha256 cmh6XwybmdXSiWQkQZMeer7wtw0QW/1lXnAIJlPjJKg= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151006Z |
| L2 | activation | infra/aws/terraform/investor-reporting/ops (module.irpt_status.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | ops: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:02:26Z-15:03:20Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-status CodeSha256 Hos/bFiiIjqK/pPFtaGwbWqTRasDFoA4HHfdfBQoajE= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151006Z |
| L3 | activation | infra/aws/terraform/investor-reporting/holdings (module.irpt_holdings.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | holdings: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:03:20Z-15:04:29Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-holdings CodeSha256 1XkzWP6p8OfobrSCI8ZrRCyMxfWgSK6sPZeYjdON50I= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151007Z |
| L4 | activation | infra/aws/terraform/investor-reporting/narrative (module.irpt_narrative.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | narrative: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:04:29Z-15:05:33Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-narrative CodeSha256 es/S9azussVLY2DfTj6hRjV1pqhZ8EaVCnaVcELqhPc= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151007Z |
| L5 | activation | infra/aws/terraform/investor-reporting/export (module.irpt_export_render.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | export: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:05:33Z-15:06:38Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-export-render CodeSha256 2gSDyxxBQ3t4tupQUf/NV4EegOhxqpA2EPBLSKdInsY= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151007Z |
| L6 | activation | infra/aws/terraform/investor-reporting/performance (module.irpt_performance_adapter.aws_lambda_function.this) | saved planfile digest == gated + safe-apply rc=0 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' | performance: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:06:38Z-15:07:47Z 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; served irpt-performance-adapter CodeSha256 jVktMAiRK+2mYPXEzyst6HjSFFv4xR3Kxm47hAyulyw= == built (IB-rth-1_apply_output.txt) | CLOSED 20260921T151007Z |
| L7 | verify | the 10 investor-reporting roots post-apply + served CodeSha256 | fresh plan per root 'No changes.' 10 of 10 (ycharts: only the known EC2 drift) + served CodeSha256 == built 6 of 6 + irpt-ycharts-generate unchanged | POST-APPLY fresh plan per root 15:07:47Z+: 'No changes.' 9 of 9 non-ycharts roots; ycharts 'Plan: 0 to add, 1 to change' = ONLY the known pre-existing EC2 state drift (aws_ec2_instance_state.runner i-0167fd745ad906a66 running->stopped, 2.0.0_SA_COO~B's host, not applied) -> 0-diff 10 of 10; served CodeSha256 == built 6 of 6; irpt-ycharts-generate UNCHANGED 1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o= (not built, row S111) (IB-rth-1_apply_output.txt) | CLOSED 20260921T151007Z |

## Log

- 20260921T145921Z OPENED by 0.7.0_AE_CloudOps~V with 7 leg(s)
- 20260921T151006Z LEG L1 closed: directory: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:00:47Z-15:02:26Z 'Apply complete! Res
- 20260921T151006Z LEG L2 closed: ops: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:02:26Z-15:03:20Z 'Apply complete! Resources
- 20260921T151007Z LEG L3 closed: holdings: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:03:20Z-15:04:29Z 'Apply complete! Reso
- 20260921T151007Z LEG L4 closed: narrative: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:04:29Z-15:05:33Z 'Apply complete! Res
- 20260921T151007Z LEG L5 closed: export: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:05:33Z-15:06:38Z 'Apply complete! Resour
- 20260921T151007Z LEG L6 closed: performance: saved planfile digest == gated; .tools/safe-apply.sh applied it rc=0 15:06:38Z-15:07:47Z 'Apply complete! R
- 20260921T151007Z LEG L7 closed: POST-APPLY fresh plan per root 15:07:47Z+: 'No changes.' 9 of 9 non-ycharts roots; ycharts 'Plan: 0 to add, 1 to change'
- 20260921T151007Z CLOSED -- all 7 legs proven
