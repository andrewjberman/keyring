# TO MDPF_DEMQUE.TO-DQ-t19 -- round 6 DQ-t-19: read a quoted request against its frozen finish day (FWD-4 exercised)
<to_id>MDPF_DEMQUE.TO-DQ-t19</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~16</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~12:5xZ (worker ~16's report):** `drawn_date` is CUMULATIVE -- the first actuals `date` (in date order) on which the job's running sum of `cells_drawn` reaches `cells_quoted`, else null. A request drawn over several days (the 15,720-cell history request) finishes the day its total is reached, not when one row alone reaches it. Add one assertion of a multi-row cumulative finish inside `test_on_time_when_drawn_on_or_before_finish_day`. No criterion changes.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-19` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 6 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-19` (FWD-4; CTO round-5 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round5.md` item 1). FWD-4 is REALIZED when a
quoted request is read as finished by its quoted day. Each quote is frozen beside its request as
`org/missions/D8/MDPF/MDPF_DEMQUE/requests/<request_id>.quote.json` (keys `request_id`, `channel`, `cells`, `quoted_at`, `finish_date`,
`finish_date_claim`, `basis`). Bloomberg actuals are lines of `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl` (written by
`bbg_quote.record_actual`; keys `date`, `job` = request_id, `cells_quoted`, `cells_drawn`, `outcome`). Read both files; edit neither.

**Build:**
1. NEW `data/mdpf/scripts/demque/quote_vs_actual.py`: `read(request_id, requests_dir, actuals_path, today) -> dict` with `request_id`,
   `finish_date`, `drawn_date` (the latest actuals `date` for that job whose cells drawn reach the quoted cells, else null),
   `cells_quoted`, `cells_drawn` (summed), and `verdict`: `ON_TIME` (drawn on or before the finish day), `LATE` (drawn after it, or still
   undrawn after it), `OPEN` (undrawn and the finish day not yet passed). A missing quote file is a `ValueError`, never a default. CLI:
   `--request <id>` prints ONE JSON line (defaults: the repo's requests dir, actuals file and today); `--all` prints one line per frozen
   quote.
2. NEW `data/mdpf/scripts/demque/test_demque_quote_vs_actual.py` (pytest; temporary files) with exactly these names:
   `test_on_time_when_drawn_on_or_before_finish_day`, `test_late_when_drawn_after_finish_day`, `test_open_when_no_actual_yet`.

### ACCEPTANCE

<criterion id="DQ6-t19-AC1" cell_refs="DQ-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t19_tests.py</invocation><expect>QVA-OK</expect></criterion>
<criterion id="DQ6-t19-AC2" cell_refs="DQ-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t19_read.py</invocation><expect>FWD4-OK</expect></criterion>
`DQ6-t19-AC1` -- the three named tests. `DQ6-t19-AC2` -- the REAL reference request read against its frozen 2026-10-09 finish day.

<expected_criteria>DQ6-t19-AC1,DQ6-t19-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `QVA-BAD no file ...`, `FWD4-BAD no file ...quote_vs_actual.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS, no Bloomberg call, no deploy.** The quote and actuals files are read, never written.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W16-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/quote_vs_actual.py
data/mdpf/scripts/demque/test_demque_quote_vs_actual.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 6), cell `DQ-t-19`.
<owned_cells>DQ-t-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ6-t19-AC1, DQ6-t19-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~16/MDPF_DEMQUE.TO-DQ-t19.quote-vs-actual.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ6-t19-AC1,DQ6-t19-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output (the verdict line verbatim), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS access.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code reading two repo files.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: PRD FWD-4; CTO round-5 analysis @7732d73c04 item 1; frozen quotes @70379bb41d; decomposition round 6.
