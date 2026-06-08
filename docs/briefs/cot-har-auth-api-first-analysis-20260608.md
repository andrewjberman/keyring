# Brief 1 — Cottonwood Capital Advisors (COT): Black Diamond Auth + Network Analysis (API-First Feasibility)

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-08
**Project (proposed):** ADVI_COTETL
**Source artifact:** `C:\Users\AndrewBerman\Downloads\bd3.bdreporting.com.har` (338 entries, capture of a full login → DataMining template build → run → export session)
**Governing standard:** `docs/architecture/THIRD_PARTY_DATA_INTEGRATION_STANDARD.md` (RATIFIED 2026-05-20) — *"we do not scrape, we reverse engineer."*

---

## 0. Headline finding

**An authenticated, API-first bronze ingest for Cottonwood is not only feasible — it is the standard-compliant path, and it is substantially cleaner than the 49 Financial EC2 scrape/CSV-export model.** The HAR captures Black Diamond's **DataMining REST API** end-to-end. We can reproduce the exact "CW_Transactions_Rich" export the operator built by hand as four programmatic calls against a documented-by-capture JSON contract. The single non-trivial piece is the **OIDC login bootstrap** (cookie-session mint, possibly MFA-gated), which maps directly onto the **Inflection `inf-jwt-trigger` + Secrets Manager `orion/jwt/current`** refresh pattern we already run in production.

Per the Third-Party Data Integration Standard, we frame this as **reverse-engineering Black Diamond's internal data API**, not "scraping." The 49 Financial DOM/CSV-export approach is the last-resort model this standard explicitly supersedes.

---

## 1. Domain map (signal vs. noise)

| Domain | Entries | Role |
|---|---|---|
| `data.pendo.io`, `*.pendo.io`, `helpscout.net`, `receptive.io` | ~180 | **Noise** — product analytics / in-app help telemetry. Ignore. |
| `bd3.bdreporting.com` | 100 | **Main app + DataMining API host** (the integration target) |
| `login.bdreporting.com` | 12 | **OIDC identity provider** (sign-in, `/connect/authorize`) |
| `firm-api.bdreporting.com` | 4 | Firm/relationship search API (`/Query/FirmDetailSearch`) |
| `broadcast-api.bdreporting.com`, `alerts.bdreporting.com`, `bd-alerts.service.signalr.net` | 18 | Broadcast/alerts (SignalR real-time) — not needed for ETL |

The entire ETL-relevant surface lives under `bd3.bdreporting.com/datamining/*` plus the `login.bdreporting.com` OIDC flow.

---

## 2. Auth / session model (the one piece needing automation)

Black Diamond uses **OIDC Authorization Code + PKCE** (IdentityServer; `.AspNetCore.*` + `.bd.identity` cookies), then mints a short-lived **opaque per-call access token** for the DataMining API.

### 2.1 Login bootstrap (browser-captured flow)

1. `POST https://login.bdreporting.com/Auth/SignIn` — **JSON body** `{ "firmAcronym", "username", "password", "multifactorToken", "registerDevice", "multifactorType", ... }`. (The capture's body carries live credentials — see §6 Security.) MFA fields are present in the schema (`multifactorToken`/`multifactorType`), so the account *can* be MFA-gated; this capture completed without an interactive OTP step, but we must design for the MFA path.
2. `GET https://login.bdreporting.com/connect/authorize` — OIDC params:
   - `client_id=BlackDiamond_Web`, `response_type=code`, `redirect_uri=https://bd3.bdreporting.com/session/signin-oidc`
   - `scope=openid profile offline_access api ix vault rebalancer timeline`  ← **`offline_access` present ⇒ refresh tokens are obtainable**
   - `code_challenge` + `code_challenge_method=S256` (PKCE)
3. `GET https://bd3.bdreporting.com/session/signin-oidc?code=...` → **302**, sets the session cookie **`.bd.identity`** (plus `.AspNetCore.Correlation.*` / `.OpenIdConnect.Nonce.*`).

The `.bd.identity` cookie **is** the durable session. Everything downstream is authorized by it.

### 2.2 Per-call DataMining token

- `GET https://bd3.bdreporting.com/datamining/auth/token` (authorized by the `.bd.identity` cookie) → `{"access_token": "<64-hex>-1"}`.
- That token is sent as **`Authorization: Bearer <access_token>`** on every `/datamining/request/*` call.
- `GET /datamining/auth/keepalive` → 204 is polled periodically to keep the session warm.
- The token is **opaque and session-scoped** (not a JWT — no embedded exp to parse). Freshness is governed by the session cookie lifetime + keepalive, not by decoding the token.

### 2.3 Implication for automation

The bootstrap is the **only** stateful/credentialed step. Two viable refresh designs, both already proven in our fabric:

- **LOGIN mode (Inflection model):** scheduled EC2 + headless browser (Playwright) performs the `/Auth/SignIn` POST, walks the OIDC redirect chain, captures `.bd.identity`, writes it to Secrets Manager. Handles MFA via the existing OTP-alert SNS path (`inf-otp-alert`) if/when BD prompts. This is exactly what `inf-jwt-trigger` does for Orion today.
- **COOKIE mode (YCharts model):** store a browser-captured `.bd.identity` cookie bundle in Secrets Manager and replay it; refresh on expiry. Lower automation, higher manual-touch — acceptable as a phase-1 bring-up while LOGIN mode is built.

Whether a fully-headless OIDC ROPC (password-grant) path exists (bypassing the browser) is an **empirical probe item** for the AE/DS kickoff — the `api` scope + `offline_access` suggest a token endpoint may accept resource-owner-password or refresh-token grants directly. If so, the refresh collapses to a pure-HTTP call (no Playwright), the cheapest possible design. **Do not assume from the scope string alone — probe it** (Standard §3.1, the ADVI_INFINC.005 empirical-over-docstring rule).

---

## 3. The DataMining API contract (reverse-engineered from capture)

This is the reproducible export pipeline. All calls are to `bd3.bdreporting.com`, `Authorization: Bearer <datamining access_token>`.

| Step | Call | Purpose | Key fields |
|---|---|---|---|
| 1 | `GET /datamining/auth/token` | Mint per-session bearer | → `access_token` |
| 2 | `POST /datamining/request/Query/DimensionsFacts` body `{"queryTypeId":N}` | **Field catalog** — all available dimensions + measures for a query type | → `levels[]` (7), `facts[].measures[]` |
| 3 | `POST /datamining/request/v1/template/` | Persist a named template (the field selection) | body = template def; → `templateId` (e.g. `225437`) |
| 4 | `POST /datamining/request/v1/run` | Execute. Accepts a persisted `templateId` **or an inline ad-hoc template** (`isAdhoc`) | → **`resultGuid`** + run `templateId` (e.g. `225438`) |
| 5 | `GET /datamining/request/v1/run/{runId}/status` | Poll | → `{"statusMessage":"In Process"\|"Completed","isComplete":bool}` |
| 6 | `GET /Api/DataMining/ExportResults/{resultGuid}` | Download | → **`.xlsx`** (`Content-Disposition: attachment; filename=CW_Transactions_Rich.xlsx`) |

**Critical detail:** the `resultGuid` consumed by the export endpoint (step 6) is returned **directly in the step-4 `v1/run` response** (`resultGuid` field) — no scraping of any page is needed to obtain it. The status poll (step 5) only gates *when* the export is ready.

### 3.1 `queryTypeId` is the data-domain selector

- `queryTypeId=2` = **Transactions** (what CW_Transactions_Rich uses).
- `queryTypeId=1` = a different domain (Holdings/positions level — DimensionsFacts for type 1 returns 7 levels incl. Team/Relationship/Portfolio/Account/Holding + a `facts`/`measures` block with measures like **Market Value**).
- This means the **same API gives us positions, holdings, performance, and aggregate (fact/measure) queries** — not just transactions. The bronze layer can pull every domain bd-pipeline needs from this one contract.

### 3.2 Export format: xlsx today, JSON-results to probe

The captured export is `.xlsx`. The status/run responses are JSON, and the DataMining engine is clearly result-set-backed (it has a `resultGuid`). **Probe item:** determine whether a JSON/CSV results endpoint exists (e.g. a `…/ExportResults/{guid}?format=json` or a `…/run/{id}/results` route) so bronze can ingest structured JSON directly instead of parsing xlsx. Even if xlsx is the only export, it parses cleanly (Brief 2) — but a JSON route would be strictly better for an automated pipeline and removes the openpyxl dependency.

---

## 4. Credential storage + refresh — conform to the established pattern

Per Andrew's directive (2026-06-08) and the Third-Party Data Integration Standard §3.2, the COT credential is stored and managed **exactly like YCharts (bundled cookie) and Inflection (JWT)** — AWS Secrets Manager primary, S3 fallback, freshness-gated, never committed.

### 4.1 The two reference patterns in our fabric

**Inflection / Orion (JWT) — `ADVI_JWTRES`:**
- Secrets Manager `orion/jwt/current` (raw token), S3 fallback `s3://opal-data-inf/orion/jwt/current.json`.
- `inf-jwt-trigger` Lambda (scheduled EventBridge) → starts `inf-exporter` EC2 → SSM doc `opal-inf-jwt-fetch` runs Playwright headless login → `sm.put_secret_value(orion/jwt/current)`. OTP via `inf-otp-alert` SNS.
- Consumers import `jwt_freshness.py` → `check_jwt_freshness(min_remaining_seconds=1800)` → **fail-fast** if stale (closes the silent-401 outage class of 2026-04-30).

**YCharts (cookie bundle) — `YALP_MDSRC`:**
- Secrets Manager `ycharts/credentials`, auto-detected modes: **COOKIE** (`cookies` header string, or `ycsessionid`+`csrftoken`+`aws_waf_token`) or **LOGIN** (`username`+`password`).

### 4.2 Proposed COT structure (mirror, do not invent)

| Element | Inflection | YCharts | **Proposed COT** |
|---|---|---|---|
| Secret ID | `orion/jwt/current` | `ycharts/credentials` | **`blackdiamond/cot/session`** (`.bd.identity` cookie bundle) + **`blackdiamond/cot/credentials`** (username/password for LOGIN-mode refresh) |
| S3 fallback | `opal-data-inf/orion/jwt/current.json` | — | `s3://opal-data-cot/blackdiamond/cot/session.json` |
| Refresh actor | `inf-jwt-trigger` Lambda + `inf-exporter` EC2 | manual/Playwright | **`cot-bd-session-trigger`** Lambda + a COT exporter VM (or reuse a shared partner-exporter EC2) running the OIDC Playwright login |
| Freshness gate | `jwt_freshness.py` (fail-fast) | session test probe | a COT-session freshness check (cookie still authorizes `/datamining/auth/token` → 200, else stale → fail loud) |
| OTP path | `inf-otp-alert` SNS | — | reuse SNS OTP-alert if BD MFA prompts |

The new AE (`0.6.2_AE_PartnerETL`) owns the Secrets Manager resources, the refresh Lambda, the exporter VM, and IAM — this is squarely the "PartnerETL" mandate. DS owns the bronze pull logic that *reads* the session and drives the DataMining API.

### 4.3 Contract-drift monitor (Standard §3.6 — mandatory)

A reverse-engineered internal API carries no stability guarantee. COT bronze must ship a monitor that alarms on: a `DimensionsFacts` schema change (dimension `id`/`mappedColumn` set drift), an auth-model change (login flow or token shape change), an endpoint move (non-200 on any of the 6 steps), or a sustained export failure. **Fail loud, never serve stale** — same posture as `jwt_freshness.py`.

---

## 5. API-first vs. 49 Financial scrape model — recommendation

| Dimension | 49 Financial (EC2 scrape / CSV export) | **COT API-first (recommended)** |
|---|---|---|
| Fidelity | DOM/CSV, cosmetic-UI-fragile | Structured JSON contract; xlsx export with stable column schema |
| Standard compliance | Last-resort model | **Reverse-engineer the internal API** — the ratified standard |
| Field control | Whatever the canned export emits | Full `DimensionsFacts` catalog; we select dimensions/measures per query type |
| Domains | Transactions export | Transactions **+ holdings + positions + fact/measure aggregates** from one contract |
| Automation cost | EC2 + browser drive per pull | 4 HTTP calls per pull; only the session refresh needs a browser (and maybe not, if ROPC works) |
| Drift detection | Implicit / brittle | Explicit schema + auth + endpoint monitor |

**Recommendation: build COT bronze API-first against the DataMining contract.** Reserve any DOM step as a flagged last resort only if a required datum is served no other way (none observed so far).

---

## 6. SECURITY — handle before anything else

> **The HAR contains live secrets.** The `POST /Auth/SignIn` body holds a **plaintext username and password**; multiple responses carry live `.bd.identity` session cookies and DataMining bearer tokens. (Deliberately not reproduced in this brief.)

Required handling:
1. **Do not commit the HAR** (`bd3.bdreporting.com.har`) to the repo. It is a local analysis artifact only. Confirm it is not under any tracked path.
2. Move the credential into **Secrets Manager** (`blackdiamond/cot/credentials`) — never into code, git, logs, or agent messages (Standard §3.2).
3. The session cookie/token captured here is already stale (short-lived) but should still be treated as sensitive; rotate the account password if there's any concern about HAR handling.

---

## 7. Open probe items for AE/DS kickoff (empirical, not assumed)

1. **ROPC / refresh-token grant?** Does `login.bdreporting.com` token endpoint accept password-grant or refresh-token-grant directly (collapsing refresh to pure HTTP, no Playwright)? `offline_access` scope suggests yes — **probe it**.
2. **JSON results endpoint?** Is there a structured-results route (`ExportResults?format=json` / `run/{id}/results`) so bronze skips xlsx parsing?
3. **MFA behavior** on the service/automation account — does BD prompt OTP on a fresh headless login? Design the SNS OTP path accordingly.
4. **Date-window + paging semantics** of `v1/run` (`dateRangeType`, `startDate`/`endDate`, `isLimitSize`, `includeAll`) — characterize for incremental daily pulls vs. full backfill.
5. **Firm/relationship scoping** — `firm-api/Query/FirmDetailSearch` + the `firmId=4175`/`teamId=6714` params; confirm COT's firm/team IDs and that the service account is scoped to COT data only.

---

## 8. Bottom line

API-first bronze for Cottonwood is feasible, cleaner, and standard-mandated. The DataMining contract is fully reverse-engineered from this capture (§3). The only build risk is the OIDC session-refresh automation, which has two in-fabric precedents (Inflection JWT, YCharts cookie) to copy rather than invent (§4). DS drives the API pull; AE `0.6.2_AE_PartnerETL` owns the credential/refresh/IAM infrastructure. Proceed to Brief 2 (field population) and Brief 3 (medallion port plan).
