# DATA_PLATFORM.DC0 -- Comprehensive-Crawl Harness Design

**Author:** 0.7.0_AE_CloudOps (lead) + 2nd AE-CloudOps lane (co-build) | **Status:** DESIGN-READY (pre-arch-gate)
**Gates:** CTO ARCH-GATES the isolation/stealth design BEFORE any live crawl (mandatory). COO TO = DATA_PLATFORM.DC0 (GO 142617Z). Andrew posture LOCK: RIDE-EXISTING-session + HARD live-pipeline isolation.
**Scope (CTO 142049Z):** UI-crawl targets = Orion (inf-exporter) + SmartX (smartx-exporter) ONLY. BD = REST-census (D2-deepened), NOT a UI crawl. Two downstream tracks ride one foundation: DC-REV (reverse-ETL supplant map, DS) + DC-LEV (SmartX capability-leverage map, 0.6.0).

## 1. Objective
A reusable, per-vendor, post-auth crawl+catalog harness: RIDE the existing exporter auth, Playwright-walk the data-bearing UI screens, capture every backend XHR -> a per-vendor comprehensive endpoint catalog (bronze->silver->gold), OBSERVE-ONLY v1. The harness is vendor-agnostic; both downstream tracks consume the same catalog.

## 2. The #1 constraint -- HARD live-pipeline isolation (the arch-gate surface)
The exporter sessions are LOAD-BEARING for live serving (ADVI/MDPF depend on the nightly pulls). A crawl must NEVER disrupt or burn them. Reconciling Andrew's RIDE-EXISTING + HARD-ISOLATION:

- **AUTH = ride the existing auth ARTIFACT, NO new login.** Reuse the SAME parked credential the exporter authenticates with -- SmartX: the parked JWT `opal-data-bd/smartx/jwt/current.json` (ROPC ~2h); Orion: the `inf-jwt-fetch.sh` artifact. A new login is the single highest-detection event; riding the parked artifact presents as the same authenticated identity, zero new-login signal. The crawl is READ-ONLY against the auth (never re-issues/rotates/invalidates it).
- **TEMPORAL isolation = never concurrent with the live pull.** The serving instances are Lambda-started -> run -> AUTO-SHUTDOWN (smartx run-all-portfolios.sh ends in `shutdown -h now`). The crawl runs in its OWN scheduled OFF-PEAK window with a hard pre-flight gate: it ABORTS if (a) a serving run is active (instance-running / serving-lock present), or (b) the next serving window is within a safety margin. A coordination lock (S3 sentinel or the serving cron schedule) is the single source of truth; crawl and serving can NEVER overlap.
- **FAIL-SAFE = detect -> backoff -> HALT the crawl, never the exporter.** On any detection signal (429/403/captcha/latency-spike/auth-challenge), the crawl exponential-backs-off then HALTS, and takes NO action that could invalidate/burn the parked auth or trip a vendor lock that would block the next serving pull. A crawl failure is contained to the crawl; serving is untouched.
- **ONE per-vendor usage envelope.** The crawl's request rate is BUDGETED + accounted together with serving so the vendor sees a single coherent normal-usage pattern, not two actors. Human-paced (reuse `humanize` / `perfect-human-session`).
- **INSTANCE isolation (arch-gate decision):** (a) a SEPARATE crawl instance per vendor (cleanest -- a crawl crash/lock physically cannot touch the serving instance; uses the same parked auth artifact from S3), vs (b) a separate scheduled job/context on the serving instance in a non-serving window. I lean (a) SEPARATE crawl instance for true blast-isolation -- CTO arch-gates.

## 3. Harness architecture (shared TS lib on the smartx-exporter stack)
Generalize the proven stack -- DO NOT rebuild stealth. Compose `humanize` + `perfect-human-session` + `fingerprint` + `stuck-detector` (smartx) and the SA `ultra_stealth` patterns (fingerprint-rand / bezier / CDP-evasion / session-health) into the shared harness.

Modules (one lib, parameterized per vendor):
- **isolation/** -- the section-2 layer: pre-flight serving-lock gate, off-peak scheduler, fail-safe backoff/halt, rate-budget accountant. (LOAD-BEARING -- the first thing built + arch-gated.)
- **auth/** -- ride-existing adapter: read the parked auth artifact per vendor (NO login flow).
- **nav-walker/** -- CURATED data-bearing screen-list FIRST (holdings / positions / performance / reporting / models), bounded-depth BFS DISCOVERY as phase-2. Deduped, depth-capped, human-paced transitions.
- **xhr-capture/** -- `page.on('request'|'response')` (+ `context.route` passthrough, never block) -> record url / method / query+body params / api-version / observed auth-audience+scope / response content-type + shape-sample / source-screen(s). OBSERVE-ONLY (never replays/probes in v1).
- **catalog/** -- bronze (raw captured XHRs) -> silver (deduped endpoint catalog) -> gold (characterized: data-plane tag, GraphQL op names, param semantics). Per-vendor S3 artifact.
- **vendor-config/** -- per-vendor: auth-artifact ref, base URLs, the curated screen-list, the api-version surface, the rate budget.

## 4. Catalog artifact schema (the DC-REV + DC-LEV interface)
Per-vendor S3 JSON; per endpoint: `url`, `method`, `query_params`, `body_params`, `api_version`, `auth_audience`, `auth_scope`, `response_content_type`, `response_shape_sample`, `source_screens[]`, `first_seen`, `times_observed`, PLUS the 3 DC-LEV fields (0.6.0 142745Z):
- `data_plane`: enum {model-state | performance-reporting | compliance-flags | trade-rebalance | identity | portal-internal} -- DC-LEV groups capabilities by plane.
- `graphql_operation`: broken out at OP-grain when the endpoint is GraphQL (the introspected roots, e.g. getFlag/listFlags/listActions/lastAction/createFlag/batchUpdateFlags/deleteFlag/addAction/addComment) -- enumerates the compliance plane.
- `consumption_status`: {consumed-today | not-consumed} -- THE core DC-LEV axis. The crawl tags each endpoint against the consumed-today set 0.6.0 supplies from the live pipeline (SmartX: api/3.1 models/{id} + /statistics + /performance + enterprises/aum + reportedmodels/holdings); everything the crawl finds BEYOND that = not-consumed = the leverage candidates.

DC-REV (DS reverse-ETL) + DC-LEV (0.6.0 capability-leverage) build straight off this single artifact.

## 5. Vendor sequencing (CTO call)
1. **Orion (inf-exporter) FIRST** -- smallest surface, we own the JWT path (`inf-jwt-fetch.sh`), lowest blast, reference-clean -> validates the harness + catalog shape + the isolation layer on the easiest case.
2. **SmartX SECOND** -- 0.6.0 stages the vendor-2 adapter inputs (data-bearing screen-list, the parked-JWT auth, the api/3.1/3.2/4.0+graphql surface). The observe-only XHR-capture on the live SPA RESOLVES 0.6.0's open gaps (which scope/version api/3.2+4.0 need; where the model/rebalance/trade plane calls -- it's not on api/3.1).

## 6. Build phases (post-arch-gate for the live crawl)
- DC0.1 isolation layer + auth(ride-existing) + the pre-flight serving-lock gate (offline-testable). [arch-gate FOCUS]
- DC0.2 nav-walker + xhr-capture + catalog bronze->silver (Orion config). Dry-run/observe-only.
- DC0.3 catalog gold characterization + the schema artifact.
- DC0.4 Orion LIVE crawl (post-CTO-arch-gate + the pre-crawl ToS ceiling on supplant) -> validate.
- DC0.5 SmartX vendor-2 config + LIVE crawl (LEVERAGE track, partner-aligned/low-risk).

## 7. Open arch-gate questions for CTO
1. Instance isolation: SEPARATE crawl instance (my lean) vs same-instance-non-serving-window?
2. The serving-lock source of truth: an S3 sentinel the serving cron writes, vs reading the EventBridge/Lambda serving schedule, vs instance-state? (I lean an explicit S3 serving-lock sentinel -- unambiguous, both sides honor it.)
3. Rate-budget ceiling per vendor (req/min + actions/session) -- needs a number; I propose deriving it from the serving run's observed cadence (the smartx 120-180s/portfolio rhythm) so crawl <= serving footprint.
4. ToS/detection ceiling per vendor (Andrew/CTO) -- the SUPPLANT-crawl hard-gate; observe-only-v1 keeps even supplant within normal-usage, but Orion is supplant-track -> needs the ceiling set before the DC0.4 live crawl.

## Out of scope
BD/cot DataMining catalog (REST = D2 census, in flight); the reverse-ETL/leverage maps (DC-REV/DC-LEV downstream); active gap-PROBING (Andrew-gated phase-2); legal/ToS sign-off (Andrew/CTO).
