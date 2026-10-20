# TO IRPT_ANLREQ.TO-AR-y-468.resident-role-writes-the-analysis-audit-terraform-statement -- TERRAFORM SOURCE ONLY: add ONE write-only statement to the resident role's policy so the packager can put the audit record under the platinum analysis_audit prefix of the enabled client firms; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-468.resident-role-writes-the-analysis-audit-terraform-statement</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~331</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ127</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD | **Decomp cell:** `AR-y-468` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.27) | **depends_on:** CTO msg 11466; the read of AR-y-462

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~331`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-331` (branch `wk-IRPT_ANLREQ-331`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~331 <0.9.0_WK_IRPT_ANLREQ~331@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W331-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR468-y-AC1,AR468-y-AC2,AR468-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-468`, inlined)

*Context.* PRD v0.27 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the row beginning `C-AUDIT-RECORD:`; CTO ruling msg 11466): one audit JSON per analysis request in a NEW PLATINUM family `ANALYSIS_AUDIT` (table `analysis_audit`, extension json, `accepted_ceiling_days` 2555, `unreferenced_days` null) of the reporting policy revision `irpt-anlreq-x10-v1`, written by the packager at attach time (the hop that holds all four linkages), the form as filed taken from the ticket answers, validated against a published schema `AnalysisAudit.v1`. The read that grounds it: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md` (read it first). Every new S3 address is `lib/opal_naming.py` `address()` output (CLAUDE.md rule 30).

*The change.* The packager runs on the resident host as the role `irpt-ycharts-runner-role`, whose inline policy is `aws_iam_role_policy.runner_resident` in `infra/aws/terraform/investor-reporting/ycharts/resident.tf` (read its `locals` block and the statements around `ReadFrozenCompositionAndNormalizedInput` and the earlier `ReadTheAnalysisCommentaryDraft`, which is your pattern; worker 320's deliverables `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/check_commentary_grant.py` is the check pattern). Additions only: (1) in the `locals` block, a policy local selecting `irpt-anlreq-x10-v1` if one is not already there (reuse it if worker 320's edit added it) and a list `resident_audit_write_prefixes` with one entry per resident scope, built from the registry exactly like `resident_commentary_read_prefixes`, as `arn:aws:s3:::<bucket>/<source>/<scope-long>/<tier>/<table>/*` for family `ANALYSIS_AUDIT` (tier `platinum`, table `analysis_audit`); NO typed ARN, bucket, firm, tier or table literal; find which bucket the platinum tier of a FIRM scope resolves to with the builder's home rule (`infra/logic/registry/tiers.json`, `lib/opal_naming.py` home lookup) and state it in a comment. (2) ONE statement `Sid = "WriteTheAnalysisAudit"`, `Effect = "Allow"`, `Action = ["s3:PutObject"]` ONLY (no get, no list, no delete, no version action), `Resource = local.resident_audit_write_prefixes`, placed after `ReadTheAnalysisCommentaryDraft`. (3) If the bucket the prefixes name is encrypted with a customer key that the role needs `kms:GenerateDataKey` for, read how the existing write statements of this role (the ones for `ycharts_opal_reports`) get it and say, in a surprise row if it differs, whether the new prefixes are covered; do NOT add a KMS statement. NO other statement or file changed. Terraform is not installed on this box: do not try to run it.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/`: `check_audit_write_grant.py` (stdlib only, ruff clean, offline) asserts by regex over the HCL that the statement exists with Effect Allow, Action exactly `["s3:PutObject"]` and Resource `local.resident_audit_write_prefixes`, that the list is built from the registry and holds no `arn:aws:s3:::opal` literal, evaluates the prefixes in Python from the registries and compares each, firm by firm, with the key the repository's naming builder gives (load `lib/opal_naming.py` BY PATH; say which comparison you used), and prints `AUDIT-WRITE-GRANT-OK firms=<n> prefixes=<n> builder_equal=yes put_only=yes`, else `AUDIT-WRITE-GRANT-BAD <why>` (rc 1); `--selftest` mutates the HCL text in memory (the table name changed, and separately `s3:GetObject` added to the actions) and prints `CONTROL-FIRES` only when BOTH read BAD; `check_audit_write_bound.py` prints `AUDIT-WRITE-BOUND-OK numstat=<n>/0 files=1` when the Terraform commit (committed FIRST and alone, message citing AR-y-468) added lines only to this one file.

---

## ACCEPTANCE

<criterion id="AR468-y-AC1" cell_refs="AR-y-468"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/check_audit_write_grant.py</invocation><expect>^AUDIT-WRITE-GRANT-OK firms=[0-9]+ prefixes=[0-9]+ builder_equal=yes put_only=yes$</expect></criterion>
<criterion id="AR468-y-AC2" cell_refs="AR-y-468"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/check_audit_write_grant.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR468-y-AC3" cell_refs="AR-y-468"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/check_audit_write_bound.py</invocation><expect>^AUDIT-WRITE-BOUND-OK numstat=[0-9]+/0 files=1$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/IRPT_ANLREQ.TO-AR-y-468.resident-role-writes-the-analysis-audit-terraform-statement.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-468.resident-role-writes-the-analysis-audit-terraform-statement`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR468-y-AC1,AR468-y-AC2,AR468-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-468</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-468.resident-role-writes-the-analysis-audit-terraform-statement.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- files named in `<paths>` plus checks in the worker deliverables; nothing is planned, applied, deployed or run against AWS; the release and apply are later orders under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO ruling (msg 11466), the PRD row and the AR-y-462 read against this cell; the lens: a typed ARN or table name, a Get or List or Delete or version action (put only), another statement or local changed, a firm or bucket the existing grants do not cover, a KMS statement added, the control that cannot fire. NOT seen (blind): the live plan (the apply order expects exactly 0 to add, 1 to change, 0 to destroy on aws_iam_role_policy.runner_resident); denominator: three criteria.
</preflight>
