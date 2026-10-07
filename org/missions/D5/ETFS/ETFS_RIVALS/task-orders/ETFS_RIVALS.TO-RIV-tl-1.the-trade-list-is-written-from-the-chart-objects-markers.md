# ETFS_RIVALS task order -- `RIV-tl-1` -- ROUND 18 (REPAIR): THE DIALOG'S TRADE LIST IS WRITTEN FROM THE CHART OBJECT'S MARKERS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-tl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~8</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (one static sentence and one function in the page's inline script)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file and the round-17 real-run record
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Rounds 15 to 17 built the security dialog's price curve: each dialog holds one chart frame per fund (`<div class=rf-chart data-chart-fund=... data-chart-key=...>`) with a status line, three range buttons and a static trade list (`[data-chart-trades]`); the page's ONE inline script (`render.CHART_SCRIPT`) fetches the fund's chart object and draws the curve and the trade markers. All of that is merged. **This order, round 18, is one small repair.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-tl-1` -- the dialog's trade list never says "No trades in the last 365 days" about a window it has not read (FWD-22, F.7; row Z-S56)
- Measured (round-17 real run, day 2026-10-06): 618 chart frames carry the static words "No trades in the last 365 days";
  542 of them belong to a fund-security whose chart object holds one or more markers; 77 more list fewer trades than the
  object holds markers. The static list is built from the trades in the page context; the markers from the fund's trades
  over 365 days.
- Interface: `render._trade_list(trades)` with no trade in the page context returns `<p data-chart-trades>` holding exactly
  `"The fund's trades over the last 365 days load with the chart."`; with context trades it lists them as today. The
  static page no longer prints "No trades in the last 365 days" anywhere. The page's one script gains a pure function
  `tradelines(markers)`, exposed as `window.rfChart.tradelines`: no marker -> `["No trades in the last 365 days"]`;
  otherwise one `words(m)` line per marker, NEWEST first by `end` (ties by `start`, newest first), at most 20 lines, and
  when there are more a last line `"and <N> earlier trades in the last 365 days."` (`"trade"` when N is 1). When a chart
  object loads, the script replaces the content of the frame's `[data-chart-trades]` element with those lines built from
  ALL of the security's markers in the object (not the chosen range), for a holding with or without a stored currency
  (so before the `nohist` return). On a failed or missing object the static element stays as rendered.
- Rulings at the cut (issuer): the list is written once per object load and is not redrawn on a range click. A line is
  text (`textContent`), never markup. The AUDIT page is untouched. `round15/checks/md-1.AC1.py` pins the static words
  "No trades in the last 365 days" for the fixture's IDVZ Apple frame; the cell may change that one expected sentence to
  the new static sentence (and the docstring line that quotes it), and nothing else in that file.
- **Organic trigger:** opening any security dialog on the live page; the issuer's real run re-measures the 618.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 07ff6ebe34 or later)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tl-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where the docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `render._trade_list(trades)` today returns `<p data-chart-trades>No trades in the last 365 days</p>` when the context holds no trade, else `<ul data-chart-trades>` with one `<li>` per trade.
- `render.CHART_SCRIPT` is plain text in a Python string. `draw(f, o, rg)` is called once when the object loads (from `init`) and again on every range click; `init` is where the object arrives. `words(m)` already writes a marker's line. `nohist(s)` returns early for a holding with no stored currency. `window.rfChart` exposes the pure functions (`plan`, `words`, `nohist`) for the tests, which run the script under node in a vm context with a stub `document` and `window`; `node --check` parses it.
- Keep it ONE bare inline script: `render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`. The script text must not contain the characters that would close its own block.
- The element may be a `<p>` or a `<ul>` when the script arrives; replace its content so the result is readable in both (for example empty it and append one child per line).
- Existing package tests pin the old static sentence in several places (the md-1 tests among them); re-pin them to the new static sentence and say which in the report.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/` except the one check file named in your `<paths>`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~8/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r18tl1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC1.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the static sentence; `tradelines` under node (none, order, the 20-line cap and its last line); the script reads `data-chart-trades`; nc-1.AC1, md-1.AC1 and md-1.AC2 still PASS; control: node runs the script and one context trade is still listed (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tl-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): in a browser, a dialog's trade list agrees with its chart's markers and with the buying section above it.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-tl-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tl-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-tl-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~8/ETFS_RIVALS.TO-RIV-tl-1.the-trade-list-is-written-from-the-chart-objects-markers.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-tl-1.the-trade-list-is-written-from-the-chart-objects-markers`. Report once: the mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the exact lines you changed in `md-1.AC1.py`; where in the script the list is written and that it runs before the `nohist` return; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.8 (round 18 appended). Source: row ETFS_RIVALS-Z-S56 @b91a3695c0 (BLOCKING, INERT), ruled by the issuer inside cell RIV-md-1's surface: no ENDPOINT text changes (F.7 says the dialog lists the fund's trades in the security; this makes the list cover the window it names). Chain `~8`, slot `~8`, position 1 of 1. Check written and dry-run at base 07ff6ebe34 by the issuer: tl-1.AC1 FAIL 5 failures as expected (arms a to e; the control f PASSES).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>18</round>
<slot>~8</slot>
<fabric>site-z</fabric>
