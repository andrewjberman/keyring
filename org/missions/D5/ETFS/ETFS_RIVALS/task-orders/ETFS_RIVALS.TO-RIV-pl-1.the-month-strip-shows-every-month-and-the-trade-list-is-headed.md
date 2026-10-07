# ETFS_RIVALS task order -- `RIV-pl-1` -- ROUND 21: THE MONTH STRIP SHOWS EVERY MONTH OF ITS WINDOW AND THE TRADE LIST IS HEADED BY ITS WINDOW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~11</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (render functions, one stylesheet string and the page's inline script)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file and the CVO's ADJUDICATION_v20
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. **This order, round 21, is one small cell on the reviewer's display findings.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-pl-1` -- the month strip shows every month of its window, the trade list is headed by its window, and the chart's currency label clears the axis (FWD-22, FWD-23; CVO row Z-C-S60)
- Measured by the CVO on the round-19 real run: 56 of the 252 year strips have one or more markers in October 2025,
  inside the 365-day trade list and outside the 12-cell strip, whose first cell is November 2025; in 141 dialogs a
  30-day or 90-day buying section sits above the 365-day trade list, and the list carries no heading of its own; the
  "Price in <currency>" label is printed over the axis's top figure when that figure is long (TWD); the drawing uses
  about two thirds of the frame's width.
- Interface:
  1. `render._month_chart(mark, end)` draws EVERY token of the mark, at most 13. When the first and the last cell are
     the same calendar month (a 13-token mark), those two cells carry the month and a two-digit year (`data-m="Oct 25"`,
     `data-m="Oct 26"`); every other cell carries the bare month. A mark of 12 tokens or fewer is drawn as round 19
     drew it. `render._month_words(mark, end)` names the same months the same way.
  2. `render._trade_list(trades)` puts, immediately before the `[data-chart-trades]` element, the caption element
     `<p data-chart-trades-head>` holding exactly `Trades in the last 365 days`, with or without a context trade. The
     script leaves the caption alone when it rewrites the list.
  3. In the page's one script the "Price in <currency>" label is drawn where it cannot overlap an axis figure (right
     aligned at the plot's top right edge), and the chart is as wide as its frame.
- Rulings at the cut (issuer): the stylesheet's month cells must stay readable at 13 cells (the two year-carrying
  labels are five characters). `round15/checks/ml-1.AC1.py` pins round 19's rule that a 13-token mark draws 12 cells
  (its arm (a), and arm (e)'s "12 months at most"); the cell may change those two arms to this cell's rule and nothing
  else in that file. Items 1 and 2 are checked mechanically; item 3 is the CVO's to grade in a browser.
- **Organic trigger:** any security dialog on the live page; the issuer's real run.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 6bee8e3a91 or later)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pl-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where the docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `render.py` today: `_month_chart(mark, end=None)` and `_month_words(mark, end=None)` count months back from `end` and keep the LAST 12 tokens; each cell is `<i class=u data-m=Oct></i>` and `MONTH_CSS` prints `content:attr(data-m)`. A label with a space needs its attribute quoted. `_trade_list(trades)` returns the `[data-chart-trades]` element (a `<p>` holding the static sentence when the context has no trade, else a `<ul>`). In `CHART_SCRIPT`, `putTrades` rewrites that element when the chart object loads, and `draw` prints the currency label with `tx("text",{x:L+4,y:T+8,...},svg,"Price in "+cy)` beside the top axis figure at `x:L-4`.
- Keep it ONE bare inline script (`render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`); the package suite runs the script's pure functions under node and `node --check` parses it.
- `round15/checks/ml-1.AC1.py` arm (a) expects 12 cells for the 13-token mark and arm (e) expects the words to name 12 months at most: change those two arms to this cell's rule (13 cells, "Oct 25" first and "Oct 26" last) and nothing else in that file; quote the lines you change, before and after, in your report. The issuer diffs the file at the merge.
- Existing package tests pin the 12-cell rule and the trade element's markup in places; re-pin them and say which in the report.
- The page's byte budget matters: the real page is 1,640,613 B against a 1,950,000 B cap. The caption costs its bytes once per chart frame (about 700 frames); keep the element as small as the prescribed markup allows.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/` except the one check file named in your `<paths>`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~11/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r21pl1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ml-1.AC1.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a 13-token mark draws 13 cells with the two year-carrying labels; a 12-token mark is unchanged; the caption element sits before the trades element; ml-1.AC1, tl-1.AC1, md-1.AC1, md-1.AC2 and pd-2.AC1 still PASS; control: a 2-token mark and the static sentence hold (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pl-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): a year strip shows a cell for every month the trade list names; the list's caption reads true beside a 30-day or 90-day buying section; the currency label overlaps no axis figure and the chart fills its frame.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pl-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pl-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-pl-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~11/ETFS_RIVALS.TO-RIV-pl-1.the-month-strip-shows-every-month-and-the-trade-list-is-headed.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pl-1.the-month-strip-shows-every-month-and-the-trade-list-is-headed`. Report once: the mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the exact lines you changed in `ml-1.AC1.py`, before and after; where the script draws the currency label now and how the chart is made as wide as its frame; the page-byte cost of the caption per frame; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.11 (round 21 appended). Source: the CVO's L9 grades for rounds 15 to 19, ADJUDICATION_v20 row ETFS_RIVALS-Z-C-S60 @0c69a8829e, ruled by the issuer inside the surfaces of cells RIV-ml-1, RIV-tl-1 and RIV-md-1: no ENDPOINT text changes. Not cut here, carried to the round analysis: row Z-S59's 11 strips, the 41 buying-section counts that differ by one or two trades at a window's edge, and the one zero-price frame (BIDD 6475395Z GR). Chain `~11`, slot `~11`, position 1 of 1. Check written and dry-run at base a9775de871 by the issuer: pl-1.AC1 FAIL 3 failures as expected (arms a, c, d; arms b, e and the control f PASS).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>21</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<status>complete</status>
