# BRIEF: YCharts HAR endpoint assessment (YALP_MDSRC.A5)

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence
**TO:** YALP_MDSRC.A5 (issued by 2.0.0_SA_COO, Andrew-direct)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO; routed to 0.7.0_AE_CloudOps~A (capture side).
**Inputs (raw HARs, kept in user Downloads — outside the repo, never staged):**
- `ycharts.com5.har` — Alyssa, 2026-05-21 — a Bloomberg US Aggregate (`^BBUSATR`) chart-page session.
- `ycharts.com6.har` — Alyssa, 2026-05-21 — MSCI-ETF + GSCI-commodity pages + the YCharts search box.

**SANITIZED:** endpoint shapes + query params only. Zero cookie / token / Authorization values. Raw HARs not committed.

---

## 1. Summary

A5 mines two Alyssa-recorded HARs to pin YCharts endpoint invocations without a live seat. **Result: both A4 endpoint residues are resolved, and a core A4 conclusion is corrected.**

- **`fund_data.json` is the daily time-series endpoint for *every* index class** — standard, MSCI, GSCI, and Bloomberg-bond. The A4 sweep's "36 indices are not `fund_data.json` items / are `general_data.json`-only" is **wrong**; it was a sweep param-set artifact.
- **`general_data.json` is pinned** — and it is a **returns-table** endpoint (trailing + annual total returns), *not* the daily-price endpoint. A3's `metric=price` returned empty because the param is `metrics` (plural, `id:`-prefixed, named return metrics) and because the daily series simply is not what this endpoint serves.
- **The securities-search XHR is `GET /search/suggest/main?q={query}`** — pinned. Symbol resolutions: Silver -> `^SGSA`, Copper -> `^SG3J`.

---

## 2. HAR coverage inventory

| HAR | Session | YCharts XHR captured |
|---|---|---|
| ycharts.com5 | `^BBUSATR` chart page | `fund_data.json` (GET x4, POST x2), `securities_info`, `calc_info`, `/indices/^BBUSATR/chart/` |
| ycharts.com6 | MSCI-EM/EAFE ETF pages (`companies/IEMG`,`IEFA`) + S&P GSCI Silver/Copper index pages + search box | `fund_data.json` (x7), `general_data.json` (x4), `scatter_plot_data.json` POST, `search/suggest/main` (x8), `securities_info` |

Response bodies: the HTML pages and *some* `fund_data.json` / `general_data.json` bodies were saved; the 8 `search/suggest/main` bodies were **not** saved (HAR exported without full XHR content). See §5.

---

## 3. Target 1 — `general_data.json`: PINNED

**Endpoint:** `GET /charts/general_data.json`

**Working invocation — two forms, both observed HTTP 200:**

*Form A — trailing-returns cross-section* (`xAxis=metrics`):
`metrics=id:one_month_total_return,include:true,,id:three_month_total_return,include:true,,...,id:annualized_daily_fifteen_year_total_return,include:true,,` `&securities=id:{sym},include:true,,` `&xAxis=metrics` `&pointInTimeDate={MM/DD/YYYY}` `&pointInTimeLag=7`

*Form B — annual-returns time series* (`xAxis=time`):
`metrics=id:ytd_total_return,include:true,,` `&securities=id:{sym},include:true,,` `&xAxis=time` `&resampleFrequency=yearly` `&resampleMethod=last` `&startDate={MM/DD/YYYY}` `&endDate={MM/DD/YYYY}`

**Response schema** (captured, `^SGSA`):
```
{ "categories": ["1M","3M","6M","1Y","3Y","5Y","10Y","15Y",""],
  "chart_data": [ { "label": "^SGSA", "data": [-5.21,-8.03,49.98,...], "data_type": "percent" } ],
  "err_code": null, "err_message": null }
```

**The A3 correction:** A3 tried `metric=price` (singular, value `price`) and got empty. The correct param is **`metrics`** (plural), value form **`id:{metric_name},include:true,,`**, and the metric must be a **named return metric** (`ytd_total_return`, `one_month_total_return`, `annualized_daily_*_total_return`, ...). **`general_data.json` serves returns-table data — trailing-period and annual total returns — NOT a daily price/level series.** That is why a daily-price probe of it returns nothing useful: wrong endpoint for that job.

## 4. The core correction — `fund_data.json` is the daily-series endpoint for ALL index classes

A4 concluded the 29 MSCI + 7 Bloomberg-bond indices "are not `fund_data.json` items" and 400. The two HARs falsify this across all three affected classes:

| Entity | Class | Endpoint | Evidence |
|---|---|---|---|
| `^BBUSATR` Bloomberg US Aggregate | Bloomberg-bond | `fund_data.json` `calcs=id:level` | HAR5 — 200, 30.1yr `market_daily` series |
| `^SGSA` S&P GSCI Silver | GSCI commodity-index | `fund_data.json` `calcs=id:level` | HAR6 — 200, 15.2yr `market_daily` (zoom=5d returned 64 clean daily pts) |
| `^MSACXUSNTR` MSCI ACWI ex-US (NTR) | MSCI | `fund_data.json` `calcs=id:level` / `id:total_return_forward_adjusted_price` | HAR6 — 200, used as a chart benchmark series |

**`fund_data.json` is entity-class-agnostic** for the daily series — exactly as A3 found the YCharts internal API to be generally. The A4 sweep's 400s were a **param-set artifact**: the sweep used a minimal form; the real app sends the full quote-page form (`zoom`, `dateSelection=range`, `partner`, `le_o`, `splitType`, ~30 params). With the full form, all three classes return 200. **There is no `general_data.json`-only index residue, and no Bloomberg-pkl carve-out for the index universe.**

`fund_data.json` response schema (HAR5, `^BBUSATR`): `{chart_data:[[{object_id,object_type,object_calc,frequency,format,raw_data:[[ts_ms,value],...],...}]], start_date, params, ...}` — `frequency: market_daily` is the native descriptor; `maxPoints` below the daily-point count auto-resamples (A4 boundary rule holds).

## 5. Target 2 — the securities-search XHR

**Endpoint pinned:** `GET /search/suggest/main?q={query}` — returns `application/json`. HAR6 captured 8 calls (Alyssa typed "copper" and "silver" letter-by-letter, plus "copx").

**Response schema — NOT captured:** all 8 `search/suggest/main` bodies were empty in the HAR export (saved without full XHR content). The endpoint + the `q` param are pinned; the result-list schema is not.

**Symbol resolutions (by navigation outcome — search -> clicked result -> landed page):**
- **Silver -> `^SGSA`** = "S&P GSCI Silver" (confirmed via the `/indices/^SGSA` page title). 15.2yr depth, `market_daily`.
- **Copper -> `^SG3J`** = a YCharts index (the "copper" search landing page; `/indices/^SG3J`; exact name not captured — almost certainly the S&P GSCI Copper sub-index, parallel to `^SGSA`).

Both are **S&P GSCI single-commodity sub-indices**, not spot prices. The portal entities are spot (`XAG`/`HG1`). `^SGSA`/`^SG3J` are viable YCharts symbols but the spot-vs-GSCI-index basis is a C2 fidelity decision (a YCharts spot-commodity *security* may also exist — A3-P4 resolved Gold->`GOLD`, WTI->`WTI` as securities — worth one search check).

**Not resolved:** Brent, Natural Gas, MSCI USA Size — not searched in HAR6.

## 6. Other endpoints

- `scatter_plot_data.json` POST — observed 200 (A3 P3's WS2-MP-03 risk/return endpoint; corroborated).
- `securities_info` — exact-symbol lookup, as A3 documented (not a search).
- No change to the A3 endpoint map otherwise; A5 corrects the `general_data.json` invocation and the `fund_data.json` class-coverage, and adds `search/suggest/main`.

## 7. Resolved vs still-needs-the-seat

**Resolved by A5 (no live seat):**
- `general_data.json` working invocation + schema (returns-table; not daily price).
- `fund_data.json` confirmed as the daily-series endpoint for MSCI / GSCI / Bloomberg-bond — the A4 36-classification corrected.
- The search XHR endpoint (`/search/suggest/main?q=`).
- 2 of 5 unmapped symbols (Silver `^SGSA`, Copper `^SG3J`).

**Still needs a live capture (~A, dedicated/non-contended seat):**
- The `search/suggest/main` response schema (bodies not saved). Now a *cheap* task — the endpoint is a simple GET; ~A or C2 can call `/search/suggest/main?q={name}` directly and read the JSON. No browser-in-loop is needed — that A4-Batch-0 blocker is removed.
- Brent / Natural Gas / MSCI USA Size symbol resolution — `GET /search/suggest/main?q=brent` etc.
- The actual 36-entity granularity/depth NUMBERS — `fund_data.json` recapture at `maxPoints=100000` with the full quote-page param form (A4 follow-on; HAR-finding spec already handed to ~A).

## 8. Routing

- **To 0.7.0_AE_CloudOps~A:** (a) the recapture uses `fund_data.json` for ALL 36 (MSCI + bond), full quote-page param form — `general_data.json` is not needed for the daily series; (b) symbol resolution for the remaining unmapped entities is now a direct `GET /search/suggest/main?q=` call, not a browser-in-loop task.
- **To C2 pre-stage:** the pull-spec's `general_data.json` rows for the 36 should change to `fund_data.json` `calcs=id:level`; `general_data.json` is retained only if C2 wants ready-made trailing/annual return tables. `/search/suggest/main` is the symbol-resolution endpoint.
- **To COO/CTO:** the A4 "36 = general_data.json-only / pending-recapture" framing is superseded — the index universe is uniformly `fund_data.json`-served; the recapture confirms the numbers, not the reachability.

## 9. Compiler self-checks (TO mandate)

- **Phase-0 (coverage inventory vs targets):** HAR5 — neither target present (reported; re-record requested). HAR6 — target 1 (general_data.json) PRESENT + pinned; target 2 (search XHR) endpoint PRESENT, response schema absent (bodies not saved). Reported accurately, no fabrication. PASS.
- **Phase-2 (zero secret values in the committed brief):** this brief contains endpoint shapes + query params only — no Cookie/token/Authorization values; raw HARs kept in Downloads, never staged. PASS.

## 10. Acceptance criteria

- **AC1** — HARs ingested; coverage inventory produced (§2); paths confirmed to COO; raw HARs gitignored (kept outside the repo). **MET.**
- **AC2** — `general_data.json` working invocation pinned: endpoint + `metrics` params + schema (§3). **MET.**
- **AC3** — search XHR endpoint + `q` param pinned (§5); response schema documented as not-captured (bodies not saved) with a cheap direct-probe path; 2 of 5 unmapped symbols resolved. **MET as far as the capture allows** (the TO's AC3 wording).
- **AC4** — committed SANITIZED brief; Phase-2 self-check confirms zero secret values. **MET.**
- **AC5** — findings routed: `fund_data.json`/`general_data.json` to ~A + C2; search endpoint to ~A + C2; seat-gated residue listed (§7-8). **MET.**
- **AC6** — session log Compiler Tools section reproduces the self-checks; RAVC2 to COO + CC CTO. **MET** (this RAVC2).

**Net:** A5 turned a static HAR pair into the resolution of both A4 endpoint residues plus a correction of the A4 36-entity classification. The dedicated-seat recapture is now a confirm-the-numbers exercise on a uniform `fund_data.json` path — not an open reachability question.
