# DATA_PLATFORM D2 — Black Diamond Architecture Spec

**Deliverable:** DATA_PLATFORM Phase-1 D2 (PRD S6 row D2). SPEC/AUDIT — not a build.
**Author:** 0.4.0_DS_ClientPlatform · **Issued by:** 2.0.0_SA_COO (GO 2026-06-24) · **Verify:** 3.0.0_SA_CVO (reconcile vs live BD/cot) · **Arch-input:** 1.0.0_SA_CTO
**Status:** v1.0 draft for CVO reconcile + CTO arch-gate · **Date:** 2026-06-24
**Grounded against (source-of-record this spec was built from):**
- `data/cot/scripts/bronze/cot_bronze_ingest.py` (the DataMining REST flow)
- `data/cot/scripts/bronze/cot_bd_session_fetch.py` (the Playwright OIDC session)
- `data/cot/scripts/bronze/templates/{transactions,allocations,holdings,realized,unrealized}.json` (the captured query bodies)
- `docs/architecture/COTETL_METHODOLOGY_THESIS.md` (snapshot-vs-FIFO methodology)
- `pipescript advi-cot` (the cot estate: producers → served → frontend)
- DATA_PLATFORM_PRD.md S2/S3.2/S9

> **Scope note (the displacement target).** Black Diamond is the aggregation+reporting vendor we displace for **49 Financial (49F)** and **Cottonwood (cot)**. There are **two distinct BD integrations** in our estate and they are NOT the same mechanism — this spec characterizes both, then specs the BD *vendor model* (the template/level/fact engine) that a proprietary platform would have to replicate or go-direct-to-custodian against.

---

## 1. Executive summary

Black Diamond (BD3, `bd3.bdreporting.com`) is a **server-side template-query reporting engine** over a **dimensional star** (Team → Relationship → Portfolio Group → Portfolio → Account → Holding → Tax Lot, crossed with fact/measure sets). You define a *query template* — a selection of dimension levels, dimensions, and fact measures, plus a date range — persist it server-side under a numeric `templateId`, then execute it asynchronously to get an xlsx export. BD's product is: (a) **custodian-feed aggregation** into that star, and (b) a **UI** over it. We already consume (a) programmatically; (b) is the layer we replace.

**The displacement seam (grounded):** the value BD adds beyond the UI is the **aggregation of custodian feeds into the account/holding/lot star and the lot-accounting (FIFO cost-basis) engine.** Everything downstream of the BD export — silver normalization, gold analytics, the served `platinum/firm` contract, the ADVI portal — **we already own.** So "replace BD" = own the ingest (direct custodian, or the reverse-engineered BD REST we already run) + own the lot-accounting where we still need it. **Difficulty: MEDIUM** — we have already reverse-engineered and run the BD REST flow end-to-end for cot, and the leaner methodology (D2 §6) shows the snapshot path needs no lot reconstruction at all for daily value.

---

## 2. The two BD integrations (they differ — this matters for the platform)

| | **cot (Cottonwood)** | **49F (49 Financial)** |
|---|---|---|
| Bucket | `opal-data-cot` | `opal-data-bd` |
| Mechanism | **API-first DataMining REST** (`/datamining/request/v1/run`) — reverse-engineered, the modern path | **Playwright UI scrape** of the BD report UI (older path) |
| Source script | `cot_bronze_ingest.py` (this spec's primary seed) | `bd-exporter` Playwright flow (legacy; not template-REST) |
| Methodology | **Snapshot-native** (Assets_Dim qt1 = canonical value/account/day directly) | **Lots-FIFO reconstruction** (`holdings_lots → canonical_lots → account_gains → performance`) — deep pre-snapshot history |
| Template catalog | 5 captured templates in repo (qt1–qt5) | No template JSONs in repo (UI-scrape, not REST) |
| Maturity | nascent, snapshot-first, single-firm-hardcoded, no advisor dim | mature, overfit, 26 `E_*` reconciliation-debt scripts |

**Platform implication:** the **cot REST flow is the reference** for how to talk to BD programmatically (it is the path we'd generalize to all BD firms); the **49F lots-FIFO methodology is the legacy reference** to retrofit to snapshot-native (PRD S9; D2 §6). A proprietary BD-displacement standardizes on the cot REST mechanism + the snapshot methodology, keeping FIFO reconstruction only where pre-snapshot history demands it (49F's back-history).

---

## 3. Auth / session / IP-binding model

Two-stage: a **browser-OIDC session capture** (Playwright) feeds a **headless REST bearer mint**.

### 3.1 Session capture — `cot_bd_session_fetch.py` (owner 0.6.2_AE)
- **Flow:** navigate `bd3.bdreporting.com` → OIDC redirect to `login.bdreporting.com/Auth/SignIn` → `POST /Auth/SignIn` (username/password from Secrets Manager `blackdiamond/cot/credentials`) → `/connect/authorize` → `/session/signin-oidc` → **`.bd.identity` cookie set on `bd3.bdreporting.com`**.
- **Post-login init (critical):** after the OIDC redirect, the script waits for `networkidle` AND explicitly navigates to `/datamining/` to establish the **firm-scoped DataMining execution context** (firmId/teamId server-side session). The generic app load establishes *user* context but NOT *datamining execution* context — `v1/run` 500s without it.
- **Captured artifact:** the **full cookie jar** (not just `.bd.identity`) written to Secrets Manager `blackdiamond/cot/session` as `{bd_identity, all_cookies:[{name,value,domain,path}], captured_at, expires_at}`. The full jar matters: `v1/run` POST execution needs `.AspNetCore.Antiforgery` + `idsrv` session cookies, not just `.bd.identity` (which alone suffices only for catalog/template GETs).
- **TTL:** session bundle metadata stamped 20h; BD sessions last 24h+ with keepalive (`/datamining/auth/keepalive`). The trigger Lambda probes freshness before use.
- **MFA:** the headless flow has **no OTP path** — it errors `FAILED_MFA_REQUIRED` if BD prompts MFA. (Today cot's BD login is password-only; this is a platform risk if BD enables MFA — see §8.)

### 3.2 Bearer mint + REST — `cot_bronze_ingest.py`
- Reads the SM session jar → `GET /datamining/auth/token` (Cookie-authorized) → opaque **Bearer `access_token`**.
- All DataMining calls thereafter are `Authorization: Bearer <token>`; the **xlsx export download** (`/Api/DataMining/ExportResults/{guid}`) is **Cookie-authorized** (not Bearer) — a dual-auth quirk to carry into any reimplementation.

### 3.3 IP-binding (the operational constraint)
- The whole flow runs on the **`cot-exporter` EC2 (`i-0643a5bee8a8feabf`, t3.small, start-on-demand, normally stopped)**. BD's session/execution context is **IP-bound** to that instance — a pull from another IP with the same cookies fails. This is why DS cannot pull BD REST locally and why a live-enriched template-catalog pull (§4.4) is an **AE-coordinated on-box** action.
- **Platform implication:** owned/automated multi-firm BD ingest must run from a **stable-egress-IP compute** BD recognizes per firm (today: one EC2 per firm-session). A direct-to-custodian path (Schwab D1) sidesteps this entirely for the firms where BD adds only aggregation+UI.

---

## 4. The DataMining template / level / fact model (the core of the spec)

### 4.1 The async REST flow (`cot_bronze_ingest.py`)
```
GET  /datamining/auth/token                      (Cookie .bd.identity jar) -> {access_token}
[reuse persisted templateId, OR POST /datamining/request/v1/template/ to create]
GET  /datamining/request/v1/template/{id}        (Bearer) -> fully-enriched template body
POST /datamining/request/v1/run  {template, asOfDate}  (Bearer) -> {templateId(runId), resultGuid}
GET  /datamining/request/v1/run/{runId}/status   (Bearer) -> {statusMessage, isComplete}
GET  /Api/DataMining/ExportResults/{resultGuid}  (Cookie) -> xlsx bytes
```
Run-body quirks captured in source (each was a real 500-debug, carry them forward):
- `v1/run` **requires a top-level `asOfDate`** (sibling to `template`) = the window end; omitting it 500s.
- The GET-enriched body must be **normalized**: set 5 fields to null (`category, parentQueryAllocationLevelId, allocationCashInclusionId, childQueryAllocationLevelId, allocationMarketValueFactId`) and strip 3 (`isAdhoc, isLimitSize, needsIDsForGrouping`) or `v1/run` rejects it.
- Dates must be re-stamped **MM/DD/YYYY** (BD echoes them as ISO datetime which `v1/run` rejects); `dateRangeType` must be re-stamped or the window silently drifts.
- **Status polling must detect `statusMessage in {error,failed,faulted}`** — BD leaves `isComplete=false` on a failed run, so polling on `isComplete` alone hangs the full timeout.

### 4.2 The template object model
A template = an envelope (`name, templateId, queryTypeId, dateRangeType, startDate, endDate, category`) + a **structure** that is one of two shapes:

**(A) Flat `levels[]`** (qt1 holdings, qt2 transactions, qt3 realized, qt4 unrealized). Each level = `{queryLevelId, name, joinType?, dimensions[]}`. Each dimension =
```
{ id, name, mappedColumn, dataType, searchType, isSelected, ordinal,
  options[] (enum domain), isAllocationChildDimension, isEnabled, isHidden, ... }
```
Plus a top-level `facts[]` = `[{queryFactId, name, isChildFact, measures[]}]`, each measure `{id, name, mappedColumn, sourceColumn, dataType, isSelected}`.

**(B) Parent/child allocation** (qt5 allocations). Uses `parentDimensionLevels[]` + `childDimensionLevels[]` (instead of flat `levels`) plus the allocation routing fields: `parentQueryAllocationLevelId` (=10), `childQueryAllocationLevelId` (=3), `allocationMarketValueFactId` (=25 → child fact `emv`), `allocationCashInclusionId` (=3). This is BD's "roll value up a parent grouping, allocate a child measure" model — distinct from a flat row export.

### 4.3 The dimensional star (levels, grounded from the captured templates)
BD's hierarchy, top→bottom (queryLevelIds vary per query type — the *level name* is the stable concept):

| Level | What it is | Key dimensions (mappedColumn) |
|---|---|---|
| **Team** | the advisory team / firm grouping | `team, teamDisplayName, teamID`, address block |
| **Relationship** | the household/client relationship | `relationshipExternalId, relationshipName, relationshipDisplayName, relationshipInceptionDate, relationshipTerminationDate, relationshipBenchmark, relationshipTarget`, SEC client type |
| **Portfolio Group** | grouping of portfolios | `portfolioGroup, advisorPreviousSystemKey, excludeFromBi` |
| **Portfolio** | a managed portfolio | `portfolioExternalID, portfolioName, portfolioRebalStrategyID/Name`, full **fee-schedule** block (`portfolioFeeScheduleLevel/RateType/Type, portfolioFlatFee, portfolioBasisPoints, portfolioLowerRange/UpperRange`), billing-config block, `portfolioHistoryStartDate`, rebal program/assignment GUIDs |
| **Account** | the custodial account | `accountNumber, accountExternalID, longNumber, accountDisplayNumber/Name, repName, custodian, accountOwnerType{Sole/Joint/Trust}, accountOwner, accountCategory/SubCategory, accountTaxStatus, taxLotMethodology, repCode, secClientType, dataProvider, manager, managerStrategyId, investmentStrategyID, managedAccountManagerID`, billing block, client address block (`clientName/Street/City/State/Zip`), UDFs (`accountUDF1..7` → "Advisor of Record", "NFS Account Number", etc.) |
| **Holding** | the asset position | `assetID, assetName/DisplayName, identifier(symbol), ticker, cusip, secAssetType, shareClassType, expenseRatio, bondDuration, couponRate, issueDate/callDate/calledDate, assetTaxStatus{Taxable/Tax-Exempt/AMT}, cashEquivalent, lastDividend` |
| **Tax Lot** | the cost-basis lot (realized qt3 / unrealized qt4 only) | realized: `rglOpenDate, rglTradeDate, rglUnitCost, isWashSale`; unrealized: `uglOpenDate, uglUnitCost, inheritedDate` |

`joinType: "portfolio"` ties the Relationship level into the portfolio grain. Account-level carries **`taxLotMethodology`** as a dimension with enum domain `[FIFO, LIFO, Highest Cost, Highest Cost Long Term First, Average Cost, Tax Optimized]` — i.e. BD tracks the lot-relief method **per account**, and the realized/unrealized query types expose the resulting lot-level open dates + unit costs.

### 4.4 The fact/measure set
| Measure (id) | mappedColumn | Appears in | Meaning |
|---|---|---|---|
| Units (5) | `units` | transactions, holdings | share/unit quantity |
| Market Value (7) | `marketValue` | holdings (qt1), transactions | position MV — **the AUA basis** |
| Transaction Fee (6) | `transFee` | transactions | per-transaction fee |
| Income (8) | `income` | transactions | income/dividend |
| Account Fee (20) | `accountFee` | transactions | account-level fee |
| Market Value (25, child) | `emv` | allocations (qt5) | allocation child-fact ending MV |

> **Completeness gap (flag for CVO + AE — the one thing the repo cannot fully answer).** The **repo template JSONs are thin envelopes for the persisted (already-provisioned) tables** — `holdings.json` and `allocations.json` carry only the envelope + (for allocations) the level/fact selection, because at runtime `run_query` fetches the **fully-enriched body via `GET /template/{id}`** (the server-side persisted selection). The transactions/realized/unrealized JSONs carry the full captured selection; holdings (qt1, templateId 226355) does NOT in-repo. **A truly complete "every dimension/measure BD exposes" catalog requires pulling the live-enriched `GET /template/{id}` for all five persisted templateIds (226274/226334/226355 + the realized/unrealized IDs) from the IP-bound cot-exporter EC2.** This is an **AE-coordinated on-box pull**; it is also exactly the CVO reconcile-to-live step (AC4). This spec documents the model + the in-repo catalog; the live-enriched full-domain catalog is the AE/CVO completeness leg.

### 4.5 The five query types (the template catalog)
| qt | Name | templateId (cot) | Structure | Grain | Role |
|---|---|---|---|---|---|
| **1** | Holdings / Assets_Dim | **226355** | flat levels (Account→Holding) + facts MV/Units | account × holding × day | **AUA + broken-out-holdings source of truth** (snapshot). Reconciles to allocations certified AUA ($373.2M vs $372.9M, 0.1%, 680 accounts). Captures transferred-in positions FIFO misses. |
| **2** | Transactions | **226274** | flat levels (Transactions→Relationship→Portfolio→Account→Holding) + facts Units/MV/Fee/Income/AcctFee | transaction × day | NNA/flow basis; external-flow flag (Contribution/Withdrawal); contra-account; trade/settle/entry dates |
| **3** | Realized G/L | (provisioned) | flat levels incl **Tax Lot** (`rglOpenDate/rglTradeDate/rglUnitCost/isWashSale`) | realized lot × day | realized gain/loss, wash-sale — **the FIFO lot-relief output** |
| **4** | Unrealized G/L | (provisioned) | flat levels incl **Tax Lot** (`uglOpenDate/uglUnitCost/inheritedDate`) | open lot × day | unrealized gain/loss, holding-period — **open-lot cost basis** |
| **5** | Allocations | **226334** | parent/child allocation (Team→Relationship parents; Portfolio→Account children; child fact `emv`) | allocation node | certified AUA cross-check + account_type/account_registration_type for gold A_00 |

### 4.6 Per-table date mode (the AUAFIX lesson, banked in source)
`TABLE_DATE_MODE` (all `Custom` now, post-ADVI_COTETL.AUAFIX-DATEMODE-A 2026-06-22):
- transactions/realized: `Custom`-14 = BD's ~14-day **restatement** window.
- holdings/allocations/unrealized: `Custom`-14 where 14 is a **holiday-gap FLOOR** (snapshot returns the END-date regardless of width; the window must span ≥1 complete business day), **not** a restatement lookback.
- **Why it matters for the platform:** BD's `CurrentDay` mode mis-stamped live snapshots with a stale early-June asOfDate → served firm-AUA froze 06-09 / ~$24M (6.5%) understated. The fix (switch to absolute `Custom` windows) is a **vintage-correctness invariant** any BD-displacement must preserve: *stamp the true data vintage, never the request day.*

---

## 5. From BD export to silver (the seam we already own)

`cot_bronze_ingest.py` lands each export at `s3://opal-data-cot/forwardfill_v2/{table}/{TABLE}_DAILY_{date}.xlsx`. The silver engine (`cot_silver_merge.py`, `merge-daily-incremental.py`) converts `forwardfill_v2/{table}` → `silver/{table}` with **zero per-table code** because **silver column == `to_snake_case(BD dimension display-name)`** — i.e. the BD `mappedColumn`/display-name IS the silver contract. Per Rule 17 silver is dedup + dtype only.

Source-side hardening already in place (defense-in-depth, carry into the platform):
- **(b) source-completeness guard** (`_holdings_nonzero_mv_fraction ≥ 0.5`): rejects an unvalued holdings snapshot **pre-land/pre-manifest** so a `$0`-priced early-day pull never enters bronze (fail-OPEN on parse ambiguity). The downstream C_03/C_01 gold guards are the backstop.
- **chain sentinel** `emit_bronze_sentinel` → `bronze/{run_date}/_BRONZE_COMPLETE.json` (emit-only-on-verified-success; a partial bronze emits nothing → chain halts visibly, no SSM-exit-0 false-advance).

**Orchestration (from `pipescript advi-cot`):** `cot-bd-session-trigger` Lambda runs a 4-phase EventBridge state machine — (1) `cot-bd-session-daily` cron `0 2 * * ?` → SSM `opal-cot-bd-session-fetch` on cot-exporter; (2) `cot-session-complete` (SSM command success) → bronze-run; (3) `cot-bronze-complete` (S3 `_BRONZE_COMPLETE.json`) → silver-run; (4) `cot-silver-complete` (S3 `silver_complete.json`) → gold-run. Gold (A-dim / B-holdings / C-canonical-perf-nna / D-portal-platinum) serves `opal-data-cot/platinum/firm/*` → ADVI Cottonwood tenant.

---

## 6. Lots FIFO-vs-snapshot methodology (the cost-basis audit — D2 AC3)

This is the single most important architectural finding for the platform.

### 6.1 What BD provides
BD exposes **both** value representations off the same star:
- **Snapshot value** (qt1 Holdings/Assets_Dim): MV/units per account×holding×day, **directly**. No reconstruction.
- **Lot-accounting** (qt3 realized + qt4 unrealized): the **Tax Lot** level with per-lot open dates, unit costs, wash-sale flags, holding-period — BD's own FIFO (or per-account `taxLotMethodology`) cost-basis engine output.

### 6.2 How the two firms use it (grounded, `COTETL_METHODOLOGY_THESIS.md`)
- **49F = reverse-engineering.** Reconstructs daily value from transactions via a lots-FIFO chain (`holdings_lots → canonical_lots → account_gains → performance`) because it has deep **pre-snapshot history**. Heavy, convoluted, NECESSARY only to recover value for an era with no snapshot. This produced real bugs ($352M phantom-lot overshoot from incomplete BD exit-events; +$91M/269-acct; $55.9M derivatives — the `advi_prices_*` investigations) and 26 `E_*` reconciliation scripts.
- **cot = snapshot-native.** BD's Assets_Dim snapshot IS the canonical value/account/day. The lots-FIFO chain is legitimately **empty for cot** (a snapshot has no lot open/close history — correct, not a defect). cot served value/AUA derives from `canonical_holdings` (the snapshot), wired at the served-AUA producer layer (`account_performance` C_03 / `D_00` clients_tab), bypassing the gains-aggregator C_00 / empty lots chain.

### 6.3 The architectural principle (the leaner methodology → the platform default)
**Daily holdings value comes from the SNAPSHOT where available; transaction reverse-engineering is the fallback for the era/firm with no snapshot, not the default.** Consequences for DATA_PLATFORM:
1. **Platform default = snapshot-native daily value** (BD Assets_Dim qt1, or direct-custodian positions D1). Wire served value to the snapshot, never the lots chain.
2. **FIFO lot-accounting (realized/unrealized G/L, lot-based returns) is a scoped capability**, retained where (a) a firm has pre-snapshot history needing reconstruction (49F back-history) or (b) a snapshot-underivable field is genuinely required (lot-level realized G/L, wash sales). Do NOT fabricate FIFO gains a snapshot can't produce — scope them explicitly.
3. **49F retrofit (downstream payoff):** once snapshot-native is proven on cot, move 49F to snapshot daily value going forward, keeping FIFO only for its pre-snapshot history.
4. **Andrew-flagged simplification:** use BD `Assets_Dim` directly as the daily-value mechanism (cot already does) — the simplest snapshot path, candidate to make the leaner methodology leaner still.

---

## 7. What a proprietary BD-displacement owns vs replaces

| BD layer | Displaceable? | How |
|---|---|---|
| **UI / reporting templates** | YES (already) | we serve ADVI/MDPF off our own gold; BD UI adds nothing we don't rebuild |
| **Custodian-feed aggregation into the star** | MEDIUM | BD ingests custodian feeds → account/holding/lot. Replace via direct-custodian (Schwab D1) where the aggregator adds only UI, OR keep the BD REST pull we already run for firms still on BD |
| **Lot-accounting (FIFO cost basis)** | SCOPED | snapshot-native eliminates the need for daily value; retain BD's lot engine output (qt3/qt4) only for realized/unrealized G/L + pre-snapshot reconstruction |
| **The REST execution engine** | N/A (consume) | the `/datamining/request/v1/*` flow is the contract we read; reimplementing BD's query engine is NOT the goal — going direct-to-custodian is |

**Bottom line (feasibility):** BD displacement is **MEDIUM difficulty and mostly already done** — we reverse-engineered and operate the REST flow, we own everything downstream of the export, and the snapshot methodology removes the hardest BD-specific dependency (lot reconstruction) for daily value. The genuinely-new work is **owned/automated ingest breadth** (direct-custodian, multi-firm) — scoped in D1 (Schwab) and D5 (the unified engine), not here.

---

## 8. Risks / open questions (for the audit + downstream phases)

1. **Live-enriched template catalog (§4.4)** — the full per-templateId dimension/measure domain requires an AE on-box `GET /template/{id}` pull from cot-exporter; CVO reconciles. Until then the "every dimension/measure" catalog is repo-complete for qt2/3/4/5 and model-complete (not field-exhaustive) for qt1.
2. **MFA fragility** — the headless OIDC capture has no OTP path (`FAILED_MFA_REQUIRED`). If BD enables MFA on a firm login, automated ingest breaks until an OTP relay (cf. the inf OTP-relay Lambda pattern) is built.
3. **IP-binding** — BD session/execution context is IP-bound to the per-firm exporter EC2; multi-firm owned ingest needs stable-egress compute per firm-session (or direct-custodian sidestep).
4. **49F is a different mechanism** (Playwright UI scrape, not REST) — unifying 49F onto the cot REST path is itself migration work, separate from the snapshot-methodology retrofit.
5. **Dual-auth quirk** — token (Bearer) for query, cookie for export download; carry both into any reimplementation.
6. **`v1/run` body fragility** — the normalize-5-null / strip-3 / re-stamp-dates / asOfDate-required quirks are undocumented BD behaviors discovered by debugging; they are vendor-version-sensitive and must be re-verified if BD updates.

---

## 9. Acceptance-criteria coverage

| AC | Status |
|---|---|
| 1. DataMining template/level/fact model + full template catalog | §4 (model + flow + object model + 7-level star + fact set + 5 query types). Catalog repo-complete for qt2/3/4/5; qt1 model-complete with the live-enriched completeness leg flagged (§4.4) for AE/CVO. |
| 2. Auth/session/IP-binding | §3 (OIDC Playwright capture → SM jar → Bearer mint; dual-auth; IP-bound cot-exporter EC2; MFA gap). |
| 3. Lots FIFO-vs-snapshot methodology | §6 (BD provides both; 49F reverse-engineers, cot snapshot-native; the leaner-methodology principle + 49F retrofit). |
| 4. CVO reconcile-verify vs live BD/cot | **PENDING CVO** — the live-enriched catalog pull (§4.4, AE-coordinated) is the reconcile-to-live step. |
| 5. SPEC only, no build; RAVC2 COO + CTO | This document. RAVC2 on commit. |

*v1.0 — grounded against the cited source-of-record. The live-enriched full-domain template catalog (§4.4) is the AE-coordinated + CVO-reconciled completeness leg; everything else is source-confirmed.*
