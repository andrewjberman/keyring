# TO MDPF_DEMQUE.TO-DQ-t72 -- round 9 DQ-t-72: a Yahoo symbol that returned EMPTY is not requested again for 7 days (138 of run 2's 200 requests went to symbols already known empty)
<to_id>MDPF_DEMQUE.TO-DQ-t72</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~62</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>EMPTYCOOL</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-72` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 31) |
**outcome_ref:** C-PRICES, C-YAHOO | **depends_on:** DQ-t-71 (merged)

---

## WORKER FACE

### THE CELL

The second manual Yahoo run (cap 600) spent 138 of its 200 added requests on symbols the pacer already holds as `FAILED_EMPTY` (158 in all: real tickers of delisted or acquired securities, such as AEPI, AKS and ANR, that Yahoo answers with an empty frame). `yahoo_pull.Pacer.done` skips only a symbol whose last outcome is `OK`, so every run asks the vendor again. Those requests cost budget and produce no price. **This cell makes a symbol that returned EMPTY within the last 7 days cost no request.** It touches no store key, no identity rule, no gate and no request file: a pure change in which symbols the pacer asks for.
It makes no vendor call and writes nothing to S3, the queue or any pacer state.

**Build** (read `yahoo_pull.py` in full: `Pacer`, `record`, `done`, `run`, `pull`, the status constants; import, do not copy; under data/mdpf/scripts/demque/):
1. `yahoo_pull.py`: a module constant `EMPTY_COOLDOWN_DAYS = 7`.
2. `Pacer.cooling(symbol, now=None) -> bool`: True when the symbol's stored outcome is exactly `FAILED_EMPTY` and its `last_attempt` (UTC, format `%Y-%m-%dT%H:%M:%SZ`) is less than `EMPTY_COOLDOWN_DAYS` days before `now` (default the current UTC time). A missing or unparsable `last_attempt`, any other outcome (`OK`, `FAILED_REFUSED`, `STOPPED_PUSHBACK`) and an unknown symbol are NOT cooling. `done` is unchanged.
3. `run(symbols, pacer, fetch=None)`: a symbol for which `pacer.cooling(sym)` is True is skipped BEFORE `pacer.allow()` and before `pacer.wait()`: no request, no count, no gap wait, nothing appended to the result list. Everything else in `run` is unchanged, including the stop on `allow()` False and on pushback.
4. **Tests** in a NEW `test_demque_empty_cooldown.py` (pytest; a temp state file, a stub fetch, no network, a no-op sleep) with exactly these names:
   `test_a_symbol_that_returned_empty_within_the_cooldown_is_not_requested_again_and_uses_no_budget`,
   `test_a_symbol_that_returned_empty_before_the_cooldown_is_requested_again`,
   `test_an_ok_symbol_and_a_new_symbol_behave_as_before_and_a_pushback_still_stops_the_run`.
   Edit an existing test ONLY if it fails because it re-asks a symbol with a recent `FAILED_EMPTY` (stub declaration or one assertion); name each edit and why in your report. Run the whole folder once: no failure.
5. **Report** the folder count and the diff stat (the source diff is the constant, one method and three lines in `run`).

### ACCEPTANCE

<criterion id="DQ9-t72-AC1" cell_refs="DQ-t-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t72_tests.py</invocation><expect>COOLT-OK</expect></criterion>
<criterion id="DQ9-t72-AC2" cell_refs="DQ-t-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t72_check.py</invocation><expect>COOL-OK</expect></criterion>
`DQ9-t72-AC1` -- the three named tests. `DQ9-t72-AC2` -- on a temp pacer state: a symbol empty an hour ago is not requested, one empty 8 days ago is, an OK symbol is not, a new one is; the stub is called for exactly two symbols and the pacer count rises by exactly two; `EMPTY_COOLDOWN_DAYS` is 7.

<expected_criteria>DQ9-t72-AC1,DQ9-t72-AC2</expected_criteria>

Run each invocation from the worktree root (AC2 needs `PYTHONPATH=.` in the shell, not in the recorded invocation). At the base: `COOLT-BAD no file ...test_demque_empty_cooldown.py`; `COOL-BAD yahoo_pull.EMPTY_COOLDOWN_DAYS is None, not 7`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state (`~/.opal/demque`); run no draw.** Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W62-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/yahoo_pull.py
data/mdpf/scripts/demque/test_demque_empty_cooldown.py
data/mdpf/scripts/demque/test_demque_yahoo.py
data/mdpf/scripts/demque/test_demque_queue.py
data/mdpf/scripts/demque/test_demque_batch_pull.py
data/mdpf/scripts/demque/test_demque_pacer_cap.py
data/mdpf/scripts/demque/test_demque_symbol_forms.py
data/mdpf/scripts/demque/test_demque_redraw_stale.py
data/mdpf/scripts/demque/test_demque_incremental_wiring.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-72`.
<owned_cells>DQ-t-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t72-AC1, DQ9-t72-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~62/MDPF_DEMQUE.TO-DQ-t72.yahoo-empty-symbol-cooldown.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t72-AC1,DQ9-t72-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, both checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE one pacer rule graded by tests and a temp-state check.
risk: LOCAL -- code and tests; the change only removes requests the pacer would have made for symbols known empty, so it writes no key the signed never-widen pair does not already cover and moves none that run 2 did not.
direct_act: true -- one cell, about twenty changed lines.
</preflight>

Source: the 2026-10-15 second manual run's receipt (200 added requests, 138 on `FAILED_EMPTY` symbols, 0 pushback); decomposition round 9, amendment 31.
