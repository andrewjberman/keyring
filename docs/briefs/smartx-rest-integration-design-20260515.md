# SmartX REST Integration — Design Brief + Endpoint Manifest

| | |
|---|---|
| **Author** | 0.4.0_DS_ClientPlatform~B |
| **Date** | 2026-05-15 |
| **Status** | DRAFT — for COO decomposition into task orders |
| **Origin** | Andrew direct (HAR analysis of a live SmartX manager-portal session) |
| **Evidence** | `~/Downloads/portal.managedaccounts.io.har` (243 entries); live ROPC token test + single-model endpoint spot-check 2026-05-15 |

---

## 1. Objective

Replace the SmartX **browser-automation exporter** (`infra/aws/ec2/smartx-exporter`, Playwright "Perfect Human Mode" page-scrape) with a **direct REST integration**, and give SmartX the same parked-JWT token-management pattern Orion already uses — so SmartX model data becomes a clean, consistent, scheduled pull instead of a fragile headless scrape.

This does **not** replace Orion. Orion and SmartX are separate pipelines tracking different clients for different purposes; both remain. This brief applies the *Orion JWT pattern* to SmartX as a parallel sibling.

**First data goal (Andrew):** daily model value + holdings weights for each Opal model. SmartX has the day's data settled by ~9:00 AM ET.

---

## 2. Why this is now possible (verified)

The HAR proved SmartX is a standards-compliant **OpenID Connect / OAuth2** stack (IdentityServer at `identity.smartxadvisory.com`), and every data surface is a JSON REST/GraphQL endpoint behind a `Authorization: Bearer <JWT>` header. No scraping is required.

**Verified live 2026-05-15** — a Resource-Owner-Password-Credentials (ROPC) grant works directly against the token endpoint with the *existing* public web client:

```
POST https://identity.smartxadvisory.com/connect/token
  grant_type=password
  client_id=smartx-managerportal-webclient      (public client, no secret needed)
  username / password                            (the smartx/credentials/* secrets)
  scope=openid profile smartx_profile manager_access offline_access
->  token_type=Bearer  expires_in=7200 (2h)  access_token (RS256 JWT)  refresh_token (present)
```

Implication: the token refresh can run **fully headless in a Lambda** — no browser, no EC2, no confidential-client provisioning from SmartX. The browser exporter's entire reason to exist (logging in) collapses to one HTTP POST.

---

## 3. Auth mechanics

| Item | Value |
|---|---|
| Identity provider | `https://identity.smartxadvisory.com` (IdentityServer / OIDC) |
| Token endpoint | `POST /connect/token` |
| Grants supported | `password`, `refresh_token`, `client_credentials`, `authorization_code`, `implicit`, `device_code` |
| Client (web) | `smartx-managerportal-webclient` — public; ROPC works with it today |
| Access token | RS256 JWT, `typ: at+jwt`, **2-hour** lifetime, `aud: [smartx_profile, manager_access]`, `role: Manager` |
| Refresh token | Issued (scope includes `offline_access`) — 43-char opaque |
| Data-call auth | `Authorization: Bearer <access_token>` on every API host |
| Credentials source | AWS Secrets Manager — `smartx/credentials/username`, `smartx/credentials/password` (already exist, used by the EC2 exporter) |

**Recommended grant:** `grant_type=password` every refresh — stateless, the credentials always work, no refresh-token-rotation bookkeeping. `refresh_token` grant is available as an optimization if password usage needs minimizing. (The browser SPA itself uses implicit flow + hidden-iframe silent-renew; that path is irrelevant to a headless consumer.)

---

## 4. Token store — Orion pattern, colocated in `opal-data-bd`

Orion parks its JWT centrally and consumers read it with a freshness gate (`data/orion/manual_api/jwt_freshness.py`):

| Pipeline | Secrets Manager | S3 |
|---|---|---|
| Orion (existing) | `orion/jwt/current` | `s3://opal-data-inf/orion/jwt/current.json` |
| **SmartX (new)** | `smartx/jwt/current` | **`s3://opal-data-bd/smartx/jwt/current.json`** |

SmartX JWT lands in `opal-data-bd` (not `opal-data-inf`) — its consumers are the 49F / BD-domain work, so the token colocates with its actual use case. (A shared cross-pipeline resource bucket would be the "correct" home; absent one, colocate-by-use-case is the call — Andrew 2026-05-15.)

S3 JSON shape (mirrors Orion's): `{ "jwt": "<access_token>", "refresh_token": "...", "captured_at": "<iso>", "expires_at": "<iso>", "scope": "..." }`.

---

## 5. Proposed architecture

```
EventBridge (09:00 ET daily)
   -> smartx-jwt-refresher Lambda
        reads  smartx/credentials/{username,password}   (Secrets Manager)
        POST   identity.smartxadvisory.com/connect/token  grant_type=password
        writes smartx/jwt/current            (Secrets Manager, raw JWT)
        writes s3://opal-data-bd/smartx/jwt/current.json  (JSON wrapper)
   -> smartx daily pull job
        reads  s3://opal-data-bd/smartx/jwt/current.json  (freshness-gated reader lib)
        GET    api.smartxadvisory.com/api/3.1/...   (Bearer)
        writes raw -> bronze -> silver -> gold      (standard tiers, opal-data-bd)
```

Components:

| Component | Owner | Notes |
|---|---|---|
| `smartx-jwt-refresher` Lambda | DS writes code, AE deploys | ROPC -> parks JWT. ~2-min job. |
| EventBridge rule | AE | `09:00 America/New_York` daily — SmartX data is settled by ~9 AM ET. |
| JWT reader lib | DS | Generalize `jwt_freshness.py` to a `pipeline` param (`orion` / `smartx`) or a thin `smartx` sibling. One real difference: SmartX uses `Bearer`, Orion uses `Session`. Refresh-on-stale fallback (re-mint via ROPC) recommended for ad-hoc consumers between scheduled refreshes. |
| SmartX REST pull scripts | DS | New `data/smartx/scripts/pull_*_rest.py`, modeled on `data/orion/manual_api/pull_inflection_*_rest.py`. |
| IAM | AE | Refresher role: `secretsmanager:GetSecretValue` on `smartx/credentials/*`, Get/Put on `smartx/jwt/current`; `s3:PutObject` on `opal-data-bd/smartx/jwt/*`. Pull role: `s3:GetObject` on `opal-data-bd/smartx/jwt/*`. |

Disposition of the old exporter: `infra/aws/ec2/smartx-exporter` can be retired once the REST pull reaches parity on the AUM data it currently scrapes. Out of scope for the first wave — decommission is a later TO.

---

## 6. Endpoint manifest

All data hosts require `Authorization: Bearer <JWT>` and respond JSON. `api/3.1` responses use a common envelope: `{ data, version, hostDetails, statusCode, requestId, timestamp }` — the payload is under `data`.

**Status legend:** `HAR` = seen in the capture (size = observed bytes); `PROBE` = response shape confirmed live 2026-05-15; `body n/a` = HAR captured no response body.

### 6.1 Identity — `identity.smartxadvisory.com`

| Method | Path | Purpose | Status |
|---|---|---|---|
| POST | `/connect/token` | Token issuance (`password` / `refresh_token` / `client_credentials`) | PROBE — works |
| GET | `/.well-known/openid-configuration` | OIDC discovery | PROBE |
| GET | `/connect/userinfo` | User claims (333 B) | HAR |
| GET | `/connect/authorize`, `/connect/endsession`, `/connect/checksession` | Browser-flow only — **not needed headless** | HAR |

### 6.2 Core API — `api.smartxadvisory.com/api/3.1`

| Method | Path | Returns | Status |
|---|---|---|---|
| GET | `/models/{modelId}` | Model metadata: `id, name, shortName, status, reportedModelId, type, rebalanceThreshold, minimumAllocation, benchmarks[], feeTotal, fees[], enterprise{}` | PROBE |
| GET | `/models/{modelId}/statistics` | **Live model snapshot:** `value`, `cash`, `exposure{long,short,net,gross:{dollar,percent}}`, `returns{today,mtd,qtd,ytd:{dollar,percent}}` | PROBE |
| GET | `/enterprises/aum?modelid={modelId}` | **`totalAum` + `performance[]` = daily `{performanceDate, closingEquity}` series** (422 pts observed ≈ daily model value history) | PROBE (~42 KB) |
| GET | `/reportedmodels/{reportedModelId}/holdings` | **Holdings + weights:** `data[]` of `{symbol{ticker,assetType,companyName,industry}, quantity, price, marketValue, percentOfPortfolio}` | PROBE (~10 KB) |
| GET | `/reportedmodels/{reportedModelId}` | Reported-model base record | HAR (643 B) |
| GET | `/reportedmodels/{reportedModelId}/historicalperformance` | Historical performance series | HAR (~1.3 KB, body n/a) |
| GET | `/reportedmodels/{reportedModelId}/changerequesthistory` | Model change-request audit trail | HAR (28 KB, body n/a) |
| GET | `/enterprises/allocations?modelid={modelId}` | Account-level allocations into the model | HAR (**689 KB**, body n/a) |
| GET | `/enterprises/advisors?modelid={modelId}` | Advisors using the model | HAR (737 B, body n/a) |
| GET | `/allocations/performance?modelids={modelId}&grouping=m&start={epoch}&end={epoch}` | Allocation performance time series, windowed (epoch sec, monthly grouping) | HAR (**1.46 MB**, body n/a) |
| GET | `/users`, `/users/access` | User list + access/permissions | HAR (~13 KB, body n/a) |

### 6.3 Performance service — `performance.smartxadvisory.com`

| Method | Path | Returns | Status |
|---|---|---|---|
| GET | `/models/performance?model_ids={modelId}&percentages=100&leverages=1&platform=` | Deep return/risk stats — per-window benchmark calcs: `cagr, cumulative_return, max_drawdown, sharpe, sortino, deviation, skewness, kurtosis, annualized[], monthly returns` | PROBE (~97 KB) |

### 6.4 Legacy API — `smartx.managedaccounts.io/api/3.0`

| Method | Path | Returns | Status |
|---|---|---|---|
| GET | `/models/{id}?type=undefined` | Fuller model detail document | HAR (up to 96 KB, body n/a) |
| GET | `/models/{numericId}/commentary?limit=25` | Model commentary / notes | HAR (small, body n/a) |

### 6.5 GraphQL — `graphql.smartxadvisory.com/graphql`

| Method | Path | Returns | Status |
|---|---|---|---|
| POST | `/graphql` | Observed query `listFlags` (symbol/asset flags). Schema is introspectable — likely a broader surface | HAR (78 KB, body n/a) |

### 6.6 Not useful

`portal.managedaccounts.io/ng_api/v1/mngr/dashboard_status` (114 B); `analytics.smartxadvisory.com` is a separate SPA; quick-panel/i18n JSON are portal UI assets.

---

## 7. Model identity model (important for the pull design)

Two distinct UUID spaces — **do not confuse them:**

- **`modelId`** — used by `/models/{id}`, `/models/{id}/statistics`, `/enterprises/*`, `performance` service.
- **`reportedModelId`** — used by `/reportedmodels/{id}/*` (incl. **holdings**). Obtained from `/models/{modelId}` -> `data.reportedModelId`.

Calling `/reportedmodels/{id}/holdings` with a *modelId* returns **HTTP 400** (verified). The pull must chain: `models/{modelId}` -> read `reportedModelId` -> `reportedmodels/{reportedModelId}/holdings`.

The HAR enumerated **7 modelIds**. Spot-checked: `69cc5e3b-…` = **"Opal Long-Term Aggressive"**, `shortName` **`49FiLiLoAg000`** — the `49F` prefix confirms these are the 49F models. The 5 Opal portfolios (`UST/ST/INT/LTC/LTA` per `production.env`) are SmartX models; 2 further modelIds are unidentified. Resolving all 7 modelId -> name/shortName -> reportedModelId is the first task order's job.

---

## 8. Mapping to the first data goal — daily model value + holdings weights

| Need | Endpoint | Field |
|---|---|---|
| Daily model value (history) | `/enterprises/aum?modelid={modelId}` | `performance[].closingEquity` keyed by `performanceDate` |
| Model value (live snapshot) | `/models/{modelId}/statistics` | `statistics.value`, `cash`, `exposure`, `returns` |
| Holdings weights (current) | `/reportedmodels/{reportedModelId}/holdings` | per-symbol `percentOfPortfolio` (+ `quantity, price, marketValue`) |

Note: `/holdings` is a **current snapshot** — no per-day history was observed. Daily holdings-weight *history* is built by snapshotting once per day (the 9 AM ET run). Whether a historical-holdings endpoint exists is an open question for the probe TO.

---

## 9. Proposed task-order decomposition (for COO)

1. **TO-1 (DS) — per-model data availability assessment.** For each of the 7 modelIds: resolve name / shortName / reportedModelId; call every §6.2–6.4 endpoint; capture real response schemas (the HAR has no bodies); confirm which endpoints carry daily-grain vs snapshot data; produce a per-model × per-endpoint availability matrix. *This is the designated initial TO.*
2. **TO-2 (AE) — stand up the pull flow.** `smartx-jwt-refresher` Lambda + EventBridge `09:00 America/New_York` + IAM + the `smartx/jwt/current` secret + the daily pull job that lands **model value + holdings weights** to `opal-data-bd` (raw -> bronze -> silver -> gold). *First AE TO — the whole flow.*
3. **TO-3+ (DS) — silver/gold modeling + portal wiring**, and later the `smartx-exporter` EC2 decommission once REST parity is confirmed. Scope TBD after TO-1.

DS authors the Lambda/pull code; AE owns Terraform/IAM/EventBridge deploy.

---

## 10. Open questions

- Does a **historical holdings** endpoint exist, or is daily-weight history accrued only by daily snapshotting?
- The 2 unidentified modelIds — Opal models, benchmarks, or other enterprise models?
- `refresh_token` rotation behavior (one-time-use vs reusable) — only matters if we choose the `refresh_token` grant over plain `password`.
- GraphQL schema scope — introspect to see what it offers beyond `listFlags`.
- Rate limits — the exporter config asserts a 20 req/min ceiling "per SmartX agreement"; confirm and have the pull respect it.

---

## 11. Security note

The `smartx/credentials/*` secrets are a real SmartX login (`opal7`, role `Manager`). ROPC sends them to the token endpoint each refresh — keep them only in Secrets Manager, never in code or env files (the EC2 exporter already follows this). The parked JWT is a 2-hour bearer credential; `opal-data-bd/smartx/jwt/*` should be locked to the refresher (put) and pull (get) roles only.
