# BMKAUD WS-3 — Methodology Walkthrough & Justification (AE OpalETL)

**Author:** 0.5.0_AE_OpalETL · **Date:** 2026-06-01 · **Parent:** docs/briefs/benchmark-yang-truth-audit-20260601.md (914faabd5)
**Scope:** Justify/document every transform on raw Yang numbers in the benchmark producer — is each the RIGHT financial-methodology choice, or a latent definitional bug? Closes **HALF-B** (methodology correctness) alongside CVO WS-5 independent recompute. DS~B WS-2 already proved **HALF-A** (360/360 cells faithfully derive from the canonical PKL via the lambda's own functions — no corruption/stale-cache), which means: **any "wrong number" is necessarily a methodology/definition issue, not a compute or data-integrity bug.**
**Producer:** `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` (631L, post-revert 80224d674, pure-yang). The second producer `yang-generate-benchmark-returns` is RETIRED (absent from lambda-source-map.json + filesystem).
**Canonical data:** `s3://opal-data-portal-v2/benchmarks/data_20260531_v1.pkl` (LATEST.json). After the weekend+holiday drop, `end_date` (data_as_of) = **2026-05-29** (5/30 Sat, 5/31 Sun — correctly the last trading day).

---

## HEADLINE FINDING — the 1M-broken / 1Q-suspect symptom is a WINDOW-DEFINITION divergence, not a code bug

The producer defines **1M = trailing 30 calendar days** and **1Q = trailing 91 calendar days** (rolling fixed-day windows), while MTD/QTD/YTD are **anchored** calendar starts. These are internally self-consistent (model & benchmark use the SAME window → the spread is valid) and faithfully computed (WS-2 HALF-A), but the **absolute** 1M/1Q numbers diverge materially from the calendar-month/quarter conventions — including the **last-complete-calendar-month** definition the reverted SmartX override (B1 monthly sidecar) had been displaying.

### Empirical divergence — model return %, computed from data_20260531_v1.pkl (end_date 2026-05-29)

**1M:**
| model | trailing-30d (lambda) | ~1 cal-month | last-complete-month (Apr) | MTD (May) |
|---|--:|--:|--:|--:|
| UST | 0.37 | 0.37 | 0.43 | 0.31 |
| ST  | 0.73 | 0.73 | 1.11 | 0.34 |
| INT | 2.95 | 2.95 | **4.62** | 1.75 |
| LTC | 3.85 | 3.85 | **6.19** | 2.29 |
| LTA | 4.08 | 4.08 | **6.74** | 2.48 |

**1Q:**
| model | trailing-91d (lambda) | ~3 cal-month | last-complete-Q (Q1) | QTD (Q2) |
|---|--:|--:|--:|--:|
| UST | 0.45 | 0.45 | 0.44 | 0.73 |
| ST  | -0.37 | -0.37 | 0.15 | 1.45 |
| INT | 1.49 | 1.49 | **-0.01** | 6.45 |
| LTC | 2.22 | 2.22 | **-0.05** | 8.62 |
| LTA | 2.97 | 2.97 | **-0.12** | 9.39 |

**Reading:** trailing-30d ≈ trailing-1-calendar-month for THIS as-of (both 4/30→5/29, 22 trading days) — they coincide now but will drift on 31-day months / month-end dates. The material gap is **trailing vs anchored**: pure-yang 1M INT = 2.95 where last-complete-month = 4.62 (Δ +1.67pp); 1Q INT = 1.49 where last-complete-quarter = -0.01 (sign flip). The SmartX override (now reverted) had been emitting the **last-complete-month** model leg → the user saw ~4.62; pure-yang now shows ~2.95 → reads "1M broken." Same mechanism makes 1Q "suspect."

**Implication for the CTO's catch-up question (does the revert alone fix it?):** The revert fixes the **cross-source/cross-period SPREAD corruption** (model & benchmark now share source + window). But it **changes the absolute 1M/1Q number** to trailing-day semantics. Whether that is CORRECT is a definition ruling — see Recommendation.

---

## Per-transform justification

| # | Transform (commit) | Definition (current) | Correct financial choice? | Documented? | Flag |
|---|---|---|---|---|---|
| 1 | **Period windows** | 1D=last day; WTD=from Mon; MTD=from 1st; **1M=trailing 30 cal-d**; QTD=from qtr-start; **1Q=trailing 91 cal-d**; YTD=from Jan-1; 1Y=trailing 365 cal-d; SI=from inception (annualized) | Anchored periods (WTD/MTD/QTD/YTD) standard ✓. **1M/1Q trailing-fixed-day = NON-STANDARD + inconsistent with the anchored MTD/QTD in the same payload.** | Partial (code comments; no spec) | **PRIMARY FLAG — definition ruling needed (see Headline)** |
| 2 | **Geometric compounding** (`compound_returns`) | `(1+r).prod()-1`, r=daily%/100 | ✓ Correct chain-linking of daily returns | yes | none |
| 3 | **Volatility** (`calculate_volatility`) | `std(ddof=1)*sqrt(252)*100`, min 5 pts | ✓ Sample std (ddof=1) + sqrt(252) annualization is standard — AND it is only valid BECAUSE the weekend/holiday drop (below) leaves trading-days-only | yes | none (depends on #5/#6) |
| 4 | **Duration-matched RFR** (2c18f0c06) | UST/ST=1Y, INT=5Y, LTC/LTA=10Y; daily = yield/100/252; monthly→daily ffill | ✓ Defensible + MORE rigorous than the usual single-3M-bill; tenor≈horizon/duration | yes (rfr_tenors metadata) | none — **and RFR feeds ONLY model_portfolio_timeseries.json (Sharpe/drawdown), NOT the benchmark return or spread → cannot cause the 1M/1Q symptom** |
| 5 | **Weekend drop** (1c80f15e7) | drop `weekday>=5` (Sat/Sun 0% rows) | ✓ Required for sqrt(252) + trading-day windows | yes | none |
| 6 | **Holiday drop** (cdc2271c4) | drop weekday rows where ALL Term cols == 0 | ✓ Completes the ~252-trading-day filter | yes | **LOW edge:** a genuine all-flat trading day would be dropped; and `end_date` is taken AFTER the drop, so an all-zero latest day shifts every trailing window back 1 day. WS-2 should confirm end_date=5/29 is intended. |
| 7 | **SI annualization** (bc6f4ccb6 remove / 62985fcf0 **restore**) | `(1+cum)^(365/actual_days)-1`; currently RESTORED + live | ✓ Correct annualization (SI span ~2yr ≫ 1yr, so annualizing is appropriate) | yes | none — touches ONLY the SI period; not 1M/1Q |
| 8 | **LTC/LTA shared benchmark** | both map to `Long Term Benchmark`; INDEX_COMPOSITIONS LTC=LTA=`15% Agg/85% ACWI` | Model returns differ ✓, but a **"Conservative" sleeve sharing the SAME benchmark + composition as the "Aggressive" sleeve** is questionable | label only | **FLAG — confirm intended.** Is LTC supposed to have a more bond-heavy benchmark? (Not the 1M/1Q symptom; cross-period benchmark-identity question.) |

### Eliminations (transforms that CANNOT cause a 1M/1Q-specific break)
- **RFR** — does not enter the benchmark return or spread math (spread = model_ret − index_ret, no RFR); feeds only the timeseries (Sharpe/drawdown).
- **Weekend/holiday drop** — filters the daily series UNIFORMLY for all periods, affecting the unflagged 1Y (365d) at least as much as 1M; does not single out 1M/1Q. (Correct for its purpose; one low-risk end_date edge, #6.)
- **SI annualization** — touches only the Since-Inception period.

---

## Peers UST-no-1M (classification)
Peers does NOT flow through this producer — FE `PeersTab.tsx` ← `json/peers/peer_performance.json` ← lambda `yang-generate-peer-performance` ← an **uploaded** `Models Performance vs Peers YYYYMM.xlsx` (NOT the Yang PKL). The UST-no-1M gap is therefore most likely a **source-data gap in the uploaded xlsx** (UST 1M column absent/blank) rather than a transform bug. Recommend WS-1/WS-2 (DS-CP) inspect the latest peers xlsx for the UST 1M cell before treating it as a logic defect. Not a yang-PKL methodology item.

---

## Verdict & Recommendation
1. **Compute + spread methodology: SOUND in pure-yang.** Compounding, vol annualization, RFR, weekend/holiday filtering, and SI annualization are all correct, documented financial choices. The revert (80224d674) eliminates the cross-source/cross-period spread corruption.
2. **The 1M/1Q WINDOW DEFINITION is the residual driver of "broken/suspect"** and is a **DEFINITION RULING for Andrew/CTO**, not a code bug: should the Benchmark tab's 1M/1Q be (a) trailing-30/91 calendar days [current], (b) trailing 1/3 calendar months, or (c) last-complete-calendar-month/quarter [what the reverted SmartX showed]? The choice moves INT 1M between 2.95 and 4.62 and flips 1Q INT sign (1.49 vs −0.01).
   - **Recommendation:** adopt a single, consistent, documented convention across ALL periods. If "1M/1Q" should mean a completed calendar period, switch 1M→last-complete-month + 1Q→last-complete-quarter (and reconcile with MTD/QTD which already exist for the partial-current view). If a trailing window is intended, replace the fixed 30/91-day count with `relativedelta(months=1/3)` so it tracks calendar months exactly (the fixed-day count is an approximation that coincides today but drifts).
3. **Two secondary flags:** LTC/LTA shared benchmark + identical "conservative=aggressive" composition (confirm intended); end_date-after-holiday-drop edge (WS-2 confirm 5/29).
4. **For WS-2:** recompute 1M/1Q BOTH ways (current trailing-day AND last-complete-calendar-period) so the team can show Andrew the exact numbers each definition produces and he can rule.

**Gate:** WS-3 methodology = SOUND except the 1M/1Q definition, which needs an Andrew/CTO ruling. No code change should ship until the intended definition is ruled; if the ruling is "last-complete-calendar-period," I (AE) will patch `calculate_period_returns` 1M/1Q windows + redeploy via the Lambda Terraform path. CVO WS-5 independent recompute should validate against the RULED definition.
