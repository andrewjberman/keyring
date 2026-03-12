# DIVZ / IDVZ Architect Exposure Query — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-11
**Start Time:** session start
**End Time:** session end

## Objective

Identify which architects are tagged to relationships currently holding DIVZ or IDVZ,
and rank those architects by how much of their AUA is concentrated in those positions.
Ad-hoc query for Andrew — no task order issued.

---

## Work Completed

### 1. Data Sources Loaded

| Source | Key | Records |
|--------|-----|---------|
| Canonical prices | `silver/prices/canonical_prices.parquet` | 10,299,877 rows |
| Positions cube (latest) | `gold/positions_cube/2026-03-09.parquet` | 119,197 positions |
| Accounts dimension | `gold/accounts_dimension_latest.parquet` | 9,706 accounts |
| NNA/AUA by advisor | `gold/views/nna_aua_by_advisor.parquet` | latest date 2026-03-09 |

### 2. Ticker Mapping

- **DIVZ** maps to asset_name `EVENTIDE HIGH DIVIDEND ETF`, latest price $37.79 (as of 2026-03-09)
- **IDVZ** — 0 rows in canonical_prices. No clients hold IDVZ. Not in our price universe.

### 3. Results — Architects Ranked by DIVZ/IDVZ AUA

Positions as of **2026-03-09**.

| Rank | Architect     | DIVZ+IDVZ AUA | Total AUA     | % DIVZ+IDVZ | Relationships | Accounts |
|------|---------------|--------------|---------------|-------------|---------------|----------|
| 1    | 49F House     | $1,409,804   | $692,291,870  | 0.20%       | 12            | 19       |
| 2    | Kyle Sims     | $120,871     | $91,376,785   | 0.13%       | 3             | 5        |

**Total firm DIVZ+IDVZ AUA:** $1,530,675
**Firm-level concentration:** 0.10% of total AUA

All exposure is DIVZ only (Eventide High Dividend ETF). IDVZ has zero positions.

### 4. Key Observations

- **49F House** is the unassigned/house bucket — relationships not attributed to a named architect.
  12 relationships holding DIVZ under this bucket is notable and may indicate unassigned
  advisor attribution for these accounts.
- **Kyle Sims** has 3 relationships / 5 accounts holding DIVZ at a similar concentration rate (0.13%).
- Concentration is very low for both architects (<0.25%) — not a material risk position.
- IDVZ is entirely absent from the firm's holdings universe as of 2026-03-09.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Used nna_aua_by_advisor for total AUA denominator | Already computed and available; accurate as of same date as positions cube |
| Used 2026-03-09 positions cube (latest available) | Most recent partition; positions data lags by 1 business day |
| Modal architect at relationship level | Consistent with how 08_build_nna_aua_by_advisor.py assigns advisor per household |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tmp_divz_idvz_by_architect.py` | Ad-hoc analysis script (temp, gitignored) | No — temp only |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Query complete. Two architects hold DIVZ: 49F House ($1.41M, 12 rels) and Kyle Sims ($120K, 3 rels).
IDVZ is not in the firm's holdings universe. Results surfaced directly to Andrew.

---

## Next Steps

No downstream handoffs required. Ad-hoc query, results delivered.

**Do NOT:**
- Commit the `.tmp_divz_idvz_by_architect.py` script — it's an ephemeral diagnostic
