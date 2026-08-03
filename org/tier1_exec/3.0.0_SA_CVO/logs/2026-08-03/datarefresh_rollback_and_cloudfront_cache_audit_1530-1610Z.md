# DataRefresh rollback + CloudFront cache audit (Andrew-direct, 2026-08-03)

**archetype:** DIAGNOSE

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1530-1610Z.
**Tasking:** Andrew-direct in-session: (1) why the 07-31 emergency rollback only offered the 07-22
file, not 07-27; (2) make sure the rollback invalidates the relevant caches (Model Portfolios /
Benchmark tab / heatmap); (3) identify all CloudFront caching surfaces/rules.

---

## T1 -- Rollback candidate selection: SORTED BY RANDOM HEX, NOT TIME (root cause, source+live)

`handle_history` in `C:\Users\AndrewBerman\Desktop\ajb_workspace\infra\aws\lambda\data_refresh\lambda_function.py`
queries DynamoDB table `opal-data-refresh-executions` (PK=`EXECUTION`) with
`ScanIndexForward=False  # Newest first` and default `limit=20`. **The sort key is
`exec-{uuid.hex[:12]}` -- a random hex string -- so "newest first" is FALSE: the list is
descending-hex-alphabet.** Only executions whose random id begins high (`f`/`e`/`d`) ever surface.

Live-verified against the table (top-25 by that ordering): dates scattered Jan..Aug 2026.
- 07-22 execution `exec-ead9d176deb1` (`ea` = high hex) -> visible, hence selectable on 07-31.
- 07-27 execution **exists, canRollback=True** (`exec-5a4149176fb6`, uploaded 07-28T13:21Z) but
  `5a` sorts structurally below any top-20 cutoff -> NEVER listed, regardless of recency.
The same defect is in the deployed artifact (verified by downloading the live Lambda zip; both
`ScanIndexForward` sites present). The code comment is a false belief carried into production.

**Fix direction:** sort by `startedAt` (paginate the PK partition + sort in-Lambda; or a GSI on
startedAt). Small, isolated, same Lambda as W3.

## T2 -- Rollback cache invalidation: THREE LAYERS; the 08-01 fix closed exactly one

**Layer 1, CloudFront edge (CLOSED 08-01):** the 07-31 21:46Z rollback ran on a Lambda with NO
invalidation code -- the fix (`0.7.0_AE_CloudOps~C` DATAREFRESH_ROLLBACK_INVALIDATION_FIX
@832560b6a4) deployed 2026-08-01T19:12:31Z. Deployed-zip-verified TODAY: `create_invalidation` on
path `/api/general/*`, distribution `EVTSA9VEHNZVH` (in-code defaults; env vars absent but
non-fatal), plus a coverage resolver. Path coverage CORRECT for the incident surface: the portal
fetches `/api/general/benchmarks/model_portfolio_benchmarks.json`
(`portal/src/api/portal-proxy.ts:828`) -> behavior `/api/general/*`. Invalidations are
demonstrably being created on the live distribution (8 Completed today). Residual: invalidation
exists only on the version-based rollback path; the re-processing fallback relies on the
pipeline-side invalidators (which did fire today) -- indirect but real coverage.

**Layer 2, browser HTTP cache (BOUNDED, acceptable):** Lambda@Edge `cache-control-injector`
(origin-response on `/json/*` after rewrite) sets `Cache-Control: public, max-age=300,
s-maxage=300` -> both edge TTL and browser TTL are ~5 min. CloudFront invalidation cannot clear a
browser cache; worst case ~5 min self-heal. Note: behavior `/api/general/*` carries
Managed-CachingOptimized (DefaultTTL 86400) but the injected s-maxage=300 overrides it; the
24h default would apply only if the injector ever failed to run.

**Layer 3, React Query client cache (THE ACTUAL 07-31 CULPRIT -- OPEN):**
`portal/src/main.tsx:37-` sets `staleTime: Infinity` + `gcTime: Infinity` + persistence to
localStorage (`QUERY_PERSISTER_MAX_AGE_MS` = 12h), eviction ONLY at logout;
`refetchOnWindowFocus/Reconnect: false`. **Once a session has loaded the Benchmark tab, NO
server-side action -- invalidation included -- can change what that session shows. A full page
reload ALSO shows old data (localStorage rehydrates).** And the DataRefresh UI contains ZERO
`invalidateQueries`/`queryClient.clear()` calls post-rollback (grep: 0 hits under
`portal/src/pages/DataRefresh/`). This precisely reproduces the 07-31 experience: bytes restored,
edge eventually coherent, the open Model Portfolios page (Benchmark tab + heatmap) frozen on
pre-rollback data.

**Fix direction:** on rollback success the DataRefresh page calls
`queryClient.invalidateQueries()` (targeted keys incl. `model-portfolio-benchmarks`,
`etf-benchmark-returns`, `model-portfolio-timeseries`, or a full clear given rollback rewrites
the whole `json/` estate) -- client-side, cheap. Cross-session users are bounded by the 5-min
HTTP TTLs. NOTE the same Infinity policy means open sessions never see NORMAL pipeline updates
either (design decision, ADHC_FECACHE_COHERENCE) -- flagged, not judged here.

## T3 -- CloudFront caching surfaces/rules (one distribution)

`EVTSA9VEHNZVH` = opalinvest.dev + www.opalinvest.dev (the ONLY distribution in the account).
25 behaviors (comp-routes behaviors = DESIRED; TTLs + invalidations live-verified), 4 families:

1. **SPA static** -- default `/*` -> S3-opalinvest-portal. Managed caching; custom-error rules
   mask 4xx as HTML (the known JSON-error-debugging trap).
2. **Public portal JSON** (the Model Portfolios surface):
   - `/api/general/*` -> S3 `opal-data-portal-v2` via `public-data-router` (URL->`json/...` key
     rewrite) + `cache-control-injector` (5-min max-age) + `auth-validator-edge`.
     CachePolicy Managed-CachingOptimized (86400 default, overridden by injected headers).
   - `/api/general/json-tiered/*` and `/json-tiered/*` -> same origin, custom policy
     `json-tiered-5min-cache` (DefaultTTL 300). ⚠ `/json-tiered/*` (no `/api` prefix) is NOT
     covered by the rollback invalidation path `/api/general/*`; anything fetched via it relies
     on the 5-min TTL only.
3. **Advisor-intelligence** -- `/api/scoped/advisor-intelligence/...` family -> S3 `opal-data-bd`
   (shared-advisor-router, firm-parametric) or API Gateway; auth edge everywhere.
4. **API passthroughs** (effectively uncached) -- `/api/scoped/data-refresh/*`, tickets,
   partners, `/api/private/*`, `/v1/*`, `/auth/*` -> API Gateways.

**Invalidation creators (7, comp-grep denominator 4914/6490 files):** `data_refresh` rollback;
`yang_pipeline/outputs/invalidate-cloudfront` (pipeline step); `yang-generate-macro`;
`market-overview-tiered-generator`; `market-regime-classifier`; `inf-portal-publisher`;
`yang-time-machine`.

**Client-side (not CloudFront but part of every staleness story):** React Query
staleTime/gcTime Infinity + 12h localStorage persistence, logout-evicted.

## Recommended MDLP_MONPUB additions (routed to CTO)

- **W5:** time-sort the execution history (T1 root cause) -- same Lambda as W3, same owner.
- **W6:** client-cache invalidation on rollback success in the DataRefresh UI (T2 layer 3).
- Spec note: rollback invalidation's fallback-path reliance on pipeline-side invalidators;
  `/json-tiered/*` invalidation non-coverage.

## Compiler Tools

- `comp-routes behaviors` -- the behavior/origin/edge-lambda map (DESIRED); TTLs, cache policies,
  invalidation history, deployed-zip diff grounded live per Rule 22a (rail-checked markers on the
  raw calls comp-tools do not model).
- `comp-cache key model_portfolio_benchmarks` -- 0/103 useQuery call-sites (artifact fetched via
  wrapper fn; located by raw two-stage drill per standing feedback).
- `comp-grep create_invalidation` -- the 7-creator census.

## Next Steps

1. **[1.0.0_SA_CTO]** Fold W5/W6 into MDLP_MONPUB (or order separately); DS/DT PortfolioAnalytics
   own both fixes.
2. **[3.0.0_SA_CVO]** Verify W5/W6 on deploy (witness discipline as for W2).
3. **[Andrew]** Aware via in-session report; no decision required unless W5/W6 scoping objected.
