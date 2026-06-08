# Brief 3 — Cottonwood Capital Advisors (COT): bd-pipeline Deep Dive + Medallion Port Plan

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-08
**Project (proposed):** ADVI_COTETL
**Companions:** Brief 1 (HAR auth / DataMining API), Brief 2 (COT transactions field population)
**Subject pipeline:** bd-pipeline (49 Financial), gold runner `bd-gold-layer-runner` (`i-01003b035d2988dfb`), data plane `s3://opal-data-bd`

---

## 0. Headline finding

The bd-pipeline is the right template to port, and the port is **far cheaper than a rewrite** for three reasons discovered in the deep dive:

1. **Bronze already eats exactly the artifact COT produces.** bd-pipeline bronze ingests BD **DataMining xlsx exports** (`TXN_DAILY_*.xlsx` + `ALLOC_DAILY_*.xlsx`, including the same `Timestamps` metadata sheet found in `CW_Transactions_Rich`). COT's API-first ingest (Brief 1) lands the *same shape* — the bronze converters port directly.
2. **The platinum layer is already firm-parameterized.** `bd-portal-publisher` reads `FIRM_ID` / `FIRM_NAME` / `INPUT_BUCKET` / `OUTPUT_BUCKET` from environment variables (defaulting to `49financial` / `opal-data-bd`). A COT publisher is a **config-only** instantiation. This confirms Andrew's "platinum virtually identical."
3. **Silver is firm-agnostic by design** (Rule 17: dedup + type-standardize only) — it ports as-is, re-pointed to the COT data plane.

The real porting work concentrates in **two seams**: (a) the bronze ingest mechanism (new — the API-first auth/refresh/landing infra, owned by AE `0.6.2_AE_PartnerETL`), and (b) firm-specific configuration in the gold layer (the D_* `FIRM_ID` hardcodes + the Lusha-enriched advisor/office mapping). Everything between is parameterize-and-repoint.

---

## 1. bd-pipeline medallion architecture (as-built)

```
                         ┌─────────────── BRONZE ───────────────┐
  BD DataMining exports → forwardfill_v2/transactions/TXN_DAILY_*.xlsx ─┐
  (today: landed to S3)   forwardfill_v2/allocations/ALLOC_DAILY_*.xlsx ┤→ convert_daily_*_to_parquet.py
  Schwab custodian      → sync_schwab_onedrive_to_s3 + convert_schwab_* ┘   (7-day dedup, Timestamps→watermark)
                                              │
                         ┌─────────────── SILVER ───────────────┐  (Rule 17: dedup + type-standardize ONLY)
                         silver/daily_transactions/, silver/daily_allocations/, silver/transactions/ (full TS 2020+)
                         silver/assets (build_bd_assets_dim), prices (yfinance/interpolated), fees
                                              │
                         ┌─────────────── GOLD ─────────────────┐  (14-phase parallel DAG; gold_dispatch.sh)
   A_ dimensions   A_00 accounts_dim · A_01 advisor_assignments · A_02 fee_rate · A_03 positions_cube · A_04 client_dim
   B_ holdings     B_00 canonical_holdings · B_01 holdings_lots · B_01b classify_new_secs · B_02 canonical_lots · B_03 account_gains
        prices     S_00 build_canonical_prices_v2
   C_ analytics    C_00 perf · C_01 canonical_nna · C_02 client_perf · C_03 account_perf · C_04 validate_aua
                   C_05 tax_liability · C_06 client_mix_timeseries · C_07 advisor_attribution · C_08 fee_efficiency
   D_ portal-art   D_00 portal_aggregates · D_00b timeseries · D_00c leaderboard · D_01 partner_analytics
                   D_02 advisor_client_detail · D_03 composition · D_04 client_portal_summary
   E_ diagnostics  (NOT in nightly chain — audits/probes)
                                              │
                         ┌─────────────── PLATINUM ─────────────┐  (publisher Lambdas, S3-event-triggered)
   bd-portal-publisher (header_metrics, timeseries, views) · bd-portal-advisor-publisher (advisors/{id}/book.json)
   bd-client-detail (clients/{key}.json) · opal-partners-data (scoped dynamic API) → CloudFront → portal
```

### 1.1 The nightly chain (from `gold_dispatch.sh`)

`CHAIN_FULL = DIMENSIONS → CANONICAL → DOWNSTREAM`, run as a validated 14-phase DAG:
- **DIMENSIONS:** `A_00 A_01 A_02 A_03 A_04` (A_00/A_02/A_03 parallel, then A_01/A_04)
- **CANONICAL:** `B_00 → B_01 → B_01b → B_02 → B_03 C_00 C_01 C_02 C_04` (B_00→B_01→B_01b serialized: B_01 reads B_00's canonical/holdings via dynamic f-string read invisible to comp-pipescript; B_01b classifies new securities into DynamoDB `bd-securities` before B_02; memory-contention-driven serialization — concurrent B_00‖B_01 stacked ~1.38 TB RSS on a 128 GB box)
- **DOWNSTREAM:** `C_03 C_05 C_07 C_06 C_08 D_00 D_00b D_00c D_01 D_02 D_03 D_04`

Triggered nightly via `bd-gold-trigger` Lambda → boots `bd-gold-layer-runner` EC2 → `run_gold_layer.sh` → `gold_dispatch.sh --chain full`. On completion writes `gold/meta/pipeline-complete.json`, whose S3 ObjectCreated event fires the publisher Lambdas (platinum).

### 1.2 Data-source philosophy (critical for COT)

- **`silver/transactions/` (full time series 2020-present) is the PRIMARY source** for dimensions, NNA, flows, and the positions cube. Transactions carry units + price + flow classification.
- **`silver/allocations/` (daily snapshots, Jan-2026+) is ENRICHMENT** — account_type / registration_type labels, and the market-value AUA snapshot used for cross-validation (A_03 positions × canonical_prices reconciles against allocations AUA). Allocations are a *snapshot, never a time series* (A_00 docstring: "NEVER use allocation market_value for time-series computation").
- **Prices** come from `build_canonical_prices_v2` (yfinance/yahoo for public securities + interpolation + scoped overrides). Firm-agnostic — public market data.

**COT implication (ties to Brief 2 §5):** COT must land **both** a Transactions export (`queryTypeId=2`, have it) **and** an Allocations/Holdings export (`queryTypeId=1`, available per Brief 1 §3.1). Transactions alone cover NNA/flows/geo/advisor cohorts; allocations are needed for the AUA snapshot enrichment + cross-validation.

---

## 2. Firm-scoping analysis — what's parameterized vs. hardcoded vs. firm-specific

This is the port-effort map. Three categories:

### 2.1 Already parameterized (ports by env-var) ✅
| Component | Mechanism |
|---|---|
| `bd-portal-publisher` (+ sibling publishers) | `FIRM_ID`, `FIRM_NAME`, `INPUT_BUCKET`, `OUTPUT_BUCKET` via `os.environ.get(..., '49financial'/'opal-data-bd')` |
| `C_06 client_mix_timeseries` | `FIRM_ID = os.environ.get('O6B_FIRM_ID', '49financial')` |

### 2.2 Hardcoded constant — needs the env-var treatment (mechanical) ⚠️
| Script | Line | Hardcode |
|---|---|---|
| `D_00 portal_aggregates` | 77–78 | `FIRM_ID='49financial'`, `FIRM_NAME='49 Financial'` |
| `D_00b portal_timeseries` | 57–58 | same |
| `D_00c portal_leaderboard` | 52 | `FIRM_ID='49financial'` |
| `D_01 partner_analytics` | 2516–17 | `'firm_id':'49financial'`, `'firm_name':'49 Financial'` |
| `D_02 advisor_client_detail` | 82 | `FIRM_ID='49financial'` |

**Fix:** promote these constants to `os.environ.get('FIRM_ID', '49financial')` (the C_06/publisher pattern). Single small PR across 5 D_* scripts. The compute is firm-agnostic; only the label + S3 path key change.

### 2.3 Firm-specific configuration + data — the real porting cost 🔨
| Asset | What it is | COT port |
|---|---|---|
| `config/office_mapping/*.csv` | 49F advisor registry + advisor→office rollups, **Lusha-enriched** (architect/implementor/consultant/local_ops). Drives advisor attribution + advisor-dimension analytics. | COT needs its **own** advisor registry + office rollups built from COT's BD role outputs + a fresh Lusha enrichment pass. Methodology + code port; the *data* is firm-specific and must be rebuilt. |
| `C_07 advisor_attribution` | '49F House' placeholder logic, architect/implementor pairing | COT's advisor placeholder + org structure differs — re-characterize from COT data (COT's DataMining export carries advisor/rep dims; note COT's `DST Rep Name` is 99% "No RepName Assigned" — **advisor attribution for COT may be thin/absent**, a real open question — see §5) |
| `s3://opal-data-bd` (single bucket) | 49F single-tenant data plane (44 references in gold) | COT needs its own data plane (`opal-data-cot` proposed) — clean isolation, independent lifecycle/schedule, zero cross-firm blast radius |
| Scoped price overrides (`inject_scoped_overrides`) | Manual per-asset price corrections (49F holdings) | COT builds its own as needed; starts empty |
| DynamoDB `bd-securities` | Shared securities classification cache | Likely **shareable** across firms (securities are public) — reuse, don't clone |

---

## 3. The central architectural decision: per-partner data plane + shared parameterized code

Two models were considered:

| Model | Description | Verdict |
|---|---|---|
| **A. Multi-tenant single pipeline** | One runner, firm-partitioned S3 prefixes, union all firms, partition by `firm_id` | Rejected for v1 — couples firms' schedules/blast-radius, requires invasive partitioning of mature single-tenant scripts, complicates per-firm SLAs |
| **B. Per-partner data plane + shared code** ✅ | Same medallion **code** (one repo, parameterized), but each partner gets its **own** S3 bucket, gold runner, publisher Lambda env, and firm-config directory | **Recommended.** Matches the per-partner AE (`0.6.2_AE_PartnerETL`) provisioning, the already-env-parameterized publisher, and the C_06 env pattern. DRY code, isolated data/compute. |

**Recommendation: Model B.** The bd-pipeline becomes a *template* instantiated per partner. COT = `opal-data-cot` + a COT gold runner (or a shared partner-ETL runner with per-firm env) + `bd-portal-publisher` deployed with `FIRM_ID=cottonwood` + a `config/cot/office_mapping/` directory. The code edits required to support this are exactly §2.2 (de-hardcode the 5 D_* `FIRM_ID`s) — after that, the same gold scripts run for any partner by env + config.

This also keeps the door open to later consolidation (Model A) without rework: parameterizing FIRM_ID is the prerequisite for both.

---

## 4. Port plan by layer

| Layer | Strategy | Effort | Owner | Notes |
|---|---|---|---|---|
| **Bronze** | **Build new** (API-first per Brief 1) + **reuse converters** | High (infra) / Low (converters) | AE 0.6.2 (auth/refresh/landing infra) + DS (pull logic) | Auth bootstrap (OIDC session → Secrets Manager, Inflection/YCharts pattern) is the main build. Once exports land as `TXN_DAILY_*.xlsx` / `ALLOC_DAILY_*.xlsx` in `opal-data-cot/forwardfill_v2/`, the existing `convert_daily_*_to_parquet.py` converters port directly (re-point bucket). |
| **Silver** | **Port as-is**, re-point prefixes | Low | DS | Rule-17 firm-agnostic dedup/type-standardize. `build_bd_assets_dim`, prices, ticker-mapping all reusable. |
| **Gold A/B/C** | **Port + parameterize** | Medium | DS | Firm-agnostic compute. Tasks: (a) env-var FIRM_ID where hardcoded; (b) re-point S3 bucket; (c) rebuild `office_mapping` for COT (Lusha pass); (d) confirm positions cube (A_03) + canonical_prices work on COT assets; (e) re-characterize advisor attribution (C_07) for COT org structure. |
| **Gold D (platinum-producing)** | **Port + de-hardcode FIRM_ID** | Low | DS | §2.2 — 5 scripts, promote constant→env. Artifact shapes identical. |
| **Platinum (publishers + portal)** | **Config-only instantiation** | Low | AE 0.6.2 + DE/DT | Deploy `bd-portal-publisher` et al. with COT env (`FIRM_ID=cottonwood`, COT buckets). Portal scoped-API + a COT tenant in the federated view (DE/DT). |

### 4.1 Proposed build sequence (phasing)

1. **P0 — Infra + auth (AE 0.6.2):** `opal-data-cot` bucket; Secrets Manager `blackdiamond/cot/*`; the OIDC session-refresh Lambda/VM (Inflection `inf-jwt-trigger` analog); IAM; contract-drift monitor (Standard §3.6).
2. **P1 — Bronze (DS + AE):** API-first pull of COT Transactions (`queryTypeId=2`) + Allocations (`queryTypeId=1`) → land as `TXN_DAILY_*`/`ALLOC_DAILY_*` xlsx → port the bronze converters → `silver/`.
3. **P2 — Silver (DS):** re-point + run the silver converters; build COT assets dim + prices.
4. **P3 — Gold dimensions + canonical (DS):** A_/B_/C_ — parameterize FIRM_ID, rebuild COT `office_mapping`, validate positions cube + NNA + AUA against the manual export as ground truth.
5. **P4 — Gold portal-artifacts (DS):** de-hardcode D_* FIRM_ID; run D_ chain; validate artifact shapes match 49F structurally.
6. **P5 — Platinum (AE + DE/DT):** deploy COT publishers (config-only); wire portal COT tenant; FE smoke.

### 4.2 Validation anchor

The **manually-built `CW_Transactions_Rich` export is the bronze ground-truth oracle** — the API-first pull must reproduce it byte-for-content. Downstream, 49F's existing gold artifacts are the *structural* template (shapes must match); COT's *values* validate against COT's own BD reports (the AUA/NNA the operator can pull by hand from BD).

---

## 5. Open questions / risks for the PRD

1. **Advisor attribution thinness.** COT's transactions show `DST Rep Name` 99% "No RepName Assigned" (Brief 2). bd-pipeline's advisor analytics (C_07, advisor leaderboards, D_00c, advisor `book.json`) lean heavily on the 49F architect/implementor/office structure. **COT may not have a populated advisor dimension** — if so, the advisor-dimension analytics (leaderboards, advisor cohort, attribution) may be N/A for COT v1, or sourced differently. **Must confirm with Andrew/COT what advisor/rep data exists.** This is the single biggest scope uncertainty.
2. **Allocations/Holdings export availability + history.** bd-pipeline allocations start Jan-2026 (snapshot, no backfill). COT's AUA cross-validation + positions valuation depend on landing the Allocations export; its date depth determines how far back COT AUA history can go.
3. **Custodian concentration.** COT is 98.8% Fidelity IWS (Brief 2); 49F's pipeline has Schwab-specific bronze paths (`convert_schwab_*`, OneDrive sync). COT likely needs **none** of the Schwab custodian path — confirm COT is pure-BD-DataMining (simpler) vs. needing a custodian feed.
4. **NNA semantics.** COT's onboarding-heavy window (Transfer In 47.5%) requires **institutional NNA** classification (Brief 2 §4, Inflection precedent) — port the transaction-classified NNA (C_01), not a cash-only definition.
5. **Office/geo mapping (Lusha).** Rebuilding COT's advisor→office mapping needs a Lusha enrichment pass + cache; budget for it. Geo analytics itself is fine (client state/city are real, 87% TX).
6. **JSON results endpoint** (Brief 1 §3.2) — if BD exposes structured results, bronze skips xlsx parsing entirely. Probe at P1.

---

## 6. Bottom line

bd-pipeline is a mature, well-structured medallion that ports to Cottonwood as a **per-partner instantiation of shared, parameterized code over an isolated data plane** (Model B). Silver and platinum are near-free (firm-agnostic / already env-parameterized); gold ports with a small FIRM_ID de-hardcoding PR plus a firm-specific config rebuild (advisor/office mapping); bronze is the one genuinely new build — the API-first ingest of Brief 1, owned by AE `0.6.2_AE_PartnerETL`. The largest open scope question is whether COT carries a usable advisor dimension at all (§5.1). Recommend the CTO instantiate PRD **ADVI_COTETL** structured on the P0–P5 phasing in §4.1, with §5 as the named risk register.
