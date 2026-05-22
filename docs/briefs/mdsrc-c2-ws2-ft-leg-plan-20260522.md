# YALP_MDSRC.C2 — WS-2 FT-02/03 Factor-Spread Leg Plan

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.3 §7 Phase 2C |
| Task Order | `YALP_MDSRC.C2` — co-owned (WS-2 = 0.2.0_DS) |
| Author | `0.2.0_DS_PortfolioAnalytics` (WS-2 co-owner) |
| Date | 2026-05-22 |
| Scope | FT-02/03 (factor-spread) — the LAST WS-2 leg per the COO GO sequencing |
| Build spec | `mdsrc-c5-factor-pair-constituents-20260521.md` §3 + §0 — RATIFIED by Andrew 2026-05-22 (commit 2c2d8aab6) |
| Freeze status | FREEZE-AWARE — built + structurally validated; NO live YCharts until the dedicated seat lands |

---

## 1. What FT-02/03 needs

The generator `yang-generate-factor-tilts` drives FT-02 (`tier2-spreads.json`) and FT-03 (`tier3-timeseries.json`) from the `factor_spread` DataFrame in `model.pkl` — 6 named columns, daily, `.tail(504)` trading days. C3 Finding 2 established `factor_spread` is **pre-computed in Yang's manual build** — the generator does not expose the constituent index per leg.

C5 closed that gap: it proposed, and Andrew ratified (2026-05-22), the constituent index for each of the 12 legs. This module re-sources FT-02/03 by pulling the constituents and computing the 6 spreads itself — replacing the pre-computed `model.pkl/factor_spread`. Opal's downstream factor-tilt rendering is unchanged.

## 2. The 6 ratified factor pairs (C5 §3 + §0)

Spread convention: `spread = return(leg A) − return(leg B)`, daily.

| Factor name (matches generator `FACTOR_NAMES`) | Leg A | Leg B |
|---|---|---|
| `Equity vs FI` | MSCI ACWI (`MXWD Index`) | Bloomberg Aggregate (`LBUSTRUU Index`) |
| `Growth vs Value` | Russell 1000 Growth (`RLG Index`) | Russell 1000 Value (`RLV Index`) |
| `US vs Foreign` | MSCI USA (`MXUS Index`) | MSCI ACWI ex US (`MXWDU Index`) |
| `Large vs Small` | Russell 1000 (`RIY Index`) | Russell 2000 (`RTY Index`) |
| `Agg vs Short` | Bloomberg Aggregate (`LBUSTRUU Index`) | Bloomberg 1-3 Year Gov/Credit (`LGC3TRUU Index`) |
| `HY vs Agg` | Bloomberg High Yield (`LF98TRUU Index`) | Bloomberg Aggregate (`LBUSTRUU Index`) |

Andrew's two flagged-leg calls (C5 §0): `Agg vs Short` SHORT = Bloomberg 1-3Y Gov/Credit (clean duration-only spread, Gov+Credit on both legs); `Equity vs FI` EQUITY = MSCI ACWI (matches the model-benchmark equity component, not S&P 500).

**10 distinct constituent indices** (Bloomberg Aggregate is reused across 3 pairs): MSCI ACWI, Bloomberg Aggregate, Russell 1000 Growth, Russell 1000 Value, MSCI USA, MSCI ACWI ex US, Russell 1000, Russell 2000, Bloomberg High Yield, Bloomberg 1-3 Year Gov/Credit. (The C5 §0 "9 distinct" line is a miscount — §4 lists 10; this module pulls 10.)

## 3. Build approach

- Pull each of the 10 constituents' daily total-return series via `client.fund_data(yc_symbol, calc="level")` → `daily_returns_from_levels` (reused from `ws2_mp_benchmark_pull` — same index-level→daily-return logic as the MP index legs).
- `compute_factor_spreads`: for each pair, `spread_t = return(A)_t − return(B)_t` on dates present in BOTH legs (a partial date is dropped, not partially computed).
- Emit the 6 named spread series — the shape the generator currently reads pre-computed from `model.pkl/factor_spread`.
- Symbol map INJECTED from the WS-1 71-entity ticker map (every C5 constituent resolves to a real dc01d4b8a crosswalk row per C5 §2) — this module does not duplicate the crosswalk.

Module: `infra/aws/lambda/ycharts-market-data-pull/ws2_factor_tilts_pull.py`. Freeze-aware — `structural_self_test()` validates the 6-pair / 10-constituent wiring + the spread arithmetic with synthetic data, no network.

## 4. Open items

| # | Item | Plan |
|---|---|---|
| FT-O1 | YCharts symbols for the 10 constituents | From the WS-1 ticker map (injected). MSCI ACWI = `^MSACWI`, Bloomberg Aggregate = `^BBUSATR` known; the other 8 resolve via the crosswalk / A3 mapping. Per-symbol fidelity check at first live run. |
| FT-O2 | Bloomberg 1-3 Year Gov/Credit YCharts symbol | A3 P4 resolved `^BBUGCR13YT` ("1-3 Year Gov/Credit") — distinct from the correlation TR2 1-3yr *Treasury* gap; here Gov/Credit IS the ratified pick (Andrew's call), so `^BBUGCR13YT` is correct, no conflation. |

## 5. Coordination

- Build spec = the C5 ratified packet. FT-02/03 is the last WS-2 module section — on landing, WS-2 is 4/4 complete.
- RAVC2 the C2 WS-2 side to COO on FT-02/03 landing; coordinate the final C2 close with 0.1.0_DS (WS-1). No CC CTO per Andrew.
