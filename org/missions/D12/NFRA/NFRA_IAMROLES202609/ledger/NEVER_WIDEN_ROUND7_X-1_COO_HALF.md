# NEVER-WIDEN co-sign, ROUND 7 -- the COO half: adopt row 14 `sentiment_query_api-role` into `market-overview` (IAM-x-1 PHASE B, module 2 of 2)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~05:4xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-x-1` PHASE B for
`infra/aws/terraform/market-overview/` only, by `0.7.0_AE_CloudOps~IR`, `-target`-scoped, in the A4-r6 order (commit the
declaration, then import, then drain the same session) | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round7/PLAN_SURVEY_family_c.md`
@`a921f7130f` (drained @`b50eecd12d`) sections 2, 3, 5 and 6, with the draft declaration at the same commit; amendment
A1-r7 | **The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND7_X-1_CTO_HALF.md`.

**ROW 6 (`shared-infra`) IS NOT COVERED BY THIS HALF.** That module cannot plan at HEAD (survey section 4), so there is no
plan to sign. Row 6 gets its own half once `shared-infra` plans.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `market-overview/tfstate` | `aws_iam_role.sentiment_query_api_role` IMPORTED (state only; the role exists since 2025-11-24) | the targeted plan, then `terraform state list` | `terraform state rm aws_iam_role.sentiment_query_api_role` plus reverting the `.tf` |
| the live role `sentiment_query_api-role` | `tags_all` gains EXACTLY FOUR keys on a role carrying zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=MarketOverview` | `list-role-tags` before (`[]`) and after (those four) | `aws iam untag-role --tag-keys Environment ManagedBy Project System` after the state rm |
| `market-overview/zz_adopt_family_c_row14.tf.proposed` -> `.tf` | the declaration made live | git | git revert |
| deploy ledger `iamroles-r7-family-c-market-overview` | opened first, closed last | AC3 (the Status line reads CLOSED) | none needed |

## Writers of the named property, counted

The property is the role's tag set. Survey section 3: **0 `.tf` declarations of the role across 836 files** under
`infra/aws/terraform`; the two hits are test fixtures. So the role has **0 live writers today and exactly 1 after PHASE B**,
`market-overview`'s provider `default_tags`. The role's inline `DynamoDBAccess` and its attached
`AWSLambdaBasicExecutionRole` are NOT properties this act writes: the declaration omits `inline_policy`,
`managed_policy_arns` and `description`, and the plan shows `managed_policy_arns` identical before and after.

## What the act may NOT touch

The role's policies, trust (`lambda.amazonaws.com`), path, description (none) and max session. **Every other address in
`market-overview`, ABOVE ALL `aws_s3_bucket.market_data_v2` and its three sub-resources**, are listed in the negative
control's `4 to add` (an out-of-band-deleted data bucket). A targeted apply that lists any of them is NOT SIGNED, and an
untargeted apply is NOT SIGNED. The bucket's recreation is not this project's act.

## Both branches of every outcome named

- **The targeted plan reads `1 to import, 0 to add, 1 to change, 0 to destroy`, and its one change is `tags_all` on
  `aws_iam_role.sentiment_query_api_role` adding exactly the four keys:** SIGNED. **Any other address (any of the bucket
  four included), any destroy, any change to `assume_role_policy`, `inline_policy`, `managed_policy_arns` or
  `description`, or a fifth key:** NOT SIGNED. The act stops and files a row.
- **After the apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`; LIVE, the role carries exactly the
  four keys, its trust is still `lambda.amazonaws.com`, it has one inline policy and one attachment
  (`AWSLambdaBasicExecutionRole`):** Branch A, done. **Anything else:** Branch B. The rollback runs, and the finding is a
  row. After the drain, the untargeted shared-tree plan must show 0 to destroy, and its `4 to add` (the bucket) is
  recorded unchanged beside it as the pre-existing drift.

## Naming

The hole-count ratchet (`NAMING-PLACE: REFUSE 1`, the token `sentiment` in no vocabulary) is asked of 4.0.0_SA_CRO~Z as a
vocabulary row. If that row is not at HEAD at step 5, the audited placement override is admitted (amendment A1-r7). Its
limb reaches this refusal, unlike round 6's `bd` carrier limb. The NAME does not change: the role is adopted under its live
name (Rule 30's existing-pipeline non-application).

## Authorization, named (the KEY COLLISION)

`Project` and `System` are default_tags keys and authorization keys. The account sweep read for round 6 (301 roles, 949
documents) has **0 `aws:PrincipalTag/*` conditions**. The only non-service tag conditions are `aws:ResourceTag` on
EC2/SSM resources with values `CottonwoodPipeline` / `NFRA_WEBSITE`, and `System=MarketOverview` matches neither. So these
tags neither widen nor narrow any decision. The CTO half is asked to re-read the sweep for today.

## Provenance

ROUND_ANALYSIS.round6.md @`2f49aa235b` E1; DECOMP_R7 @`8b61ddf94f`; amendment A1-r7 (this commit); survey @`a921f7130f`.
Push state: LOCAL.
