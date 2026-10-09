# TO MDPF_DEMQUE.TO-DQ-t20 -- round 6 DQ-t-20: the history reserve seeded from the ledger's measured daily draw
<to_id>MDPF_DEMQUE.TO-DQ-t20</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~17</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-20` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 6 -- CUT) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-20` (FWD-3, C-RESERVE; CTO round-5 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round5.md` R1; row
`MDPF_DEMQUE-D1-W13-S1`). `data/mdpf/scripts/demque/bbg_allowance.json` holds `history.reserve` = 40 cells, counted from static producer
names, while the served demand ledger (builder home `lib.opal_naming.address("bloomberg","global","bronze","demand_ledger","dt=<day>")`)
measures 5,858 history cells drawn in a day. R1: the reserve becomes the ledger's measured daily history draw plus a margin, recomputed
from the ledger, never typed. If the allowance (ceiling - reserve) cannot hold it, the quote says so -- it never lets a backfill take
production's cells.

**Build:**
1. `data/mdpf/scripts/demque/ceiling_from_ledger.py` (read it): add `--write-reserve <channel>` (and a `reserve_from_ledger(rows,
   channel, margin)` function): reserve value = round(the largest single-day `cells` sum for that channel x (1 + margin)), margin
   stated (default 0.25, overridable by `--margin`), written to `<channel>.reserve` as `{"value", "claim": "held", "basis"}`, the basis
   naming the ledger day and object read and the margin. Run it for `history`.
2. `data/mdpf/scripts/demque/reserve_estimate.py`: its `--write` never lowers a reserve whose basis names the demand ledger.
3. NEW `data/mdpf/scripts/demque/test_demque_reserve_ledger.py` (pytest; stub ledger rows, no S3) with exactly these names:
   `test_history_reserve_is_measured_daily_draw_plus_margin`, `test_reserve_carries_claim_held_and_ledger_basis`,
   `test_quote_names_allowance_not_positive_when_reserve_meets_ceiling` (this one calls the existing `bbg_quote.quote()`; do not edit
   `bbg_quote.py`). Keep the existing `test_demque_*.py` passing.
4. Report the history quote after the write (`python data/mdpf/scripts/demque/bbg_quote.py --quote
   org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json`), verbatim, including its `allowance_gap` if any.
   A non-positive allowance is a finding with its numbers, not a failure of this order.

### ACCEPTANCE

<criterion id="DQ6-t20-AC1" cell_refs="DQ-t-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t20_tests.py</invocation><expect>RSV-OK</expect></criterion>
<criterion id="DQ6-t20-AC2" cell_refs="DQ-t-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t20_seam.py</invocation><expect>RSVL-OK</expect></criterion>
`DQ6-t20-AC1` -- the three named tests. `DQ6-t20-AC2` -- the committed `history.reserve` reads at or above the ledger's measured draw.

<expected_criteria>DQ6-t20-AC1,DQ6-t20-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `RSV-BAD no file ...`, `RSVL-BAD reserve 40 vs measured 5858`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Bloomberg call, no deploy.** The demand ledger is read only.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W17-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/ceiling_from_ledger.py
data/mdpf/scripts/demque/reserve_estimate.py
data/mdpf/scripts/demque/bbg_allowance.json
data/mdpf/scripts/demque/test_demque_reserve_ledger.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 6), cell `DQ-t-20`.
<owned_cells>DQ-t-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ6-t20-AC1, DQ6-t20-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~17/MDPF_DEMQUE.TO-DQ-t20.history-reserve-from-ledger.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ6-t20-AC1,DQ6-t20-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the allowance figures written, the history quote verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the ledger read uses the seat's existing S3 read.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code and a config file.
risk: LOCAL -- code, config and tests; the served ledger is read only.
direct_act: false -- a worker order.
</preflight>

Source: PRD FWD-3, C-RESERVE; CTO round-5 analysis @7732d73c04 R1; row D1-W13-S1; decomposition round 6.
