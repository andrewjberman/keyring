# IRPT_YCDGEN task order -- `YCD-h-5` -- ROUND 5 (ENRICHMENT): THE OPAL-HELD CENSUS AND THE HELD-DATA MODULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R5.md</decomp_doc>
<owned_cells>YCD-h-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 5** cuts the Overview to a 12-request plan (Andrew's bar: the report in one sitting), feeds the held-data elements from data Opal already holds, wires the six risk statistics, keys the change flag on the request, and closes the two maps' residuals. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-5 decomposition)

### `YCD-h-5` -- the Opal-held census and module (E2 census; FWD-1, FWD-3)
- `held_data.py` (new) and `overview_coverage.json`'s feeds (5.2).
- Census against Y-5's 99 holdings. The tickers are read in memory only; the census prints counts, never a ticker or an amount.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

### 2.7 The coverage table and the probe map (cell YCD-c-2)

- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json`:
  `{"schema": "irpt-ycdgen-coverage-v1", "run": "YCD-R1-20261004T1944Z", "elements": [{"id": "p2.e05", "class":
  "HELD_DATA | OTHER_ENDPOINT | BUILDER_ONLY", "reason": "one line", "via": {...}}]}`.
  - `HELD_DATA`: computable from security-level answers weighted by the portfolio's holdings, which Opal holds (the
    frozen upload); `via` names the security-level endpoint and field, and the weighting.
  - `OTHER_ENDPOINT`: a YCharts endpoint that answers for a model portfolio; `via` names the probe call (by `name` in the
    probe map).
  - `BUILDER_ONLY`: neither; `reason` says why.

  Exactly one class per element, for exactly the 176 element ids run 3 left with no answer.
- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/coverage_probe_map.json`: the C-MAP shape (2.3) holding `calls`
  only (and `elements: []`): one candidate call per OTHER_ENDPOINT route, each GET or the one admitted read-only POST, with
  the same placeholders. It is what the issuer runs live at close.

### 3.2 The holdings (C-RUN v2; built by YCD-r-3, read by YCD-l-3)

- `runner.main --holdings-from <REQ-id>` reads the frozen input of that served request, read-only, with the HOST role's S3
  and DynamoDB clients (the research principal cannot read `opal-data-irpt`).
  - The `irpt-requests` row gives the request's composition reference, and the composition's `resolved.document.rows` gives
    each row. Follow `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` for the reads.
  - A row's ticker is its resolved symbol (`security_id`, which carries the user's correction, e.g. SGOV for TIMXX); its
    amount is `original.quantity.value`; `basis` is the document's `basis`.
- run.json gains `"holdings": {"source_request": "REQ-...", "basis": "USD", "rows": [{"ticker": "AAPL", "amount": "123.45"}]}`,
  and `schema` becomes `irpt-ycdgen-run-v2`; every v1 key is kept.
- The amounts are client figures. They live only in the firm's store, never in git or a log line.

### 5.2 The Opal-held feed (YCD-h-5 builds; YCD-w-5 wires)

- `research/held_data.py` (new) has two parts:
  - `census(holdings_tickers, sources) -> {group_id: {"status": "FED" | "NOT_HELD", ...}}` with, per FED group, `{"table", "field",
    "key", "method", "held": <count of holdings held>, "of": <count>}`, and per NOT_HELD group `{"reason"}`.
  - `value_of(group_id, field, holdings, held_rows) -> {"value", "method"}`, or `NotHeld(reason)`. Weights are the holdings'
    analysis amounts (3.2), renormalized over the held holdings, and the method names that.
- A group is a HELD_DATA row group of `overview_coverage.json` (its `via.columns` group).
- The sources are data Opal already holds for the holdings: the security tables, prices and classifications. They are read
  read-only, by schema and field name. No vendor call is made.
- Each HELD_DATA row of `overview_coverage.json` gets its `feed` rewritten as one of:
  - `{"source": "OPAL_HELD", "table", "field", "key", "method"}`;
  - `{"source": "NOT_HELD", "reason"}`.
- `YCD-w-5`:
  - Each HELD_DATA element of `overview_map.json` is re-sourced as `{"computed": "OPAL_HELD", "group": <group id>, "field": ...}`.
  - The layout computes OPAL_HELD elements through `held_data.value_of`, with the method in the 3.5 trace.
  - A NOT_HELD group's elements read NOT_AVAILABLE with reason `NOT_HELD:<reason>`.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `deliverables/maps/overview_coverage.json`: 158 HELD_DATA rows, each with `via` (the table_data `columns` group, `field`, `aggregation`, `weighting`) and, from round 4, `feed: YCHARTS_SECURITY`. The live probe of those feeds answered HTTP 400 on 6 of 6 requests (row S8), and a per-holding YCharts plan cannot fit 12 requests for 99 holdings (CTO round-4 ruling 2). Your census replaces every feed with OPAL_HELD or NOT_HELD.
- Round 4's census (row W2-S6) found, keyed by ticker: `etf-classifications` (2,866 items, an asset-class label), `bd-securities` (10,965 items, a label), `opal-data-etfs` `bbg/<date>/characteristics.parquet` (114 rows keyed 'TICKER US Equity': FUND_EXPENSE_RATIO, EQY_DVD_YLD_IND_NET, HB_OAS_EFF_DURTN, TOTAL_NUMBER_OF_HOLDINGS_IN_PORT), and `gold/book` and `gold/holding` (Opal's four ETF books). The CTO adds prices: look for Opal-held prices and any other security table with `comp-which "<question>"` and `comp-estate --definitions` (read-only; schemas, keys and field NAMES).
- Y-5's 99 holdings are the frozen input of REQ-a618aa83407689bc95193a01; `runner.read_holdings(dynamo, s3, tenant, source_request)` (contract 3.2) reads them. Read them in memory only, with the laptop's read-only credentials through the main tree's shim; print and commit counts only, never a ticker or an amount. If the read is refused, file a surprise row and census by table coverage alone.
- Put fixtures under `tests/fixtures/held/`, made-up tickers and numbers only.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json
infra/aws/lambda/investor-reporting/ycharts/research/held_data.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_held_data.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/held/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every HELD_DATA row carries a 5.2 feed: OPAL_HELD with table, field, key and method, or NOT_HELD with a reason (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/h-5.AC1.py`)
- **AC2** -- held_data computes a renormalized weighted group value with its method and reads NotHeld with a reason (tests -k held in test_held_data.py, >= 3) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/h-5.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-h-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/h-5.AC1.py</invocation><expect>h-5.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-h-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/h-5.AC2.py</invocation><expect>h-5.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-h-5.opal-held-census-and-module.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-h-5.opal-held-census-and-module`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 5 cut from the CTO's round-4 analysis @a1b47e6b3f sections 2-3 (E1-E6) and REMEDIATION_v4 (W3-S6, S7) with W4-S4; decomposition round 5 v1.0 (`IRPT_YCDGEN_DECOMP_R5.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~3`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: h-5.AC1 FAIL as expected; h-5.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~12:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @a2df1b5d80, merged a979784ea4 (channel union: base plus both appendices); h-5.AC1 PASS (158 of 158 rows 5.2-shaped: 86 OPAL_HELD, 72 NOT_HELD; 83 FED and 70 NOT_HELD groups), h-5.AC2 PASS (7) on the merged tree; research suite 128 passed. Issuer rulings: W3-S7 ACCEPTED -- Opal holds the figures for at most 37 of Y-5's 99 holdings, so a FED group's value is renormalized over the held holdings and its method says how many of how many; the worker's choices are CONFIRMED (its sector and region mappings, group id = the columns joined by '+', NotHeld returned not raised, shares in percent 0-100). The module takes rows already read; the reader that loads them at render time rides YCD-w-5.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>5</round>
<slot>~3</slot>
<fabric>laptop</fabric>
