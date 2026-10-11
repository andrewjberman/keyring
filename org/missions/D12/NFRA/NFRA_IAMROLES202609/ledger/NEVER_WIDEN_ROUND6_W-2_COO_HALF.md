# NEVER-WIDEN co-sign, ROUND 6 -- the COO half: adopt rows 1 and 2 (Family A, Black Diamond) into `bd-pipeline` (IAM-w-2 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-10 ~23:5xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-w-2` PHASE B, by
`0.7.0_AE_CloudOps~IR` through `safe-apply` in `infra/aws/terraform/bd-pipeline/`, `-target`-scoped to TWO addresses
(A2-r6), in the order of acts A4-r6 / A5-r6 fix (commit the renamed `.tf` first, then import, then drain the same
session) | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round6/PLAN_SURVEY_family_a.md` @`a1667d4af4` (drained
@`df0248d4f6`), `zz_adopt_family_a.tf.proposed` @`d27dec64c2`, and step 1a's guard @`a18b96fd5d` | **The other half:**
`1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND6_W-2_CTO_HALF.md`. No PHASE B GO until both halves are files.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| Terraform state `bd-pipeline/tfstate` | `aws_iam_role.bd_merge_daily_lambda_role` and `aws_iam_role.bd_pipeline_task_role` IMPORTED (state only; both roles exist, created 2026-01-15 and 2026-01-29) | the targeted plan, then `terraform state list` | `terraform state rm` of each address (state only) plus reverting the `.tf` rename |
| live role `bd-merge-daily-lambda-role` (row 1) | `tags_all` gains EXACTLY FOUR keys on a role carrying zero: `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=BDPipeline` | `aws iam list-role-tags` before (`[]`) and after (those four) | `aws iam untag-role --tag-keys Environment ManagedBy Project System` after the state rm |
| live role `bd-pipeline-task-role` (row 2) | the same four keys, the same values | the same | the same |
| `bd-pipeline/zz_adopt_family_a.tf.proposed` -> `.tf` | the rename that makes the declaration live | git | git revert |
| deploy ledger `iamroles-r6-family-a` | opened first, closed last | AC3 | none needed |

Step 1a's one-clause guard on `bd-served-vintage-alarm.tf` is already landed (@`a18b96fd5d`) and moves nothing in AWS. The
shared-tree plan reads "No changes" with it in place. It is NOT part of this act's blast radius.

## Writers of the named property, counted

The property is each role's tag set. Survey section 7: **0 declarations of either role across 833 files** under
`infra/aws/terraform` at the cut (70 binary and 9 ephemeral-floor files not searched, stated). So each role has **0 live
writers today and exactly 1 after PHASE B**, the module's provider `default_tags`, read from its provider block. That is
1 rule for 2 roles. Neither role's inline policy (`bd-merge-daily-policy`; `BDPipelineTaskPolicy`) is a property this act
writes: the declaration omits `inline_policy` and `managed_policy_arns` (AC1 grep reads 0), and the plan shows both
unchanged on both roles.

## What the act may NOT touch

Each role's policies, trust, path, description (row 2 has none) and max session; any other address in the module. The
plan holds **205 resource_changes, exactly 2 non-no-op, both the adopted roles**, and the negative control reads "No
changes", so there is zero pre-existing drift. A targeted apply listing any other address is NOT SIGNED. Any EC2 instance
is outside the set: the module's 7 managed instances do not include `i-0643a5bee8a8feabf` (`cot-exporter`), which
the survey measured with a positive control. The tag advisory on that instance is therefore not this act's. The
pre-existing `fmt -check` failures are NOT touched.

## Both branches of every outcome named

- **The targeted plan reads `2 to import, 0 to add, 2 to change, 0 to destroy`, and its two changes are `tags_all` on the
  two adopted roles, each adding exactly the four keys above:** SIGNED. **Any other address, any destroy, any change to
  `assume_role_policy`, `inline_policy`, `managed_policy_arns` or `description`, or a fifth key:** NOT SIGNED. The act
  stops and files a row. An open `.open_deploys/` entry on `bd-pipeline` before step 4 also means NOT SIGNED.
- **After the apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`; LIVE, both roles carry exactly the
  four keys, row 2's trust principal is still `ecs-tasks.amazonaws.com` (`get-role`), and each role still has its one
  inline policy (`list-role-policies`):** Branch A, done. **Anything else:** Branch B. The rollback runs, and the
  finding is a row. After the drain, the untargeted shared-tree plan must read `0 to destroy` (A4-r6, row Z-S27).

## Authorization, named (the KEY COLLISION)

`Project` and `System` are both default_tags keys and authorization keys (comp-tagauthz, verbatim in the survey). The
sweep re-run for this survey: 301 roles, 78 policies, 9 users, 2 groups, no SCPs (not an Organization member). It reads
**0 `aws:PrincipalTag/*` conditions account-wide**. The only two non-service tag conditions are `aws:ResourceTag` on
EC2/SSM resources (`System=CottonwoodPipeline`, `Project=NFRA_WEBSITE`). Neither reaches an IAM role, and neither value
matches `OpalPortal` / `BDPipeline`. comp-tagauthz's GATE pass was over **0 candidates**, an empty denominator, and
this half does NOT rest on it. The CTO half is asked to re-read the sweep.

## Provenance

ROUND_ANALYSIS.round5.md @`f77e32d7c3` E2; DECOMP_R6 @`c838c9347a`; A2-r6 @`3293b97a90`; A3-r6 @`29f269fca3`;
A4-r6 @`7af7a24e9f`; A5-r6 @`f37fb5892d`; A6-r6 @`59d56f3848`; survey @`a1667d4af4`; Z-S29 disarmed by row Z-S33 on
f1r.AC1 / f1r.AC2 PASS re-run by this seat in the shared tree. Push state: LOCAL.
