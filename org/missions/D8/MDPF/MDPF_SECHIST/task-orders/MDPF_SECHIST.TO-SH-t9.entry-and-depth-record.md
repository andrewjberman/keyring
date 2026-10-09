# TO MDPF_SECHIST.TO-SH-t9 -- round 3 SH-t-9: entry and depth record

<to_id>MDPF_SECHIST.TO-SH-t9</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~8</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-9` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-9` (FWD-3). Where each security entered Opal and how far back its history must go (C-DEPTH, PRD `:94`; CRO note section 4).
Build `data/mdpf/scripts/silver/security_entry_depth.py`: per security, each source -- Opal ETF holding (one year), client account by firm
(from the security's first appearance in that firm's holdings: bd `holdings_lots.acquisition_date`, inf `lots.buy_date`, 49f acquired
dates; reuse `data/black_diamond/scripts/silver/build_bd_assets_dim.py:127` logic for bd), rival fund (one year) -- with its required
start date, and the governing (deepest) rule. Cottonwood enters only through the id map (cell SH-t-10); never invent a date. Never write
classification (C-TABLE). Output address is builder output only:
`lib.opal_naming.address("mdpf","global","silver","security_entry","as_of=<d>","entry_depth.json")`; expose it as `record_address(as_of)`.
Offline tests with fakes in `data/mdpf/scripts/silver/test_security_entry_depth.py`. 49 Financial data never goes into another firm's tree.

### ACCEPTANCE

<criterion id="SH3-t9-AC1" cell_refs="SH-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py ENTRY data/mdpf/scripts/silver/test_security_entry_depth.py test_each_source_depth test_deepest_rule_governs test_record_address_is_builder_output</invocation><expect>ENTRY-TESTS-OK</expect></criterion>

<expected_criteria>SH3-t9-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
data/mdpf/scripts/silver/security_entry_depth.py
data/mdpf/scripts/silver/test_security_entry_depth.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~8/MDPF_SECHIST.TO-SH-t9.entry-and-depth-record.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-9`.
<owned_cells>SH-t-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t9-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~8/MDPF_SECHIST.TO-SH-t9.entry-and-depth-record.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t9-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-2 (opal-data-etfs, opal-data-portal-v2, etf-classifications read); no new grant.
comp-adversary: RUN -- 9 of 9 round-3 criteria dry-run at the base 2026-10-09 ~13:3xZ, 9 FAIL (decomposition Battery); BLIND: live S3 and DynamoDB contents after that read, and the worker's code before it exists.
risk: SERVED -- graded on the served artifact.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-2 analysis @d0230a0dac section 2 (+ ADDENDUM 1 @678d85e071 for item 6); PRD v0.2 + ADDENDUM v0.3.
