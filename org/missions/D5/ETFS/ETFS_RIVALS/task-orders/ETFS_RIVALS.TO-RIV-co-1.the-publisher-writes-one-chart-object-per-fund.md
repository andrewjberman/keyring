# ETFS_RIVALS task order -- `RIV-co-1` -- ROUND 15 (ENRICHMENT): THE PUBLISHER WRITES ONE CHART OBJECT PER FUND BESIDE THE PAGE, WITH ITS SIZE LINE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-co-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
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

### `RIV-co-1` -- the publisher writes one chart object per fund beside the page, with its size line (FWD-22; F.5 items 1 and 4)
- Interface: `publish_page` writes `homes.page(day, "charts/<FUND>.json")` for every fund of the page, in the shape of the shared
  vocabulary, covering exactly the securities whose dialog on the rendered page carries that fund's section
  (`publish_page.dialog_fund_keys(html) -> {fund: [security_key, ...]}`, exported by THIS cell from a regex over the rendered HTML:
  `data-sec-dialog="<key>"` blocks and their `<section data-fund=...>` children; no render.py edit). Built from
  `price_series.load` and `trade_markers.markers`. `CHART_MAX_BYTES = 1_900_000` per object: over it, the 365-day points are
  thinned to weekly (and the object says `"thinned": true`); still over -> the object is not written and the stage prints `FAIL:
  chart object over cap for <FUND>`. The manifest gains `charts: {<FUND>: {"uri", "bytes", "securities", "markers",
  "thinned"}}`. The day's page publishes whether or not a chart object fails. Write once per revision, like audit.html.
- Rulings at the cut (issuer): `dialog_fund_keys(html)` and `CHART_MAX_BYTES` live in `publish_page` (this cell's file) and the
  cap is read at call time. A fund of the page with no dialog section gets NO object and no manifest entry. In the manifest
  `securities` and `markers` are counts. Thinning keeps the last trading day of each ISO week and every day that carries a
  marker's start or end. A fund whose object is refused has the manifest entry `{"uri": null, "bytes": <over-cap bytes>,
  "refused": true}`. `fund_mv_by_date` is the sum of `market_value` over the fund's G1 report of that date.
- **Organic trigger:** the 07:00 ET marker publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `publish_page.py` already writes index.html, audit.html and the manifest with read-back and per-revision copies: write the chart objects the same way, after the page is rendered (the dialog set comes from the rendered HTML).
- Round 14 added `ai_grounding` and `audit_trades_left_out` to the manifest: keep both.
- The address is `homes.page(day, "charts/<FUND>.json")`: never a typed bucket or key.
- You run this LAST on the branch, on your own ps-1 and tm-1.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15co1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/trade_markers.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- one object per fund in the prescribed shape covering exactly that fund's dialog securities, with its manifest entry; control: the page publishes on the fixture (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC1.py`)
- **AC2** -- under the cap unthinned; one byte over, thinned and said so; still over, not written with its FAIL line and the page still publishes (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-co-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-co-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-co-1" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on a real day's objects, never self-graded): for one fund, a sample of points equals the market close or the holding-implied price of that day, and each marker equals a trade of the audit page's trade log in side, window and dollars.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-co-1.the-publisher-writes-one-chart-object-per-fund.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-co-1.the-publisher-writes-one-chart-object-per-fund`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~2`, slot `~2`, position 3 of 3. Checks dry-run at base by the issuer: co-1.AC1 FAIL as expected (control PASS); co-1.AC2 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~2</slot>
<fabric>site-z</fabric>
