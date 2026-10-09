# TO MDPF_DEMQUE.TO-DQ-t22 -- round 7 DQ-t-22: a history backfill is quoted over non-trading days at the measured ceiling
<to_id>MDPF_DEMQUE.TO-DQ-t22</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~19</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-22` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 7 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-22` (FWD-3, FWD-4; CTO round-6 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round6.md` R1, read it). Today the
history allowance is ceiling 5,858 (held) minus reserve 7,322 = negative, so every history quote reads `finish_date: null`. R1: production
draws history only on TRADING days, and a trading day has already drawn 5,858 history cells with no vendor limit hit, so 5,858 a day is
MEASURED drawable capacity. A history backfill is quoted against the coming NON-trading days (weekends and market holidays, from
`lib/trading_calendar.py` `is_trading_day`), at most the ceiling per day; on a trading day its allowance is 0. Production is never touched.

**Build:**
1. `data/mdpf/scripts/demque/ceiling_from_ledger.py`: the history ceiling it writes carries claim `measured` (the ledger's largest day,
   a completed draw with no limit warning), its basis naming the day and object. Run its `--write` so `bbg_allowance.json`'s
   `history.ceiling` reads `{"value": 5858, "claim": "measured", "basis": ...}`. Other channels unchanged.
2. `data/mdpf/scripts/demque/bbg_quote.py` (read it): for channel `history`, the finish date walks calendar days from `today`, adding
   the ceiling on each NON-trading day and 0 on each trading day, until the cells are covered (`today` counts if it is a non-trading
   day). The quote gains `allowance_today` (the ceiling minus what is drawn today on a non-trading day; 0 on a trading day) and names
   the rule in a `basis` line. `finish_date_claim` follows the figures' claims. Other channels unchanged. The CLI gains `--today
   YYYY-MM-DD` (default today).
3. NEW `data/mdpf/scripts/demque/test_demque_nontrading.py` (pytest; no network) with exactly these names:
   `test_history_backfill_quoted_on_non_trading_days_at_ceiling`, `test_trading_day_backfill_allowance_is_zero`,
   `test_history_ceiling_claim_measured_from_ledger`. Keep every existing `test_demque_*.py` passing.

### ACCEPTANCE

<criterion id="DQ7-t22-AC1" cell_refs="DQ-t-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t22_tests.py</invocation><expect>NTD-OK</expect></criterion>
<criterion id="DQ7-t22-AC2" cell_refs="DQ-t-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t22_quote.py</invocation><expect>NTDQ-OK</expect></criterion>
`DQ7-t22-AC1` -- the three named tests. `DQ7-t22-AC2` -- the REAL 15,720-cell request: finish 2026-10-17 quoted on 2026-10-09 with 0
drawable that (trading) day and ceiling claim `measured`; 5,858 drawable on Saturday 2026-10-10.

<expected_criteria>DQ7-t22-AC1,DQ7-t22-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `NTD-BAD no file ...`; the quote check fails (`--today` unrecognized).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Bloomberg call, no deploy.** The demand ledger is read only.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W19-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/ceiling_from_ledger.py
data/mdpf/scripts/demque/bbg_allowance.json
data/mdpf/scripts/demque/test_demque_nontrading.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 7), cell `DQ-t-22`.
<owned_cells>DQ-t-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ7-t22-AC1, DQ7-t22-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~19/MDPF_DEMQUE.TO-DQ-t22.history-on-nontrading-days.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ7-t22-AC1,DQ7-t22-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the two quotes verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the ledger read uses the seat's existing S3 read.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL quote code and a config file.
risk: LOCAL -- code, config and tests.
direct_act: false -- a worker order.
</preflight>

Source: PRD FWD-3, FWD-4, C-RESERVE; CTO round-6 analysis @4f7ded8845 R1; row D1-W17-S1; decomposition round 7.
