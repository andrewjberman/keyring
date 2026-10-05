# IRPT_YCDGEN -- DECOMPOSITION, ROUND 4 (ENRICHMENT): the call budget, the held-data feed census, the six statistics, the two maps' rows

```json
{
 "project": "IRPT_YCDGEN",
 "round": 4,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.1 @8b364d6d94; RATIFIED)",
 "prd_version": "v0.1",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_YCDGEN_ROUND3_20261005.md @033795b666 sections 2-3",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "round_scope": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-6"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 4,
 "chains": 4,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "cell_ids": ["YCD-r-4", "YCD-o-4", "YCD-l-4", "YCD-m-4"]
}
```

**Issuer:** `2.0.0_SA_COO~Y`, 2026-10-05 ~05:2xZ, FULL lease. **Source:** the CTO's round-3 analysis, section 3 (E1-E6) and
section 2 (the W2-S4 ruling). Rounds 1-3 contracts hold unless extended below.

## Issuer rulings at this cut

1. **E1 splits into a build half and a live half.**
   - Build: the runner plans every run within a per-window budget (`YCD-r-4`), and an offline census finds which HELD_DATA
     groups Opal already holds (`YCD-o-4`).
   - Live, the issuer's at close: measure the window length, then probe the YCharts security routes the census leaves, at most
     6 requests per window and never a 7th. The live half waits only for the session: 2.0.0_SA_COO~D's Y-6 page runs hold it
     one job at a time, and research never interleaves with them.
2. **E3 (the keeper's point-object rule) is a repair batched into `YCD-r-4`.**
3. **E4 is `YCD-l-4`; E2 is `YCD-m-4`.**
4. **E5 and E6 are the issuer's close acts.** E5 is two runs with different `--end` dates, inside one window's budget. E6 renders
   once E1's feed answers.
5. **Chains:** `~1` r-4, `~2` o-4, `~3` l-4, `~4` m-4. No two cells write one file. All four are WORLD (the floor for `infra/`
   paths); no worker calls YCharts, writes the store, deploys or grants.

## 2. Contracts (round 4)

### 4.1 The call budget (built by YCD-r-4)

- `runner.run(..., budget=None)`. `budget` is `{"requests_per_window": N, "window_seconds": W}`; N is 1-6 and W is a positive
  int.
- With a budget, the planned requests are split into windows of at most N. After each window the runner releases the lease
  (`transport.close()`), waits W seconds through the session's wait (counted in `opal_waiting_ms`), and acquires a fresh lease
  for the next window. It never sends an (N+1)th request inside one window.
- Without a budget, a plan of more than 6 requests REFUSES before any lease (`BUDGET_REQUIRED:<n> requests`). Six or fewer run
  as today.
- CLI: `--requests-per-window N --window-seconds W`.
- A STOP inside any window ends the whole run (the C-SESSION stop rules hold per window).

### 4.2 The held-data feed (written by YCD-o-4)

Each HELD_DATA row of `overview_coverage.json` gains `"feed"`:
- `{"source": "OPAL_HELD", "table": "<estate table or object family>", "field": "<field>", "key": "<how a holding is keyed>"}`;
- or `{"source": "YCHARTS_SECURITY", "call": "<a call name in feed_probe_map.json>", "field": "<JSONPath>"}`;
- or `{"source": "NONE", "reason": "..."}`.

`deliverables/maps/feed_probe_map.json` is the C-MAP shape (calls only). Its calls are the YCharts security-level candidates
(`/charts/general_data.json`, `/charts/fund_data.json`, `/securities/securities_info`), each with `expand` over the holdings,
and it plans to **at most 6 requests** for Y-5's 99 holdings. It is what the issuer runs live.

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

### 4.4 The map label rule (built by YCD-m-4)

`map_pdf`'s label rule keeps a label containing a lowercase-initial word (`iShares`, `iPath`); a label is dropped only for a
reason that is not its case. The two maps' rows come from the rule, with no map-side repair. The m-3 rows W4-S4 names are added.

## 3. THE CELLS

### `YCD-r-4` -- the runner's call budget, and the keeper's point-object rule (E1 build, E3; FWD-1, FWD-2, FWD-6)
- `ycharts/research/runner.py`: contract 4.1.
- `ycharts/research/keeper.py`: the series rule (3.3) also reads DATA when `series[].data` is a list of point OBJECTS (dicts
  whose values include numbers), the live shape. Pin it with a fixture built from the round-2 kept scatter answer's TYPE
  SKELETON (keys and value types, no value).
- Tests: a 12-request plan runs as 2 windows of 6 with a release and a fresh lease between; a 7th request is never sent in a
  window; no budget with more than 6 requests refuses before the lease; a stop in window 2 ends the run; the point-object
  scatter skeleton labels DATA.

### `YCD-o-4` -- the held-data feed census and the security probe map (E1 build; FWD-1, FWD-3)
- Offline, read-only: for each of the 158 HELD_DATA rows' column groups, find whether Opal already holds that figure per
  holding, in the served holdings data or the estate's security tables (DynamoDB tables and S3 families the estate already
  reads, e.g. the ETF classifications, the security master, the served holdings snapshots). Read schemas, field names and
  key shapes only, never a client figure.
- Write 4.2's `feed` on each HELD_DATA row and `feed_probe_map.json` for the rest (at most 6 requests for 99 holdings).

### `YCD-l-4` -- the six statistics (E4; FWD-3)
- `ycharts/research/layout_overview.py`: 4.3's statistics in the computed path, with the trace.
- Tests named `test_six_statistic_*`: each of the six computed on a hand-checked fixture and NOT_AVAILABLE when its benchmark
  or risk-free input is absent.

### `YCD-m-4` -- the map label rule and the two maps' rows (E2; FWD-3, FWD-4)
- `ycharts/research/map_pdf.py`: 4.4's rule, with a test named `test_lowercase_*` (a label starting `iShares` is kept).
- Re-run on the two retained PDFs (as m-3 did, OS temp only): `comparison_map.json` and `multi_map.json` gain the 21 and 29
  rows that m-3.AC2 found missing. The Multi's third-security rows go on the comparison calls at `key_index` 2; the holdings
  rows are BUILDER_ONLY data rows. The Comparison's p8 Bond Maturity chart is listed, and p8.e03 sourced to its key. p22.e16-e19
  are masked. Element ids are never renumbered.

## 4. Not in round 4

The Comparison and Multi layouts (from their coverage, after E1's feed); FWD-5; FWD-7.
