# SmartX — Comprehensive Backend Endpoint + Granularity Inventory

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` |
| Trigger | Andrew-direct, 2026-05-21: "know how deep SmartX goes ... all available endpoints and granularities ... the extent of snapshot and historical portfolio analytics and raw info for downstream portfolio analytics procurable on the platform." |
| Author | `0.2.0_DS_PortfolioAnalytics` |
| Date | 2026-05-21 |
| Status | v2 — surfaces A-E inventoried + the live api/3.1 exhaustion sweep COMPLETE. The sweep found a material net-new endpoint (`/models/{id}/performance`) that 4 prior work-pieces missed — see §0 and §8. |

## 0. Sweep correction (READ FIRST) — SmartX HAS a daily flow-adjusted model-return series

The live api/3.1 exhaustion sweep (§8) found **`/models/{id}/performance`** — an endpoint
**no prior work probed** (not B1, not S1, not SXPL_RESTIN.001, not b2597ea25). It is
multi-cadence (`?grouping=daily|weekly|monthly`) and at `grouping=daily` returns a **431-record
daily series**, fresh to T-1, each record:
`pnl{dollar, percent}` + `summary{beginningMarketValue, endingMarketValue, increaseByAmount,
decreaseByAmount, isFullRange, transactions, fees}`.

`pnl.percent` is a **daily return**, and `summary` carries the cash flows
(`increaseBy/decreaseByAmount`) + an `isFullRange` clean-period flag — i.e. it is a
**flow-adjusted** daily return, not the flow-contaminated `enterprises/aum.closingEquity`.

**This corrects the prior consensus.** b2597ea25 caveat 7 and this brief's earlier draft both
stated "SmartX model-performance is monthly end-to-end; no daily model-return series." That
is **WRONG** — superseded by this finding. SmartX has a daily, weekly, AND monthly
flow-adjusted model-return series via `/models/{id}/performance`. Consequence: the S1
Factor-Tilts sub-finding ("SmartX gives only a monthly model-return input") no longer holds —
a daily model-return input IS available (the factor *spreads* + regression remain non-SmartX,
so Factor Tilts is not fully unlocked, but the model-return leg can be daily-SmartX-sourced).
| Method | Reverse-engineer / integrate against the provider backend — NOT scrape (Third-Party Data Integration Standard). |
| Evidence | SmartX HAR `portal.managedaccounts.io.har` (2026-05-15, 243 entries) parsed; live GraphQL schema introspection (this session); `docs/briefs/smartx-rest-api-inventory-20260521.md` (b2597ea25, the B1+S1+SXPL_RESTIN.001 REST baseline) consumed. |

---

## 1. Headline — how deep does SmartX go

SmartX is a **managed-accounts platform**, and its backend depth reflects exactly that:
it is **deep on what the Opal models hold and how the managed accounts performed** —
holdings, model returns, model risk statistics, trade events, AUM — and **shallow-to-absent
on everything that is not managed-account state**: no market data, no portfolio attribution,
no factor data, no peer universe.

**Five distinct backend surfaces** (prior YALP/SXPL work saw only the first two):

| # | Surface | Host | What it is | Portfolio-analytics value |
|---|---|---|---|---|
| A | REST `api/3.1` | `api.smartxadvisory.com` | Model / enterprise / holdings / trade data | **HIGH** — the core |
| B | Performance service | `performance.smartxadvisory.com` | Monthly model returns + risk calcs | **HIGH** — the analytics core |
| C | GraphQL | `graphql.smartxadvisory.com` | Compliance restriction-flags + action log | **NONE** — not analytics (see §4C) |
| D | Legacy REST `api/3.0` | `smartx.managedaccounts.io` | Superseded by `api/3.1` | none — drop |
| E | Portal internal | `portal.managedaccounts.io/ng_api` | Portal dashboard widgets | none — UI plumbing |

**The hard limits on SmartX analytics depth (revised post-sweep):**
1. **Holdings are snapshot-only.** No historical-holdings endpoint exists; holdings history
   must be **accrued** by daily-snapshotting `/holdings`. (This limit STANDS.)
2. **Performance** — NOT monthly-only (corrected, §0): `/models/{id}/performance` serves a
   daily / weekly / monthly flow-adjusted model-return series. The `performance.smartxadvisory.com`
   service and `historicalperformance` are monthly; the api/3.1 `/models/{id}/performance`
   endpoint is multi-cadence incl. daily.
3. **Still genuinely absent:** per-segment / per-asset-class returns (attribution input),
   peer / category-relative analytics, holdings classification, factor data, market data.
   The sweep confirmed NO `/attribution`, `/risk`, `/sectors`, `/characteristics`,
   `/transactions` endpoints exist (all 404).

So SmartX answers "what does the model hold now", "how did the model perform — daily, weekly
or monthly", "what trades happened", and "what is the AUM" — but NOT "what did it hold last
quarter", "how did it do vs peers", or "decompose the excess return by segment".

---

## 2. Method & evidence

- **HAR parse** — `portal.managedaccounts.io.har` (2026-05-15 SmartX advisory-portal web
  session, 243 entries). Host histogram + endpoint extraction via `jq`. This is a *thin*
  session walk — model-list + per-model statistics/holdings + flags + users; it does NOT
  walk deep analytics screens (no attribution / performance drill-down / risk screens).
- **GraphQL schema introspection** — live, this session: minted the ROPC-JWT (same auth as
  `api/3.1`), POSTed the standard GraphQL introspection query to
  `graphql.smartxadvisory.com/graphql`, HTTP 200, full schema captured. Reproducible probe
  retained at `.runtmp/smartx_graphql_introspect.py` (read-only; ROPC-JWT from Secrets
  Manager; mirrors `sxpl_restin_probe.py`). NOTE: the probe's permanent home is
  `data/smartx/scripts/` — the `SHARED_OPAL_ETL` owned-paths lane (AE 0.5.0 / ~B); when the
  COO SmartX TO is formalized, the OpalETL lane owner should land it there.
- **REST baseline** — `docs/briefs/smartx-rest-api-inventory-20260521.md` (b2597ea25): the
  consolidated B1 + S1 + SXPL_RESTIN.001 endpoint table, auth model, identity map, 7 vendor
  bugs, confirmed-vs-inferred flags. This inventory **supersets** it with surfaces C/D/E.

---

## 3. Auth (one model, all surfaces)

OIDC ROPC password grant — `POST identity.smartxadvisory.com/connect/token`,
`grant_type=password`, `client_id=smartx-managerportal-webclient`,
`scope=openid profile smartx_profile manager_access offline_access`. Credentials = the
`opal7` Manager-role account, from Secrets Manager (`smartx/credentials/{username,password}`).
Bearer JWT, `expires_in` ~7200s, fresh token per mint (no eviction). **Confirmed this
session: the same Bearer JWT authenticates `api/3.1`, `performance.smartxadvisory.com`, AND
`graphql.smartxadvisory.com` — one credential, all surfaces.** Rate limit is per-credential
(shared `opal7` account), ~20/min ceiling; stay <=17/min; avoid the MDPF WS-B daily-chain
window.

---

## 4. Surface-by-surface endpoint + granularity inventory

### Surface A — REST `api.smartxadvisory.com/api/3.1`

Envelope `{data, version, hostDetails, statusCode, requestId, timestamp}`.

| Endpoint | Grain | Time-grain | Analytics primitive yielded | Notes |
|---|---|---|---|---|
| `models/{modelId}` | model | static | identity (name, reportedModelId, enterprise) | the modelId->reportedModelId chain |
| `models/{modelId}/statistics` | model | snapshot | value, cash, exposure (long/short/net/gross) | **returns BUGGY** — wrong-model + dead mtd/qtd/ytd |
| `enterprises/aum?modelid=` | model | **daily series** (~336-425 pts) | `closingEquity` daily book value | flow-contaminated — NOT a TWR |
| `enterprises/allocations?modelid=` | per-allocation (account) | snapshot | allocation roster: advisor, value, openedDate | no history |
| `enterprises/advisors?modelid=` | per-advisor | snapshot | advisor roster | — |
| `allocations/performance?modelids=&grouping=m` | allocation | snapshot, heavy | nested perf stats | to 11.7 MB; window or avoid |
| `reportedmodels/{rmid}` | reportedmodel | static | metadata | — |
| `reportedmodels/{rmid}/holdings` | **per-symbol** | **snapshot only** | ticker, qty, price, marketValue, percentOfPortfolio | 12-16 ETF holdings/model; `assetType` uniformly "equity" (WRONG); `industry`="Unknown"; `?date=`/`?asOf=` ignored, `holdings/historical` 404 |
| `reportedmodels/{rmid}/historicalperformance` | reportedmodel | monthly series | `performanceValue` | **STALE ~14mo — dead**; use Surface B |
| `reportedmodels/{rmid}/changerequesthistory` | per-trade | event log (historical) | tradeTimestamp, ticker, qty, activity, from/to | rebalance/trade history |
| `users` | user | snapshot | user record | **net-new** (not in b2597ea25); access-control, not analytics |
| `users/access` | user | snapshot | access-control grants | **net-new**; not analytics |
| `models/{modelId}/performance?grouping=` | model | **daily / weekly / monthly series** | per-period `pnl{dollar,percent}` + `summary{begin/endMarketValue, increase/decreaseByAmount, isFullRange, transactions, fees}` | **NET-NEW — sweep-discovered; the key find.** `grouping=daily` -> 431 daily records (flow-adjusted return, fresh T-1); `weekly` -> 90; `monthly` -> 21. THE SmartX daily model-return source. |
| `models` / `reportedmodels` / `enterprises` | collection | snapshot/list | roster/list of models / reportedmodels / enterprises | net-new (sweep); the bare-collection forms (b2597ea25 had only the `/{id}` forms) |
| `models/{modelId}/holdings` | model | snapshot | HTTP 400 unparameterized — a model-keyed holdings variant of `reportedmodels/{rmid}/holdings` | net-new (sweep); exists, needs params |
| `benchmarks` | benchmark | snapshot/list | benchmark reference list (small, 394 B) | net-new (sweep) |
| `accounts` | account | (empty for this credential) | account roster | net-new (sweep); returned empty for `opal7` |

**Sweep negative results (confirmed ABSENT — HTTP 404):** `reportedmodels/{rmid}/`
`{statistics, performance, transactions, trades, allocations, attribution, risk,
characteristics, sectors, commentary}`; `models/{id}/{allocations, transactions}`;
`/securities`, `/sleeves`, `/transactions`, `/enterprises/{models, transactions, performance}`.
This bounds the api/3.1 surface: **no attribution / risk / per-segment / transactions /
sectors data endpoint exists** — confirming the §5 gaps empirically, not by inference.

### Surface B — `performance.smartxadvisory.com/models/performance`

`GET ?model_ids=&percentages=100&leverages=1&platform=`. **The SmartX analytics core.**

| Field group | Grain | Time-grain | Content |
|---|---|---|---|
| `trackedYearsForModels.{id}.months` | model | **monthly series** | per-month return % + per-month `.benchmark` |
| `models.{id}.monthly_statistics` | model | monthly, to current month | monthly perf series (FRESH) |
| `models.{id}.monthly_benchmark_statistics` | model + 1 benchmark | monthly | benchmark return series |
| `models.{id}.windows / ytd` | model | period snapshots | period returns |
| `model.calculations` | model | snapshot (monthly-derived) | **risk/return stats**: deviation, alpha_spread, cagr, sharpe, sortino, max_drawdown, skewness, kurtosis, cumulative_return |

Caveats: date params **ignored** (always full-history). **No peer/category data** anywhere
(S1-confirmed — model + exactly one "Benchmark"). Monthly cadence end to end.

### Surface C — GraphQL `graphql.smartxadvisory.com/graphql` (NET-NEW — introspected)

**Definitive finding: NOT a portfolio-analytics surface.** Full schema introspected this
session — `Query` + `Mutation` + `Subscription` roots, 30 types, but the entire surface is
**compliance restriction-flags + an action log**:

- **Root queries (4):** `getFlag`, `listFlags`, `listActions`, `lastAction`.
- **Mutations (5):** `createFlag`, `batchUpdateFlags`, `deleteFlag`, `addAction`, `addComment`.
- **Types:** `Flag`, `Action`, enums `ActionType`/`ObjectType`/`Status`, `*Payload`/`*Input`
  wrappers. A `Flag` carries `objectId/objectName/objectType/assetType/status` — e.g. a
  restriction flag on a *symbol* (the HAR's captured query was `listFlags objectType=symbol`).

It is a trade-restriction / compliance-flag microservice. It yields **zero** holdings,
performance, or risk data. Mapped and bounded — no further depth here.

### Surface D — Legacy `smartx.managedaccounts.io/api/3.0`

`models/{id}` (returns a 105-byte `{status,msg,type}` stub — not usable) + `models/{numeric}/commentary`
(model notes). Superseded by `api/3.1` for all data. **Drop from scope.**

### Surface E — Portal internal `portal.managedaccounts.io/ng_api/v1/mngr/*`

`dashboard_status` (114-byte status blob) + the portal's `app/data/quick-panel/*.json`
(activities, events, notes, onboarding checklist). Portal-UI plumbing — not a data API.

---

## 5. Portfolio-analytics depth — what is procurable vs a gap

| Analytics need | SmartX provides? | Endpoint / caveat |
|---|---|---|
| Current model holdings + weights | **YES** (snapshot) | `reportedmodels/{rmid}/holdings` — per-symbol |
| Holdings history (point-in-time) | **NO** | snapshot-only; must accrue daily snapshots |
| Holdings asset-class classification | **NO** | `assetType` broken; needs an external classifier (Opal ETFClassifier) |
| Model return series (monthly) | **YES** | `/models/{id}/performance?grouping=monthly` OR Surface B `monthly_statistics` |
| Model return series — **DAILY** | **YES** (corrected — §0) | `/models/{id}/performance?grouping=daily` -> 431 daily `pnl.percent`, flow-adjusted, fresh T-1 |
| Model return series — weekly | **YES** | `/models/{id}/performance?grouping=weekly` -> 90 records |
| Model risk statistics (sharpe/sortino/drawdown/etc.) | **YES, monthly** | Surface B `model.calculations` |
| Benchmark return series | **YES** (one benchmark/model, monthly) | Surface B `monthly_benchmark_statistics` |
| Peer / category-relative analytics | **NO** | confirmed absent across Surfaces A+B |
| Per-segment / per-asset-class returns (attribution input) | **NO** | only model-level returns |
| Trade / rebalance event history | **YES** | `changerequesthistory` |
| Model AUM (daily) | **YES** | `enterprises/aum` (the value series is fine for AUM, not for TWR) |
| Per-account allocation roster | **YES** (snapshot) | `enterprises/allocations` |
| Market data (prices, indices) | **NO** | SmartX is not a market-data vendor |
| Factor data | **NO** | — |

**Net for downstream portfolio analytics:** SmartX can supply the **model-portfolio
performance dimension** (monthly returns + risk stats + benchmark), the **holdings/weights
dimension** (current snapshot; forward-accruable), **trade history**, and **AUM**. It cannot
supply daily returns, holdings classification, per-segment/attribution inputs, peer data,
factor data, or any market data — those remain non-SmartX (Bloomberg-pkl / YCharts / Opal
methodology). This is consistent with and extends the S1 finding: Positioning is
SmartX-securable as a hybrid (SmartX weights + Opal classifier); Brinson attribution is a
forward-only hybrid build; Factor Tilts stays proprietary.

---

## 6. Known vendor bugs (carried from b2597ea25 §5 — track for any build)

1. `models/{id}/statistics` returns the WRONG model + dead mtd/qtd/ytd.
2. `historicalperformance` monthly + ~14mo stale — effectively dead.
3. `holdings.assetType` uniformly "equity" (wrong for bond ETFs); `industry`="Unknown".
4. `holdings` is current-snapshot only — no historical endpoint.
5. `performance/models/performance` ignores date params — always full-history.
6. `enterprises/aum.totalAum` mis-scaled — use per-day `closingEquity`.
7. **CORRECTED (§0):** SmartX model-performance is NOT monthly-only. `historicalperformance`
   + the `performance.smartxadvisory.com` service are monthly, but `/models/{id}/performance`
   (api/3.1, sweep-discovered) serves daily / weekly / monthly. The prior "monthly end-to-end,
   no daily model-return series" claim (b2597ea25 caveat 7 + this brief's earlier draft) is
   superseded — a daily flow-adjusted model-return series exists.

---

## 7. Acceptance vs Andrew's ask

- "All available endpoints" — 5 surfaces, ~17 distinct endpoint patterns inventoried (§4).
- "Granularities" — per-endpoint entity-grain + time-grain mapped (§4 tables).
- "Snapshot vs historical analytics" — §5 table; net: snapshot holdings, monthly history.
- "Raw info for downstream analytics" — §5: model performance + holdings + trades + AUM
  procurable; daily/classification/attribution/peer/factor/market = gaps.

## 8. Live api/3.1 exhaustion sweep — DONE

Ran 2026-05-21 (read-only, ROPC-JWT, 3.6s throttle; probe `.runtmp/smartx_api31_sweep.py`
+ `.runtmp/smartx_netnew_characterize.py`). 11 known endpoints re-confirmed live (all 200);
27 candidate endpoints tested. **Result: 9 candidates EXIST, 18 ABSENT (404).**

- **Material find:** `/models/{id}/performance` — daily/weekly/monthly model-return series
  (§0). No prior work probed it. This is why an exhaustion sweep was worth running.
- Other net-new: `/benchmarks`, `/accounts`, the `/models` `/reportedmodels` `/enterprises`
  collection forms, `/models/{id}/holdings` — all folded into §4A.
- 18 ABSENT confirms no attribution/risk/transactions/sectors/securities endpoint exists —
  the §5 gaps are now empirically bounded, not inferred.

Open: a fuller SmartX HAR walking the attribution/risk screens would be belt-and-suspenders,
but the sweep + the HAR + b2597ea25 now bound the api/3.1 data surface with confidence. The
GraphQL introspection probe + the two sweep probes are in `.runtmp/` pending the OpalETL-lane
landing into `data/smartx/scripts/` (per the COO routing — SHARED_OPAL_ETL, 0.7.0_AE~A).
