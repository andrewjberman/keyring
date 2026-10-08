# TO MDPF_SECCLASS.TO-SC-e72 -- round 12 SC-e-72: READ-ONLY cash grade: cash/Cash rows by classified_by against the 316 planned

<to_id>MDPF_SECCLASS.TO-SC-e72</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~62</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-72` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-72`. CTO round-12 analysis section 3 item 6: "Cash grade, read only: count of `cash`/`Cash` rows by `classified_by` after
e32's legs, against the 316 the V3 set planned." e65 left the cash outcome unexercised (0 cash_token rows), so this is its evidence.

**Build:**
1. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_grade.py`. It is read-only: a paginated ConsistentRead scan of etf-classifications.
   - Count the rows with asset_class `cash`, by sub_asset_class and by classified_by.
   - Count how many of the V3 set's cash-planned keys (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv`, route DIRECT, asset_class cash)
     are present at their planned sub-class.
   - Print `CASH-GRADE ok=<bool> cash_rows=<n> by_classified_by=<dict> v3_planned=<n> v3_present_at_plan=<n> fixed_income_Cash=<n>`.
   - ok means v3_present_at_plan equals the planned keys still absent-free, AND fixed_income_Cash is 0. Report it as measured; the grade
     is run again at e32's close.

### ACCEPTANCE

<criterion id="SC12-e72-AC1" cell_refs="SC-e-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_grade.py</invocation><expect>CASH-GRADE</expect></criterion>
`SC12-e72-AC1` -- the grade runs and prints its counts with denominators.

<expected_criteria>SC12-e72-AC1</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e72-AC1 FAIL as expected (the grade script is absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- Read-only DynamoDB scan; no write of any kind. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W62-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_grade.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-72`.
<owned_cells>SC-e-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e72-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~62/MDPF_SECCLASS.TO-SC-e72.cash-grade-read-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e72-AC1` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE read-only; it is re-run at e32's close.
comp-iam: DECLARED-NOT-APPLICABLE a read dell1 already makes.
comp-adversary: RUN -- a grade on one scan page (paginated scan); a pass that hides legacy fixed_income/Cash rows (they are counted); BLIND: the e32 and e49 AI legs' rows not yet written (the grade is re-run at e32's close).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 6; CTO note msg 766; DECOMP_R12.
