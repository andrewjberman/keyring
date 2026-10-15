# ETFS_RIVALS task order -- `RIV-ya-1` -- A BLOOMBERG CORPORATE-ACTION ROW BEATS AN INFERRED ROW OF THE SAME KEY IN BOTH READERS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ya-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~43</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ya-1` -- a Bloomberg corporate-action row beats an inferred row of the same (security_id, event_type, ex_date) in BOTH readers, and the drop is counted (CTO half condition C1, msg 5612; disarms row D1-S16) -- APPENDED 2026-10-15, revision 1.32
- Placement: this seat's staged cell `deliverables/2.0.0_SA_COO~V1/round31_prep/STAGED_CELL_bloomberg_wins_cross_source.md`; Andrew "Call bbd5: yes fix only round now".
- Measured (2026-10-15, S3 LIST+GET read-only): `gold/corporate_actions/` holds 12 objects, all plain Bloomberg pulls (`actions-<rev>`), 0 `actions-inferred-*`, 0 `actions-void-*`. A Bloomberg row carries `claim` "MEASURED"; an inferred row (written by
  `dramatic_move`) carries `claim` "INFERRED", a `source_url` and a `raw_event_type` that is the lookup's own phrase, so it never shares the union's own key (`gold_trade_schedule._ACTION_KEY`) with Bloomberg's row. The chart reader
  `price_series._adjustments` already collapses an IDENTICAL (ex_date, ratio) split (MEASURED first) but applies BOTH when the two ratios differ.
- Interface: (1) `gold_trade_schedule.load_actions(s)`: after the void rows leave and BEFORE the union is taken, of the EVENT rows that share (normalised security_id as `price_series._norm_key`, `event_type`, `ex_date`), where at least one has `claim` == "MEASURED" and
  another has `claim` == "INFERRED", the INFERRED rows are dropped. The returned triple is unchanged; the frame carries the number of rows dropped in `df.attrs["precedence_dropped"]` (an int, 0 when none; set on every frame returned, an empty one included). A frame with no `claim` column
  behaves exactly as before. The G5 stage (`gold_trade_schedule.py`, the function that calls `load_actions` at about line 1140) adds `"precedence_dropped": <n>` to its result `detail` dict (the one holding `corporate_actions_revision`, about line 1225), `0` when `actions` is None; no new log line. (2) `price_series.series(...)`: the same rule over the `actions` frame before `_adjustments`, so a Bloomberg split and an inferred split of the same
  ex_date apply ONCE (the Bloomberg row) whatever the two ratios; each key's result gains `"precedence_dropped": <int>` (0 when none). One inferred row with no Bloomberg row for its key is applied as before; two MEASURED rows are never dropped by this rule.
- Out of bounds: `dramatic_move.py` (the writer stays as is: no switch stops it, the disarm is the readers' rule), every other reader and stage file, the void rules (`actions-void-*` behave as before), any S3 write or vendor call, any Lambda or Terraform act.
- Checks: `round31/checks/ya1_bloomberg_wins_check.py` (AC1 the G5 reader, two tests; AC2 the chart reader, two tests; base FAIL 4) and the round-30 control `round30/checks/xe3_union_reader_check.py` (AC3: must stay green, 5 passed). The live-store DELTA = 0 read (today's 12 plain pulls, 0 inferred, through
  both readers) is the issuer's drain act, not a worker criterion. J1: none (a LOCAL cell; the deploy is its own pair, a `SERVED` path).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/ya1_bloomberg_wins_check.py`. It FAILS at the base (4 failed) and is your target; do not edit it. It builds a local sink with a Bloomberg pull and an inferred object (`actions-inferred-*`) and a chart frame set.
- `gold_trade_schedule.load_actions` is at about line 986; it already drops VOIDED event rows (`price_series._voids`) before the union and keeps the greatest-pull row per `_ACTION_KEY`. Put the precedence rule AFTER the void drop and BEFORE the union. Normalise the security id with `price_series._norm_key` (spaces to underscores), as the void rule does.
- `price_series.series` is at about line 162 and `_adjustments` at about line 128. `_adjustments` already collapses an identical (ex_date, ratio) split with the MEASURED row first; the new rule runs before it and also removes an INFERRED split whose ratio differs from the vendor's. Keep `_adjustments`' own behaviour for rows that survive.
- A row's `claim` column reads "MEASURED" (Bloomberg) or "INFERRED" (the dramatic-move lookup); read it with the file's own blank/NaN helpers (`hc._blank`). A frame without the column is the old behaviour exactly.
- The G5 stage (the function calling `load_actions` at about line 1140) builds `detail` at about line 1221; add `"precedence_dropped": <n>` there. `sweep.py:319` also calls `load_actions`; do not edit it (it ignores the attr).
- Regression net: `cd data/etfs/scripts && python -m pytest -q rivalfunds/tests`; report its final line. The round-30 control check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py` must stay green (5 passed).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~43/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W43-S<k>`, `"fabric": "dell1"`, `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/tests/test_riv_ya1_bloomberg_wins.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the G5 reader: a Bloomberg split beats an inferred split of the same key and the drop is counted; a claim-less frame, an inferred-only store and an empty store read as before.
- **AC2** -- the chart reader: a Bloomberg split beats an inferred split of the same ex_date whatever the ratios, counted per key; an inferred split alone applies; two MEASURED rows are never dropped.
- **AC3** -- the round-30 union-reader check stays green (the control).
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ya-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/ya1_bloomberg_wins_check.py -k ac1</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ya-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/ya1_bloomberg_wins_check.py -k ac2</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ya-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py</invocation><expect>5 passed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_ya1_bloomberg_wins.py`: one test per behaviour you added that the check file does not pin (for example the stage `detail` carries `precedence_dropped`). Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~43/ETFS_RIVALS.TO-RIV-ya-1.bloomberg-wins-cross-source-both-readers.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ya-1.bloomberg-wins-cross-source-both-readers`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~RV):** Round 31, the fix-only round before the park, ONE issuance on Andrew-direct "Call bbd5: yes fix only round now" and CTO msg 6232. Decomposition revision 1.32. Check file dry-run at the base before the cut: ya1 base: FAIL (4 failed) as expected; the round-30 xe3 control base: PASS (5 passed) as expected. Chain A (`gold_trade_schedule.py`, `price_series.py`); no edge to chain B. The live-store DELTA = 0 read through both readers, the never-widen pair (COO half and CTO half), the deploy by a CloudOps seat and the D1-S16 disarm follow at the drain.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>31</round>
<workstream>1</workstream>
<slot>~43</slot>
<fabric>dell1</fabric>
