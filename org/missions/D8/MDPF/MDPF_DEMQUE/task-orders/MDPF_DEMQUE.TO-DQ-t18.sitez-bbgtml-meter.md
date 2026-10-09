# TO MDPF_DEMQUE.TO-DQ-t18 -- round 5 DQ-t-18: meter the OPAL_BBGTML notebook draws into the demand ledger (site Z)
<to_id>MDPF_DEMQUE.TO-DQ-t18</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~ZQ</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~10:0xZ (row MDPF_DEMQUE-Z-W1-S3, refusal `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T18_REFUSAL.md`):** build item 2's `bbgtml-unmetered` row contradicts three exact-count assertions in `test_demque_bbg_ledger_upload.py`, which the cut left outside the grant -- the issuer's defect. GRANTED: `data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py`. Its cardinality expectations may count exactly ONE `bbgtml-unmetered` row (cells null, claim absent) on a fixture day with no `bbgtml-*` line; every original conversion, dry-run and idempotence assertion stays as it is. Build item 3 now reads: keep `test_demque_bbg_ledger_upload.py` passing with only that change. The sentinel interface is unchanged.
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~10:5xZ (CTO~Z half @3ccf1f560f, C1: merge only after today's 07:00 ET run is read, so the first metered run is 2026-10-10):** build item 4's last sentence no longer holds the order open. The order completes when the meter is merged at site Z after today's run, the RUNNER step points at it inside the change-management entry, and AC1 + AC2 pass. The first metered scheduled run's ledger lines are read by the issuer at round 6's real run, not by this order. No criterion changes.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-18` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 5 -- CUT) |
**outcome_ref:** FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-18` (CTO round-4 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round4.md` R2; your own row
`MDPF_DEMQUE-Z-W1-S2`). The scheduled task `OPAL_BBGTML_daily_pull` (07:00 ET) runs `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`
RUNNER, which runs `tplus1/tools/run_daily_pull.py`, which executes `market_indices_data_pull.ipynb` and
`model_portfolio_regression_analysis.ipynb`. None of them call `bbg_budget.record()`, so their Bloomberg draws are missing from the demand
ledger your uploader (`data/mdpf/scripts/demque/bbg_ledger_upload.py`) serves. C-PRODUCERS: the queue records and the producer is not
rewritten -- no notebook is edited.

**Build:**
1. NEW `data/mdpf/scripts/demque/bbgtml_meter.py`: runs the runner's notebooks exactly as `run_daily_pull.py` does (or wraps that
   runner), and after each notebook run writes ONE `bbg_budget.record(mode="bbgtml-<notebook stem>", rows=<n>, batch_id="bbgtml-<UTC
   stamp>")` line. `rows` is what the run returned where the runner can read it (state how); where it cannot, record `rows=0` and
   carry that in the batch id so the uploader marks it unreadable. Its exit code is the runner's: a meter failure never fails the pull.
2. `bbg_ledger_upload.py`: a `bbgtml-*` mode becomes a ledger row with `cells` from a readable field declaration, else `cells: null` and
   `claim: "absent"` (never an invented conversion); a day with no `bbgtml-*` line gets ONE row `mode: "bbgtml-unmetered"`,
   `cells: null`, `claim: "absent"`, basis naming this order.
3. NEW `data/mdpf/scripts/demque/test_demque_bbgtml_meter.py` (pytest; stub notebook runs, a temporary ledger dir) with exactly these
   names: `test_each_notebook_run_records_one_budget_line`, `test_unreadable_cells_record_null_with_claim_absent`,
   `test_ledger_day_without_meter_lines_carries_unmetered_line`. Keep `test_demque_bbg_ledger_upload.py` passing.
4. **The site-Z act (a pair; `1.0.0_SA_CTO~Z` signs the site-Z half):** point the RUNNER step of `scheduled_daily_pull.cmd` at the meter
   (the 07:00 task itself is not changed), under a change-management entry opened at start and closed at completion. Read the next
   scheduled 07:00 ET run's ledger lines back and name them in your report; if that run is not before your report, say so and leave the
   order open for it.

### ACCEPTANCE

<criterion id="DQ5-t18-AC1" cell_refs="DQ-t-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t18_tests.py</invocation><expect>METER-OK</expect></criterion>
<criterion id="DQ5-t18-AC2" cell_refs="DQ-t-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t18_ledger.py</invocation><expect>BBGTML-OK</expect></criterion>
`DQ5-t18-AC1` -- the three named tests. `DQ5-t18-AC2` -- at site Z, the uploader's dry run for the latest ledger day carries a
`bbgtml-*` row (a metered run, or the one unmetered row).

<expected_criteria>DQ5-t18-AC1,DQ5-t18-AC2</expected_criteria>

Run each invocation from the worktree root at site Z. At the base: `METER-BAD no file ...`; `BBGTML-BAD ... bbgtml_rows=0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No notebook edited, no Bloomberg call of your own** (the 07:00 run draws as it always has), no change to the 07:00 task, no IAM or
  auth change. The `.cmd` edit is this order's WORLD act, under the pair. Naming: a new name comes from `lib/opal_naming.py`
  (naming-place enforcement is live, msg 2082).
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-Z-W1-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbgtml_meter.py
data/mdpf/scripts/demque/test_demque_bbgtml_meter.py
data/mdpf/scripts/demque/bbg_ledger_upload.py
data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py
integrations/bloomberg/pipeline/scheduled_daily_pull.cmd
org/critical_paths/change_management/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 5), cell `DQ-t-18`.
<owned_cells>DQ-t-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ5-t18-AC1, DQ5-t18-AC2. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t18.sitez-bbgtml-meter.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ5-t18-AC1,DQ5-t18-AC2` BEFORE the flip.
Identical canonical tree copy for the completion gate:
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.7.0_AE_CloudOps~ZQ/MDPF_DEMQUE.TO-DQ-t18.sitez-bbgtml-meter.proof_of_spec.json`.
</proof_of_spec>

**REPORT:** the files, every check's output, the change-management entry, the 07:00 run's ledger lines, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at the cut: the 07:00 ET OPAL_BBGTML task is read, not changed; the seat reads comp-schedule at site Z before the .cmd edit and names it in the report.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject (read at DQ-t-14) is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE a wrapper that records and never fails the pull; reviewed under the site-Z half.
risk: WORLD -- an edit to the 07:00 production runner's step at site Z, under a pair (CTO~Z signs the site-Z half).
direct_act: false -- a seat order to the site-Z per-project lane.
</preflight>

Source: CTO round-4 analysis @91f3ee9da6 R2; row MDPF_DEMQUE-Z-W1-S2; PRD C-PRODUCERS; decomposition round 5. Codex lanes run this
mission-tree order directly (site Z AGENTS.md @a55888e3a2).

## Completion -- 0.7.0_AE_CloudOps~ZQ, 2026-10-09

Completed under issuer amendment ebdd71e8ed. CTO signature 3ccf1f560f C1 discharged by reading the completed Oct9 07:00 Eastern
baseline log before signed source e465eabe7b merged as 04124013f9. Live RUNNER points to the meter; five code files match the signed
candidate and scheduled task XML is unchanged. AC1 METER-OK (5 passing executions); AC2 BBGTML-OK day2026-10-09, 1 bbgtml row of4.
Original uploader suite:5 passed. Bound proof VALID (2 of2 criteria,0 violations) before this status flip.
Deployment record `org/critical_paths/change_management/20261009T1002Z_mdpf-demque-zq-t18-meter_deploy_completion.md` CLOSED @856117665b.
Report: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T18_REVIEW.md`.
First metered scheduled run remains unobserved and is assigned to issuer round6 by the amendment; not a claim of this completion.
