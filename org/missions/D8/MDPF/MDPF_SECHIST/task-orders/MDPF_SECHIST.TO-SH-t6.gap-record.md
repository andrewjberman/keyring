# TO MDPF_SECHIST.TO-SH-t6 -- round 3 SH-t-6: gap record

<to_id>MDPF_SECHIST.TO-SH-t6</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~5</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-6` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-6` (FWD-4). The gap record (C-GAP, PRD v0.2 `:97`; CRO note `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_SECHIST_ROUND3_SUBSTRATE_NOTE_20261009.md` section 1).
Build `data/etfs/scripts/silver/etf_history_gap_record.py`: for each tracked security, its stored range, its required range (C-DEPTH: one
year for an Opal ETF holding), and the listed days -- an ABSENT interior day (a day the vendor counted in a run's `vendor_observations`
but no stored row carries) and a HELD-NULL day (a stored row whose `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` is null). NEVER a trading calendar:
`compute_returns`'s docstring (`data/etfs/scripts/gold/etf_positioning_gold.py:855+`) explains why a calendar test is wrong for
non-US and bond-calendar instruments. Inputs: the `bbg/<date>/` partitions (`history_topup.csv`, `run_manifest.json`
`vendor_observations`) in `s3://opal-data-etfs`. Output address is builder output only:
`lib.opal_naming.address("bloomberg","etfs","silver","history_gaps","as_of=<d>","gap_record.json")`
(= `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json`); expose it as `record_address(as_of)`.
Offline tests with fakes (no network) in `data/etfs/scripts/silver/test_etf_history_gap_record.py`.

### ACCEPTANCE

<criterion id="SH3-t6-AC1" cell_refs="SH-t-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py GAP data/etfs/scripts/silver/test_etf_history_gap_record.py test_absent_interior_day_listed test_held_null_day_listed test_record_address_is_builder_output</invocation><expect>GAP-TESTS-OK</expect></criterion>

<expected_criteria>SH3-t6-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
data/etfs/scripts/silver/etf_history_gap_record.py
data/etfs/scripts/silver/test_etf_history_gap_record.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~5/MDPF_SECHIST.TO-SH-t6.gap-record.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-6`.
<owned_cells>SH-t-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t6-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~5/MDPF_SECHIST.TO-SH-t6.gap-record.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t6-AC1`
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
