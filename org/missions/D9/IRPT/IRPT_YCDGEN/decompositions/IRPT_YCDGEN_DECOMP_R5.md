# IRPT_YCDGEN -- DECOMPOSITION, ROUND 5 (ENRICHMENT): the 12-request plan, the Opal-held feed, the statistics wired, the request hash, the map residuals

```json
{
 "project": "IRPT_YCDGEN",
 "round": 5,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.1 @8b364d6d94; RATIFIED)",
 "prd_version": "v0.1",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_YCDGEN_ROUND4_20261005.md @a1b47e6b3f sections 2-3",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "round_scope": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-6"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 5,
 "chains": 4,
 "join_cells": 1,
 "frozen": true,
 "revision": "1.0",
 "cell_ids": ["YCD-r-5", "YCD-p-5", "YCD-h-5", "YCD-m-5", "YCD-w-5"]
}
```

**Issuer:** `2.0.0_SA_COO~Y`, 2026-10-05 ~09:5xZ, FULL lease. **Source:** the CTO's round-4 analysis, section 2 (rulings 1-4) and
section 3 (E1-E6), and REMEDIATION_v4 (W3-S6, S7) with REMEDIATION_v3's W4-S4. Rounds 1-4 contracts hold unless extended below.

## Issuer rulings at this cut

1. **E1 splits by file.** The runner's half (count, print, refuse over 12) is `YCD-r-5`. The Overview map's half (calls cut to those
   an element reads, the budget reason) rides with E3 in `YCD-p-5`, because both write `overview_map.json` and `layout_overview.py`.
2. **E2 splits into a census and a wiring.** `YCD-h-5` finds and computes the Opal-held figures in its own new module. `YCD-w-5`
   wires them into the map and the layout after `YCD-p-5` and `YCD-h-5` merge (the round's one join).
3. **E4's build half (the request hash, the lookup) is `YCD-r-5`.** Its live half is the issuer's close act: one indexed run of
   the level-series request on the merged runner during the day, and the byte-identical request after today's close reaches
   YCharts (no call in the maps moves intraday: every portfolio answer is daily).
4. **E5 is `YCD-m-5`. E6 is the issuer's close act** once `YCD-w-5` merges: one budgeted live Overview, rendered, timed, and a
   fresh link to Andrew.
5. **Chains:** `~1` r-5; `~2` p-5 then w-5; `~3` h-5 (w-5 also waits on it); `~4` m-5. No two cells running together write one
   file. All are WORLD (the floor for `infra/` paths). No worker calls YCharts, writes the store, deploys or grants.

## 2. Contracts (round 5)

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

### 5.3 The six statistics wired (YCD-p-5)

- The p7 elements carry a `statistic` and 4.3's ids: e02 alpha, e03 beta, e05 sharpe, e06 sortino and e07 max_drawdown. On e08,
  `value_at_risk_monthly_5_<w>` becomes `var_monthly_<w>`.
- **Benchmark:** a benchmark level series is kept by the run. It is one `fund_data` call inside 5.1's 12 requests, for the
  benchmark the source PDF's p7 names; if the PDF names none, the one `portfolio_info`'s answer names.
- **Risk-free:** a risk-free series Opal holds, named by table and field and converted to a level series where it is a yield.
- Both render paths pass the two series into `compute_all`. Where either is missing, the element reads
  `INPUT_MISSING:benchmark` or `INPUT_MISSING:risk_free`.

### 5.4 The request hash and the lookup (YCD-r-5)

- Each kept call records `request_sha256`: the sha256 of the canonical JSON of `{method, path, params}` after templating.
- `changed_since_previous` compares against the previous run's kept call with the same name AND the same `request_sha256`:
  - same request: `true` or `false` as before;
  - no previous call with that name: `no_previous`;
  - a previous call with the name but a different request: `request_changed` (never `true`).
- A previous run record without `request_sha256` reads `no_previous`.
- `research/lookup.py` (new): `python lookup.py --firm <f> --request <REQ> --call <name>` prints the call's kept record for an
  analyst. That is its status, shape, sha256, request_sha256, changed_since_previous and kept_at, plus a one-line summary of
  the answer's kind (identifiers, data or document) and size. It reads through the keeper's store and prints no figure value
  from a client file.

### 5.5 The map residuals (YCD-m-5; W4-S4 R1 and R2)

- **R1:** Multi p9's third-security Bond Credit Quality row ("No data available") is listed as an element. It reads not available,
  with its source on the comparison call at key_index 2.
- **R2:** each of the seven placeholder labels "row" (Comparison p5.e17 and p9.e04; Multi p5.e12-e14, p9.e03 and p9.e04) takes
  the name the PDF prints on the line above. That name comes from `map_pdf`'s rule, not from map-side repair.
- Ids are never renumbered.

## 3. THE CELLS

### `YCD-r-5` -- the runner's 12-request plan, the request hash, and the lookup (E1 runner half, E4 build; FWD-6, FWD-2)
- `runner.py`: 5.1's print and refusal; 5.4's `request_sha256` and the flag rule (with `keeper.py` if the flag is computed there).
- `lookup.py` (new): 5.4's one-command lookup.
- Tests:
  - the PLAN line;
  - a 13-request plan refuses before the lease;
  - a changed parameter under one call name reads `request_changed`, not `true`;
  - an unchanged request with a changed answer reads `true`;
  - the lookup prints a kept record from a fake store.

### `YCD-p-5` -- the budgeted Overview map and the six statistics wired (E1 map half, E3; FWD-6, FWD-1, FWD-3)
- `overview_map.json`: 5.1's dedupe plus the benchmark call (at most 12 requests for 99 holdings); 5.3's p7 ids.
- `layout_overview.py`: 5.1's `OUTSIDE_TIME_BUDGET` reason; 5.3's benchmark and risk-free inputs in both render paths.

### `YCD-h-5` -- the Opal-held census and module (E2 census; FWD-1, FWD-3)
- `held_data.py` (new) and `overview_coverage.json`'s feeds (5.2).
- Census against Y-5's 99 holdings. The tickers are read in memory only; the census prints counts, never a ticker or an amount.

### `YCD-m-5` -- the map residuals (E5; FWD-3, FWD-4)
- 5.5 on `map_pdf.py` and the two maps, re-run on the two retained PDFs (OS temp only, as m-4 did).

### `YCD-w-5` -- the Opal-held elements wired (E2 wiring; FWD-1, FWD-3). JOIN: after YCD-p-5 and YCD-h-5 merge
- `overview_map.json` HELD_DATA sources and `layout_overview.py`'s OPAL_HELD path (5.2).

## 4. The issuer's close acts

- **E4 live:**
  - On the merged runner, run one indexed level-series run (zoom=max), then the byte-identical request after today's close
    reaches YCharts.
  - The second reads `true`, with the kept series' last date advanced.
  - Then the lookup (5.4) of that call.
- **E6 live:**
  - One budgeted Overview run (at most 12 requests, 2 windows), rendered.
  - Its timing is split into YCharts time and Opal waiting.
  - A fresh link goes to Andrew.

## 5. Not in round 5

The Comparison and Multi layouts; FWD-5; FWD-7.
