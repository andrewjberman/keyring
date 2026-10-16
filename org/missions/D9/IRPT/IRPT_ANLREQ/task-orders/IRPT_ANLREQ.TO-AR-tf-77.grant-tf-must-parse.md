# TO-AR-tf-77 -- FWD-4 repair: the grant's Terraform source must parse (AR-tf-77, round 56, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tf-77</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~234</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>56</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tf-77` (`decompositions/IRPT_ANLREQ_DECOMP_R56_TX.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none (AR-tf-73 is merged)

---

## WORKER FACE

### THE CELL

`AR-tf-77`: "the grant's Terraform source must parse." Round 48's cell AR-tf-73 added statements S6 and S7 to `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf` (the inline policy `jsonencode` list of the draft-store role) and a static text test `infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py`. The applier `0.7.0_AE_CloudOps~AQ2` ran `terraform plan` on the merged file and it FAILED TO PARSE: "Missing item separator ... line 88" (S7 closes at line 87 and the old S1 opens at line 88 with NO comma between them; applier record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_t54/A_PRE_T54.txt`, READ it first). The static test did not catch it because it read statements by Sid and never checked the list separators. This is a defect of the merged cell, and `terraform` is not installed in your environment.

**What to do.** (1) Fix `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf`: the missing separator, and nothing else; every other byte of the file stays identical (the diff must be exactly the one comma, or the smallest change that makes the list well formed). (2) Extend `infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py` with tests named `test_hop_failure_<what>` that catch this class: a small scanner over the `policy = jsonencode({...})` block of the role policy that walks the `Statement = [ ... ]` list tracking bracket and brace depth and strings, and asserts that between every pair of adjacent top-level statement objects `{...}` there is exactly one comma, there is no trailing comma problem you can cheaply prove (HCL allows a trailing comma in a list), and the number of top-level statements is 7 (S6, S7, S1 to S5). Add in-memory mutants: the real text with the comma between S7 and S1 removed must be refused by the scanner; the real text with a comma between S1 and S2 removed must be refused; the real text must pass. Keep every existing test green. At least 12 tests in the file in total pass. (3) Also scan the SAME file for any other statement-list or block syntax problem your scanner can cheaply prove (unbalanced braces, brackets or quotes across the whole file) and add a test for balance. If you find another defect, fix it only if it is a pure separator or bracket defect inside the grant, and say so in a surprise row; otherwise file the row and leave it.

Standard library and pytest only. No terraform, no AWS. Use plain names.

### ACCEPTANCE

<criterion id="AR77-tf-AC1" cell_refs="AR-tf-77"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 12 --prefix=test_hop_failure_ infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR77-tf-AC1` -- the tests pass and at least 12 pass (the file had 11 before this cell, so the base reads FAIL). Dry-run at box/dell2 baf4fcf244: `R46-TESTS-FAIL 11 passed, need 12` -- FAIL as expected.

<expected_criteria>AR77-tf-AC1</expected_criteria>

## BOUNDS

- **Grant.** `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf` (the one-comma repair only) and `infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py`, this order's file, your deliverables folder, the surprise channel. No other file.
- **No terraform, no plan, no apply, no AWS, no deploy.**
- **Refusal clause.** If the file at your base already has the comma, say so in a row and make no edit to `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf
infra/aws/terraform/investor-reporting/export/tests/test_hop_failure_grant.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R56_TX.md</decomp_doc> (round 56, workstream ~TX), cell `AR-tf-77`.
<owned_cells>AR-tf-77</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR77-tf-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~234/IRPT_ANLREQ.TO-AR-tf-77.grant-tf-must-parse.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR77-tf-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the exact diff of `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf` (line count added and removed), the count passed, each mutant's refusal text, anything else the scanner found, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one separator in a Terraform source file not yet applied, plus a test; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission changes in this cell (the grant itself is AR-tf-73's and is applied by the applier).
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: a text test that reads statements by Sid and never the separators between them (the defect that shipped); fixing more than the one separator so the signed grant changes in meaning; a scanner that treats a comma inside a string as a separator; HCL's allowance of a trailing comma read as a defect.
</preflight>

- Repair of a defect found at the applier's plan (msg 9184). Risk WORLD by the path floor (`<paths>` under `infra/`): one comma and a test, no deploy.
- Base: `AR77-tf-AC1` FAIL as expected at box/dell2 baf4fcf244.
