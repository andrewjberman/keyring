# D_04 Spec: Books Tab Portal Publisher (Platinum Layer)

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Status:** Design -- pending Andrew approval

---

## Purpose

D_04 is the canonical publisher for the Books tab drill hierarchy. It reads gold-layer
analytical outputs (C_06, C_07, C_08, D_00, D_02, D_03) and writes lightweight,
portal-ready JSON artifacts to `platinum/`. The portal reads ONLY from `platinum/` --
no direct reads of `gold/` files.

This establishes the rule: **`gold/` = analytical layer, `platinum/` = portal-serving layer.**

---

## Problem

Today the Books tab fires multiple fetches per drill level, several of which pull
full analytical datasets just to extract a small summary:

| Level | Current Fetches | Problem |
|-------|----------------|---------|
| N1 (Firm) | `getEmployeeLeaderboard`, `getClientsTab`, `getFirmMixViews`, `getAdvisorFeeEfficiency` | 4 fetches on tab open, reads from scattered gold/ paths |
| L2 (Advisor) | `getAdvisorBook`, `getAdvisorMixViews`, `getBooksAdvisorComposition` | 3 fetches, composition comes from D_03 gold/ path |
| L3 (Client) | `getBooksClientDetail`, `getRelationshipCompositionStatic`, `getRelationshipMixViews`, `getBooksRelationshipTimeseries` | 4 fetches; `_views.json` is C_06 (gold/ leak); timeseries pulls full history just to sum 90 days |
| L4 (Account) | `getBooksAccountComposition` | Lambda reads full parquet |

---

## Current Fetch Map (what fires today)

### N1 -- Firm Dashboard (on tab open)

| Fetch | Source File | Script | Layer |
|-------|-----------|--------|-------|
| `getEmployeeLeaderboard()` | `gold/artifacts/employee_leaderboard.json` | D_00 | gold |
| `getClientsTab()` | `gold/artifacts/clients_tab.json` | D_00 | gold |
| `getFirmMixViews()` | `gold/artifacts/firm_mix_views.json` | D_03 | gold |
| `getAdvisorFeeEfficiency()` | `gold/artifacts/advisor_fee_efficiency.json` | C_08 | gold |
| `getBooksFirmComposition()` | `gold/views/firm_composition.json` (Lambda) | D_03 | gold |

### L2 -- Advisor Book (on advisor select)

| Fetch | Source File | Script | Layer |
|-------|-----------|--------|-------|
| `getAdvisorBook()` | `gold/entities/advisors/{id}/book.json` | D_02 | gold |
| `getAdvisorMixViews()` | `gold/entities/advisors/{id}/mix.json` (Lambda) | D_03 | gold |
| `getBooksAdvisorComposition()` | `gold/entities/advisors/{id}/composition.json` (Lambda) | D_03 | gold |

### L3 -- Client Relationship (on client select)

| Fetch | Source File | Script | Layer |
|-------|-----------|--------|-------|
| `getBooksClientDetail()` | `gold/entities/clients/{id}/detail.json` | D_02 | gold |
| `getRelationshipCompositionStatic()` | `gold/entities/clients/{id}_composition.json` | D_03 | gold |
| `getRelationshipMixViews()` | `gold/entities/clients/{id}_views.json` | C_06 | **gold (C leak)** |
| `getBooksRelationshipTimeseries()` | `gold/entities/clients/{id}/aua_timeseries.json` | D_02 | gold |

### L4 -- Account (on account select)

| Fetch | Source File | Script | Layer |
|-------|-----------|--------|-------|
| `getBooksAccountComposition()` | Lambda reads full parquet | opal-partners-data | gold |

---

## Target Fetch Map (D_04 output)

### N1 -- Firm Dashboard

| Fetch | Platinum File | Contents |
|-------|-------------|----------|
| `getFirmDashboard()` | `platinum/firm/dashboard.json` | employee leaderboard, clients tab headline, fee efficiency scorecard |
| `getFirmMixSummary()` | `platinum/firm/mix_summary.json` | latest mix snapshot, quarterly bars (5 periods), composition (mix pie + concentration pie + top holdings) |

### L2 -- Advisor Book

| Fetch | Platinum File | Contents |
|-------|-------------|----------|
| `getAdvisorSummary()` | `platinum/advisors/{id}/summary.json` | book (client list, AUA, NNA), mix snapshot, quarterly bars (5 periods), composition, top holdings |

### L3 -- Client Relationship

| Fetch | Platinum File | Contents |
|-------|-------------|----------|
| `getClientSummary()` | `platinum/clients/{rel_id}/summary.json` | detail (accounts, AUA, tax lots, gains), mix snapshot, quarterly bars (5 periods), composition, top holdings, 90d decomposition (market_growth, nna, synthetic_correction) |

### L4 -- Account

| Fetch | Platinum File | Contents |
|-------|-------------|----------|
| `getAccountSummary()` | `platinum/accounts/{acct_id}/summary.json` | composition (mix pie + top holdings) |

---

## Platinum File Schemas

### `platinum/firm/dashboard.json`

```json
{
  "data_as_of": "2026-04-07",
  "generated_at": "2026-04-08T02:15:00Z",
  "headline": {
    "total_aua": 1250000000,
    "client_count": 612,
    "account_count": 3487
  },
  "employee_leaderboard": { ... },
  "clients_tab": { ... },
  "fee_efficiency": { ... }
}
```

Note: This may stay as separate files if the combined payload is too large.
The key point is they all live under `platinum/firm/`.

### `platinum/firm/mix_summary.json`

```json
{
  "data_as_of": "2026-04-07",
  "mix": {
    "equity": {"market_value": 900000000, "pct": 0.72},
    "fixed_income": {"market_value": 300000000, "pct": 0.24},
    "alternatives": {"market_value": 25000000, "pct": 0.02},
    "cash": {"market_value": 25000000, "pct": 0.02}
  },
  "mix_periods": [
    {"period": "2026-Q1", "equity": 0.71, "fixed_income": 0.24, "alternatives": 0.03, "cash": 0.02},
    {"period": "2025-Q4", "equity": 0.70, ...},
    {"period": "2025-Q3", ...},
    {"period": "2025-Q2", ...},
    {"period": "2025-Q1", ...}
  ],
  "concentration": {
    "top_n": 10,
    "items": [
      {"ticker": "IVV", "asset_name": "iShares Core S&P 500", "asset_class": "equity",
       "market_value": 85000000, "pct": 0.068}
    ],
    "other": {"market_value": 200000000, "pct": 0.16}
  }
}
```

### `platinum/advisors/{id}/summary.json`

```json
{
  "advisor_id": "ADV001",
  "data_as_of": "2026-04-07",
  "book": {
    "client_count": 45,
    "account_count": 210,
    "total_aua": 180000000,
    "nna_qtd": 2500000,
    "nna_ytd": 8000000,
    "clients": [
      {"relationship_id": "z08327149", "name": "Smith Family", "aua": 4200000, "nna_ytd": 150000},
      ...
    ]
  },
  "mix": {
    "equity": {"market_value": 130000000, "pct": 0.72},
    "fixed_income": {"market_value": 43000000, "pct": 0.24},
    "alternatives": {"market_value": 3600000, "pct": 0.02},
    "cash": {"market_value": 3400000, "pct": 0.02}
  },
  "mix_periods": [
    {"period": "2026-Q1", "equity": 0.73, "fixed_income": 0.23, ...},
    ...
  ],
  "concentration": {
    "top_n": 10,
    "items": [...],
    "other": {"market_value": ..., "pct": ...}
  }
}
```

### `platinum/clients/{rel_id}/summary.json`

```json
{
  "relationship_id": "z08327149",
  "data_as_of": "2026-04-07",
  "detail": {
    "name": "Smith Family",
    "total_aua": 4200000,
    "accounts": [
      {"account_id": "ABC123", "account_name": "Joint Brokerage", "aua": 2100000,
       "tax_status": "taxable", "account_type": "Individual"},
      ...
    ],
    "tax": {
      "taxable": 2100000, "taxable_pct": 0.50,
      "tax_deferred": 1500000, "tax_deferred_pct": 0.357,
      "tax_free": 600000, "tax_free_pct": 0.143,
      "capital_gains_ttm": 35000,
      "cost_basis_by_year": [...],
      "top_gain_positions": [...]
    }
  },
  "mix": {
    "equity": {"market_value": 3024000, "pct": 0.72},
    "fixed_income": {"market_value": 1008000, "pct": 0.24},
    "alternatives": {"market_value": 84000, "pct": 0.02},
    "cash": {"market_value": 84000, "pct": 0.02}
  },
  "mix_periods": [
    {"period": "2026-Q1", "equity": 0.73, ...},
    ...
  ],
  "concentration": {
    "top_n": 10,
    "items": [...],
    "other": {"market_value": ..., "pct": ...}
  },
  "decomposition_90d": {
    "market_growth": 42150.00,
    "nna": -12300.00,
    "synthetic_correction": 800.00
  }
}
```

### `platinum/accounts/{acct_id}/summary.json`

```json
{
  "account_id": "ABC123",
  "data_as_of": "2026-04-07",
  "mix": {
    "equity": {"market_value": 1512000, "pct": 0.72},
    "fixed_income": {"market_value": 504000, "pct": 0.24},
    "alternatives": {"market_value": 42000, "pct": 0.02},
    "cash": {"market_value": 42000, "pct": 0.02}
  },
  "concentration": {
    "top_n": 10,
    "items": [...],
    "other": {"market_value": ..., "pct": ...}
  }
}
```

---

## D_04 Input/Output Summary

### Reads (all from gold/)

| Source | Script | Used For |
|--------|--------|----------|
| `gold/artifacts/employee_leaderboard.json` | D_00 | Firm dashboard |
| `gold/artifacts/clients_tab.json` | D_00 | Firm dashboard headline + client list |
| `gold/artifacts/advisor_fee_efficiency.json` | C_08 | Firm dashboard fee scatter |
| `gold/artifacts/firm_mix_views.json` | D_03 | Firm mix periods |
| `gold/views/firm_composition.json` | D_03 | Firm mix snapshot + concentration |
| `gold/entities/advisors/{id}/book.json` | D_02 | Advisor book |
| `gold/entities/advisors/{id}/mix.json` | D_03 | Advisor mix periods |
| `gold/entities/advisors/{id}/composition.json` | D_03 | Advisor mix snapshot + concentration |
| `gold/entities/clients/{rel_id}/detail.json` | D_02 | Client detail (accounts, tax, gains) |
| `gold/entities/clients/{rel_id}_composition.json` | D_03 | Client mix snapshot + concentration |
| `gold/entities/clients/{rel_id}_views.json` | C_06 | Client mix periods (quarterly bars) |
| `gold/entities/clients/{rel_id}/aua_timeseries.json` | D_02 | Client 90d decomposition |
| `gold/entities/accounts/{acct_id}/aua_timeseries.json` | D_02 | Account (not used yet, placeholder) |
| `gold/timeseries/holdings_lots/{date}.parquet` | B_01 | Account composition (if pre-computing L4) |

### Writes (all to platinum/)

| File | Count | Approx Size |
|------|-------|-------------|
| `platinum/firm/dashboard.json` | 1 | ~50-100KB |
| `platinum/firm/mix_summary.json` | 1 | ~5KB |
| `platinum/advisors/{id}/summary.json` | ~20 | ~10-20KB each |
| `platinum/clients/{rel_id}/summary.json` | ~600 | ~2-5KB each |
| `platinum/accounts/{acct_id}/summary.json` | ~3,500 | ~1-2KB each |

---

## Execution

- **Position in chain:** After D_03, as the final script in the downstream chain
- **Chain update:** `CHAIN_DOWNSTREAM="C_03 C_05 C_07 C_06 C_08 D_00 D_01 D_02 D_03 D_04"`
- **Catalog entry:** `D_04|D_04.client_portal_summary.py|--upload`
- **Concurrency:** ThreadPoolExecutor for S3 writes (~4,100 files, small JSONs)
- **Idempotent:** Yes, safe to re-run. Overwrites all platinum/ files.

---

## Portal Migration (separate effort, after D_04)

Once D_04 is deployed and writing to `platinum/`, the portal migration is:

1. Update `shared-advisor-router` Lambda@Edge to rewrite to `platinum/` for Books tab paths
2. Update `opal-partners-data` Lambda to read from `platinum/` for Books routes
3. Update frontend API calls to point at new platinum paths
4. Remove fallback paths that read from `gold/`
5. Migrate remaining D_00/D_01 non-Books artifacts to `platinum/` (Asset Overview, Partner Analytics -- separate D_05+ scripts or expansion of D_04)

---

## What Stays in gold/ (unchanged)

- All Group A/B/C parquet outputs (analytical layer)
- C_06 full timeseries envelopes (`gold/entities/clients/{rel_id}.json`) -- kept for future use
- All `gold/canonical/`, `gold/timeseries/`, `gold/dimensions/`, `gold/views/` parquets
- D_00/D_01/D_02/D_03 continue writing to `gold/` as before -- D_04 reads their output

---

## Open Questions

1. **N1 dashboard.json size** -- Employee leaderboard + full clients_tab + fee efficiency may exceed 200KB combined. Should these stay as separate platinum files (`platinum/firm/dashboard.json`, `platinum/firm/leaderboard.json`, `platinum/firm/clients_tab.json`, `platinum/firm/fee_efficiency.json`) or merge into one?

2. **L4 account composition** -- Currently computed by Lambda from full `holdings_lots` parquet. D_04 can pre-compute `platinum/accounts/{acct_id}/summary.json` (~3,500 files) from the same parquet. Worth doing now or defer?

3. **Advisor book client list** -- The `book.json` client list can be large for advisors with 50+ clients. Keep full list in advisor summary or paginate?
