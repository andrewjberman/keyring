# ETFS_RIVALS task order -- `RIV-bf-1` -- ROUND 15 (ENRICHMENT): AN AD HOC BLOOMBERG CLOSE-PRICE BACKFILL OVER A DATE RANGE, UNDER A ROW BUDGET (BUILD ONLY; NO CALL)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-bf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the backfill is ad hoc by Andrew's word and is run by the issuer, never scheduled)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the chart objects sit under the page prefix the publisher already writes and the gateway already reads)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. **Round 15** (PRD v0.18 FWD-22, FWD-23): every period becomes 30 / 90 / 365 calendar days; the security dialog gains a price curve with the fund's buys and sells marked on it, fed by a per-fund chart object behind one gateway route and drawn by the page's one script; a Bloomberg close-price backfill is built (never run by a worker). Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

Shared vocabulary (binding on every cell):
- **Periods:** `R30`, `R90`, `R365` -- calendar days. `asof = prev_trading_day(page_day)` (the existing CALL 3 rule); a window's
  first day is `asof - N calendar days`, its last day `asof`. `MTD`, `QTD`, `YTD` keep computing and are never displayed.
- **Chart object:** one JSON per fund per page day at `homes.page(<day>, "charts/<FUND>.json")` (opal_naming output), shape
  `{"fund", "asof", "generated_at", "ranges": {"R30": <first day>, "R90": ..., "R365": ...}, "securities": {<security_key>:
  {"name", "source_words", "points": [[<YYYY-MM-DD>, <price>|null, <source code>], ...], "gaps": [{"start", "end", "reason"}],
  "markers": [{"side": "buy"|"sell", "start", "end", "span": bool, "usd", "bps", "r", "n_trades"}]}}}`. Source codes:
  `m` market close, `i` holding-implied. `points` ascend by date and cover `asof - 365d .. asof`.
- **Route:** `GET /rivalfunds/<YYYY-MM-DD>/chart/<FUND>` on the gateway, JSON, behind the same identity wall.

### `RIV-bf-1` -- an ad hoc Bloomberg close-price backfill over a date range, on the existing market route, under a row budget (FWD-22; F.5 card 2 answer; WORLD)
- Andrew-direct @96d0ab2f4b: "Yes for the rivalfunds funds only ... an ad hoc backfill for the selected funds that uses the
  existing BBG route"; @69c7f24b44: about 365 calendar days. Existing route: `enrichment_bloomberg` mode `market` already sends a
  one-day `HistoricalDataRequest` for a past date (`_market_pull`, `_blp_historical_data`).
- Interface: new mode `market-range` of stage `pull-enrichment`: event `{"mode": "market-range", "start", "end", "securities":
  [...], "batch_id", "sink", "max_points": int, "dry_run": bool}`. It plans `len(securities) x trading days in [start, end]`
  points; `dry_run` returns the plan and spends nothing; if the plan exceeds `max_points`, or exceeds `bbg_budget`'s
  `ceiling - reserve - spent(today)`, it REFUSES before any request, naming the points left. Otherwise ONE historical request
  per batch of 50 securities over `[start, end]` for `px_close`'s field only; it writes one `gold/security_market/date=<D>`
  object per date that has rows (never overwriting an existing object of that date: a date already holding a `market-*.parquet`
  is skipped and counted), each row `as_of_source = "backfill"`; it records the points in the `bbg_budget` ledger with mode
  `market-range`; a tripped session stops the run with what landed stated. No file under `integrations/` changes. The live
  run is the ISSUER's act under a never-widen pair, after the day's 07:00 ET vehicle run; the worker makes NO Bloomberg call.
- Rulings at the cut (issuer): a refusal is `status == "REFUSED"` (the module's own word). The result carries `plan: {"points",
  "securities", "trading_days", "batches"}`; a refusal's detail names the planned points and the points left, where "left" is
  the smaller of `max_points` and the budget remainder. Skipped dates are returned as `skipped_dates` (a list). The ledger
  records the points REQUESTED (securities x trading days of the range), since that is what the vendor was asked for. The
  budget read is a new `bbg_budget.check_points(points, today=None) -> None | detail` beside `check_backfill` (unchanged).
  A tripped session returns `FAILED` naming the dates that landed.
- **Organic trigger:** none (ad hoc by Andrew's word); the negative arm is the daily `market` mode, unchanged.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- YOU MAKE NO BLOOMBERG CALL, EVER. The terminal on this machine is live and shared with the firm's 07:00 ET production pull: an ad hoc backfill on 2026-10-05 exhausted its daily capacity and blocked production (`bbg_budget.py` header). Every test stubs `_blp_historical_data` / `_blp_reference_data` at the seam `tests/test_s4_security_market.py` uses, and sets `RIVALFUNDS_BBG_BUDGET_DIR` to a temp dir.
- `integrations/bloomberg/` is read-only by Andrew's order: the existing `blp_client.historical_data(securities, fields, start, end)` already takes a range; change nothing there.
- The existing `market` mode (one date) and `daily` mode must behave exactly as today: the daily production pull is never refused and never changed.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15bf1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/bbg_budget.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the dry run spends nothing; a plan over max_points and a plan over the budget remainder are REFUSED before any request; control: plan-market still plans (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC1.py`)
- **AC2** -- a fitting run makes one historical request per batch over the range, writes one partition per date as backfill rows, skips a date that already holds an object, records the points; control: plan-market still plans (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-bf-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-bf-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-bf-1.a-bloomberg-close-price-backfill-over-a-date-range-under-a-budget.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-bf-1.a-bloomberg-close-price-backfill-over-a-date-range-under-a-budget`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~3`, slot `~3`, position 1 of 1. Checks dry-run at base by the issuer: bf-1.AC1 FAIL as expected (control PASS); bf-1.AC2 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~3</slot>
<fabric>site-z</fabric>
