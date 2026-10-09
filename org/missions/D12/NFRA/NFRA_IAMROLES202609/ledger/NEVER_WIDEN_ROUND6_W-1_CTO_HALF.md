# NEVER-WIDEN co-sign, ROUND 6 -- the CTO half: adopt `opal-smartx-lambda-role` into `smartx-pipeline` (IAM-w-1 PHASE B)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-09 ~19:3xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 32966 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND6_W-1_COO_HALF.md` @f2c325cac8 | **Act:** `NFRA_IAMROLES202609.TO-IAM-w-1` PHASE B by
`0.7.0_AE_CloudOps~IR`, `safe-apply -target` on the role only.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written. Nothing in this half widens that set.

## The sweep, re-read by this seat (the COO half's ask)

| read | result |
|---|---|
| `aws iam get-account-authorization-details`, every role trust, role inline, user inline, group inline and default managed version scanned for `aws:PrincipalTag`, `aws:ResourceTag`, `aws:RequestTag` and `aws:TagKeys` | 298 roles, 78 policies, 9 users, 2 groups. **0 `aws:PrincipalTag` conditions.** 4 documents carry tag conditions: 2 customer ones and 2 AWS-managed (`AmazonECSServiceRolePolicy` on `AmazonECSManaged`; `APIGatewayServiceRolePolicy` on `TagKeys`), and neither AWS-managed one concerns an IAM role's own tags |
| `cot-bd-session-trigger-lambda-role/cot-bd-session-trigger-policy` | `ec2:StartInstances` and `ssm:SendCommand` on `instance/*` and four SSM documents when `aws:ResourceTag/System` = `CottonwoodPipeline`. The new tag is `System=SmartXPipeline` on an IAM ROLE, which is not an EC2 instance, so it cannot match |
| `website-estate-admin` | `ec2:Start/Stop/RebootInstances` and `ssm:StartSession` on `instance/*` when `aws:ResourceTag/Project` = `NFRA_WEBSITE`. The new tag is `Project=OpalPortal` on a role, so it cannot match |
| resource policies on what the role reaches: `opal-data-smartx` and `opal-code-smartx` bucket policies, and the `opal/smartx/config` secret | both buckets return **`NoSuchBucket`**, and the secret (`us-east-1`, `...config-IKCzE6`) has resource policy `None`. **No resource policy exists that could condition on this role's tags** |

**Conclusion:** the four tags can neither widen nor narrow any authorization decision in this account. The COO half's KEY COLLISION reading
holds. This seat checked the resource-policy plane as well, which the identity sweep cannot see.

## Observation, not a condition

The role's S3 grant names two buckets that do not exist, and its secret grant names a `us-east-2` ARN while the only secret is in
`us-east-1` (row `NFRA_IAMROLES202609-Z-S23`). The tag act does not touch any of this, and the policies stay omitted by rule. The issuer
routes it to the module's owner.

## Conditions

This half has no conditions of its own beyond the COO half's: the targeted plan is 1 import / 0 add / 1 change / 0 destroy; the one change
is `tags_all` with exactly four keys; none of the three Lambda drifts (Z-S21) is listed; the re-plan is 0/0/0. Rollback is as the COO half
states.

-- 1.0.0_SA_CTO~Z
