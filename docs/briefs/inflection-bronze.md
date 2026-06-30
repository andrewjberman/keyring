# Brief: Inflection — BRONZE / Ingestion layer (end-to-end audit)

**Author:** 3.0.0_SA_CVO (Andrew-direct, ADVI_BREAKS unified-flow audit) | **Date:** 2026-06-30
**Scope:** Inflection (Orion) ingestion only. Silver = `inflection-silver`; Gold+portal = `inflection-gold`.
**Purpose:** Ground the ingestion layer end-to-end so a single unified flow can be designed without guessing. All facts grounded vs live source / Terraform / S3 (not self-report).

---

## 1. Two source systems

| Source | Base URL | Auth | Ingest vehicle |
|---|---|---|---|
| **Orion Cloud REST** (the backbone) | `https://api.cloud.orionadvisor.com` | Orion JWT in SM `orion/jwt/current` (also mirrored `s3://opal-data-inf/orion/jwt/current.json`); refresh needs a **human OTP** written to `s3://opal-data-inf/otp/` via `inf-otp-relay` | 9 dimension pulls (Lambda + EC2-inline) |
| **Orion Eclipse** (NOT load-bearing) | `https://www.orioneclipse.com` | Eclipse JWT `orion/eclipse_jwt/current`, derived from Orion JWT via `GET /v1/admin/Token` | `inf-bronze-runner` EC2 — **orphaned downstream** (see §6) |

Orion REST dimensions come through the **Envision "ExcelReports"** report API (saved-report query→generate→fetch), NOT direct resource endpoints:
`GET /api/v1/Reporting/Envision/ExcelReports` (find) → `POST .../ExcelReports/Verbose` (create) → `POST .../{queryId}/Generate` → `GET .../Verbose/{queryId}` (fetch). HTTP verbs are per-dim and multi-call (e.g. `performance` = 1 POST + 3 GET; `tax` = "two ExcelReports POSTs in series"; `positions` = single GET). There is **no** clean GET/POST split by dimension count.

## 2. The 9 Orion REST dimensions + where they land

```
 s3://opal-data-inf/
 ├── bronze/orion-api/{YYYY-MM-DD}/        (Envision CSVs, datestamped)
 │     transactions.csv | tax_unrealized.csv | tax_realized.csv | billing.csv
 │     performance_dim.csv | unified_account_dim.csv
 ├── bronze/orion-api-v2/{YYYY-MM-DD}/     (v2 JSON dims, datestamped)
 │     representatives.json | household_rep_mapping.json | new_portfolio_accounts.json | assets...
 ├── bronze/positions/{YYYY-MM-DD}.parquet     ◄ AUA SOURCE — own prefix, parquet (NON-STANDARD)
 └── bronze/assets/{YYYY-MM-DD}.parquet        ◄ own prefix, parquet (NON-STANDARD)
```
**No `forwardfill` in Inflection** — that is a Black-Diamond/49F concept only.

## 3. Resources + timing (EventBridge crons, UTC; TF `infra/aws/terraform/inf-pipeline/`)

| Time | Rule | Resource | Output |
|---|---|---|---|
| 12:13 | `opal-inf-jwt-fetch` | `inf-jwt-trigger` λ → SSM → `inf-exporter` EC2 (t3.medium, i-081ae6aafb394fb1a) | SM `orion/jwt/current`, `orion/eclipse_jwt/current` |
| 12:30 | (reps) | `inf-api-reps` λ | representatives.json, household_rep_mapping.json |
| 12:35 | `inf-accounts-v2-daily` | `inf-accounts-v2-daily` λ | new_portfolio_accounts.json |
| 12:40 | (unified) | `inf-unified-account-dim-daily` λ | unified_account_dim.csv |
| 12:43 | `opal-inf-bronze-runner-cron` | `inf-bronze-trigger` λ → `inf-bronze-runner` EC2 (t3.small, i-083ad9ae297f88e9f) | Eclipse bronze + `_BRONZE_COMPLETE.json` |
| 12:45 | `inf-api-assets-v2-daily` | `inf-api-assets-v2` λ | assets parquet |
| 12:50 | (positions) | `inf-api-positions` λ | positions parquet |
| 12:55 | (tax) | `inf-tax-daily` λ | tax_unrealized.csv, tax_realized.csv |
| 13:00 | (txn) | `inf-api-txn` λ | transactions.csv |
| 13:35 | (billing) | `inf-billing-daily` λ | billing.csv |
| 13:40 | (performance) | `inf-performance-daily` λ | performance_dim.csv |
| 14:00 | `inf-canonical-prices-daily` | `inf-gold-trigger` λ → `inf-gold-layer-runner` EC2 (c6a.4xlarge, i-0ed5afded2ebd4ed4) | gold chain |
| 21:00 | `opal-inf-export-schedule` | `inf-jwt-trigger` λ (evening export) | JWT refresh |

All 9 dimension-Lambda EventBridge rules confirmed `state = ENABLED`. Resilience: `inf-ec2-launch-monitor` λ (EC2 state-change) → SNS `inf-otp-alert` → `inf-ec2-retry-launch` λ (backoff restart; DDB `opal-inf-launch-locks` idempotency).

## 4. The TWO pull layers (the core redundancy)

There are **two** mechanisms that pull Orion data:
- **Layer 1 — 9 scheduled cron Lambdas** (above) → bronze, 12:30–13:40Z.
- **Layer 2 — the gold-EC2 inline re-pulls** inside `orion-gold-dispatch.sh` `CHAIN_FULL` (~14:00Z+): `INF_API_PULL_{REPS, NEW_PORTFOLIO, ASSETS_V2, TXN, PERF, POSITIONS_DAILY}` — 6 dims.

6 dims overlap (pulled twice/day). The 3 cron-only (NOT re-pulled inline): `unified_account_dim`, `tax`, `billing` (gold reads their cron bronze).

## 5. The four axes of variance (what a unified flow must eliminate)

| Axis | Today | Unified target |
|---|---|---|
| **Bronze layout** | 3 patterns: `orion-api{,-v2}/{date}/*.csv\|json` (7 dims); `bronze/positions/{date}.parquet`; `bronze/assets/{date}.parquet` | 1 pattern: `bronze/orion-api/{date}/<dim>` for ALL dims |
| **Resume/skip** | only `positions` + `assets` skip-if-exists; other 7 re-pull unconditionally | every dim: same idempotent skip-if-exists |
| **Pull script per dim** | `txn`: cron `transactions_v2.py` (370L) vs inline `transactions_rest.py` (547L); `perf`: cron `performance_dim.py` (390L) vs inline `performance_rest.py` (409L). The `_rest` copies live in `data/inf/manual_api/` | 1 script per dim |
| **Execution layers** | 2 layers (cron Lambdas + inline EC2), 6-dim overlap, 4 dims genuinely double-pull (reps/accounts/txn/perf — no guard) | 1 layer: EC2 pulls all → silver → gold |

## 6. Eclipse: pulled daily, NOT utilized downstream

`inf-bronze-runner` EC2 pulls Eclipse (`/v1/portfolio/portfolios{,/simple}`, `/v1/modeling/models{,/{id}}`) → `bronze/eclipse/*` → `convert_eclipse_portfolios_to_silver.py` → `silver/eclipse/{date}/*` → `INF_E_00.eclipse_model_portfolios.py` → `gold/eclipse/{date}/model_portfolio_*.parquet`. **No consumer**: not promoted to platinum, not read by any publisher, not read by the portal (the portal `model_portfolio` route is the *benchmarks* feature, a name collision). It runs as a separate best-effort "new and largely untested" chain (`--chain eclipse`, ADVI_ECLDAT 2026-05-15). = removable dead weight: an EC2 + cron + a second JWT/auth dependency feeding a dead-end artifact.

## 7. Unified-flow target (Andrew-stated)

One machine (`inf-gold-layer-runner` already runs the book in a ~2h envelope) does: **pull all dims → consistent datestamped bronze → silver → gold**. Collapses all 4 variance axes: one pull layer (kills layer-2 redundancy + double-pull), one bronze pattern (positions/assets stop being special), one pull script per dim with a uniform resume guard. Inflection's small book makes single-machine end-to-end feasible. Eclipse arm to be dropped (or wired to a real served feature) since it is currently orphaned.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| pipescript advi-inf | estate map (producers/served/resources) | PASS |
| comp-freshness chain inf | silver/gold freshness baseline | PASS |
| live aws (s3 ls / s3api / TF read) | bronze key layout, EventBridge crons, instance IDs | PASS (rail-checked) |
| grep/read on inf source | endpoints, pull-script divergence, resume guards | PASS |

— 3.0.0_SA_CVO
