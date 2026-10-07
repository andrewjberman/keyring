# ETFS_RIVALS task order -- `RIV-pm-1` -- ROUND 22: A PART MONTH IS MARKED, NO CURVE IS DRAWN WHERE THERE IS NONE, AND THE MARKERS ARE HONEST AND KEYED AS THE PAGE IS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~12</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (render functions, the page's inline script, the marker builder and the publisher's chart read of tables it already reads)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the round analysis and the R3 read
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A per-fund chart object, written by the publisher from the price series and the fund's trades (`trade_markers.py`, `publish_page.py`), feeds that script. **This order, round 22, is the second cell on the reviewer's display findings.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-pm-1` -- the oldest strip cell is marked as a part month; no curve is drawn where there is none; the markers run through the page day and a zero-dollar trade is not one (FWD-22, FWD-23; analysis R2, R3; row Z-S59)
- Measured: the 365-day window begins inside October 2025, so the 180 thirteen-cell strips' first cell is a part month,
  and a 90-day strip's first cell is July from the 8th (cause B: 3 strips read as disagreeing with their markers). One
  fund-security has a stored currency, 4 markers and 0 prices and draws nothing (BIDD 6475395Z GR); CGIC 2454 TT has 2
  prices and 126 markers riding the top edge. Two strips show an October trade whose window ends on the page day and has
  no marker (cause A); two securities carry trims at -0.0 dollars drawn as markers (cause C).
- Interface:
  1. `render._month_chart(mark, end=None, start=None)` and `render._month_words(mark, end=None, start=None)` take the
     trend row's `window_start`. When `start` is given, its day of month is after the 1st, and the strip's first cell is
     `start`'s own calendar month (same year and month), the FIRST cell carries the attribute `data-part` and no other
     cell does; `render.MONTH_CSS` gains a rule on `[data-part]` that shows the reader the month is partial;
     `_month_words` appends " (part month)" to that month. Otherwise no cell carries it. Both call sites pass the row's
     `window_start`. Everything round 21 built stays.
  2. In the page's one script: `nohist(s)` returns the no-history sentence also for a security with a stored currency and
     not one priced point (the plain sentence; the object's `source_words` only when the currency is null); a new pure
     function `window.rfChart.curve(pl)` answers true only when the range's plan holds two or more priced points, and for
     a range where it is false the script draws no svg and prints "Fewer than two prices on file in this range." when the
     range holds exactly one priced point (a range with none keeps "No price on file in this range."). Each sentence
     appears once in the script.
  3. `trade_markers.markers` skips a trade whose `est_notional` is zero (0.0 or -0.0) as it skips a null one. The chart
     object's markers run through the PAGE day: the trades handed to `trade_markers.markers` include one whose
     `window_end` is the page day. Prices (`points`, `ranges`, `asof`) still end at the as-of day.
  4. (Amendment 1, row ETFS_RIVALS-Z-C-S64; CTO ruling msg 31031.) The chart object's markers are keyed by the SAME
     one-key rule the trend and the rankings use: a fund's trade recorded in G5 under a CUSIP or ISIN key whose G4
     `security_parsekey` gives a Bloomberg key is gathered under that Bloomberg key, so a security the page shows
     under one key carries every trade the fund made in it. Measured on the round-21 real run: 7 GQGU securities
     folded into their Bloomberg keys by round 20 lost their 86 markers, because the publisher groups G5 rows by the
     recorded key. Reuse the join the trend stage applies to G5 rows (`gold_buying_trend.build`: `parsekey_map(g4)`
     and `identity_maps`); do not derive a second rule.
- Rulings at the cut (issuer): the fund market value read for the markers' basis points is widened through the page day
  too, so a page-day marker states its basis points. In the script a marker whose end is after the object's `asof` is
  kept by `plan` and drawn at the chart's right edge; it is in the trade list either way. The script builds its nodes
  with `createElement` / `createElementNS` as today, never `innerHTML`. No key is added to the chart object. The audit
  page is untouched. Cause D of the R3 read (a trade under another key) is item 4 where the other key is a CUSIP or
  ISIN with a parsekey; any other shape of cause D is not in this cell. Item 4 has no check file of its own: the cell
  adds a package test for it (a fund's trade under a CUSIP key with a G4 parsekey row appears as a marker under the
  Bloomberg key), and the proof is the issuer's real run: total markers per fund equal the run before the fold for
  all 13 funds, GQGU's 7 Bloomberg keys hold the 86, and 0 dialogs show a buying section above "No trades".
- **Organic trigger:** any security dialog on the live page; the issuer's real run re-reads the 11 strips of row Z-S59.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 6d7cd1fe3c or later)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC3.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `render.py`: `_month_chart(mark, end=None)` and `_month_words(mark, end=None)` count months back from `end`; a 13-token mark draws 13 cells whose first and last carry a two-digit year (`data-m="Oct 25"`). The two call sites pass the trend row's `window_end`; the same row carries `window_start`. `MONTH_CSS` prints each label with `content:attr(data-m)`.
- `render.CHART_SCRIPT` is the page's ONE inline script, plain text in a Python string. `plan(s, from, to)` returns the range's priced points, segments, gaps and markers (it keeps markers with `m.end<=to`); `nohist(s)` returns the object's words or the sentence only when `s.currency==null`; `draw(f, o, rg)` prints "No price on file in this range." when the plan holds no point and otherwise draws; each marker is placed at its end date on the y of the nearest priced point; `putTrades` writes the trade list when the object loads. `window.rfChart` exposes the pure functions for the tests, which run the script under node in a vm context with a stub document and window; `pm-1.AC2.py` arm (g) drives `draw` itself through a stub DOM built on `createElement` / `createElementNS`, so build nodes that way. Keep it ONE bare inline script (`render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`).
- `trade_markers.markers(trades, fund_mv_by_date)` skips an unknown action and a null `est_notional` today. `publish_page._chart_reads` reads the trades and the funds' market values from the window's first day through the as-of day; `_build_charts` hands them to `trade_markers.markers`. The page day's G5 partition and G1 report exist when the page is published.
- Existing package tests pin the strip's markup, the script's sentences and the markers' inputs in places; re-pin them and say which in the report.
- The page's byte budget matters: the real page is 1,688,519 B against a 1,950,000 B cap; `data-part` is written on at most one cell per strip.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~12/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r22pm1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/trade_markers.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the strip's first cell carries `data-part` when the window starts inside that month, and only then; the words mark it; the stylesheet shows it; pl-1.AC1, ml-1.AC1 and pd-2.AC1 still PASS; control: the round-21 strip holds (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC1.py`)
- **AC2** -- `nohist` for a stored-currency security with no priced point; `curve` for one, two and no priced points; each sentence once in the script; the script's own draw makes no svg where there is no curve; nc-1.AC1, tl-1.AC1 and md-1.AC2 still PASS; control: node runs the script (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC2.py`)
- **AC3** -- a zero-dollar trade makes no marker; the chart object lists a marker for a trade ending on the page day while its prices still end at the as-of day; co-1.AC1, co-1.AC2 and tl-1.AC1 still PASS; control: the fixture's G5 holds the page-day trade (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC3.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): a reader can tell the strip's first month is partial; a security shown under one key lists every trade the fund made in it; a dialog with no curve says why and still lists its trades; no marker is a zero-dollar trade; a page-day trade is on the list and at the chart's right edge.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-pm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-pm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pm-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-pm-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~12/ETFS_RIVALS.TO-RIV-pm-1.a-part-month-is-marked-no-curve-where-there-is-none-honest-markers.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pm-1.a-part-month-is-marked-no-curve-where-there-is-none-honest-markers`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; each call site and the value it now passes as `start`; where in the script the no-curve branch sits and how a marker after `asof` is placed; how the publisher's reads were widened to the page day (trades and fund market value); how item 4 keys the G5 rows, which function of the trend stage it reuses, and the name of the test that pins it; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.12 (round 22 appended). Source: ROUND_ANALYSIS.round20 @c9a9e27770 rulings R2 (items 2 and 4) and R3, and the R3 read @ad9f13a0bb (causes A and C); R2 items 1 and 3 were built in round 21. No ENDPOINT text changes. Not cut here: cause D of the R3 read (a trade under another key), traced first. Chain `~12`, slot `~12`, position 1 of 1. Check files drafted by a helper under the issuer's brief in the round-21 worktree and re-run by the issuer at base 6d7cd1fe3c: pm-1.AC1 FAIL 5, pm-1.AC2 FAIL 4, pm-1.AC3 FAIL 2 on the build arms; every control PASSES. AMENDMENT 1 (before any worker was spawned): interface item 4, the marker one-key rule, on the CTO's ruling msg 31031 of row ETFS_RIVALS-Z-C-S64 (BLOCKING: the Lambda deploy waits on it). No criterion added; its proof is the issuer's real run as that ruling words it.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>22</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<status>complete</status>
