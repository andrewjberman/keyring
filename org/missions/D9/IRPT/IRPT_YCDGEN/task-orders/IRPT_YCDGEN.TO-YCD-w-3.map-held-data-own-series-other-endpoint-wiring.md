# IRPT_YCDGEN task order -- `YCD-w-3` -- ROUND 3 (ENRICHMENT): THE MAP'S HELD-DATA, OWN-SERIES AND OTHER-ENDPOINT WIRING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md</decomp_doc>
<owned_cells>YCD-w-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 3** builds the Overview's held-data (167) and other-endpoint (7) elements on round 2's coverage table, fixes the keeper's series rule, and maps the Comparison and Multi reports. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-w-3` -- the map's held-data, own-series and other-endpoint wiring (E1 map side, E2, W3-S2; FWD-1, FWD-3)
- `overview_map.json`:
  - adds the expand calls the coverage table's HELD_DATA `via` names (one `/indices/table_data` call per column group over
    `indices`, one `/charts/fund_data.json` level-series call over `securities`), each with `expand` per 3.1;
  - adds the two probed calls from `coverage_probe_map.json`;
  - re-points each HELD_DATA element's `source` to a 3.4 computed source;
  - moves the elements computable from the portfolio's own kept series to `OWN_SERIES`;
  - points each OTHER_ENDPOINT element at its probe call and field.

  `claim` stays `inferred`. Ids never renumber. The 2 BUILDER_ONLY stay.
- `overview_coverage.json`: the `OWN_SERIES` class (3.4), with the moved elements reclassified. Each class still holds
  exactly one entry per element id.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

### 2.3 The element map (C-MAP) -- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`

```json
{
 "schema": "irpt-ycdgen-map-v1", "report_type": "OVERVIEW", "template_id": "14141822",
 "source_pdf": {"bucket": "opal-data-irpt", "artifact_prefix": "ART-<first 12 hex>", "pages": 4},
 "calls": [{"name": "snake_case", "method": "GET", "path": "/charts/general_data.json",
            "params": {"securities": "id:{security_id},include:true,,", "metrics": "id:total_return,include:true,,"}}],
 "elements": [{"id": "p1.e01", "page": 1, "kind": "number | table | chart | text", "label": "printed label text",
               "source": {"call": "snake_case", "field": "JSONPath into the kept body_json"},
               "claim": "inferred | measured", "note": "one line"},
              {"id": "p3.e04", "page": 3, "kind": "chart", "label": "...", "source": "BUILDER_ONLY",
               "claim": "inferred", "note": "computed only inside YCharts' report builder"}]
}
```

- Labels are printed label text only. **No figure value from the PDF enters git** (C-FIRM): no number read from a figure's
  position, no dollar amount, no percentage value.
- `params` placeholders: `{security_id}` (the portfolio's typed id), `{start}`, `{end}`.

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

### 3.1 The expand call (C-MAP v2; built by YCD-r-3, used by YCD-w-3)

A map call may carry:

```json
"expand": {"over": "holdings", "param": "indices", "chunk": 20, "item": "{ticker}", "join": ","}
```

- `param` names the one param the runner fills with the chunk. `item` is `{ticker}` or `id:{ticker},include:true,,`.
  `chunk` is 1-50.
- The runner issues one request per chunk of the holdings' tickers, in the holdings' order. Each answer is kept under the
  name `<call name>__c<kk>` (kk = 01, 02, ...), with one step per chunk, continuing the run's step numbers.
- Every other param is filled as today: `{security_id}`, `{start}`, `{end}`.
- `runner.plan_calls(map_doc, security_id, window, holdings=None)` plans the expanded requests. An `expand` call with no
  holdings given REFUSES before any lease (`EXPAND_REQUIRES_HOLDINGS:<name>`).

### 3.4 Computed element sources (C-MAP v2; written by YCD-w-3, computed by YCD-l-3)

A map element's `source` may be:

```json
{"computed": "<METHOD>", "call": "<call name>", "columns": ["calc ids"], "field": "<JSONPath per security>",
 "sleeve": "stock | bond | null", "statistic": "<series statistic id or null>"}
```

METHOD is one of:
- `WEIGHTED_MEAN`: `sum_i w_i * v_i` over holdings with an answer.
- `WEIGHTED_MEAN_SLEEVE`: the same, with `w_i` scaled by holding i's sleeve share (its `asset_allocation_stock` or
  `asset_allocation_bond` answer) and renormalized to 1.
- `HARMONIC_WEIGHTED_MEAN`: `1 / sum_i (w_i / v_i)`.
- `SUM`: `sum_i v_i`.
- `BUY_AND_HOLD`: the portfolio value path `V(t) = sum_i amount_i * series_i(t) / series_i(t0)`, then `statistic`.
- `OWN_SERIES`: `statistic` over the portfolio's own kept level series (step `portfolio_level_series`).

Weights: `w_i = amount_i / sum(amount)` for basis `USD`; `w_i = amount_i` for a weight basis.

Statistic ids (series methods): `total_return_<1m|3m|ytd|1y|3y|5y|10y|15y>`, `annualized_return_<3y|5y|10y|15y>`,
`std_dev_<1y|3y|5y|10y|15y>` (annualized from monthly returns), `max_drawdown_<1y|3y|5y|10y|all>`, `cumulative_series`.

The coverage table gains class `OWN_SERIES` (row W3-S2): an element computable from the portfolio's own kept level
series. Its `via` names the statistic.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `deliverables/maps/overview_coverage.json` (round 2): 176 elements; 167 HELD_DATA, 7 OTHER_ENDPOINT, 2 BUILDER_ONLY. Each HELD_DATA `via` names `endpoint`, `columns` (table_data calc ids) or `params_names`, `field`, `aggregation` and `weighting`: 96 stock-sleeve weighted means, 38 bond-sleeve, 15 plain weighted means, 10 buy-and-hold from fund_data series, 3 sums, 3 harmonic means, 2 weighted means of market cap. Row W3-S2 (in the channel) names the elements computable from the portfolio's own kept level series: move those to `OWN_SERIES`.
- `deliverables/maps/coverage_probe_map.json`: the two probed calls (`portfolio_scatter_documented_ids`, a POST; `portfolio_snapshot_metrics`, a GET of `/charts/general_data.json` with `xAxis=metrics`). Both answered 200 for a model portfolio on 2026-10-04. Add them to the Overview map's `calls` and point the 7 OTHER_ENDPOINT elements at them (field = the JSONPath into each answer; claim `inferred`).
- One table_data call per column group is the shape: the group's calc ids in `columns`, the holdings in `indices` via `expand` (chunk 20, item `{ticker}`). Keep a call's query short: round 1's step 7 (a long column list) drew the firewall every time, so split any group above 8 columns. One fund_data level-series call over `securities` (`expand` chunk 10, item `id:{ticker},include:true,,`, calcs `id:level,include:true,,`, zoom max).
- The 77 elements outside the coverage table and the 2 BUILDER_ONLY keep their sources (check w-3.AC2).

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every HELD_DATA element has a 3.4 computed source on an expand call, every OWN_SERIES one an OWN_SERIES source, every OTHER_ENDPOINT one a probe call; the coverage table holds the OWN_SERIES class with one row per id (176) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/w-3.AC1.py`)
- **AC2** -- control: the elements outside the coverage table keep their sources, and the 2 BUILDER_ONLY gain no computation (PASS at the base and after) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/w-3.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-w-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/w-3.AC1.py</invocation><expect>w-3.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-w-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/w-3.AC2.py</invocation><expect>w-3.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-w-3.map-held-data-own-series-other-endpoint-wiring.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-w-3.map-held-data-own-series-other-endpoint-wiring`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 3 cut from the CTO's round-2 analysis section 2 (E1-E6); decomposition round 3 v1.0 (`IRPT_YCDGEN_DECOMP_R3.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~2`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: w-3.AC1 FAIL as expected; w-3.AC2 PASS (control) as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~01:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 @039cec613f, merged 37e2a053c6 (channel append resolved as base + both appendices); w-3.AC1 PASS (22 expand calls, 158 HELD_DATA, 9 OWN_SERIES, 7 OTHER_ENDPOINT, 0 unwired), w-3.AC2 PASS (control). Issuer rulings: 9 not 10 elements to OWN_SERIES (p12.e04 stays BUY_AND_HOLD, no market price of its own) -- accepted; W2-S4 (alpha/beta/Sharpe/Sortino/VaR and max_drawdown_15y outside 3.4's statistic list) -- those elements read not available this round, carried to the round-3 analysis; W2-S5 (a 16-column element spans two chunks; inferred field paths) -- accepted, measured by the close run.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>3</round>
<slot>~2</slot>
<fabric>laptop</fabric>
