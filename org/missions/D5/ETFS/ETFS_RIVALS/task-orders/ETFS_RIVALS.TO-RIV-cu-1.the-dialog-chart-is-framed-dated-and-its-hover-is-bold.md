# ETFS_RIVALS task order -- `RIV-cu-1` -- ROUND 24: THE DIALOG CHART IS FRAMED, DATED, AND ITS HOVER IS BOLD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-cu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~14</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the page's inline script and two stylesheet strings)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the round-22 analysis ADDENDUM 1 and 2, and Andrew's words
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. Each dialog section draws a price chart with buy and sell markers by the page's one inline script. **This order, round 24, is one cell on that chart's look: Andrew read the live page and asked for a framed chart with dated x-ticks, a bold read-out and a dramatic marker tooltip.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-cu-1` -- the dialog chart is framed, its x-axis is dated, its hover read-out is bold and focal, and a buy or sell marker has a dramatic tooltip (Andrew-direct 2026-10-07 ~19:0xZ; analysis round 22 ADDENDUM 1 and 2)
- Measured on the served page (rounds 15 to 23): the chart is a 600 x 200 svg with no border and no x-axis label; the
  hover read-out is one `<p class="rf-ch-read">` under the chart in the dialog's body type; a marker's hover text is the
  svg's own `<title>` (a small delayed browser tooltip). Andrew's words: the price/date read-out "should be much more focal,
  bold, and obvious"; the tooltip, "especially when hovering over a buy/sell moment, should be much more dramatic"; "a box
  around the chart element itself with clear dates on x-ticks, give it a little more space and make it more of an event".
  "The mechanics are all there": no change to the data.
- Interface (all in `render.py` -- `CHART_SCRIPT`, `CHART_CSS` -- and `page_theme.py`; one inline script as today):
  1. **Dated x-ticks.** A new pure function `window.rfChart.ticks(pl)` takes a plan (`rfChart.plan(s, from, to)`, whose
     `a` and `b` are the range's first and last day numbers) and returns an array of 4 to 7 objects `{x, label}`: `x` a day
     number with `pl.a <= x <= pl.b`, strictly increasing; `label` a date a reader can place: day and month ("8 Sep") for a
     range of 100 days or fewer, month and two-digit year ("Oct 25") for a longer one; no two labels equal. The script's
     draw writes one svg `text` per tick carrying the attribute `data-tick` with that label as its text, under the plot.
  2. **The frame and the room.** The chart's svg sits inside an element of class `rf-ch-frame`; `render.CHART_CSS` gives
     `.rf-ch-frame` a border of at least 1px solid, a border-radius, a padding of at least 10px and a background; the svg's
     viewBox height is at least 280 (today 200) with the same 600 width.
  3. **The read-out.** The read-out element (class `rf-ch-read`) is placed BEFORE the svg inside the frame, and
     `render.CHART_CSS` gives `.rf-ch-read` a `font-size` of at least 20px and a `font-weight` of at least 700 (the dialog's
     body is 17px, weight 400), stated as plain numbers in px. On a pointer move over the curve it shows the price with
     its currency and the date, as today; the price and the date are each in their own child element (`data-read="price"`,
     `data-read="date"`) so the price can be the larger.
  4. **The marker tooltip.** The script creates ONE element of class `rf-ch-tip` per chart (hidden by default: the
     attribute `hidden`), inside the frame. On `mouseover` (and `focus`) of a marker it is shown (no `hidden`), carries
     `data-side="buy"` or `"sell"`, and its text states the side in a word ("Bought" / "Sold"), the dollars, and the date
     or dates -- the content of `rfChart.words(m)` at least; on `mouseout` (and `blur`) it is hidden again. `CHART_CSS`
     gives `.rf-ch-tip` a `font-size` of at least 16px, a `font-weight` of at least 600, `position:absolute`, a padding and
     a coloured background or border that differs by `data-side` (green for buy, red for sell, the script's `G` and `X`
     colours). Each marker is focusable (`tabindex="0"`). The svg `<title>` of a marker stays.
- Rulings at the cut (issuer): nodes are built with `createElement` / `createElementNS`, never `innerHTML`. No key is
  added to the chart object and no gold table, price series, marker or window changes. The audit page is untouched (it
  has no script). The dialog's static trade list and month strip stay as they are. Everything rounds 15 to 23 built
  stays: every existing check file under `round15/checks/` still ends `PASS 0 failures`. The page stays under its
  1,950,000-byte cap; the script may grow by at most 3,000 bytes (today 7,369) and the frame adds no per-dialog markup
  to the static page (it is built by the script).
- Rulings on the check drafter's questions (issuer; the check files accept exactly these): a tick's label names the date
  its own `x` falls on; the 100-day boundary is `pl.b - pl.a`; the price child shows the stored currency code, not a
  sign; the date child names the same point as the price; the tooltip states "Bought" or "Sold" (never both), the
  dollars with thousands separators and the date or dates; the tooltip's colour by side is set by `CHART_CSS` rules on
  `[data-side=buy]` and `[data-side=sell]`, not by inline style; hidden means the attribute `hidden`; a marker is a
  circle with a `title` child and `data-m`, focusable with `tabindex="0"`; there is exactly one frame, one read-out and
  one tooltip per chart after every range switch; CSS lengths are in px and the frame's padding is at least 10px on
  every side; the static page carries no `rf-ch-frame` or `rf-ch-tip` markup.
- **Organic trigger:** any security dialog on the live page, pointer over the curve and over a buy or sell marker.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD edec515854 or later)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC3.py` before you build. They run the page's script under node in a vm context with a stub document and window and drive the script's own draw; they fire `pointermove` then `mousemove` on the svg, `mouseover` / `mouseout` and `focus` / `focusin` / `blur` / `focusout` on a marker.
- `render.CHART_SCRIPT` is the page's ONE inline script, plain text in a Python string (7,369 bytes). `plan(s, from, to)` returns the range's points, segments, gaps, markers and its first and last day numbers `a` and `b`; `draw(f, o, rg)` builds `div.rf-ch-out` holding the svg (viewBox `0 0 600 200`, constants `W=600,H=200,L=46,R=8,T=8,B=20`), the read-out `p.rf-ch-read` and the trade list; each marker is a circle with `data-m` and a `title` child whose text is `words(m)`; a `mousemove` on the svg writes the price and date into the read-out. `window.rfChart` exposes `plan, words, nohist, tradelines, curve` for the tests. `render.CHART_CSS` is the chart's stylesheet string (308 bytes). Keep it ONE bare inline script (`render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`).
- The dialog (`.rf-modal` in `page_theme.py`) is up to 1080px wide with 17px body type.
- Existing package tests and check files pin the script's sentences, the svg's presence and the read-out's class in places (`pm-1.AC2.py`, `md-1.AC2.py`, `tl-1.AC1.py`, `nc-1.AC1.py`, `pc-1.AC1.py`); they must stay green. If a package test pins the viewBox height or the read-out's position, re-pin it and say which line in the report.
- The page's byte budget matters: the real page is 1,690,296 B against a 1,950,000 B cap; the script may grow by at most 3,000 bytes.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~14/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r24cu1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/page_theme.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- `rfChart.ticks(pl)` for a 30-, 90- and 365-day range and one `text[data-tick]` per tick in the drawn svg; control: node runs the script (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC1.py`)
- **AC2** -- the frame, the room and the read-out: one `rf-ch-frame` holding the read-out before the svg, viewBox height at least 280, the price and date children after a pointer move, the two stylesheet rules as numbers; control: the base draw and the CSS parser (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC2.py`)
- **AC3** -- the marker tooltip: one hidden `rf-ch-tip`, shown with its side and words on `mouseover` and `focus`, hidden on `mouseout` and `blur`, focusable markers that keep their `title`, the stylesheet rule and its two sides; regression: one script within its byte bound; control: the stub's events reach a listener (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC3.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run in a browser, never by you; then Andrew's own look): hovering the curve, the price and date are the most prominent text of the chart; hovering a buy or sell marker shows what was traded, when and for how much without reading small text; the chart reads as a framed figure with dates on its x-axis.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-cu-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-cu-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-cu-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/cu-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-cu-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~14/ETFS_RIVALS.TO-RIV-cu-1.the-dialog-chart-is-framed-dated-and-its-hover-is-bold.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-cu-1.the-dialog-chart-is-framed-dated-and-its-hover-is-bold`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the script's byte count before and after; the viewBox and the plot margins you chose and why; where the read-out and the tooltip sit and the type sizes and weights you set, as numbers; how the tooltip is positioned beside a marker; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.14 (round 24 appended). Source: ROUND_ANALYSIS.round22 ADDENDUM 1 and 2 @be5cb4f530; Andrew-direct record @f76452470f. No ENDPOINT text changes. Chain `~14`, slot `~14`, position 1 of 1. Check files drafted by a helper under the issuer's brief (@c7111c1153), re-run by the issuer at base edec515854: cu-1.AC1, AC2 and AC3 each FAIL 6 on arms (a) to (f); every control and regression arm PASSES; the helper's simulated conforming build passes every arm and six planted defects each fail only their own arm.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>~14</slot>
<fabric>site-z</fabric>
