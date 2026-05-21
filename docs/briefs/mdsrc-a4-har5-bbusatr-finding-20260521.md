# FINDING: ycharts.com5.har contradicts the A4 "36 not fund_data.json items" conclusion

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence
**Audience:** Andrew (HAR provided direct); 2.0.0_SA_COO; CC 1.0.0_SA_CTO; 0.7.0_AE_CloudOps~A (capture side).
**Input:** `C:\Users\AndrewBerman\Downloads\ycharts.com5.har` — recorded by Alyssa, 2026-05-21 (60 MB, 248 entries). It is a single browsing session on the **Bloomberg US Aggregate** index chart page.

---

## 1. The finding

A4 concluded that all 36 MSCI + Bloomberg-bond indices return `fund_data.json` HTTP 400 *"no valid items"* — "not `fund_data.json` items" — and are served only by `general_data.json` (which 403'd). `ycharts.com5.har` **directly contradicts that for `^BBUSATR`** (Bloomberg US Aggregate — one of the 7 Bloomberg-bond indices, A4-classified in the 36, `verdict = pending-recapture`).

The HAR shows the `/indices/^BBUSATR/chart/` page driving **`/charts/fund_data.json`** — and it returns **HTTP 200** with a real series:

| Call | Params | Result |
|---|---|---|
| GET `fund_data.json` | `securities=id:^BBUSATR`, `calcs=id:level`, `zoom=5d/1m/3m`, `maxPoints=673` | 200, JSON |
| POST `fund_data.json` | `securities=id:^BBUSATR`, `calcs=id:level`, `zoom=3m/max`, `maxPoints=782/791` | 200, full `chart_data` |

Extracted from the POST `zoom=max` response (`maxPoints=791`):
- `object_id: ^BBUSATR`, `object_type: index`, `object_calc: level`, **`frequency: market_daily`**.
- 784 data points, **1996-04-29 -> 2026-05-20 = 30.1 years**.
- The returned series is spaced ~14 days (resampled): `maxPoints=791` is far below the native daily-point count (~7,500 for 30yr), so the endpoint auto-resampled — exactly the A4 maxPoints-boundary rule. The entity's *native* frequency is `market_daily`.

So `^BBUSATR` **is** a `fund_data.json` item, with **30 years of daily history** — reachable, deep, daily. It is not a `general_data.json`-only entity, and it is not unreachable.

## 2. Why the A4 sweep got 400 for it — hypothesis, not yet resolved

The A4 sweep (`~A`) and the HAR both call `fund_data.json` with **identical** `securities=id:^BBUSATR,include:true,,` and `calcs=id:level,include:true,,`. So the 400 *"no valid items"* is **not** a security/calc problem. The difference is the rest of the param set:

- **A4 sweep call:** minimal — `securities`, `calcs`, `format=real`, `chartType=interactive`, `maxPoints=100000`, `redesign=true`. No `zoom`, no date context, no quote-page params.
- **HAR working call:** the full quote-page param set — adds `zoom=`, `dateSelection=range`, `partner=basic_2000`, `le_o=quote_page_fund_data`, `splitType`, `scaleType`, and ~25 others; `maxPoints=673-791`.

Candidate causes (cannot be distinguished without a live session): (a) a **missing required param** for index-type entities — `zoom` / `dateSelection` / a date context — that securities/ETFs don't need but indices do; (b) a **disturbed-session artifact** — the A4 sweep ran while the session was being evicted (the F1 contention), and `fund_data.json` may have partially mis-behaved. The clean entity-class split A4 saw (all MSCI + all bonds) argues somewhat against a pure timing artifact and toward a param/class cause.

## 3. Scope of this finding — precise

This HAR proves the point for **`^BBUSATR` only** — 1 of the 7 Bloomberg-bond indices, 0 of the 29 MSCI indices. It does **not** prove the other 35 are reachable. What it **does** do is **falsify the blanket A4 claim** that "all 36 are not `fund_data.json` items / are `general_data.json`-only." At least one is a normal `fund_data.json` item; the blanket classification is unsafe.

## 4. Actions

1. **The recapture must re-test the 36 with the HAR's working param set** — the full quote-page `fund_data.json` form (POST, `zoom=max`, the complete param list), `maxPoints=100000` for native daily — before concluding any entity needs `general_data.json` or is unreachable. The A4 sweep's minimal param set is the prime suspect and must not be reused for the 36.
2. **The 7 Bloomberg-bond indices are now likely `fund_data.json`-reachable** (^BBUSATR demonstrates it). The recapture should try `fund_data.json` first for the bond subset, not assume `general_data.json`.
3. **`^BBUSATR` provisional verdict (HAR-measured):** access CONFIRMED, depth CONFIRMED 30.1yr, native frequency `market_daily`. Expected A4 verdict `meets`. The one item not yet measured is a native-daily point series (the HAR's was resampled at `maxPoints=791`) — one pull at `maxPoints>=8000` settles it. This is a real measurement, not a theory — distinct from the other 35, which remain genuinely untested.
4. **A4 matrix:** recommend `^BBUSATR` move from `pending-recapture` to a HAR-provisional `meets` on the recapture, and the 36-recapture's endpoint assumption be corrected (fund_data.json-first for bonds). Not unilaterally re-committing the A4 matrix on this single HAR data point — flagging for COO.

## 5. Net

Andrew's HAR-capture approach is working: one Alyssa-recorded chart-page session was enough to falsify a blanket A4 conclusion and recover a 30-year daily Bloomberg-bond series. The reachable universe is very likely **larger** than the A4 sweep's "31 of 67" — the sweep's minimal param set, not YCharts' coverage, is the probable limiter. The dedicated-seat recapture should be run with the HAR-derived param set; expect materially more than 31 to come back clean.
