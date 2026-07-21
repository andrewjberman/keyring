# Model Portfolios page — data dictionary (header + AUA/AUM tab) + MDPF_REVAMP coverage census

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-21 · **For:** Andrew (direct ask) + joint census with 1.0.0_SA_CTO (reconcile to one authoritative list)
**Grounding:** live portal source (portal/ @ DEV) + live S3 served artifacts (read-only) + the revamp producer scripts + a rendered /portfolios screenshot. Every field path is `file:line`. **A fetch is "covered" only when CTO and I both confirm it — this is my INDEPENDENT leg.**
**Page:** `portal/src/pages/ModelPortfolios.tsx` (route `/portfolios`, 2053 lines). SEV1 critical surface.

---

## PART 1 — The full query denominator (EVERY fetch the page makes)

| queryKey | endpoint fn | served URL (CF `/api/general/*` -> `/json/*`) | S3 key | area | revamp produces? |
|---|---|---|---|---|---|
| `['mdpf-per-firm-timeseries', firm]` | `getMdpfAggregateAUATimeSeriesByFirm(firm)` | `/api/general/mdpf/{firm}/aggregate-aua-timeseries.json` | `json/mdpf/{firm}/aggregate-aua-timeseries.json` | header + AUA | **YES** `gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` |
| `['mdpf-aggregate-timeseries','global']` | `getMdpfAggregateAUATimeSeriesByFirm('global')` | `/api/general/mdpf/global/aggregate-aua-timeseries.json` | `json/mdpf/global/...` | header + AUA (global) | **YES** `gold/mdpf_revamp/global/...` |
| `['mdpf-per-firm-distribution', firm]` | `getAccountDistributionByFirm(firm)` | `/api/general/mdpf/{firm}/account-distribution.json` | `json/mdpf/{firm}/account-distribution.json` | AUA (Client Holdings) | **YES** `gold/mdpf_revamp/{firm}/account_distribution.json` |
| `['account-distribution']` | `getAccountDistribution()` | `/api/general/portfolios/account-distribution.json` | `json/portfolios/account-distribution.json` | AUA (global Client Holdings) | **YES** `gold/mdpf_revamp/global/account_distribution.json` |
| `['non-model-assets']` | `getNonModelAssets()` | `/api/general/portfolios/non_model_assets.json` | `json/portfolios/non_model_assets.json` | header Total (global) | **YES** `gold/mdpf_revamp/global/non_model_assets.json` |
| `['aum-metrics']` | `getAUMMetrics()` | `/api/general/portfolios/aum-metrics.json` | `json/portfolios/aum-metrics.json` | header quarter tiles + AUMGrowthMetrics | **NO — GAP (A1)** |
| `['aum-timeseries']` | `getAUMTimeSeries()` | `/api/general/portfolios/aum-timeseries.json` | `json/portfolios/aum-timeseries.json` | AUA Daily Trend chart + enterprise-trend | **NO — GAP (A2)** |
| `['model-portfolio-benchmarks']` | `getModelPortfolioBenchmarks()` | `/api/general/benchmarks/model_portfolio_benchmarks.json` | `json/benchmarks/...` | **BENCHMARK tab** (`performance`) | out-of-scope (YANG/phase-2) |
| `['etf-benchmark-returns']` | `getETFBenchmarkReturns()` | `/api/general/benchmarks/etf_returns.json` | `json/benchmarks/etf_returns.json` | BENCHMARK tab | out-of-scope (phase-2) |
| `['peer-performance']` | `getPeerPerformance()` | `/api/general/peers/peer_performance.json` | `json/peers/peer_performance.json` | **PEERS tab** (`peers`) | out-of-scope (phase-2) |

**Tabs (render labels):** `growth`->**"AUA"** (in scope) · `performance`->**"BENCHMARK"** (phase-2) · `peers`->**"PEERS"** (phase-2).

---

## PART 2 — Data dictionary: HEADER + AUA (growth) tab (component -> field -> source -> covered?)

The header/main panel is **PORTFOLIO ANALYTICS** (always visible): `AUA BY MODEL` chart · `CLIENT HOLDINGS` distribution · `Total AUA` + 3 quarter-delta tiles. Below it, the **AUA** tab adds the AUA Daily Trend chart.

| rendered element | component | source (queryKey -> artifact) | exact field(s) `file:line` | transform | revamp-covered? |
|---|---|---|---|---|---|
| **Total AUA** tile | inline tile (`ModelPortfolios.tsx:1057`) | per-firm: aggregate-aua; global: non_model_assets + trend | per-firm `perFirmMdpfData.partner_custody_total` (lastNonNull) `:759`; global `modelAUM + nonModelData.latest.non_model_aum` `:763` | lastNonNull / sum | per-firm **YES**; **global = MIXED** (model from revamp by_model + non_model from revamp A4, but see :745 enterprise path) |
| **AUA BY MODEL** bars | recharts block | aggregate-aua | `by_model[k].model_value` (lastNonNull -> currentAUM) `:508`; `display_name` `:507`; `cohort_class` (sma fold) | lastNonNull; blend-split `:200-205` | **YES** |
| **Last Qtr / 2Q / 3Q** delta tiles | inline (`:1221`,`qMetric`) | **aum-metrics** | `metricsData.dates.{q0,q1,q2,q3}` `:519`; `metricsData.total.{q0..q3}` `:1242` | QoQ change | **NO (A1)** |
| **AUM growth metric cards** | `AUMGrowthMetrics` `:1217,1236` | **aum-metrics + aum-timeseries + aggregate-aua** | `metricsData.total` `:1239`; `aum: totalAUM` `:1239`; `enterpriseQ0/Q1 = trendEnterpriseAt(dates.qN)` `:1231` (aum-timeseries) | mix | **MIXED / NO** (2 of 3 legs uncovered) |
| **CLIENT HOLDINGS** distribution | `AccountDistributionChart` `:1309,1351` + `AccountDistributionMetrics` `:1314,1356` | account-distribution (per-firm/global) | `distribution.by_model[k].{percentiles,median,histogram,account_count}`; `total.{...}` | group stats | **YES** |
| **AUA Daily Trend** chart | recharts (`activeTab==='growth' && timeSeriesData.aggregate` `:1426`) | **aum-timeseries** | `timeSeriesData.aggregate[].{period,aum,account_count}` (547 pts); `by_model{}` | columnar trend | **NO (A2)** |
| **as-of date** (header badge) | `PageHeaderCleanBadge` | aggregate-aua | `perFirmMdpfData.as_of_last` / `globalMdpfData.as_of_last` `:479` | — | **YES** |
| **DATA SOURCE** footer | inline | static text | "SmartX Connected / Non-Model AUA = Total AUA − SmartX Model AUM, rolled forward" | — | n/a |

**FE field consumption of aggregate-aua (the covered artifact):** `dates`, `model_aua`, `non_model_aua`, `partner_custody_total`, `opal_aggregate_aua` (global), `as_of_last`, `by_model.{display_name, cohort_class, model_value, account_count}`. **NOT consumed by ANY FE code (0 refs, comp-grep):** `cohort_provenance`, `source_vintage_last`, `sma_aua`. The FE type `MdpfPerFirmTimeSeries` (portal-proxy.ts:424) does not even declare `cohort_provenance`.

---

## PART 3 — Cross-reference: current SERVED shape vs REVAMP production (the non-overlap Andrew predicted)

### 3a. Artifact-level coverage
| artifact | served (today, json/…) | revamp (gold/mdpf_revamp/…) | gap |
|---|---|---|---|
| aggregate-aua-timeseries (A5/A6) | 429 dates, all fields | 427 canonical dates, all data fields byte-verified | `cohort_provenance` NOT produced (see 3b); axis 427 vs 429 (named date-delta) |
| account-distribution (A3/A7) | total + by_model stats | produced, parity-clean | none (1-day vintage drift only) |
| non_model_assets (A4) | 455-date v0_9 | 433-date 2-term (D-2 basis) | named D-2+F2 delta (ruled) |
| **aum-metrics (A1)** | period+dates{q0-3}+total+by_model[7]{model_name,aum,account_count,q0-3} | **NOT PRODUCED** | **whole artifact — header quarter tiles + AUMGrowthMetrics + FactorTilts** |
| **aum-timeseries (A2)** | aggregate[547]{period,aum,account_count}+by_model{5}+periods[547] | **NOT PRODUCED** | **whole artifact — AUA Daily Trend + enterprise-trend legs** |

### 3b. Field-level non-overlap within aggregate-aua (Andrew's `cohort_provenance` example — CONFIRMED)
- **`cohort_provenance`**: SERVED 49F = **82 non-None** real labels (`{'basis':'schwab_canonical_rederived','custody':'rollforward:<date>','model_1a':'measured','sma_1c':'interpolated_estimate','sma_1c_method':'bandaid_interp'}`). REVAMP 49F = **all None** — hardcoded `[None]*len(dates)` at `dim_mdpf_aggregate_aua_timeseries.py:656` (49F) / `:814` (inflection); global omits it entirely. **This is the trap in my earlier "byte-identical" — that compared two REVAMP re-stages, not revamp-vs-served.**
  - MECHANICAL: field present but unpopulated (placeholder) in revamp; served populates it.
  - DECLARATIVE: **consistent** — docstring `:16`, comment `:649`, meta `cohort_provenance_note` `:688`, co-sign item `:694` all declare None-by-design ("revamp uniformly real-measured; no interpolation/rollforward to label").
  - SEMANTIC: **FE-SAFE** — `cohort_provenance` has **0 FE consumers** (comp-grep portal/src), so all-None changes no rendering. It IS an information loss vs served (which dates were estimated/rolled-forward), but the revamp's methodology genuinely has no bandaid interpolation to label. **Disposition: co-sign decision, not an FE gate.**
- **`source_vintage_last`**: served + revamp both carry it; **0 FE consumers** — not rendered. (This is the "vintage block" I earlier flagged on the re-stage; FE-irrelevant.)
- **`sma_aua`**: declared-optional in the FE type, **collapsed into non_model at the producer, absent from served + revamp** — no gap.

---

## PART 4 — Uncovered surfaces + dispositions (the joint-census payload)

| item | what it feeds | current producer | disposition |
|---|---|---|---|
| **aum-metrics.json (A1)** | header quarter tiles + AUMGrowthMetrics cards + **FactorTilts** (cross-surface, `FactorTilts.tsx:83`) | legacy (json/portfolios/) | **MUST-MIGRATE or FE-rederive.** Spec §4 says A1 derives from A5/A6 (last + quarter-end); the revamp build did NOT emit it. A cross-surface consumer (FactorTilts) widens blast radius. |
| **aum-timeseries.json (A2)** | AUA Daily Trend chart + AUMGrowthMetrics enterprise-trend (`trendEnterpriseAt`) | **legacy-compat DAILY emitter** `build_legacy_compat_emit.py` on the `mdpf-daily-runner` EC2 (wired `mdpf-daily-dispatch.sh:358` + `legacy-emit-ssm.tf`) | **MUST-MIGRATE.** A whole parallel daily production path (v0_9 methodology, 547-day/legacy axis) the revamp does not replace. `dim_mdpf_non_model_assets.py:7` couples the revamp A4 to this legacy emitter — verify the coupling survives a repoint. |
| **MIXED-BASIS Global Total** | header Total AUA (global) | `ModelPortfolios.tsx:745`/`:763` builds Global enterprise Total = aum-timeseries(legacy model) + non_model_assets(revamp) | **RISK on repoint.** If aggregate-aua/A4 flip to revamp but aum-timeseries stays legacy, the Global Total mixes a legacy-model basis with a revamp-non_model basis. Must migrate A2 together, or re-derive the Total from revamp aggregate. |
| **cohort_provenance** | nothing (0 FE refs) | — | co-sign note only; NOT an FE gate. |
| FactorTilts (aum-metrics) | Factor Tilts page | legacy | separate-surface consumer of A1 — migrate A1 with it in mind. |

### Content gaps flagged by CTO (to reconcile — my independent read pending per-date grounding)
- (A) revamp **inflection model_value** post-onset None at feed-gaps vs served: NB served blends carry only ~38 non-None (shallow) while revamp blends carry ~421 (fuller) — direction is not uniformly "revamp-gap"; needs per-date, per-cohort diff before ruling. **OPEN.**
- (B) revamp **account_count** honest-None at published-only (all firms) = picket-fence where served was COMPLETE. **Open question CTO raised (I concur it must be answered first): was the SERVED completeness REAL historical data or a forward-fill?** If forward-fill, revamp honest-None is more correct, not a regression. **Ground the served source before ruling.**

---

## Verdict (this leg)
- **Header + AUA tab render from 5 artifacts; the revamp covers 3 (aggregate-aua, account-distribution, non_model_assets) and does NOT cover 2 (aum-metrics A1, aum-timeseries A2).**
- The 2 uncovered artifacts feed the **quarter-delta tiles, the AUM growth cards, the AUA Daily Trend chart, the global enterprise Total (mixed-basis risk), AND a second surface (FactorTilts).**
- `cohort_provenance` is a genuine served/revamp non-overlap but is **FE-unconsumed** -> co-sign note, not a gate.
- **A repoint that flips only the 3 covered artifacts leaves the page mixed-source and the Global Total mixed-basis.** A1+A2 are the must-migrate items; the legacy-compat daily EC2 emitter is the surface to retire.

**Reconcile with CTO's parallel FE-consumption census -> one authoritative list for Andrew.**
