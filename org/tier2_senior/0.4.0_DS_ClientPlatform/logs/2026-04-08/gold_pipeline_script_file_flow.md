# Gold Pipeline -- Script-to-File Flow Reference
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Project:** ADVI_GLDOPS (reference documentation)

---

## Summary

Complete mapping of every gold layer script, the S3 files it produces, the files it reads,
and what downstream scripts consume its output. All paths under `s3://opal-data-bd/`.
Scripts live at `data/black_diamond/scripts/gold/`. Key registry: `lib/s3_layout.py`.

---

## Execution Order

```
CHAIN: full (daily)
  B_00 -> B_02 -> B_03 -> C_00 -> C_01 -> C_02 -> C_04
  -> C_03 -> C_05 -> C_07 -> C_06 -> C_08 -> D_00 -> D_01 -> D_02 -> D_03

CHAIN: rebuild (rare, after schema change)
  A_00 -> A_01 -> A_02 -> A_03 -> A_04 -> B_01
  -> B_00 -> B_02 -> B_03 -> C_00 -> C_01 -> C_02 -> C_04
  -> C_03 -> C_05 -> C_07 -> C_06 -> C_08 -> D_00 -> D_01 -> D_02 -> D_03
```

---

## Silver Layer Inputs

| S3 Key | Format | Description |
|--------|--------|-------------|
| `silver/transactions/{YYYY-MM-DD}.parquet` | parquet | Daily BD transaction exports |
| `silver/allocations/{YYYY-MM-DD}.parquet` | parquet | Daily BD allocation exports |
| `silver/fees/{YYYY-MM-DD}.parquet` | parquet | Daily BD fee exports |
| `silver/prices/canonical_prices.parquet` | parquet | Merged pricing (Yahoo + overrides) |
| `silver/unrealized/unrealized_gain_loss.parquet` | parquet | BD unrealized gain/loss |
| `silver/realized/bd_realized_compact.parquet` | parquet | BD realized gain/loss |
| `schwab/silver/rps/date={YYYYMMDD}/data.parquet` | parquet | Schwab RPS (positions) |
| `schwab/silver/uln/date={YYYYMMDD}/data.parquet` | parquet | Schwab ULN (unrealized lots) |
| `schwab/silver/rld/date={YYYYMMDD}/data.parquet` | parquet | Schwab RLD (realized lots) |

---

## Group A -- Foundation (dimensions, run infrequently)

### A_00 accounts_dimension

| | |
|---|---|
| **Script** | `A_00.accounts_dimension.py` |
| **Reads** | `silver/transactions/{date}.parquet`, `silver/allocations/{date}.parquet` |
| **Writes** | `gold/dimensions/accounts_dimension_latest.parquet` |
| **Format** | parquet |
| **Consumed by** | A_01, A_04, B_00, B_01, B_02, C_00, C_01, C_02, C_03, C_05, C_06, D_00, D_01 |

### A_01 advisor_assignments

| | |
|---|---|
| **Script** | `A_01.advisor_assignments.py` |
| **Reads** | `silver/transactions/{date}.parquet`, A_00 `gold/dimensions/accounts_dimension_latest.parquet` |
| **Writes** | `gold/dimensions/advisor_assignments_history.parquet` |
| **Format** | parquet |
| **Consumed by** | C_08 |

### A_02 fee_rate_history

| | |
|---|---|
| **Script** | `A_02.fee_rate_history.py` |
| **Reads** | `silver/fees/{date}.parquet`, `silver/allocations/{date}.parquet` |
| **Writes** | `gold/dimensions/fee_rate_history.parquet` |
| **Format** | parquet |
| **Consumed by** | C_08, D_02 |

### A_03 positions_cube

| | |
|---|---|
| **Script** | `A_03.positions_cube.py` |
| **Reads** | `silver/transactions/{date}.parquet` |
| **Writes** | `gold/timeseries/positions_cube/{YYYY-MM-DD}.parquet` (one per date), `gold/timeseries/synthetic_positions_index.parquet` |
| **Format** | parquet |
| **Consumed by** | B_00, C_06, D_03 |

### A_04 client_dimension

| | |
|---|---|
| **Script** | `A_04.client_dimension.py` |
| **Reads** | A_00 `gold/dimensions/accounts_dimension_latest.parquet`, `silver/transactions/{date}.parquet` |
| **Writes** | `gold/dimensions/client_dimension.parquet` |
| **Format** | parquet |
| **Consumed by** | D_00, D_01, D_02, D_03 |

---

## Group B -- Holdings (canonical stack)

### B_00 canonical_holdings

| | |
|---|---|
| **Script** | `B_00.canonical_holdings.py` |
| **Reads** | A_03 `gold/timeseries/positions_cube/{date}.parquet`, `schwab/silver/rps/`, `silver/unrealized/`, `silver/realized/`, `silver/prices/canonical_prices.parquet`, `gold/dimensions/schwab_bd_account_mapping.parquet` |
| **Writes** | `gold/canonical/holdings/{YYYY-MM-DD}.parquet`, `gold/canonical/holdings_gaps/{YYYY-MM-DD}.parquet` (when gaps), `gold/canonical/watermarks.json` |
| **Format** | parquet + JSON |
| **Consumed by** | B_02, B_03, C_02 |

### B_01 holdings_lots

| | |
|---|---|
| **Script** | `B_01.holdings_lots.py` |
| **Reads** | `silver/transactions/{date}.parquet`, `silver/prices/canonical_prices.parquet`, A_00 `gold/dimensions/accounts_dimension_latest.parquet` |
| **Writes** | `gold/timeseries/holdings_lots/{YYYY-MM-DD}.parquet` |
| **Format** | parquet |
| **Consumed by** | D_00, D_02, D_03 |
| **Note** | Runs in foundation chain, not canonical |

### B_02 canonical_lots

| | |
|---|---|
| **Script** | `B_02.canonical_lots.py` |
| **Reads** | B_00 `gold/canonical/holdings/{date}.parquet`, `schwab/silver/uln/`, `schwab/silver/rld/`, `silver/unrealized/`, `silver/realized/`, `silver/prices/canonical_prices.parquet`, A_00, `gold/dimensions/schwab_bd_account_mapping.parquet` |
| **Writes** | `gold/canonical/lots_unrealized/{YYYY-MM-DD}.parquet`, `gold/canonical/lots_realized/{YYYY-MM-DD}.parquet` |
| **Format** | parquet |
| **Consumed by** | B_03, C_05 |

### B_03 account_gains

| | |
|---|---|
| **Script** | `B_03.account_gains.py` |
| **Reads** | B_00 `gold/canonical/holdings/{t-1}.parquet` (prior day), B_00 `gold/canonical/holdings/{t}.parquet` (current), B_02 `gold/canonical/lots_realized/{t}.parquet`, B_02 `gold/canonical/lots_unrealized/{t}.parquet`, `silver/transactions/{t}.parquet` |
| **Writes** | `gold/canonical/account_gains/{YYYY-MM-DD}.parquet` |
| **Format** | parquet |
| **Consumed by** | C_00, C_01, C_02, C_03 |

---

## Group C -- Activity (performance, NNA, analytics)

### C_00 canonical_performance

| | |
|---|---|
| **Script** | `C_00.canonical_performance.py` |
| **Reads** | B_03 `gold/canonical/account_gains/{date}.parquet`, A_00 `gold/dimensions/accounts_dimension_latest.parquet` |
| **Writes** | `gold/canonical/performance/{YYYY-MM-DD}.parquet` |
| **Format** | parquet |
| **Consumed by** | C_02 |

### C_01 canonical_nna

| | |
|---|---|
| **Script** | `C_01.canonical_nna.py` |
| **Reads** | B_03 `gold/canonical/account_gains/{date}.parquet`, A_00, `silver/transactions/` (via `lib/nna_flows.py`) |
| **Writes** | `gold/canonical/nna/{YYYY-MM-DD}.parquet`, `gold/canonical/nna_validation/{YYYY-MM-DD}.json` (diagnostic) |
| **Format** | parquet + JSON |
| **Consumed by** | C_02, C_08, D_00, D_01 |

### C_02 client_performance

| | |
|---|---|
| **Script** | `C_02.client_performance.py` |
| **Reads** | C_00 `gold/canonical/performance/{date}.parquet`, B_03, B_00 `gold/canonical/holdings/{date}.parquet`, A_00, `silver/transactions/` (via nna_flows), `silver/allocations/{date}.parquet` |
| **Writes** | `gold/timeseries/client_performance.parquet`, `gold/validation/aua_certification/{date}.json` |
| **Format** | parquet + JSON |
| **Consumed by** | C_03, C_04, D_00, D_01, D_03 |

### C_03 account_performance

| | |
|---|---|
| **Script** | `C_03.account_performance.py` |
| **Reads** | B_03 `gold/canonical/account_gains/{date}.parquet`, A_00, `silver/transactions/` (via nna_flows) |
| **Writes** | `gold/timeseries/account_performance.parquet` |
| **Format** | parquet |
| **Consumed by** | C_06, C_07, D_01, D_02, D_03 |

### C_04 validate_aua

| | |
|---|---|
| **Script** | `C_04.validate_aua.py` |
| **Reads** | C_02 `gold/timeseries/client_performance.parquet`, `silver/allocations/{date}.parquet` |
| **Writes** | `gold/validation/aua_validation_{date}.json` |
| **Format** | JSON (validation only, no downstream consumers) |

### C_05 client_tax_liability

| | |
|---|---|
| **Script** | `C_05.client_tax_liability.py` |
| **Reads** | B_02 `gold/canonical/lots_unrealized/{date}.parquet`, A_00 |
| **Writes** | `gold/views/client_tax_liability.parquet` |
| **Format** | parquet |
| **Consumed by** | D_00, D_02 |

### C_06 client_mix_timeseries

| | |
|---|---|
| **Script** | `C_06.client_mix_timeseries.py` |
| **Reads** | A_03 `gold/timeseries/positions_cube/{date}.parquet`, `silver/prices/canonical_prices.parquet`, A_00, C_03 `gold/timeseries/account_performance.parquet` |
| **Writes** | `gold/entities/clients/{rel_id}.json` (one per relationship ~600), `gold/entities/clients/{rel_id}_views.json`, `gold/views/mix_daily_summary.json`, `gold/meta/client_timeseries_watermark.json` |
| **Format** | JSON |
| **Consumed by** | Portal (direct S3 reads via CloudFront) |

### C_07 advisor_attribution

| | |
|---|---|
| **Script** | `C_07.advisor_attribution.py` |
| **Reads** | A_00 `gold/dimensions/accounts_dimension_latest.parquet`, C_03 `gold/timeseries/account_performance.parquet` |
| **Writes** | `gold/views/account_team.parquet`, `gold/views/relationship_team.parquet`, `gold/views/rel_architect_lookup.parquet` |
| **Format** | parquet |
| **Consumed by** | C_08, D_00, D_02, D_03 |

### C_08 advisor_fee_efficiency

| | |
|---|---|
| **Script** | `C_08.advisor_fee_efficiency.py` |
| **Reads** | C_01 `gold/canonical/nna/{date}.parquet`, C_07 `gold/views/account_team.parquet`, A_01 `gold/dimensions/advisor_assignments_history.parquet`, A_02 `gold/dimensions/fee_rate_history.parquet` |
| **Writes** | `gold/canonical/advisor_fee_detail/{YYYY-MM-DD}.parquet` (one per date), `gold/artifacts/advisor_fee_efficiency.json` (scorecard) |
| **Format** | parquet + JSON |
| **Consumed by** | D_00, D_02 |

---

## Group D -- Portal Publishers (JSON artifacts)

### D_00 portal_aggregates

| | |
|---|---|
| **Script** | `D_00.portal_aggregates.py` |
| **Reads** | C_02 `client_performance.parquet`, C_01 `nna/{date}.parquet`, C_07 `account_team.parquet` + `rel_architect_lookup.parquet`, A_04 `client_dimension.parquet`, A_00 `accounts_dimension_latest.parquet`, C_05 `client_tax_liability.parquet`, B_01 `holdings_lots/{date}.parquet`, C_08 `advisor_fee_detail/{date}.parquet` |
| **Writes** | |

| S3 Key | Description |
|--------|-------------|
| `gold/artifacts/timeseries_chart.json` | Firm-level AUA/NNA timeseries for main chart |
| `gold/artifacts/architect_leaderboard.json` | Architect leaderboard data |
| `gold/artifacts/employee_leaderboard.json` | Employee leaderboard data |
| `gold/artifacts/clients_tab.json` | Clients tab (firm headline + ~600 client entries) |
| `gold/artifacts/summary/header_metrics.json` | Dashboard header KPIs |
| `gold/artifacts/filters/dimensions.json` | Filter dropdown values |
| `gold/artifacts/snapshots/aua_by_architect.json` | AUA snapshot by architect |
| `gold/artifacts/snapshots/aua_by_tax_status.json` | AUA snapshot by tax status |
| `gold/artifacts/snapshots/aua_by_state.json` | AUA snapshot by state |
| `gold/artifacts/snapshots/aua_by_region.json` | AUA snapshot by region |
| `gold/artifacts/advisor_rolling_flows.json` | Rolling NNA flows by advisor |
| `gold/views/nna_aua_by_geography.parquet` | NNA/AUA by geography (consumed by D_01) |
| `gold/views/nna_aua_by_geography_city.parquet` | NNA/AUA by city |
| `gold/views/nna_aua_by_advisor.parquet` | NNA/AUA by advisor (consumed by D_01) |

### D_01 partner_analytics

| | |
|---|---|
| **Script** | `D_01.partner_analytics.py` |
| **Reads** | C_02 `client_performance.parquet`, C_03 `account_performance.parquet`, A_00, A_04, C_07, C_01, D_00 `nna_aua_by_geography.parquet` + `nna_aua_by_advisor.parquet` |
| **Writes** | |

| S3 Key | Description |
|--------|-------------|
| `gold/artifacts/partner_analytics/header_metrics_quarterly.json` | QTD partner metrics |
| `gold/artifacts/partner_analytics/header_metrics_monthly.json` | MTD partner metrics |
| `gold/artifacts/partner_analytics/header_metrics_annual.json` | YTD partner metrics |

### D_02 advisor_client_detail

| | |
|---|---|
| **Script** | `D_02.advisor_client_detail.py` |
| **Reads** | C_03 `account_performance.parquet`, C_05 `client_tax_liability.parquet`, A_04 `client_dimension.parquet`, B_01 `holdings_lots/{date}.parquet`, C_07 `rel_architect_lookup.parquet` + `account_team.parquet`, C_08 `advisor_fee_detail/{date}.parquet`, A_02 `fee_rate_history.parquet` |
| **Writes** | |

| S3 Key | Count | Description |
|--------|-------|-------------|
| `gold/artifacts/implementor_leaderboard.json` | 1 | Implementor leaderboard |
| `gold/entities/advisors/{id}/book.json` | ~20 | Per-advisor book (client list) |
| `gold/entities/advisors/{id}/timeseries.json` | ~20 | Per-advisor AUA timeseries |
| `gold/entities/advisors/{id}/mix_timeseries.json` | ~20 | Per-advisor mix timeseries |
| `gold/entities/clients/{rel_id}/detail.json` | ~3,500 | Per-client detail |
| `gold/entities/clients/{rel_id}/aua_timeseries.json` | ~600 | Per-relationship AUA timeseries |
| `gold/entities/accounts/{acct_id}/aua_timeseries.json` | ~3,500 | Per-account AUA timeseries |

### D_03 composition_artifacts

| | |
|---|---|
| **Script** | `D_03.composition_artifacts.py` |
| **Reads** | B_01 `holdings_lots/{date}.parquet`, C_07 `rel_architect_lookup.parquet`, A_04 `client_dimension.parquet`, C_02 `client_performance.parquet`, C_03 `account_performance.parquet`, A_03 `positions_cube/{date}.parquet` |
| **Writes** | |

| S3 Key | Count | Description |
|--------|-------|-------------|
| `gold/views/firm_composition.json` | 1 | Firm-level composition |
| `gold/artifacts/firm_mix_views.json` | 1 | Firm mix views (period) |
| `gold/artifacts/firm_mix_views_daily.json` | 1 | Firm mix views (daily) |
| `gold/entities/advisors/{id}/composition.json` | ~20 | Per-advisor composition |
| `gold/entities/advisors/{id}/mix.json` | ~20 | Per-advisor mix views |
| `gold/entities/advisors/{id}/mix_daily.json` | ~20 | Per-advisor daily mix |
| `gold/entities/advisors/{id}/mix_timeseries.json` | ~20 | Per-advisor mix timeseries |
| `gold/entities/clients/{rel_id}_composition.json` | ~3,500 | Per-client composition |
| `gold/views/mix_daily_summary.json` | 1 | Summary mix daily |

---

## Dependency Graph (text DAG)

```
silver ---+---> A_00 ---+---> A_01 -----------------> C_08
          |             |---> A_04 -------> D_00, D_01, D_02, D_03
          |             |---> B_00, B_01, B_02, C_00, C_01, C_02, C_03, C_05, C_06, D_00, D_01
          |
          +---> A_02 ---+---> C_08, D_02
          |
          +---> A_03 ---+---> B_00, C_06, D_03
          |
          +---> B_00 ---+---> B_02 ---+---> B_03 ---+---> C_00 ---> C_02
          |             |             |             |---> C_01 ---> C_02, C_08, D_00, D_01
          |             |             |             |---> C_03 ---> C_06, C_07, D_01, D_02, D_03
          |             +---> C_05 ---+---> D_00, D_02
          |
          +---> B_01 ---+---> D_00, D_02, D_03
          |
          +---> C_02 ---+---> C_04 (validation)
          |             |---> D_00, D_01, D_03
          |
          +---> C_07 ---+---> C_08, D_00, D_02, D_03
          |
          +---> C_08 ---+---> D_00, D_02
          |
          +---> D_00 ---+---> D_01 (reads geo/adv views)
```

---

## Files Modified

None -- reference documentation only.

---

## Current State

Reference log. No code changes.
