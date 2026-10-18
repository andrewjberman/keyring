# TO MDPF_DEMQUE.TO-DQ-t76 -- DQ-t-76: an EMPTY probe is the security's answer, not the identifier form's; the next /cusip/ security probes the form (row MDPF_DEMQUE-Z-S8)
<to_id>MDPF_DEMQUE.TO-DQ-t76</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~66</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PROBEEMPTY</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-76` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 37) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-56 (the probe), DQ-t-75 (the empty-window cooldown; merged)

---

## WORKER FACE

### THE CELL

The 2026-10-18 14:00Z fire drew 0 history cells. The standing drawer verifies the `/cusip/` identifier form with a ONE-ROW PROBE of the FIRST `/cusip/` security it meets, caches the verdict for the whole run (`_identifier_form`, `data/mdpf/scripts/demque/standing_drawer.py`, about line 757), and REFUSES every request of that form when the verdict is not VERIFIED. The probe security that day, `/cusip/662858FV6`, is a municipal bond that carries no `PX_LAST` on this channel (the Bloomberg Terminal seat measured it read-only: sign-in fine, entitlement fine, and `/cusip/037833100` returns PX_LAST 343.46 for 2026-10-16, so the form works). Its history is `[]`, the probe returned "probe response empty", and one unpriceable security therefore refused every history request of the fire.

**An EMPTY probe answers a question about the SECURITY, not about the identifier form.** Fix, in `standing_drawer.py` only:
1. **A new probe verdict `INCONCLUSIVE`** for exactly these two causes: the history probe's "probe response empty" and the reference probe's "probe value for <field> is empty". Every other UNVERIFIED cause stays UNVERIFIED and refuses the request exactly as today: "probe errored", "probe response named X, not Y", "probe row carries no <field> on <day>", "probe security error".
2. **On INCONCLUSIVE the verdict is NOT cached.** The probed security is skipped for this fire (it draws nothing further, costs no more cells) and is recorded as an empty window by the DQ-t-75 mechanism (`COOLED_NEW`, seven days, listed in the receipt's `empty_windows`, counted toward the more-than-5-empties stop). The run goes on to the NEXT `/cusip/` security of the queue, which probes the form.
3. **At most THREE probes per channel per run.** If a probe returns VERIFIED the verdict is cached for the run as today. If three distinct securities in a row are INCONCLUSIVE, the form is cached `UNVERIFIED` with the reason `three probes empty` and the request is refused as today.
4. The probe's own cells are counted exactly as today (`probe_cells`). Change nothing else: the room, the budgets, the trading-day gate, the outcome rule of DQ-t-74, the cooldown of DQ-t-75, any request file.

Read first, in full: `standing_drawer.py` (`_probe_history`, `_probe_reference`, `_identifier_form`, the two call sites near lines 889 and 993, and the DQ-t-75 helpers `_cooldown_gate`, `_empty_window`, `_list_window`), and the fixtures of `test_demque_empty_window.py` and `test_demque_standing_drawer.py` (a stub client, `tmp_path`, `OPAL_DEMQUE_HOME` set to `tmp_path`).

**Build**
1. The change above in `standing_drawer.py`, with a short comment naming this cell.
2. NEW `data/mdpf/scripts/demque/test_demque_probe_empty.py` (pytest, `tmp_path`, stub client, no network, `OPAL_DEMQUE_HOME` set to `tmp_path`) with EXACTLY these names:
   - `test_an_empty_probe_security_is_skipped_and_the_next_cusip_security_verifies_the_form` -- a `/cusip/` request whose first security's probe returns an empty history and whose second security's probe returns a priced row: the form is VERIFIED, the second security draws, the first draws nothing and is listed `COOLED_NEW`; the run does not refuse.
   - `test_three_empty_probes_leave_the_form_unverified_and_refuse_the_request` -- three securities whose probes all return empty: the request is refused with the form UNVERIFIED (`three probes empty`), no further cells; a fourth security is NOT probed.
   - `test_a_probe_that_names_the_wrong_security_or_errors_still_leaves_the_form_unverified` -- a probe response keyed by another identifier, and a probe that errors: each leaves the form UNVERIFIED and refuses the request, with the next security NOT probed (the old behavior kept).
   - `test_the_skipped_probe_security_is_listed_in_the_receipt_and_cooled_for_seven_days` -- the skipped security appears in `empty_windows` with `COOLED_NEW`, and a second fire inside seven days makes no vendor call for it.
   Edit an existing test ONLY if it fails because it pins the old rule (an empty probe refuses the request); name each edit and why in your report. Two existing tests, `test_drawer_draws_min_of_allowance_and_remaining_in_rank_order` and `test_no_zero_cell_drawn_line_after_completion`, fail on the days 2026-10-17 and 2026-10-18 only (the real date names the budget ledger file the fixture then reads); do NOT edit them and do not treat that as yours. Run the whole `data/mdpf/scripts/demque` folder once at the end: no failure that was not failing at the base (known base failures: 4 failed and 8 collection errors from the missing `integrations/` and `commonwealth_signs`, plus those two on those two dates; report the counts).
3. **Report** the files, the two criteria's output, every edited existing test and why, the folder count, and commits (never an account number).

### ACCEPTANCE

<criterion id="DQ9-t76-AC1" cell_refs="DQ-t-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t76_tests.py</invocation><expect>PROBE-OK</expect></criterion>
<criterion id="DQ9-t76-AC2" cell_refs="DQ-t-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t76_regress.py</invocation><expect>PROBE-OK</expect></criterion>

<expected_criteria>DQ9-t76-AC1,DQ9-t76-AC2</expected_criteria>

`DQ9-t76-AC1` -- the four named tests. `DQ9-t76-AC2` -- the DIFFERENCE CONTROL: the drawer's existing tests, the surface-room, DQ-t-74 outcome and DQ-t-75 empty-window tests pass unedited (the check deselects the two date-coupled tests on 2026-10-17 and 2026-10-18 only). Run each invocation from the worktree root. At the base: `PROBE-BAD no file ...test_demque_probe_empty.py`; AC2 reads `PROBE-OK` (a control that must keep passing).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger under `org/` or `~/.opal`, the queue state, the price store or any pacer state; run no draw (`--apply` is not run).** Tests write only under `tmp_path`. Change no request file, no allowance value, no quote file, and not the trading-day gate. Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W66-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_probe_empty.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 37), cell `DQ-t-76`.
<owned_cells>DQ-t-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t76-AC1, DQ9-t76-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~66/MDPF_DEMQUE.TO-DQ-t76.probe-empty-is-not-unverified.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t76-AC1,DQ9-t76-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the two checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the site Z task already fires daily).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE code graded by tests and an unedited-suite control.
risk: LOCAL -- code and tests on dell1; the change reaches site Z only when it reaches CLOUD and the site Z checkout pulls it. It relaxes one refusal (an EMPTY probe), keeps every other, and is bounded to three probes per channel per run.
direct_act: true -- one cell, about 80 changed lines plus a test file.
</preflight>

Source: site Z row MDPF_DEMQUE-Z-S8 and the Terminal seat's read-only measure (`0.0.3_BG_BBGTerminal`, site Z msg 35723, relayed by 0.0.0_AB_MSTR~DELL1 msg 8088): the probe security 662858FV6 is a municipal bond with no PX_LAST; sign-in, entitlement and the `/cusip/` form are not the cause. Issuer and disarm owner: `2.0.0_SA_COO~Q1`.
