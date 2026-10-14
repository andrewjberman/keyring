# ETFS_RIVALS task order -- `RIV-xe-3` -- `gold_trade_schedule.load_actions` reads the UNION of every pull's actions per security, so a short incremental pull keeps every older action (CTO msg 5577; the precondition of RIV-xe-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xe-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~40</issued_to>
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

### `RIV-xe-3` -- `gold_trade_schedule.load_actions` reads the UNION of every pull's actions per security, so a short incremental pull keeps every older action (CTO msg 5577; the precondition of RIV-xe-2) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's consumer read `round30_prep/XE2_CONSUMER_READ_G3_PARTITIONS_20261014.md` @8c6eab1456; CTO ruling msg 5577 (REC accepted): "the UNION of every pull's
  actions per security, de-duplicated on the action's own key, with the latest pull winning on a key collision"; `xe-2` waits on this cell deployed and read once.
- Measured (code at box/dell1 HEAD): `gold_trade_schedule.load_actions` (`gold_trade_schedule.py:983-994`) concatenates every `corporate_actions` object and keeps, per
  `security_id`, only the rows of its LATEST pull (`as_of|revision` greatest). Today that is a full snapshot (every pull asks 730 days); a short incremental pull (RIV-xe-2) would
  become a security's latest pull and drop its older actions from G5 (moved served output). `price_series._actions` and `dramatic_move` already read the union.
- Interface (`data/etfs/scripts/rivalfunds/gold_trade_schedule.py`, `load_actions` only; its signature and return triple are unchanged): an EVENT row (`row_kind == "event"`) is kept
  from EVERY pull; its key is (`security_id`, `event_type`, `raw_event_type`, `ex_date`), a column the frame lacks reading as the empty string; of several rows with one key the row of the
  greatest (`as_of`, `revision`) pull is kept. A STATUS row (`row_kind == "status"`) follows the rule as it was: kept only when it belongs to the security's LATEST pull. The label is the
  `+`-joined sorted revisions of the rows returned; an empty store returns `(None, None, [])`.
- Out of bounds: every other function of the file, `sweep.py`, `price_series.py`, `dramatic_move.py`, the G5 schema and every stage output; no S3 read (a local sink only).
- Checks: `round30/checks/xe3_union_reader_check.py` (AC1 the short pull keeps the older actions; AC2 one action in two pulls appears once with the latest pull's values; AC3 status rows follow the
  old rule, a full-snapshot store reads as before, an empty store returns the old triple; base FAIL 3, the empty-store control PASS). The live-store arm (the new reader's G5 output equals today's,
  DELTA = 0, read-only, BEFORE any deploy) is the issuer's drain act, not a worker criterion. J1: none (a LOCAL cell; the Lambda deploy goes under its own pair).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py`. It FAILS at the base (3 failed, 1 passed) and is your target; do not edit it.
- `load_actions` is at `gold_trade_schedule.py:983`; it builds a frame from every object under `gold/corporate_actions/date=` and today filters with `key == key.groupby(df["security_id"]).transform("max")`.
  Rows written by `enrichment_bloomberg.rows_from_responses` carry `row_kind` `event` or `status`, `event_type`, `raw_event_type`, `ex_date`, `as_of`, `revision`; the existing test helper `_g3`
  in `tests/test_g52_trade_schedule_v2.py` builds event rows WITHOUT `raw_event_type`.
- The existing test `test_the_latest_pull_per_security_wins_in_the_stage_loader` (same file) must stay green unedited: its two pulls share one (security, event_type, ex_date) key, so the latest pull wins.
- Callers: the trade-schedule stage (`gold_trade_schedule.py` about line 1102) and `sweep.py:319`; both take the triple unchanged.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~40/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W40-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_riv_xe3_union_reader.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- short incremental pull keeps every older action.
- **AC2** -- the same action in two pulls appears once, with the latest pull's values.
- **AC3** -- status rows follow the old rule, a full-snapshot store reads as before, an empty store returns the old triple.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xe-3"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py -k ac1</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xe-3"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py -k ac2</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-xe-3"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py -k ac3</invocation><expect>2 passed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_xe3_union_reader.py`: a copy of the three planted-store scenarios of the check at the cell's own test path (so the suite carries them). Run `python -m pytest -q rivalfunds/tests/test_g52_trade_schedule_v2.py rivalfunds/tests/test_r10rp2_g5_code_replay.py rivalfunds/tests/test_r9gd1_g5_drift.py` and report the final line (the readers' neighbours).
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~40/ETFS_RIVALS.TO-RIV-xe-3.union-reader-for-corporate-actions.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xe-3.union-reader-for-corporate-actions`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed or retired and why; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 30, workstream `sz`, ONE issuance on the round-29 analysis section 3 item 3 and the CTO's msgs 4568, 4932, 4969, 5577. Decomposition revision 1.31.
Check file(s) dry-run at the base before the cut (see the issuance commit). Chain B (one file, `gold_trade_schedule.py`); no edge to xe-1 or xf-1. xe-2 (chain A, after xe-1) additionally waits on this cell DEPLOYED and read once (CTO msg 5577).
The deploy is not a worker's act: xe-3 a Lambda deploy under its own pair (and the issuer's DELTA = 0 live-store read before it), xe-1 and xf-1 site Z's under `1.0.0_SA_CTO~Z`'s half.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>30</round>
<workstream>5</workstream>
<slot>~40</slot>
<fabric>dell1</fabric>
