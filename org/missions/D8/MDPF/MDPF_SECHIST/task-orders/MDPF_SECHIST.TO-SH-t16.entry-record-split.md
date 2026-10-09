# TO MDPF_SECHIST.TO-SH-t16 -- round 4 SH-t-16: entry record split

<to_id>MDPF_SECHIST.TO-SH-t16</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~15</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-16` (`decompositions/MDPF_SECHIST_DECOMP_R4.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-16` (FWD-3). SH-t-9's SPLIT (round-3 analysis R1; REC `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/REC_SH_T9_ENTRY_RECORD_SCOPE_20261009.md`).
Change `data/mdpf/scripts/silver/security_entry_depth.py` so it produces TWO kinds of record: (1) per firm, at
`lib.opal_naming.address("mdpf", <firm registry key>, "silver", "security_entry", "as_of=<d>", "entry_depth.json")`, that firm's
first-appearance date per security; (2) global, at the existing global address, per security ONLY `governing_start` and the governing
source CLASS (`opal_etf` / `client_account` / `rival_fund`) -- never a firm name, never a per-firm date. Firm keys come from the registry
(`lookup()`), never typed. 49 Financial data never goes into another firm's tree. Offline tests with fakes in
`data/mdpf/scripts/silver/test_security_entry_depth_split.py`; keep `test_security_entry_depth.py` passing.

### ACCEPTANCE

<criterion id="SH4-t16-AC1" cell_refs="SH-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py SPLIT data/mdpf/scripts/silver/test_security_entry_depth_split.py test_firm_dates_only_in_firm_scope test_global_holds_only_governing_start</invocation><expect>SPLIT-TESTS-OK</expect></criterion>

<expected_criteria>SH4-t16-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~15:4xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher; tests use fakes.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.

<paths>
data/mdpf/scripts/silver/security_entry_depth.py
data/mdpf/scripts/silver/test_security_entry_depth_split.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~15/MDPF_SECHIST.TO-SH-t16.entry-record-split.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R4.md</decomp_doc> (round 4), cell `SH-t-16`.
<owned_cells>SH-t-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH4-t16-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~15/MDPF_SECHIST.TO-SH-t16.entry-record-split.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH4-t16-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; the schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE fakes only; the Lambda write grant is checked at the deploy pair, not here.
comp-adversary: RUN -- 5 of 5 round-4 criteria dry-run at the base 2026-10-09 ~15:4xZ, 5 FAIL (decomposition Battery); BLIND: live S3 contents after that read, and the worker's code before it exists.
risk: SERVED.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-3 analysis (msg 2675) section 3; PRD v0.2 + ADDENDUM v0.3.
