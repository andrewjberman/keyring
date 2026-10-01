# ETFS_RIVALS -- DECOMPOSITION, ROUND 5 (ENRICHMENT): the G1 bound, the hop-9 method fixes, per-fund issuer floors, the v0.8 leg

```json
{
 "project": "ETFS_RIVALS",
 "round": 5,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.8, CVO-signed @18fca64073; text @fe946c1366)",
 "prd_version": "v0.8",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md@6dcb0074e4",
 "author": "2.0.0_SA_COO~RV",
 "cells": 8,
 "chains": 5,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0 at L5",
 "round4_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round4.md (blob 55eec38022)"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-01 ~23:xxZ.
**Source:** the CTO's message 28075 and the round-4 analysis, section 4: the 8 enrichment items, ONE issuance, cap 8, the W4-S9 bound
FIRST. Also binding:
- the hop-9 rulings (a), (b), (d) @4baf852611;
- PRD v0.8, with CVO~Z's condition that the ACWI/IWM G9 preview comes first;
- fabric rulings 8-12.

**Input state:**
- Round 4 is CLOSED (slug @7256e90b67).
- The 2026-10-01 page serves 13 funds, 12 updated.
- Code is at CLOUD 9e201639c3. The five Lambdas carry addendum 1's package (21:55Z).
- No round-5 cell deploys. Every cell is code + tests. The G5/G6 replay and the backfills are round 6, under a pair.

## Issuer rulings at this cut

1. **Cut by write set (C10); five chains.**
   - `~1` b-2 (G1 bound; `gold_canonical_shape.py`, `sweep.py`).
   - `~2` m-2 -> l-1 (`collector_bloomberg.py` serialises them).
   - `~3` h-4 -> h-5 -> h-6 (`gold_trade_schedule.py` serialises them).
   - `~4` f-4 (the page cell: `guardrails.py`, `publish_page.py`, `render.py`).
   - `~5` s-6 (`enrichment_bloomberg.py`).
   - Fan-out: 5 of 5 chains, cap 8.
   - `guardrails_config.json` belongs to h-5 alone. f-4 adds per-fund issuer support to `resolved_floor()` but sets no value; the
     values are a round-6 live-join act, measured as d-5 measured its floors.
   - `render.py` belongs to f-4 alone. The page halves of rulings (b) and (d) (a REFUSED window shown as not inferred;
     `key_resolution` shown) are f-4's, written column-optional, so f-4 depends on no other cell.
2. **The G1 bound is FIRST and gates every bulk run** (W4-S9; ruling 1).
   - Until it ships, COO~RV holds the disarm: no bulk batch runs (row Z-S12).
   - The bound is code-only: a time budget inside `gold_canonical_shape.handler_entry` and a cursor that continues from where it
     stopped. **No infra change in round 5.** The existing EventBridge trigger, async retries and the 09:00 sweep re-invoke an
     unfinished batch.
3. **The v0.8 leg ships INERT** (item 7).
   - The terminal vehicle runs the CLOUD working tree, so a merge IS a serve on that leg.
   - The four new names (IDVZ, PFOE, ACWI, IWM) enter the map as PENDING. The gate `RIVALFUNDS_LEG_ENABLE=1` makes them live.
   - The issuer sets the gate in round 6, after (i) the request-cost measurement per `integrations/bloomberg/READ_HERE.md`
     (PRD v0.8, Bloomberg budget) and (ii) the ACWI/IWM G9 style-read preview (CVO~Z's condition).
   - Retiring the `home_producer` read (IDVZ/PFOE) and switching their source is the SAME round-6 act. Round 5 changes no G1
     source.
4. **Drain timing for vehicle-run cells (m-2, l-1, s-6, all `SERVED`).**
   - The issuer drains them only after reading the 2026-10-02 morning: the 07:00 issuer fetch markers, the 08:03 vehicle exit
     lines, and the 09:00 sweep.
   - That keeps the first organic morning (W4-S13 and Z-S10's live tests) on known code.
5. **Fabric rulings bind every order:**
   - (9) a check that reads a whole window states its own bound; the orders say `timeout 600` for h-4.AC2, h-5.AC2 and b-2.AC1;
     rc 124 is never graded FAIL;
   - (10) a worker never holds a deploy-only ref;
   - (8) halves name the stage roles as the negative-control subject (round 6).
6. **Every check is issuer-written and dry-run at base 9e201639c3.** Each FAILs there for the defect it names, and its controls
   PASS there. Where a ruling names served cases (PFOE 2026-09-28; INEQ 2025-08-29, TXUE 2025-04-14), the check reads the served
   G1 READ-ONLY and runs the merged inference locally.

## Rulings reaching every cell

Rounds 1-4's rulings stand (`ETFS_RIVALS_DECOMP.round{1,2,3,4}.md`, "Rulings reaching every cell"):
- builder-only addresses;
- markers;
- one revision contract (`revision.newest`, never a name);
- per-source floors read through `guardrails.load_config()`;
- the Positioning pull read-only (Andrew-direct no-modify);
- no Bloomberg or OpenAI call from a worker;
- no S3 write;
- no deploy.

## 3. THE CELLS

### `RIV-b-2` -- a marker-driven G1 run is windowed and continued from a cursor (W4-S9; ruling 1; FIRST)

`gold_canonical_shape.handler_entry` takes a time budget: the event's `budget_s`, else the environment `RIVALFUNDS_G1_BUDGET_S`,
default 600 s.
- It stops STARTING report dates once the budget is spent.
- It returns status `PARTIAL` with a cursor in `detail`, and writes NO output marker.
- The same event re-invoked continues from the cursor: dates already built are not rebuilt.
- When every date is built it returns OK and writes the marker as today.
- `sweep.run_gold_chain` treats `PARTIAL` as not done and re-invokes while its own budget allows.
- Without a budget the behaviour is unchanged.
- No infra file changes.

### `RIV-m-2` -- the collector's capture dedup is linear (W5-S21; ruling 2)

`collector_bloomberg._existing_by_sha` re-lists and re-reads an acquisition partition's sidecars for every capture.
- Memoise the sidecar index per partition in the product sink for the run, or key the dedup on the sha, so a bulk import reads
  each sidecar a bounded number of times.
- `_issuer_has_bronze` (per issuer fund per day) gets the same memo.
- Idempotence across batch ids is unchanged.

### `RIV-l-1` -- the v0.8 Bloomberg leg, built and inert (PRD v0.8; item 7; after m-2 on `~2`)

`peer_groups.json` gains pending entries:
- ACWI (group IDVZ) and IWM (group PFOE): `role` index_control, `source_policy` bloomberg_primary, `"leg": "pending"`.
- IDVZ and PFOE: `"pending_source_policy": "bloomberg_primary"`.
- SCHY: `"pending_role": "rival"`.

Behaviour of the gate:
- **Unset:** every reader (`universe.funds`, `policy`, `entries`, `collector_bloomberg.funds_for_day`) behaves EXACTLY as today.
- **`RIVALFUNDS_LEG_ENABLE=1`:** pending entries and pending fields take effect:
  - the four join the leg;
  - one index_control per group, ACWI and IWM;
  - SCHY reads rival.
- `collector_bloomberg.request_plan(report_date)` returns the offline request plan: `funds`, `names`, and the request shape
  (sheets and rounds as `excel_fetch` would split them).
- No G1, silver or page change in this cell.

### `RIV-h-4` -- an ID-CHANGE needs an identifier relation; CUSIPs zero-padded at silver (hop-9 ruling a)

**When an exit and an entry pair as ID-CHANGE.** Only when one of these holds:
- a G3 or issuer-published identifier event names both;
- a crosswalk hit (ISIN, SEDOL or FIGI) maps one to the other;
- the two CUSIPs are equal after normalisation.

A shared CUSIP-6 qualifies only alongside a G3 event. Equal value alone stays an exit plus an entry, with real share counts.

**Normalisation.** `silver_issuer.parse_capture` zero-pads a CUSIP of 1-8 characters to 9 (BP `55622104` -> `055622104`).

### `RIV-h-5` -- an implausible window is REFUSED, never inferred (hop-9 ruling b; after h-4 on `~3`)

**Refusal rule.** A fund-window is refused when either holds:
- the flow factor f lies outside `flow_factor_band`;
- the share of its non-cash lines with quantity 0 on either side exceeds `max_zero_quantity_share`.

**Thresholds.** Both live in `guardrails_config.json` as PROVISIONAL: `flow_factor_band` value `[0.5, 1.5]`,
`max_zero_quantity_share` value `0.2`.

**What a refused window serves.**
- A G6 row gains `status` (`REFUSED`, or empty) and `reason` (`flow_factor_out_of_band` | `zero_quantity_share`).
- The window infers ZERO trades.
- The same rule runs on the daily, backfill and replay paths, so a refused window cannot reach served trades by any path.

### `RIV-h-6` -- key resolution is its own G5 column (hop-9 ruling d; after h-5 on `~3`)

- **New column.** G5 gains `key_resolution` in {`RESOLVED`, `ALIAS`, `UNRESOLVED`}. ALIAS is a resolved key whose G1
  `resolution_method` is `issuer-alias`.
- **Confidence.** `confidence` grades the inference only (flow factor, event cleaning, price band). It is no longer overridden by
  `UNRESOLVED`.
- **Additive.** `key_resolved` is still written.

### `RIV-f-4` -- the page cell: per-fund issuer floors, the headline, the REFUSED and key-resolution displays (rulings 3, 7; b and d's page halves)

**Per-fund issuer floors.** `guardrails.resolved_floor()` accepts per-fund entries under `issuer` (`{"issuer": {"BASG": x, "GQGU":
y}}`, like `home_funds`).
- An issuer fund the table does not name is held to the strictest issuer floor, and the reason names it.
- The shipped config is not changed by this cell.

**Headline.** The manifest's top-level `status` means "page published".
- The headline states "`<n>` of `<m>` funds current", from the manifest's counts.
- It names each lagging fund with its reason.
- Failed figures still never publish (FWD-9).

**REFUSED windows.** A G6 row whose `status` is REFUSED renders as "not inferred" with its reason, never as an empty window.

**Key resolution.** Where G5 carries `key_resolution`, the page shows it where it showed UNRESOLVED.

**Column-optional.** Every column read here is optional.

### `RIV-s-6` -- the G4 as-of guard (W3-S15; ruling 4)

`enrichment_bloomberg`'s market pull never writes current values under a past partition.
- **Past date.** A date before the run date (ET) uses a historical request through a new hook `_blp_historical_data(securities,
  fields, start, end, ...)` (wrapping `integrations/bloomberg/mcp/blp_client.historical_data`). Its rows carry `as_of` = that date
  and `as_of_source` = `historical`.
- **No historical answer.** If the historical request answers nothing, nothing is written under the past date, and the result says
  so.
- **Run date.** A pull for the run date carries `as_of_source` = `pull`.

## 4. DEPENDENCY EDGES AND CHAINS

```
~1  RIV-b-2                         (FIRST: gates every bulk run)
~2  RIV-m-2 --> RIV-l-1             (collector_bloomberg.py)
~3  RIV-h-4 --> RIV-h-5 --> RIV-h-6 (gold_trade_schedule.py)
~4  RIV-f-4                         (guardrails.py, publish_page.py, render.py)
~5  RIV-s-6                         (enrichment_bloomberg.py)
```

**Write sets**, disjoint across concurrent orders:

| cell(s) | writes |
|---|---|
| b-2 | `gold_canonical_shape.py`, `sweep.py` |
| m-2, l-1 (`~2`, serial) | `collector_bloomberg.py`, `universe.py`, `peer_groups.json` (l-1) |
| h-4, h-5, h-6 (`~3`, serial) | `gold_trade_schedule.py`, `silver_issuer.py` (h-4), `gold_flow_reconciliation.py` and `guardrails_config.json` (h-5) |
| f-4 | `guardrails.py`, `publish_page.py`, `render.py` |
| s-6 | `enrichment_bloomberg.py` |

## 5. BATTERY

- **comp-schedule (RUN):** no armed gate names this project's surfaces. The vehicle's 08:03 leg runs the CLOUD tree (ruling 4
  times the vehicle-run drains).
- **comp-iam:** no IAM change in any cell.
- **comp-adversary:** declared on b-2 (any batch size completes, and no date is built twice) and l-1 (inert by default, proved by
  the gate-unset clause).
