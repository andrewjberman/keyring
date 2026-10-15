# TO MDPF_DEMQUE.TO-DQ-t66 -- round 9 DQ-t-66: the Yahoo leg's gate is the V2 active set (active names Bloomberg only, every other name may take Yahoo); unenrolled landed names roll
<to_id>MDPF_DEMQUE.TO-DQ-t66</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~58</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>YAHOOGATE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-66` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 29) |
**outcome_ref:** C-PRICES, C-YAHOO, C-PRIORITY, FWD-8 | **depends_on:** DQ-t-52, DQ-t-58, DQ-t-64, DQ-t-65 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-15 (CTO msg 6105, ruling amendment 1 @bed1cdb778): "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." **Active means the V2 set** (`active_set.py`, 860 accounts, 3,368 securities). Today the Yahoo leg (the daily draw and the standing extension) excludes the P2 (match open) and P3 (former client) names (DQ-t-52, Andrew-direct 2026-10-13). The new rule replaces that exclusion FOR THE YAHOO LEG ONLY: a name in V2 is never drawn or extended on Yahoo; every other name (P1, P2 or P3) may be. The Bloomberg side keeps the P2/P3 gate untouched (`b1_request.py` `excluded_names`, `priority_gate.excluded_for`, `priority_gate.excluded`, `classify`).
A second change is forced by the first. The extension puts every landed name that is not in the IRPT rolling request into the DAILY tier, and `_day` refuses over 380. Once ~1,000 inactive names land, the day's request would exceed 380 and the nightly extension (and with it the whole run) would fail. So **a landed name enrolled in no tier rolls**.
This order changes code the nightly run executes. It makes no vendor call and writes nothing to S3, the queue or any pacer; the issuer merges it only after the never-widen pair for this act is signed.

**Build** (read `priority_gate.py` in full; `daily_draw.py` `run` and its docstring; `extend_frontier.py` `_excluded_for`, `_tiers`, `plan`, `plan_week`, `_week`, `lag_report`, the module docstring; `demand_queue.py` `is_gated`, `gated`; `active_set.py` `load`; import, do not copy; all under data/mdpf/scripts/demque/):
1. **`priority_gate.py`**: `REASON_ACTIVE = "active account: Bloomberg only (Andrew-direct 2026-10-15)"`; `REASON_NO_CUSIP = "no cusip: nothing keys a store row for it"`; `yahoo_excluded(cusips, active) -> dict` (pure): `{cusip: REASON_ACTIVE}` for each cusip in `active` (a set or mapping), `{None: REASON_NO_CUSIP}` for a `None` cusip, nothing for any other; `yahoo_excluded_for(cusips) -> dict` over `active_set.load()`; if `active_set.load` raises (any exception or `SystemExit`) it raises `GateUnreadable` (fail closed), and an empty `cusips` returns `{}` without a read. `tally(excl, cusips)` keeps `excluded_p2` and `excluded_p3` and gains `excluded_active` (the count of `REASON_ACTIVE`). `excluded_for`, `excluded` and `classify` are UNCHANGED.
2. **`daily_draw.py`**: `run`'s default gate becomes `pg.yahoo_excluded_for`; the docstring says why. Everything else in `run` is unchanged.
3. **`extend_frontier.py`**: `_excluded_for` returns `pg.yahoo_excluded_for(cusips)`. Every JSON output that carries `excluded_p2` and `excluded_p3` keeps both (they now count 0) and gains `excluded_active` (`plan`, `plan_week`, `lag_report`). `_tiers`: **`daily`** = the known names that are in the stored-at-enrolment set or in a `daily_extra` request; **a known name in NO enrolled set (not stored at enrolment, not a daily_extra, not in the rolling request) is appended to the rolling cohort**, ranked with it (`_rank_order`) and cut into the same `cycle` blocks. Read the existing `_tiers` first: today `daily` is "every known name not in the rolling request, plus the landed extras"; your change moves only the never-enrolled names. `tiers` and `rolling_names` counts follow. The module docstring's TIERS and GATE paragraphs are updated.
4. **Tests.** A NEW `test_demque_yahoo_gate.py` (pytest; stub frames and injected gates, no network) with exactly these names:
   `test_the_yahoo_gate_excludes_exactly_the_active_set_names_and_no_p2_or_p3_name`,
   `test_a_landed_name_in_no_tier_joins_the_rolling_cohort_and_the_daily_tier_keeps_the_stored_at_enrolment_and_extras`,
   `test_the_day_request_stays_under_the_cap_with_a_thousand_landed_inactive_names`,
   `test_the_daily_draw_skips_an_active_name_of_a_client_request_and_draws_a_p2_name`.
   Nine existing test files mention the gate (`test_demque_drawer_cusip_entries.py`, `test_demque_extend_frontier.py`, `test_demque_extend_guard.py`, `test_demque_incremental_wiring.py`, `test_demque_lag_report.py`, `test_demque_extend_future.py`, `test_demque_priority_gate.py`, `test_demque_rolling_tiers.py`, `test_demque_yahoo_need_class.py`). Edit one ONLY where it pins the Yahoo gate's P2/P3 behaviour or the old daily-tier rule (a stub declaration or one assertion); the Bloomberg-side gate tests stay as they are. **Name every test you edit and why in your report.**
5. **Report** the folder count (`pytest data/mdpf/scripts/demque` once), the two real read-only lines (`extend_frontier.py --plan`, `extend_frontier.py --plan-week --from 2026-10-19 --days 10`) verbatim.

### ACCEPTANCE

<criterion id="DQ9-t66-AC1" cell_refs="DQ-t-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t66_tests.py</invocation><expect>GATE-OK</expect></criterion>
<criterion id="DQ9-t66-AC2" cell_refs="DQ-t-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t66_real.py</invocation><expect>GATE-REAL-OK</expect></criterion>
`DQ9-t66-AC1` -- the four named tests. `DQ9-t66-AC2` -- on the REAL store index and the V2 set (read only): `extend_frontier.py --plan` shows `excluded_active` above 0, no V2 CUSIP in the day's securities, 1 to 380 symbols, `excluded_p2` and `excluded_p3` both 0; `--plan-week` over 10 days shows `max_requests` at most 380.
The check runs two plans (about 30 s each): invoke it under `timeout 260`. At the base the plan prints `excluded_p2` 72 and `excluded_p3` 8.

<expected_criteria>DQ9-t66-AC1,DQ9-t66-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `GATE-BAD no file ...test_demque_yahoo_gate.py`; `GATE-REAL-BAD excluded_active is missing or not above 0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state; do NOT write into `org/missions/.../requests/`**; no AWS write; no deploy; no timer. Run no draw: `daily_draw.py` and `extend_frontier.py --apply` are NEVER run against the real home; only `--plan`, `--plan-week` and tests. Never print an account number. Build no alarm, monitor or notification. **Do not merge anything**; the issuer merges after the pair is signed.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W58-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/priority_gate.py
data/mdpf/scripts/demque/daily_draw.py
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_yahoo_gate.py
data/mdpf/scripts/demque/test_demque_drawer_cusip_entries.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
data/mdpf/scripts/demque/test_demque_extend_guard.py
data/mdpf/scripts/demque/test_demque_incremental_wiring.py
data/mdpf/scripts/demque/test_demque_lag_report.py
data/mdpf/scripts/demque/test_demque_extend_future.py
data/mdpf/scripts/demque/test_demque_priority_gate.py
data/mdpf/scripts/demque/test_demque_rolling_tiers.py
data/mdpf/scripts/demque/test_demque_yahoo_need_class.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-66`.
<owned_cells>DQ-t-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t66-AC1, DQ9-t66-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~58/MDPF_DEMQUE.TO-DQ-t66.yahoo-gate-is-the-active-set.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t66-AC1,DQ9-t66-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the two real lines verbatim, the folder count, every edited existing test and why, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the nightly run reads the merged code).
comp-iam: DECLARED-NOT-APPLICABLE no new AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE a gate and tier change graded by tests and two read-only plans.
risk: SERVED -- the code changes what the nightly run writes to the served Yahoo store; the never-widen pair `ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_{COO,CTO}_HALF.md` covers it and gates the MERGE.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-15 via CTO msgs 6105, 6114 and ruling `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` items 2 to 4 and amendment 1; the DQ-t-64/65 census; decomposition round 9, amendment 29.
