# IRPT_YCDGEN task order -- `YCD-p-5` -- ROUND 5 (ENRICHMENT): THE BUDGETED OVERVIEW MAP AND THE SIX STATISTICS WIRED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R5.md</decomp_doc>
<owned_cells>YCD-p-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 5** cuts the Overview to a 12-request plan (Andrew's bar: the report in one sitting), feeds the held-data elements from data Opal already holds, wires the six risk statistics, keys the change flag on the request, and closes the two maps' residuals. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-5 decomposition)

### `YCD-p-5` -- the budgeted Overview map and the six statistics wired (E1 map half, E3; FWD-6, FWD-1, FWD-3)
- `overview_map.json`: 5.1's dedupe plus the benchmark call (at most 12 requests for 99 holdings); 5.3's p7 ids.
- `layout_overview.py`: 5.1's `OUTSIDE_TIME_BUDGET` reason; 5.3's benchmark and risk-free inputs in both render paths.

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

### 3.5 The computed trace (C-RUN v2; written by YCD-l-3)

When the layout finishes, each computed element's entry in run.json's `elements` carries:

```json
"computed": {"method": "...", "inputs": ["kept keys"], "coverage": 0.0-1.0, "status": "VALUE | NOT_AVAILABLE", "reason": null}
```

- `coverage` is the weight share of holdings with an answer.
- Below 0.95 the element is NOT_AVAILABLE with reason `COVERAGE_BELOW_0.95` (issuer ruling). A missing input gives
  `INPUT_MISSING:<call>`.
- The page prints the value, or the not-available line with its reason. Never an approximation (C-BUILDERONLY).

### 4.3 The six statistics (CTO round-3 analysis section 2; built by YCD-l-4)

Contract 3.4's statistic list gains these six, each computed only from held series and each with its method in the 3.5 trace:

| statistic | method |
|---|---|
| beta | covariance of the portfolio's monthly returns with the benchmark's, over the benchmark's variance |
| alpha | annualized, Jensen's form, against the same benchmark and risk-free series |
| Sharpe | annualized mean monthly excess return over its standard deviation |
| Sortino | annualized mean monthly excess return over the downside deviation |
| monthly Value at Risk | the historical 5th percentile of monthly returns |
| max_drawdown_15y | the existing max_drawdown, over 15y |

Statistic ids: `alpha_<w>`, `beta_<w>`, `sharpe_<w>`, `sortino_<w>`, `var_monthly_<w>` (w = 1y, 3y, 5y, 10y, 15y) and
`max_drawdown_15y`.
- Inputs: the portfolio series (step `portfolio_level_series`), a benchmark series kept by the run, and a risk-free series Opal
  holds.
- An input not kept or held makes the element NOT_AVAILABLE with reason `INPUT_MISSING:<series>`. No vendor call is added to
  fetch one.

### 5.1 The 12-request plan (YCD-r-5 runner half; YCD-p-5 map half)

- `MAX_RUN_REQUESTS = 12` (2 windows of 6; CTO round-4 ruling 1).
- Before the first call (and before the lease), `runner.main` prints one line: `PLAN requests=<n> windows=<w>
  per_window=<N> window_seconds=<W>`. With no budget, `windows=1` and `per_window=6`.
- A plan over 12 requests REFUSES before the lease, with `PLAN_OVER_BUDGET:<n> requests (max 12)`. It refuses with or without
  `--requests-per-window`.
- The Overview map (`deliverables/maps/overview_map.json`) keeps only the calls an element reads. With Y-5's 99 holdings it
  plans to at most 12 requests, counting `YCD-p-5`'s benchmark call.
- An element whose call is not in the map reads NOT_AVAILABLE, with reason `OUTSIDE_TIME_BUDGET`. Its line reads "Not
  available: outside the run's time budget."
- No answer kept from an earlier run stands in for a call in this run.

### 5.3 The six statistics wired (YCD-p-5)

- The p7 elements carry a `statistic` and 4.3's ids: e02 alpha, e03 beta, e05 sharpe, e06 sortino and e07 max_drawdown. On e08,
  `value_at_risk_monthly_5_<w>` becomes `var_monthly_<w>`.
- **Benchmark:** a benchmark level series is kept by the run. It is one `fund_data` call inside 5.1's 12 requests, for the
  benchmark the source PDF's p7 names; if the PDF names none, the one `portfolio_info`'s answer names.
- **Risk-free:** a risk-free series Opal holds, named by table and field and converted to a level series where it is a yield.
- Both render paths pass the two series into `compute_all`. Where either is missing, the element reads
  `INPUT_MISSING:benchmark` or `INPUT_MISSING:risk_free`.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `deliverables/maps/overview_map.json` at the base: 36 calls (14 portfolio calls, 22 `holdings_*` expand calls at chunk 20 or 10) and 253 elements (188 sourced to a call, 65 BUILDER_ONLY). It plans 129 requests for 99 holdings. Elements read 7 portfolio calls: portfolio_info, portfolio_level_series, portfolio_snapshot_metrics, portfolio_equity_exposure, portfolio_region_exposure, portfolio_fundamentals, portfolio_scatter_documented_ids. Seven are read by no element: portfolio_scatter, portfolio_returns, portfolio_key_stats, portfolio_allocation, portfolio_bond_exposure, portfolio_risk_stats, portfolio_standardized_returns. The 22 expand calls feed the 158 HELD_DATA elements: they leave the map, and those elements read OUTSIDE_TIME_BUDGET until a later cell (YCD-w-5) re-sources them to data Opal holds. Do not touch their element ids.
- p7 at the base: e02 alpha, e03 beta, e05 Historical Sharpe, e06 Historical Sortino, e07 Max Drawdown, e08 Monthly VaR 5 percent; each `computed: OWN_SERIES` on portfolio_level_series with `statistic: null`; e08's columns are `value_at_risk_monthly_5_<w>`, which do not parse as 4.3's `var_monthly_<w>` (CVO round-4 grade).
- `layout_overview.py` at the base: `compute_element(element, kept_by_name, run_doc, benchmark=None, risk_free=None)`, `compute_all(run_doc, kept_by_name, map_doc, benchmark=None, risk_free=None)`, `statistic_of(points, statistic, benchmark=None, risk_free=None)`; `_risk_stat` raises INPUT_MISSING:benchmark / INPUT_MISSING:risk_free; the two render paths call `compute_all(run_doc, kept, map_doc)` with neither series (around lines 703 and 811). Keep every existing test passing (test_layout_overview.py: 21 at the base). Put new fixtures under `tests/fixtures/overview/`.
- The benchmark: the model portfolio's own `portfolio_info` answer kept at run G names it. Read ONLY its benchmark field (read-only, OS temp, deleted after) from `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R4-20261005T0700Z-G/step=01_portfolio_info.json`; the map then holds one `fund_data` level-series call for that benchmark id, inside the 12 requests.
- The risk-free series: find what Opal already holds (read-only: `comp-which "risk-free rate treasury yield series"`, `comp-estate --definitions`; table and field NAMES only). If Opal holds none, the four elements read INPUT_MISSING:risk_free and you file a surprise row saying so; you never call a vendor for one.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/overview/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the Overview map plans 1..12 requests for 99 holdings through runner.plan_calls, and every call in it is read by an element (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC1.py`)
- **AC2** -- an element whose call is not in the map reads OUTSIDE_TIME_BUDGET, and the statistics compute from a run fixture carrying a benchmark and a risk-free series (tests -k 'budget_reason or wired' in test_layout_overview.py, >= 3) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC2.py`)
- **AC3** -- the six p7 elements carry a statistic and 4.3's ids (alpha_, beta_, sharpe_, sortino_, max_drawdown_, var_monthly_) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-p-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC1.py</invocation><expect>p-5.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-p-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC2.py</invocation><expect>p-5.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-p-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/p-5.AC3.py</invocation><expect>p-5.AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-p-5.budgeted-overview-map-and-statistics-wired.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-p-5.budgeted-overview-map-and-statistics-wired`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 5 cut from the CTO's round-4 analysis @a1b47e6b3f sections 2-3 (E1-E6) and REMEDIATION_v4 (W3-S6, S7) with W4-S4; decomposition round 5 v1.0 (`IRPT_YCDGEN_DECOMP_R5.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~2`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: p-5.AC1 FAIL as expected; p-5.AC2 FAIL as expected; p-5.AC3 FAIL as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>5</round>
<slot>~2</slot>
<fabric>laptop</fabric>
