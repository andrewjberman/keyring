# YALP_MDSRC WS-3 — Client-Based / Client-Facing Data Domain Audit

| | |
|---|---|
| **TO** | YALP_MDSRC.003.ds-ws3-client-facing-data-domain-audit |
| **Workstream** | WS-3 — Client-Based / Client-Facing Data |
| **Author** | 0.4.0_DS_ClientPlatform (base lane) |
| **Date** | 2026-05-20 |
| **PRD** | docs/architecture/YALP_MDSRC.md v0.2 (§4 WS-3, §6 Q4, §7) |
| **Status** | COMPLETE — audit deliverable; RAVC2 to 2.0.0_SA_COO CC 1.0.0_SA_CTO |
| **Scope** | Audit-only. v0.2 authorizes NO code/Terraform/portal change. |

This brief is the WS-3 slice of the YALP_MDSRC migration-candidate audit: model-portfolio
**performance** sourcing (the §4 seam with WS-2), the SmartX backend, and the client-tied
portal surfaces. It answers PRD Q4 (model-portfolio performance — YCharts vs SmartX vs
`model.pkl`).

---

## 1. Method & evidence base

| Evidence | Source |
|---|---|
| SmartX legacy scrape pipeline | `data/smartx/SMARTX_BIBLE.md`, `data/smartx/docs/SMARTX_API_DOCUMENTATION.md` |
| SmartX REST API surface | `docs/briefs/smartx-per-model-availability-matrix-20260515.md` (SXPL_RESTIN.001 — 13-endpoint x 7-model probe), MDPF DS~B coordination (§7) |
| YCharts `/model_portfolios/*` | `C:\Users\AndrewBerman\Downloads\ycharts.com.har` (92 MB, 1,894 entries) — deep parse; WS-1 live-session test `docs/briefs/mdsrc-ycharts-live-session-test-20260520.md` |
| yang `model_pkl` performance surfaces | `infra/aws/lambda/v2_portal/yang_pipeline/PORTAL_DATA_FLOW.md`; live artifacts `model_portfolio_benchmarks.json`, `model_portfolio_timeseries.json` |
| Portal serving paths | `comp-routes behaviors`; `portal/src/api/portal-proxy.ts` fetch-path grep |

Compiler-tools results are in the session log Compiler Tools section. Honest scope note (PRD §5):
the YCharts side is an external system — no comp-* tool applies; evidence is the HAR + the WS-1
live-session capture. The SmartX gold-tier is off the comp-pipescript graph (BD-gold IDs only) —
direct source read substituted.

---

## 2. The two SmartX paths (critical distinction)

"SmartX" in the Opal codebase is **two separate integrations** against the same vendor. Conflating
them is the central audit hazard — they expose different data and have different operational shape.

### 2.1 Legacy `data/smartx/` scrape pipeline — AUM / allocation only

- **Mechanism:** EC2 Docker + Playwright scrapes CSVs from the SmartX *advisory portal*
  (`portal.managedaccounts.io`); Lambda `opal-smartx-ingestion-pipeline` consolidates to Parquet
  and emits portal JSON. EventBridge Mon-Fri 09:00 ET.
- **Data:** per-account allocation snapshots — `AllocationId`, `EndMarketVal`, `ModelName`,
  `Period` (YYYYMM monthly), `AllocationStatus`, `Custodian`. ~6,300 active accounts, 5 models,
  ~$1.1B. **Market value only — no return / TWR / performance series.**
- **Read API:** `jpn26ozdgg.execute-api.us-east-1.amazonaws.com/prod/smartx/allocations*` —
  built for Excel/Power Query.
- **Portal outputs:** `aum-timeseries.json`, `aum-metrics.json`, `account-distribution.json`,
  `non_model_assets.json`, `model_portfolios/views/*`.

### 2.2 SmartX REST API `api.smartxadvisory.com/api/3.1` — incl. performance

- **Mechanism:** direct REST, ROPC JWT (`mint_token()` reads `smartx/credentials/*` from
  Secrets Manager, POSTs `identity.smartxadvisory.com/connect/token`; opal7 Manager-role creds).
  This is MDPF_ASSETS's WS-B feeder path (`data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py`)
  and the SXPL_RESTIN project's domain — distinct from §2.1.
- **Data — and this is the Q4 crux: SmartX is NOT performance-blind.** Probe-confirmed
  (SXPL_RESTIN.001, all 7 Opal models):

  | Endpoint | Grain | Carries |
  |---|---|---|
  | `enterprises/aum?modelid=` | daily time series (~422 pts) | `closingEquity` per `performanceDate` — daily model value |
  | `models/{modelId}/statistics` | live snapshot | `returns.{today,mtd,qtd,ytd}` (dollar + percent) |
  | `reportedmodels/{rmid}/historicalperformance` | time series | `performanceValue` per date — model-level performance series |
  | `performance.smartxadvisory.com/models/performance` | snapshot | deep risk/return stats |
  | `reportedmodels/{rmid}/holdings` | current snapshot | per-symbol weights |

- **Coverage:** all 7 Opal models — the 5 portal models (UST/ST/INT/LTC/LTA) **plus** Opal
  Dividend Income + Pathfinder Focused Opportunities. Enterprise: Opal Capital LLC.
- **Auth:** proper machine API auth (client-credential ROPC JWT). No browser session, no WAF,
  no single-concurrent-session limit.

---

## 3. YCharts `/model_portfolios/*` — characterized

HAR deep-parse (entries filtered to `ycharts.com/model_portfolios`, trackers/JS-bundles excluded):

| Endpoint | Method | Response | What it is |
|---|---|---|---|
| `/model_portfolios/` | GET | JSON 6.3 KB | Portfolio **directory listing** — query params `portfolioType={model_portfolio,client_portfolio,household_portfolio,blended_benchmark}`, `owner`, `editState`, `name=` search, `sortColumn` |
| `/model_portfolios/list/` | GET | HTML 61 KB | The portfolio-list **web page** |
| `/model_portfolios/collection_status` | GET | JSON 3.3 KB | Collection/refresh status |
| `/model_portfolios/transition_analysis/list` | GET | JSON `[]` | Transition-analysis list (empty in capture) |

**Finding:** YCharts `/model_portfolios/*` is a **portfolio-construction tool** — a directory of
user-built / shared portfolios with `editState` (draft/completed), an owner model, and a
name-search. It is NOT a feed of Opal's live managed model-portfolio performance. YCharts would
only carry Opal's model performance if an analyst manually rebuilt each Opal model inside the
YCharts seat — a manual-maintenance burden, and still a *reconstruction*, not the system of record.

**WS-1 corroboration** (`mdsrc-ycharts-live-session-test-20260520.md` §4): under a valid
authenticated YCharts session, `/model_portfolios/` and `/model_portfolios/collection_status`
JSON both return **HTTP 403 "You are signed out"** while `/indices/table_data` JSON returns 200
real data in the same session. Most probable cause: the `/model_portfolios/*` JSON API is
subscription-tier / feature-entitlement gated on the current seat (consistent with WS-1 Finding
F3 — YCharts features are plan-gated with inconsistent error messaging). So the endpoint class
is, on the current seat, **both the wrong kind of data and not reachable**.

---

## 4. yang `model.pkl` — model-portfolio performance content

The yang-pipeline `model_pkl` (weekly manual Bloomberg-exported pickle, "Opal model-portfolio
outputs — proprietary", PRD §2.1) is the **current** source of the portal's model-portfolio
performance surfaces. Two live artifacts (both generated by `yang-model-portfolio-benchmarks`,
fed by `data_pkl + model_pkl`):

- **`json/benchmarks/model_portfolio_benchmarks.json`** — per model (UST/ST/INT/LTC/LTA), per
  period (1D/WTD/MTD/1M/QTD/1Q/YTD/1Y/Since Inception): `model` (the model's own return),
  `index_benchmark`, `etf_benchmark`, `index_spread`, `etf_spread`, `model_volatility`.
  `inception_date` 2024-04-30.
- **`json/benchmarks/model_portfolio_timeseries.json`** — daily series per (date, model_code):
  `model_return`, `benchmark_return`, `rfr`. `rfr_tenors` per model.

The `model` / `model_return` fields are the **WS-3 surface** (model-portfolio performance
sourcing). `index_benchmark` / `etf_benchmark` / `benchmark_return` / `rfr` are the **WS-2
surface** (benchmark/analytics) — same artifacts, column-level seam (see §7, §8).

`model.pkl` performance characterization: it is Opal's **proprietary computed** model-return
series — the model as Opal *constructs and measures* it (model design returns), refreshed weekly
by manual Bloomberg pickle upload. It is not the realized return of the actual managed accounts;
that is what SmartX holds.

---

## 5. Q4 — canonical source for model-portfolio performance

**Three candidates, adjudicated:**

| Source | Verdict | Reasoning |
|---|---|---|
| **YCharts `/model_portfolios/*`** | **REJECTED** | Wrong data kind (portfolio-construction directory, not a managed-model performance feed) AND not reachable on the current seat tier (403, §3). Would require an analyst to manually rebuild Opal models in YCharts + a tier upgrade. |
| **yang `model.pkl`** | **RETAIN as the proprietary/design view** | Opal's own computed model-return series. Authoritative for "the model as Opal designs it." But: weekly manual Bloomberg upload — not a daily automated pull, and not the realized managed-account return. |
| **SmartX REST API `api/3.1`** | **RECOMMENDED as the canonical live source** | The system of record for the actual managed Opal model portfolios. `reportedmodels/{rmid}/historicalperformance` + `models/{id}/statistics` + `performance.smartxadvisory.com/models/performance` give a daily-automatable performance series for all 7 models, with proper machine API auth (no WAF, no session-eviction). Already a live, trusted Opal integration (MDPF_ASSETS WS-B). |

**Recommendation (Q4):** **SmartX REST API is the canonical source for the portal's
model-portfolio *performance* surfaces** (`model` / `model_return`), superseding the weekly manual
`model.pkl` for those fields. Rationale: (1) it is the realized performance of the actual managed
accounts — the system of record; (2) proper API auth, daily-automatable, all 7 models; (3) it is
already a live Opal integration with a probed schema (SXPL_RESTIN.001) and the active SXPL_RESTIN
project building the pull. `model.pkl` is **retained** as the Opal-proprietary *design/computed*
view — recommend WS-5 / v0.3 decide whether the portal shows realized (SmartX) or design
(`model.pkl`) model returns, or both side-by-side; that is a product call, not an audit call.

**Caveats for v0.3 (do not pre-decide — PRD §6):**
- SmartX `reportedmodels/{rmid}/historicalperformance` cadence (daily/weekly/monthly) is not
  confirmed from shape alone (SXPL_RESTIN.001 caveat) — v0.3 modeling must confirm against real
  values, and confirm `performanceValue` units / sign convention.
- `enterprises/aum.closingEquity` is a **value** series — deriving a true TWR requires
  flow-adjustment; `historicalperformance` / `statistics.returns` are the return-native fields.
- Methodology reconciliation: SmartX realized return vs `model.pkl` design return may diverge
  (fees, cash drag, trade timing). If the portal switches source, expect a one-time level shift —
  flag to DE/RD at v0.3.
- This is a **performance** recommendation only. SmartX-as-AUA (MDPF) is a separate dimension and
  is unaffected (§7).

---

## 6. WS-3 migration-candidate matrix slice

Common 14-column schema (agreed with WS-1/WS-2). Classification vocabulary: YCharts-replaceable /
Bloomberg-pkl-only / hybrid / proprietary / SmartX-sourced.

| surface_id | portal_page | component | surface | json_artifact | serving_path | current_source | refresh_cadence | data_class | ycharts_endpoint | ycharts_coverage | classification | evidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WS3-MP-01 | Model Portfolios | ModelPortfolioBenchmarks | model-portfolio performance (`model` field, 9 periods) | json/benchmarks/model_portfolio_benchmarks.json | /api/public/json/benchmarks/model_portfolio_benchmarks.json | yang `model_pkl` | weekly (manual pkl) | model-portfolio performance | none usable | 403 / un-entitled + wrong kind | **SmartX-sourced** (recommend) | §3,§4,§5; SXPL_RESTIN.001 | WS-2/WS-3 seam — `model` col WS-3; benchmark cols WS-2 |
| WS3-MP-02 | Model Portfolios | ModelPortfolioTimeseries | model daily return series (`model_return`) | json/benchmarks/model_portfolio_timeseries.json | /api/public/json/benchmarks/model_portfolio_timeseries.json | yang `model_pkl` | weekly (manual pkl) | model-portfolio performance | none usable | 403 / un-entitled | **SmartX-sourced** (recommend) | §4,§5; portal-proxy.ts:720 | `model_return` WS-3; `benchmark_return`/`rfr` WS-2 |
| WS3-SX-01 | Portfolios / AUM | AUMTimeSeries | model AUM daily series | json/portfolios/aum-timeseries.json | /api/general/portfolios/aum-timeseries.json | SmartX legacy scrape | daily Mon-Fri 09:00 ET | client-account AUM | n/a (not market data) | n/a | **SmartX-sourced** (already) | §2.1; SMARTX_BIBLE.md | Client-account backend — not a YCharts candidate |
| WS3-SX-02 | Portfolios / AUM | AUMMetrics | latest AUM + quarterly change | json/portfolios/aum-metrics.json | /api/general/portfolios/aum-metrics.json | SmartX legacy scrape | daily Mon-Fri 09:00 ET | client-account AUM | n/a | n/a | **SmartX-sourced** (already) | §2.1 | — |
| WS3-SX-03 | Portfolios / AUM | AccountDistribution | account-size bell curve | json/portfolios/account-distribution.json | /api/general/portfolios/account-distribution.json | SmartX legacy scrape | daily Mon-Fri 09:00 ET | client-account distribution | n/a | n/a | **SmartX-sourced** (already) | §2.1 | — |
| WS3-SX-04 | Portfolios / AUM | NonModelAssets | non-model (non-SmartX) AUM | json/portfolios/non_model_assets.json | /api/general/portfolios/non_model_assets.json | BD `certified_aua` - SmartX model AUM (Lambda Step 6) | daily | client-account AUM (derived) | n/a | n/a | **proprietary** (derived) | §2.1; SMARTX_BIBLE.md Stage 3 | Enterprise - Model residual; 49F-specific |
| WS3-SX-05 | Model Portfolios (detail) | ModelPortfolioViews | per-account allocation detail | json/model_portfolios/views/* | /api/public/json/model_portfolios/views/* | SmartX legacy scrape | daily Mon-Fri 09:00 ET | client-account allocation | n/a | n/a | **SmartX-sourced** (already) | §2.1 | by_assetclass/ + by_period/ |

**Slice read:** No WS-3 surface is YCharts-replaceable. The model-portfolio *performance*
surfaces (WS3-MP-01/02) are recommended to move from manual weekly `model.pkl` to the SmartX
REST API (a manual->automated upgrade, source change not a YCharts migration). The SmartX
client-account surfaces (WS3-SX-*) are already SmartX-sourced and structurally not YCharts
candidates (client-account data is not market data). The migration-candidate count for the
YCharts question in the WS-3 domain is therefore **zero** — but WS-3 surfaces a distinct,
high-value automation win: model-portfolio performance manual-pkl -> SmartX-REST.

---

## 7. MDPF_ASSETS coordination (AC4)

Mandatory base-lane <-> ~B-lane coordination (PRD §7). MCP thread with `0.4.0_DS_ClientPlatform~B`
(MDPF lane), COO~B pre-threaded. DS~B replied in full from MDPF_ASSETS.027 + SXPL_RESTIN work
(no new investigation needed). Consumed:

- **MDPF's SmartX integration** (WS-B feeder) pulls 49F Opal-**model AUA** — per-model allocation
  roster + holdings composition. Coverage: 49F only, model/SMA book (7 SmartX-mapped models = the
  5 core + 2 SMAs), ~$1.37B; no non-model (1b) visibility. Daily snapshot via the mdpf chain.
- **API surface:** `api.smartxadvisory.com/api/3.1`, ROPC JWT — distinct from the legacy
  `data/smartx/` scrape pipeline. (This is §2.2.)
- **DS~B confirmed SmartX is NOT AUA-only** — the REST API exposes the performance endpoints in
  §2.2; MDPF's feeder simply does not consume them (WS-B is AUA/membership only). This corrected
  an initial WS-3 read that would have ruled SmartX out as AUM-only.
- **MDPF model-AUA architecture:** MDPF is an AUA/balance architecture with **no performance
  dimension** — WS-B (SmartX)->49F model+SMA AUA, WS-E->49F non-model, WS-C->Inflection,
  WS-A aggregates. It answers "how much AUA," not "what return."

**Reconciliation:** the Q4 recommendation (SmartX REST as the model-portfolio *performance*
source) does **not** contradict MDPF. Performance and AUA are orthogonal dimensions of the same
SmartX API; MDPF consumes the AUA endpoints, WS-3's recommendation consumes the performance
endpoints. No architectural conflict; the two integrations share the auth pattern (ROPC JWT,
Secrets Manager `smartx/credentials/*`) — a v0.3 reuse opportunity, not a collision.

Canonical MDPF/SmartX references (cited): `docs/briefs/smartx-per-model-availability-matrix-20260515.md`
(SXPL_RESTIN.001), `docs/briefs/mdpf-assets-027-smartx-49f-coverage-probe-20260520.md`,
`docs/briefs/mdpf-assets-007-wsb-49f-smartx-phase0-feasibility-20260518.md`,
`docs/briefs/mdpf-assets-011-smartx-per-account-model-membership-probe-20260518.md`.

---

## 8. WS-2 <-> WS-3 Model Portfolios seam coordination (AC5)

MCP thread with `0.2.0_DS_PortfolioAnalytics` (WS-2). Seam cut agreed both ways:

- **WS-2** owns the Model Portfolios *analytics/benchmark* surfaces — benchmark returns,
  model-portfolio benchmarks (the benchmark columns), ETF returns, peer performance.
- **WS-3** owns model-portfolio *performance sourcing* — the `model` / `model_return` columns.

`model_portfolio_benchmarks.json` and `model_portfolio_timeseries.json` are **shared artifacts
with a column-level seam**: `model` / `model_return` = WS-3; `index_benchmark` / `etf_benchmark`
/ `benchmark_return` / `rfr` = WS-2. Both slices co-cite these artifacts with the column split
noted (WS-2 slice row WS2-MP-03 records the same split — confirmed resolved by WS-2). No surface
is double-audited or dropped; WS-5 reconciles at synthesis.

---

## 9. Open items / handoff to WS-5

- **Q4 answered:** SmartX REST API recommended as the canonical model-portfolio performance
  source; `model.pkl` retained as the proprietary design view. Realized-vs-design display is a
  product call for v0.3 (§5).
- **Q1 (official API vs scrape):** for the WS-3 domain this is moot — SmartX REST is already an
  official, key-authed API (ROPC JWT); no scrape decision. YCharts `/model_portfolios/*` is
  rejected regardless of Q1.
- **Q7 (ToS):** not triggered in the WS-3 domain — SmartX REST is a contracted Opal integration;
  no YCharts extraction is recommended for WS-3 surfaces.
- **v0.3 inputs:** confirm `historicalperformance` cadence + units; decide realized vs design
  model returns; reuse the SmartX ROPC-JWT auth pattern (shared with MDPF WS-B / SXPL_RESTIN);
  expect a one-time level shift if the portal source switches `model.pkl` -> SmartX.
- **SXPL_RESTIN overlap:** the SmartX REST integration is already an active project. WS-5 should
  note that a v0.3 "model-portfolio performance from SmartX REST" implementation likely
  co-scopes with / reuses SXPL_RESTIN rather than standing up a parallel SmartX pull.

---

## 10. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — YCharts `/model_portfolios/*` + SmartX backend + `model.pkl` characterized | MET — §2,§3,§4 |
| AC2 — canonical-source recommendation (Q4), reconciled with MDPF | MET — §5,§7 |
| AC3 — client-tied / per-account surfaces inventoried + classified | MET — §6 matrix slice (WS3-SX-01..05) |
| AC4 — MDPF_ASSETS coordination evidence | MET — §7 (MCP thread, 4 briefs cited) |
| AC5 — WS-2 seam coordination evidence | MET — §8 (MCP thread, column-seam agreed) |
| AC6 — committed brief + matrix slice + session log + RAVC2 | this brief + session log; RAVC2 on commit |
