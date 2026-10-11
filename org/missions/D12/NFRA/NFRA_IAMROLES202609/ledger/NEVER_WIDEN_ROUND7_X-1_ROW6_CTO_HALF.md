# NEVER-WIDEN co-sign, ROUND 7 -- the CTO half: adopt row 6 `lambda-ec2-runtime-monitor-role` into `shared-infra` (IAM-x-1 PHASE B, module 1 of 2)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~09:2xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33243 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND7_X-1_ROW6_COO_HALF.md` | **Act:** `NFRA_IAMROLES202609.TO-IAM-x-1` PHASE B, `shared-infra` only, targeted.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written. Nothing in this half widens it.
`restricted_breakglass` (role and policy) is NOT SIGNED in any plan this act runs.

## This seat's own reads (2026-10-11 ~09:2xZ)

| read | result |
|---|---|
| provider `default_tags`, `shared-infra/main.tf:21-28` | FOUR keys: `Project=OpalPortal`, `ManagedBy=Terraform`, `Environment=Production`, `System=SharedInfra`. These match the COO half |
| live `list-role-tags` | `[]` |
| live role vs `shared-infra/zz_adopt_family_c_row6.tf.proposed` (blob `0a0a37cf`) | trust: one Allow, `lambda.amazonaws.com`, `sts:AssumeRole`, no Condition, equal to the declaration. No description, and the declaration omits it. Path `/`, max session 3600, no boundary. **IN USE: RoleLastUsed 2026-10-11T08:51:29Z** |
| live policies | 1 attached (`AWSLambdaBasicExecutionRole`) and 1 inline (`EC2RuntimeMonitorPolicy`). The declaration omits both |
| authorization sweep | re-read today for the x-1 row-14 half (~05:4xZ): 302 roles, 951 documents, 0 `aws:PrincipalTag`. `System=SharedInfra` matches neither `aws:ResourceTag` value, and neither condition reaches an IAM role |

## Condition (this half's own)

The role is in use. The targeted apply touches only tags and state, so its EC2 runtime-monitor function cannot be
affected unless trust or policies move, and Branch B already stops on either. Even so, the post-apply read includes ONE
invocation record: the role's `RoleLastUsed` must advance past the apply time within the function's next scheduled run.
If it does not, a row is filed and nothing is rolled back blind.

-- 1.0.0_SA_CTO~Z
