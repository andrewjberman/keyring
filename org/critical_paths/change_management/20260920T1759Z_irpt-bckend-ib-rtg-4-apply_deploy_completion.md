# Deploy Completion Record
**Date opened:** 2026-09-20T17:59:38.559477+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T184445Z
**Deploy:** IRPT_BCKEND.TO-IB-rtg-4 -- apply irpt-holdings pointer-follow fix (holdings root only). Both never-widen halves at HEAD, packet-keyed, blob b515836bb4db340dd1a4a6fb630ab70627432f3a. source_code_hash uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA= -> rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=. Rollback: re-publish prior CodeSha256 via Terraform pinned to build-store VersionId=U4sKRs.HJ0Jc4Ik323Y0b.qY7LsWU2Pg, never update-function-code.
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | tf-lambda | module.irpt_holdings.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/holdings apply <planfile> rc=0: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Post-apply verification: get-function-configuration CodeSha256=rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0= (was uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA= before). Post-apply re-plan: 'No changes.' (0-diff). Subtraction gate PASS: 132 resource_changes entries compared across 10 roots, 10 paths subtracted (top-level .timestamp x10; 0 s3-data-source version_id/last_modified hits this round); holdings shows EXACTLY module.irpt_holdings.aws_lambda_function.this update, source_code_hash uS+WBeN...->rAAn3bt7..., handler unchanged (already entry.lambda_handler); the 6 non-round-7 roots (api,core,directory,intake,narrative,ycharts) each EMPTY; the 3 sibling round-7 roots (export,ops,performance) each show EXACTLY their own packet-declared build (export cn8YKEP2...+aws_iam_role_policy.export_render_receipt create; ops B0AmyfRK...; performance W4rYXgZz...) and nothing else. | CLOSED 20260920T184429Z |

## Log

- 20260920T175938Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 1 leg(s)
- 20260920T184429Z LEG L1 closed: safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/holdings apply <planfile> rc=0: 'Apply complete! Resources: 
- 20260920T184445Z CLOSED -- all 1 legs proven
