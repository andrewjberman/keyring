# IRPT_YCDGEN round 11 -- decomposition: Andrew's own journey read hop by hop, and a job that states why it died

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_11_20261011.md` @457305b604, section 4
(eight items, in order). It answers `3.0.0_SA_CVO`'s REMEDIATION_v9 @1f3e35873b (26 rows, 22 of them backlog graduated as
filed). No PRD addendum. The sitting is not asked.

## Read by the issuer before cutting (three backlog rows are already MET at HEAD)

The analysis sends the backlog to a read because nobody had re-read it. Three of its build or hygiene items were read here,
before any order was written, and are NOT cut as work:

- **Item 2, row W1-S8 (the Opal page prints vendor wording and a vendor footer): MET.** Fixed 2026-10-05 @fc018ca6c7
  (YCD-h-6). `layout_overview.py` prints `OPAL_SOURCE_CREDIT` ("Data: Opal Capital") and `OPAL_NOT_IN_VERSION_LINE` when
  `pricing=False`, which is what `opal_producer` passes. `test_opal_page_no_vendor_wording` (tests/test_layout_overview.py)
  asserts the built page and the rendered PDF text hold no "ycharts": run alone at HEAD, 1 passed. The fix is in the st27
  package too, so it was on the host before st30. The three "YCharts" strings left in the file are the `pricing=True`
  research branch.
- **Item 8, rows W3-S12 and W3-S18 (a resident test fails when run alone): MET.**
  `python -m pytest -q infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py` at HEAD: 19 passed.

`YCD-a-11` still records all three with their evidence, so the slug's 26 rows are read in one place.

## Cells (round 11)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-11` | worker, read-only | 1 | One record of Andrew's journey at HEAD, by code and fixtures and with no generation: each hop from the page to the opened Overview with its code lines, and each of the slug's 26 rows as OPEN or MET, on his path or not, with evidence |
| `YCD-b-11` | ~G2 (direct read, done above) | 2 | Row W1-S8 MET with its evidence; no build |
| `YCD-c-11` | ~G2 (one send) | 3 | Rows W2-S13 and W6-S4 with `2.0.0_SA_COO~P2` and `2.0.0_SA_COO~D2`, in the fixed order: the portal's reader admits the Opal form on PROD first, then the contract and the service |
| `YCD-d-11` | by amendment, after `YCD-a-11` | 4 | Whatever the journey read finds broken on Andrew's own path, in hop order |
| `YCD-e-11` | worker | 5 (row D2-S49) | A generation job whose message is about to be dead-lettered records FAILED with a closed cause, so its record no longer reads RECEIVED with no reason. Built and tested in the tree; NOT deployed here |
| `YCD-f-11` | ~G2 (direct, under its own pair) | 6 | The one-equity data request with its never-widen pair: the store's owner, the one row added, its rollback. Sent only on both halves |
| `YCD-g-11` | ~G2 (direct, a design record) | 7 | Fund allocations as weights per sector and per country: a design record with its four-postulate record (CLAUDE.md rule 24) and the statement that the source's allocation fields are current-day only. No build |
| `YCD-h-11` | ~G2 (direct) | 8 | The package gate applies the recorded map source in whole-tree mode and writes the same tar bytes twice (row D2-S46); the install script carries no dead placeholder (row D2-S47). Row W3-S21 is the portal's and goes to `2.0.0_SA_COO~D2` with `YCD-c-11` |

## Dependencies

- `YCD-d-11` follows `YCD-a-11`. The eight existing dead letters are reconciled BY RECORD only after `YCD-e-11` is on the
  host, under a pair naming each of the 8; that write is not a cell of this issuance.
- `YCD-a-11` and `YCD-e-11` have no unmet dependency and start now. So do the issuer's direct acts.

## Not cells

- **The sitting**, and **Andrew's word on a measuring identity**: his acts (analysis section 5).
- **A redrive of any dead letter.** None, in whole or part, without a pair naming each of the 8.
- **A standing status-only read path.** Not built (analysis section 4).
- **The two research roles for 49financial and inflection** (row D2-S19): stay as they are, fail-closed.

## The record's value set (a schema this issuer authors; four postulates)

`YCD-a-11` states each row on two fields, because the analysis asks two questions of it.
(i) MECE over the declared domain, which is the 26 row ids REMEDIATION_v9 names (the check prints that denominator and finds
a missing id by subtraction): `state` is OPEN or MET, and every row is one or the other at HEAD; `on_path` is YES, NO or
NOT_DETERMINED. (ii) Same grain: one row id, one line. (iii) One intent per field: `state` answers "is what the row says
still true at HEAD", `on_path` answers "does Andrew's own submission pass through it". (iv) State coherence: a code fix moves
`state` and never `on_path`; only a change to the journey moves `on_path`. A row the code cannot settle is OPEN with
`needs_live_read` true, never MET.

## Four-postulate record of the round

(i) Domain: the analysis's eight items, one cell each. (ii) Two tree orders (one read, one build) and six issuer acts.
(iii) One intent: nothing known to be broken stands on Andrew's path when he sits. (iv) What this round does NOT move: the
resident host, the allow list, the store's contents, and any served contract. `YCD-e-11` changes the tree only.

fanout: 2 of 8 chains in this issuance as tree orders (a, e), cap 8; b, c, f, g, h are this seat's direct acts; d is cut by
amendment.
