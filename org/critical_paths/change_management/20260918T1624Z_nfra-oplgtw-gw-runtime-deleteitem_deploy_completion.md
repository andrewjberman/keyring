# Deploy Completion Record
**Date opened:** 2026-09-18T16:24:07.681518+00:00
**Status:** OPEN
**Deploy:** Gateway login outage fix: runtime grant gains dynamodb:DeleteItem on RUNTIME#* (Andrew-direct 2026-09-18 ~16:1xZ, branch 1)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-edit plan 0-drift AND post-edit plan exactly 1 in-place change (aws_iam_role_policy.gw_access_state_runtime) | terraform plan output: No changes (pre) ; Plan: 0 to add, 1 to change, 0 to destroy (post), only that address |  | OPEN |
| L2 | activation | aws_iam_role_policy.gw_access_state_runtime applied via safe-apply from the saved planfile | Apply complete! Resources: 0 added, 1 changed, 0 destroyed + iam get-role-policy shows dynamodb:DeleteItem under the LeadingKeys RUNTIME#* condition |  | OPEN |
| L3 | verify | EXERCISED under the instance role opal-gateway-role on the host: conditional delete_item on a RUNTIME#probe key SUCCEEDS (was AccessDeniedException) and a delete on a POLICY# key is still AccessDenied; gateway service active, /mcp 401 via ALB | SSM command output with both arms |  | OPEN |

## Log

- 20260918T162407Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
