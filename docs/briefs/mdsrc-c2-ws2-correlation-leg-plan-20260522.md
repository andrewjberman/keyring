# YALP_MDSRC.C2 — WS-2 Correlation Leg Plan (correlation input-series YCharts pull)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.3 §7 Phase 2C |
| Task Order | `YALP_MDSRC.C2` — co-owned (WS-2 = 0.2.0_DS) |
| Author | `0.2.0_DS_PortfolioAnalytics` (WS-2 co-owner) |
| Date | 2026-05-22 |
| Scope | The Correlation hybrid surface — 2nd WS-2 leg per the COO GO sequencing (after MP-01/02/03) |
| Build inputs | C3 input spec §3.1, A3 P3 mapping TSV (WS1-COR-01 + WS1-COR-TR1/2/3), V1B catalog scan, dc01d4b8a ticker map |
| Freeze status | FREEZE-AWARE — plan + module built/structurally-validated now; NO live YCharts until the dedicated seat lands |

---

## 1. What Correlation needs

The generator `yang-generate-correlation` (`infra/aws/lambda/v2_portal/yang_pipeline/correlation/yang-generate-correlation/lambda_function.py`) reads `data.pkl -> return_monthly`, filters `index_name` to a hard-coded **63-index** list (`MARKET_OVERVIEW_INDICES`, lines 34-74), reads the `return` column per index per month, and computes pairwise Pearson correlation matrices over 5 windows (1M/3M/6M/1Y/2Y = 21/63/126/252/504 monthly rows).

**Verified 2026-05-22:** the `MARKET_OVERVIEW_INDICES` list is exactly 63 entries — matches C3 §3.1. The C2 input is **63 monthly total-return series**. No ETF or per-security input (indices only).

The WS-2 re-source: pull each index's monthly return series from YCharts, hand the generator the same `return_monthly`-shaped input. Opal computation (the Pearson matrices) is unchanged — TO `do_not`.

## 2. The 63 series — 59 clean, 4 flagged (C3 §4 finding 1)

**59 of 63** map cleanly by `portal_name` to the dc01d4b8a crosswalk `bbg_ticker`; their YCharts symbols are A3-resolved (the WS1-COR-01 row — `/charts/general_data.json`, `metric=price`, `xAxis=time` per ticker; the generator pivots monthly). Endpoint call shape is identical to the MP index legs.

**4 flagged** — resolution status as of this plan:

| # | Correlation input | Resolution | Status |
|---|---|---|---|
| TR1 | `Bloomberg US Treasury` | `^BBUSTTR` — Bloomberg US Treasury, an **exact** match (V1B catalog scan §2, the broad Bloomberg US Treasury index). | RESOLVED |
| TR2 | `Bloomberg 1-3 Year Treasury` | **No pure-Treasury 1-3yr maturity band on YCharts** (V1B §2 verbatim: "no pure-Treasury intermediate/long maturity band"). The 1-3yr *Government/Credit* index `^BBUGCR13YT` exists but is a DIFFERENT index — it carries corporate credit; C3 §4 explicitly forbids that conflation. | OPEN — see §3 |
| TR3 | `Bloomberg 7-10 Year Treasury` | **No pure-Treasury 7-10yr maturity band on YCharts** (same V1B finding). | OPEN — see §3 |
| CO  | `Crude Oil` (generator uses the bare name) | Crosswalk carries Brent (`CO1 Comdty` -> `^BCOB`) AND WTI (`CL1 Comdty` -> `WTI`). The generator's `return_monthly` "Crude Oil" series is ONE of them. | OPEN — see §4 |

## 3. TR2 / TR3 — the two unresolved Treasury bands

V1B's catalog scan (75 Bloomberg fixed-income entities, 13 family queries incl. "Treasury") established that YCharts' Bloomberg Treasury catalog is exactly two indices: `^BBUSTTR` (broad US Treasury) and `^BBUTB13MTR` (1-3 Month T-Bills). There is **no Bloomberg pure-Treasury 1-3yr or 7-10yr maturity-band index on the platform** — the same structural finding V1A/V1B hit for the HY / TIPS / 20+yr bands.

Per Andrew's V1B ruling (representative-of-concept Bloomberg-origin index acceptable when the exact band is absent), the candidate resolutions:

- **TR2 `Bloomberg 1-3 Year Treasury`** — short-duration pure Treasury. No clean pick: `^BBUTB13MTR` (1-3 *month*) is far too short and is already the 0-1yr-band representative (MP UST leg); `^BBUGCR13YT` (1-3yr Gov/Credit) has the right duration but the wrong credit segment and is C3-§4-forbidden for this slot. **Recommendation:** a small post-unfreeze `client.search()` probe for any Bloomberg short-Treasury index V1B's family queries did not surface; if none, escalate to a methodology call (accept the duration proxy with a documented credit-contamination caveat, OR drop the index from the correlation universe).
- **TR3 `Bloomberg 7-10 Year Treasury`** — intermediate-long pure Treasury. No YCharts Bloomberg match. Same recommendation.

This is a **representative-index / methodology decision, not a build blocker** — correlation builds clean for 60/63 (the 59 + TR1); TR2/TR3 are 2 cells of a 63x63 matrix, deferrable behind a flagged decision. NOT silently mapping either to a Gov/Credit index (C3 §4 hard rule). Surfaced to COO for a methodology routing call.

## 4. CO — the Crude Oil variant

The generator's bare `Crude Oil` index_name resolves deterministically: Yang's `data.pkl` carries a `bbg_ticker` column (per the C2 TO `ticker_map` ref) giving every index its exact Bloomberg ticker. The `Crude Oil` row's `bbg_ticker` is either `CL1 Comdty` (WTI) or `CO1 Comdty` (Brent). **Resolution path:** read that column from `data.pkl` — a deterministic lookup, not a guess. Expectation: WTI (`CL1` -> YCharts `WTI`) — the US-advisor-platform default and C3 §3.1's stated likely answer — but confirm from the pkl column before pinning. Both Crude Oil symbols are already pull-spec READY (rows 67-68: `^BCOB` / `WTI`).

## 5. Endpoint + module

- All 63 series -> `client.general_data(yc_symbol, metric="price")` -> `parse_chart_series(rec)` -> monthly resample. One call per index (the generic entity-agnostic endpoint).
- Module section: `ws2_correlation_pull.py` in `infra/aws/lambda/ycharts-market-data-pull/`, importing the shared `ycharts_client`. Builds the 63-symbol pull + the monthly-return shaping; emits the `return_monthly`-shaped input the generator consumes.
- Freeze-aware: `structural_self_test()` validates the 63-symbol map completeness, the monthly-resample logic, and the 4 flagged-row handling against synthetic data — no live YCharts.

## 6. Open items

| # | Item | Plan |
|---|---|---|
| CR-O1 | TR2 / TR3 — no pure-Treasury 1-3yr / 7-10yr YCharts Bloomberg index | Methodology decision (COO-routed) — representative proxy w/ caveat, post-unfreeze search probe, or drop from the correlation universe. NOT a Gov/Credit silent map. |
| CR-O2 | Crude Oil variant (Brent vs WTI) | Deterministic — read the `bbg_ticker` column for `Crude Oil` from `data.pkl`; pin accordingly. |
| CR-O3 | The known `MSCI United Kindom` PKL typo is in the 63-index list | The crosswalk join is on `portal_name` — the crosswalk must carry the typo'd string verbatim; confirm the dc01d4b8a row matches `MSCI United Kindom` exactly (do not "correct" it — the generator + pkl both use the typo). |

## 7. Coordination

- 3 Treasury crosswalk gaps + Crude Oil variant are WS-2-side calls (C3 §4; confirmed by 0.1.0_DS). TR1 resolved; TR2/TR3 surfaced to COO as a methodology decision; CO is a deterministic pkl lookup.
- RAVC2 to 2.0.0_SA_COO (no CC CTO per Andrew directive). This is C2 phase artifact 3.
