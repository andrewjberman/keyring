# ETFS_RIVALS task order -- `RIV-xe-1` -- the enrichment leg runs on TRADING days only, and reads the standing request's queue state before a history-owed draw (analysis section 2.3; CTO msg 4568; row D1-S2; round-22 ADDENDUM 7 condition 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xe-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~41</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xe-1` -- the enrichment leg runs on TRADING days only, and reads the standing request's queue state before a history-owed draw (analysis section 2.3; CTO msg 4568; row D1-S2; round-22 ADDENDUM 7 condition 1) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's staged cell `round30_prep/STAGED_CELL_enrichment_trading_gate_and_queue_reader.md` (items 1 and 2); CTO msg 4568 ("one cell with the gate, at the site-Z window -- accepted").
- Measured: 2026-10-10 (a Saturday) exited 97 (the MON-FRI daily Lambda had not built the previous trading day's G1 before the leg looked) and 2026-10-11 (a Sunday) exited 95 on a signed-out Terminal; the
  leg has no trading-day gate. The standing request `ETFS_RIVALS-HISTORY-OWED-DAILY` has a queue state at
  `s3://opal-data-assets/bloomberg/global/silver/request_state/request=ETFS_RIVALS-HISTORY-OWED-DAILY/state.json` (`{"state": active|paused|stopped, ...}`, writer DQ-t-16, reader
  `data.mdpf.scripts.demque.standing.read_state`, which returns "unreadable" for a missing object or a failed read, never "active"); the leg does not read it.
- Interface (`data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` only):
  1. GATE. In `main(argv)`: with NO `--date` and `--mode` in (`daily`, `market`), when `_run_date_et()` is not a trading day by `lib.trading_calendar.is_trading_day` (imported lazily, as `main` already does), print
     ONE line beginning `SKIP:` (naming the date) and return 0 WITHOUT calling `handler_entry`. An explicit `--date` run, any other mode and a trading day are not gated. The calendar is the only source: no typed date list.
  2. READER. A new function `_queue_state() -> str`: `data.mdpf.scripts.demque.standing.read_state("ETFS_RIVALS-HISTORY-OWED-DAILY")`, imported lazily; any exception (an ImportError included) returns `"unreadable"`.
     In `_history_owed`, for `mode == "ask"` only, after the owed set is computed and BEFORE the stored-currency read or any Bloomberg request: state `active` proceeds exactly as today; any other value asks ZERO
     (no `_blp_call`, a currency lookup included), prints ONE `HISTORY OWED:` line naming the state (through `_owed_line` with `refusal="queue state <state>"`), and returns `asked` 0, `carried` = `owed`, and
     `refused` naming the state. `print` mode does not read the state. `RIVALFUNDS_HISTORY_OWED` is NOT set by this cell.
- Out of bounds: every other function of the file, `history_owed.py`, the switch-on, any window or cap constant, the vehicle's scripts and `integrations/bloomberg/pipeline/` (Andrew's no-modify order), any Bloomberg or S3 call in a check.
- Checks: `round30/checks/xe1_gate_and_queue_reader_check.py` (AC1 the gate: a Saturday, a Sunday and Labor Day print one `SKIP:` line and exit 0 without the leg, a trading day, an explicit `--date` and another mode are not gated, the calendar
  is the source; AC2 the reader: `active` draws, `paused`/`stopped`/`unreadable`/anything else draw zero and name the state, the reader fails closed, `print` does not read it; base FAIL 10, one control PASS) and the existing
  enrichment tests (AC3: must be green after your edits to the test files named in your paths). J1: none (a LOCAL cell; the deploy is site Z's under the CTO~Z half).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe1_gate_and_queue_reader_check.py`. It FAILS at the base (10 failed, 1 passed) and is your target; do not edit it. Its docstring restates the rule.
- `main` is at `enrichment_bloomberg.py:1241` (it already imports `lib.trading_calendar` lazily to default the date); `_run_date_et` is at line 378 ("one hook, so a test can pin it"); `_history_owed` is at line 945: the
  `mode == "print"` branch returns first, then `if not units`, then the stored-currency read (line 973), the budget check, the currency lookup and the history requests. Put the state read after `units` is known and before line 973.
- `_owed_line(owed, asked, landed, carried, refusal=...)` (line 927) prints the one `HISTORY OWED:` line; use it for the refusal.
- Existing tests that this changes the ground under: `tests/test_v2_enrichment_cli.py` calls `e.main([])` with no date (line 43), which the gate would turn into a `SKIP:` on a weekend: pin `_run_date_et` to a trading day there. `tests/test_r27tw1_history_owed_leg.py`
  and `tests/test_r28tc1_topup_currency_and_page_day.py` exercise the `ask` path: add an autouse fixture setting `_queue_state` to return `"active"` so their draws are unchanged. List every assertion or fixture you changed.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~41/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W41-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_riv_xe1_gate_and_queue_reader.py
data/etfs/scripts/rivalfunds/tests/test_v2_enrichment_cli.py
data/etfs/scripts/rivalfunds/tests/test_r27tw1_history_owed_leg.py
data/etfs/scripts/rivalfunds/tests/test_r28tc1_topup_currency_and_page_day.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the gate: non-trading days skip with one line and exit 0 without the leg; the other cases are not gated.
- **AC2** -- the reader: active draws, every other state draws zero and names the state, unreadable fails closed, print does not read it.
- **AC3** -- the existing enrichment tests stay green.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xe-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe1_gate_and_queue_reader_check.py -k ac1</invocation><expect>5 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xe-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe1_gate_and_queue_reader_check.py -k ac2</invocation><expect>6 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-xe-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_v2_enrichment_cli.py rivalfunds/tests/test_r27tw1_history_owed_leg.py rivalfunds/tests/test_r28tc1_topup_currency_and_page_day.py rivalfunds/tests/test_e1_enrichment_bloomberg.py</invocation><expect>the final line reads N passed with no failed and no error</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_xe1_gate_and_queue_reader.py`: a copy of the check's scenarios at the cell's own test path (so the suite carries them), adapted to import from the package. Run the rivalfunds suite and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~41/ETFS_RIVALS.TO-RIV-xe-1.trading-day-gate-and-queue-state-reader.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xe-1.trading-day-gate-and-queue-state-reader`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed or retired and why; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 30, workstream `sz`, ONE issuance on the round-29 analysis section 3 item 3 and the CTO's msgs 4568, 4932, 4969, 5577. Decomposition revision 1.31.
Check file(s) dry-run at the base before the cut (see the issuance commit). Chain A (one file, `enrichment_bloomberg.py`); xe-2 follows it on the same file. No edge to xe-3 or xf-1.
The deploy is not a worker's act: xe-3 a Lambda deploy under its own pair (and the issuer's DELTA = 0 live-store read before it), xe-1 and xf-1 site Z's under `1.0.0_SA_CTO~Z`'s half.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>30</round>
<workstream>5</workstream>
<slot>~41</slot>
<fabric>dell1</fabric>
