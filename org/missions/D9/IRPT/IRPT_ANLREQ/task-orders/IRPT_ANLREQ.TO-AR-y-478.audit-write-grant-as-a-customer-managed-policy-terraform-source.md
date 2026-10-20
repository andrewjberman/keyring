# TO IRPT_ANLREQ.TO-AR-y-478.audit-write-grant-as-a-customer-managed-policy-terraform-source -- TERRAFORM SOURCE ONLY: move the audit-write grant out of the resident role's inline policy (which has 109 bytes of headroom) into ONE new customer-managed policy attached to the role; the inline policy returns to its applied form; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-478.audit-write-grant-as-a-customer-managed-policy-terraform-source</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~349</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ137</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-478` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** IB2's stop (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_auditgrant/A_AFTER_AUDITGRANT.txt`: PutRolePolicy 409 LimitExceeded, the role's inline policies total 10131 of 10240 bytes, the planned resident policy is 522 bytes larger), CTO msg 11566 (one customer-managed policy attached to `irpt-ycharts-runner-role`, same statement and same resources), AR-y-468's edit (trunk `2ff88544d1d`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~349`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-349` (branch `wk-IRPT_ANLREQ-349`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~349 <0.9.0_WK_IRPT_ANLREQ~349@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W349-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the selftest below) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR478-y-AC1,AR478-y-AC2,AR478-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-478`, inlined)

*The measured stop.* The audit grant of AR-y-468 adds a Put-only statement and three KMS-context entries to the resident role's inline policy `irpt-ycharts-runner-resident-policy` (`aws_iam_role_policy.runner_resident`, `infra/aws/terraform/investor-reporting/ycharts/resident.tf`). IB2's apply failed at `PutRolePolicy`: IAM caps all inline policies of one role at 10240 bytes together and the role is at 10131 (its five inline policies: export-render-host-evidence 1073, parameter-fence 305, token 231, irpt-ycharts-runner 2053, the resident policy 6469), so the planned 6991-byte resident policy does not fit. Nothing was applied; the live inline policy is unchanged. IB2 also found that the KMS action for the audit key's context simulates ALLOWED at baseline through the role's OTHER inline policies; the KMS statement below stays (the CTO's ruling: "and its KMS entries"), as a separate statement of the new policy.

*The change.* (1) In `infra/aws/terraform/investor-reporting/ycharts/resident.tf`: remove from the inline policy exactly what AR-y-468 added to it: the statement `WriteTheAnalysisAudit` and the fourth argument `local.resident_audit_write_prefixes` of the `concat(...)` in the `ReportEncryptionViaS3ForResidentFamiliesOnly` statement (restore that line to its applied text, the one at commit `680818fdb3e`). KEEP the `locals` definition `resident_audit_write_prefixes` (the new file reuses it). After your edit `git diff 680818fdb3e <your edit commit> -- infra/aws/terraform/investor-reporting/ycharts/resident.tf` shows ONLY additions (the local and its comment) and no deletion: the inline policy document is byte-for-byte what is applied now. (2) New file `infra/aws/terraform/investor-reporting/ycharts/resident_audit_policy.tf`, additions only: one `aws_iam_policy` (name from the `modules/opal_name` module the way `module.ycdgen_research_policy_name` is built in `resident.tf`: read `infra/aws/terraform/modules/opal_name` for the valid `system`, `scope`, `function` and `kind` values; function `audit-write`, kind `policy`; use the scope the module accepts for the product (`irpt`) if it accepts one, else say so in a surprise row and use the narrowest accepted) whose `policy` is a `jsonencode` of version `2012-10-17` and exactly TWO statements: `Sid = "WriteTheAnalysisAudit"`, Allow, `Action = ["s3:PutObject"]` only, `Resource = local.resident_audit_write_prefixes`; and `Sid = "AuditEncryptionViaS3ForAuditPrefixesOnly"`, Allow, `Action = ["kms:Decrypt", "kms:GenerateDataKey"]`, `Resource = [data.terraform_remote_state.core.outputs.kms_key_arn]`, `Condition = { StringEquals = { "kms:ViaService" = "s3.${var.aws_region}.amazonaws.com" }, StringLike = { "kms:EncryptionContext:aws:s3:arn" = local.resident_audit_write_prefixes } }` (the same form as the existing KMS statement, narrowed to the audit prefixes); and one `aws_iam_role_policy_attachment` of it to `aws_iam_role.runner`. Comments in the file's style cite the stop, CTO msg 11566, and that the inline cap is why. NO typed bucket, firm, tier, table or ARN literal. The new policy's compact JSON must be under 6144 bytes (state its size in a comment). (3) No other file changes.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/`: `check_audit_managed_policy.py` (stdlib only, ruff clean, offline) reads the two .tf files and asserts by regex: `resident.tf` no longer contains the statement `WriteTheAnalysisAudit` or the audit argument in the KMS line, still defines `resident_audit_write_prefixes`, and its KMS line equals the line at `680818fdb3e`; the new file declares exactly one `aws_iam_policy`, exactly one `aws_iam_role_policy_attachment` to the runner role, exactly the two statements above (Put-only action list; the KMS statement's condition list is `local.resident_audit_write_prefixes`), no `arn:aws:s3:::opal` literal; it evaluates the prefixes in Python from the registries and compares each, firm by firm, with `reporting_destination(firm, 'ANALYSIS_AUDIT', ART_SAMPLE, SHA_SAMPLE, policy_revision='irpt-anlreq-x10-v1')` (load `lib/opal_naming.py` BY PATH): bucket `opal-data-irpt`; and it estimates the compact JSON size of the policy document from the evaluated statements and requires it under 6144; it prints `AUDIT-MANAGED-OK firms=<n> prefixes=<n> builder_equal=yes put_only=yes inline_restored=yes size=<bytes>` or `AUDIT-MANAGED-BAD <why>` (rc 1). `--selftest` mutates the text in memory three ways (the Put action list given `s3:GetObject`; the inline KMS line given the audit argument again; the attachment removed) and prints `CONTROL-FIRES` only when ALL THREE read BAD. `check_audit_managed_bound.py` prints `AUDIT-MANAGED-BOUND-OK resident_tf=<n>/0 new_files=1 others=0` when, between `680818fdb3e` and your last Terraform edit commit, `resident.tf` has additions only (deletions 0), exactly one new file under `infra/aws/terraform/investor-reporting/ycharts/` (`resident_audit_policy.tf`) is added, and no other file under `infra/` changed in your own commits (trunk-side changes merged in are in the base: compare against the trunk commit you merged, as AR-y-468's AMENDMENT 2 did). Commit order: the Terraform edits (both files) as ONE commit first, message citing AR-y-478; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR478-y-AC1" cell_refs="AR-y-478"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/check_audit_managed_policy.py</invocation><expect>^AUDIT-MANAGED-OK firms=[0-9]+ prefixes=[0-9]+ builder_equal=yes put_only=yes inline_restored=yes size=[0-9]+$</expect></criterion>
<criterion id="AR478-y-AC2" cell_refs="AR-y-478"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/check_audit_managed_policy.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR478-y-AC3" cell_refs="AR-y-478"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/check_audit_managed_bound.py</invocation><expect>^AUDIT-MANAGED-BOUND-OK resident_tf=[0-9]+/0 new_files=1 others=0$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/IRPT_ANLREQ.TO-AR-y-478.audit-write-grant-as-a-customer-managed-policy-terraform-source.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-478.audit-write-grant-as-a-customer-managed-policy-terraform-source`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR478-y-AC1,AR478-y-AC2,AR478-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-478</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident.tf
infra/aws/terraform/investor-reporting/ycharts/resident_audit_policy.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~349/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-478.audit-write-grant-as-a-customer-managed-policy-terraform-source.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two Terraform files edited (one by additions only, one new) and checks in the worker deliverables; nothing is planned, applied or run; the apply is a later IB2 order under a fresh signed pair (expected plan: 2 to add, 0 to change, 0 to destroy).
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the issuer read the role's five inline policies and its one attached managed policy live (attached-policies-per-role quota 20).
comp-adversary: RUN -- by reading IB2's stop receipt, the role's live policies, the CTO ruling (msg 11566) and AR-y-468's edit against this cell; the lens: a deletion in resident.tf beyond the audit additions (the inline policy must equal what is applied, or the plan will try to change it), a Get or List or Delete action in the new statement (put only), a typed ARN or table literal, a KMS statement wider than the audit prefixes, a policy name not from the naming module, an attachment to the wrong role, a managed policy over 6144 bytes, the control that cannot fire. NOT seen (blind): the live plan (the apply order expects exactly 2 to add, 0 to change, 0 to destroy); denominator: three criteria.
</preflight>
