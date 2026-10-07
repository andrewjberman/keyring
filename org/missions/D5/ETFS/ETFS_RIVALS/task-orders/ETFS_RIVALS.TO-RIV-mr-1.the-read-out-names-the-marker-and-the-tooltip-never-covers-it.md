# ETFS_RIVALS task order -- `RIV-mr-1` -- ROUND 25: THE READ-OUT NAMES THE MARKER POINTED AT AND THE TOOLTIP NEVER COVERS IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-mr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~16</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the page's inline script and one stylesheet string)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. Each dialog section draws a price chart with buy and sell markers by the page's one inline script; round 24 gave it a frame, a bold read-out above the curve and a tooltip on each marker. **This order, round 25, repairs two faults the reviewer found in that chart: the read-out can name a different day than the marker's tooltip, and the tooltip can cover the read-out.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-mr-1` -- while a marker is pointed at, the read-out names THAT marker's day and price, and the tooltip never covers the read-out (CVO ADJUDICATION_v28; CTO round-24 analysis msg 31413)
- Measured on the served page (round 24): pointing at a buy or sell marker shows the tooltip for the marker while the
  read-out above the chart keeps the price and date of the last curve position the pointer crossed, so the two can name
  different days; and a marker near the top of the plot flips its tooltip to a position that can cover the read-out.
- Interface (`render.py` `CHART_SCRIPT` / `CHART_CSS` only; one inline script as today):
  1. On `mouseover` or `focus` of a marker the read-out (`.rf-ch-read`) shows the marker's END date in its
     `data-read="date"` child and, in its `data-read="price"` child, the price of the priced point the marker is drawn
     on (the nearest priced point, as the marker's `cy` is computed today) with the stored currency code; a marker
     with no priced point in the range shows the date and no price. On `mouseout` or `blur` the read-out returns to its
     idle prompt until the pointer next moves over the curve. A `mousemove` whose target is a marker does not overwrite
     it (as today: the handler returns for `data-m`).
  2. The tooltip (`.rf-ch-tip`) is positioned only over the svg's own box: its top edge is never above the svg's top
     edge inside the frame, so it cannot overlap the read-out, which sits before the svg. It still flips below a marker
     when there is no room above, and stays inside the frame horizontally.
  3. Everything round 24 built stays: `cu-1.AC1.py`, `cu-1.AC2.py` and `cu-1.AC3.py` still end `PASS 0 failures`; the
     script grows by at most 600 bytes (today 9,348).
- Rulings at the cut (issuer): nodes by `createElement` / `createElementNS`, never `innerHTML`; no key is added to the
  chart object; no data change.
- **Organic trigger:** any dialog chart on the live page, pointer on a marker.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 7f7e680abf or later)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/mr-1.AC1.py` before you build. It runs the page's script under node in a vm context with a stub document and window whose elements have a layout (`getBoundingClientRect`, `offsetWidth`, `offsetHeight`): the frame at the origin, the read-out above the svg, a tip of 220 x 60; it reads the tip's `style.left` / `style.top` in px relative to the frame.
- `render.CHART_SCRIPT` (9,348 bytes) as round 24 left it: the read-out `p.rf-ch-read` sits before the svg inside `div.rf-ch-frame` and gets `data-read="price"`, `"date"` and `"src"` children on a pointer move over the curve; each marker is a focusable circle with `data-m` and a `title`; on `mouseover` / `focus` of a marker the one `div.rf-ch-tip` is shown and placed above the marker, flipping below when its top would be negative relative to the FRAME (not the svg), which is how it can cover the read-out; on `mouseout` / `blur` it is hidden. A marker's `cy` is the y of the nearest priced point.
- `cu-1.AC1.py`, `cu-1.AC2.py`, `cu-1.AC3.py` must still end `PASS 0 failures`; the script may grow to at most 9,948 bytes.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~16/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r25mr1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- on `mouseover` and `focus` of a marker the read-out names the marker's end date and the price of the point it sits on, not the last curve position; on `mouseout` and `blur` it stops naming them; a move over the marker does not overwrite it; the tooltip's top is never above the svg's top edge, so it cannot cover the read-out, and it stays inside the frame; the three round-24 checks still PASS; control: the base draw, its markers and the stub's layout (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/mr-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run in a browser, never by you): pointing at a marker, the read-out and the tooltip name the same day; the tooltip does not hide the read-out for a marker anywhere on the plot.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-mr-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/mr-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-mr-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~16/ETFS_RIVALS.TO-RIV-mr-1.the-read-out-names-the-marker-and-the-tooltip-never-covers-it.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-mr-1.the-read-out-names-the-marker-and-the-tooltip-never-covers-it`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the script's byte count before and after; what the read-out shows while a marker is pointed at and after the pointer leaves it; the rule that places the tooltip, in one sentence; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.15 (round 25 appended). Source: CVO ADJUDICATION_v28 @f97c41e692 (two faults on RIV-cu-1 J1 MET) and the CTO's round-24 analysis msg 31413. Chain `~16`, slot `~16`, position 1 of 1. Check file drafted by a helper under the issuer's brief (@2d317208a8), re-run by the issuer at base 7f7e680abf: mr-1.AC1 FAIL 4 (arms a, b, e, f; c and d pass vacuously at base; the regression g and the control h PASS). The helper's simulated conforming build passes and four planted defects each fail the arms that grade them.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>25</round>
<slot>~16</slot>
<fabric>site-z</fabric>
