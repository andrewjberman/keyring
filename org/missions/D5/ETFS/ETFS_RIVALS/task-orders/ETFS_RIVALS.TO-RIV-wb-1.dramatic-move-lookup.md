# ETFS_RIVALS task order -- `RIV-wb-1` -- WORKSTREAM 2: A DRAMATIC MOVE WITH NO ACTION ON FILE IS LOOKED UP ON THE WEB AND STORED AS AN INFERRED CORPORATE-ACTION ROW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~24</issued_to>
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

### `RIV-wb-1` -- a dramatic move with no action on file is looked up on the web and, when found, stored as an INFERRED corporate-action row (WS2-b)
- Measured: gold corporate_actions date=2026-10-06 and date=2026-10-07 (160 rows each) carry no TKOMY or 8766 row, and no
  date=2026-10-08 object exists. Egress is open except Bloomberg (law 4d77a9c3ea). A SERP client exists:
  `lib/research/management/ceo_search.py` (Bright Data, `BRIGHT_DATA_API_KEY`, `BD_SERP_ZONE`).
- Interface, a new module `data/etfs/scripts/rivalfunds/dramatic_move.py`:
  1. `detect(g4, actions) -> list[dict]`: per security, consecutive stored closes (ascending dates) where the close is
     more than 3x or below one third of the previous one and no `split` or `merger` row of that security has an ex-date in
     `(prior_date, date]`. Each candidate: `security_id`, `date`, `prior_date`, `prior_close`, `close`, `security_name`
     when the frame has one. Keys match across the two forms by mapping spaces to underscores.
  2. `lookup(candidate, search=None) -> dict | None`: builds a query from the security name (or id) and the date (e.g.
     "Tokio Marine Holdings stock split October 2026"), calls `search(query)` -> list of `{title, url, snippet}`, and parses
     an explicit ratio ("15-for-1", "15:1", "1-for-10 reverse", a merger exchange ratio). Found: ONE row in the stored
     corporate_actions shape: `security_id` in the Bloomberg form, `event_type` `split` (or `merger`), `ratio` new-per-old as
     a float, `ex_date` the candidate's date unless the result names another, `claim` `INFERRED`, `source` `web_search`,
     `source_url` the result's URL, `status` `OK`, `row_kind` `event`. Nothing parseable: `None`, never a guessed ratio.
     `search=None` uses the Bright Data SERP the way `ceo_search.py` does (read it; do not edit it).
  3. `write_rows(s, rows, day)` writes one object `address("rivalfunds","etfs","gold","corporate_actions",f"date={day}",
     f"actions-inferred-{revision}.parquet")` through a sink. It is BUILT and tested on a memory sink only: running it
     against live S3 is a served write under guards 1 and 3, not this cell's act.
- Out of bounds: no live search in tests (inject `search`), no S3 write, no deploy, no hookup into the sweep (the issuer adds
  the hookup at the merge); `enrichment_bloomberg.py`, `price_series.py`, `render.py` untouched.

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

- Read the check `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-b.AC1.py` before you build. It FAILS at the base; it is
  your target. Do not edit it.
- Read `lib/research/management/ceo_search.py` for the Bright Data SERP call (key `BRIGHT_DATA_API_KEY`, zone `BD_SERP_ZONE`, both from the process environment); `dramatic_move.serp_search(query)` wraps the same call and returns `[{title, url, snippet}]`. Never call it from a test: inject `search`.
- Write through a sink as the other gold writers do (see `data/etfs/scripts/rivalfunds/sinks.py` and how `enrichment_bloomberg.py` writes corporate actions, READ ONLY); test `write_rows` on the memory sink only.
- The stored corporate_actions columns (one live object, read at the cut): security_id, security_bloomberg, record_seq, row_kind, status, status_detail, event_type, raw_event_type, ratio, amount, raw_amount, currency, declared_date, ex_date, record_date, pay_date, frequency, date_anomalies, source, as_of, source_class, capture_origin, revision, produced_at, producer_version, input_manifest, claim. Your rows carry every one (None where unknown) plus `source_url`.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `enrichment_bloomberg.py`, the
decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~24/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W24-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/dramatic_move.py
data/etfs/scripts/rivalfunds/tests/test_ws2_wb1_dramatic_move.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cell's interface as the check grades it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-b.AC1.py`).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wb-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws2/checks/ws2-b.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~24/ETFS_RIVALS.TO-RIV-wb-1.dramatic-move-lookup.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wb-1.dramatic-move-lookup`. Report once: AC1's verdict line with the output above it; any judgment criterion left
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
<status>complete</status>
<!-- drained 2026-10-09 by 2.0.0_SA_COO~V1: merged 98c5ba6d31; amended AC1 PASS 5 of 5 (worker ~24 proof VALID) -->
<round>28</round>
<workstream>2</workstream>
<slot>~24</slot>
<fabric>dell1</fabric>
