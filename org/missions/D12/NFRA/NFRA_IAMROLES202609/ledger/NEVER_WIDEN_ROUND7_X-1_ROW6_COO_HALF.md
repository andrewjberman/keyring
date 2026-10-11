# NEVER-WIDEN co-sign, ROUND 7 -- the COO half: adopt row 6 `lambda-ec2-runtime-monitor-role` into `shared-infra` (IAM-x-1 PHASE B, module 1 of 2)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~09:1xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-x-1` PHASE B for
`infra/aws/terraform/shared-infra/` only, by `0.7.0_AE_CloudOps~IR`, `-target`-scoped, in the A4-r6 order | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round7/PLAN_SURVEY_family_c.md` section 4a (the re-survey after ADVI_COTBKF's fix
@`8c6fc7652a`), with `shared-infra/zz_adopt_family_c_row6.tf.proposed` @`a921f7130f`; the CTO's XB-0989 reading (msg
33237) | **The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND7_X-1_ROW6_CTO_HALF.md`. Row 14 has its own pair
(`NEVER_WIDEN_ROUND7_X-1_*`), already landed.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `shared-infra/tfstate` | `aws_iam_role.lambda_ec2_runtime_monitor_role` IMPORTED (state only; the role exists since 2026-02-06) | the targeted plan, then `terraform state list` | `terraform state rm aws_iam_role.lambda_ec2_runtime_monitor_role` plus reverting the `.tf` |
| the live role `lambda-ec2-runtime-monitor-role` | `tags_all` gains EXACTLY FOUR keys on a role carrying zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=SharedInfra` | `list-role-tags` before (`[]`) and after (those four) | `aws iam untag-role --tag-keys Environment ManagedBy Project System` after the state rm |
| `shared-infra/zz_adopt_family_c_row6.tf.proposed` -> `.tf` | the declaration made live | git | git revert |
| deploy ledger `iamroles-r7-family-c-shared-infra` | opened first, closed last | AC3 (the Status line reads CLOSED) | none needed |

## Writers of the named property, counted

The property is the role's tag set. Survey section 7: **0 declarations** of the role under `infra/aws/terraform` at the
cut. So it has **0 live writers today and exactly 1 after PHASE B**, `shared-infra`'s provider `default_tags`. Its inline
`EC2RuntimeMonitorPolicy` and attached `AWSLambdaBasicExecutionRole` are not written: the declaration omits
`inline_policy`, `managed_policy_arns` and `description`.

## What the act may NOT touch

The role's policies, trust (`lambda.amazonaws.com`; the role is IN USE, last assumed this morning), path, description
(none) and max session. **`aws_iam_role.restricted_breakglass` and `aws_iam_role_policy.restricted_breakglass`**, the
negative control's `2 to add`, are ADVI_COTBKF's declared, never-applied pair (CTO msg 33237). A targeted plan listing
either is NOT SIGNED, and an untargeted apply is NOT SIGNED: it would CREATE an IAM role and policy. Every other address in
`shared-infra`, including the firm-bucket policies, is outside the set.

## Both branches of every outcome named

- **The targeted plan reads `1 to import, 0 to add, 1 to change, 0 to destroy`, and its one change is `tags_all` on
  `aws_iam_role.lambda_ec2_runtime_monitor_role` adding exactly the four keys:** SIGNED. **Any other address (the
  breakglass pair above all), any destroy, any change to `assume_role_policy`, `inline_policy`, `managed_policy_arns` or
  `description`, or a fifth key:** NOT SIGNED. The act stops and files a row.
- **After the apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`; LIVE, the role carries exactly the
  four keys, its trust is still `lambda.amazonaws.com`, it has one inline policy and one attachment
  (`AWSLambdaBasicExecutionRole`):** Branch A, done. **Anything else:** Branch B. The rollback runs, and the finding is a
  row. After the drain, the untargeted shared-tree plan must read 0 to destroy, and its `2 to add` (the breakglass pair)
  is recorded unchanged beside it.

## Naming

Survey section 6: `NAMING NO-SYSTEM-ASKED`. The canonical form equals the live name, so no override or registry row is
owed. Grade the `.tf` form with `--no-renames` (the rename-blind and `.tf.proposed`-blind dry-grades this round found).

## Authorization, named (the KEY COLLISION)

`Project` and `System` are default_tags keys and authorization keys. The account sweep re-read today (CTO, w-3 and x-1 row
14 halves) holds **0 `aws:PrincipalTag/*` conditions**. `System=SharedInfra` matches neither `aws:ResourceTag` value
(`CottonwoodPipeline`, `NFRA_WEBSITE`), and neither condition reaches an IAM role. So these tags neither widen nor narrow
any decision.

## Provenance

ROUND_ANALYSIS.round6.md @`2f49aa235b` E1; DECOMP_R7 @`8b61ddf94f`; A1-r7 @`af187b410b`; ADVI_COTBKF fix @`8c6fc7652a`;
survey section 4a. Push state: LOCAL.
