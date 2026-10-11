# Deploy Completion Record
**Date opened:** 2026-10-11T09:28:01.530827+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609.TO-IAM-x-1 PHASE B row 6: adopt lambda-ec2-runtime-monitor-role into shared-infra, targeted
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role.lambda_ec2_runtime_monitor_role in shared-infra | the SAVED targeted plan reads 1 to import / 0 to add / 1 to change / 0 to destroy, the ONE changed attribute is tags_all gaining EXACTLY the four keys Environment=Production ManagedBy=Terraform Project=OpalPortal System=SharedInfra, and the plan contains ZERO restricted_breakglass addresses -- measured by filtering every resource_change address, not by reading the summary, because a bare 1-change would read identically for a trust-policy rewrite. assume_role_policy, inline_policy, managed_policy_arns and description must each read byte-identical before and after. A fifth key, any destroy, or any other address is NOT SIGNED and stops the act. |  | OPEN |
| MANAGED | verify | lambda-ec2-runtime-monitor-role | THE OMISSION RULE'S STOP CONDITION ON A ROLE THAT CARRIES A MANAGED ATTACHMENT: after the apply, list-attached-role-policies still returns EXACTLY 1, AWSLambdaBasicExecutionRole, and list-role-policies still returns EXACTLY 1, EC2RuntimeMonitorPolicy. Setting managed_policy_arns even to [] would detach the role's CloudWatch Logs access; the declaration omits it, and this leg is what proves the omission held in the world rather than only in the plan. |  | OPEN |
| REPLAN | verify | infra/aws/terraform/shared-infra | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy; and AFTER the drain the UNTARGETED plan in the SHARED tree reads 0 to destroy with its pre-existing 2 to add (aws_iam_role.restricted_breakglass + aws_iam_role_policy.restricted_breakglass, ADVI_COTBKF's never-applied pair) UNCHANGED -- unchanged is the test here, not absent, because absorbing those two would mean this act created an IAM role nobody signed. |  | OPEN |
| INVOCATION | verify | lambda-ec2-runtime-monitor-role | THE CTO HALF'S OWN CONDITION: the role is IN USE, so RoleLastUsed must ADVANCE past the apply time within the function's next scheduled run. Read RoleLastUsed immediately before the apply and again after. If it does not advance, a surprise row is filed and NOTHING is rolled back blind -- the CTO half says so explicitly. |  | OPEN |

## Log

- 20261011T092801Z OPENED by 0.7.0_AE_CloudOps~IR with 4 leg(s)
