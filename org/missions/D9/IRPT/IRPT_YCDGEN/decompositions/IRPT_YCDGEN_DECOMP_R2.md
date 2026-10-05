# IRPT_YCDGEN -- DECOMPOSITION, ROUND 2 (ENRICHMENT): the map's missing charts, the coverage table, the runner's two repairs

```json
{
 "project": "IRPT_YCDGEN",
 "round": 2,
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.1 @8b364d6d94; RATIFIED)",
 "prd_version": "v0.1",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_YCDGEN_ROUND1_20261004.md @34daa80ad5 section 2",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "round_scope": ["FWD-1", "FWD-2", "FWD-3", "FWD-6"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 3,
 "chains": 3,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "cell_ids": ["YCD-r-2", "YCD-m-2", "YCD-c-2"]
}
```

**Issuer:** `2.0.0_SA_COO~Y`, 2026-10-04 ~21:5xZ, FULL lease. **Source:** the CTO's round-1 analysis, section 2, which is the
enrichment list E1 to E5, read as this round's rectangle. Round 1's contracts (`IRPT_YCDGEN_DECOMP.md` section 2: C-KEEP 2.1,
C-RUN 2.2, C-MAP 2.3, the module home 2.4) hold unchanged unless a cell below says otherwise.

## Issuer rulings at this cut

1. **E1 is Andrew's act, not a cell.** `~Y` puts a fresh short-lived signed link to the run-3 report to him in its session;
   the run record notes whether he had it in the same sitting.
2. **E4 and E5 are both runner repairs, so they are batched into ONE cell** (`YCD-r-2`; spine: repairs batched into one
   cell).
3. **E3's live calls are the issuer's, not the worker's.** The cell builds the coverage table offline and a probe map.
   The issuer runs the probe map once at close: inside the lease, one call at a time, under `~Y`'s egress word, with no
   generate call. That keeps every YCharts call on the one seat that serializes them with the served runs.
4. **Chains, cut by write set:**
   - `~1`: `YCD-r-2` (runner.py and its tests);
   - `~2`: `YCD-m-2` (map_pdf.py, its tests, overview_map.json);
   - `~3`: `YCD-c-2` (two new files under `deliverables/maps/`).

   No two cells write the same file. `YCD-c-2` classifies round 1's element ids; the chart elements `YCD-m-2` adds are
   classified at the issuer's close.
5. **Risk:** all three are WORLD, the gate's floor for `infra/` paths and the class of `YCD-c-2`'s vendor-facing probe map.
   No cell deploys, grants or writes the store.

## 2. Contract additions (this round)

### 2.5 The previous-run index (FWD-2; cell YCD-r-2)

- Key: `address('irpt', firm, 'state', 'ycharts_runs', 'index=latest', object='latest_by_portfolio.json')`, i.e.
  `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/index=latest/latest_by_portfolio.json` for Cottonwood.
  It sits inside the research principal's Put/Get grant (`ycharts_runs/*`); no list grant exists or is added.
- Body: `{"schema": "irpt-ycdgen-run-index-v1", "firm": "...", "portfolios": {"P:123": {"request_id": "...",
  "run_key": "...", "at": "..."}}}`.
- Without a list grant, a missing key reads AccessDenied, the same as a real permission failure. So a missing or
  unreadable index REFUSES before the lease (`RUN_REFUSED:PREVIOUS_INDEX_UNREADABLE`), unless the CLI is given
  `--bootstrap-index`; that flag writes an empty index and is used once per firm by the issuer.
- After a run that kept at least one call, the runner writes the index entry for its portfolio (read, modify, write).
  Runs are serialized by the lease, so the read-modify-write cannot race.
- `changed_since_previous` is `no_previous` only when the index has no entry for the portfolio.

### 2.6 The stop row (C-SESSION; cell YCD-r-2)

- On any STOP (a STOP_DECISIONS reply, a lease refusal, a lease-release failure), the runner writes
  `address('irpt', firm, 'state', 'ycharts_runs', 'request=' + request_id, object='stop_row.json')` beside run.json. It
  is a surprise-row-shaped object WITHOUT an `id`: `project`, `fabric` (`laptop`), `surfaced_by` (the runner's
  `--surfaced-by`, default `2.0.0_SA_COO~Y`), `surfaced_at`, `one_line`, `class` `OBSERVATION`, `hazard_standing`
  `INERT`, `grounding` (status GROUNDED; evidence = the run key and the stop reason), `disposition`
  `UNDER_INVESTIGATION`, `spec_asserts` (the C-SESSION sentence), `world_is` (the step, call name, HTTP status and
  decision).
- `ycharts/research/file_stop_row.py <stop_row.json> <row-id>` prints the channel section (`## <id> -- <title>` and a fenced
  json row with the id set) for the issuer to append and commit. The issuer files it; the runner never writes git.

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

## 3. THE CELLS

### `YCD-r-2` -- the runner's previous-run lookup and its stop row (E4, E5; FWD-2, C-SESSION)
- `ycharts/research/runner.py`:
  - `RunIndex(s3_client)` with `get(firm)` and `put(firm, doc)` at 2.5's key.
  - `main()` reads the index BEFORE the lease (2.5 refusal; `--bootstrap-index` writes an empty one), passes the
    previous run.json for the portfolio (via `RunStore.get`) to `run()`, and after the run writes the portfolio's entry
    when at least one call was kept.
  - `run()` on a STOP writes 2.6's stop row through a `stops` writer (same S3 client), after the lease is released.
- `ycharts/research/file_stop_row.py`, as in 2.6.
- Tests (in `tests/test_runner.py`, plus `tests/test_file_stop_row.py`):
  - a run-2-then-run-3 case reads `changed_since_previous` `false` for an unchanged answer and `true` for a changed one,
    and `no_previous` only for a portfolio absent from the index;
  - a missing index refuses before any lease, and `--bootstrap-index` writes an empty index;
  - a WAF-challenged call writes a stop row whose `world_is` names the step and decision, and the lease is released;
  - `file_stop_row.py` prints a section the surprise-row gate's schema admits.

### `YCD-m-2` -- the map's four vector-drawn charts and two small gaps (E2; FWD-3, m-1.AC2)
- `ycharts/research/map_pdf.py`: detect a chart drawn as vector shapes (pdfplumber `rects`, `curves`, `lines` clustered into
  one region), not only an embedded image, and give it the nearest printed title as its label.
- Re-run on the same retained source Overview (the 23-page PDF of row W2-S2, read from S3 into OS temp only, never into
  the repo), then update `overview_map.json`:
  - add the four charts: p3 Stock Style Exposure, p3 Market Classification, p3 Region, p5 Stock Sector Exposure. Each
    gets the next unused element id on its page; existing ids never renumber;
  - p14.e03 lists all six of its columns;
  - p13.e04 regains its dropped header word.
- A test on a small synthetic PDF (made in the test with reportlab or pypdf drawing ops, if available, or a fixture
  under `tests/fixtures/`) has one chart drawn only as rectangles, and it is detected with its title.

### `YCD-c-2` -- the coverage table for the 176 unanswered elements, and the probe map (E3; FWD-3, FWD-1 depth)
- Inputs, read-only: the map; run 3's kept answers (`s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/
  request=YCD-R1-20261004T1944Z/`, six objects, read with the laptop's credentials into OS temp, never into the repo); the
  HAR request shapes file the issuer extracted (method, path and parameter NAMES only); the estate's YCharts clients
  (the gateway's `client.py`, `ycharts-market-data-pull/ycharts_client.py`); the security-level data Opal already reads
  (the served generate path's `securities_info`, `general_data`, `fund_data` uses).
- Output: 2.7's two files. No figure value enters git (C-FIRM): classes, reasons, endpoint paths and field paths only.

## 4. Not in round 2

FWD-4 and FWD-7 (Comparison and Multi) wait for 2.7's table (CTO analysis section 2). FWD-5 (the firm-private read) is
round 3. No portal page, no schedule, no second firm.
