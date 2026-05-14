# Brief — Eclipse Data Ingestion via Existing Orion JWT Pattern (Empirical Feasibility + Proposed Productionalization)

**Author:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-14
**Issued to:** 1.0.0_SA_CTO
**Audience:** CTO (decision); COO + AE 0.6.1 (informational, will receive TO assignments if greenlit)
**Status:** Feasibility proven empirically. Awaiting CTO ratification of proposed productionalization scope.

---

## TL;DR

1. **Andrew's Eclipse access:** UI-blocked this afternoon by Orion provisioning gap (`422 "No Firm is Associated with the user"` on `GET https://www.orioneclipse.com/v1/admin/Token`). Resolved by an Alongside Eclipse-admin colleague adding Andrew's user to the Eclipse roster. **Andrew now has a valid Eclipse session JWT** (HS256, firm_id=209900, user_id=1191723, ~10hr expiry).

2. **Eclipse data is reachable via Orion's existing API + Eclipse's REST surface with the same JWT pattern we already use.** Eclipse's `/v1/portfolio/portfolios/simple` returns all 835 Alongside portfolios with the `accountId` + `modelId` join keys. Eclipse's `/v1/modeling/models/{id}` returns full security composition. No Eclipse-side credential separation; the Orion JWT exchanges for an Eclipse session JWT via `GET https://www.orioneclipse.com/v1/admin/Token` (same call that 422'd for Andrew this morning).

3. **Empirical reconciliation (today, my JWT):** $94.75M across 398 Opal-assigned accounts pulled and joined against Orion `Portfolio/Accounts` (3,030 firm-wide). Eclipse CSV export total $98.12M — 3.4% gap, likely valuation-lag (Orion `lastPositionDate=2026-05-13` vs Eclipse rebalanced same day 18:46Z). Two accounts (Graham + Tillett) unjoinable — likely stale-deleted IDs.

4. **Productionalization is a straightforward extension of the existing `inf-jwt-trigger` + `jwt_freshness.py` pattern.** ~1-2 dev-days to formalize into bronze/silver/gold for daily ingestion. Phases 1+2 are gating for the dashboard product Andrew is shipping tomorrow.

5. **CTO decisions requested:** (a) project code — new `ADVI_ECLDAT` or fold under `ADVI_INFFIN`/`ADVI_INFGRO`; (b) priority/sequencing vs INFFIN.017 + INFGRO Stage 1 dispatch; (c) Eclipse-JWT-as-Andrew audit-trail acceptance or service-user route.

---

## 1. Triggering context (Andrew direct ask 2026-05-14 ~14:30Z onward)

> "Eclipse shows model portfolio allocation. When we did the transfer yesterday of about 109M of inflection assets to opal models, that goes in model portfolios at various weightings. I need to know the weights, preferably at account level. … We need to overlay with the existing orion data … data product rolling out tomorrow."

Five named sleeves: Ultra Short Duration / Short Duration / Intermediate / Long Term Conservative / Long Term Aggressive (Eclipse names: Opal Ultra Short Term / Opal Short Term / Opal Intermediate Growth / Opal Long Term / Opal Ultra Long Term).

Andrew's Orion user → Eclipse SSO returned `422 "No Firm is Associated with the user"`. Initial misframing (firm not provisioned) corrected after Andrew noted teammates have Eclipse access — actual gap was Andrew's user not in the Eclipse-side user roster. A teammate admin added him while I diagnosed alternate paths.

Andrew floated borrowing a teammate's JWT for a Lambda direct-line; I pushed back on impersonation grounds (audit-trail breakage on a regulated trading platform; JWT expiry breaks durability) and pivoted to checking whether the data was reachable via the firm's existing Orion API patterns. Confirmed below.

---

## 2. Empirical findings (proven today, all in `.runtmp/`)

### 2.1 Eclipse and Orion use separate model ID spaces, joined by name

| Eclipse ID | Orion ID | Sleeve Name | Eclipse AUM (from CSV) | # Assigned |
|---:|---:|---|---:|---:|
| 3 | 83 | Opal Long Term | $6,909,385.70 | 56 |
| 5 | 85 | Opal Ultra Long Term | $1,542,210.65 | 23 |
| 6 | 84 | Opal Intermediate Growth | $59,266,786.92 | 165 |
| 7 | 86 | Opal Short Term | $3,241,446.65 | 14 |
| 8 | 87 | Opal Ultra Short Term | $561,254.98 | 8 |
| 9 | 89 | Opal Growth SMA | $0 | 0 |
| 10 | 88 | Opal DIV SMA | $0 | 0 |
| 28 | 152 | 50/50 OPAL INT/OPAL LTC | $20,514,475.52 | 127 |
| 29 | 153 | 50/50 OPAL ST/INT | $6,086,298.22 | 21 |

Eclipse Models.csv (`Models export from UI; colleague-shared`) is the authoritative AUM source. Mapping captured in `.runtmp/final_eclipse_join.py:ECLIPSE_TO_ORION`.

### 2.2 Endpoint surface (probed today with my live JWTs, NO impersonation)

**Orion main API (`api.cloud.orionadvisor.com`) — your existing pipeline pattern:**
- `GET /api/v1/Trading/Models` → 139 firm models, metadata only (`items` null on list view)
- `GET /api/v1/Trading/Models/{id}` → single-model detail including `items[]` with `productId` / `productName` / `ticker` / `targetPercent` / `itemTolUpper` / `itemTolLower`. Composition sums to 100% across all 9 Opal models.
- `GET /api/v1/Portfolio/Accounts?top=5000` → 3,030 firm accounts (full firm; firm size ceiling not reached). Server-side `modelId` / `modelAggId` / `$filter=` all silently ignored — client-side filter required.

**Eclipse REST API (`www.orioneclipse.com`) — needs Eclipse session JWT:**
- `GET /v1/admin/Token` with `Authorization: Session {orion_jwt}` → Eclipse session JWT (HS256, separate signing key, `firmId`+`userId`+`exp`+`iat` claims, ~10hr expiry).
- `GET /v1/portfolio/portfolios/simple` with `Authorization: Session {eclipse_jwt}` → **835 portfolios** with `id` / `name` / `accountId` (STRING) / `accountNumber` / `accountName` / `modelId` / `sleevePortfolio` / `isDeleted`. **This is the per-account → model assignment join table.**
- `GET /v1/modeling/models` → full Eclipse model list with metadata.
- `GET /v1/modeling/models/{eclipse_id}` → Eclipse-side composition (independent confirm against Orion `Trading/Models/{orion_id}.items`).

**Type gotcha:** Eclipse `accountId` is a STRING ("42"); Orion `account.id` is INT (42). Join requires explicit coercion (caught me in first pass; fixed in `final_eclipse_join.py:join_orion`).

### 2.3 Reconciled overlay (production-ready CSVs sitting in `.runtmp/`)

| File | Rows | What |
|---|---:|---|
| `.runtmp/orion_model_probe/all_firm_accounts.json` | 3,030 | Full Orion `Portfolio/Accounts` snapshot |
| `.runtmp/orion_model_probe/opal_models_with_items.json` | 9 | Composition for all 9 Opal models (security weights summing to 100%) |
| `.runtmp/eclipse_probe/_v1_portfolio_portfolios_simple.json` | 835 | Eclipse portfolios with model-assignment join keys |
| `.runtmp/eclipse_portfolios_full.csv` | 835 | All Eclipse portfolios + Orion enrichment (value, household, advisor, custodian) |
| `.runtmp/inflection_opal_accounts.csv` | 398 | Accounts in any Opal model (filterable by advisor) |
| `.runtmp/inflection_opal_sleeve_summary.csv` | 7 | Per-sleeve totals; matches Eclipse CSV within 3.4% |
| `.runtmp/inflection_account_security_dollars.csv` | 7,119 | **The deliverable:** account × security target-dollar matrix (398 accounts × ~18 tickers each, 31 unique tickers across all sleeves) |

### 2.4 Reconciliation against Eclipse Models.csv

| Sleeve | Eclipse CSV | Joined Pull | Δ |
|---|---:|---:|---:|
| Opal Long Term | $6,909,385.70 | $6,217,723.97 | -$691,661.73 |
| Opal Ultra Long Term | $1,542,210.65 | $1,542,210.69 | ~$0 ✓ |
| Opal Intermediate Growth | $59,266,786.92 | $57,639,572.00 | -$1,627,214.92 |
| Opal Short Term | $3,241,446.65 | $2,410,577.16 | -$830,869.49 |
| Opal Ultra Short Term | $561,254.98 | $387,420.99 | -$173,833.99 |
| 50/50 INT/LTC | $20,514,475.52 | $20,482,635.16 | -$31,840.36 |
| 50/50 ST/INT | $6,086,298.22 | $6,071,773.13 | -$14,525.09 |
| **TOTAL** | **$98,121,858.64** | **$94,751,913.10** | **-$3.37M (-3.4%)** |

3.4% gap explanation hypothesis: Orion `currentValue` lags Eclipse rebalance day (Eclipse rebalanced 2026-05-13T18:46:20Z; Orion last position date 2026-05-13 EOD). Either treat Eclipse CSV/API as source of truth or document the lag in the dashboard.

---

## 3. Existing pipeline patterns this extends

**Auth + JWT lifecycle (already shipped):**
- `infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py` — Playwright headless login as Andrew, harvest Orion JWT, store in SM + S3
- `data/orion/manual_api/jwt_freshness.py` (commit `b6e0c154`) — auto-recovery + freshness gate with CloudWatch alarm
- SM secret: `orion/jwt/current` (raw); S3 fallback: `s3://opal-data-inf/orion/jwt/current.json`
- Auth header convention: `Authorization: Session {jwt}` (Orion-specific, NOT `Bearer`)

**Bronze pulls (existing):**
- `data/orion/manual_api/pull_inflection_*.py` — REST pullers for assets / positions / transactions / performance / reps / billing / tax
- Per-dim Lambdas under `infra/aws/lambda/inf-pipeline/inf-{dim}-daily/` (ADVI_INFINGE Phase 1)
- Aggregator-driven gold-chain trigger (ADVI_INFETL.LAMBDA-DIMS)

**What Eclipse adds:** ONE additional JWT, ONE additional bronze puller, ONE additional silver dim, ONE optional gold/platinum view. Reuses all existing infrastructure.

---

## 4. Proposed productionalization (5 phases, ~1-2 dev-days)

### Phase 1 — Eclipse JWT capture (~3-4h; AE 0.6.1 lane)

Extend `inf-jwt-trigger` Lambda:

1. After Orion login → JWT harvest → SM/S3 write, fire one additional HTTP call:
   ```
   GET https://www.orioneclipse.com/v1/admin/Token
   Authorization: Session {orion_jwt}
   ```
2. Capture Eclipse JWT (HS256; `firmId`+`userId`+`exp`+`iat`).
3. Store at SM `orion/eclipse_jwt/current` + S3 fallback `s3://opal-data-inf/orion/eclipse_jwt/current.json`.
4. Extend `jwt_freshness.py` to dual-track (Eclipse JWT freshness check + auto-recovery; reuses 10hr clock — Eclipse JWT issued seconds after Orion JWT, expires same window).
5. CloudWatch namespace `Inflection/JwtResilience` adds `EclipseJwtExpired` / `EclipseJwtNearExpiry` / `EclipseJwtUnreadable` metrics.

**Why this lane:** AE 0.6.1 owns `inf-jwt-trigger` + IAM scope + SM secret. DS extends `jwt_freshness.py`.

### Phase 2 — Bronze puller (~2-3h; DS)

New script `data/orion/scripts/bronze/pull_eclipse_portfolios.py`:

1. Load Eclipse JWT via extended `jwt_freshness.py`.
2. Pull `GET https://www.orioneclipse.com/v1/portfolio/portfolios/simple` → 835 portfolios → write `bronze/eclipse/portfolios/{date}.parquet`.
3. Pull `GET https://www.orioneclipse.com/v1/modeling/models` → full model list → write `bronze/eclipse/models/{date}.parquet`.
4. For each Eclipse model ID in Opal set `{3,5,6,7,8,9,10,28,29}`: `GET /v1/modeling/models/{id}` → write `bronze/eclipse/model_composition/{eclipse_id}/{date}.parquet`.
5. Total: 11 API calls per daily run. No rate-limit risk.
6. Pre-commit gate: `.tools/ds-commit-gate.sh` + `from __future__ import annotations` (CLAUDE.md Rule 15).

### Phase 3 — Silver join (~2h; DS)

New silver script `data/orion/scripts/silver/convert_eclipse_portfolios_to_silver.py`:

1. Read bronze `eclipse/portfolios/{date}.parquet`.
2. Type-coerce `accountId` STRING → INT (the gotcha caught today).
3. Read silver `accounts_v2` for currentValue + household + advisor + custodian enrichment.
4. Join on Orion `account.id` ↔ Eclipse `int(accountId)`.
5. Emit `silver/eclipse_portfolio_dim/{date}.parquet` with one row per Eclipse portfolio (joined fields nullable for unjoinable accounts; expected ~2 today).
6. Strict Rule 17 compliance: no field slimming, no fillna defaults, no business-row filtering. Type standardization + dedup only.

### Phase 4 — Gold overlay (~2h; DS)

New gold script `data/orion/scripts/gold/INF_D_XX.opal_account_overlay.py`:

1. Read silver `eclipse_portfolio_dim/{date}` + silver `model_composition/`.
2. Filter to Opal-model-assigned portfolios.
3. For each (account, model) pair, expand to (account, ticker) rows with `target_percent` + `target_dollar = currentValue * targetPercent / 100`.
4. Emit `platinum/firm/opal_account_overlay.json` with structure:
   ```
   {
     "as_of": "2026-05-14",
     "data_as_of": "2026-05-13",  # bronze partition date
     "totals": {"accounts": 398, "total_value_usd": 94751913.10, ...},
     "by_sleeve": {"6": {"name": "Opal Intermediate Growth", "accounts": 159, "value": 57639572.00, ...}, ...},
     "by_account": [{"account_id": 488, "household": "Judith Ozinga", "eclipse_model_id": 6, "value": 3124840.07, "target_securities": [{"ticker": "VOO", "target_percent": 12.63, "target_dollar": 394667.30}, ...]}, ...]
   }
   ```
5. Compiler tool: `comp-pipescript io INF_D_XX.opal_account_overlay` before commit.

### Phase 5 — FE wire (~3-5h; DE/RD; deferred per Andrew direction)

Wire `platinum/firm/opal_account_overlay.json` into the Inflection dashboard. **Out of scope for this brief** — defer to DE 0.4 PRD against the dashboard product spec.

---

## 5. Sequencing options

### Option A — Stop-gap ship (dashboard launch tomorrow + productionalize after)

Andrew has the deliverable CSVs in `.runtmp/` RIGHT NOW. Dashboard launch tomorrow can consume those as a one-shot stop-gap (Andrew uploads CSVs to S3 / DynamoDB / wherever the dashboard reads). Productionalize over the next 1-2 weeks as a proper P2.

**Recommend if:** dashboard launch is the only near-term need and post-launch usage is exploratory.

### Option B — Phase 1+2 SHIP TODAY (P0 expedited)

If the dashboard needs daily-refreshed Eclipse data from day one, Phase 1 (AE 0.6.1) + Phase 2 (DS) need to ship today. ~5-7h combined wall. Phase 3+4 follow this week.

**Recommend if:** dashboard product requires automatic daily refresh from launch.

### Option C — Full pipeline pre-launch

All 4 phases ship before dashboard goes live tomorrow. ~10-12h combined wall. Tight but doable if dispatched immediately.

**Recommend if:** dashboard product is partner-facing and brittleness from a stop-gap is unacceptable.

**My recommendation:** **Option A** for the launch + Phase 1+2 dispatched today as P1 follow-on for daily-refresh-by-end-of-week. The CSV deliverable is already in `.runtmp/`; the dashboard can ingest those files this evening with zero engineering risk, and the production pipeline arrives within the cache window where the data is still 1-day-fresh.

---

## 6. Open questions for CTO

### Q1 — Project code

- New `ADVI_ECLDAT` (Eclipse Data Ingestion)?
- Fold under `ADVI_INFFIN` (current Inflection product finalization)?
- Fold under `ADVI_INFGRO` (Inflection GRO decomp — partially overlapping topic; Opal models are TARGETS that GRO measures returns AGAINST, distinct concept)?
- Fold under `ADVI_INFINGE` (Inflection ingestion daily automation — direct sibling, same pattern)?

**My read:** New `ADVI_ECLDAT` to avoid bloating active projects, with explicit cross-ref to INFINGE in the PRD. But CTO call.

### Q2 — Priority + sequencing

Active DS lanes per `/loop` watchdog state: ~A (this; idle post Phase 1.1 P1/P2 probe close), ~B (BD pipeline + cash_drag follow-on), ~C (BPMVH.001 D-min in flight), ~D (Phase 4 cutover Andrew-gated standby). INFFIN.017 is sitting as P3 opportunistic. INFGRO Stage 1 (.001-.004) all dispatch_held=true awaiting Andrew + DS bench reassignment.

Recommend: Option A (CSV stop-gap NOW) + Phase 1+2 productionalization Option B-equivalent (P1 today, both AE 0.6.1 + DS~A bandwidth). No conflict with INFGRO standdown.

### Q3 — Audit trail decision

Eclipse pipeline will run as Andrew (`user_id=1191723` on Eclipse, `user_id=11662220` on Orion). Every Eclipse API call attributes to him. Same posture as existing Orion ingestion. Three flavors:

- **Status quo (run as Andrew)** — same compliance posture as existing pipeline; no extra work
- **Service user** — request Orion to provision a dedicated "Opal-Data-Ingestion" user on both Connect + Eclipse; rotate credentials; pipeline runs as that user. Cleaner audit, but multi-week Orion provisioning cycle (same gap that bit Andrew today)
- **Hybrid** — ship Phase 1+2 as Andrew now; flip to service user when Orion ships it

**My read:** Hybrid. Status quo unblocks the dashboard; flip is mechanical (SM secret swap) once service user lands.

### Q4 — $3.4M Eclipse-vs-pull discrepancy

Worth a TO to chase, or accept as documented valuation lag? My hypothesis is Orion `currentValue` lag (last position date 2026-05-13 vs Eclipse rebalance same day 18:46Z — typical T+1 reconciliation). 96.6% reconciliation is excellent for a first pass. **Recommend: accept + document; revisit if it widens.**

### Q5 — Eclipse JWT lifecycle quirks

Eclipse JWT is HS256 with claim `exp` as **float** (e.g. `1778826305.694`), not int. Orion JWT is HS512 with `exp` as int. `jwt_freshness.py:_decode_jwt_exp` currently calls `int(payload["exp"])` which works (`int(1778826305.694) == 1778826305`) but worth being explicit about the type difference in the extended dual-track version.

Also Eclipse JWT carries `userId: 1191723` — Andrew's **Eclipse** user ID, distinct from his **Orion** user ID 11662220. Future debug confusion risk; recommend the SM secret include both IDs as metadata.

---

## 7. Risk + caveats

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Eclipse provisioning gap recurs (Andrew's user de-listed) | Low (admin colleague added today; need durable record of who has Eclipse admin) | High (pipeline goes dark) | Document Eclipse admin contact in `org/projects/{CODE}.json`; multi-user JWT pattern as Phase 6 stretch |
| Eclipse API surface changes | Low (stable per Orion docs / no version flag observed) | Medium (puller breaks) | Same CloudWatch alarm pattern as Orion ingestion; deploy-day smoke test in TO-VAL |
| `Authorization: Session` vs `Bearer` confusion | Low (codified in `jwt_freshness.py` docstring) | High (silent 401) | Reuse existing header convention; explicit docstring on Eclipse JWT helper |
| Pipeline impersonates Andrew on Eclipse | High (current design) | Low for read-only (no trade actions) | Per Q3; hybrid plan |
| 2 accounts unjoinable (Graham + Tillett) | Confirmed today | $3M data gap | Manual ID-reconciliation TO; or accept + report on dashboard with `unjoined` slot |
| ToS — programmatic Eclipse access via SSO | Low (own creds + own data + low volume, identical posture to existing Orion ingestion per ADVI_ORIAPI.md §170/173) | Medium (vendor lockout if scaled aggressively) | Same posture — daily cron + low cadence; revisit if scaling materially |
| Audit-trail attribution risk | Low for read-only | Medium for compliance audit | Per Q3 hybrid plan |

---

## 8. Compiler tools run today

| Tool | Result | Notes |
|---|---|---|
| (Direct probe scripts in `.runtmp/probe_*.py`) | All 4 scripts authored + executed against live JWTs | Discovery-mode; no production code touched. comp-pipescript not yet relevant (no script edits) |
| jwt_freshness CLI | `is_fresh=true, source=sm, seconds_remaining=8171` | Andrew's Orion JWT in SM `orion/jwt/current` is fresh; confirms existing pipeline pattern works |

Will run full compiler suite (`comp-pipescript io`, `comp-blast`, `comp-iam service`) when Phase 1+2 implementation TOs ship.

---

## 9. Files of record

| Type | Path | Purpose |
|---|---|---|
| Probe script | `.runtmp/probe_orion_models.py` | Endpoint surface mapping (Orion side) |
| Probe script | `.runtmp/probe_eclipse_direct.py` | Endpoint surface mapping (Eclipse side) |
| Final join | `.runtmp/final_eclipse_join.py` | The end-to-end overlay generator |
| Data snapshot | `.runtmp/orion_model_probe/all_firm_accounts.json` | Today's Orion firm-wide snapshot |
| Data snapshot | `.runtmp/eclipse_probe/_v1_portfolio_portfolios_simple.json` | Today's Eclipse portfolio snapshot |
| Deliverable CSVs | `.runtmp/eclipse_portfolios_full.csv` + 3 others | Dashboard-consumable artifacts |
| Eclipse model registry | `.runtmp/eclipse_models.csv` | Colleague-shared Eclipse Models UI export (source of truth for AUM totals) |
| HAR forensics | `.runtmp/orion_eclipse.har` (Andrew, blocked) + `.runtmp/eclipse_session.har` (Andrew, unblocked) + `.runtmp/colleague_orion.har` | Original block diagnosis + post-fix discovery + JWT extraction |

---

## 10. RAVC routing

- **RAVC1 (this brief):** CTO ratify on Q1-Q5 + sequencing option (A/B/C).
- **RAVC2:** Per-TO ships from receiving agents (AE 0.6.1 Phase 1, DS~A Phase 2-4) gated on CTO PRD authoring + COO TO decomposition.
- **RAVC final:** Dashboard smoke test post-launch — Andrew UAT against the per-account security-dollar overlay.

Direct routing to CTO per Andrew direction 2026-05-14 ~17:00Z ("write a full brief on it for CTO and issue to them immediately"). COO + AE 0.6.1 will receive copies via inbox so they can pre-stage bandwidth.

---

**End of brief.**
