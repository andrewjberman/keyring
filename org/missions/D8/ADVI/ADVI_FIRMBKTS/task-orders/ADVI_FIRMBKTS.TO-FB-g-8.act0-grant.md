# ADVI_FIRMBKTS task order -- `FB-g-8` -- ACT 0: THE PRODUCERS' ROLE GRANT APPLIED (STAGED; FB-g-2'S POLICY, ITS OWN PAIR)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one IAM role policy is created; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the actor at the act -- `simulate-principal-policy` is denied to this identity for the role (row D1-S18's second gap), so the read is the live policy document and the scoped plan, printed into the change-management entry; the act's own PutRolePolicy is read against the actor's identity before the first write. The grant is least-privilege to one prefix (Put, Get, scoped List; no Delete).
comp-adversary: RUN by the issuer -- before the act the live role holds 16 inline policies and none names `advi-49f-platinum-canonical-rw` (AC1 and AC2 FAIL, AC3 reads a pending create); after, 17 and the two Sids. Blindness: nothing proves the producers can PUT through the role until the first canonical-mode run; the grant's effect is read from the document, not from a request.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED -- DO NOT START

Status `parked`. The issuer un-parks it (`parked` to `pending`, and to this seat) ONLY when ALL of these hold, each read by
the issuer at the time: (a) `FB-g-2` is merged to the dell1 branch and its AC1 reads 4 of 4; (b) the never-widen pair
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT0_GRANT_COO_HALF.md` and `..._CTO_HALF.md` both read SIGNED at the current bytes; (c) the
change-management entry for this act is open (step 1). A seat that finds this order `pending` has had it un-parked: read
the pair first.

## 1. THE ACT -- `FB-g-8` (round 4, the window's act 0; row D1-S18)

The gold producers' role `bd-exporter-ec2-role` (Terraform `aws_iam_role.bd_exporter`, root
`infra/aws/terraform/bd-pipeline`) must be allowed to put, get and list the canonical home of the served platinum before
act 2 (FB-f-9 phase B) moves the producers' mode. `FB-g-2` drafted the grant as one additive policy,
`aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical` (name `advi-49f-platinum-canonical-rw`, in `infra/aws/terraform/bd-pipeline/iam.tf`).

1. **Open the change-management entry** (`python .tools/deploy_ledger.py open ...`, slug `advi-firmbkts-fb-g-8-act0-grant-<UTCdate>`)
   BEFORE the first write: scope `bd-pipeline` root, one resource, rollback = `aws iam delete-role-policy` of that one
   policy name (nothing else changes; the QA runner shares the role, so the entry names it as a recipient of the Allow).
2. **Plan, scoped.** In the root, with the saved-plan discipline the earlier acts used: `.tools/safe-apply.sh`'s plan limb
   with `-target=aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical`. The plan must show exactly ONE resource
   to add and nothing else. A plan naming any other resource is a STOP: file a BLOCKING row and leave this order open.
3. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan. Close the entry with the
   three outputs below.

## 2. BOUNDS

1. One resource, one policy name, one role. No other IAM change, no S3 or bucket-policy change, no trust change.
2. No apply if the pair is not SIGNED at the current bytes; no apply of a plan naming a second resource.
3. If the identity cannot `iam:PutRolePolicy` on the role, STOP and file a BLOCKING row naming the laptop lane
   (`0.7.0_AE_CloudOps~FBL`) as the holder of the grant act; do not widen anything to make the call pass.

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
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-g-8.act0-grant.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-8"><invocation>timeout 100 aws iam get-role-policy --role-name bd-exporter-ec2-role --policy-name advi-49f-platinum-canonical-rw --query "PolicyDocument.Statement[].Sid" --output text</invocation><expect>AdviPlatinumCanonicalObjects\s+AdviPlatinumCanonicalList</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-8"><invocation>timeout 100 aws iam list-role-policies --role-name bd-exporter-ec2-role --query PolicyNames --output text | tr '\t' '\n' | wc -l</invocation><expect>^\s*17\s*$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-8"><invocation>cd /c/dev/ajb_workspace/infra/aws/terraform/bd-pipeline &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical 2&gt;&amp;1 | tail -n 6</invocation><expect>No changes</expect></criterion>
</proof_of_spec>

AC1 reads the live policy's two statements, AC2 reads that the role now holds 17 inline policies (16 before: the
count is a client-side count of the unpaginated list, not a page count), AC3 reads that the scoped plan is now empty.
Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance; flip `<status>` to `complete` only when AC1 to
AC3 pass. Report once to `2.0.0_SA_COO~B1`: the plan's one-resource summary, AC1 to AC3 outputs, the entry id, and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** staged by the CTO's round-3 analysis (section 3 item 1: "the producers' role grant (D1-S18), its own
pair"). The window's order is act 0 (this), act 2 (FB-f-9 phase B), act 3 (FB-f-10), act 4 (FB-f-11), acts 4b and 4c
(FB-f-13): those four orders stay parked as cut in round 3 and are re-homed to round 4 by amendment at their un-park. Act
4's un-park also waits on row D1-S21 (the asset-dim pin) and on the dormant readers of this round being merged.

<status>parked</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-8</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
