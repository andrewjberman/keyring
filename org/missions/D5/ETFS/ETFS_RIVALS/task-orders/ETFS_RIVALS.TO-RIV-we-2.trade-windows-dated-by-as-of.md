# ETFS_RIVALS task order -- `RIV-we-2` -- WORKSTREAM 3: A TRADE WINDOW IS DATED BY ITS REPORTS' AS-OF DATES; THE DELIVERY DAYS RIDE ALONG

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-we-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~28</issued_to>
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

### `RIV-we-2` -- a trade window is dated by its reports' AS-OF dates; the delivery days ride along (completes CTO ADDENDUM 2 with RIV-we-1; ADDENDUM 3 @9f0a957c00) -- APPENDED 2026-10-09, revision 1.22
- Measured (2.0.0_SA_COO~V1's real run, ~08:2xZ): with RIV-we-1 merged and canonical_shape rebuilt fresh, every fund's
  trade windows were UNCHANGED (0 dates changed of 164 across 13 funds), because `gold_trade_schedule.infer_windows`
  labels each window with the canonical `report_date` (the delivery day) and reads `source_report_date` only for RIV-wd-1's
  repeat test. The ruling says CGIC's windows move a trading day earlier; that needs the window dates themselves.
- Interface (`gold_trade_schedule.py`, plus tests):
  1. Every trade row's `window_start` / `window_end` are the as-of dates of its two reports: the modal
     `extra_attributes.bloomberg.source_report_date` of each report's rows (`_actual_dates`), falling back to the
     canonical `report_date` where no as-of is carried (issuer and home rows).
  2. Two new columns, `window_start_delivered` / `window_end_delivered`, carry the canonical `report_date`s (the delivery
     days); the G5 schema gains them; recon rows carry the same pair.
  3. A fund whose as-of equals its delivery day is unchanged in every column but the two new ones.
  4. Readers that key on window dates (publish_page's audit windows, trade markers, the buying trend) keep working on the
     as-of dates; the existing tests stay green except those pinning a delivery-day window (each named in the report).
- Out of bounds: `gold_canonical_shape.py`, `render.py`, `publish_page.py`, `price_series.py`, `enrichment_bloomberg.py`;
  no S3, no deploy. The served rebuild of the affected (fund, capture) pairs is the issuer's act under its own pair, after
  the round-28 J1 reads (ADDENDUM 3).

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

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-2.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `gold_trade_schedule.infer_windows` (read it whole) labels windows d0/d1 by canonical report_date; `_actual_dates(df)` already reads the modal source_report_date per report (RIV-wd-1). `COLUMNS` and the G5 schema define the row shape; `_pair_rows` writes window_start/window_end.
- Fixtures: the check we-2.AC1.py builds canonical rows with extra_attributes.bloomberg.source_report_date; existing G5 tests are under data/etfs/scripts/rivalfunds/tests/ (test_g52_trade_schedule_v2.py, test_wd1_tolerance_and_repeat.py).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~28/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W28-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-2.AC1.py`).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-we-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/we-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~28/ETFS_RIVALS.TO-RIV-we-2.trade-windows-dated-by-as-of.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-we-2.trade-windows-dated-by-as-of`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<status>complete</status>
<!-- drained 2026-10-09 by 2.0.0_SA_COO~V1: merged 598173c0fa; AC1 PASS 3 of 3 (worker ~28 proof VALID) -->
<round>28</round>
<workstream>3c</workstream>
<slot>~28</slot>
<fabric>dell1</fabric>
