# Deploy Completion Record
**Date opened:** 2026-10-11T19:52:48.128788+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T200433Z
**Deploy:** OG-ap-8: the ONE market_update PutObject grant aws_iam_role_policy.market_update_gateway_put on opal-gateway-role
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the targeted pre-apply plan captured with its exit code | W/ap8_plan_target.txt and .rc: exactly 1 to add, 0 to change, 0 to destroy on that one address, at rc=0 | Targeted pre-apply plan captured to W/ap8_plan_target.txt with its exit code in W/ap8_plan_target.rc: 'Plan: 1 to add, 0 to change, 0 to destroy.' on the single address aws_iam_role_policy.market_update_gateway_put, at rc=0 with 0 Error lines. The -var came from the BUILDER and was never typed: address('sharepoint','transcripts','bronze','market_update','date=X') minus the date segment yields s3://opal-data-transcripts/sharepoint/transcripts/bronze/market_update/, asserted to end in /bronze/market_update/ before it was passed. The planned shape already matched the halves: name gateway-market-update-put-policy, Action s3:PutObject only, Resource the builder prefix, role opal-gateway-role. The exit code is captured separately because the order says a summary at rc!=0 is not a verdict -- the trap this seat measured at OG-ap-7 step 5b, where an incomplete plan printed 1/0/0 at rc=1. | CLOSED 20261011T200432Z |
| L2 | activation | safe-apply of the same -target and -var from the detached box/sitez-HEAD worktree C-colon-slash-tmp-slash-og-tf-ap8, never a release root (row Z-S81) | apply completes and the policy exists live | Applied via .tools/safe-apply.sh -chdir=C:/tmp/og-tf-ap8/infra/aws/terraform/opal-gateway apply ap8.tfplan -- the SAVED plan, which encodes the same -target and -var and so applies exactly the reviewed row. 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Run from the DETACHED box/sitez-HEAD worktree at 7411ca08922668f0f70611f3f14f15430b510598, never a release root, per COO condition A citing row Z-S81. The cone carries the agent home so the halt gate's premise held with NO HALT_OVERRIDE; the gate's silent pass is not cited as evidence (cloud-ops, LD-0267). The consumed plan file was removed after the apply. | CLOSED 20261011T200432Z |
| L3 | verify | targeted re-plan after the apply | W/ap8_replan.txt and .rc read 0 to add, 0 to change, 0 to destroy at rc=0 | Post-apply targeted re-plan into W/ap8_replan.txt with W/ap8_replan.rc: 'No changes. Your infrastructure matches the configuration.' at rc=0, 0 Error lines, same -target and same builder-derived -var. The act is fully landed and not half-applied. | CLOSED 20261011T200432Z |
| L4 | verify | live read-back by aws iam get-role-policy, recorded in W/ap8_policy.json | ONE statement, Action exactly s3:PutObject, Resource exactly the market_update bronze prefix from address(), no Get/List/Delete and no other prefix | LIVE read-back recorded in W/ap8_policy.json: role opal-gateway-role, policy_name gateway-market-update-put-policy. get-role-policy returns ONE statement, Sid OplgtwPutMarketUpdateBronzeOnly, Effect Allow, Action exactly ['s3:PutObject'], Resource exactly ['arn:aws:s3:::opal-data-transcripts/sharepoint/transcripts/bronze/market_update/*'] -- no Get, List or Delete and no other prefix or bucket, which is the halves' statement exactly. Inline policy count 22 -> 23, so precisely one policy was added and nothing else on the role moved. BEFORE the act the absence was established by the RIGHT predicate rather than by the resource name: 0 of 22 inline policy names matched 'market', with 'advi' matching 1 as a positive control. That mattered because the TF resource name (market_update_gateway_put) is NOT the live policy name (gateway-market-update-put-policy), so a get-role-policy on the resource name returns NoSuchEntity even after a successful apply and would have read as a false absence. | CLOSED 20261011T200433Z |

## Log

- 20261011T195248Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20261011T200432Z LEG L1 closed: Targeted pre-apply plan captured to W/ap8_plan_target.txt with its exit code in W/ap8_plan_target.rc: 'Plan: 1 to add, 0
- 20261011T200432Z LEG L2 closed: Applied via .tools/safe-apply.sh -chdir=C:/tmp/og-tf-ap8/infra/aws/terraform/opal-gateway apply ap8.tfplan -- the SAVED 
- 20261011T200432Z LEG L3 closed: Post-apply targeted re-plan into W/ap8_replan.txt with W/ap8_replan.rc: 'No changes. Your infrastructure matches the con
- 20261011T200433Z LEG L4 closed: LIVE read-back recorded in W/ap8_policy.json: role opal-gateway-role, policy_name gateway-market-update-put-policy. get-
- 20261011T200433Z CLOSED -- all 4 legs proven
