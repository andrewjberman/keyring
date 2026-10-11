# Deploy Completion Record
**Date opened:** 2026-10-11T11:12:42.341979+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T112607Z
**Deploy:** OG-ap-6 B2 step 6: the ONE E2 PutObject grant aws_iam_role_policy.advi_billing_gateway_put on opal-gateway-role (targeted apply from detached box/sitez HEAD)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the targeted pre-apply plan captured to deliverables/0.7.0_AE_CloudOps~Z/ap6_plan_target.txt and committed | the commit hash carrying ap6_plan_target.txt, whose header records plan rc and the worktree commit | Targeted pre-apply plan captured to deliverables/0.7.0_AE_CloudOps~Z/ap6_plan_target.txt and committed @8a79550c21. The capture reads exactly one row, 'aws_iam_role_policy.advi_billing_gateway_put will be created', with 'Plan: 1 to add, 0 to change, 0 to destroy.' AND terraform exit code 0 and 0 Error lines -- both limbs of CTO C3 ruling @eb37eb2e29 asserted separately, because at step 5b an incomplete plan printed exactly 1/0/0 while exiting rc=1 after a failed data source dropped a row. | CLOSED 20261011T112432Z |
| L2 | activation | terraform apply of the SAVED targeted plan ap6_target.tfplan via safe-apply, -target aws_iam_role_policy.advi_billing_gateway_put only, from C:/tmp/og-tf-e2 detached at 4344db632f | apply completes and the policy exists live | Applied via .tools/safe-apply.sh -chdir=C:/tmp/og-tf-e2/infra/aws/terraform/opal-gateway apply ap6_target.tfplan -- the SAVED targeted plan, so the apply executed exactly the reviewed one row. Terraform reported 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' The worktree was DETACHED at the HEAD of the act 4344db632f8c7da29d6bdb47f05581ac62266fa4 with advi_billing_gateway_iam.tf blob re-checked = 49c420acbce7cfb99c8726f5439b3f2cc6ea9f5a. Never applied from the release worktree og-rel16c, per AMENDMENT 1. | CLOSED 20261011T112607Z |
| L3 | verify | live read-back of the new inline policy by aws iam get-role-policy on opal-gateway-role | ONE statement, Action exactly s3:PutObject, Resource exactly the fee_statement prefix, no Get/List/Delete and no other prefix | LIVE aws iam get-role-policy --role-name opal-gateway-role --policy-name gateway-49f-advi-billing-put-policy returns ONE statement: Sid AdviBillingPutFeeStatementBronzeOnly, Effect Allow, Action exactly ['s3:PutObject'], Resource exactly ['arn:aws:s3:::opal-data-assets/smartx/49financial/bronze/fee_statement/*']. No Get, List or Delete; no other prefix or bucket -- the CTO half's grant shape exactly. Inline policy count on the role moved 21 -> 22, so precisely one policy was added. BEFORE the act the same get-role-policy returned NoSuchEntity while a positive control on gateway-mcportal-fabric-read-policy returned its name, so the pre-act absence was real and not an instrument failure. | CLOSED 20261011T112432Z |
| L4 | verify | targeted re-plan after the apply | reads 0 to add, 0 to change, 0 to destroy AND exits rc=0 (a summary at rc!=0 is not a verdict, CTO C3 ruling) | Post-apply targeted re-plan from the same worktree reads 'No changes. Your infrastructure matches the configuration.' with terraform exit code 0 and 0 Error lines -- the 0/0/0 state CTO C3's ruling requires, with the exit-code limb asserted separately rather than read off the summary line. The act is fully landed and not half-applied. | CLOSED 20261011T112607Z |

## Log

- 20261011T111242Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20261011T112432Z LEG L1 closed: Targeted pre-apply plan captured to deliverables/0.7.0_AE_CloudOps~Z/ap6_plan_target.txt and committed @8a79550c21. The 
- 20261011T112432Z LEG L3 closed: LIVE aws iam get-role-policy --role-name opal-gateway-role --policy-name gateway-49f-advi-billing-put-policy returns ONE
- 20261011T112607Z LEG L2 closed: Applied via .tools/safe-apply.sh -chdir=C:/tmp/og-tf-e2/infra/aws/terraform/opal-gateway apply ap6_target.tfplan -- the 
- 20261011T112607Z LEG L4 closed: Post-apply targeted re-plan from the same worktree reads 'No changes. Your infrastructure matches the configuration.' wi
- 20261011T112607Z CLOSED -- all 4 legs proven
