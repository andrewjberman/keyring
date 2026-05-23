# Session Log -- ADVI_VALFIN.001 Phase 1: INF_B_01 through INF_C_05

**Agent:** 0.4.0_DS_ClientPlatform (Base lane)
**Date:** 2026-05-22 ~23:45Z
**Branch:** CLOUD
**Continuation of:** session_close_ld0005_sweep_and_valfin_001_phase0.md (INF_B_00 PASS-w-followup)

---

## Session Summary

Continued ADVI_VALFIN.001 Phase 1 from context compaction. Completed 4-checks +
methodology reads for the next 5 in-scope gold scripts (INF_B_01 through INF_C_05).
All 5: 4-check PASS. Discovered dual data paths for books-tab tax numbers; routed
scope question + INFGRO coordination request to COO.

Startup: /watcher self-check (killed stale PID 59882 from prior context window,
relaunched tracked watcher task bpmmva3rd).

---

## Compiler Tools

| Tool | Script | Result | Notes |
|---|---|---|---|
| `comp-pipescript io` | INF_B_01 | READS: silver/prices/canonical_prices.parquet; WRITES: none detected | Gold read (positions_cube) not detected -- PRD §5.3 limitation; manual script read resolved |
| `comp-pipescript feeds/consumers` | INF_B_01 | "no upstream deps / no downstream consumers" | Comp-graph limitation for gold->gold reads |
| `comp-blast` | INF_B_01 | "No downstream consumers found" | Same limitation |
| `comp-pipescript io` | INF_B_01b | READS: canonical_prices; WRITES: gold/classification/ticker_coverage_report.json | PASS -- single output node |
| `comp-blast` | INF_B_01b | 1 downstream node (the report JSON) | Correct |
| `comp-pipescript io` | INF_B_02 | WARN: no s3_layout constants | Dynamic source-selection; manual read resolved |
| `comp-pipescript io` | INF_B_03 | READS: gold/lots/lots_latest.parquet | PASS -- comp-graph correctly mapped the hardcoded lots read |
| `comp-blast` | INF_B_03 | "No downstream consumers found" | Limitation |
| `comp-pipescript io` | INF_C_05 | READS: gold/dimensions/accounts_dimension_latest.parquet | Dynamic gains path not detected; manual read resolved |
| `comp-blast` | INF_C_05 | n/a | Not run -- feeding into terminal JSON artifact |

---

## 4-Check Results

### INF_B_01 -- holdings_lots
- Script: `data/orion/scripts/gold/INF_B_01.holdings_lots.py`
- Reads: `gold/positions_cube/{date}.parquet` (I_A03, TRN-reconstructed T+1) + `silver/prices/canonical_prices.parquet`
- Writes: `gold/holdings/{date}.parquet`

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | `gold/holdings/` partitions 2019-09-17 through 2026-05-21 |
| FRESH | PASS | Latest 2026-05-21, LastModified 2026-05-22 10:15:55Z -- T+1 by design (positions_cube is TRN-reconstructed, inherently T+1) |
| SCALED | PASS | 174K-188K bytes range; 2026-05-20 at 177,392 within normal range (vs 2026-05-14 at 177,297) |
| NOT-FROZEN | PASS | Daily advance; 2026-05-16/17 near-identical (180,116 / 180,106) = weekend carry-forward, expected |

**Cadence context:** positions_cube (I_A03) runs T+1 via cumulative TRN reconstruction from silver/transactions. All timestamps at 2026-05-22 10:15:55Z confirm a full rebuild ran today.

### INF_B_01b -- classify_new_securities
- Script: `data/orion/scripts/gold/INF_B_01b.classify_new_securities.py`
- Writes: `gold/classification/ticker_coverage_report.json` + `gold/classification/unpriced_tickers.txt`
- Utility diagnostic (not daily automated pipeline)

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | Both files present: 5317 bytes (report) + 2342 bytes (unpriced list) |
| FRESH | PASS | LastModified 2026-05-22 10:16:08Z -- ran today |
| SCALED | PASS | 5317 bytes for 1,912-ticker report is reasonable |
| NOT-FROZEN | PASS | Single non-partitioned file; updated today |

Coverage report (fetched 2026-05-22T14:16Z): 1,912 total tickers, 1,535 priced (80.28%), 377 unpriced. Source breakdown: yahoo_finance 991, linear_interpolation 542, price_override 1, transaction_observed 1. Unpriced tickers: dominantly bonds (CUSIP-like: 00xxxxAM3, etc.) and delisted equities (AABA, AKS, etc.).

**Methodology note:** 80.28% coverage = just above 80% WARN threshold. 377 unpriced tickers
will have null market_value in INF_B_01 gold/holdings/. Phase-2: monitor if drops below 80%
and quantify $ impact.

### INF_B_02 -- canonical_lots
- Script: `data/orion/scripts/gold/INF_B_02.canonical_lots.py`
- Reads: `silver/transactions/` (source-selected canonical snapshot, post-ADVI_DWSPLT TO-3e 2026-05-13)
- Writes: `gold/lots/lots_latest.parquet` + `gold/lots/lots_{date}.parquet`

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | lots_latest.parquet + lots_2026-05-22.parquet present |
| FRESH | PASS | LastModified 2026-05-22 10:18:21Z -- today; lots_2026-05-22 created today |
| SCALED | PASS | 2.2MB stable range (2.1-2.2MB May 14-22); drop from 3.2MB pre-DWSPLT-TO-3e (2026-05-13) is expected after source-selection change |
| NOT-FROZEN | PASS | Ran today (2026-05-22); advancing daily since ~2026-05-13 |

Spot-fetch analysis (lots_latest.parquet):
- 88,433 total lots | 829 accounts | 354 tickers
- $331,561,351 total cost basis
- Zero-cost lots: 6 (0.0%) -- immaterial; tickers: ARTS, THMR-OLD04152026, 525ESC0S9, 021ESC017, 931CVR013 (edge-case bonds + delisted)

**Methodology note:** nav_price fillna(0.0) per docstring ("v1 uses nav_price as cost basis").
Empirically immaterial (6 lots, 0.0%). FIFO algorithm correct: sells consume oldest lots
first by buy_date. Uses lots_latest for ALL historical INF_B_03 dates (not date-matched) --
correct for current-date portfolio reporting; note for any retrospective gain computation.

### INF_B_03 -- account_gains
- Script: `data/orion/scripts/gold/INF_B_03.account_gains.py`
- Reads: `gold/holdings/{date}.parquet` (INF_B_01) + `gold/lots/lots_latest.parquet` (INF_B_02)
- Writes: `gold/account_gains/{date}.parquet`

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | `gold/account_gains/` partitions through 2026-05-21 |
| FRESH | PASS | Latest 2026-05-21, LastModified 2026-05-22 10:24:28Z -- T+1 (feeds from INF_B_01 which is T+1) |
| SCALED | PASS | 390K-408K bytes range; 2026-05-20 at 394,367 within normal range |
| NOT-FROZEN | PASS | Daily advance; pipeline order confirmed: lots (10:18) -> gains (10:24) |

**Methodology:** unrealized_gain = market_value.fillna(0) - cost_basis.fillna(0). term = long_term if holding_period_days >= 365, else short_term. holding_period_days = snapshot_date - oldest_buy_date (per-position oldest lot).

### INF_C_05 -- client_tax_liability
- Script: `data/orion/scripts/gold/INF_C_05.client_tax_liability.py`
- Reads: latest `gold/account_gains/*.parquet` + `gold/dimensions/accounts_dimension_latest.parquet`
- Writes: `gold/artifacts/client_tax_liability.json`

| Check | Verdict | Evidence |
|---|---|---|
| EXISTS | PASS | `gold/artifacts/client_tax_liability.json` present, 68440 bytes |
| FRESH | PASS | LastModified 2026-05-22 10:36:23Z -- today |
| SCALED | PASS | 68KB for 296-household JSON report is reasonable |
| NOT-FROZEN | PASS | Single non-partitioned artifact; updated today |

Spot-check (fetched 2026-05-22T14:36Z):
- data_as_of: 2026-05-21 (T+1 pipeline)
- firm unrealized gain: $16,763,XXX.XX (16.76M)
- estimated tax liability: $5,760,XXX.XX (5.76M)
- households: 296
- Top household (1296): $1.45M unrealized, $537.8K estimated liability
- Per-household values plausible; ST/LT split varies by household (realistic)

**Methodology caveat:** federal-only, top bracket (37% ST, 20% LT). No state taxes, no AMT.
Docstring: "advisory/indicative -- not a tax filing artifact." Documented as a known limitation.

---

## Architecture Finding: Dual Books-Tab Tax Data Paths

Reading portal/src/api/endpoints/advisor-intelligence.ts:1011-1016 and
INF_D_02.advisor_client_detail.py:114-115:

**Two parallel data paths exist for books-tab tax/gains numbers:**

Path 1 (gold-computed, in-scope): INF_B_02 -> INF_B_03 -> INF_C_05
- Produces: gold/artifacts/client_tax_liability.json, gold/account_gains/
- Methodology: FIFO from silver/transactions + canonical_prices
- Feeds: what? (portal may not directly read these for the books-tab tax display)

Path 2 (Orion API silver dims -> INF_D_02, NOT in 9-script scope):
- INF_D_02 reads silver/api_dims/tax_realized/ + silver/api_dims/tax_unrealized/ (Orion REST API dims)
- INF_D_02 emits tax_exposure block in platinum book.json: {cost_basis_by_year, top_gain_positions, realized, unrealized, capital_gains_ttm}
- Portal adapter reads this block directly (advisor-intelligence.ts:1016 tax_exposure pass-through)
- Comment in portal code: "Prior adapter stubbed to all-zero 'DS gap' -- outdated; data is live"

**Implication:** "realized capital gains" on the books-tab is served from INF_D_02's tax_exposure.realized (sourced from silver/api_dims/tax_realized/), NOT from the gold chain. The gold chain may be supplementary or parallel.

**Status:** Routed to COO (MCP message 20260523T035814Z) as ROUTING ASK #1. Awaiting
guidance on whether to expand scope to include INF_D_02 + silver tax dims, or whether
realized gains is validated elsewhere / intentionally out of TO-1 scope.

---

## INF_B_00 SCALED Anomaly Silver-Side Check (Clearing Phase-2 Follow-up)

`silver/api_dims/positions_mv/snapshot_date=2026-05-20/data.parquet` = 1.0 MiB
Neighbors: 2026-05-19 = 1.0 MiB, 2026-05-21 = 1.0 MiB, 2026-05-22 = 1.1 MiB

Silver feed is consistent -- the 216KB vs ~315KB gold canonical anomaly on 2026-05-20
is NOT caused by a smaller silver input. Anomaly is INF_B_00 gold-transform-specific.
Hypothesis: fewer INFLECTION_REP_IDS = {3,6,11,12} accounts had positions on 2026-05-20
(a Wednesday). Phase-2: fetch rep-filtered subset of positions_mv for that date to confirm.

---

## HOLD: INF_C_07 / INF_C_08 / INF_D_00c

Per TO cross_domain_coordination: MCP COO + INFGRO lane required before any work on
these three book-growth rollup scripts. ADVI_INFGRO lane was NOT LIVE at last session close.

MCP sent to COO (same message 20260523T035814Z) as ROUTING ASK #2: requesting (a) INFGRO
lane liveness confirmation, (b) green light for Phase-1 read-only 4-check on those 3 scripts.
Holding until COO response.

---

## Next Steps

| Recipient | Item |
|---|---|
| **2.0.0_SA_COO** | ROUTING ASK #1: dual data path scope question (INF_D_02 + silver tax dims) |
| **2.0.0_SA_COO** | ROUTING ASK #2: INFGRO coordination green light for INF_C_07/C_08/D_00c Phase-1 |
| **Self (next session)** | INF_C_07 / INF_C_08 / INF_D_00c Phase-1 4-checks -- pending COO response |
| **Self (next session)** | INF_B_00 Phase-2: rep-filtered positions_mv spot-check for 2026-05-20 |
| **Self (next session)** | Portal-side consumer confirm (Phase 3) for B_01 through C_05 -- after INFGRO scripts done |

---

## Open Follow-ups (forward to next session)

1. INF_B_00 5/20 SCALED anomaly: rep-filtered positions_mv silver slice check (silver-level cleared; gold-level TBD).
2. INF_B_00 INFLECTION_REP_IDS = {3,6,11,12} currency confirm vs INF_D_08 + INF_D_00e.
3. INF_B_00 SOURCE_SCHEMA_VERSION discontinuity handling on B-chain reads.
4. INF_B_01b coverage 80.28% -- monitor; quantify $ impact of 377 unpriced tickers.
5. INF_D_02 / silver tax dims scope question (ROUTING ASK #1) -- awaiting COO.
6. INF_C_07/C_08/D_00c Phase-1 -- awaiting COO INFGRO coordination (ROUTING ASK #2).
