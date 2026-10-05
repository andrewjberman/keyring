# IRPT_YCDGEN task order -- `YCD-l-4` -- ROUND 4 (ENRICHMENT): THE SIX STATISTICS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md</decomp_doc>
<owned_cells>YCD-l-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 4** gives the runner a per-window call budget (the firewall challenges the 7th request of any run), finds which held-data figures Opal already holds, adds six risk statistics, and fixes the two maps' missing rows. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-l-4` -- the six statistics (E4; FWD-3)
- `ycharts/research/layout_overview.py`: 4.3's statistics in the computed path, with the trace.
- Tests named `test_six_statistic_*`: each of the six computed on a hand-checked fixture and NOT_AVAILABLE when its benchmark
  or risk-free input is absent.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

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

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `layout_overview.py` at the base computes 3.4's methods and statistics (round 3, l-3): series statistics `total_return_*`, `annualized_return_*`, `std_dev_*`, `max_drawdown_*`, `cumulative_series`, with the 3.5 trace and not-available reasons; returns, risk and drawdown are in percent (row W3-S4's conventions, confirmed). Keep every existing test passing (test_layout_overview.py: 14 at the base).
- The six elements are on map page 7 (p7.e02, e03, e05, e06, e08 and p7.e07); their `source.columns` hold the statistic ids and `statistic` is null today (row W2-S4). Your cell computes 4.3's ids; the map wiring that names the benchmark and risk-free inputs per element is a later cell, so take them as optional named inputs to the statistic functions and read NOT_AVAILABLE when absent.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- each of the six statistics computes a hand-checked value and reads NOT_AVAILABLE with its missing input named (tests -k six_statistic, >= 6) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/l-4.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-l-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/l-4.AC1.py</invocation><expect>l-4.AC1 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-l-4.layout-six-statistics.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-l-4.layout-six-statistics`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 4 cut from the CTO's round-3 analysis @033795b666 sections 2-3 (E1-E6); decomposition round 4 v1.0 (`IRPT_YCDGEN_DECOMP_R4.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~3`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: l-4.AC1 FAIL as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>4</round>
<slot>~3</slot>
<fabric>laptop</fabric>
