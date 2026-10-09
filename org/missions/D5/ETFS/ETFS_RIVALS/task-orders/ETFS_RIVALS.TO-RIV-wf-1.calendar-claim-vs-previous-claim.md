# ETFS_RIVALS task order -- `RIV-wf-1` -- WORKSTREAM 3: THE HOLDINGS CALENDAR CLASSIFIES A CAPTURE AGAINST THE PREVIOUS CAPTURE'S CLAIM; DELIVERED_ON IS THE REQUESTED DATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~29</issued_to>
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

### `RIV-wf-1` -- the holdings calendar classifies a capture against the PREVIOUS capture's claim (new / repeat / regressed); a Bloomberg row's delivered_on is the requested date (CTO ruling ADDENDUM 4, msg 2128; row D1-S7) -- APPENDED 2026-10-09, revision 1.23
- Measured: canonical_shape partitions are the vendor's claimed as-of (date=2026-10-05 holds capture 20261007T110910Z,
  requested 10-06, claims 10-05); the calendar (`gold_holdings_coverage.classify`) compares the claim with the REQUESTED
  day, so CGIC, whose file always lags one trading day, reads `repeat` every day (10-01..10-06) although each capture is a
  new report. RIV-we-1 set `delivered_on` to the partition (the as-of), not the delivery day.
- Interface:
  1. `classify(expected, actual, periodic, prev_actual=None)`: with a previous capture's claim for the same fund and
     source: newer -> `new`, equal -> `repeat`, older -> `regressed`. With none (the first capture), today's rule. `gap`
     (no capture, undated, or dated after the expected day) and `periodic` keep their meaning. `STATUSES` gains `regressed`.
  2. `build_rows` passes each fund-source's previous capture claim, in expected-day order.
  3. `gold_canonical_shape.build_bloomberg_rows(..., requested_date=None)`: `delivered_on` = the capture's requested date
     (the sidecar's `requested_date`, passed by the caller); None -> the partition, as today. Forward-only (no rebuild).
  4. `render.py` `CAL_STATUSES` and `page_theme.py` show `regressed` with its own label and color; the page keeps ONE script.
- Out of bounds: `gold_trade_schedule.py`, `publish_page.py`, `price_series.py`, `enrichment_bloomberg.py`; no S3, no
  deploy (WS2 guards).

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

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wf-1.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `gold_holdings_coverage.py`: `classify` (line ~119), `build_rows` (~330, observations per fund in expected-day order), `STATUSES` (~90); its tests test_g21_holdings_coverage.py. `gold_canonical_shape.py`: `build_bloomberg_rows` and `_bbg_claim` (RIV-we-1) -- the sidecar it reads also carries `requested_date`.
- `render.py` `CAL_STATUSES` (line 41) and the calendar cell rendering; `page_theme.py` line ~137 colors `td[data-status=...]`. The page keeps exactly ONE inline script.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~29/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W29-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/page_theme.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wf-1.AC1.py`).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wf-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wf-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~29/ETFS_RIVALS.TO-RIV-wf-1.calendar-claim-vs-previous-claim.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wf-1.calendar-claim-vs-previous-claim`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<workstream>3d</workstream>
<slot>~29</slot>
<fabric>dell1</fabric>
