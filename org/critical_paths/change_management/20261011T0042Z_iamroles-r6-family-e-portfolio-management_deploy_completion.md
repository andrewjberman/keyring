# Deploy Completion Record
**Date opened:** 2026-10-11T00:42:45.973423+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609 IAM-w-3 PHASE B module 1: adopt portfolio-management-lambda-role into portfolio-management (-target import + THREE default tags, no System key)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| TF | activation | aws_iam_role.portfolio_management_lambda_role | the SAVED targeted plan reads 1 to import / 0 to add / 1 to change / 0 to destroy, tags_all is the only changed attribute, and the keys are EXACTLY THREE -- Environment, ManagedBy, Project -- with NO System key, which this module does not declare; a System key or a fourth key is NOT SIGNED and is a STOP |  | OPEN |
| MANAGED | verify | portfolio-management-lambda-role | THE STOP CONDITION FOR THIS ROLE: list-attached-role-policies reads 1 attached managed policy, AWSLambdaBasicExecutionRole, AFTER the apply exactly as before it -- read LIVE, not from the apply output. This is the program first role with a managed attachment, and setting managed_policy_arns even to [] would detach the grant that gives it CloudWatch Logs access |  | OPEN |
| REPLAN | verify | infra/aws/terraform/portfolio-management | the targeted re-plan reads 0 to add, 0 to change, 0 to destroy, recorded in POST_APPLY_family_e.md; AND after the drain the untargeted plan in the SHARED tree reads 0 to destroy (A4-r6, row Z-S27) |  | OPEN |

## Log

- 20261011T004245Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)
