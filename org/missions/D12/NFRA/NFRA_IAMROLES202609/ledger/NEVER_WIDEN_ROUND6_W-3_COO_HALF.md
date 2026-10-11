# NEVER-WIDEN co-sign, ROUND 6 -- the COO half: adopt row 11 into `portfolio-management` and row 3 into `news-pipeline` (IAM-w-3 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-10 ~23:3xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-w-3` PHASE B, by
`0.7.0_AE_CloudOps~IR` through `safe-apply` in TWO modules, each `-target`-scoped (A2-r6), in the order of acts A4-r6 /
A5-r6 fix (commit the renamed `.tf` first, then import, then drain the same session) | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round6/PLAN_SURVEY_family_e.md` @`8361e51c56` (drained @`f219486b2a`), with
`portfolio-management/zz_adopt_family_e.tf.proposed` and `news-pipeline/zz_adopt_row3.tf.proposed` at the same commit |
**The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND6_W-3_CTO_HALF.md`. No PHASE B GO until both halves are
files. (Originally also: AND w-2's PHASE B has landed, by plan order. RELEASED by A7-r6 2026-10-11, row Z-S36: w-2 PHASE B
is held on the sovereign R20 call of row Z-S34, and portfolio-management / news-pipeline share no state with bd-pipeline.
The blast radius signed below is unchanged.)

**Verdict:** SIGNED for the two blast radii below, each on its own, and ONLY them. **The two modules write DIFFERENT
tag sets (survey section 2): THREE keys on row 11, FOUR on row 3.** Neither number carries to the other module.

## MODULE 1 -- `portfolio-management`, role `portfolio-management-lambda-role` (row 11)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `portfolio-management/tfstate` | `aws_iam_role.portfolio_management_lambda_role` IMPORTED (state only; the role exists since 2026-02-19) | the targeted plan, then `terraform state list` | `terraform state rm aws_iam_role.portfolio_management_lambda_role` plus reverting the `.tf` rename |
| the live role | `tags_all` gains EXACTLY THREE keys on a role carrying zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`. **No `System` key: this module declares none.** | `aws iam list-role-tags` before (`[]`) and after (those three) | `aws iam untag-role --tag-keys Environment ManagedBy Project` after the state rm |
| `portfolio-management/zz_adopt_family_e.tf.proposed` -> `.tf` | the rename that makes the declaration live | git | git revert |
| deploy ledger `iamroles-r6-family-e-*` for this module | opened first, closed last | AC3 | none needed |

**Stop condition specific to this role:** `managed_policy_arns` must show NO change. The attached
`arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole` must survive, verified LIVE with
`list-attached-role-policies` after the apply (1 before, the same 1 after), not from the apply's output.

## MODULE 2 -- `news-pipeline`, role `codebuild-semantic-clustering-role` (row 3)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `news-pipeline/tfstate` | `aws_iam_role.codebuild_semantic_clustering_role` IMPORTED (state only; the role exists since 2026-02-17) | the targeted plan, then `terraform state list` | `terraform state rm aws_iam_role.codebuild_semantic_clustering_role` plus reverting the `.tf` rename |
| the live role | `tags_all` gains EXACTLY FOUR keys on a role carrying zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=NewsPipeline` | `list-role-tags` before (`[]`) and after (those four) | `aws iam untag-role --tag-keys Environment ManagedBy Project System` after the state rm |
| `news-pipeline/zz_adopt_row3.tf.proposed` -> `.tf` | the rename | git | git revert |
| deploy ledger `iamroles-r6-family-e-*` for this module | opened first, closed last | AC3 | none needed |

**Stop condition specific to this role:** `assume_role_policy` must show NO change. The principal is
`codebuild.amazonaws.com`, and the role is IN USE (RoleLastUsed 2026-09-11). Verify it LIVE with `get-role` after the
apply. The declaration omits `description` because the role has none, so a plan that sets it is NOT SIGNED.

## Writers of the named property, counted

The property is each role's tag set. Survey section 7: **0 declarations of either role across 834 files** under
`infra/aws/terraform` at the cut (70 binary and 9 ephemeral-floor files not searched, stated). So each role has **0 live
writers today and exactly 1 after PHASE B**: its module's provider `default_tags`. That makes 2 writers in all, one per
role, and both rules were read from the provider blocks. Neither role's inline policy (`portfolio-s3-dynamodb`;
`CodeBuildSemanticClusteringPolicy`) nor row 11's managed attachment is a property this act writes: both declarations
omit `inline_policy` and `managed_policy_arns` (AC1 grep reads 0), and the plans show both unchanged.

## What the act may NOT touch

Each role's policies, trust, path, description and max session; any other address in either module. The survey's
negative controls read **"No changes"** in both modules (zero pre-existing drift, unlike Family B), and the plans hold
exactly ONE non-no-op of 39 and of 141 resource_changes. A targeted apply listing any other address, in either module,
is NOT SIGNED. The five pre-existing `fmt -check` failures (survey section 6) are NOT touched.

## Both branches of every outcome named, per module

- **The targeted plan reads `1 to import, 0 to add, 1 to change, 0 to destroy`, and its one change is `tags_all` on that
  module's role adding exactly that module's keys (3 for portfolio-management, 4 for news-pipeline):** SIGNED. **Any other
  address, any destroy, any change to `assume_role_policy`, `inline_policy`, `managed_policy_arns` or `description`, a
  `System` key in portfolio-management, or a fifth key in news-pipeline:** NOT SIGNED. The act stops and files a row.
  An open `.open_deploys/` entry on the same module before step 4 also means NOT SIGNED.
- **After each apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`, the live tags are exactly that
  module's set, and the stop condition holds live:** Branch A, done. **Anything else:** Branch B. The rollback runs,
  and the finding is a row. After the drain, the untargeted shared-tree plan in each module must read `0 to destroy`
  (A4-r6, row Z-S27).

## Authorization, named (the KEY COLLISION)

`Project` (both modules) and `System` (news-pipeline only) are both default_tags keys and authorization keys
(comp-tagauthz `--from-plan`, verbatim in the survey). The survey re-swept `get-account-authorization-details` today:
301 roles, 78 policies, 9 users, 2 groups, no SCPs (not an Organization member). It reads **0 `aws:PrincipalTag/*`
conditions account-wide**. The only two non-service tag conditions are `aws:ResourceTag` on EC2/SSM resources
(`System=CottonwoodPipeline`, `Project=NFRA_WEBSITE`). Neither reaches an IAM role, and neither value matches
`OpalPortal` / `NewsPipeline`. So these tags can neither widen nor narrow any decision. comp-tagauthz's own GATE pass
was over **0 candidates**, an empty denominator, and this half does NOT rest on it. The CTO half is asked to re-read
the sweep.

## Provenance

ROUND_ANALYSIS.round5.md @`f77e32d7c3` E3; DECOMP_R6 @`c838c9347a`; A2-r6 @`3293b97a90`; A3-r6 @`29f269fca3`;
A4-r6 @`7af7a24e9f`; A5-r6 @`f37fb5892d`; survey @`8361e51c56`. Push state: LOCAL.
