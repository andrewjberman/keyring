# TO MDPF_DEMQUE.TO-DQ-t74 -- DQ-t-74: the standing drawer records each request's own outcome; a stop belongs to the request that caused it (row MDPF_DEMQUE-Z-S7)
<to_id>MDPF_DEMQUE.TO-DQ-t74</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~65</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>OUTCOMES</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-74` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 35) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-34 (the COMPLETE outcome), DQ-t-69 (merged)

---

## WORKER FACE

### THE CELL

The 2026-10-17 14:00Z fire of the standing drawer STOPPED in a surface-B request (an empty vendor response), after the TR request (`DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS`, surface D) had drawn its LAST 1,004 cells. The actuals ledger recorded TR as `STOPPED`, not `COMPLETE`, because `data/mdpf/scripts/demque/standing_drawer.py` decides every attempted request's outcome with `elif reason: outcome = "STOPPED"` BEFORE it asks `request_complete` (around lines 1063-1070). One request's stop therefore turns every request attempted earlier in the same run into `STOPPED`, and a request that was fully drawn can never read `COMPLETE` (a complete request is skipped at the start of later runs, so no later run writes the line).

**Fix, in `standing_drawer.py` only:** decide the outcome per attempted request, in attempt order:
1. `REFUSED` when the request's `got["refusal"]` is set (unchanged);
2. `COMPLETE` when `request_complete(req, stored)` is true (moved BEFORE the stop test: a request every security of which reached its end reads COMPLETE even in a run that stopped later, or at this request);
3. `STOPPED` when the run's stop `reason` came from THIS request, i.e. `got["stop"]` is set on this entry (the draw loop `break`s on the first stop, so at most one attempted request carries it);
4. `GATED` (unchanged rule: nothing drawn and every owed security excluded);
5. otherwise `DRAWN`.
A request attempted BEFORE the stopping request that is not complete reads `DRAWN` (it drew what it drew and did not stop the run). The RUN-level result is unchanged: any stop `reason` still makes the run `STOPPED` with its reason, and the receipt's `stop_reason` is unchanged. Where a request that stopped the run is ALSO complete (its last security reached its end in the stopping call), it reads COMPLETE. Change nothing else: not the draw order, rooms, budgets, the trading-day gate, or any request file.

Read first, in full: `data/mdpf/scripts/demque/standing_drawer.py` (the module docstring, `run`, the outcome loop `for entry, got in attempted:`, `request_complete`, `_draw_history`) and the fixtures of `data/mdpf/scripts/demque/test_demque_standing_drawer_close.py` and `test_demque_standing_drawer.py` (a stub client, `tmp_path`, a monkeypatched budget directory and priority gate; copy that shape).

**Build**
1. The change above in `standing_drawer.py`; a two-line comment naming this cell.
2. NEW `data/mdpf/scripts/demque/test_demque_outcome_per_request.py` (pytest, `tmp_path`, stub client, no network) with EXACTLY these names:
   - `test_a_request_drawn_complete_before_a_later_requests_stop_is_recorded_complete` -- two requests on a Saturday fixture: request 1 small enough to complete in the run; request 2 makes the stub return an EMPTY response (so the run stops). The actuals lines: request 1 `COMPLETE` with cells_drawn > 0, request 2 `STOPPED`.
   - `test_the_request_that_stopped_the_run_is_recorded_stopped_even_with_cells_drawn` -- request 1 draws some cells but is not complete, then a second call of the same request returns EMPTY: its line is `STOPPED` with its cells; an earlier incomplete request that drew and did not stop the run reads `DRAWN`.
   - `test_a_run_that_stops_still_reports_the_run_as_stopped_and_names_the_reason` -- the run result has `outcome == "STOPPED"` and the stop reason `EMPTY_OR_INCOMPLETE_RESPONSE`.
   Edit an existing test ONLY if it fails because it pins the old rule (an earlier request STOPPED by a later one); name each edit and why in your report. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (known base failures: 4 failed and 8 collection errors from the missing `integrations/` and `commonwealth_signs`; report the counts).
3. **Report** the files, the two criteria's output, every edited existing test and why, the folder count, and commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t74-AC1" cell_refs="DQ-t-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t74_tests.py</invocation><expect>OUT-OK</expect></criterion>
<criterion id="DQ9-t74-AC2" cell_refs="DQ-t-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t74_regress.py</invocation><expect>OUT-OK</expect></criterion>

<expected_criteria>DQ9-t74-AC1,DQ9-t74-AC2</expected_criteria>

`DQ9-t74-AC1` -- the three named tests. `DQ9-t74-AC2` -- the DIFFERENCE CONTROL: the drawer's existing tests (`test_demque_standing_drawer.py`, `test_demque_standing_drawer_close.py`) and `test_demque_surface_room.py` pass unedited. Run each invocation from the worktree root. At the base: `OUT-BAD no file ...test_demque_outcome_per_request.py`; AC2 reads `OUT-OK` at the base (a control that must keep passing).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw (`--apply` is not run).** Change no request file, no allowance value, no quote file. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W65-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_outcome_per_request.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 35), cell `DQ-t-74`.
<owned_cells>DQ-t-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t74-AC1, DQ9-t74-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~65/MDPF_DEMQUE.TO-DQ-t74.outcome-per-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t74-AC1,DQ9-t74-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the two checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the site Z task already fires daily).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests and an unedited-suite control.
risk: LOCAL -- code and tests on dell1; the change reaches site Z only when it reaches CLOUD and the site Z checkout pulls it.
direct_act: true -- one cell, about 40 changed lines plus a test file.
</preflight>

Source: site Z row MDPF_DEMQUE-Z-S7 (`0.7.0_AE_CloudOps~MDPF1`, 2026-10-17 14:10Z; relayed by 0.0.0_AB_MSTR~DELL1 msg 7576): the 14:00Z fire's receipt `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/receipt.2026-10-17.json`. Issuer and disarm owner: `2.0.0_SA_COO~Q1`.
