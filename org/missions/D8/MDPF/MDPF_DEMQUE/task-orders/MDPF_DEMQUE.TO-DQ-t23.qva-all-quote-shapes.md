# TO MDPF_DEMQUE.TO-DQ-t23 -- round 7 DQ-t-23: quote_vs_actual --all reads every quote file, older shapes included
<to_id>MDPF_DEMQUE.TO-DQ-t23</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~20</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-23` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 7 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-23` (FWD-4; CTO round-6 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round6.md` R2; row `MDPF_DEMQUE-D1-S4`).
`data/mdpf/scripts/demque/quote_vs_actual.py --all` raises `KeyError: 'finish_date'` on
`org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json`, an older quote shape with no `finish_date`.

**Build:**
1. `quote_vs_actual.py`: a quote file with no `finish_date` reads `verdict: "UNQUOTED"` with `finish_date: null` and a `gap` naming
   the missing key -- never a raise, never a default date. `--all` prints one JSON line per `requests/*.quote.json` file and exits 0.
   `--request` on a missing quote FILE still raises `ValueError`.
2. NEW `data/mdpf/scripts/demque/test_demque_qva_all.py` (pytest; temporary files) with exactly these names:
   `test_quote_without_finish_date_reads_unquoted_not_raises`, `test_all_reads_every_quote_file`. Keep
   `test_demque_quote_vs_actual.py` passing.

### ACCEPTANCE

<criterion id="DQ7-t23-AC1" cell_refs="DQ-t-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t23_tests.py</invocation><expect>QALLT-OK</expect></criterion>
<criterion id="DQ7-t23-AC2" cell_refs="DQ-t-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t23_all.py</invocation><expect>QALL-OK</expect></criterion>
`DQ7-t23-AC1` -- the two named tests. `DQ7-t23-AC2` -- `--all` over the REAL requests folder: one line per quote file, the SECHIST card
`UNQUOTED`.

<expected_criteria>DQ7-t23-AC1,DQ7-t23-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `QALLT-BAD no file ...`, `QALL-BAD rc=1 lines=2 of 4 ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS, no Bloomberg call, no deploy.** The quote and actuals files are read, never written.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W20-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/quote_vs_actual.py
data/mdpf/scripts/demque/test_demque_qva_all.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 7), cell `DQ-t-23`.
<owned_cells>DQ-t-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ7-t23-AC1, DQ7-t23-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~20/MDPF_DEMQUE.TO-DQ-t23.qva-all-quote-shapes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ7-t23-AC1,DQ7-t23-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS access.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code reading repo files.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-6 analysis @4f7ded8845 R2; row D1-S4; decomposition round 7.
