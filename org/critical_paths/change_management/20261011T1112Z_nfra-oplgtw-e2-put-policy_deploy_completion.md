# Deploy Completion Record
**Date opened:** 2026-10-11T11:12:42.341979+00:00
**Status:** OPEN
**Deploy:** OG-ap-6 B2 step 6: the ONE E2 PutObject grant aws_iam_role_policy.advi_billing_gateway_put on opal-gateway-role (targeted apply from detached box/sitez HEAD)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the targeted pre-apply plan captured to deliverables/0.7.0_AE_CloudOps~Z/ap6_plan_target.txt and committed | the commit hash carrying ap6_plan_target.txt, whose header records plan rc and the worktree commit |  | OPEN |
| L2 | activation | terraform apply of the SAVED targeted plan ap6_target.tfplan via safe-apply, -target aws_iam_role_policy.advi_billing_gateway_put only, from C:/tmp/og-tf-e2 detached at 4344db632f | apply completes and the policy exists live |  | OPEN |
| L3 | verify | live read-back of the new inline policy by aws iam get-role-policy on opal-gateway-role | ONE statement, Action exactly s3:PutObject, Resource exactly the fee_statement prefix, no Get/List/Delete and no other prefix |  | OPEN |
| L4 | verify | targeted re-plan after the apply | reads 0 to add, 0 to change, 0 to destroy AND exits rc=0 (a summary at rc!=0 is not a verdict, CTO C3 ruling) |  | OPEN |

## Log

- 20261011T111242Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
