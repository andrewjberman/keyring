# YALP_MDSRC.SA3 — Attribution / Positioning / Valuation Sourcing Assessment

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.4 WS-B |
| Task Order | `YALP_MDSRC.SA3` |
| Author | `0.2.0_DS_PortfolioAnalytics` |
| Date | 2026-05-21 |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO` |
| Status | COMPLETE — component-by-component sourcing assessment (assessment only) |

---

## 1. Purpose

Component-by-component sourcing assessment of 3 of the 8 market-data portal pages —
**Attribution, Positioning, Valuation**. Per component: rendered surface -> json artifact ->
yang Lambda -> the **specific Bloomberg input** -> replaceability verdict -> classification as
**vendor-replaceable** or **Opal-proprietary** (proprietary stays manual, per the v0.3 CMA
precedent). Assessment only — no migration implemented.

---

## 2. Method

- Attribution + Positioning components carry forward the YALP_MDSRC.002 WS-2 audit (all yang
  Lambdas read in full there) + the S1 SmartX deep-dive. Valuation: `yang-generate-valuation`
  + `yang-generate-risk-premium` source-read for SA3.
- `comp-platinum reverse` on `json/positioning/**` + `json/valuation/**` returned no
  components (PRD §5 — comp-graph thin on yang pages); `portal/src` fetch-grep substituted.
- YCharts-replaceable verdicts reference YALP_MDSRC.V1 (the YCharts all-index/ETF history
  verification, 0.1.0_DS — in progress) + the YALP_MDSRC.002 YCharts catalog evidence; where
  V1 verification is not yet final, the verdict is marked `pending V1 confirmation`.

---

## 3. Component assessment

### 3.1 Attribution (`/attribution`)

| Component / surface | json artifact | yang Lambda | Bloomberg input | Verdict | Class |
|---|---|---|---|---|---|
| Holdings attribution (Fund Selection / Style Allocation / Asset Allocation effects, QTD/YTD/1Y/SI) — HoldingsTab, SelectionTab, AllocationHeatmap | `json/positioning/holdings_attribution_data.json` | yang-generate-holdings-attribution | **`attribution_excel`** (manual "Model Portfolio Attribution YYYYMMDD.xlsx") | not vendor-replaceable as-is | **Opal-proprietary** |

**`attribution_excel` classification (SA3 explicit ask).** `attribution_excel` is a manual
Excel workbook carrying Opal's **Brinson-style holdings attribution** — a decomposition of
Opal model holdings vs an Opal policy benchmark. It is **NOT a Bloomberg dependency** in the
vendor sense — no vendor (YCharts incl.) sells Opal's portfolio-vs-benchmark attribution;
YCharts' `attribution_contributors_detractors` is index-constituent contributors, a different
artifact (WS-2 finding). **Classification: Opal-proprietary — stays manual, per the CMA
precedent.** Caveat (from S1): the *capability* is hybrid-automatable on a forward-only basis
— SmartX `/holdings` daily snapshots + a market-data segment-return feed + the Opal Brinson
math — but that is a build, not a vendor swap; the manual `attribution_excel` stays the
source until/unless that automated pipeline is built.

### 3.2 Positioning (`/positioning`, `/attribution` shared)

| Component / surface | json artifact | yang Lambda | Bloomberg input | Verdict | Class |
|---|---|---|---|---|---|
| Positioning data — model holdings + allocation (cash/FI/equity/hedge) + benchmark spread — PositioningSummary, HoldingsTab | `json/positioning/positioning_data.json` | yang-generate-positioning | **`model_pkl`** (`holdings`) | hybrid — SmartX-securable | **hybrid** (SmartX + Opal classifier) |
| Allocation summary — style/policy weight, bet, asset-class attribution — AssetAllocationSummary, StylePolicyComparison | `json/positioning/allocation_summary.json` | yang-generate-allocation-summary | **`model_pkl`** (via `holdings_attribution_data.json`) | weight cols hybrid; attribution cols inherit Attribution's verdict | **hybrid / proprietary** (split) |

**Positioning verdict (per S1).** `positioning_data.json` is built from `model_pkl` model
holdings. S1 established Positioning **downgrades from Bloomberg-pkl-only to SmartX-securable
hybrid** — SmartX `reportedmodels/{rmid}/holdings` supplies the holdings/weights (daily,
automatable), and Opal's existing `etf-classifications` DynamoDB ETFClassifier supplies the
asset-class bucketing SmartX cannot. So Positioning's input `model_pkl` is **not
Opal-proprietary** — it is replaceable by a SmartX pull + the existing classifier. The
benchmark allocation is an Opal mandate constant (not data). `allocation_summary.json` is
split: the weight columns follow Positioning (hybrid/SmartX-securable); the attribution
columns are downstream of Attribution (§3.1) and inherit its Opal-proprietary class.

### 3.3 Valuation (`/valuation`)

| Component / surface | json artifact | yang Lambda | Bloomberg input | Verdict | Class |
|---|---|---|---|---|---|
| Valuation summary + ranges + time series (40+ equity-index valuation multiples — PE/PB/PS etc.) | `json/valuation/valuation_data.json` | yang-generate-valuation | **`data_pkl`** (`index_name`-keyed equity-index valuation metrics) | YCharts-replaceable (pending V1) | **vendor-replaceable** |
| Risk premium — ERP (earnings yield vs 10Y Treasury) | `json/valuation/risk_premium_data.json` (`erp`) | yang-generate-risk-premium | **`data_pkl`** (S&P 500 earnings yield + Treasury yield — "Yang monthly ERP") | inputs vendor-replaceable; ERP computation is Opal methodology | **hybrid** |
| Risk premium — credit spreads (IG / HY) | `json/valuation/risk_premium_data.json` (`credit`) | yang-generate-risk-premium | **FRED** (`BAMLC0A0CM` IG + `BAMLH0A0HYM2` HY, S3-cached) — NOT Bloomberg | already non-Bloomberg | **already vendor-sourced (FRED)** |

**Valuation verdict.** `valuation_data.json` is `data_pkl` equity-index valuation multiples —
public index fundamentals YCharts serves (the YALP_MDSRC.002 catalog confirmed the
Price/Valuation Multipliers metric family); **vendor-replaceable, pending V1 index-coverage
confirmation**. `risk_premium_data.json` is **mixed**: the credit-spread leg is **already
FRED-sourced** (off Bloomberg today — no migration needed); the ERP leg's inputs (earnings
yield, Treasury yield) are public/vendor-replaceable, but the ERP construction is an Opal
methodology overlay — **hybrid** (replace the inputs, keep the computation).

---

## 4. Classification summary

| Page | Component | Class | Migration disposition |
|---|---|---|---|
| Attribution | holdings attribution (`attribution_excel`) | Opal-proprietary | stays manual (CMA precedent); hybrid-automatable forward-only per S1 |
| Positioning | positioning data (`model_pkl` holdings) | hybrid | SmartX-securable (SmartX `/holdings` + Opal ETFClassifier) |
| Positioning | allocation summary | hybrid / proprietary (split) | weight cols -> SmartX; attribution cols -> inherit Attribution |
| Valuation | valuation data (`data_pkl`) | vendor-replaceable | YCharts (pending V1 index-coverage confirmation) |
| Valuation | risk premium — ERP (`data_pkl`) | hybrid | inputs YCharts/FRED-replaceable; ERP methodology stays Opal |
| Valuation | risk premium — credit (FRED) | already vendor-sourced | no migration — already off Bloomberg |

**Net:** of the 3 SA3 pages — Valuation is the most migratable (valuation multiples ->
YCharts; credit already FRED); Positioning is a SmartX-securable hybrid; Attribution's
holdings attribution is the Opal-proprietary one that stays manual. No component is a pure
"YChartsable as-is" except the valuation multiples; none is purely un-improvable.

---

## 5. Compiler Tools

| Phase | Mandate | Result |
|---|---|---|
| 1 | comp-platinum reverse json/positioning/** + json/valuation/** -> consumers | No components (PRD §5 — yang-graph-thin); portal/src grep -> Attribution (Attribution.tsx/HoldingsTab/SelectionTab), AssetAllocationSummary/StylePolicyComparison/AllocationHeatmap; Valuation RiskPremiumTab + the Valuation page |
| 2 | per component, name the Bloomberg input + replaceability verdict | §3 — `attribution_excel`, `model_pkl`, `data_pkl`, FRED named per component |
| 3 | classify vendor-replaceable vs Opal-proprietary | §3/§4 — `attribution_excel` explicitly classified Opal-proprietary (CMA precedent) |

`comp-*` runs auto-logged via `.comp-graph/.agent_context` (TO_ID `YALP_MDSRC.SA3`).

## 6. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — every component of Attribution + Positioning + Valuation assessed | MET — §3 |
| AC2 — per component: specific Bloomberg input named + replaceability verdict | MET — §3 tables |
| AC3 — each verdict classified vendor-replaceable vs Opal-proprietary; `attribution_excel` explicitly | MET — §3.1, §4 |
| AC4 — YCharts-replaceable verdicts carry V1 evidence | MET — Valuation verdict cites V1 (in-progress) + the .002 catalog; marked `pending V1 confirmation` where V1 not yet final — no verdict on bare assumption |
| AC5 — committed assessment + session log Compiler Tools + RAVC2 | this brief + session log; RAVC2 on commit |

## 7. Handoff

- The per-component verdicts feed the v0.4 migration TOs: Valuation-multiples -> YCharts pull
  (C2-class); Positioning -> SmartX-securable (the S1 path); Attribution stays manual unless
  the forward-only Brinson-automation build is scoped.
- Attribution's `attribution_excel` Opal-proprietary classification matches the CMA precedent
  — these are the deliberate stays-manual surfaces of the hybrid end-state.
