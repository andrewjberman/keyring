# ETFS_RIVALS task order -- `RIV-wd-1` -- WORKSTREAM 3: A SHARE CHANGE IS A TRADE ONLY WHEN THE COUNT MOVED AND IT CLEARS THE 20 BPS TOLERANCE; NO TRADE ACROSS A REPEATED REPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~26</issued_to>
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

### `RIV-wd-1` -- a share change is a trade only when the share count moved and the trade clears Andrew's 20 bps tolerance; no trade is read across a repeated report (WS3 items 5 and 6)
- Measured: `gold_trade_schedule._pair_rows` infers a holding's trade as `q1 - f * q0`, with `f` the median ratio over the
  window's untouched holdings (`FLOW_WINDOW_EPS` 0.001; `flow_adjusted` true past it). In a window with fund flows an
  UNCHANGED holding therefore reads as a trade. The CGIC audit (latest report 2026-10-06, revision 20261008T122342Z-6ea2fb54eece)
  shows 12 such rows, all "flow adjusted": MediaTek 2454_TT 428,000 -> 428,000 (-1,442; window 09-30 -> 10-02), Renault
  RNO_FP 277,771 -> 277,771 (-936; -2,361 in 09-29 -> 09-30), SMC 6273_JP 10,700 -> 10,700 (-36), Jentech 3653_TT 23,000 ->
  23,000 (-77), Taisei 1801_JP 56,900 -> 56,900 (-192), Aura AUGO_US 46,976 -> 46,976 (-158; -399), Grifols GRFS_US
  120,713 -> 120,713 (-407; -1,026), Tokyo Electron 8035_JP 205,000 -> 205,000 (-1,743). Andrew's tolerance (PRD v0.21
  FWD-10 SOURCE): "at a 20bps tolerance it's immediately clear who is discretionary and who is systematic"; today no code
  applies it. The holdings calendar (`gold_holdings_coverage`) marks 10-01, 10-02, 10-05 and 10-06 `repeat` ("report dated
  <d> re-published") while the 10-02 -> 10-05 and 10-05 -> 10-06 windows carry trades.
- Interface (`gold_trade_schedule.py`, and `gold_holdings_coverage.py` only if item 3 needs it; plus tests):
  1. **Unchanged count, no trade.** A holding whose share count is the same in both reports (`q1 == q0`, both > 0) is NEVER
     a trade, whatever the flow factor; it is not emitted as an add or trim.
  2. **The tolerance.** `TRADE_TOLERANCE_BPS = 20`: a candidate trade whose absolute estimated notional is below 20 bps of the
     fund's total (the later report's) market value is not a trade on the page or in the rankings. It is kept as a row with
     `action` `below_tolerance` (or an equivalent flag the readers skip), counted, so the audit can say how many and the
     numbers stay reconstructible. Entries and full exits are trades whatever their size.
  3. **No trade across a repeated report.** Where the later report of a window is a re-publication of the earlier one (the
     same actual report date, the coverage table's `repeat`), the window yields no trade; and the windows and the calendar
     read the same object, so a day the calendar marks `repeat` never carries a trade. Find which of the two is wrong today
     (state it in the report with the two objects read), and make them agree.
     This item is graded by J1 on the issuer's real run over CGIC's actual windows (no trade on a day the calendar marks
     `repeat`); the check's arm (c) is a control (a re-published report with identical counts yields no trade, at the
     base and after).
  4. Readers that count trades (rankings, buying trend, trade markers) skip the rows items 1-3 exclude; existing tests stay
     green except where they asserted an unchanged-count or sub-tolerance trade (each such change named in the report).
- Out of bounds: no S3 write, no deploy; `render.py`, `price_series.py`, `publish_page.py`, `dramatic_move.py`,
  `enrichment_bloomberg.py` untouched (a reader in one of them that needs changing is a row and the issuer's hookup).

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

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wd-1.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- `gold_trade_schedule._pair_rows` (around lines 526-700): the flow factor `f` is the median of q1/q0 over holdings no share-changing event touches; the inferred trade is q1 - f*q0; `flow_adjusted` when |f-1| > FLOW_WINDOW_EPS. `infer_trades(canonical, actions=None, ...)` is the public entry the check calls.
- Fixtures: `data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py` (`_canon`) is the canonical-shape fixture the check copies. The holdings calendar: `gold_holdings_coverage.py` (`classify`, statuses new/repeat/gap/periodic; repeat = 'report dated <d> re-published').
- Item 3 (repeat days) is graded by J1 on the issuer's real run over CGIC's real windows; the check's arm (c) is a control. In your report name the two objects you read to decide which of label and windows was wrong.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~26/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W26-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/trade_markers.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wd-1.AC1.py`).
- **J1** (judgment): on the issuer's real run over CGIC's 2026-09-28..2026-10-06 windows, no unchanged-count row and no sub-20-bps row is shown as a trade, and no trade sits on a day the calendar marks repeat (graded by 3.0.0_SA_CVO~RV1, never by you).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wd-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wd-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~26/ETFS_RIVALS.TO-RIV-wd-1.no-trade-below-tolerance-or-on-a-repeat-day.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wd-1.no-trade-below-tolerance-or-on-a-repeat-day`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<!-- drained 2026-10-09 by 2.0.0_SA_COO~V1: merged 67f42b7329; AC1 PASS 4 of 4 (worker ~26 proof VALID); J1 owed (CVO) after the issuer reads CGIC G1 source_report_date and G2 coverage for 10-01..10-06; row D1-W26-S1 ARMED: publish_page/ai_accounts below_tolerance skips are the issuer hookups -->
<round>28</round>
<workstream>3</workstream>
<slot>~26</slot>
<fabric>dell1</fabric>
