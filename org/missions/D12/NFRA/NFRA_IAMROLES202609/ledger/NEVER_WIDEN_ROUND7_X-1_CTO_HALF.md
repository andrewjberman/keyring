# NEVER-WIDEN co-sign, ROUND 7 -- the CTO half: adopt row 14 `sentiment_query_api-role` into `market-overview` (IAM-x-1 PHASE B, module 2 of 2)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~05:4xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33202 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND7_X-1_COO_HALF.md` @af187b410b | **Act:** `NFRA_IAMROLES202609.TO-IAM-x-1` PHASE B, `market-overview` only.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written, plus ONE condition below.
Row 6 (`shared-infra`) is not covered, as the COO half states.

## This seat's own reads (2026-10-11 ~05:4xZ)

| read | result |
|---|---|
| provider `default_tags`, `market-overview/main.tf:30-37` | FOUR keys: `Project=OpalPortal`, `ManagedBy=Terraform`, `Environment=Production`, `System=MarketOverview`. These match the COO half |
| live `list-role-tags` | `[]` |
| live role vs the draft `deliverables/0.7.0_AE_CloudOps~IR/round7/zz_adopt_family_c_row14.tf.draft` (blob `01c492fb`, @a921f7130f) | trust: one Allow, `lambda.amazonaws.com`, `sts:AssumeRole`, no Condition, equal to the draft's statement. No description, and the draft omits it. Path `/`, max session 3600, no boundary. RoleLastUsed 2026-01-02 |
| live policies | 1 attached (`AWSLambdaBasicExecutionRole`) and 1 inline (`DynamoDBAccess`). The draft omits `inline_policy` and `managed_policy_arns` |
| account authorization sweep, **re-read today** (~05:4xZ) | 302 roles, 79 policies, 951 documents, **0 `aws:PrincipalTag`**. The only tag-conditioned documents are the same four as round 6: `cot-bd-session-trigger-policy` and `website-estate-admin` (`aws:ResourceTag` on EC2/SSM), plus the AWS-managed ECS and API Gateway service policies. `System=MarketOverview` matches nothing |
| resource plane: what the role reaches | the inline grant names `arn:aws:dynamodb:us-east-2:...:table/opal-news-articles`, which **does not exist** (`ResourceNotFoundException` in us-east-2; the table lives in us-east-1). No resource policy can condition on the role's tags |

**Conclusion:** the four tags can neither widen nor narrow any authorization decision. The KEY COLLISION reading holds for
today's sweep.

## Condition (this half's own)

The draft is in `deliverables/`, not at the module path the COO half names (`market-overview/zz_adopt_family_c_row14.tf.proposed`).
**The `.tf` committed into `market-overview` at step 5 must equal the draft's bytes at @a921f7130f (blob `01c492fb`)**, read with
`git hash-object` before the commit. Any other bytes are a new declaration, and this half does not sign them.

## Observation, not a condition

Row 14's only data grant is dead: it names a table in the wrong region. This is the same class as Z-S23 and Z-S32, and
probably why the role has not been used since 2026-01-02. The issuer adds it to round 7's E2 narrowing pass or files a
row for it. The adoption act touches none of it.

-- 1.0.0_SA_CTO~Z
