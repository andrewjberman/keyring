# ETFS_RIVALS task order -- `RIV-pd-1` -- ROUND 15 (ENRICHMENT): THE GOLD TABLES COMPUTE 30d / 90d / 365d AS CALENDAR DAYS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
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

### `RIV-pd-1` -- the gold tables compute 30d / 90d / 365d as calendar days (FWD-23; F.2, F.6)
- Today `gold_holding_contribution.PERIODS = ("MTD","QTD","YTD","R30")` with R30 = the 30th NYSE trading day ending on the day
  (`period_start`, :120-128); `gold_buying_trend.PERIODS = ("YTD","R30","MTD","QTD")`, R30 likewise (`_period_starts`, :123-136).
- Interface: both modules' `PERIODS` gain `R90` and `R365` and keep `MTD`, `QTD`, `YTD`. `gold_holding_contribution.period_start(p,
  day)` and `gold_buying_trend._period_starts(day)[p]` return, for `R30` / `R90` / `R365`, `date(day) - 30 / 90 / 365` calendar
  days (`day` here is the as-of the stage already passes). `earliest_start` follows. A fund whose history starts after the window's
  first day keeps the existing partial rule (`period_clipped`, `price_coverage`). Each table's stage detail states, for one fund,
  the old and the new R30 window (`r30_window_was`, `r30_window_is`).
- Rulings at the cut (issuer): ONE anchor for both tables. The pure functions stay pure on the day they are handed
  (`period_start(p, d)` and `_period_starts(d)[p]` return `d - N` calendar days); `gold_buying_trend.build` hands the three
  rolling periods `gold_holding_contribution.as_of(<event day>)`, exactly as holding_contribution already does, so both tables'
  R30 / R90 / R365 start on the same day. MTD / QTD / YTD keep their present anchors and starts. `r30_window_was` and
  `r30_window_is` sit in each stage's result `detail`, each `{"fund": <id>, "start": <ISO>, "end": <ISO>}` for the first fund
  built.
- **Organic trigger:** the 07:00 ET marker publish's stale-table rebuild (`publish_page.produce_a1`).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- The 30-day period MOVES from 30 NYSE trading days to 30 calendar days: existing tests that pin the trading-day R30 (for example `tests/test_r8hc1_r30_trading_days.py`, `tests/test_r8bt1_periods.py`) will fail and are yours to re-pin; list every assertion you change and why.
- `period_clipped`, `price_coverage` and `n_days_period` must stay truthful for a 365-day window on a fund with a short history.
- You run pd-1 FIRST; RIV-pd-2 and RIV-md-1 follow on the same branch.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15pd1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the period arithmetic and both PERIODS tuples; control: MTD / QTD / YTD keep their starts (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC1.py`)
- **AC2** -- both stages driven offline write R90 and R365 rows on ONE as-of anchor and state the old and new R30 window; control: MTD and YTD rows keep their starts (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-pd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-pd-1.periods-are-30-90-365-calendar-days-in-the-tables.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pd-1.periods-are-30-90-365-calendar-days-in-the-tables`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~1`, slot `~1`, position 1 of 3. Checks dry-run at base by the issuer: pd-1.AC1 FAIL as expected (control PASS); pd-1.AC2 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~1</slot>
<fabric>site-z</fabric>
