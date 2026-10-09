# TO MDPF_SECHIST.TO-SH-t15 -- round 4 SH-t-15: gap record producer

<to_id>MDPF_SECHIST.TO-SH-t15</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~14</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-15` (`decompositions/MDPF_SECHIST_DECOMP_R4.md`) | **outcome_ref:** FWD-4, FWD-5 |
**depends_on:** none (SH-t-6, SH-t-7 merged)

---

## WORKER FACE

### THE CELL

`SH-t-15` (FWD-4, FWD-5). The gap-record PRODUCER (round-3 analysis item 1; the missing hop). Today nothing calls
`data/etfs/scripts/silver/etf_history_gap_record.py`'s `write_record`. In the scheduled Positioning path
(`data/etfs/scripts/gold/etf_positioning_gold.py`, `lambda_handler` -> `build_tables`), build the day's gap record with that module's own
functions (`load_partitions`, `build_gap_record`) and write it with `write_record` BEFORE returns are computed, then pass it to
`compute_returns` (SH-t-7's `gap_record` argument), so gold blanks over a listed gap the same day and the next pull re-requests from it.
A day with no gap writes NO gap line for that security (negative arm). A write failure is logged and the run continues (production is
never blocked by bookkeeping), and the record address is `record_address(as_of)` only. Offline tests with fakes (no network) in
`data/etfs/scripts/gold/test_etf_positioning_gap_record_producer.py`. Keep every existing gold test that passed before still passing.

### ACCEPTANCE

<criterion id="SH4-t15-AC1" cell_refs="SH-t-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py PRODUCER data/etfs/scripts/gold/test_etf_positioning_gap_record_producer.py test_scheduled_run_writes_gap_record test_no_gap_day_writes_no_gap_line</invocation><expect>PRODUCER-TESTS-OK</expect></criterion>

<expected_criteria>SH4-t15-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~15:4xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher; tests use fakes.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.

<paths>
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/test_etf_positioning_gap_record_producer.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~14/MDPF_SECHIST.TO-SH-t15.gap-record-producer.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R4.md</decomp_doc> (round 4), cell `SH-t-15`.
<owned_cells>SH-t-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH4-t15-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~14/MDPF_SECHIST.TO-SH-t15.gap-record-producer.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH4-t15-AC1`
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
