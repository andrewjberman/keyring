# TO IRPT_CUSTDY.TO-CU-b-3 -- round 2 CU-b-3 (E4): hop 3 on 2024 onward -- QTD, YTD, 1Y computed; SI held before 2024; every figure names its source rows

<to_id>IRPT_CUSTDY.TO-CU-b-3</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~6</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-b-3` (`decompositions/IRPT_CUSTDY_DECOMP.round2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (round 1's code is at HEAD)

---

## WORKER FACE

### THE CELL

`CU-b-3`, item E4 of the CTO's round-1 analysis: "Hop 3 on 2024 onward." Round 1 built
`data/assets/scripts/gold/irpt_custody/client_report_figures.py` (the client-report contract; periods from
`data/assets/scripts/gold/runners_49f/parity_period_returns.py` `RULED_PERIODS = ('QTD', 'YTD', '1Y', 'SI')` via `link()` and
`period_window()`). Two standing constraints now bind it:
- **HOLD A** (laptop CTO, 2026-10-07 08:5xZ): on dell2 nothing dated before 2024-01-01 goes through `lib/trading_calendar.py` until a
  calendar fix lands. So an SI window whose start (the account's inception) is before 2024-01-01 is NOT computed: it is reported with
  status `HELD_CALENDAR_FIX`, value `null`, and the calendar is never called for that date. QTD, YTD and 1Y for 2026-09-30 start in
  2025-2026 and are computed as before.
- **The firm bucket is fenced from dell2** (row S4): the returns gold under `opal_naming.address("irpt", <firm>, "gold",
  "account_return_daily", ...)` cannot be read here. Build and check on fixtures only; the real read runs on the laptop.

**Build, in `client_report_figures.py`:**
1. The status set of a figure becomes `OK | NO_DATA | WINDOW_NOT_RULED | HELD_CALENDAR_FIX`. SI with an inception before 2024-01-01 is
   `HELD_CALENDAR_FIX`; the household SI is `HELD_CALENDAR_FIX` when any member account's is.
2. Every figure carries `source`: `{"table": <table name>, "partition": <date=...>, "rows": <count of rows used>}` -- for returns the
   returns-gold partitions the linked series read, for market value, holdings, activity and fees the Schwab silver table and partition.
   A figure with no source rows says `rows: 0` and is not `OK`.
3. The self-test grows two flags: the LAST line becomes `CLIENT-FIGURES-SELFTEST contract_ok=<..> periods_ok=<..> nodata_marked=<..>
   held_ok=<True|False> sources_ok=<True|False>`, with a fixture account whose inception is 2019 (SI held, QTD/YTD/1Y computed) and a
   check that no call reached `lib/trading_calendar.py` with a date before 2024-01-01.
4. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_client_report_held_si.py` (round 1's
   `test_client_report_figures.py` must still pass; edit it only where the new status or the `source` key requires): pre-2024 inception
   -> SI `HELD_CALENDAR_FIX`, value null; 2024-or-later inception -> SI computed; QTD/YTD/1Y for 2026-09-30 computed; every figure has a
   `source` with a row count; the calendar is not called for a pre-2024 date (patch it and assert).

### ACCEPTANCE

<criterion id="CU7-AC1" cell_refs="CU-b-3"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_client_report_held_si.py</invocation><expect>passed</expect></criterion>
`CU7-AC1` -- the HOLD rule, the computed periods, and the source on every figure, on fixtures.

<criterion id="CU7-AC2" cell_refs="CU-b-3"><invocation>python data/assets/scripts/gold/irpt_custody/client_report_figures.py --self-test</invocation><expect>held_ok=True sources_ok=True</expect></criterion>
`CU7-AC2` -- the seam through the real CLI on fixtures (the real neighbour is fenced from dell2, row S4); the round-1 flags must stay
True on the same line.

<expected_criteria>CU7-AC1,CU7-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call** in tests or self-test. **Never call `lib/trading_calendar.py` with a date before 2024-01-01.** Never run `--apply`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W6-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_held_si.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round2.md</decomp_doc> (round 2), cell `CU-b-3`.
<owned_cells>CU-b-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU7-AC1, CU7-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~6/IRPT_CUSTDY.TO-CU-b-3.figures-2024-onward.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU7-AC1,CU7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test line, the test list, how the calendar guard is enforced, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE round 2 runs by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (fixtures only; the firm bucket is fenced, row S4).
comp-adversary: RUN -- cross-firm (49financial only); HOLD A enforced in code and test; BLIND: the real returns gold until the laptop's file (decomposition round 2 constraint 3).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-1 analysis @822468e309 section 3 E4; HOLD A (msgs 179, 192); row S4; decomposition round 2 constraints 3-4.
