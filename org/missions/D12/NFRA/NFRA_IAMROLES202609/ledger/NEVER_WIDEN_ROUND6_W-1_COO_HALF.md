# NEVER-WIDEN co-sign, ROUND 6 -- the COO half: adopt `opal-smartx-lambda-role` into `smartx-pipeline` (IAM-w-1 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-09 ~19:0xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-w-1` PHASE B, by
`0.7.0_AE_CloudOps~IR` through `safe-apply` in `infra/aws/terraform/smartx-pipeline/`, `-target`-scoped (amendment A2-r6) |
**Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round6/PLAN_SURVEY_family_b.md` @`4dff2b348a` and
`zz_adopt_family_b.tf.proposed` @`8b6cfcf18a` | **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND6_W-1_CTO_HALF.md`. No PHASE B GO until both halves are files.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `smartx-pipeline/tfstate` | `aws_iam_role.opal_smartx_lambda_role` IMPORTED (state only; the role already exists) | the targeted plan, then `terraform state list` | `terraform state rm aws_iam_role.opal_smartx_lambda_role` (state only, no AWS change) plus reverting the .tf rename |
| the live role `opal-smartx-lambda-role` | `tags_all` gains EXACTLY four keys on a role that carries zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=SmartXPipeline` | `aws iam list-role-tags` before (`[]`) and after (those four) | `aws iam untag-role --tag-keys Environment ManagedBy Project System` after the state rm, or the module's provider default_tags removed for this resource |
| `infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf.proposed` -> `.tf` | the rename that makes the declaration live | git | git revert |
| the deploy ledger `iamroles-r6-family-b` | opened first, closed last | w-1 AC3 | none needed |

**Writers of the named property, counted:** `comp-find '"opal-smartx-lambda-role"' infra` reads 6 hits across 7888 files.
There is ONE declaration, the inert `zz_adopt_family_b.tf.proposed`; the other three files are census and gap data. So
there are 0 live writers today and exactly 1 after PHASE B. **The role's three inline policies** (`opal-smartx-logs`,
`opal-smartx-s3-access`, `opal-smartx-secrets`) are NOT a property this act writes: the declaration omits `inline_policy`
and `managed_policy_arns` (0 matches), and the survey's plan shows them unchanged, 0 detachments.

## What the act may NOT touch

The role's policies, trust, path, description and max session; every `aws_lambda_function` in the module. The plan's
three Lambda changes (`assets_daily_pull`, `jwt_refresher`, `rest_pull` to new `s3_object_version`s) are PRE-EXISTING
DRIFT shown by the survey's negative control (row Z-S21). A targeted apply that lists any of them is NOT SIGNED. The
module's outputs are untouched; nothing outside `smartx-pipeline/` moves.

## Both branches of every outcome named

- **The targeted plan reads `1 to import, 0 to add, 1 to change, 0 to destroy`, and the one change is `tags_all` on
  `aws_iam_role.opal_smartx_lambda_role` adding exactly the four keys:** SIGNED. **Any other address, any destroy, any
  change to `assume_role_policy`, `inline_policy`, `managed_policy_arns`, or a fifth tag:** NOT SIGNED; the act stops and
  files a row. Another open `.open_deploys/` entry on `smartx-pipeline` before step 4 also means NOT SIGNED.
- **After the apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`** and list-role-tags shows exactly the
  four keys: Branch A, done. **Anything else:** Branch B; the rollback above runs, and the finding is a row.

## Authorization, named (the KEY COLLISION)

`Project` and `System` are both default_tags keys and authorization keys in this account (safe-apply's KEY COLLISION
line). The survey's sweep of `get-account-authorization-details` (298 roles, 78 policies, 9 users, 2 groups; no SCPs)
reads **0 `aws:PrincipalTag/*` conditions account-wide**. The only two tag conditions are `ResourceTag` on EC2/SSM
resources, requiring `NFRA_WEBSITE` and `CottonwoodPipeline`. So these four tags on this role can neither widen nor narrow
any decision. This half relies on that sweep, and the CTO half is asked to re-read it.

## Provenance

ROUND_ANALYSIS.round5.md @`f77e32d7c3` E1; DECOMP_R6 @`c838c9347a`; A1-r6 @`2b2091822f`; A2-r6 @`3293b97a90`; survey
@`4dff2b348a`. Push state: LOCAL.
