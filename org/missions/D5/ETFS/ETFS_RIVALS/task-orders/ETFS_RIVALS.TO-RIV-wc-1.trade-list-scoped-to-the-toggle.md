# ETFS_RIVALS task order -- `RIV-wc-1` -- WORKSTREAM 2: THE SECURITY DIALOG'S TRADE LIST FOLLOWS THE SELECTED WINDOW, BEHIND A CLOSED DISCLOSURE; AN ADJUSTED SERIES SAYS SO

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~25</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wc-1` -- the security dialog's trade list follows the selected window, behind a closed disclosure; an adjusted series says so (WS2-c)
- Measured: `render.py` writes a fixed heading `HEADP = "<p data-chart-trades-head>Trades in the last 365 days</p>"` and
  `_trade_list`; the page script's `putTrades` fills the list from every marker of the chart object and ignores the range
  toggle (`draw(f,o,rg)`, the `[data-chart-range]` click handler). Andrew: the 365-day list "was not ... asked for if
  you're looking at the 30d Toggle. That should at the very least be behind a dropdown, and it should be scoped for the
  toggle value".
- Interface (`render.py` only, plus its tests):
  1. The list sits inside `<details data-chart-trades-box>` with NO `open` attribute; its `<summary>` is the heading.
     No static text names 365 days.
  2. The page script exposes `window.rfChart.tradehead(rg)` -> `"Trades in the last 30 days"` / `"... 90 days"` /
     `"... 365 days"` for `R30` / `R90` / `R365`, and `window.rfChart.tradelines(markers, from)` -> the trade lines of the
     markers whose `end` is on or after `from` (the window's first day), oldest first, worded as today's `tradelines`.
  3. On every `draw` (first load and every toggle click) the heading and the list are rewritten for the selected window;
     an empty window says `"No trades in the last <n> days."`.
  4. When the chart object's security entry carries a non-empty `adjustment` (WS2-a's field), the dialog shows one muted
     line under the chart: `"Prices before <ex_date> are adjusted for a <ratio>-for-1 split"` (a reverse split as
     `"1-for-<1/ratio> reverse split"`), plus `" (found by web search)"` and the link when `claim` is `INFERRED`.
  5. Existing tests that pin the old heading (`test_r21pl1_strip_and_caption.py`, `test_r18tl1_trade_list_from_markers.py`)
     are updated to the new shape; every other test stays green.
- Out of bounds: no S3, no deploy, no other module.

### The workstream's guards (verbatim)

## WORKSTREAM 2 (split-adjusted history; the dramatic-move lookup; the trade list scoped to the toggle) -- APPENDED 2026-10-09, revision 1.19 of this file

Issuer `2.0.0_SA_COO~V1` (dell1). Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md`
(1.0.0_SA_CTO~DELL1, msg 1762, @f26ff8fbbc), on Andrew-direct ~05:1xZ
(`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @9d08dd64d4).
A workstream, not a round: round 28 stays frozen on its three acts. Three cells, three chains, no edge: each cell owns a
disjoint write set and they meet only through two stated contracts (the corporate-action row shape; the chart object's
`adjustment` field). GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the
2026-10-09 11:00Z vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py`
(a cell that finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-c.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `render.py`: `HEADP` and `_trade_list` (about line 2024); the page script is the string `CHART_SCRIPT` (around lines 1841-1935): `tradelines`, `putTrades`, `draw(f,o,rg)`, the `[data-chart-range]` click handler and `window.rfChart` (what `test_r17nc1_no_currency_no_curve.py` runs in node with `vm`). The page carries exactly ONE inline script; keep it one.
- The chart object's security entry gains `adjustment` (a list of `{event_type, ratio, ex_date, claim, source_url}`) from cell RIV-wa-1; render item 4 from it and test it with a fixture entry.
- node is on PATH; the check and test_r17nc1 run the script under node `vm`.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~25/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W25-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r21pl1_strip_and_caption.py
data/etfs/scripts/rivalfunds/tests/test_r18tl1_trade_list_from_markers.py
data/etfs/scripts/rivalfunds/tests/test_ws2_wc1_trade_list_scope.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-c.AC1.py`).
- **J1** (judgment): on the issuer's one real run (a page rendered with this code, opened in a browser), the dialog's trade list is closed by default, its heading names the selected window, and on 30d it lists only the last 30 days' trades (graded by 3.0.0_SA_CVO~RV1, never by you).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-c.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~25/ETFS_RIVALS.TO-RIV-wc-1.trade-list-scoped-to-the-toggle.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wc-1.trade-list-scoped-to-the-toggle`. Report once: AC1's verdict line with the output above it; any judgment criterion left
UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the suite's final line; every existing test assertion changed and
why; rows filed (id + one line); anything the issuer must do at the merge (a hookup line in a shared file is the issuer's).
Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Workstream 2, placed by 1.0.0_SA_CTO~DELL1 msg 1762
(`ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` @f26ff8fbbc) on Andrew-direct ~05:1xZ (@9d08dd64d4).
PRD v0.21 (ADMITTED). Decomposition revision 1.19. Cell id and slot listed against every existing id in the project tree
before naming (0 hits for RIV-w[abc]-1 and slots ~23-~25; control: slot ~22's branch found). Check dry-run at the base:
FAIL as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<workstream>2</workstream>
<slot>~25</slot>
<fabric>dell1</fabric>
