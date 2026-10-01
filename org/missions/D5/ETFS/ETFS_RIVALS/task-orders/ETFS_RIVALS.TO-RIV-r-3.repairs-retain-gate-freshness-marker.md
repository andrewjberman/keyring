# ETFS_RIVALS task order -- `RIV-r-3` -- ROUND 3 (ENRICHMENT): THE REPAIR CELL -- ISSUER RETAIN, NARROWED GATE, TRADING-DAY FRESHNESS, NOT-UPDATED MARKER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell; the build-silver role's lack of s3:DeleteObject (policy rivalfunds-build-silver-lambda.json: Put/Get only) is the reason for item 1 and is not widened.
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified); declared on RIV-i-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE),
each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-2 built and enriched the live pipeline (package
`data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg). **Round 3** adds the home funds,
identity, GICS, and repairs four round-2 defects -- THIS cell. Work ONLY in the worktree your spawn line names; every path below is
relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-r-3` -- the round's repair cell: issuer retain, narrowed gate, trading-day freshness, the not-updated marker

1. **`silver_issuer.py` supersedes WITHOUT deleting** (row Z-S4; the W5-S24 remedy, as `silver_bloomberg.py` @e622b2fef9 does it):
   remove the `_delete` of earlier captures' silver; record each in `dropped` with `was_in_silver: True, retained: True`; a
   re-capture of a landed report date returns OK WITH a marker. `gold_canonical_shape` already reads the newest issuer object per
   date (`max(..., key=_revision)`), so no reader changes.
2. **The narrowed enrichment gate** (W5-S23, ruling 2). Replace the round-2 `enrichment_gate`'s whole-batch hold: a fund is HELD
   only if its trade window `(prior report date, report date]` contains the ex-date of a corporate action -- in the latest landed G3
   -- on a security the fund holds in that window; every other fund builds its G5 now (BASG included). `sweep.run_gold_chain`
   passes the held set to `build-trade-schedule` as `event["hold_funds"]` and reports it as `detail["held_funds"]` (fund -> reason);
   `build-trade-schedule` is SKIPPED only when every fund is held. A held fund builds when its pull-enrichment marker arrives, as a
   NEW G5 object whose revision sorts after the partial one and carries every fund (nothing is overwritten; the page reads the newest
   revision per date, as today).
3. **Trading-day freshness per source** (W5-S28, ruling 3). `report_date_freshness` counts trading days with
   `lib/trading_calendar.py` (as it already does) against a per-source, measured allowance: `bloomberg` 1 trading day (Bloomberg
   reports one trading day late, measured in row W5-S28), `home_producer` 1 (the Positioning pull runs on Bloomberg's T-1),
   `issuer` 0. The allowance is a named constant citing its row; the reason string names the source, the lag and the allowance in
   trading days.
4. **The not-updated publish marker** (W1-S5). When the page publishes with some funds marked not updated, `publish_page` still
   writes its marker; the marker record carries `not_updated: {fund: reason}` for that batch (so the sweep does not re-run
   publish-page for the batch forever). A page that publishes NOTHING (every fund failing, or a render failure) still writes no marker.

## 2. WHAT YOU NEED TO KNOW ABOUT THE CODE (measured at the cut, base 78167bb8fc)

- `silver_issuer.py` handler: the loop `for u in existing: ... _delete(s, u) ...` near line 251; on a failed delete it records a
  failure, so on S3 (no DeleteObject) the batch returns PARTIAL with no marker. Locally `_delete` unlinks, so ONLY a retention
  assertion can see the fix. `silver_bloomberg.py`'s handler (same package) is the pattern: it keeps the object and records
  `retained: True`.
- `sweep.py`: `enrichment_gate(date, batch_id, sink, markers=None, enrichment_dates_fn=None)` (~line 232) and
  `run_gold_chain(ev, runners=None, gate=None, markers=None)` (~line 259); `run_dag` uses the gate for batches too -- keep both paths
  consistent. G3 lives at `address('rivalfunds','etfs','gold','corporate_actions','date=<D>','actions-<rev>.parquet')` with
  `security_id`/`security_bloomberg`, `event_type`, `ex_date`; G1 rows carry `fund_ticker`, `report_date`, `security_bloomberg` /
  `position_id`, `is_cash_line`.
- `gold_trade_schedule.py`: `handler_entry(event)`; G5 object `trades-<revision>.parquet` per date; `_revision(uri)`; readers take
  the greatest revision per date.
- `publish_page.py`: the manifest's `funds` dict is keyed `"<GROUP>/<FUND>"`, each with `checks` [{check, status, reason}];
  `report_date_freshness`'s reason today reads `latest report <d> vs expected <d>: lag <n> trading day(s), threshold 0
  (PROVISIONAL)`; the expected date is the trading day before the page day. `marker = None if agg_failed else write_marker(...)`.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/trading_calendar.py`, `lib/opal_naming.py`; `data/etfs/scripts/rivalfunds/homes.py`, `markers.py`,
`sinks.py`, `silver_bloomberg.py`, `gold_canonical_shape.py`, `enrichment_bloomberg.py`, `render.py`;
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`, `round2/checks/`, `round3/checks/`; the device-local
captures, read-only, outside your worktree: `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\etfs-rivals-idvz-20260930\`
and `...\.runtime\amgt-reconn-daily-census-20260929\` (the checks find them through the main worktree).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg
or OpenAI call, any alert/monitor, any file another round-3 cell owns (`gold_canonical_shape.py`, `gold_holdings_coverage.py`,
`enrichment_bloomberg.py`, `home_producer.py`, `identity.py`). Unit tests go beside the code as `tests/test_r3_*.py`, run with
`python -m pytest <file> -q` from `data/etfs/scripts/`.

<paths>
data/etfs/scripts/rivalfunds/silver_issuer.py
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/test_r3_*.py
data/etfs/scripts/rivalfunds/tests/test_s1_silver_issuer.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
data/etfs/scripts/rivalfunds/tests/test_p2_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_*.py
data/etfs/scripts/rivalfunds/tests/test_g2_*.py
data/etfs/scripts/rivalfunds/tests/test_g52_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

(The existing test files above are granted because they may assert the round-2 behaviour this cell changes: delete, whole-batch
hold, threshold 0. Change an assertion only where it encodes exactly that behaviour, and say which in your report.)

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a re-capture of a landed issuer report date keeps both silver objects, writes its marker, records the earlier one
  retained, and G1 reads the newer (`.../round3/checks/r-3.AC1.py`)
- **AC2** -- with a pull-enrichment marker that does NOT cover the newest date and a planted split on one TXUE holding, the chain
  builds G5 for the un-held funds, holds TXUE with a reason, and reports `held_funds` (`.../round3/checks/r-3.AC2.py`)
- **AC3** -- a Bloomberg fund 1 trading day behind passes freshness, one 2 behind fails with a trading-day reason, and the publish
  marker is written naming the failing fund under `not_updated` (`.../round3/checks/r-3.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-r-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/r-3.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-r-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/r-3.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-r-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/r-3.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-r-3.repairs-retain-gate-freshness-marker.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-r-3.repairs-retain-gate-freshness-marker`. Report once: each criterion's verdict line with the output above it; the files you wrote; any test assertion you changed and why; any row filed (id + one line). Leave the order's `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.7 @01114ae8a8 (ADMITTED; CVO ratified-text half signed, brief auto-admitted).
Round-2 analysis @01114ae8a8 items 1-2 + rulings 1-3 + W1-S5. Checks dry-run at base 78167bb8fc: r-3.AC1 FAIL (both objects kept:
1; retained not recorded), r-3.AC2 FAIL (build-trade-schedule SKIPPED; held_funds absent), r-3.AC3 FAIL (TXUE lag 1 fails at
threshold 0; marker None) -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>3</round>
<slot>~2</slot>
<fabric>site-z</fabric>
