# Model Portfolios — AUTHORITATIVE census: data dictionary (header + AUA tab) + MDPF_REVAMP coverage

**Status:** AUTHORITATIVE — CTO-CO-SIGNED (1.0.0_SA_CTO @220244Z) / two-independent-confirmed (3.0.0_SA_CVO + 1.0.0_SA_CTO). The census for Andrew.
**Authors:** 3.0.0_SA_CVO (FE data-dictionary + revamp-coverage + field-level + content grounding) reconciled with 1.0.0_SA_CTO (FE-consumption census). **Rule: a fetch is "covered" only when BOTH confirmed it — every row below survived that cross-check (it corrected 2 real errors: CVO's FactorTilts row that CTO's agent dropped; CTO's getAUMSummary rows CVO didn't have).**
**Date:** 2026-07-21 · **For:** Andrew (direct ask). **Grounding:** live portal @ DEV + live S3 served artifacts + revamp producer scripts + a rendered /portfolios. Every field path is `file:line`.
**Page:** `portal/src/pages/ModelPortfolios.tsx` (route `/portfolios`). SEV1 critical surface.

---

## PART 0 — BOTTOM LINE for Andrew
- The MP header + AUA tab render from **5 in-scope served artifacts.** The revamp **covers 3** (aggregate-aua, account-distribution, non_model_assets) and **does NOT cover 2**: **`aum-metrics` (A1)** and **`aum-timeseries` (A2)**.
- Those 2 uncovered artifacts feed the header **quarter-delta tiles**, the **AUM growth cards**, the **AUA Daily Trend chart**, and the **global enterprise Total** — and `aum-metrics` has a **4-surface blast radius** (MP + FactorTilts + Attribution + Positioning), 2 of them non-MP pages that don't fetch the aggregate.
- **DISPOSITION (CTO, SPLIT after the staleness grounding): A1 = Option Y (BUILD producer); A2 = Option X (FE-DERIVE).** A1 (aum-metrics) has a 4-surface blast radius (2 non-MP pages don't fetch the aggregate) -> build the producer off the revamp aggregate, repoint-only. A2 (aum-timeseries) is a **deprecated frozen artifact the FE already routes around** -> FE-derive the trend from the current revamp aggregate (a correction, not a rebuild). Plus **fold `non_model_assets` into the revamp** to decouple A4 from the legacy emitter (cutover-blocking, DS).
- **`cohort_provenance`** — **RESOLVED (Andrew-direct):** DS **source-path-derives** it in the aggregate producer (each cohort's provenance == the `{source}` segment it reads from: SmartX/Schwab/Eclipse/Orion/BD), replacing BOTH the served's 82 hand-labels AND the revamp's all-None. A NAMED parity delta vs the served hand-labels (intended, not a reset). Still FE-safe (0 consumers), NOT a render gate. **CVO future-verify:** when DS reports the source->provenance map, check each label == the real read-path segment (lineage-derived, not re-hand-labeled).
- **Cutover-blocker (CVO EXT#1, routed to DS):** the revamp A4 is coupled to the legacy daily emitter (`build_legacy_compat_emit.py`) that produces A2 — untangle + verify-survives-repoint regardless of A1/A2.

---

## PART 1 — Full consumer denominator (every MDPF/AUM/Portfolio-Analytics fetch)

### In-scope (Model Portfolios page)
| queryKey | endpoint | S3 key | area | revamp covers? |
|---|---|---|---|---|
| `['mdpf-per-firm-timeseries',firm]` | `getMdpfAggregateAUATimeSeriesByFirm(firm)` | `json/mdpf/{firm}/aggregate-aua-timeseries.json` | header + AUA | ✅ `gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` |
| `['mdpf-aggregate-timeseries','global']` | `getMdpfAggregateAUATimeSeriesByFirm('global')` | `json/mdpf/global/...` | header + AUA (global) | ✅ |
| `['mdpf-per-firm-distribution',firm]` | `getAccountDistributionByFirm(firm)` | `json/mdpf/{firm}/account-distribution.json` | AUA (Client Holdings) | ✅ |
| `['account-distribution']` | `getAccountDistribution()` | `json/portfolios/account-distribution.json` | AUA (global) | ✅ |
| `['non-model-assets']` | `getNonModelAssets()` | `json/portfolios/non_model_assets.json` | header Total (global) | ✅ (but A4 legacy-coupled, see Part 4) |
| `['aum-metrics']` (`:425`) | `getAUMMetrics()` | `json/portfolios/aum-metrics.json` | header tiles + growth cards | ❌ **GAP A1** |
| `['aum-timeseries']` (`:430`) | `getAUMTimeSeries()` | `json/portfolios/aum-timeseries.json` | AUA Daily Trend + enterprise-trend | ❌ **GAP A2** |
| `['model-portfolio-benchmarks']` / `['etf-benchmark-returns']` / `['peer-performance']` | benchmarks/etf/peers | `json/benchmarks/*`, `json/peers/*` | BENCHMARK + PEERS tabs | out-of-scope (YANG/phase-2) |

### Cross-surface consumers of the uncovered artifacts (the blast radius — why disposition = Y)
| consumer | call | reads | fetches the aggregate too? |
|---|---|---|---|
| `ModelPortfolios.tsx:425` | `getAUMMetrics()` | `aum-metrics.json` | yes |
| `FactorTilts.tsx:83` | `getAUMMetrics()` | `aum-metrics.json` | **no** (CVO EXT#2; corrected CTO's agent) |
| `Attribution/tabs/SelectionTab.tsx:89` | `getAUMSummary()` | `aum-metrics.json` (portal-proxy.ts:264) | **no** (CTO leg; CVO-confirmed) |
| `Positioning/tabs/HoldingsTab.tsx:564` | `getAUMSummary()` | `aum-metrics.json` | **no** (CTO leg; CVO-confirmed) |
| `ModelPortfolios.tsx:430` | `getAUMTimeSeries()` | `aum-timeseries.json` | yes |
| PartnerAnalytics AUA surface (AdvisorIntelligence) | advisor-intelligence pipeline | `opal-data-bd`/`opal-data-inf` (NOT MDPF) | **SEPARATE DOMAIN — not a migration target** |

---

## PART 2 — Data dictionary: HEADER + AUA (growth) tab
Header/main panel = **PORTFOLIO ANALYTICS** (always visible): `AUA BY MODEL` bars · `CLIENT HOLDINGS` distribution · `Total AUA` + 3 quarter-delta tiles. Below it the **AUA** tab (`growth`) adds the AUA Daily Trend chart. (Rendered /portfolios confirmed layout; local dev shows $0/empty — a CORS/no-data local limitation, not a defect.)

| element | component | source artifact | field(s) `file:line` | transform | covered? |
|---|---|---|---|---|---|
| Total AUA tile | inline `:1057` | per-firm aggregate-aua / global non_model+trend | `partner_custody_total` lastNonNull `:759`; global `modelAUM + nonModelData.latest.non_model_aum` `:763` | lastNonNull/sum | per-firm ✅; **global MIXED** |
| AUA BY MODEL bars | recharts | aggregate-aua | `by_model[k].{model_value(lastNonNull),display_name,cohort_class}` `:507-508` | lastNonNull; blend-split `:200` | ✅ |
| Last Qtr/2Q/3Q tiles | inline `:1221` | **aum-metrics** | `metricsData.dates.{q0-3}` `:519`; `metricsData.total.{q0-3}` `:1242` | QoQ | ❌ A1 |
| AUM growth cards | `AUMGrowthMetrics` `:1217,1236` | **aum-metrics + aum-timeseries + aggregate** | `metricsData.total` `:1239`; `aum:totalAUM`; `enterpriseQ0/Q1=trendEnterpriseAt(dates.qN)` `:1231` | mix | ❌ MIXED |
| CLIENT HOLDINGS | `AccountDistributionChart` `:1309` + `AccountDistributionMetrics` `:1314` | account-distribution | `by_model[k].{percentiles,median,histogram,account_count}`, `total.{...}` | group stats | ✅ |
| AUA Daily Trend | recharts `:1426` (`activeTab==='growth' && timeSeriesData.aggregate`) | **aum-timeseries** | `timeSeriesData.aggregate[].{period,aum,account_count}` (547) | columnar | ❌ A2 |
| as-of badge | `PageHeaderCleanBadge` | aggregate-aua | `as_of_last` `:479` | — | ✅ |

**FE consumes from aggregate-aua:** `dates, model_aua, non_model_aua, partner_custody_total, opal_aggregate_aua(global), as_of_last, by_model.{display_name,cohort_class,model_value,account_count}`. **NOT consumed (0 FE refs):** `cohort_provenance, source_vintage_last, sma_aua` — none are in the FE type `MdpfPerFirmTimeSeries` (portal-proxy.ts:424).

---

## PART 3 — Coverage cross-reference (current SERVED shape vs REVAMP production)

### 3a. Artifact level
| artifact | served (json/…) | revamp (gold/mdpf_revamp/…) | gap |
|---|---|---|---|
| aggregate-aua (A5/A6) | 429 dates, all fields | 427 canonical dates, data byte-verified | `cohort_provenance` all-None; 427 vs 429 named date-delta |
| account-distribution (A3/A7) | total+by_model stats | parity-clean | 1-day vintage drift only |
| non_model_assets (A4) | 455-date v0_9 | 433-date 2-term (D-2) | ruled D-2+F2 named delta; **A4 legacy-coupled (Part 4)** |
| **aum-metrics (A1)** | period+dates{q0-3}+total+by_model[7]{model_name,aum,account_count,q0-3} | **NOT PRODUCED** | whole artifact; 4-surface blast radius |
| **aum-timeseries (A2)** | aggregate[547]{period,aum,account_count}+by_model{5}+periods[547] | **NOT PRODUCED** | whole artifact; STALE@05-29 (see Part 5) |

### 3b. Field-level non-overlap (`cohort_provenance` — Andrew's example, CONFIRMED)
SERVED 49F = **82 non-None** real labels (`{basis:'schwab_canonical_rederived', custody:'rollforward:<date>', model_1a:'measured', sma_1c:'interpolated_estimate', sma_1c_method:'bandaid_interp'}`). REVAMP = **all-None**, hardcoded `[None]*len(dates)` (`dim_mdpf_aggregate_aua_timeseries.py:656`/`:814`; global omits). MECHANICAL = present-but-unpopulated. DECLARATIVE = consistent (docstring `:16`, meta note `:688`, co-sign item `:694` all declare None-by-design). SEMANTIC = **FE-safe (0 consumers)** but a **fidelity loss** vs served's estimate/rollforward labels. **Disposition — RESOLVED (Andrew-direct, CTO 205030Z): SOURCE-PATH-DERIVED** — DS populates it in the aggregate producer from each cohort's real read-source (`{source}` segment), replacing both the served hand-labels and the revamp None; a NAMED intended parity delta, still FE-safe. CVO verifies the source->provenance map is lineage-derived when DS reports. *(My earlier "byte-identical" compared two revamp re-stages, not revamp-vs-served — corrected here.)*

---

## PART 4 — Producer topology + dispositions

**Producer topology:**
- Revamp aggregate/account-dist: `dim_mdpf_aggregate_aua_timeseries.py` -> `gold/mdpf_revamp/{firm}/`.
- Revamp A4: `dim_mdpf_non_model_assets.py` -> `gold/mdpf_revamp/global/non_model_assets.json` — **but `:7` couples it to** the legacy emitter.
- **Legacy daily emitter:** `build_legacy_compat_emit.py` on the `mdpf-daily-runner` EC2 (wired `mdpf-daily-dispatch.sh:358` + `legacy-emit-ssm.tf`) produces **A2 (`aum-timeseries`) AND `non_model_assets`** to `json/portfolios/`, v0_9 methodology.

| item | disposition | why |
|---|---|---|
| **aum-metrics (A1)** | **Option Y: BUILD a revamp producer off the aggregate** (field-identical) | 4-surface blast radius incl. 2 non-MP pages (Attribution/Positioning) that don't fetch the aggregate -> FE-derive is invasive; producer keeps all consumers repoint-only. |
| **aum-timeseries (A2)** | **Option X: FE-DERIVE the trend from the revamp aggregate** (not build) | A2 is a DEPRECATED frozen artifact the FE already routes around (`:753`); building a fresh producer just perpetuates the legacy split. FE-derive = single-source correction; axis flips calendar->trading-day (aligns NEVER#1; the 146 weekend fills are the artifact). Also RETIRE the frozen 11:30 emitter (Part 5). |
| **A2/A4 legacy coupling (CVO EXT#1)** | **CUTOVER-BLOCKING — untangle + verify-survives-repoint (routed to DS)** | A4 (a covered 7-key member) is derived via the same legacy emitter that produces A2; a repoint of A4 must not break, and A2's retirement must not orphan A4. |
| **Global enterprise Total** | migrate A2 with the others OR re-derive Total from revamp aggregate | `:745`/`:763` builds global Total = aum-timeseries(legacy model) + non_model_assets(revamp) = mixed-basis if A2 lags. |
| **cohort_provenance** | **RESOLVED: source-path-derived in the aggregate producer (Andrew-direct)** | replaces served hand-labels + revamp None; a NAMED intended parity delta; FE-safe (0 consumers); CVO verifies lineage vs read-paths when DS reports. |

---

## PART 5 — Content groundings (open questions resolved)

**A2 is a live CLOBBER, not benign staleness (Andrew "make certain" -> deep-verified) — this SETTLES A2=X:** version-history of `json/portfolios/aum-timeseries.json` (23 versions) shows TWO producers writing one key: a **daily 11:30 `build_legacy_compat_emit.py`** (self-referential, `RunDate` NOT passed to the script -> self-perpetuating **FROZEN 05-29** snapshot, byte-identical daily) and an **irregular fresh producer** (current to 07-18, then STOPPED). The frozen 11:30 emitter now dominates -> served A2 is stuck at 05-29 (~35 trading days), and the **AUA Daily Trend chart currently renders 05-29 data**. Applying "07-18 is Saturday": the fresh-pipeline gap is 2 trading days (mild); the 05-29 A2 is the egregious deprecated asset. `non_model_assets`/`aggregate-aua` are NOT clobbered. **So A2=X is not just "FE-derive because stale" — it is RETIRE a deprecated self-perpetuating clobber + derive fresh from the revamp aggregate.** (Detected reproducibly by the new `comp-clobber --sweep opal-data-portal-v2 json/portfolios/` -> 1 clobbered key: aum-timeseries. The aggregate carries what A1+A2 need: `dates`, `model_aua`/`custody`, `by_model.account_count`, quarter-end lookups; axis flips calendar->trading-day, aligning NEVER#1.)

**Content-gap B (account_count real-vs-fill) — ANSWERED:** SERVED account_count is **REAL daily history** — `by_model[LTC]`: 388 distinct/429, max flat-run 3 (weekend fill), **0 None on any trading day**. The revamp **ties served exactly on all 407 common dates**; the picket-fence = **20 real trading days the served axis lacks entirely** (legacy backfill gaps), on all of which the revamp has real `model_value` but `account_count=None`. **Root = an asymmetric source in the producer:** `model_value` is SILVER-derived (has the dates) but `account_count` is IMPORTED from the gappy served aggregate. **NOT a regression.** DS call: accept honest-None on the 20 additive dates, or derive `account_count` from silver (symmetric with `model_value`) for completeness.

**Content-gap A (inflection model_value) — OPEN:** direction is NOT uniform (served blends carry ~38 non-None vs revamp ~421 — revamp is *fuller* there); needs a per-date, per-cohort diff before ruling. Lower priority than B.

---
*Reconciled two-independent-confirmed census, CTO-CO-SIGNED (1.0.0_SA_CTO @220244Z). Sources: this session's live-S3 + portal@DEV grounding, all `file:line` cited.*
