# ADVI_49PUSH.033 -- Distribution P2 Continuous Data

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-09
**Project:** ADVI_49PUSH
**Commit:** dbb1d105
**Status:** COMPLETE (Issues 1 + 3 implemented; Issue 2 flagged for D_00 follow-on).

---

## Prerequisites satisfied

- .027 step_0 geo_coverage_decision = OPTION A (accounts, 99.97%). Applied to P2.
- `geo_aua_grain: 'accounts'` added to both partner_analytics JSON (.027) and cumulative_chart.json (.033).

---

## Issue 1: new_clients_by_period -- COMPLETE

D_04 `build_cumulative_chart` now reads `client_dimension.parquet` (CLIENT_DIMENSION key) and aggregates `first_seen_date` to period grain:

```json
new_clients_by_period: {
  quarterly: [{"period": "2026-Q1", "label": "Q1 '26", "count": N}, ...],
  monthly:   [{"period": "2026-01", "label": "Jan '26", "count": N}, ...],
  annually:  [{"period": "2026",    "label": "2026",    "count": N}, ...]
}
```

Frontend sums count within the active time window (QTD/YTD/1Y/ALL) to derive window total.

---

## Issue 2: nna_geo_drill (city-level NNA continuous) -- FLAGGED

**Status:** Not implementable in D_04 alone. D_00 does not produce city-level NNA timeseries in `timeseries_chart.json`.

D_04's drill passthrough already handles `nna_geo_drill` (line in `for drill_key in ('geo_drill', 'adv_drill', 'nna_geo_drill'):`). When D_00 adds city-level NNA columns, they will automatically flow through D_04 to cumulative_chart.json.

**Required D_00 change:** Add city-level NNA drill to D_00's Y9 section — new `_nna_city_drill_data` function that groups canonical NNA by (city, date) using `accounts_dimension.client_city` join, outputs `nna_geo_drill: {state_key: {categories: [city1, city2, ...], data: [{date, city1, city1_inflow, city1_outflow, ...}]}}`. Apply Top 9+Other per state. This is a D_00 task for a follow-on session.

---

## Issue 3: nna_adv_drill (advisor-level NNA continuous) -- Level 1 COMPLETE, Level 2 DEFERRED

**Level 1 (per-advisor NNA series):** COMPLETE.

D_04 `build_cumulative_chart` extracts per-advisor NNA from `nna_adv.data` — each row already has advisor name as a column (from D_00 `_nna_drill_data`). Builds:

```json
nna_adv_drill: {
  "Travis Penfield": {
    "description": "Cumulative NNA for Travis Penfield",
    "categories": ["Travis Penfield"],
    "data": [{date, NNA, Inflows, Outflows}, ...]  // weekly-downsampled
  },
  ...
}
```

Skips 'Other' and 'Unresolved' pseudo-advisors.

**Level 2 (client NNA within advisor): DEFERRED.**

Per-client NNA timeseries data does not exist in `timeseries_chart.json`. The `adv_drill` has per-client AUA timeseries, but there is no equivalent for NNA. Computing it would require joining canonical NNA parquet with client-to-advisor mapping at the client grain — a significant new computation in D_00. Flagged as a future enhancement for DE .036 to note.

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | `build_cumulative_chart`: Issue 1 (new_clients_by_period + geo_aua_grain), Issue 2 (flag comment), Issue 3 (nna_adv_drill Level 1) |

---

## Commits

| SHA | Description |
|---|---|
| `dbb1d105` | 0.4.0_DS_ClientPlatform: ADVI_49PUSH.033 Distribution P2 continuous data (D_04) |

---

## Acceptance Criteria Status

| Criterion | Status |
|---|---|
| 1. cumulative_chart.json has new_clients_by_period | DONE (after AE re-run) |
| 2. nna_geo_drill populated | NOT DONE -- requires D_00 enhancement (flagged) |
| 3. adv_drill populated (Level 1 AUA by advisor) | ALREADY EXISTED in timeseries_chart |
| 4. nna_adv_drill added | DONE -- Level 1 per-advisor series |
| 5. Client entries use pseudonymized names | N/A for Level 1; Level 2 deferred |
| 6. Level 2 status documented | DEFERRED -- no per-client NNA timeseries in D_00 output |
| 7. DE notified | DONE (MCP message) |

---

## Pending

1. **AE re-run D_04** -- Upload D_04.client_portal_summary.py to S3, re-run. cumulative_chart.json will include new fields.
2. **D_00 enhancement** -- Add city-level NNA drill to timeseries_chart.json (nna_geo_drill, flagged above).
3. **DE .034-.036** -- Companion frontend TOs unblocked after AE re-run.

## Next Steps

[AE 0.6.0] Upload D_04 to S3 and re-run. cumulative_chart.json will have new_clients_by_period, nna_adv_drill, geo_aua_grain.
[DE 0.4.0_DE] .034-.036: P2 continuous frontend wiring. Note nna_geo_drill (city-level NNA) not yet available -- D_00 follow-on required before city drill is live.
