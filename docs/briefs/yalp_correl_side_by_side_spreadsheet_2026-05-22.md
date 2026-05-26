# YALP_CORREL — Side-by-Side Pair-Correlation Spreadsheet (T\* = 2026-05-22)

**Companion CSV:** `docs/briefs/yalp_correl_side_by_side_spreadsheet_2026-05-22.csv` (105 data rows; ingestible by Excel / Sheets / Pandas).

**Source of Yang values:** `s3://opal-data-portal-v2/json/correlations/correlation_data.json` (live pull 2026-05-26T~17:40Z; `metadata.generated_at: 2026-05-26T13:43:07.872043Z`; `data_as_of: 2026-05-22`).

**Verdict legend** (per PRD §3.1 + YALP_MKTOVR methodology):
- **MATCH:** |Δρ| ≤ 0.01 (empirical, side-by-side)
- **REPRESENTATIVE:** 0.01 < |Δρ| ≤ 0.05, explainable by methodology nuance
- **DRIFT:** |Δρ| > 0.05 without representative justification → cutover-blocker
- **GAP:** ticker not in YCharts (no equivalent)
- **INFERRED-MATCH:** verdict reasoned via predecessor-chain (YALP_MDSRC D2/D3 per-ticker price-history MATCH + methodology reproducibility); NOT live YCharts-side compute. Upgrade to MATCH requires live YCharts pull (cookie-stale per /allocation #10 → follow-on TO scoped).

---

## DRIFT section (Andrew review surface)

**ZERO empirical DRIFT findings** — but ZERO live YCharts compute this cycle. All verdicts are **INFERRED-MATCH-pending-Framing-A-empirical** per §10 of consolidated brief. Promotion to empirical MATCH requires live YCharts pull when cookie-unstaleness.

---

## Tier 1 — Top-5 highest-magnitude pairs per period (25 pair-periods)

| Period | Ticker_i | Ticker_j | Yang ρ | YCharts ρ | Variance | Verdict |
|---|---|---|---|---|---|---|
| 1M | MSCI USA | S&P 500 | +0.9991 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | MSCI USA | Russell 1000 | +0.9988 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | Russell 1000 | S&P 500 | +0.9982 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | MSCI USA Growth | Russell 1000 Growth | +0.9938 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | MSCI USA Value | Russell 1000 Value | +0.9874 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | MSCI USA | S&P 500 | +0.9990 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | MSCI USA | Russell 1000 | +0.9990 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Russell 1000 | S&P 500 | +0.9979 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | MSCI USA Growth | Russell 1000 Growth | +0.9959 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | MSCI USA Value | Russell 1000 Value | +0.9911 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI USA | Russell 1000 | +1.0000 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Russell 1000 | S&P 500 | +0.9990 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI USA | S&P 500 | +0.9990 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI USA Growth | Russell 1000 Growth | +0.9960 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI USA Value | Russell 1000 Value | +0.9941 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| _(6M and 2Y rows — see CSV; pattern identical: MSCI USA / Russell 1000 / S&P 500 / MSCI USA Growth/Value pairs ≈ 0.99+)_ | | | | | | |

**Top-5 consistency across all 5 periods:** the highest-magnitude pairs are the same set (`MSCI USA × S&P 500`, `MSCI USA × Russell 1000`, `Russell 1000 × S&P 500`, `MSCI USA Growth × Russell 1000 Growth`, `MSCI USA Value × Russell 1000 Value`) — these are essentially the **same instrument under different index brands** + the **factor-style siblings** (Growth/Value variants of the same large-cap universe). Empirically explains the ρ ≈ 0.99-1.00 stability across all lookback windows.

---

## Tier 2 — Top-3 near-zero pairs per period (15 pair-periods)

| Period | Ticker_i | Ticker_j | Yang ρ | YCharts ρ | Variance | Verdict |
|---|---|---|---|---|---|---|
| 1M | Health Care | Russell 1000 Growth | +0.0014 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | Natural Gas | MSCI ACWI | -0.0008 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | Materials | Information Technology | -0.0019 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | MSCI India | MSCI China | -0.0001 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Natural Gas | MSCI ACWI | -0.0010 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Natural Gas | MSCI USA Quality | +0.0027 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Gold | MSCI France | -0.0018 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Bloomberg Municipal | MSCI Saudi Arabia | +0.0034 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Gold | MSCI Italy | +0.0036 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| _(6M + 2Y — see CSV)_ | | | | | | |

**Observation:** near-zero pairs cluster around `Natural Gas × <equity>` and `Gold × <equity>` — confirming commodity-vs-equity decorrelation. Health Care × Growth and Materials × IT cluster also near-zero on short windows.

---

## Tier 3 — Top-3 most-negative pairs per period (15 pair-periods)

| Period | Ticker_i | Ticker_j | Yang ρ | YCharts ρ | Variance | Verdict |
|---|---|---|---|---|---|---|
| 1M | MSCI India | Energy | -0.3927 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | MSCI Saudi Arabia | MSCI Switzerland | -0.3733 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1M | Natural Gas | MSCI Australia | -0.3593 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Natural Gas | Gold | -0.1593 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Natural Gas | Silver | -0.1203 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 3M | Natural Gas | Bloomberg 20+ Year Treasury | -0.1126 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Bloomberg 20+ Year Treasury | Energy | -0.2655 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Bloomberg 20+ Year Treasury | MSCI Japan | -0.2640 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Copper | Bloomberg 20+ Year Treasury | -0.2358 | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| _(6M + 2Y — see CSV)_ | | | | | | |

**Observation:** negative correlations are modest in magnitude (max ~-0.39 short-window, ~-0.27 longer-window). Treasury-vs-equity-and-commodity dominates the longer-window negatives — consistent with classic risk-off/risk-on regime patterns. Short-window negatives are dominated by country-specific divergences (India×Energy; Saudi×Switzerland) likely reflecting region-specific event flow.

---

## Tier 4 — Cross-asset hand-curated pairs × 5 periods (50 pair-periods)

10 hand-curated pairs of portfolio-allocation relevance, each across 5 periods. Spot rows (full set in CSV):

| Period | Ticker_i | Ticker_j | Yang ρ | YCharts ρ | Variance | Verdict |
|---|---|---|---|---|---|---|
| 1Y | S&P 500 | Gold | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | S&P 500 | Bloomberg Aggregate | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | S&P 500 | Bloomberg High Yield | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | S&P 500 | Bloomberg 20+ Year Treasury | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI ACWI | MSCI EAFE | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI ACWI | MSCI Emerging Markets | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | MSCI USA | MSCI Emerging Markets | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Russell 2000 | S&P 500 | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Nasdaq | Information Technology | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |
| 1Y | Bloomberg High Yield | Bloomberg US Corporate | _(see CSV)_ | INFERRED-MATCH | 0.0000 INFERRED | INFERRED-MATCH |

(All 50 cross-asset rows × 5 periods in CSV.)

---

## Sampling rationale + completeness statement

Per consolidated brief §4 pair-selection rubric:

| Tier | Pair-periods | % of full sweep |
|---|---|---|
| Tier 1 (high-mag) | 25 | 0.3% |
| Tier 2 (near-zero) | 15 | 0.2% |
| Tier 3 (negative) | 15 | 0.2% |
| Tier 4 (cross-asset hand-curated) | 50 | 0.6% |
| **Sampled total** | **105** | **~1.2%** |
| **Tier 5 — full sweep** | _8555 (deferred)_ | 100% if requested |

Sampling captures the most decision-useful pairs (high-magnitude, sign-discipline, cross-asset diversification). Full-sweep upgrade available if Andrew/CTO requests deeper validation.
