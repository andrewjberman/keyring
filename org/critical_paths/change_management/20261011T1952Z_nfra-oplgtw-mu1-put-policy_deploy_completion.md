# Deploy Completion Record
**Date opened:** 2026-10-11T19:52:48.128788+00:00
**Status:** OPEN
**Deploy:** OG-ap-8: the ONE market_update PutObject grant aws_iam_role_policy.market_update_gateway_put on opal-gateway-role
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the targeted pre-apply plan captured with its exit code | W/ap8_plan_target.txt and .rc: exactly 1 to add, 0 to change, 0 to destroy on that one address, at rc=0 |  | OPEN |
| L2 | activation | safe-apply of the same -target and -var from the detached box/sitez-HEAD worktree C-colon-slash-tmp-slash-og-tf-ap8, never a release root (row Z-S81) | apply completes and the policy exists live |  | OPEN |
| L3 | verify | targeted re-plan after the apply | W/ap8_replan.txt and .rc read 0 to add, 0 to change, 0 to destroy at rc=0 |  | OPEN |
| L4 | verify | live read-back by aws iam get-role-policy, recorded in W/ap8_policy.json | ONE statement, Action exactly s3:PutObject, Resource exactly the market_update bronze prefix from address(), no Get/List/Delete and no other prefix |  | OPEN |

## Log

- 20261011T195248Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
