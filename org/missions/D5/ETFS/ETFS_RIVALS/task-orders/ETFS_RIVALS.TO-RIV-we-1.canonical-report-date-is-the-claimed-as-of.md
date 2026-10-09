# ETFS_RIVALS task order -- `RIV-we-1` -- WORKSTREAM 3: A BLOOMBERG CANONICAL ROW'S REPORT DATE IS THE VENDOR'S CLAIMED AS-OF DATE; THE DELIVERY DAY IS KEPT AS DELIVERED_ON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-we-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~27</issued_to>
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

### `RIV-we-1` -- a Bloomberg canonical row's report date is the vendor's claimed as-of date; the delivery day is kept as `delivered_on` (WS3 item 6, the repeat-day remedy; CTO ruling ADDENDUM 2 @9f0a957c00, row ETFS_RIVALS-D1-S5) -- APPENDED 2026-10-09, revision 1.21
- Measured: for every CGIC capture 2026-10-02..10-06 the Bloomberg bronze sidecar's `claimed_report_date` is one trading day
  BEFORE the delivery (requested) date (10-05 capture claims 10-02; 10-06 claims 10-05), while
  `gold_canonical_shape.build_bloomberg_rows` stamps `extra_attributes.bloomberg.source_report_date` from the silver row
  (= the delivery date). The calendar (`gold_holdings_coverage`) reads the claim and so marks those days `repeat`; the trade
  windows (`gold_trade_schedule.infer_windows`, RIV-wd-1) read `source_report_date`. Ruled: the claim is the as-of (the
  delivery carries a one-trading-day lag); `source_report_date` takes it.
- Interface (`gold_canonical_shape.py` only, plus tests; NOT loaded by the site-Z vehicle, so no site-Z half):
  1. `build_bloomberg_rows(..., claimed_report_date=None)`: `extra_attributes["bloomberg"]` carries `source_report_date` =
     the claim (ISO), `delivered_on` = the function's `report_date` (the delivery day), `report_date_claim` = `"MEASURED"`.
  2. No claim (None): `source_report_date` = the trading day before `delivered_on` (`lib.trading_calendar`),
     `report_date_claim` = `"INFERRED"`.
  3. The caller (around line 894) passes the claim of the capture it read: the bronze sidecar's
     `claimed_report_date[fund]` for that silver object (the sidecar `_bbg_latest` selected), so every Bloomberg row carries it.
  4. The canonical `report_date` column (the partition / delivery day) is unchanged; only the attributes above move. Existing
     tests stay green except those pinning the old `source_report_date` (each named in the report).
- Out of bounds: `gold_trade_schedule.py`, `gold_holdings_coverage.py`, `render.py`, `publish_page.py`,
  `enrichment_bloomberg.py`; no S3, no deploy. The proof that CGIC's windows move a trading day earlier (and a control fund
  stays byte-equal) is the issuer's real run at the drain; the deploy follows the round-28 J1 reads under its own pair.

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

## WORKSTREAM 3 (the audit's exclusion line; no trade below tolerance or on a repeat day; the header Period bar) -- APPENDED 2026-10-09, revision 1.20 of this file

Issuer `2.0.0_SA_COO~V1`. Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 1
(1.0.0_SA_CTO~DELL1 msg 1852, @a50caca634), on Andrew-direct comments 4-7 (record
`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @588865eef8).
Item 8 (the Direction Verdict prompt) is WS3's SECOND issuance, cut only after aw-1's J1 read at the 13:00Z sweep. WS3 carries
the three WS2 guards and takes no file a live WS2 order owns: `render.py` belongs to RIV-wc-1, so items 4 and 7 are
`RIV-wc-2`, the next order on wc-1's chain (same worker, after wc-1 is terminal). Two chains: `RIV-wd-1` alone; `RIV-wc-1 -> RIV-wc-2`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-1.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `build_bloomberg_rows` (around line 549) writes `extra_attributes['bloomberg']` at about line 602; the production call is around line 894 (`bbg[f][1]` is the silver object `_bbg_latest` chose). Read `_bbg_latest` (line 339) to find that capture's bronze sidecar and its `claimed_report_date` (a dict fund -> ISO date).
- Test fixtures: `data/etfs/scripts/rivalfunds/tests/test_r6nm1_names.py` calls `build_bloomberg_rows` with a fixture resolver; the check `we-1.AC1.py` does the same.
- `lib/trading_calendar.py` gives the previous trading day (read it; do not edit it).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~27/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W27-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-1.AC1.py`).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-we-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~27/ETFS_RIVALS.TO-RIV-we-1.canonical-report-date-is-the-claimed-as-of.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-we-1.canonical-report-date-is-the-claimed-as-of`. Report once: AC1's verdict line with the output above it; any judgment criterion left
UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the suite's final line; every existing test assertion changed and
why; rows filed (id + one line); anything the issuer must do at the merge (a hookup line in a shared file is the issuer's).
Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Workstream 3, placed by 1.0.0_SA_CTO~DELL1 msg 1852 (ADDENDUM 1 @a50caca634)
(`ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` @f26ff8fbbc) on Andrew-direct ~05:1xZ (@588865eef8).
PRD v0.21 (ADMITTED). Decomposition revision 1.20. Cell id and slot listed against every existing id in the project tree
before naming (0 hits for RIV-wd-1, RIV-wc-2 and slot ~26; ~25 continues its chain; control: slot ~22's branch found). Check dry-run at the base:
FAIL as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<workstream>3b</workstream>
<slot>~27</slot>
<fabric>dell1</fabric>
