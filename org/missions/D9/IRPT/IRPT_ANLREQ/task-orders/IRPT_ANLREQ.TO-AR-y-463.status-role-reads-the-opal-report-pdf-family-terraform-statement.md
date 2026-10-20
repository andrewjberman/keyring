# TO IRPT_ANLREQ.TO-AR-y-463.status-role-reads-the-opal-report-pdf-family-terraform-statement -- TERRAFORM SOURCE ONLY: add the Opal report PDF family (state/ycharts_opal_reports) to the irpt-status role's existing retained-families read statement for the same client firms; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-463.status-role-reads-the-opal-report-pdf-family-terraform-statement</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~328</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ122</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-463` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 and FWD-9 (the Opal report opens from the ticket) | **depends_on:** run 7b receipt (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7b/A_E2E7B.txt`, stop at R), CTO msg 11459 ("add that family for the same three firms to the same statement, GetObject plus GetObjectVersion, read only, with addresses as builder output (C-NAMES)")

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~328`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-328` (branch `wk-IRPT_ANLREQ-328`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~328 <0.9.0_WK_IRPT_ANLREQ~328@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W328-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the selftest below) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR463-y-AC1,AR463-y-AC2,AR463-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The shape of this order is the earlier sibling `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement.md` (read it, and its worker 320 deliverables `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/check_commentary_grant.py` and `check_commentary_bound.py`, as your pattern).

### THE CELL (`AR-y-463`, inlined)

*The measured gap.* Run 7b stopped at its route read: the status Lambda `irpt-status`, running as `irpt-status-role`, was denied `s3:GetObjectVersion` on `opal-data-irpt/irpt/49financial/state/ycharts_opal_reports/ART-<hex>/<sha>.pdf` (the Opal producer's retained report PDF). The role's inline policy `irpt-status-policy` (Terraform `aws_iam_role_policy.irpt_status`, data `aws_iam_policy_document.irpt_status`, file `infra/aws/terraform/investor-reporting/ops/iam.tf`) has the statement `ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly` (`s3:GetObject`, `s3:GetObjectVersion`) over six families per enabled client firm and not `state/ycharts_opal_reports`. The family is `YCHARTS_OPAL_REPORT` of the reporting policy revision `irpt-x10-v1` (`infra/logic/registry/reporting_policies.json`: `{"tier": "state", "table": "ycharts_opal_reports", "extension": "pdf"}`).

*The change.* In `infra/aws/terraform/investor-reporting/ops/iam.tf`, additions only: (1) in the existing `locals` block, next to `vendor_pdf_family`, add `opal_report_family = "${local.irpt_reporting_policy.families["YCHARTS_OPAL_REPORT"].tier}/${local.irpt_reporting_policy.families["YCHARTS_OPAL_REPORT"].table}"` with a comment in the file's style citing the run 7b stop and CTO msg 11459; (2) append `local.opal_report_family` to the second list of the `concat(...)` that builds the `family` loop of that one statement (the list that already holds `local.original_holdings_family` and `local.vendor_pdf_family`). NO typed bucket, firm, tier or table literal; NO other statement, local or file changed; the actions stay `s3:GetObject` and `s3:GetObjectVersion` (read only: no put, no list, no delete).

*What to do.* (1) Read `infra/aws/terraform/investor-reporting/ops/iam.tf` lines 60-150, `infra/logic/registry/reporting_policies.json`, `data/firm_registry.json` (client enabled firms) and `lib/opal_naming.py` (its `key()` signature). (2) Make the edit above (`git diff --numstat` for the file must read `<n> 0`, one file). (3) Write in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/`: `check_opal_report_grant.py` (stdlib only, ruff clean, offline) that (a) reads `ops/iam.tf` and asserts by regex that the local `opal_report_family` is built from the `YCHARTS_OPAL_REPORT` row of `local.irpt_reporting_policy`, that the statement's family list includes `local.opal_report_family`, that its actions are exactly the two read actions, and that the file holds no literal `ycharts_opal_reports`; (b) evaluates the prefixes in Python from the registries (the enabled client firms of `data/firm_registry.json`, the `irpt` PRODUCT bucket of `infra/logic/registry/scopes.json`, the policy row) as `arn:aws:s3:::<bucket>/irpt/<firm_id>/<tier>/<table>/*` and compares them, firm by firm, with the key the repository's naming builder gives (load `lib/opal_naming.py` BY PATH; say in a comment which comparison you used); (c) takes a real report-PDF key (the `ycharts_opal_reports` key named in the investigation row `IRPT_ANLREQ-D2-S224` of `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, and the run 7b key if `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7b/` names one) and proves it matches exactly one computed prefix by `fnmatch`; it prints ONE line `OPAL-REPORT-GRANT-OK firms=<n> prefixes=<n> builder_equal=yes real_key_covered=yes` or a `OPAL-REPORT-GRANT-BAD <why>` line (rc 1). `--selftest` runs the same checks on a mutated copy of the file text in memory (the table name changed in the computed family, and separately a Put action added) and prints `CONTROL-FIRES` only when BOTH mutants read BAD. `check_opal_report_bound.py` runs `git diff --numstat origin/PROD`-free: it compares the file at HEAD with its first-parent base (`git diff --numstat HEAD~1 HEAD -- infra/aws/terraform/investor-reporting/ops/iam.tf` after your commit of the edit, so commit the edit FIRST and alone) and prints `OPAL-REPORT-BOUND-OK numstat=<n>/0 files=1` only when deletions are 0 and exactly this one file changed in that commit. (4) Commit order: the Terraform edit alone first (message cites AR-y-463), then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR463-y-AC1" cell_refs="AR-y-463"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/check_opal_report_grant.py</invocation><expect>^OPAL-REPORT-GRANT-OK firms=[0-9]+ prefixes=[0-9]+ builder_equal=yes real_key_covered=yes$</expect></criterion>
<criterion id="AR463-y-AC2" cell_refs="AR-y-463"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/check_opal_report_grant.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR463-y-AC3" cell_refs="AR-y-463"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/check_opal_report_bound.py</invocation><expect>^OPAL-REPORT-BOUND-OK numstat=[0-9]+/0 files=1$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/IRPT_ANLREQ.TO-AR-y-463.status-role-reads-the-opal-report-pdf-family-terraform-statement.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-463.status-role-reads-the-opal-report-pdf-family-terraform-statement`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR463-y-AC1,AR463-y-AC2,AR463-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-463</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ops/iam.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~328/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-463.status-role-reads-the-opal-report-pdf-family-terraform-statement.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Terraform file edited by additions only (one local, one list entry), plus checks in the worker deliverables; nothing is planned, applied or run; the apply is a later IB2 order under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the issuer read the live policy statements of irpt-status-role (3 inline policies of interest, the retained-families statement lists 18 prefixes, none under ycharts_opal_reports).
comp-adversary: RUN -- by reading the live role policy, the Terraform source, the registry row and the CTO ruling (msg 11459) against this cell; the lens: a typed ARN or table name (forbidden: the family must come from the registry row and be proved equal to the naming builder), a Put or List or Delete action (read only), another statement or local changed, a firm the existing statement does not cover, a Terraform edit that lands in a different statement than the one that was denied, the control that cannot fire (the selftest mutates the table name and adds a Put, both must read BAD). NOT seen (blind): the live plan (the apply order expects exactly 0 to add, 1 to change, 0 to destroy on aws_iam_role_policy.irpt_status); denominator: three criteria.
</preflight>
