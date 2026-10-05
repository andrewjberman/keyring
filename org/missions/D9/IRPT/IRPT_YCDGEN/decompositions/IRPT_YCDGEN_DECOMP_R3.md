# IRPT_YCDGEN -- DECOMPOSITION, ROUND 3 (ENRICHMENT): the Overview's held-data and other-endpoint elements, the keeper's series rule, the Comparison and Multi maps

```json
{
 "project": "IRPT_YCDGEN",
 "round": 3,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.1 @8b364d6d94; RATIFIED)",
 "prd_version": "v0.1",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_YCDGEN_ROUND2_20261005.md section 2",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "round_scope": ["FWD-1", "FWD-2", "FWD-3", "FWD-4"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 4,
 "chains": 4,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "cell_ids": ["YCD-r-3", "YCD-w-3", "YCD-l-3", "YCD-m-3"]
}
```

**Issuer:** `2.0.0_SA_COO~Y`, 2026-10-05 ~00:4xZ, FULL lease. **Source:** the CTO's round-2 analysis, section 2 (E1-E6), read as
this round's rectangle. Rounds 1-2 contracts (`IRPT_YCDGEN_DECOMP.md` 2.1-2.4, `IRPT_YCDGEN_DECOMP_R2.md` 2.5-2.7) hold
unless a contract below extends them.

## Issuer rulings at this cut

1. **E1 splits by write set.** Three cells share the contracts below: the runner gathers the holdings and the per-holding
   answers (`YCD-r-3`); the map names the calls and each element's computation (`YCD-w-3`); the layout computes
   (`YCD-l-3`).
2. **E3, the keeper's series rule, is a repair batched into `YCD-r-3`**, the cell that owns `keeper.py`'s neighbour.
3. **E2, the seven OTHER_ENDPOINT elements, is wiring in the map:** `YCD-w-3`.
4. **E4, rows S3, W3-S2 and W3-S3:**
   - W3-S3 (per-holding calls the placeholders cannot reach) is answered by contract 3.1, in `YCD-r-3`.
   - W3-S2 (the coverage enum lacks "the portfolio's own kept series") is answered by contract 3.4's class `OWN_SERIES`, in
     `YCD-w-3`.
   - S3 (stop rows) was answered in round 2 by `YCD-r-2`. The issuer files the disposition at close.
5. **E5 is the issuer's close run on a new trading day; E6 is `YCD-m-3`.**
6. **Chains:** `~1` r-3, `~2` w-3, `~3` l-3, `~4` m-3. No two cells write one file. Each builds against the contracts, not
   against another cell's code. The issuer joins them at the drain and in the close run.
7. **Risk:** WORLD on all four (the gate's floor for `infra/` paths). No cell calls YCharts, writes the store, deploys or
   grants.

## 2. Contracts (round 3)

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

### 3.3 The keeper's series rule (C-KEEP; built by YCD-r-3)

`shape` is `DATA` when a JSON answer holds a `series` key whose value is a list of objects, any of which carries a list
of numbers or of `[number, number]` pairs (YCharts' scatter answer, `data.series`). It is added to the existing DATA keys,
and no other label changes.

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

## 3. THE CELLS

### `YCD-r-3` -- the runner's holdings and expand calls, and the keeper's series rule (E1 data side, E3, W3-S3; FWD-1, FWD-2, FWD-3)
- `ycharts/research/runner.py`: contracts 3.1 and 3.2. `plan_calls(..., holdings=None)` expands; `main --holdings-from`
  reads the frozen input with the host role's clients (`_compose` returns them beside the research S3 client); `run()`
  takes `holdings` and writes the `holdings` block and schema v2.
- `ycharts/research/keeper.py`: contract 3.3.
- Tests: expand planning (chunking, item format, order, kept names `__cNN`, refusal without holdings); the holdings read
  over fake clients shaped like the served rows (a corrected row reads its corrected ticker); run.json v2 keeps every v1
  key; the scatter-shaped answer labels DATA.

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

### `YCD-l-3` -- the layout computes the held-data and own-series elements, with the trace (E1 build side; FWD-1, FWD-3)
- `ycharts/research/layout_overview.py`: the 3.4 methods and statistics over kept answers, including the chunked
  `__cNN` names and run.json's `holdings`; the 3.5 trace written into the finished run.json; the page prints each value or
  the not-available line with its reason.
- Tests on fixtures: each METHOD on a small hand-checked case; sleeve renormalization; coverage below 0.95 gives
  NOT_AVAILABLE with its reason; the trace lists the kept keys used.

### `YCD-m-3` -- the Comparison and Multi maps (E6; FWD-3, FWD-4)
- By the method of m-1/m-2 (`map_pdf.py`, as is; read-only) over Cottonwood's retained certified PDFs:
  - **Multi:** Y-3's REQ-329a56182b2668d44a28c8d7.
  - **Comparison:** REQ-e4b7f5ab... or REQ-7ea49c2d....

  Locate each through its request's job checkpoint, as `live_walk/case_trace.py` does, read into OS temp only.
- Write `deliverables/maps/comparison_map.json` and `deliverables/maps/multi_map.json` (C-MAP shape, `report_type`
  `COMPARISON` / `MULTI`). Each element is sourced to an Overview call or computed method where the same figure exists
  there, else to a candidate endpoint (`claim` `inferred`), else `BUILDER_ONLY`. These are maps only; no layout this round.

## 4. Not in round 3

The Comparison and Multi layouts (round 4, from these maps' coverage); FWD-5 (the firm-private read); FWD-7 (the
side-by-side check). No portal page, no schedule, no second firm.
