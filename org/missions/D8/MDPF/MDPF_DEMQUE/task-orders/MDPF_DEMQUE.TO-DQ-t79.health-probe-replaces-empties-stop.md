# TO MDPF_DEMQUE.TO-DQ-t79 -- DQ-t-79: a health probe replaces the more-than-5-empties stop (row MDPF_DEMQUE-Z-S10)
<to_id>MDPF_DEMQUE.TO-DQ-t79</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~68</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>HEALTHPROBE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-79` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 39) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-75, DQ-t-76, DQ-t-77 (merged)

---

## WORKER FACE

### THE CELL

The first 16:00 ET sweep (2026-10-19) had 2,481,016 cells of room and drew 606. It stopped on its SIXTH empty window: DQ-t-75's guard in `data/mdpf/scripts/demque/standing_drawer.py` stops a fire with `EMPTY_OR_INCOMPLETE_RESPONSE` when more than 5 windows return empty in one fire (`EMPTY_WINDOW_STOP_AT = 5`, `_empty_window`). The six were sparse bonds and funds, not an outage: the history identifier-form probe had VERIFIED on a priced security in the same fire. `1.0.0_SA_CTO~DELL1` ruled (msg 8524) that a HEALTH PROBE replaces that stop, with three bounds. **This cell implements it, in both passes (the 14:00Z fire and the sweep).**

**THE RULE (implement exactly this):**
1. **Trigger:** when the empty-window count of the fire passes `EMPTY_WINDOW_STOP_AT` (the 6th empty window, and again each time it passes it after a reset), the drawer runs ONE health probe instead of stopping.
2. **The probe:** a history request for ONE security known to be priced, `HEALTH_PROBE_IDENT = "/cusip/037833100"`, field `PX_LAST`, ONE day: the previous NYSE trading day before the fire day (`lib/trading_calendar.py`). It goes through the same client call path as a draw and COUNTS AGAINST THE FIRE'S BUDGET like any draw: its cells are added to the fire's `cells` and to the room spent (the surface room of the request being drawn in the default pass; `daily_total_left` in the sweep), and it is recorded with `bbg_budget.record(mode=BUDGET_MODE, ...)` as every draw is.
3. **Rows back** (one row carrying `PX_LAST`): the channel is up; the empty counter RESETS to 0 and drawing continues with the next security.
4. **Empty, a missing field, or any error/refusal/diagnostic:** STOP the fire with `stop_reason` `OUTAGE`; the receipt names the probe's result.
5. **At most THREE health probes per fire.** A 4th trigger stops the fire with `stop_reason` `SPARSE-STOP` and the receipt names the empty windows of the fire.
6. **Receipt (both passes):** `health_probes`: a list in order of `{"identifier", "day", "rows", "verdict" (UP | OUTAGE), "why"}`; `empty_counts`: the number of empty windows per `request_id` this fire. The existing `empty_windows` list, the 7-day cooldown and the standing-gap rule of DQ-t-75 are unchanged; only the stop at more than 5 is replaced.
Change nothing else: the identifier-form probe (DQ-t-76), the outcome per request (DQ-t-74), the rooms, the sweep's room rule (DQ-t-77), the trading-day gate of the default pass, any request file.

Read first, in full: `standing_drawer.py` (`_empty_window`, `_cooldown_gate`, `_probe_history`, the history draw loop, `run`, the receipt writer), and the fixtures of `test_demque_empty_window.py`, `test_demque_probe_empty.py` and `test_demque_sweep.py` (stub client, `tmp_path`, `RIVALFUNDS_BBG_BUDGET_DIR` and `OPAL_DEMQUE_HOME` set to `tmp_path`).

**Build**
1. The change above in `standing_drawer.py`, with a comment naming this cell.
2. NEW `data/mdpf/scripts/demque/test_demque_health_probe.py` (pytest, `tmp_path`, stub client, no network) with EXACTLY these names:
   - `test_a_sixth_empty_window_runs_the_health_probe_and_a_priced_answer_keeps_drawing` -- six securities return empty, the health probe returns a priced row, a seventh security returns rows: the seventh is drawn, the run is not stopped, `health_probes` has one UP entry.
   - `test_an_empty_or_failed_health_probe_stops_the_fire_as_outage` -- the health probe returns empty (and, in a second case, raises): the fire stops `OUTAGE`, the receipt names the result, no further security is asked.
   - `test_a_fourth_trigger_stops_the_fire_as_sparse_stop_and_names_the_windows` -- 24 empty windows with every health probe UP: three probes run, the 4th trigger stops `SPARSE-STOP` and the receipt lists the windows.
   - `test_the_health_probe_counts_against_the_fire_and_the_receipt_lists_it` -- the probe's cells are in the fire's cells and in the budget ledger (mode `demque-backfill`), and `empty_counts` lists the empties per request.
   ONE existing test may be edited: `test_demque_empty_window.py::test_more_than_five_empty_windows_in_one_fire_stop_the_run` pins the stop this cell replaces; change it to assert the new behavior (its stub's health probe returns empty -> `OUTAGE`, or rows -> drawing continues) and say which in your report. Edit no other existing test unless it pins that same stop; name each edit. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (known base failures: 4 failed and 8 collection errors; report the counts).
3. **Report** the files, the two criteria's output, every edited existing test and why, the folder count, commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t79-AC1" cell_refs="DQ-t-79"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t79_tests.py</invocation><expect>HEALTH-OK</expect></criterion>
<criterion id="DQ9-t79-AC2" cell_refs="DQ-t-79"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t79_regress.py</invocation><expect>HEALTH-OK</expect></criterion>

<expected_criteria>DQ9-t79-AC1,DQ9-t79-AC2</expected_criteria>

`DQ9-t79-AC1` -- the four named tests. `DQ9-t79-AC2` -- the CONTROL: the drawer's existing tests and the DQ-t-69/74/75/76/77 tests pass, with the one permitted edit above. Run each from the worktree root. At the base: `HEALTH-BAD no file ...test_demque_health_probe.py`; AC2 reads `HEALTH-OK`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw; register no task.** Tests write only under `tmp_path`. Change no request file, allowance value or quote file. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W68-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_health_probe.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 39), cell `DQ-t-79`.
<owned_cells>DQ-t-79</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t79-AC1, DQ9-t79-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~68/MDPF_DEMQUE.TO-DQ-t79.health-probe-replaces-empties-stop.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t79-AC1,DQ9-t79-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the two checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests and a suite control.
risk: LOCAL -- code and tests on dell1; it reaches site Z through CLOUD and site Z's box pass. It replaces one stop with a bounded probe (at most three per fire) that still stops on an outage.
direct_act: true -- one cell, about 80 changed lines plus a test file.
</preflight>

Source: site Z row MDPF_DEMQUE-Z-S10 (`0.7.0_AE_CloudOps~MDPF1`, receipt `receipt.2026-10-19.sweep.json` on box/sitez: room 2,481,016, drawn 606, six empty windows, history probe VERIFIED); `1.0.0_SA_CTO~DELL1` ruling msg 8524 (2026-10-19 ~20:2xZ). The known-good security `/cusip/037833100` returned PX_LAST 343.46 for 2026-10-16 in the Terminal seat's read-only measure (relayed msg 8088). Issuer: `2.0.0_SA_COO~Q1`.
