# ADVI_FIRMBKTS task order -- `FB-f-17` -- ACT 3c: THE EXEC-SUMMARY GENERATOR'S FENCE ROW APPLIED (ONE BUCKET POLICY, GENERATED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-17</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one bucket policy is put; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the actor's identity put act 3b's policy on this bucket (`FB-f-14`, @0acccf7d8e: `s3:PutBucketPolicy` read through `cloudops-dell-agent-respol-allow-policy`). The permitted set is ONE principal: Get, List and Put exempt on one directory, with a read-only Get and List Allow (`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_COO_HALF.md` and `..._CTO_HALF.md`, both SIGNED, CTO msg 3974).
comp-adversary: RUN by the issuer -- before the act the live policy holds 29 statements and `r4_act3b.py --arms live` reads 2 of 3 (L1 FAILS: the registry now renders 34; L2 and L3 PASS as controls). Blindness: an organization SCP is invisible to every instrument here; act 4's widened sample (one real invocation per admitted principal, the exec-summary generator included) is where it is read.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS LIVE. READ THE PAIR FIRST.

Both halves of the act 3c pair read SIGNED at HEAD. The row it rests on is merged and graded: `FB-g-27` @deb92d1530
(`r4_exec.py` 4 of 4). A seat that finds the pair changed since its read stops and reports.

## 1. THE ACT -- `FB-f-17` (round 4, act 3c; the CTO's round-3 ADDENDA 10 and 11)

`aws_s3_bucket_policy.opal_data_49financial` in the shared-infra root is changed in place: one generated scoped row adds three
Deny statements and two Allow statements; the blanket Deny's exemption list gains one principal. Nothing else changes. INERT:
nobody reads or writes the generator's keys at the canonical home until act 4b.

1. **Open the change-management entry** (`python .tools/deploy_ledger.py open ...`, slug
   `advi-firmbkts-fb-f-17-act3c-execsum-fence-<UTCdate>`) BEFORE the first write: scope the `shared-infra` root, ONE resource
   (`aws_s3_bucket_policy.opal_data_49financial`), rollback = the prior policy put back verbatim (step 2).
2. **Print the prior policy** to `D/PRIOR_opal-data-49financial_policy_<UTC>.json` (`aws s3api get-bucket-policy --bucket
   opal-data-49financial --query Policy --output text`), `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1`; it must read 29 statements.
3. **Plan, scoped.** In `infra/aws/terraform/shared-infra`: `.tools/safe-apply.sh`'s plan limb with
   `-target=aws_s3_bucket_policy.opal_data_49financial`. The plan must show exactly ONE resource to change in place and
   `Plan: 0 to add, 1 to change, 0 to destroy`; print the policy diff (the `~ policy` hunk). Any other resource, an add or a
   destroy is a STOP: file a BLOCKING row and leave this order open.
4. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan.
5. **Read after.** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act3b.py --arms live` must read 3 of 3 (34 statements: 21 Deny, 13 Allow). A post-apply
   scoped plan must read `No changes`.
6. Close the entry with the outputs below.

## 2. BOUNDS

1. One resource, one bucket policy. No IAM change, no other bucket, no registry or module edit.
2. No apply if either half is not SIGNED at its current bytes, or if the plan names a second resource.
3. If `s3:PutBucketPolicy` is refused, STOP, file a BLOCKING row and name the laptop lane (`0.7.0_AE_CloudOps~FBL`) as the holder
   of the apply; do not widen anything to make the call pass.
4. If the post-apply read differs from the plan, put the prior policy back the same hour (step 2's file), close the entry
   ROLLED-BACK, file a BLOCKING row. The registry row stays as the record of what was asked.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-17.act3c-execsum-fence-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-17"><invocation>cd /c/dev/ajb_workspace &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act3b.py --arms live; echo "exit=$?"</invocation><expect>ROUND 4 ACT 3B LIVE: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-17"><invocation>cd /c/dev/ajb_workspace/infra/aws/terraform/shared-infra &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=aws_s3_bucket_policy.opal_data_49financial 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
</proof_of_spec>

AC1 reads the live policy against the policy the registry renders (34 statements), that no Allow writes, deletes or names the
whole bucket, and that an unsigned GET of the ownership key is refused. AC2 reads that the scoped plan is empty after the apply.
Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance and the prior policy file; flip `<status>` to
`complete` only when AC1 and AC2 pass. Report once to `2.0.0_SA_COO~B1`: the plan's one-resource summary line, the entry id, AC1
and AC2 outputs, the number of statements before and after, and the commit hash. The simulation for the generator role is the
issuer's act and is not yours.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** act 3c, signed with act 4b/4c (CTO msg 3974: 3c complete before 4b; 3b before 4c). The Put at the canonical home
is Allowed identity-side by `FB-f-18` (the exec-summary root); the fence exemption alone grants no write. The close simulation
(Get and List on a sample object allowed; Put allowed only after `FB-f-18`) is the laptop lane's, with the act 3b close.

<status>complete</status>
<round>4</round>
<workstream>ACT3C</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-17</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
