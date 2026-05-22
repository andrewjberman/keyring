# YALP_MDSRC.C2 WS-1 — Live Validation (Andrew directive 2026-05-22)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — C2 WS-1 (0.1.0_DS) |
| By | `0.1.0_DS_MarketIntelligence` |
| Date | 2026-05-22 |
| Directive | Andrew 2026-05-22 (via COO): validate the C2 WS-1 choices against the live Menachem YCharts session NOW — do not defer as post-dedicated-seat first-live-run. |
| Session | the Menachem ("mchm") YCharts session, `ycharts/credentials` secret (single-session — staggered with 0.2.0_DS's WS-2 validation) |
| Audience | `2.0.0_SA_COO` (RAVC) |

---

## 1. Scope

Two checks against the live YCharts internal API, run via the C2 `YChartsClient`
(this doubled as the first live integration test of the C2 shared client):
1. **Per-symbol resolution** — every one of the 71 WS-1 ticker-map YCharts
   symbols returns a clean live daily series.
2. **WS1-VAL-01 columns** — does `indices/table_data` serve the valuation
   multiples (P/E, P/B, ...) for index entities (the A3 P3 UNVERIFIED-COLS item).

## 2. Check 1 — 71-symbol resolution: 67/71 first pass -> 71/71 after fix

First pass: **67 of 71 symbols PASS** — HTTP 200, clean daily series (e.g.
`^SPX` 19,226 pts, `^DJI` 24,221, `^MSEAFE` 14,314, `^BBUSATR` 7,549). **4
FAILED** HTTP 400: the S&P GSCI commodity sub-indices — Copper `^SG3J`, Crude
Oil Brent `^BCOB`, Natural Gas `^SG8A`, Silver `^SGSA`.

**Root cause — a yc_kind mis-classification, not a bad symbol.** The 4 symbols
are correct (YCharts search confirms `^SG3J` = "S&P GSCI Copper", `^BCOB` = "The
Brent Crude Oil Benchmark Index", etc.). They were tagged `yc_kind=security` in
the pull-spec / ticker map, so the pull used `fund_data(calc=price)` — the
securities calc. They are **indices** (`^`-prefixed S&P GSCI sub-indices) and
need `calc=level`. Re-probed with `calc=level`: **all 4 return HTTP 200** —
`^SG3J` 3,888 pts, `^BCOB` 3,480, `^SG8A` 3,891, `^SGSA` 3,891. (Contrast: Gold
`GOLD` and Crude Oil WTI `WTI` are genuine plain-ticker securities — they pass
on `calc=price`; the `^`-prefixed GSCI sub-indices do not.)

**Fixed** — `yc_kind` `security -> index` + the calc `price -> level` for the 4
commodity rows in: the C2 pull-spec, the finalized ticker-map CSV, and the
bundled `ticker_map.py` (regenerated). **Net result: 71/71 WS-1 ticker-map
symbols resolve to a clean live YCharts series.** The 4 V1A/V1B
representative-index picks (`^BBUTB13MTR`, `^BBUSCOHYTR`, `^BBUTISTR`,
`^BBUSLGCRTR`) are among the 67 first-pass passes — confirmed clean live.

## 3. Check 2 — WS1-VAL-01 valuation multiples: UNRESOLVED (endpoint-discovery finding)

`indices/table_data` was probed for the 6 VAL-01 valuation columns. Findings:
- The endpoint itself is healthy — `ytd_total_return` resolves (`^SPX` 9.27),
  multi-index works.
- Valuation column names split: some are **accepted but return EMPTY for index
  entities** (`pe_ratio` -> HTTP 200, `{}`; `forward_pe_ratio` -> 200, `{}`);
  others are **invalid -> HTTP 404** (`pe_ratio_forward`, `price_to_earnings`).
  A multi-column request including an invalid name 404s the whole call.

**Finding: YCharts index entities do not serve fundamental valuation ratios via
`indices/table_data`** — the column is accepted but the value is empty for an
index. WS1-VAL-01's pull path is **UNRESOLVED**; it needs YCharts
index-fundamental endpoint discovery (a HAR of the YCharts index valuation
page). This is the **same class** as 0.2.0_DS's WS-2 finding — `^SPX` does not
serve `forward_pe_ratio` for the ERP surface. Together: **index fundamentals
(P/E, P/B, forward-P/E) need a distinct YCharts endpoint, not
`indices/table_data` or `general_data`.** Carried to the joint C2 RAVC2 as a
post-validation discovery item (it does not block the freeze-aware build — the
ws1_surface_pull `pull_valuation_multiples` is wired; the endpoint/columns are
the open piece).

## 4. C2 client — live integration confirmed

The validation ran entirely through the C2 `YChartsClient`. Auth (the
`ycharts/credentials` secret), `freshness_probe`, `fund_data`,
`indices_table_data`, `search`, and the `parse_chart_series` parser all worked
live against the Menachem session — the C2 shared client is live-validated, not
only structurally validated.

## 5. Outcome + handoff

- 71/71 WS-1 ticker-map symbols resolve live (after the 4-commodity yc_kind fix).
- WS1-VAL-01 valuation-multiples endpoint UNRESOLVED — joint-RAVC2 discovery item.
- Fixes committed: pull-spec + ticker-map CSV + `ticker_map.py` (4 commodity rows).
- Probe artifacts (gitignored): `.runtmp/c2_ws1_validation_result.json`,
  `c2_ws1_validation_followup_result.json`, `c2_val01_probe_result.json`.
- The joint C2 RAVC2 (0.1.0_DS + 0.2.0_DS) folds this in alongside the WS-2
  validation results; AC3 (model_portfolio_* / TO-B1 seam) flagged open.

## 6. VAL-01 disposition — COO ruling 2026-05-22

The Check-2 finding was carried to a definitive per-multiple discovery and a COO
ruling. **WS1-VAL-01 is a HYBRID surface:**
- `pe_ratio` — MIGRATES to YCharts: indicator entities `I:SP500PNM` (trailing) /
  `I:SP500PND` (estimate/forward), pulled via `fund_data` `calc=id:level`.
- `pb_ratio`, `ps_ratio`, `price_to_free_cash_flow`, `ev_to_sales`,
  `dividend_yield` — **STAY Bloomberg-pkl-sourced.** They have no YCharts
  indicator entity (robust negative, multi-phrasing search). COO ruling: the
  project's hybrid migration model keeps hard-to-migrate surfaces on the pkl
  rather than chasing a fragile multi-component discovery — these 5 are not
  migrated.

Folded into `ws1_surface_pull.py` — `VAL01_PE_INDICATORS` (the migrated leg) +
`VAL01_STAYS_PKL` (the 5 pkl-retained multiples); `pull_valuation_multiples`
pulls only the YCharts `pe_ratio` leg. The index-fundamental discovery item is
closed — ERP forward-P/E and VAL-01 both definitively resolved.
