# TO MDPF_DEMQUE.TO-DQ-t75 -- DQ-t-75: one empty Bloomberg window is skipped for seven days; it no longer stops the whole fire (row MDPF_DEMQUE-Z-S6)
<to_id>MDPF_DEMQUE.TO-DQ-t75</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~65</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>EMPTYWIN</workstream>
**GO (issuer, 2026-10-17 ~15:2xZ):** `TO-DQ-t74` is merged @0e5d1578e7; this order is pending, same worker continued.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-75` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 36) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-74

---

## WORKER FACE

### THE CELL

The 2026-10-17 14:00Z fire STOPPED when one security-window returned zero rows: `/cusip/78658RKQ3 2022-11-22..2023-05-26`. `data/mdpf/scripts/demque/standing_drawer.py` (`_draw_history`, about line 861) ends the whole run on `if not returned or any(any(f not in row for f in fields) ...)` with `res["stop"] = "EMPTY_OR_INCOMPLETE_RESPONSE"`. A security that stores no rows keeps the same cursor, so the next fire asks the same window first and stops again, and every request ranked behind it starves. The CTO ruled (`1.0.0_SA_CTO~DELL1` msg 7589):

1. **An EMPTY return for one security-window** (the call returned, the security is present, zero rows) is SKIPPED for **7 days** and listed in the receipt; the run CONTINUES with the next security.
2. **An INCOMPLETE return** (rows present but a requested field missing), a vendor limit refusal, an entitlement refusal, a diagnostic, an out-of-window or duplicate date, and an over-cap response STILL stop the run, exactly as today.
3. **Guard:** if MORE THAN 5 windows return EMPTY in ONE fire, STOP that fire with `stop` `EMPTY_OR_INCOMPLETE_RESPONSE` (many empties in a row look like an outage or a broken query). The five already skipped are still recorded.
4. **A cooled window gets ONE retry after 7 days.** If it is empty again it is listed as a STANDING GAP (still skipped; listed in every receipt, no further retry until the issuer clears it).

**Where the cooldown lives.** Reuse the device-state home the Yahoo FAILED_EMPTY cooldown (DQ-t-72, `inactive_request.py` and the pacer state under `~/.opal/demque`) uses, if its record shape generalizes to a (request_id, security identifier, window start, window stop) key with a first-empty UTC date and a retry count; else a small JSON file in the same directory with an atomic write (write a temp file, then replace). The location comes from the same function the existing state uses (no hand-typed path; tests pass a `tmp_path`). The key uses the identifier the drawer already draws with (`bloomberg_id`), never an account number. A cooled window is skipped BEFORE the draw call (it costs no cell and no request).

**Receipt.** The run result and the receipt gain `"empty_windows": [{"request_id", "security", "start", "stop", "state"}]` with `state` one of `COOLED_NEW` (first empty this fire), `COOLED` (skipped, inside its 7 days), `RETRIED_EMPTY_STANDING_GAP`. An empty window draws zero cells, writes no rows and adds no actuals cells; the request's `request_complete` rule is unchanged.

Read first, in full: `standing_drawer.py` (`_draw_history`, the draw loop, the receipt/marker writers), `inactive_request.py` and the Yahoo empty-cooldown code of `DQ-t-72` with its tests (`test_demque_empty_cooldown.py`), and the fixtures of `test_demque_standing_drawer.py` and `test_demque_outcome_per_request.py` (stub client, `tmp_path`).

**Build**
1. The change above in `standing_drawer.py` (and the shared cooldown helper if reusing one); a short comment naming this cell.
2. NEW `data/mdpf/scripts/demque/test_demque_empty_window.py` (pytest, `tmp_path`, stub client, no network) with EXACTLY these names:
   - `test_an_empty_window_is_skipped_and_the_run_continues_to_the_next_security` -- security 1's call returns zero rows, security 2's returns rows: the run does NOT stop, security 2's cells are drawn, the receipt lists security 1 as `COOLED_NEW`.
   - `test_a_cooled_window_is_not_asked_again_for_seven_days_and_is_asked_once_after` -- a second fire 1 to 6 days later makes NO vendor call for that window (the stub records calls); on day 7 or later it is asked once; if it returns rows they are stored and the cooldown record clears.
   - `test_more_than_five_empty_windows_in_one_fire_stop_the_run` -- six distinct empty windows in one fire: the run result is `STOPPED` with `EMPTY_OR_INCOMPLETE_RESPONSE`; five empties do NOT stop it.
   - `test_an_incomplete_row_or_a_refusal_still_stops_the_run` -- a response whose rows lack a requested field stops the run with `EMPTY_OR_INCOMPLETE_RESPONSE`; a refusal still stops as before.
   - `test_the_receipt_lists_empty_windows_and_a_second_empty_makes_a_standing_gap` -- after the retry returns empty again the window is listed `RETRIED_EMPTY_STANDING_GAP` and is not retried a third time.
   Edit an existing test ONLY if it fails because it pins the old rule (an empty response stops the run); name each edit and why in your report. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (known base failures: 4 failed and 8 collection errors from the missing `integrations/` and `commonwealth_signs`; report the counts).
3. **Report** the files, the two criteria's output, where the cooldown lives, every edited existing test and why, the folder count, and commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t75-AC1" cell_refs="DQ-t-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t75_tests.py</invocation><expect>EMPTY-OK</expect></criterion>
<criterion id="DQ9-t75-AC2" cell_refs="DQ-t-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t75_regress.py</invocation><expect>EMPTY-OK</expect></criterion>

<expected_criteria>DQ9-t75-AC1,DQ9-t75-AC2</expected_criteria>

`DQ9-t75-AC1` -- the five named tests. `DQ9-t75-AC2` -- the DIFFERENCE CONTROL: the drawer's existing tests, the surface-room tests and the DQ-t-74 outcome tests pass unedited. Run each invocation from the worktree root. At the base (after `TO-DQ-t74` has merged): `EMPTY-BAD no file ...test_demque_empty_window.py`; AC2 reads `EMPTY-OK` (a control that must keep passing).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw (`--apply` is not run).** Tests write only under `tmp_path`. Change no request file, no allowance value, no quote file, and not the trading-day gate. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W65-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/inactive_request.py
data/mdpf/scripts/demque/test_demque_empty_window.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 36), cell `DQ-t-75`.
<owned_cells>DQ-t-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t75-AC1, DQ9-t75-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~65/MDPF_DEMQUE.TO-DQ-t75.empty-window-cooldown.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t75-AC1,DQ9-t75-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the two checks' output, where the cooldown lives, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the site Z task already fires daily).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests and an unedited-suite control.
risk: LOCAL -- code and tests on dell1; the change reaches site Z only when it reaches CLOUD and the site Z checkout pulls it.
direct_act: true -- one cell, about 120 changed lines plus a test file.
</preflight>

Source: site Z row MDPF_DEMQUE-Z-S6 (`0.7.0_AE_CloudOps~MDPF1`, 2026-10-17 14:10Z; relayed by 0.0.0_AB_MSTR~DELL1 msg 7576); CTO ruling msg 7589 (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~14:2xZ): YES to the 7-day empty-window cooldown with a stop if more than 5 windows return empty in one fire. Issuer and disarm owner: `2.0.0_SA_COO~Q1`.
