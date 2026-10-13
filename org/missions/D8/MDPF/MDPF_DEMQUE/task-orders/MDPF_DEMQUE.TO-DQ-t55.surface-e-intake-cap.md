# TO MDPF_DEMQUE.TO-DQ-t55 -- round 9 DQ-t-55: surface E has a turnaround CAP -- a request above 10 percent of the day's history allowance is REFUSED at intake naming the cap, never split
<to_id>MDPF_DEMQUE.TO-DQ-t55</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~47</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SURFACEECAP</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-55` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 18) |
**outcome_ref:** C-RESERVE, C-PRIORITY, FWD-3, FWD-4 | **depends_on:** DQ-t-44 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct ~20:0xZ 2026-10-13 (CTO msgs 5130 and 5134; [the queue form](file:///C:/dev/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md), the ~20:0xZ section):
**Surface E (Opal ad-hoc, requests through the Opal agent) has NO oversized requests.** A CAP on what can be turned around; a request above it is **refused at intake, never split.** The cap is the
day's surface E reserve: **10 percent of that day's history allowance**, a STARTING value that Andrew sees on the surface E card and may raise. It is enforced at the gateway by NFRA_OPLGTW; this cell
builds DEMQUE's side: the cap function, the intake check and the cost print. **The day's history allowance is the measured history ceiling in `bbg_allowance.json` (5,858 cells a day), NOT the 2,673
a-day averaged rate used in the P1 depth cuts: the cap is 585 cells.** This cell makes no vendor call and writes nothing.

**Build** (NEW `data/mdpf/scripts/demque/surface_e_intake.py`; read `bbg_quote.py` (`quote`, the allowance loader `ALLOWANCE_PATH`, `_figure`, `_trading_days`), `bbg_allowance.json` and `lib/trading_calendar.py` first):
1. **`cap(day=None, allowance=None) -> int`**: `(history_ceiling * 10) // 100` where `history_ceiling` is the allowance file's `history.ceiling.value` (an int); the percentage is one named constant `SURFACE_E_PERCENT = 10`. If the ceiling's claim is not `measured` the cap is still computed from the held figure and the result carries `claim`.
2. **`check(cells, day=None) -> dict`**: `{"day", "history_allowance", "cap", "cells", "verdict": "ACCEPT" | "REFUSE", "message", "remaining_reserve"}`; REFUSE when `cells > cap`, with the exact message
   `request of <cells> cells is above the surface E cap of <cap> cells (10 percent of the <allowance>-cell history allowance): refused at intake, not split`; ACCEPT carries `remaining_reserve` = `cap - cells`.
   It never splits a request, never writes a file and never records a spend.
3. **`cost(securities, trading_days, fields)`** = `securities * trading_days * fields` (a history request's cells, as `bbg_quote` prices a single window).
4. **CLI:** `--cost --securities N --trading-days D --fields F --day DAY` prints ONE JSON line `{"day", "history_allowance", "cap", "cells", "verdict", "message"}` (the check of the cost);
   `--check --cells N --day DAY` prints the same line for a given cell count. Both read the allowance file only.
5. NEW `test_demque_surface_e_cap.py` (pytest; a stub allowance, no network) with exactly these names:
   `test_the_cap_is_ten_percent_of_the_days_history_allowance_and_a_request_above_it_is_refused_naming_the_cap`,
   `test_a_request_at_or_below_the_cap_is_accepted_and_the_remaining_reserve_is_printed`,
   `test_a_refused_request_is_never_split_and_writes_nothing`.

### ACCEPTANCE

<criterion id="DQ9-t55-AC1" cell_refs="DQ-t-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t55_tests.py</invocation><expect>CAP-OK</expect></criterion>
<criterion id="DQ9-t55-AC2" cell_refs="DQ-t-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t55_real.py</invocation><expect>CAP-REAL-OK</expect></criterion>
`DQ9-t55-AC1` -- the three named tests. `DQ9-t55-AC2` -- against the real allowance file: the cap is 10 percent of the measured history ceiling (585 of 5,858), the cost of a one-security one-year
(252 trading days) two-field request is 504 cells and is ACCEPTed under it, 100 cells is accepted, cap + 1 cells is refused naming the cap. Print in your report what a one-security, one-year,
two-field request costs against the cap. Report the whole folder `pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t55-AC1,DQ9-t55-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `CAP-BAD no file ...`; `CAP-REAL-BAD no file ...surface_e_intake.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue or any pacer state; no AWS write; no deploy; no timer.** Build no alarm, monitor or notification (standing moratorium).
  The gateway side (NFRA_OPLGTW) is NOT in this cell: do not edit any file outside the grant.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W47-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY. Do NOT merge `box/dell1` (it is blocked by a foreign row);
  append your rows at the end of your own branch's copy and the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/surface_e_intake.py
data/mdpf/scripts/demque/test_demque_surface_e_cap.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-55`.
<owned_cells>DQ-t-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t55-AC1, DQ9-t55-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~47/MDPF_DEMQUE.TO-DQ-t55.surface-e-intake-cap.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t55-AC1,DQ9-t55-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--cost` line verbatim, what a one-security one-year two-field request costs against the cap, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS access; the allowance file is read from the repo.
comp-adversary: DECLARED-NOT-APPLICABLE a pure cap function and a CLI over a repo file; the gateway enforcement is NFRA_OPLGTW's.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct ~20:0xZ 2026-10-13 via CTO msgs 5130, 5134; decomposition round 9.
