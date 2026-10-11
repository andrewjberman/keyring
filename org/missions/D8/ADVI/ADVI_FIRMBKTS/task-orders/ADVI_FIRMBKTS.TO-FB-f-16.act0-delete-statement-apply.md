# ADVI_FIRMBKTS task order -- `FB-f-16` -- ACT 0 ADDENDUM: THE NARROW DELETE STATEMENT APPLIED (ONE POLICY, `1 to change`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-16</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one IAM role policy changes in place; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the policy is the one act 0 created (`FB-g-8`, applied @f942dcb9a8); this adds one statement, `AdviPlatinumCanonicalDelete`, `s3:DeleteObject` on two directories printed from the code (`D_04:789-812`, `D_02:3245-3284`) and generated through `class_prefix`. The identity that applied act 0 holds `iam:PutRolePolicy` on the role (the same call). Pair: `NEVER_WIDEN_ROUND4_ACT0_GRANT_COO_HALF.md` ADDENDUM 1 and `NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md` ADDENDUM 1, both SIGNED (CTO msg 3959).
comp-adversary: RUN by the issuer -- before the act the live policy holds 2 statements (`r4_delgrant.py` reads the file, 5 of 5 at HEAD; AC1 and AC2 FAIL by construction: they read a third statement that does not exist yet). Blindness: nothing proves a producer can DELETE through the role until the first canonical chain run with a departed advisor; the grant's effect is read from the document.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS LIVE. READ THE PAIR FIRST.

Both halves read SIGNED at HEAD (the COO half's ADDENDUM 1 @bda6f4ebc4, the CTO half's ADDENDUM 1; CTO msg 3959). The statement
is merged and graded: `FB-g-25` @555ba2e0f5 (`r4_delgrant.py` 5 of 5). The act must land BEFORE act 2 (CTO ruling).

## 1. THE ACT -- `FB-f-16` (round 4, act 0's addendum; row D1-S29)

The producers' role `bd-exporter-ec2-role` gains one statement on the policy `advi-49f-platinum-canonical-rw-policy`
(Terraform `aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical`, root `infra/aws/terraform/bd-pipeline`).

1. **Open the change-management entry** (`python .tools/deploy_ledger.py open ...`, slug
   `advi-firmbkts-fb-f-16-act0-delete-statement-<UTCdate>`) BEFORE the first write: scope the `bd-pipeline` root, ONE resource,
   rollback = the prior two-statement document put back (step 2's file).
2. **Print the prior policy** to `D/PRIOR_advi-49f-platinum-canonical-rw-policy_<UTC>.json` (`aws iam get-role-policy`), `D` =
   `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1`; it must read two statements.
3. **Plan, scoped.** In the root, with the saved-plan discipline act 0 used: `.tools/safe-apply.sh`'s plan limb with
   `-target=module.opal_name_platinum_grant -target=aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical`. The plan must
   show exactly ONE resource to change in place and `Plan: 0 to add, 1 to change, 0 to destroy`. Any other resource, an add or a
   destroy is a STOP: file a BLOCKING row and leave this order open.
4. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan. Close the entry with the
   outputs below.

## 2. BOUNDS

1. One resource, one policy, one role. No other IAM change, no S3 or bucket-policy change, no trust change.
2. No apply if either half is not SIGNED at its current bytes, or if the plan names a second resource.
3. If `iam:PutRolePolicy` is refused, STOP and file a BLOCKING row naming the laptop lane (`0.7.0_AE_CloudOps~FBL`); do not
   widen anything to make the call pass.
4. If the post-apply read differs from the plan, put the prior document back the same hour (step 2's file), close the entry
   ROLLED-BACK, file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/terraform/bd-pipeline/iam.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-16.act0-delete-statement-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-16"><invocation>timeout 100 aws iam get-role-policy --role-name bd-exporter-ec2-role --policy-name advi-49f-platinum-canonical-rw-policy --query "PolicyDocument.Statement[].Sid" --output text</invocation><expect>AdviPlatinumCanonicalObjects\s+AdviPlatinumCanonicalList\s+AdviPlatinumCanonicalDelete</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-16"><invocation>timeout 100 aws iam get-role-policy --role-name bd-exporter-ec2-role --policy-name advi-49f-platinum-canonical-rw-policy --query "PolicyDocument.Statement[2].[Action,Resource]" --output text</invocation><expect>s3:DeleteObject\s+arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/\*\s+arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/entities/advisors/\*</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-16"><invocation>cd /c/dev/ajb_workspace/infra/aws/terraform/bd-pipeline &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=module.opal_name_platinum_grant -target=aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
</proof_of_spec>

AC1 reads the live policy's three Sids. AC2 reads the third statement's one action and its two resources, and no other. AC3
reads that the scoped plan is empty after the apply. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance and the prior-policy file; flip `<status>` to
`complete` only when AC1 to AC3 pass. Report once to `2.0.0_SA_COO~B1`: the plan's one-resource summary line, the entry id, AC1 to
AC3 outputs, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the act-0 addendum's apply, ruled by the CTO (msg 3931) and signed (msg 3959). It must land before act 2 (and
before the window: it is inert until a producer deletes at the canonical home). Row `ADVI_FIRMBKTS-D1-S29`. The QA runner shares the
role and receives the same Allow (stated in the COO addendum); `FB-g-15`'s guard keeps QA off canonical.

<status>pending</status>
<round>4</round>
<workstream>DELGRANTAPPLY</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-16</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
