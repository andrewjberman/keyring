# Session Log -- 0.4.0_DS_ClientPlatform~C -- 2026-04-28

**Lane:** ~C (challenger / parallel-build lane)
**Project:** ADVI_INFSHIP P1.L3
**Session span:** ~03:35Z -- ~04:05Z
**TO:** GO via COO MCP 20260428T040000Z (no .md TO file; PRD §4 row L3 is the spec)

---

## Summary

Shipped INF_D_04 changes for ADVI_INFSHIP Phase 1 Lane L3:

1. **Geo-aware partner_analytics emitter** -- `views.geo.donut.segments[].cities[]` populated end-to-end with top 8 states + Other; cities[] nested per state; distribution.by_segment per-state percentile stats; distribution.total cohort-level. Validated against reference data: $199.4M total / 308 HH / 852 accts / WA-dominant 86.1% (matches silver $200M, COO brief WA-dominant claim).

2. **MAX-window TWR-based market component** -- new `growth_decomposition_max_twr` block in `timeseries_overview.json` computing `Sigma beginning_mv * cumulative_return` per account where `cumulative_return = (1 + twr_value)^window_years - 1`. Per-period (quarterly/monthly/annual) growth_decomposition retained as residual subtraction -- per-period TWR not yet pulled from ORIAPI (single annualized 3Y TWR per account in current pull).

3. **3-tier silver/bronze fallback chain** for `silver/api_dims/{household,performance,activity}/` -- code activates automatically when DS~A's L2 schema lands; falls back to bronze CSV for AE's L5 raw drops; falls back to empty stub when neither exists. No code change needed when silver lands.

---

## Work Item: INF_D_04 changes

### File modified
`data/orion/scripts/gold/INF_D_04.client_portal_summary.py` (+547 / -9)

### New helpers
| Function | Purpose |
|---|---|
| `load_household_dim()` | 3-tier load: silver `api_dims/household/` parquet -> bronze CSV -> empty. Snake_case column normalization. |
| `load_performance_dim()` | 3-tier load: silver `api_dims/performance/` -> bronze CSV (parses `12.85 %` -> 0.1285, currency strings -> floats). |
| `load_activity_dim()` | 3-tier load: silver `api_dims/activity/` -> bronze CSV (parses Beginning MV / Ending MV / Contributions / etc). |
| `_build_geo_view(holdings, household_dim)` | Builds `views.geo` PartnerAnalyticsView: top 8 states + Other, cities[] per state, distribution.by_segment, distribution.total. Inflection-scope rep_id filter (defense-in-depth). |
| `_compute_max_twr_market(performance_dim, activity_dim)` | Per-account MAX-window TWR cumulative return -> firm-level market component $; reconciliation against residual (ending_mv - beginning_mv - net_flows) included for sanity check. |

### Wiring
- `build_partner_analytics()` signature gained `household_dim` parameter; `geo_view = _build_geo_view(holdings, household_dim)` replaces the empty stub at the call site.
- `build_timeseries_overview()` signature gained `performance_dim, activity_dim`; emits `growth_decomposition_max_twr` block when both dims load successfully (None when either empty -- portal ignores unknown keys).
- `main()` loads all 3 new dims early and passes through.

### Critical data-source decision (per DS~A 03:44Z)
- `holdings.market_value` is the SOLE source of $-truth for per-account AUA (silver $200M-aligned, matches Andrew's ~$191M Inflection-only figure with rep_id=3 + $8M margin from rep_id=11/12).
- `household_dim` provides STATE / CITY ONLY -- never the $-amount. The $140M vs $200M divergence DS~A surfaced is pull-config (geo_verify.csv's Activity.Value with wrong activityOptionId, not Ending MV).
- TWR$ recompute joins performance_dim (twr_value) + activity_dim (beginning_mv) on `(account_id, snapshot_date)` -- DS~A's recommended pattern.

### Per-period TWR data gap (deferred scope)
- Current ORIAPI pull: ONE annualized "Rolling 3-Year" TWR per account (Performance.Value).
- Per-period (quarterly/monthly/annual TWR) requires multi-pull pattern: separate ORIAPI query per period x per account with parametrized DateRange. Out of scope for P1.L3.
- Documented in `_compute_max_twr_market.note` field of the JSON output. P1.L3-followup TO needed (DS~B / AE pull-spec; then ~C or ~A consumes for `_build_growth_periods` rewrite).
- For v1: per-period growth_decomposition stays residual; MAX-window TWR ships alongside as additive intelligence.

---

## Validation (local mock run)

Test driver: `/tmp/test_geo_view.py`
Inputs:
- `data/orion/manual_api/pulls/20260428_geo_verify.csv` (state/city)
- `data/orion/manual_api/pulls/20260428_unified_account_dim.csv` (Ending MV per ~A)
- Filtered to Inflection rep_id IN {3, 11, 12} per ADVI_INFGRD silver scope

Output (from `_build_geo_view()` direct call):
```
donut.total: $199,440,829
donut.segments: 9 segments (8 top + Other)
   WA | $171,723,526 | 86.1% | 264 HH | 744 accts | 10 cities
   MT | $  8,472,627 |  4.2% |   4 HH |  13 accts |  3 cities
   CA | $  4,444,985 |  2.2% |   6 HH |  17 accts |  6 cities
   IN | $  3,151,317 |  1.6% |   1 HH |   8 accts |  1 cities
   MN | $  2,315,400 |  1.2% |   4 HH |   8 accts |  2 cities
   AZ | $  2,002,331 |  1.0% |   6 HH |   9 accts |  5 cities
   IL | $  1,805,727 |  0.9% |   5 HH |   7 accts |  5 cities
   TX | $  1,765,939 |  0.9% |   2 HH |  13 accts |  2 cities
OTHER | $  3,758,977 |  1.9% |  16 HH |  33 accts |  0 cities

Top WA cities (drill):
  Everett    | $37.8M | 22.0% | 48 HH
  Snohomish  | $26.7M | 15.5% | 38 HH
  Seattle    | $15.7M |  9.2% | 31 HH
  Mill Creek | $11.9M |  7.0% | 10 HH
  Arlington  | $ 8.3M |  4.9% | 10 HH
```

Distribution.total: count=308 HH | sum=$199.4M | mean=$234K | p50=$86K | p75=$252K | max=$3.08M

Assertions passed:
- total > 0
- segments >= 1, every segment has cities[]
- segments <= 9 (top 8 + Other)
- $100M < total < $250M (silver-aligned, not the $140M Activity.Value pitfall)
- segment_aua sum == donut.total (no rounding drift)
- Top state == WA (matches COO brief "WA-dominant 85.9%"; my 86.1% reflects $200M denominator vs brief's $140M)

Note: state '34' in the geo_verify.csv (looks like raw data anomaly, possibly empty StateCode mis-cast). Lands in OTHER bucket (low AUA). Not a v1 blocker; could add 2-letter US-state validation in a hardening pass.

---

## Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| Pre-edit | `comp-pipescript io D_04` | Confirmed `partner_analytics_{*}.json` + `timeseries_overview.json` consumed by `PartnerAnalytics`, `DistributionTab` components. Both targets PRD-spec'd. |
| Pre-commit | `.tools/ds-commit-gate.sh data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | OK: pre-commit gate clean (py_compile + AST undefined-name + ruff all green) |
| Local validation | `python /tmp/test_geo_view.py` | All assertions PASS; output shape matches INFLEC_PORTAL_FIELD_USAGE.md §5 panel #5 spec |

---

## RAVCs Sent

| When | To | Subject |
|------|----|---------|
| 03:38Z | 2.0.0_SA_COO | RAVC2 ACK -- ADVI_INFSHIP P1.L3 starting now |
| 03:44Z | 0.4.0_DS_ClientPlatform~A | Q -- silver/api_dims/{household,performance}/ status |
| 03:51Z | 2.0.0_SA_COO | PROGRESS -- Geo emitter going; GRO TWR data gap, propose scope split |
| 03:51Z | 0.4.0_DS_ClientPlatform~A | RAVC2 ACK -- schema noted, coding against your spec |
| ~04:05Z | 2.0.0_SA_COO + DE 0.4.0 | RAVC4 -- INF_D_04 P1.L3 SHIP (this log) |

---

## Pending / Next

| Item | State | Owner |
|------|-------|-------|
| Push commit to CLOUD | Next step | ~C |
| `aws s3 cp INF_D_04.client_portal_summary.py s3://opal-data-inf/code/gold/` | Next step | ~C |
| Run INF_D_04 on inf-gold-runner against real silver data | After silver/api_dims/* lands | DS~A signal -> ~C dispatch |
| Validate views.geo populated end-to-end in real platinum/firm/partner_analytics_*.json | After live run | ~C |
| Per-period TWR pull spec (P1.L3-followup) | Future TO | DS~B / AE / ~C consumer |
| RAVC4 COO + DE B1 (PartnerAnalytics nested schema migration) | After live run validation | ~C |

---

## Cross-domain coordination

- **DS~A (P1.L2):** silver/api_dims/{household,performance,activity}/ schema designed; ETA ~2-4h. Will MCP ~C when each dim lands. ~C's INF_D_04 reads silver-first, falls back to bronze CSV (same column naming via rename_map), falls back to empty stub. No code change needed when silver lands.
- **AE 0.6.1~B (P1.L5):** bronze/orion-api/{date}/{dim}.csv layout for raw API drops. INF_D_04's bronze fallback assumes flat CSV at `bronze/orion-api/household/latest.csv` etc. If AE's layout differs, ~C will adjust the BRONZE_API_*_LATEST keys.
- **DE 0.4.0 (B1):** PartnerAnalytics nested schema migration consumes `views.geo.{period}.donut.segments[].cities[]`. Once INF_D_04 emits real geo data, RAVC4 to DE B1 with sample artifact path.

---

## Risk / open questions

1. **State code dirty values:** `'34'` appears as a state_code in geo_verify (1 HH). Could indicate raw data carrying empty StateCode mis-cast or genuine territory code. Lands in OTHER bucket, not a v1 blocker. Hardening: add 2-letter US-state validation pass.
2. **TWR cumulative-return assumption:** `(1 + twr_value)^window_years - 1` assumes annualized geometric compounding. Holds for Performance.AnnualizedMethod = "Annualized" (current pull). If non-annualized TWR is pulled in future, formula needs adjustment.
3. **Per-account TWR coverage:** Per ~A's note, only 22% of Inflection accounts have populated cost basis -- TWR coverage may be similar. Need to verify TWR populates for all 852 accounts in real silver run, not just the cost-basis-populated subset.
