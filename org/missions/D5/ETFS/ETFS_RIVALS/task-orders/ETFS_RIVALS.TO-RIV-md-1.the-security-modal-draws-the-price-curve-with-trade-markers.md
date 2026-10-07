# ETFS_RIVALS task order -- `RIV-md-1` -- ROUND 15 (ENRICHMENT): THE SECURITY MODAL DRAWS THE PRICE CURVE WITH THE FUND'S TRADE MARKERS, BY THE PAGE'S ONE SCRIPT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-md-1</owned_cells>
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

### `RIV-md-1` -- the security modal draws the price curve with the fund's trade markers, by the page's ONE script (FWD-22; F.7)
- Interface: each `<section data-fund=...>` of a security dialog gains a chart frame `<div class=rf-chart data-chart-fund="<FUND>"
  data-chart-key="<security_key>">` holding a three-way range switch (30d first, then 90d, 365d), a words line (`data-chart-status`)
  and the fund's trade list in words (from the context's trades; present with or without the script). The page carries EXACTLY
  ONE inline `<script>` block with no `src`; `_BAD_CONSTRUCTS` admits that one block and still refuses every other script,
  `src=`, `<link`, `@import`, `url(`; `render.script_count(html) -> int`. The script: on a dialog opening, fetches
  `/rivalfunds/<page day>/chart/<FUND>` (same origin, once per fund, cached), draws an inline-SVG curve of the chosen range
  from `points`, breaks the line at gaps and prints each gap's reason, draws each marker as a hollow circle of radius `r` at
  its end date (green buy, red sell; a `span` marker also draws a bar over its window), shows price + date on pointing at any
  part of the curve and the marker's words on a marker, prints `source_words`. On a failed or missing object the status line
  reads "Chart could not load" and the trade list stays. `data-history=none` and HISTORY_NONE leave the dialog.
  The script lands on the SERVED page only after the chart route serves (issuer's sequencing at the deploy).
- Rulings at the cut (issuer): the script is emitted unconditionally by `render_page`; the route-before-script order is the
  issuer's deploy sequence, not a flag. The AUDIT page gets no chart frame and no script, and `validate_audit` /
  `validate_fund` still refuse any script. `data-chart-fund` carries the fund ticker exactly as the route takes it. The range
  switch is three buttons `<button data-chart-range="R30|R90|R365">` reading 30d, 90d, 365d, R30 marked current. The trade
  list is one line per trade from `trade_markers.words` when that module is importable, else the page's own trade words; a
  fund with no trade in the security lists none and says "No trades in the last 365 days".
- **Organic trigger:** opening a security modal from a fund's section on the live page.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- NO browser exists in your environment: write the script small and plain (no library, no external source, no network call except `fetch` to `/rivalfunds/<page day>/chart/<FUND>` on the same origin), and unit-test its pure parts by keeping the geometry simple enough to read. Say in your report what you could not exercise.
- The chart object's shape is in the shared vocabulary above: build against it with a fixture object; the object and the route are built by other chains.
- The page must keep working with the script absent or failed: every switch, table, dialog and the trade list.
- Size: the main page is 1,279,784 B of a 1,950,000 B cap and must keep 20% headroom (1,560,000 B). 671 fund sections gain a frame: keep the frame markup under 250 B each and print the page's byte growth on the round-8 fixture in your report.
- You run this LAST on the branch, after RIV-pd-1 and RIV-pd-2.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15md1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a chart frame per fund section with its range switch, status line and trade list in words; the history note leaves; control: the dialogs and their fund sections stand (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC1.py`)
- **AC2** -- exactly one inline script that names the chart route and the could-not-load words; the render check admits it and still refuses six planted constructs (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-md-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-md-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-md-1" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on the live page in a signed-in browser, never self-graded): the modal reads as the Market Overview security modal does -- the curve for 30d / 90d / 365d, hollow green and red markers sized by the trade's share of the fund, price and date on pointing at any day, the trade's value and basis points on a marker, a gap drawn as a gap with its reason, the price source named.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-md-1.the-security-modal-draws-the-price-curve-with-trade-markers.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-md-1.the-security-modal-draws-the-price-curve-with-trade-markers`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~1`, slot `~1`, position 3 of 3. Checks dry-run at base by the issuer: md-1.AC1 FAIL as expected (control PASS); md-1.AC2 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
