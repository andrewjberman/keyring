# TO MDPF_SECHIST.TO-SH-t13 -- round 3 SH-t-13: series writer

<to_id>MDPF_SECHIST.TO-SH-t13</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~12</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-13` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-13` (FWD-2). SECHIST's one series writer (C-SERIES as amended by PRD ADDENDUM v0.3; CTO ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md` + ADDENDUM 1; round-2 analysis
ADDENDUM 1 item 6). Build `data/mdpf/scripts/silver/security_series_writer.py`: given rows for one security (from MDPF_DEMQUE's queue:
card-A Bloomberg rows, or Yahoo rows), write per day the as-traded price, the dividend/interest cash on its ex-date, and the
total-return value ((P + D) / P_prev, analysis item 4), keyed by the Commonwealth 9-character CUSIP exactly as `price_store` keys it
(`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md`; addresses from `lib.opal_naming`).
KEEP, then PORT: `price_store` stays the only live writer -- this module writes NOTHING unless an explicit switch argument is set, and
the switch is a later window under its own pair. Gaps stay blank (C-GAP). Offline tests with fakes in
`data/mdpf/scripts/silver/test_security_series_writer.py`. No S3 write, no queue draw.

### ACCEPTANCE

<criterion id="SH3-t13-AC1" cell_refs="SH-t-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py WRITER data/mdpf/scripts/silver/test_security_series_writer.py test_three_values_per_day test_cusip_key_namespace test_no_write_without_switch</invocation><expect>WRITER-TESTS-OK</expect></criterion>

<expected_criteria>SH3-t13-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
data/mdpf/scripts/silver/security_series_writer.py
data/mdpf/scripts/silver/test_security_series_writer.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~12/MDPF_SECHIST.TO-SH-t13.series-writer.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-13`.
<owned_cells>SH-t-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t13-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~12/MDPF_SECHIST.TO-SH-t13.series-writer.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t13-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and tests only; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-2 (opal-data-etfs, opal-data-portal-v2, etf-classifications read); no new grant.
comp-adversary: RUN -- 9 of 9 round-3 criteria dry-run at the base 2026-10-09 ~13:3xZ, 9 FAIL (decomposition Battery); BLIND: live S3 and DynamoDB contents after that read, and the worker's code before it exists.
risk: LOCAL.
direct_act: false -- a build cell.
</preflight>

Source: CTO round-2 analysis @d0230a0dac section 2 (+ ADDENDUM 1 @678d85e071 for item 6); PRD v0.2 + ADDENDUM v0.3.
