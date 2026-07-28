# DEBT.FRONTEND — Mission Brief

    mission     DEBT.FRONTEND
    macro       DEBT
    scope       Portal API route migration + deprecation of non-canonical namespaces
    author      0.2.0_DT_PortfolioAnalytics
    created     2026-07-28
    status      Phase 0 — brief only, NOT decomposed, NOT staffed
    priority    ** LOW — Andrew-direct 2026-07-28 **
    origin      Andrew-direct, during the MDPF P0 route census

---

## §0 — Andrew-direct charter (VERBATIM)

> "api/private/ should not even exist, my understanding is we only use api/general/ and api/scoped/ on a
> canonical basis, so you should be checking these out and listing any non-canonical routes for deprecation
> if they are really still present/active"

> "use the comp-tools particularly comp-cache and so on to track what is actually on the portal right now
> that is actually accessed via these deprecated paths. It is very possible that many if not all of these
> are not even displayed, even if they are generated. Rather than dealing with it right now, i would prefer
> that you instantiate an investigation into the topic and create a brief for the mission "DEBT.FRONTEND"
> which covers API migration and deprecation, and send that briefing to CTO with the instruciton that it is
> a project that is low priority at this time"

**PRIORITY IS SET BY THE SOVEREIGN AND IT IS LOW.** This brief exists so the work is *recorded and
scopeable*, not so it gets staffed. **Nothing here competes with MDPF_DEBTCLEAN.**
**Andrew's second instruction is a HYPOTHESIS he supplied and it is the mission's central question:**
*generated ≠ displayed.* Early evidence (§2.3) supports it.

---

## §1 — Canonical model

**`/api/general/` and `/api/scoped/` are the canonical namespaces. Everything else is debt.**

Encouragingly, **the model is already half-implemented and the precedent worked**: the MDPF-adjacent
`/api/private/portfolios/{aum-summary,aum-timeseries,aum-metrics,account-distribution}.json` calls were
migrated to `/api/general/` and the reasoning is recorded in-source at `portal-proxy.ts:356-357`:
> `// prior DEMO comment + TODO to move to /api/private/ removed — the general`
> `// endpoint is now auth-gated at CF layer, equivalent protection to /api/private/.`

**This mission finishes a migration already begun, rather than starting one.**

---

## §2 — Measured current state (2026-07-28)

### 2.1 — Non-canonical route families LIVE on `EVTSA9VEHNZVH`
Denominator: **24 cache behaviors + 1 default, enumerated in full** (`get-distribution-config`, APPLIED
plane). 18 canonical, 5 not.

| # | behavior | origin | unauth probe | portal clients | note |
|---|---|---|---|---|---|
| 16 | `/json-tiered/*` | S3 portal-v2-json | **200 UNAUTH** | **0** | auth-posture split, §2.2 |
| 23 | `/api/partners` | APIGateway-portal | 401 | **0** (docstring) | canonical twin (22) exists |
| 20 | `/v1/*` | APIGateway-portal | 401 | 1 | `sentiment.ts:798` |
| 18 | `/api/private/portfolio*` | APIGateway-portfolio | 401 | 11 | **live feature**, §2.3 |
| 19 | `/api/private/*` | APIGateway-portal | 401 | 3 | mixed, §2.3 |

### 2.2 — The one item with a security-posture dimension
```
/json-tiered/market-overview/rsi-summary.json               200  <- NO auth
/api/general/json-tiered/market-overview/rsi-summary.json   401  <- auth-gated
```
Same S3 origin; behavior 16 carries neither `auth-validator-edge` nor `public-data-router`. Body verified
as real data.
**BOUNDED (5 probes): NO AUM, holdings, or client data is reachable** — `mdpf/*` and `portfolios/*` return
**403**. Exposure is limited to objects literally under a `json-tiered/` prefix (market-overview tier-1).
**Either behavior 15's auth is unnecessary or 16 bypasses it — both cannot be true.** The app fetches these
via `publicApiRequest` on the canonical path, hinting the data is *intended* public, which would make 15 the
anomaly. **Architecture call, deliberately not made here.**

### 2.3 — ANDREW'S HYPOTHESIS IS ALREADY PARTLY CONFIRMED — "generated ≠ displayed"
`comp-cache map`: **105 of 105 `useQuery` call sites captured, 0 unparseable**; 85 distinct keys / 40 files.

| deprecated path | consumer status | evidence |
|---|---|---|
| `/api/private/portfolios/aum-flows.json` | **DEAD — zero component consumers** | `portal-proxy.ts:296` → wrapper `aum.ts:201` → **no `.tsx` caller anywhere** |
| `/api/private/portfolio/*` (PM) | **LIVE + rendered** | 4 real `useQuery` sites, `PortfolioManagement/hooks/usePortfolioApi.ts:97,114,129,241` |
| `/v1/sentiment/keyword-intelligence` | **LIVE but modal-gated** | `KeywordSentimentModal.tsx:128`, direct `await`, fires only on modal open |
| `/json-tiered/*` | **no portal client at all** | zero source references to the bare form |
| `/api/partners` | **no portal client** | docstring only, `advisor-intelligence.ts:8` |

> **So of the 14 "live" `/api/private/` call sites, at least one whole path is dead-ended, and the real
> migration weight is a single feature (Portfolio Management).** The headline count overstated the work.
> **This is exactly Andrew's point and it is why the mission is scoped as an INVESTIGATION first.**

---

## §3 — Mission questions (investigation, in priority order)

1. **Which deprecated-path fetches reach the DOM at all?** Extend §2.3 across every non-canonical call site.
   `comp-cache map` + `comp-transform schema-check <Component>` (`UNUSED` = fetched-and-not-rendered) +
   a runtime capture. **Dead paths delete; they do not migrate** — and deleting is far cheaper.
2. **Is there any NON-PORTAL consumer of each route?** The blocking unknown (§5).
3. **`/json-tiered/*` — which of the two auth postures is correct?** Architecture call, then act.
4. **Cost the Portfolio Management migration** (`APIGateway-portfolio`, behavior 18) — the only genuinely
   large item. Is it a re-point or a backend move?
5. **Does behavior REMOVAL change fallthrough for any surviving path?** (§5)
6. **Do `/api/general/` and `/api/scoped/` themselves need sub-conventions?** `/api/general/` currently
   fronts `json/mdpf/`, `json/portfolios/`, `json/benchmarks/`, `json/peers/`, `json-tiered/` — canonical at
   the prefix, unstructured beneath. Possibly out of scope; flagged because the census surfaced it.

## §4 — Suggested sequencing (recommendation only; routing is CTO's)
1. `/json-tiered/*` — zero clients, resolves the auth split
2. `/api/partners` — zero clients, canonical twin already live
3. `/api/private/portfolios/aum-flows.json` — **dead code, delete rather than migrate**
4. `/v1/*` — one call site
5. `/api/private/portfolio*` — **its own project**, not a cleanup

## §5 — GATES BEFORE ANY REMOVAL (both currently OPEN)
- ⛔ **"Zero portal clients" is scoped to `portal/src` ONLY.** A script, integration, or other application
  would be invisible. **A removed route with an unknown consumer is an outage.**
- ⛔ **CloudFront behavior order is PRECEDENCE-BEARING and fallthrough was NOT analysed.** Removing
  behavior 16 sends `/json-tiered/*` to the default `/*` (SPA) — which returns **HTML, not 403** — the
  `comp-routes behaviors` HTML-masking class. **Every removal needs its fallthrough traced first.**

## §6 — Non-goals
Fixing anything in this brief. Re-litigating the canonical model (Andrew set it). MDPF data-correctness
(→ MDPF_DEBTCLEAN). **Building any monitor, alarm, or freshness checker** — standing moratorium,
CLAUDE.md @`638cf6c36`.

## §7 — Instrument blind spots (so the next agent does not inherit a false denominator)
- **`comp-cache` audits `useQuery` ONLY** — `useQueries` / `useInfiniteQuery` / `useAutoSaveQuery` are not
  audited (its own disclosure), and **a direct `await` is invisible to it** (both live consumers found in
  §2.3 are direct awaits, not `useQuery`).
- **A source grep reports completeness over its own pattern.** COO's `mdpf|portfolios` grep could not see
  `/api/scoped/advisor-intelligence/*`; the count went 4 → 5 → 8 → "8 is short" today, and **every
  correction came from widening the METHOD, never from looking harder with the same one.**
- **A runtime capture misses the unexercised** (an unclicked lazy tab, an unopened modal). The
  `/v1/` consumer is modal-gated and would not appear in a default capture.
- **Use at least two methods with DIFFERENT blind spots and report each denominator separately.** A single
  reconciled number hides the thing that has been wrong repeatedly.

## §8 — Evidence
- Route census + probes: `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/PORTAL_ROUTE_CANONICALITY_CENSUS_20260728.md` @`3370c546f`
- `comp-cache map` / `comp-cache key`, this session
- Live `get-distribution-config` on `EVTSA9VEHNZVH`, 6 unauthenticated probes
