# TO MDPF_DEMQUE.TO-DQ-t71 -- round 9 DQ-t-71: the Yahoo pacer's daily cap steps 400 to 600 (CTO ruling msg 6379: one step, read pushback before any further step)
<to_id>MDPF_DEMQUE.TO-DQ-t71</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~61</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PACERCAP</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-71` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 30) |
**outcome_ref:** C-PRICES, C-YAHOO | **depends_on:** DQ-t-66, DQ-t-67 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-15 ("increase limits on all our pull surfaces"; "I am fine with pushing yahoo finance harder"), ruled by the CTO (msg 6379): the Yahoo pacer's daily request cap steps **400 to 600**, ONE step. Nothing else about the Yahoo leg changes: the identity lock, the V2 gate, the inactive-only rule, the per-request gap (8 to 12 seconds) and the pushback rule (a pushback doubles the next day's gap factor) stay exactly as they are. The cap is a default in three places; they must agree.
This order changes constants and the tests that pin them. It makes no vendor call and writes nothing to S3, the queue or any pacer state.

**Build** (read `yahoo_pull.py` `Pacer` in full; `extend_frontier.py` `DAILY_CAP`, `TIER2_RESERVE`, `_request_cap`, the module docstring; `inactive_request.py` `DAILY_CAP`; `daily_draw.py` where it builds its `Pacer`; all under data/mdpf/scripts/demque/):
1. `yahoo_pull.py`: `Pacer.__init__`'s `daily_cap` default `400` becomes `600`. Update any docstring or comment that states 400 as the default.
2. `extend_frontier.py`: `DAILY_CAP = 600` (its comment says it is the Pacer's default and the unit the quote and the draw count); the module docstring's CAP line follows. `TIER2_RESERVE` stays 20, so `_request_cap()` reads 580.
3. `inactive_request.py`: `DAILY_CAP = 600` (the same comment).
4. `daily_draw.py` is NOT edited: it builds `yp.Pacer(state)` with the default, and a test pins that it stays so.
5. **Tests.** A NEW `test_demque_pacer_cap.py` (pytest; a temp state file, no network) with exactly these names:
   `test_the_pacer_stops_a_draw_at_six_hundred_requests_and_not_before` (a Pacer on a temp state with a no-sleep clock admits 600 requests and refuses the 601st; at 599 it still admits),
   `test_the_standing_extension_request_cap_is_the_daily_cap_less_the_tier_two_reserve` (`extend_frontier._request_cap()` equals `extend_frontier.DAILY_CAP - extend_frontier.TIER2_RESERVE` equals 580).
   Existing tests that pin the old cap (for example `test_demque_yahoo_gate.py`, which pins 380 as the request cap and the refusal text "over the cap 380") are edited ONLY where the number is the cap: change 380 to 580 and nothing else. **Name every edited test and why in your report.** Run the whole folder once (`pytest data/mdpf/scripts/demque`): the four failures that need `integrations/` are absent from a sparse worktree and are not yours; there must be no other failure.
6. **Report** the folder count and the diff stat (the source diff is three one-line constant changes, plus any docstring line).

### ACCEPTANCE

<criterion id="DQ9-t71-AC1" cell_refs="DQ-t-71"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t71_tests.py</invocation><expect>CAP-OK</expect></criterion>
<criterion id="DQ9-t71-AC2" cell_refs="DQ-t-71"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t71_check.py</invocation><expect>PACER-OK</expect></criterion>
`DQ9-t71-AC1` -- the two named tests. `DQ9-t71-AC2` -- the Pacer default is 600, `extend_frontier.DAILY_CAP` is 600 with a request cap of 580, `inactive_request.DAILY_CAP` is 600, and `daily_draw.py` builds its Pacer once with the default.

<expected_criteria>DQ9-t71-AC1,DQ9-t71-AC2</expected_criteria>

Run each invocation from the worktree root (AC2 with `PYTHONPATH=.`). At the base: `CAP-BAD no file ...test_demque_pacer_cap.py`; `PACER-BAD Pacer default daily_cap is 400, not 600`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state (`~/.opal/demque`); run no draw.** Do not merge anything; the issuer drains. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W61-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`.

<paths>
data/mdpf/scripts/demque/yahoo_pull.py
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/inactive_request.py
data/mdpf/scripts/demque/test_demque_pacer_cap.py
data/mdpf/scripts/demque/test_demque_yahoo_gate.py
data/mdpf/scripts/demque/test_demque_rolling_tiers.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
data/mdpf/scripts/demque/test_demque_extend_guard.py
data/mdpf/scripts/demque/test_demque_extend_future.py
data/mdpf/scripts/demque/test_demque_lag_report.py
data/mdpf/scripts/demque/test_demque_yahoo_need_class.py
data/mdpf/scripts/demque/test_demque_priority_gate.py
data/mdpf/scripts/demque/test_demque_inactive_request.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-71`.
<owned_cells>DQ-t-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t71-AC1, DQ9-t71-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~61/MDPF_DEMQUE.TO-DQ-t71.yahoo-pacer-cap-600.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t71-AC1,DQ9-t71-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, both checks' output, every edited existing test and why, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE three constants and their tests.
risk: LOCAL -- code and tests; the runs that use the new cap are covered by the signed never-widen pair (the same keys, a bounded name set), and each is read on its receipt.
direct_act: true -- one cell, about ten changed lines.
</preflight>

Source: CTO ruling msg 6379 (Yahoo pacer cap 400 to 600, then read pushback before any further step); Andrew-direct 2026-10-15; decomposition round 9, amendment 30.
