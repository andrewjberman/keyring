# TO IRPT_ANLREQ.TO-AR-y-481.analysis-audit-gets-its-own-policy-row-and-the-anlreq-row-is-restored -- FIX AND PROVE OFFLINE: restore the registry row irpt-anlreq-x10-v1 byte for byte (AR-y-466 edited it in place and changed its policy_sha256, which made run 7e's retention refuse) and register ANALYSIS_AUDIT in its OWN row irpt-anlreq-audit-x10-v1 (PENDING_ENFORCEMENT); repoint the audit code, tests and the Terraform local; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-481.analysis-audit-gets-its-own-policy-row-and-the-anlreq-row-is-restored</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~350</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ140</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-481` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** run 7e's stop (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7e/A_E2E7E.txt`, row S239), CTO rulings msgs 11637, 11640 and 11646 (the ruling file `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_RETENTION_REVISION_ROWS_ARE_IMMUTABLE_20261020.md` @88ae0673276c9c9b0ce068c0273c6ebf25de5a48, LOCAL on the CTO's branch: you may not be able to read it; the terms are quoted below)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~350`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-350` (branch `wk-IRPT_ANLREQ-350`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~350 <0.9.0_WK_IRPT_ANLREQ~350@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W350-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the selftest below) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR481-y-AC1,AR481-y-AC2,AR481-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-481`, inlined)

*The measured cause.* AR-y-466 (your predecessor `0.9.0_WK_IRPT_ANLREQ~340`, commit `1c277930e66`) added the family `ANALYSIS_AUDIT` INSIDE the existing row `irpt-anlreq-x10-v1` of `infra/logic/registry/reporting_policies.json`. That changed the row's `policy_sha256` (the issuer's colleague measured `8edbe84b05765c36` -> `cfed04bb8c2f1982` by computing `reporting_policy()` from the packaged r34n and r34o trees). `reports/retention.py` (lines 53-88, `_registered` and `_policy`) binds every retention reference to its revision's policy and its canonical hash, and `reports/generate_installed.py` (line 13) uses the packaged registry's `policy_sha256` as the `destination_revision`; two components packaged with different bytes of that row therefore disagree, and run 7e stopped at the packager with `RetentionRefused`. `reports/composition.py` (lines 17-19) already states the rule: a policy row is never edited in place.

*The CTO's terms (msg 11646).* Restore `irpt-anlreq-x10-v1` byte for byte. Put `ANALYSIS_AUDIT` in its OWN row `irpt-anlreq-audit-x10-v1`: `register_commit` reuse `705dae3202cac873a133825bee9d0381c7dd6b7f` (the value `irpt-anlreq-x10-v1` carries), `ruling_commit` `88ae0673276c9c9b0ce068c0273c6ebf25de5a48`, `state` `PENDING_ENFORCEMENT`, `enforcement_ref` null (it flips to ACTIVE, with a commit recording the applied audit policy, before any row is reserved under it, and is never edited after).

*The change.* (1) In `infra/logic/registry/reporting_policies.json`: restore the row `irpt-anlreq-x10-v1` to exactly the text it had at `1c277930e66^` (its families are then only `ANALYSIS_COMMENTARY`); add ONE new row after it, `policy_revision` `irpt-anlreq-audit-x10-v1`, with the same shape of fields as `irpt-anlreq-x10-v1` (`policy_id` `irpt-anlreq-audit`, `register_id`, `register_path`, `retention_policy_id`, `source`, `product_scope`, `firms`, `physical_disposal` as that row has them) and the terms above, and `families` holding only `ANALYSIS_AUDIT` with the same values AR-y-466 gave it (`tier` platinum, `table` analysis_audit, `extension` json, `unreferenced_days` null, `accepted_ceiling_days` 2555). READ `lib/opal_naming.py` (`_validate_reporting_policies`, `reporting_policy`, `reporting_destination`) first and say, in your report, how each treats a row whose state is not ACTIVE and whose `enforcement_ref` is null: if the validator REFUSES the row as the CTO specified it, STOP with a BLOCKING row naming the refusing line and change nothing in the registry. (2) In `infra/aws/lambda/investor-reporting/reports/analysis_audit.py` point the policy revision at `irpt-anlreq-audit-x10-v1` (and nothing else); update `infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py` and `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py` for the new revision; if the builder refuses an address under a not-ACTIVE row, the tests must supply the registry the way their existing fixtures do (a copy with the row ACTIVE in memory) and say so in a comment; no test is deleted or skipped. (3) In `infra/aws/terraform/investor-reporting/ycharts/resident.tf`: add one local selecting the policy `irpt-anlreq-audit-x10-v1` (the way `resident_commentary_policy` selects its row) and build `resident_audit_write_prefixes` from it for family `ANALYSIS_AUDIT` (additions in that local only; the bucket, firms, tier and table values must be unchanged: the prefix strings equal what they were). No other file changes. The old checkers of AR-y-466, AR-y-468 and AR-y-478 stay as history; do not edit them.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~350/`: `check_audit_row.py` (stdlib only, ruff clean, offline). It computes `reporting_policy('irpt-anlreq-x10-v1')['policy_sha256']` by loading `lib/opal_naming.py` BY PATH at HEAD and at the commit `1c277930e66^` (use `git show` into a temporary file outside the repository, or read the blob into memory) and requires them EQUAL; it requires the new row to hold exactly the terms above and `families` == `['ANALYSIS_AUDIT']`; it requires that no other row of the file differs from `1c277930e66^`; and it requires `resident_audit_write_prefixes` in `resident.tf` to name the new row. It prints `AUDIT-ROW-OK old_policy_sha_equal=yes new_row=PENDING_ENFORCEMENT enforcement_ref=null register_commit=705dae32 ruling_commit=88ae0673 other_rows_unchanged=yes` or `AUDIT-ROW-BAD <why>` (rc 1). `--selftest` mutates in memory three ways (the old row given `ANALYSIS_AUDIT` again; the new row `state` ACTIVE with `enforcement_ref` null; the new row given a 40-hex `enforcement_ref`) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the registry, code, test and Terraform edits as ONE commit first, message citing AR-y-481; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR481-y-AC1" cell_refs="AR-y-481"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~350/check_audit_row.py</invocation><expect>^AUDIT-ROW-OK old_policy_sha_equal=yes new_row=PENDING_ENFORCEMENT enforcement_ref=null register_commit=705dae32 ruling_commit=88ae0673 other_rows_unchanged=yes$</expect></criterion>
<criterion id="AR481-y-AC2" cell_refs="AR-y-481"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~350/check_audit_row.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR481-y-AC3" cell_refs="AR-y-481"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest reports/tests/test_analysis_audit.py ycharts/generate/tests/test_audit_live_wiring.py reports/tests/test_generate_installed.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~350/IRPT_ANLREQ.TO-AR-y-481.analysis-audit-gets-its-own-policy-row-and-the-anlreq-row-is-restored.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-481.analysis-audit-gets-its-own-policy-row-and-the-anlreq-row-is-restored`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR481-y-AC1,AR481-y-AC2,AR481-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-481</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/logic/registry/reporting_policies.json
infra/aws/lambda/investor-reporting/reports/analysis_audit.py
infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py
infra/aws/terraform/investor-reporting/ycharts/resident.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~350/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-481.analysis-audit-gets-its-own-policy-row-and-the-anlreq-row-is-restored.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- the registry file edited (one row restored, one added), two source/test files and one Terraform local; nothing is planned, applied, deployed or run against AWS; the packaged registry of r34p is built by 2.0.0_SA_COO~G2 from r34o minus this file.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading run 7e's receipt, the retention module and the CTO's terms against this cell; the lens: the old row restored by hand-editing instead of from the commit before AR-y-466 (the policy hash must EQUAL the old one), another row changed, a row the validator accepts only because its fields were guessed (read the validator), an ACTIVE state set before the audit policy is applied, an enforcement_ref invented, a test deleted or skipped to pass, a Terraform local that changes the prefix strings, the control that cannot fire. NOT seen (blind): the live retention rows reserved since 23:12Z; denominator: three criteria.
</preflight>
