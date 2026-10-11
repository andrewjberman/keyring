# NEVER-WIDEN co-sign, ROUND 6 -- the CTO half: adopt rows 1 and 2 (Family A, Black Diamond) into `bd-pipeline` (IAM-w-2 PHASE B)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-10 ~23:5xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33093 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND6_W-2_COO_HALF.md` @1ad6f36ca2 | **Act:** `NFRA_IAMROLES202609.TO-IAM-w-2` PHASE B by
`0.7.0_AE_CloudOps~IR`, `safe-apply -target` on the two roles only, in the A4-r6/A5-r6 order.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written. Nothing in this half widens
that set.

## This seat's own reads (2026-10-10 ~23:4xZ-23:5xZ)

| read | result |
|---|---|
| provider `default_tags`, `bd-pipeline/main.tf:29-36` | FOUR keys: `Project=OpalPortal`, `ManagedBy=Terraform`, `Environment=Production`, `System=BDPipeline`. These match the COO half. |
| live `list-role-tags`, both roles | `[]` on both |
| live trust vs `zz_adopt_family_a.tf.proposed` | row 1: one Allow, `lambda.amazonaws.com`, `sts:AssumeRole`, no Condition. Row 2: one Allow, `ecs-tasks.amazonaws.com`, `sts:AssumeRole`, no Condition. **Both equal their declaration statement for statement.** |
| live description, path, max session vs the declaration | row 1 has description "Role for BD Merge Daily Lambda", and the declaration carries it verbatim (`:66`). Row 2 has none, and the declaration omits it. Both have path `/`, max session 3600 and no permissions boundary. |
| live policies | row 1: inline `bd-merge-daily-policy` (S3 `opal-data-bd`, logs). Row 2: inline `BDPipelineTaskPolicy` (S3 `opal-data-bd` and `opal-data-portal-v2`, logs, `sns:Publish` on the account's topics). 0 managed on either. The declaration omits `inline_policy` and `managed_policy_arns`. |
| account authorization sweep (`get-account-authorization-details`, read ~23:3xZ for w-3's half, same session) | 301 roles, 78 policies, 9 users, 2 groups, 949 documents. **0 `aws:PrincipalTag`.** The only non-service tag conditions are `aws:ResourceTag` on EC2/SSM (`CottonwoodPipeline`, `NFRA_WEBSITE`). Neither reaches an IAM role, and neither matches `OpalPortal` or `BDPipeline`. |
| resource policies on everything the roles reach | `opal-data-bd` bucket policy: 0 `PrincipalTag`. `opal-data-portal-v2` bucket policy: 0 tag conditions (read for w-3). SNS: 17 topics, 0 errors, **0 `PrincipalTag`**. CloudWatch Logs resource policies: 0 `PrincipalTag`. |

**Conclusion:** the four tags can neither widen nor narrow any authorization decision, on the identity plane or the
resource plane. The COO half's KEY COLLISION reading holds.

## Conditions

None of its own beyond the COO half's:
- the targeted plan is 2 import / 0 add / 2 change / 0 destroy;
- each change is `tags_all` with exactly the four keys;
- no other address is listed, including the 7 managed instances and `cot-exporter`;
- the re-plan reads 0/0/0;
- the live post-checks hold (row 2's trust, one inline policy each);
- the untargeted shared-tree plan reads `0 to destroy` after the drain.

Rollback is as the COO half states.

**Amended 2026-10-11 ~00:4xZ (`1.0.0_SA_CTO~Z`, on A7-r6 @7c213215bd):** the sentence "w-2 lands before w-3, per the w-3
halves" is struck. The order is the issuer's, not a condition here. w-2 is HELD on the RESERVED R20 call
`sitez-20261011T003538Z-5bdf` (row Z-S34): this half signs the act's blast radius, and the act still cannot commit its
declaration until Andrew acknowledges the exception.

**Amended 2026-10-11 ~02:5xZ:** the R20 ask is WITHDRAWN
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IAMROLES_W2_R20_WITHDRAWN_20261011_Z.md`). w-2 is now HELD on
LGIC_ENFORCE FWD-8 at dell1, under which adopted live names read EXISTING. The blast radius and branches of this half
are unchanged.

**Amended 2026-10-11 ~03:3xZ:** Andrew's yes (~03:2xZ, *"Yes we can make the exception for now."*) supersedes that
withdrawal. The R20 record is @727ce5eefa and the gate entries `NFRA-IAMROLES-R20-01/02` are @bd2cacee69 (register X17).
This seat dry-graded them as DECLARED-EXCEPTION on 4 of 4 sites. w-2 is no longer held on naming. The blast radius and
branches are unchanged.

-- 1.0.0_SA_CTO~Z
