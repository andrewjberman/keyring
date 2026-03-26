# ADVI_GLDRST Session Log -- Canonical Methodology + Pre-Computed Views
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_GLDRST (Gold Layer Restructure)

---

## Summary

Two workstreams converged today:

1. **Canonical exclusion unification** (this session): created `lib/exclusions.py`, applied ghost account exclusion to scripts 05b, 06b, 12. All gold scripts now apply the same account universe.

2. **DE finding (0.4.0_DE_ClientPlatform)**: quarterly mix views are pre-computed only at firm level (N1). L2 and L3 derive quarterly snapshots client-side from daily timeseries — fragile, wasteful, and methodologically inconsistent. See `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-03-26/advi_mvplvl_010_l2_composition_mix_session.md`.

These are the same problem viewed from different angles. The exclusion unification ensures **what goes into the views** is consistent. The pre-compute expansion ensures **how the views are served** is consistent.

---

## Current State: What Exists vs. What's Needed

### Pre-Computed Mix Views

| Level | Artifact | Exists? | Script | Schema | Notes |
|-------|----------|---------|--------|--------|-------|
| N1 Firm | `gold/firm_mix_views.json` | YES | 06b | `{views: {quarterly, monthly, annually}}` | Canonical. 24Q, 69M, 7A periods. |
| L2 Advisor | `gold/advisors/{id}/mix.json` | YES | 06b | Same as N1 with `advisor_id`, `advisor_name` | 25KB per advisor, full history. |
| L2 Advisor | `gold/advisors/{id}/mix_timeseries.json` | YES (alias) | 06b (today's fix) | Same file as mix.json | Lambda reads this key. |
| L3 Relationship | `gold/client_timeseries/{id}_views.json` | NO | -- | -- | Does not exist. Portal derives from daily JSON (~50KB per relationship). |
| L4 Account | `gold/accounts/{id}/mix_views.json` | NO | -- | -- | Does not exist. No account-level timeseries at all. |

### Pre-Computed Composition (Asset Mix + Top Holdings)

| Level | Artifact | Exists? | Script | Notes |
|-------|----------|---------|--------|-------|
| N1 Firm | `gold/views/firm_composition.json` | YES | 12 | Static S3 artifact via CloudFront. |
| L2 Advisor | `gold/advisors/{id}/composition.json` | YES | 12 | 20 advisors. DE rerouted through CloudFront today (commit `a56fcf1`). |
| L3 Relationship | -- | NO | Lambda `handle_books_composition` computes on-the-fly | Reads holdings_lots live. Expensive (~3s Lambda). |
| L4 Account | -- | NO | Lambda `handle_books_composition` computes on-the-fly | Same as L3. |

### Pre-Computed AUA Timeseries (for quarterly bar)

| Level | Artifact | Exists? | Script | Notes |
|-------|----------|---------|--------|-------|
| N1 Firm | `gold/timeseries_chart.json` | YES | bd-portal-publisher Lambda | Stacked by architect. |
| L2 Advisor | `gold/advisors/{id}/timeseries.json` | YES | bd-portal-advisor-publisher Lambda | Daily AUA per advisor. |
| L3 Relationship | `gold/client_timeseries/{id}.json` | YES | 06b | Daily mix + concentration. ~50KB per relationship. |
| L4 Account | -- | NO | -- | -- |

---

## DE's Recommendation (Agreed)

All quarterly mix views should be pre-computed by script 06b at all levels using the same methodology:

```
gold/firm_mix_views.json                              # N1 -- already exists
gold/advisors/{advisor_id}/mix.json                   # L2 -- already exists
gold/client_timeseries/{relationship_id}_views.json   # L3 -- NEEDS CREATION
gold/accounts/{account_id}/mix_views.json             # L4 -- future
```

Same schema everywhere:
```json
{
  "views": {
    "quarterly": [{period, label, end_date, total_aua, equity, fixed_income, alternatives, cash, other}],
    "monthly":   [...],
    "annually":  [...]
  }
}
```

This eliminates `deriveQuarterlyFromTimeseries()` from the portal entirely.

---

## GLDRST Implications for Script 06b

Script 06b already produces N1 and L2 quarterly views. Extending to L3 requires:

### What 06b already does for L3:
- Processes positions_cube per date
- Resolves account_id -> relationship_id via accounts_dimension
- Classifies holdings via ETFClassifier
- Writes `gold/client_timeseries/{relationship_id}.json` with daily mix + concentration

### What's missing for L3 quarterly views:
- After writing the daily JSON, 06b needs to call `compute_period_views()` (which already exists and produces the quarterly/monthly/annually structure) scoped to each relationship
- Write `gold/client_timeseries/{relationship_id}_views.json` alongside the daily file
- This is a ~20-line addition to `_write_relationship_json()` in 06b

### Exclusion alignment (completed today):
- 06b now applies ghost exclusion via `lib/exclusions.py` (commit `ae3403f5`)
- 06b already applies AP gate with insurance override
- L3 views will inherit the full canonical exclusion stack automatically

### Sizing estimate:
- ~1,400 relationships currently
- Each `_views.json` is ~5-10KB (same as advisor mix.json)
- Total S3 footprint: ~10-15MB additional
- Compute: negligible — `compute_period_views()` runs in <10ms per relationship

---

## GLDRST Implications for Script 12

Script 12 already pre-computes firm and advisor composition. Extending to L3/L4 means the Lambda `handle_books_composition` can be replaced by static S3 artifacts, eliminating the ~3s Lambda compute per request.

### What's needed:
- After building firm + advisor composition, iterate over relationships (group by relationship_id instead of architect)
- Write `gold/client_timeseries/{relationship_id}_composition.json`
- Same schema as firm_composition.json scoped to one relationship

### Trade-offs:
- **Pro:** Eliminates Lambda cold-start + holdings_lots read per request
- **Pro:** Composition uses the same exclusion stack as everything else
- **Con:** ~1,400 additional S3 objects per gold run
- **Con:** L3 composition needs relationship_id on holdings_lots (currently only has account_id; needs accounts_dimension join)

### Recommendation: Phase this after L3 mix views (lower complexity, higher impact).

---

## Today's Commits (GLDRST Canonical Methodology)

| Commit | Description |
|--------|-------------|
| `9bca5ff6` | mix_timeseries.json alias + script 06 ghost exclusion |
| `38faa34f` | lib/exclusions.py creation + dedup scripts 05+06 |
| `df5e8004` | Script 05b ghost exclusion (primary $7.4M fix) |
| `ae3403f5` | Scripts 06b+12 ghost + shared insurance AP gate |
| `16c3139e` | DFAC classified as equity / US Small Cap / active |

---

## Cross-Reference: DE Fixes Today

From `0.4.0_DE_ClientPlatform/logs/2026-03-26/advi_mvplvl_010_l2_composition_mix_session.md`:

| DE Commit | What it fixed | DS dependency |
|-----------|---------------|---------------|
| `a56fcf1` | L2 composition routed through CloudFront | Script 12 composition.json must exist (confirmed: 20 advisors) |
| `865ab7d` | Mix chart cash+other merge | Script 06b firm_mix_views.json outputs both `cash` and `other` fields (confirmed) |
| `5e921e6` | Mix chart wired to Window toggle | firm_mix_views.json has full history (confirmed: 24Q, 69M, 7A) |
| `decd651` | Exclude current quarter from quarterly bar | Requires correct quarter-end dates in views (confirmed) |

---

## Next Steps

| Priority | Owner | Action |
|----------|-------|--------|
| P1 | AE | Full gold rerun to apply ghost exclusion to all parquets + populate mix_timeseries.json aliases |
| P2 | DS | Extend script 06b to write L3 `{relationship_id}_views.json` (quarterly/monthly/annually) |
| P2 | DE | Wire L2 `mix.json` to quarterly bar via advisor mix-views CloudFront endpoint (portal-only) |
| P3 | DS | Extend script 12 to write L3 `{relationship_id}_composition.json` (eliminate Lambda compute) |
| P3 | DE | Replace `deriveQuarterlyFromTimeseries()` with L3 _views.json artifact reads |
| Future | DS | L4 account-level mix views + composition artifacts |
