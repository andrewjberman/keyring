# ETFS_RIVALS task order -- `RIV-wa-1` -- WORKSTREAM 2: EVERY PRICE SERIES THE PAGE DRAWS IS ADJUSTED FOR STORED SPLITS; A BIG MOVE WITH NO ACTION ON FILE IS A GAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~23</issued_to>
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

### `RIV-wa-1` -- every price series the page draws is adjusted for stored splits, so a split leaves a continuous curve; a big move with no action on file is a gap (WS2-a)
- Measured: on the 2026-10-08 page, IDVZ's chart object holds `TKOMY_US_Equity` points `[2026-10-05, 49.59, m]`,
  `[2026-10-06, 50.5, m]`, `[2026-10-07, 3.33, m]`: Tokio Marine's 15-for-1 split took effect 2026-10-07 (Andrew), and the
  pre-split closes are drawn unadjusted. Gold corporate_actions stores splits as `event_type` `split`, `ratio` = new shares
  per old share (ANET 4.0, PANW 2.0), `ex_date`, `claim` `MEASURED`; `security_id` there is the Bloomberg form with spaces
  (`TKOMY US Equity`), while gold security_market's is underscored (`TKOMY_US_Equity`).
- Interface:
  1. `price_series.series(g4, g1, keys, start, end, actions=None)`: `actions` is a frame in the corporate_actions shape
     (at least `security_id`, `event_type`, `ratio`, `ex_date`, `claim`; `source_url` optional). For a key, every row
     with `event_type` `split` (a reverse split is a ratio below 1) and an `ex_date` inside `(start, end]` divides every
     price dated before the ex-date by its ratio (cumulative over several rows; market and holding-implied points alike).
     Keys match after mapping spaces to underscores. `cash_div` and other event types adjust nothing.
  2. Each key's result gains `"adjustment"`: a list of `{"event_type", "ratio", "ex_date", "claim", "source_url"}`, one per
     applied row, oldest first; `[]` when none. With `actions=None` the points equal today's output, except item 3.
  3. A drawn price more than 3x, or below one third of, the key's previous drawn price (after adjustment), with no applied
     row between them, is not drawn: point `(d, None, None)` and a gap with reason
     `"the price moved more than threefold in one day and no corporate action is on file"`.
  4. `price_series.load(s, keys, start, end)` also reads every object under gold `corporate_actions/date=<D>/` for the
     window's dates (ALL objects there, including WS2-b's `actions-inferred-*` objects) and passes them as `actions`.
  5. `publish_page._build_charts` copies each series' `adjustment` into the chart object's security entry (`"adjustment"`).
     WS2-c renders it; this cell writes no render code.
- Out of bounds: no S3 write, no deploy; `enrichment_bloomberg.py`, `render.py` and `dramatic_move.py` untouched.

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

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-a.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `price_series.series` today (read it whole): one series per key from gold security_market (`m`) and the funds' implied prices (`i`, USD listings only); `load` reads the two tables through a sink. Its tests: `data/etfs/scripts/rivalfunds/tests/test_r15ps1_price_series.py`, `test_r15pc1_currency.py`, `test_r26rg2_misdated_object_is_not_read.py` -- they must stay green with `actions=None`.
- `publish_page._build_charts` (around line 705) builds each fund's chart object from `price_series.load`; add `"adjustment": ser.get("adjustment", [])` to each security entry. `_thin` must keep the field.
- Corporate actions on S3 (read in `load` only, through the sink): `homes.address("rivalfunds","etfs","gold","corporate_actions","date=")`; columns include `security_id` (spaces), `event_type` (`split`, `cash_div`), `ratio`, `ex_date`, `claim`, and on WS2-b rows `source_url`. Read every `.parquet` under each date in the window; a frame with no `source_url` column reads it as None. A load test uses a memory sink, as test_r15ps1 does.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~23/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W23-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/test_ws2_wa1_split_adjusted_series.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-a.AC1.py`).
- **J1** (judgment): the dialog for Tokio Marine (IDVZ) on the first page published with this code reads a continuous 30d curve near 3.3 across 2026-10-07 and names the 15-for-1 split, the factor coming from a stored row (graded by 3.0.0_SA_CVO~RV1 on the issuer's one real run, never by you).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wa-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-a.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wa-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~23/ETFS_RIVALS.TO-RIV-wa-1.split-adjusted-series.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wa-1.split-adjusted-series`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<slot>~23</slot>
<fabric>dell1</fabric>
