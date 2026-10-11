# ADVI_FIRMBKTS task order -- `FB-f-18` -- ACT 4b'S IDENTITY POLICY APPLIED: THE EXEC-SUMMARY GENERATOR'S NARROW PUT (ONE POLICY, `1 to add`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-18</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one inline IAM policy is created; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the policy grants `s3:PutObject` on `arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*/exec_summary.json` and nothing else (no PutObjectAcl, no Get, no Delete). The identity that applied act 0 and 0's addendum holds `iam:PutRolePolicy` on roles of this account through the same group policies; the exec-summary root's own plan reads are the actor's first measurement. Pair: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` (amended) and `..._CTO_HALF.md`, both SIGNED (CTO msg 3974).
comp-adversary: RUN by the issuer -- before the act the role holds ONE inline policy (`exec-summary-generator-policy`) and none names `advi-49f-exec-summary-canonical-put-policy` (AC1 and AC2 FAIL, AC3 reads a pending create); after, two policies and the Sid. Blindness: nothing proves the generator can PUT through the role until act 4b's first run after the move; the grant is read from the document. The bucket's fence exemption for this role is act 3c's (`FB-f-17`); the Put is allowed only when both have landed.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS LIVE. APPLY AFTER `FB-f-17` OR BEFORE, IT IS INERT EITHER WAY.

The policy is merged and graded: `FB-g-28` @ef5c7f45cb (`r4_execiam.py` 5 of 5). It grants a write at a home nobody writes until
act 4b. Order against `FB-f-17`: either; the CTO's condition is that BOTH are applied before 4b.

## 1. THE ACT -- `FB-f-18` (round 4, act 4b's identity side; the CTO's round-3 ADDENDUM 11)

1. **Open the change-management entry** (slug `advi-firmbkts-fb-f-18-exec-summary-canonical-put-<UTCdate>`) BEFORE the first
   write: scope the `exec-summary` root, ONE resource (`aws_iam_role_policy.exec_summary_canonical_put`), rollback =
   `aws iam delete-role-policy` of that one policy name.
2. **Print the role's inline policies before** (`aws iam list-role-policies --role-name exec-summary-generator-role`) into the
   entry; the name `advi-49f-exec-summary-canonical-put-policy` must be absent.
3. **Plan, scoped.** In `infra/aws/terraform/exec-summary`: `.tools/safe-apply.sh`'s plan limb with
   `-target=module.opal_name_exec_summary_canonical_put -target=aws_iam_role_policy.exec_summary_canonical_put`. The plan must
   show exactly ONE resource to add and `Plan: 1 to add, 0 to change, 0 to destroy`. Any other resource is a STOP: file a
   BLOCKING row and leave this order open. A root that cannot plan scoped is a BLOCKING row.
4. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan. Close the entry with the
   outputs below.

## 2. BOUNDS

1. One resource, one policy, one role. No other IAM change, no Lambda change, no S3 or bucket-policy change.
2. No apply if either half is not SIGNED at its current bytes, or if the plan names a second resource.
3. If `iam:PutRolePolicy` is refused, STOP and file a BLOCKING row naming the laptop lane (`0.7.0_AE_CloudOps~FBL`); do not
   widen anything to make the call pass.

## 3. SURFACES

<paths>
infra/aws/terraform/exec-summary/iam.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-f-18.exec-summary-canonical-put-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-18"><invocation>timeout 100 aws iam get-role-policy --role-name exec-summary-generator-role --policy-name advi-49f-exec-summary-canonical-put-policy --query "PolicyDocument.Statement[].[Sid,Action,Resource]" --output text</invocation><expect>ExecSummaryCanonicalPut\s+s3:PutObject\s+arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/\*/exec_summary\.json</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-18"><invocation>timeout 100 aws iam list-role-policies --role-name exec-summary-generator-role --query PolicyNames --output text</invocation><expect>advi-49f-exec-summary-canonical-put-policy\s+exec-summary-generator-policy|exec-summary-generator-policy\s+advi-49f-exec-summary-canonical-put-policy</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-18"><invocation>cd /c/dev/ajb_workspace/infra/aws/terraform/exec-summary &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=module.opal_name_exec_summary_canonical_put -target=aws_iam_role_policy.exec_summary_canonical_put 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
</proof_of_spec>

AC1 reads the new policy's one statement, one action and one resource. AC2 reads that the role holds exactly the legacy policy and
the new one. AC3 reads that the scoped plan is empty after the apply. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance; flip `<status>` to `complete` only when AC1 to AC3
pass. Report once to `2.0.0_SA_COO~B1`: the plan's one-resource summary line, the entry id, AC1 to AC3 outputs, and the commit
hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** act 4b's identity side (the CTO's ADDENDUM 11 standing rule: a write lives identity-side in the writer's root).
The legacy policy keeps its own `PutObjectAcl` on the pipeline bucket (the CTO's condition 1 binds the new home only). The role
is not otherwise changed.

<status>pending</status>
<round>4</round>
<workstream>ACT4BIAM</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-18</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
