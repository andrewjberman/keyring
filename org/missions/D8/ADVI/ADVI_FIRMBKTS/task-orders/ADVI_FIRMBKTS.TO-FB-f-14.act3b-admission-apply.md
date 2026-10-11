# ADVI_FIRMBKTS task order -- `FB-f-14` -- ACT 3b: THE READERS' ADMISSION APPLIED TO `opal-data-49financial` (ONE BUCKET POLICY, GENERATED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-14</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one bucket policy is put; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the actor's identity (user/cloudops-dell1-agent-user, group cloudops-dell-agents-group) carries `s3:PutBucketPolicy` and `s3:DeleteBucketPolicy` on `*` through `cloudops-dell-agent-respol-allow-policy` (read 2026-10-11 ~15:2xZ); `simulate-principal-policy` and `simulate-custom-policy` are denied to it, so the close simulation is the laptop lane's. The permitted set is ten principals, each Get on one object ARN or nine served prefixes; no Put, Delete, bucket-wide or `s3:*` row (`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_COO_HALF.md` and `..._CTO_HALF.md`, both SIGNED).
comp-adversary: RUN by the issuer -- before the act the live policy holds 4 statements and `r4_act3b.py --arms live` reads 2 of 3 (L2 and L3 PASS as controls; L1 FAILS: the rendered policy holds 29 statements, 25 of them not live). Blindness: an organization SCP is invisible to every instrument here; act 4's widened sample (every admitted principal, one real invocation) is where it is read.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS LIVE. READ THE PAIR FIRST.

Both halves of the never-widen pair read SIGNED at HEAD: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_COO_HALF.md` (COO,
@ac44d4a847) and `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_CTO_HALF.md` (CTO, msg 3932). The cells it rests on are merged and
graded: `FB-g-19` through `FB-g-23`. A seat that finds the pair changed since its read stops and reports.

## 1. THE ACT -- `FB-f-14` (round 4, act 3b; row D1-S27; CTO ADDENDA 8 to 11)

`aws_s3_bucket_policy.opal_data_49financial` in the shared-infra root is changed in place: its three hand-kept performance
adapter statements are replaced by the registry's generated Deny rows, and the module's generated Allow statements are
appended. Nothing else changes. The act is INERT: nobody reads the canonical home until the flip (act 4).

1. **Open the change-management entry** (`python .tools/deploy_ledger.py open ...`, slug
   `advi-firmbkts-fb-f-14-act3b-admission-<UTCdate>`) BEFORE the first write: scope the `shared-infra` root, ONE resource
   (`aws_s3_bucket_policy.opal_data_49financial`), rollback = the prior policy put back verbatim (step 2).
2. **Print the prior policy** to `D/PRIOR_opal-data-49financial_policy_<UTC>.json` (`aws s3api get-bucket-policy --bucket
   opal-data-49financial --query Policy --output text`), `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1`; it must read 4 statements. Commit it with the entry.
3. **Plan, scoped.** In `infra/aws/terraform/shared-infra`, with the saved-plan discipline the earlier acts used: `.tools/safe-apply.sh`'s plan limb with
   `-target=aws_s3_bucket_policy.opal_data_49financial`. The plan must show exactly ONE resource to change, in place, and
   `Plan: 0 to add, 1 to change, 0 to destroy`. Print the policy diff (the `~ policy` hunk). A plan naming any other resource, a
   destroy, or an add is a STOP: file a BLOCKING row and leave this order open. A root that cannot plan scoped is a BLOCKING row.
4. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan.
5. **Read after.** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act3b.py --arms live` must read 3 of 3. A post-apply scoped plan must read `No changes`.
6. Close the entry with the outputs below.

## 2. BOUNDS

1. One resource, one bucket policy. No IAM change, no other bucket, no trust change, no registry or module edit.
2. No apply if either half of the pair is not SIGNED at its current bytes, or if the plan names a second resource.
3. If `s3:PutBucketPolicy` is refused to this identity, STOP, file a BLOCKING row and name the laptop lane
   (`0.7.0_AE_CloudOps~FBL`) as the holder of the apply; do not widen anything to make the call pass.
4. If the post-apply read differs from the plan, put the prior policy back the same hour (step 2's file), close the entry
   ROLLED-BACK, file a BLOCKING row. The registry rows stay as the record of what was asked.
5. Keys carry client ids: your report names counts, never an id.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-14.act3b-admission-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-14"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act3b.py --arms live; echo "exit=$?"</invocation><expect>ROUND 4 ACT 3B LIVE: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-14"><invocation>cd /c/dev/ajb_workspace/infra/aws/terraform/shared-infra &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=aws_s3_bucket_policy.opal_data_49financial 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
</proof_of_spec>

AC1 reads the live policy against the policy the registry renders (29 statements: the blanket Deny, 17 scoped Denies, 11
Allows), that no Allow writes, deletes or names the whole bucket, and that an unsigned GET of the ownership key is refused.
AC2 reads that the scoped plan is empty after the apply. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance and the prior policy file; flip `<status>` to
`complete` only when AC1 and AC2 pass. Report once to `2.0.0_SA_COO~B1`: the plan's one-resource summary line, the entry id,
AC1 and AC2 outputs, the number of statements before and after, and the commit hash. The close simulation (ten principals on
the ownership key, run by the laptop lane) is the issuer's act and is not yours.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut after the CTO signed the act 3b half (msg 3932) and `FB-g-19` to `FB-g-23` merged. The close
instrument is `iam:SimulatePrincipalPolicy` with the live bucket policy as `ResourcePolicy`, run by `0.7.0_AE_CloudOps~FBL`
(one call per principal on KEY; the negative arm is the QA-fabric role `inf-gold-qa-runner-ec2-role` by evaluation and an
unsigned GET for the one real 403: this fabric's QA runner shares the admitted `bd-exporter-ec2-role`, so it is not a
negative arm; see the COO half's ADDENDUM 1). Act 4's CTO half ADDENDUM 2 widens its sample to every admitted principal.

<status>pending</status>
<round>4</round>
<workstream>ACT3B</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-14</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
