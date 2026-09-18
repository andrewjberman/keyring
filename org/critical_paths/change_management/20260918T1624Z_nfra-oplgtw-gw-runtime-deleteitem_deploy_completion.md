# Deploy Completion Record
**Date opened:** 2026-09-18T16:24:07.681518+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T163840Z
**Deploy:** Gateway login outage fix: runtime grant gains dynamodb:DeleteItem on RUNTIME#* (Andrew-direct 2026-09-18 ~16:1xZ, branch 1)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-edit plan 0-drift AND post-edit plan exactly 1 in-place change (aws_iam_role_policy.gw_access_state_runtime) | terraform plan output: No changes (pre) ; Plan: 0 to add, 1 to change, 0 to destroy (post), only that address | pre-edit: terraform plan -detailed-exitcode rc=0 'No changes. Your infrastructure matches the configuration.' (16:2xZ, infra/aws/terraform/opal-gateway, scratch tf_plan_pre.txt); post-edit: rc=2, 'Plan: 0 to add, 1 to change, 0 to destroy.', terraform show -json: resource_changes=84, non-no-op=1, address aws_iam_role_policy.gw_access_state_runtime actions=['update'] replace_paths=None (scratch deleteitem.plan.json); the only Action diff is + dynamodb:DeleteItem in Sid AccessStateRuntimeWritesRuntimeKeysOnly | CLOSED 20260918T163143Z |
| L2 | activation | aws_iam_role_policy.gw_access_state_runtime applied via safe-apply from the saved planfile | Apply complete! Resources: 0 added, 1 changed, 0 destroyed + iam get-role-policy shows dynamodb:DeleteItem under the LeadingKeys RUNTIME#* condition | safe-apply (halt-gate PASS after the session .serial was written; naming-apply-gate WARN only on pre-existing names) from saved planfile: 'aws_iam_role_policy.gw_access_state_runtime: Modifications complete after 1s'; 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' (16:3xZ). iam get-role-policy opal-gateway-role/opal-gateway-access-state-runtime, Sid AccessStateRuntimeWritesRuntimeKeysOnly: Action [PutItem, UpdateItem, DeleteItem], Condition ForAllValues:StringLike LeadingKeys [RUNTIME#*] + Null LeadingKeys false | CLOSED 20260918T163840Z |
| L3 | verify | EXERCISED under the instance role opal-gateway-role on the host: conditional delete_item on a RUNTIME#probe key SUCCEEDS (was AccessDeniedException) and a delete on a POLICY# key is still AccessDenied; gateway service active, /mcp 401 via ALB | SSM command output with both arms | SSM 14330e8e-0532-4c3a-a117-90a55d6cf64f on i-07dccb1615503ac99, gateway venv boto3 under opal-gateway-role, 16:37:05Z: ARM1 put RUNTIME#probe-ae-deleteitem-20260918T163705Z OK; ARM2 conditional delete_item RUNTIME# probe SUCCEEDED (journal 14:55:37Z/15:16:07Z had AccessDeniedException on the same action); ARM3 strong read-back present=False; ARM4 delete_item POLICY# key REFUSED AccessDeniedException (LeadingKeys condition intact); systemctl is-active active; local /mcp 401; access-state ALARM count since 16:00Z = 0 | CLOSED 20260918T163840Z |

## Log

- 20260918T162407Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260918T163143Z LEG L1 closed: pre-edit: terraform plan -detailed-exitcode rc=0 'No changes. Your infrastructure matches the configuration.' (16:2xZ, i
- 20260918T163840Z LEG L2 closed: safe-apply (halt-gate PASS after the session .serial was written; naming-apply-gate WARN only on pre-existing names) fro
- 20260918T163840Z LEG L3 closed: SSM 14330e8e-0532-4c3a-a117-90a55d6cf64f on i-07dccb1615503ac99, gateway venv boto3 under opal-gateway-role, 16:37:05Z: 
- 20260918T163840Z CLOSED -- all 3 legs proven
