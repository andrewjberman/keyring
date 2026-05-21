# BRIEF: YCharts Granularity + Depth Verification — full index + ETF sweep (TO scoping)

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence
**Audience:** 2.0.0_SA_COO — to draft a proper TO. CC 1.0.0_SA_CTO.
**Trigger:** Andrew direct, 2026-05-21 — "It's not enough to look at the S&P alone; we need to explore every index and every ETF tracked on the portal."
**References:** A3 brief `docs/briefs/mdsrc-ycharts-internal-api-20260520.md` + the P3 mapping `mdsrc-ycharts-internal-api-mapping-20260520.tsv`; the 71-row crosswalk `mdsrc-ycharts-ticker-map-20260520.csv`; PRD `docs/architecture/YALP_MDSRC.md`.

---

## 1. The gap this TO closes

A3 reverse-engineered the YCharts internal API and established, per portal requirement: **which endpoint** serves it, **what params**, **what JSON path** to the value, and the **response schema**. A3 did **not** establish — systematically, per entity — the two properties that decide whether a YCharts pull can actually *replace* the Bloomberg `data_pkl` feed for a given surface:

- **Granularity** — the finest time resolution the endpoint actually returns for that entity (daily / trading-day / weekly / monthly).
- **Depth** — how far back the history goes.

A single spot-probe was run (Andrew's question, 2026-05-21): for **S&P 500** (`^SPX`), `fund_data.json` returned ~76 years of history, and a date-bounded request returned clean **daily** (trading-day) granularity — far exceeding the portal's ~6-year daily DynamoDB backbone. **Encouraging — but n=1.** It does not establish that the same holds for the other ~63 indices, the bond indices, the commodities, or the ETFs. Granularity and depth genuinely vary by entity: older / smaller / foreign / bond / commodity series, and ETFs, can have shorter history or coarser native granularity, and the daily-vs-weekly auto-resample boundary can sit at a different point per entity.

**This TO: verify granularity + depth for EVERY index and EVERY ETF the portal tracks — not a sample.**

---

## 2. Proposed scope — the entity universe

| Class | Count | Source of the list |
|---|---|---|
| **Indices** (equity + style/factor + country) | 53 | DynamoDB `opal-portal-market-data` `entity_type=INDEX` |
| **Bond indices** | 11 | DynamoDB `entity_type=BOND_INDEX` |
| **ETFs** | ~5 (confirm exact set) | `json/benchmarks/etf_returns.json` / the yang ETF-benchmark set (WS2-MP-04). The TO's first step enumerates the exact ETF list. |
| **Commodities** | 7 | DynamoDB `entity_type=COMMODITY` |

Andrew's directive names "every index and every ETF" — the **64 indices + the ETF set** are the firm core. **Scoping note for the COO/Andrew:** the 7 commodities face the identical granularity/depth question and excluding them would leave a market-data gap — recommend folding them in, but flag it as a one-line scope confirmation rather than silently expanding. Total universe ~78–83 entities; the exact ETF count is the TO's first deliverable.

---

## 3. What "verify" means — the per-entity checks

For each entity, pull its actual time series from the YCharts internal API and record:

1. **Finest granularity obtainable** — date-bound the request and confirm whether daily (trading-day) data returns; note the inter-point spacing.
2. **History depth** — earliest available data point; total span in years.
3. **The daily-vs-resample boundary** — at what range/`maxPoints` the endpoint stops returning daily and auto-resamples to weekly/monthly (so C2 knows how to bound its pulls).
4. **Requirement-match verdict** — does the obtainable granularity + depth MEET the portal surface that consumes this entity? The portal needs ~6 years of **daily** prices for the DynamoDB backbone (Market Overview, Correlation, ticker timeseries); **monthly** series for the Valuation `time_series` and risk-premium surfaces. Verdict per entity: `meets` / `partial` (e.g. daily-but-shallow, or deep-but-only-weekly) / `gap`.
5. **Endpoint note** — `fund_data.json` (date-bounded) is the reliable time-series endpoint; `general_data.json` returned empty for the `metric=price` time-series combo in the A3 probe — the TO should also nail the correct `general_data.json` time-series invocation or confirm `fund_data.json` is the canonical series endpoint for C2.

---

## 4. Method

- Drive the YCharts internal API (`fund_data.json` date-bounded for series; `table_data` for snapshot) with the live authenticated session — same mechanism as A3.
- Resolve each entity to its YCharts symbol via the dc01d4b8a 71-row crosswalk **with the A2/A3 corrections applied** — critically the MSCI-country LOC-variant fix (`^MS**L`) and the bond plain-USD symbols. A wrong-variant symbol would granularity-check the wrong series.
- Single capture seat (the F1 single-concurrent-session constraint) — one DS runs the sweep; measured request rate.

---

## 5. Proposed deliverable

- A committed **per-entity granularity/depth matrix** (machine-readable table) — one row per index / bond index / ETF (/ commodity): `entity, yc_symbol, finest_granularity, history_depth_years, earliest_date, resample_boundary, portal_requirement, verdict`.
- A brief summarizing: how many entities `meet` vs `partial` vs `gap`, the entity-classes that systematically differ (if any), and the C2 implications (how to bound pulls; any entity that cannot be daily-sourced from YCharts and therefore stays Bloomberg-pkl).
- Feeds **TO-C2** directly as a pre-build input.

---

## 6. Dependencies / risks / open items (for the TO author)

- **Symbol-resolution dependency:** 5 entities are still genuinely-unmapped from A3-P4 (Silver, Brent, Natural Gas, Copper, MSCI USA Size) — granularity cannot be checked for an entity whose YCharts symbol is unresolved. The TO must either sequence the YCharts securities-search symbol-resolution first, or scope those 5 as "blocked-pending-symbol."
- **Entity-class variation is the whole point** — equity indices likely behave like `^SPX`; bond indices, country indices, and commodities may not. The TO should expect and document per-class differences.
- **F1 single-session** — the sweep needs the YCharts seat; coordinate so it does not collide with C1's credential-pipeline work or any other YCharts-seat consumer.
- **Effort:** ~78–83 entities, one series pull + analysis each — an investigation TO, estimate ~1–2 effort-days.
- **Owner:** recommend `0.1.0_DS_MarketIntelligence` — holds the A3 internal-API context, the crosswalk, and the granularity-probe method already.

---

## 7. Suggested acceptance criteria (to seed the TO)

- AC1 — every portal index + ETF (+ commodities if confirmed in scope) enumerated and probed; none skipped.
- AC2 — per entity: finest granularity, history depth, resample boundary recorded from a live pull.
- AC3 — per entity: a `meets / partial / gap` verdict against the consuming portal surface's granularity+depth requirement.
- AC4 — any entity that YCharts cannot serve at the required granularity/depth explicitly flagged (it stays Bloomberg-pkl — a real migration-scope finding).
- AC5 — committed machine-readable matrix + brief; RAVC2 to COO + CC CTO; feeds TO-C2.
