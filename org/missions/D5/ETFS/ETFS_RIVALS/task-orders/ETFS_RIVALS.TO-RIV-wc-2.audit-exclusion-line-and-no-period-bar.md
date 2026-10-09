# ETFS_RIVALS task order -- `RIV-wc-2` -- WORKSTREAM 3: THE AUDIT'S EXCLUSION LINE READS AS ITS OWN LINE, NAMING WHAT IT EXCLUDES; THE HEADER PERIOD BAR IS GONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wc-2</owned_cells>
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

### `RIV-wc-2` -- the audit's exclusion line reads as its own line, naming what it excludes; the header Period bar is gone (WS3 items 4 and 7)
- Measured: `render.py` writes, inside each audit window above the trade table, "<n> money-market line(s) traded: cash
  management, not a holding decision, so not shown as trades (as in the rankings and the trend)." (about lines 392 and 431).
  Andrew read it as naming the trade beneath it ("Tokyo Electron being "excluded" becuse its a cash management operation?").
  The page header carries a PERIOD row (30d / 90d / 365d with their dates) beside the peer-group rows; the ranking panels
  have their own period controls. Andrew: "we do not need this "Period" component in the top of the page anymore".
- Interface (`render.py` and its tests; the next order on wc-1's chain, so it starts from wc-1's merged `render.py`):
  1. The exclusion line names the excluded line(s): the security name (or identifier) and the amount traded, e.g.
     "Left out: 1 money-market line traded (JPMorgan US Government Money Market, $2.1m): cash management, not a holding
     decision." It sits in its own block, visually apart from the trade table (not immediately above the first row), so it
     cannot be read as describing the row beneath it.
     The carrier: the audit window dict gains `cash_equiv_lines`, a list of `{security_key, name, est_notional}`, one per
     excluded money-market line; render from it when present, and from the count alone (as today) when absent. The
     window dict is built in `publish_page.py`, which RIV-wa-1 owns: populating `cash_equiv_lines` there is the issuer's
     hookup at the merge, not this cell's.
  2. The header's PERIOD row is removed from the main page. The ranking panels' period controls and the 30/90/365 data stay.
     No other header row changes; the page keeps exactly ONE inline script.
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

## WORKSTREAM 3 (the audit's exclusion line; no trade below tolerance or on a repeat day; the header Period bar) -- APPENDED 2026-10-09, revision 1.20 of this file

Issuer `2.0.0_SA_COO~V1`. Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 1
(1.0.0_SA_CTO~DELL1 msg 1852, @a50caca634), on Andrew-direct comments 4-7 (record
`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @588865eef8).
Item 8 (the Direction Verdict prompt) is WS3's SECOND issuance, cut only after aw-1's J1 read at the 13:00Z sweep. WS3 carries
the three WS2 guards and takes no file a live WS2 order owns: `render.py` belongs to RIV-wc-1, so items 4 and 7 are
`RIV-wc-2`, the next order on wc-1's chain (same worker, after wc-1 is terminal). Two chains: `RIV-wd-1` alone; `RIV-wc-1 -> RIV-wc-2`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wc-2.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- This is the NEXT order on your chain: you finished RIV-wc-1 in this same worktree; build on it.
- `render._trades(fund, wmax)` renders an audit window (the exclusion strings are near lines 392 and 431); `render._controls(ctx, funds, opening)` renders the header (the PERIOD row is the `rf-periods` block); `render._component_switch()` renders the ranking panels' period controls, which stay.
- The carrier `cash_equiv_lines` is a list of `{security_key, name, est_notional}` on the window dict; render from it when present, from the count `cash_equiv` alone when absent. Do not edit `publish_page.py` (another cell owns it).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~25/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W25-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wc-2.AC1.py`).
- **J1** (judgment): on the issuer's real run (the main page and the CGIC audit opened in a browser), the header carries no Period row, the ranking panels still switch periods, and the audit's exclusion line names the excluded line apart from the trade table (graded by 3.0.0_SA_CVO~RV1, never by you).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wc-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/wc-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wc-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~25/ETFS_RIVALS.TO-RIV-wc-2.audit-exclusion-line-and-no-period-bar.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wc-2.audit-exclusion-line-and-no-period-bar`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<workstream>3</workstream>
<slot>~25</slot>
<fabric>dell1</fabric>
