# TO MDPF_SECHIST.TO-SH-t8 -- round 3 SH-t-8: pull fill and total return field

<to_id>MDPF_SECHIST.TO-SH-t8</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~7</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-8` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-5, FWD-9 |
**depends_on:** TO-SH-t6 (reads the gap record's listed days)

---

## WORKER FACE

### THE CELL

`SH-t-8` (FWD-5, FWD-9). The pull, BUILD ONLY, in `integrations/bloomberg/pipeline/etf_daily_pull.py` (Andrew lifted no-modify for THIS file:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_CALLS_ANSWERED.md`; every other file under
`integrations/bloomberg/pipeline/` stays under the order -- do not touch them).
(1) The next run's history request also covers each listed day of the gap record (today the top-up window starts the day after the
prior manifest's window end, `:425-441`, so a held-null day is never re-requested).
(2) The history request (`:472`, today `PX_LAST` and `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`) gains ONE total-return level field (route 2a).
Both changes stay inside the bbg_budget plan and its refusal (C-BUDGET). Offline tests in
`integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`. No Bloomberg call, no run of the pull. The site-Z take is NOT this
cell: it is a separate WORLD act under `1.0.0_SA_CTO~Z`'s never-widen half and an MDPF_DEMQUE quote.

### ACCEPTANCE

<criterion id="SH3-t8-AC1" cell_refs="SH-t-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py PULL integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py test_next_run_requests_listed_gap_days test_history_request_carries_total_return_level</invocation><expect>PULL-TESTS-OK</expect></criterion>

<expected_criteria>SH3-t8-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. No S3 write, no Bloomberg call, no run of the pull or the publisher.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
integrations/bloomberg/pipeline/etf_daily_pull.py
integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~7/MDPF_SECHIST.TO-SH-t8.pull-fill-and-total-return-field.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-8`.
<owned_cells>SH-t-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t8-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~7/MDPF_SECHIST.TO-SH-t8.pull-fill-and-total-return-field.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t8-AC1`
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
