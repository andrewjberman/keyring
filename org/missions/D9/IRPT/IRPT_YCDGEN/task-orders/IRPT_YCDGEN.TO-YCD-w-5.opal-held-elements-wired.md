# IRPT_YCDGEN task order -- `YCD-w-5` -- ROUND 5 (ENRICHMENT): THE OPAL-HELD ELEMENTS WIRED (JOIN: AFTER YCD-p-5 AND YCD-h-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R5.md</decomp_doc>
<owned_cells>YCD-w-5</owned_cells>
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

### `YCD-w-5` -- the Opal-held elements wired (E2 wiring; FWD-1, FWD-3). JOIN: after YCD-p-5 and YCD-h-5 merge
- `overview_map.json` HELD_DATA sources and `layout_overview.py`'s OPAL_HELD path (5.2).

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

- You start from CLOUD after YCD-p-5 and YCD-h-5 merged. Then: the Overview map holds at most 12 requests and no `holdings_*` call; its 158 HELD_DATA elements read OUTSIDE_TIME_BUDGET (5.1). `held_data.py` exists with `census` and `value_of` (5.2), and every HELD_DATA row of `overview_coverage.json` carries an OPAL_HELD or NOT_HELD feed. Read both merged files before you change anything.
- Re-source each HELD_DATA element (by the coverage row's id) to `{"computed": "OPAL_HELD", "group": <group id>, "field": ...}`. The layout computes it through `held_data.value_of`, with the method in the 3.5 trace; a NOT_HELD group's elements read NOT_AVAILABLE with `NOT_HELD:<reason>`. The map's request count must stay 1..12 (check p-5.AC1 still passes). Keep every existing layout test passing. Put fixtures under `tests/fixtures/overview/`.

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

- **AC1** -- every HELD_DATA element is sourced OPAL_HELD with a group (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/w-5.AC1.py`)
- **AC2** -- an OPAL_HELD element computes through held_data with its method in the trace, and a NOT_HELD group's element reads NOT_HELD:<reason> (tests -k opal_held in test_layout_overview.py, >= 2) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/w-5.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-w-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/w-5.AC1.py</invocation><expect>w-5.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-w-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/w-5.AC2.py</invocation><expect>w-5.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-w-5.opal-held-elements-wired.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-w-5.opal-held-elements-wired`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 5 cut from the CTO's round-4 analysis @a1b47e6b3f sections 2-3 (E1-E6) and REMEDIATION_v4 (W3-S6, S7) with W4-S4; decomposition round 5 v1.0 (`IRPT_YCDGEN_DECOMP_R5.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~2`. JOIN: start only after YCD-p-5 and YCD-h-5 are merged; the slot-~2 worker continues into it. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: w-5.AC1 FAIL as expected; w-5.AC2 FAIL as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>5</round>
<slot>~2</slot>
<fabric>laptop</fabric>
