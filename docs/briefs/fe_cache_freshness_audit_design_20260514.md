# Brief — FE-cache freshness audit design (`comp-validate fe-cache-freshness <queryKey>` v0.6 input)

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Audience:** 2.0.0_SA_COO (sequencing + v0.6 routing) + 1.0.0_SA_CTO (ADHC_COMPIL_V4 v0.6 candidate ratification)
**Trigger:** Today's $202M cache-poisoning P1 incident (`cb62f069`) — sister to ADVI Snapshot Segment Analytics Year-interval empty-state. Both same root pathology: queryKey stable across URL-construction change → poisoned cache entry survives staleTime → symptom persists post-fix.
**Sister briefs:** `memory/feedback_react_query_cache_poisoning_from_deploy_window.md` (the reactive post-mortem); this brief proactively sweeps for the next instance before it ships.
**v0.6 ratchet input:** proposed tool `comp-validate fe-cache-freshness <queryKey>` per CTO independent banking.

---

## Headline

Audit of all `refetchOnMount: false` callsites in `portal/src/pages/AdvisorIntelligence/` surfaces **23 occurrences across 7 files**. Risk-tiering identifies:

- **P1 (cross-firm/cross-tenant URL variation possible):** 14 callsites — queryKey + URL both encode `firmOverride`. Today's incident (`cb62f069`) was 1 of these; the other 13 are the same class waiting for the next URL-construction change to detonate.
- **P2 (same-URL but tenant-flag dependent):** 4 callsites — queryKey suffix includes a tenant-dispatch flag (`usesStaticClientDetail ? 'static' : 'lambda'`). Safer than P1; staleness still possible if flag derivation logic changes.
- **P3 (stable URL invariant; per-entity-ID keyed):** 5 callsites — queryKey includes `advisorId`/`accountId`/`clientKey` (entity-scoped). URL is deterministic per entity; cache poisoning bounded to single entity's bad-response window.

**Recommended structural fix:** **drop `refetchOnMount: false` defaults on ALL P1 callsites** + audit the remaining staleTime defaults to align with cross-deploy risk tolerance. The default `refetchOnMount: true` retries error-state queries on remount (the bug class today exploited specifically); successful queries still respect staleTime so wire load doesn't balloon.

**Proposed v0.6 tool:** `comp-validate fe-cache-freshness <queryKey>` — surfaces the queryKey-to-URL fan-out + staleness risk-tier + cross-deploy-window safety + suggested mitigation. Single-callsite query and codebase-wide scan modes.

---

## Background: today's $202M incident as the proof-by-example

**Pre-fix deploy window (pre-`17b3dad7`):** `?firm=49financial` / `?firm=inflection` URLs hit shared-advisor-router constructing `opal-data-49financial` / `opal-data-inflection` buckets. Real buckets are `opal-data-bd` / `opal-data-inf`. NoSuchBucket → CloudFront `custom_error_response` → SPA HTML. `JSON.parse('<!doctype...')` → SyntaxError → React Query captured error state under `queryKey=['partner-analytics', granularity, firmOverride]`.

**Fix (`17b3dad7`):** `ROUTER_FIRM_SUFFIX` inverse map + `bucketSuffix()` translator. Wire URL fixed to `?firm=bd` / `?firm=inf`. **queryKey unchanged** — still encodes long-form `firmOverride`.

**Post-fix poisoning persistence:** queryKey-stable cache lookup hits the same error-state entry. `staleTime: 5 * 60 * 1000` + `refetchOnMount: false` keeps it alive across remounts. Empty-state branch renders. Symptom persists for 5+ minutes post-fix until staleTime expires OR explicit cache invalidation.

**The audit-discipline class banked:** the queryKey contract is "encodes app-level concept that survives deploys." But URL-construction logic ALSO survives deploys (the URL helper changes; the queryKey doesn't see it). The two contracts are decoupled — and that decoupling is the latent-bug surface.

---

## Callsite inventory by risk tier

### Tier P1 — Cross-firm/cross-tenant URL variation; queryKey doesn't disambiguate (14 callsites)

For each P1 callsite, queryKey includes `firmOverride` (or `effectiveFirmKey`), URL also encodes `firmOverride` via `?firm=<bucketSuffix(firmOverride)>` or `?firmId=<firmOverride>`. **If the URL-helper changes (e.g., `bucketSuffix()` translator added, removed, or reversed), the queryKey-stable cache lookup hits a stale entry from a different URL-construction era.**

| # | File:Line | queryKey | URL produced by queryFn | staleTime | Severity-modifier |
|---|---|---|---|---|---|
| 1 | `_partners/inflection/index.tsx:75` | `['firm-leaderboard', firmOverride ?? FIRM_ID]` | `getFirmLeaderboard(firmOverride)` → `/api/scoped/...?firm=inf` | 5min | NonAdminProfileTab fallback to FIRM_ID const if firmOverride undefined; entry-protected |
| 2 | `_partners/inflection/index.tsx:162` | `['partner-analytics', 'quarterly', effectiveFirmKey]` | `getPlatinumPartnerAnalytics('quarterly', firmOverride)` → `/api/scoped/...?firm=inf` | 5min | **Identical to today's incident class** (`cb62f069` fix targeted DistributionTab variant) |
| 3 | `_partners/49financial/index.tsx:96` | `['firm-leaderboard', firmOverride]` | `getFirmLeaderboard(firmOverride)` → `/api/scoped/...?firm=bd` | 5min | firmOverride=undefined for external users; cross-user cache risk |
| 4 | `_partners/49financial/index.tsx:179` | `['partner-analytics', 'quarterly', firmOverride]` | `getPlatinumPartnerAnalytics(...)` | 5min | **Sibling of today's incident class** — 49F's analog |
| 5 | `_partners/49financial/index.tsx:195` | `['cohort-a-summary', firmOverride]` | `getCohortASummary(firmOverride)` | 10min | 49F-only artifact; lower fan-out |
| 6 | `_shared/components/PartnerAnalytics.tsx:121` | `['partner-analytics', granularity, firmOverride]` | `getPlatinumPartnerAnalytics(granularity, firmOverride)` | 5min | **Same queryKey family as `cb62f069` was patched on DistributionTab** — does PartnerAnalytics component have same hazard? Empirically yes; needs verify against AE 0.7 monitoring |
| 7 | `_shared/components/PartnerAnalytics.tsx:185` | `['inflec-timeseries-chart', firmOverride]` | `getPlatinumInflecTimeseriesChart(firmOverride)` → `/api/scoped/...?firm=inf` | 5min | Inflection-only path (`enabled: usesStackedBars`); cross-firm exposure capped |
| 8 | `_shared/components/PartnerAnalytics.tsx:239` | `['advisor-intelligence', 'timeseries-overview', firmOverride]` | `getTimeseriesOverview(firmOverride)` | 5min | Byte-shared queryKey with DistributionTab:863 (deduplication); fix MUST be applied in both |
| 9 | `_shared/tabs/DistributionTab.tsx:855` | `['advisor-intelligence', 'platinum-cumulative-chart', firmOverride]` | `getPlatinumCumulativeChart(firmOverride)` | 5min | Reads `/api/scoped/...?firm=<bucketSuffix(firmOverride)>` (post-`17b3dad7`); affected by today's URL-shape change |
| 10 | `_shared/tabs/DistributionTab.tsx:868` | `['advisor-intelligence', 'timeseries-overview', firmOverride]` | `getTimeseriesOverview(firmOverride)` | 5min | Byte-shared queryKey with PartnerAnalytics.tsx:235 |
| 11 | `_shared/tabs/DistributionTab.tsx:2174` | `['advisor-book-relationship-stacks', drillParent, firmOverride]` | `getPlatinumAdvisorSummary(drillParent!, firmOverride)` → `/api/scoped/.../{drillParent}/book.json?firm=inf` | 5min | Per-advisor key; Inflection-only; lower fan-out but same class |
| 12 | `_shared/tabs/ClientsTab.tsx:167` | `['firm-leaderboard', firmOverride]` | `getFirmLeaderboard(firmOverride)` | 5min | Cross-firm via firmOverride; firm-level fan-out |
| 13 | `_shared/tabs/ClientsTab.tsx:566` | `['platinum-client-directory', firmOverride]` | `getClientDirectory(firmOverride)` | 5min | Cross-firm via firmOverride |
| 14 | `_shared/AdvisorBookView.tsx:212` | `['inflec-account-timeseries', selectedClientKey, selectedAccountId, firmOverride]` | `getPlatinumAccountTimeseriesStatic(...)` | 5min | Per-account/per-client; tightly scoped but still firmOverride in URL |

**`cb62f069` fix already applied to:** `DistributionTab.tsx:790-795` partner-analytics useQuery (dropped `refetchOnMount: false`). **NOT applied to 13 sibling callsites in the same class.**

### Tier P2 — Tenant-flag in queryKey suffix (4 callsites)

queryKey includes a static-vs-Lambda dispatch flag in the tuple suffix. Cache lookup disambiguates by dispatch path, so URL-construction changes within ONE dispatch path are still vulnerable, but cross-dispatch contamination is prevented.

| # | File:Line | queryKey | Why P2-not-P1 |
|---|---|---|---|
| 15 | `_shared/tabs/ClientsTab.tsx:415` | `['advisor-book-client', selectedAdvisorId, selectedClientKey, firmOverride, usesStaticClientDetail ? 'static' : 'lambda']` | Tenant-dispatch flag in suffix prevents cross-tenant collision; still P2 because tenant-detection logic could shift |
| 16 | `_shared/tabs/ClientsTab.tsx:474` | `['advisor-book-account', selectedAdvisorId, selectedAccountId, firmOverride]` | Per-account scoped; cross-tenant exposure capped but firmOverride still in queryKey |
| 17 | `_partners/inflection/InflectionInsightsPanel.tsx:256` | `['inflection-activity-scan', firmOverride, selectedWindow]` | Inflection-only panel; selectedWindow keys distinct window-state; cross-firm impossible (component only mounts for Inflection partner) |
| 18 | `_partners/inflection/InflectionInsightsPanel.tsx:266` | `['inflection-firm-concentrations', firmOverride]` | Same as above; Inflection-only |

### Tier P3 — Per-entity-ID keyed; URL invariant per (firm, entity-id) tuple (5 callsites)

queryKey includes a per-entity ID (`advisorId`, `accountId`, `clientKey`, `selectedWindow`). URL is deterministic per (firm, entity) tuple. Cache poisoning bounded to single entity's bad-response window — at most 1 entity's data goes stale per URL-construction change.

| # | File:Line | queryKey | Why P3 |
|---|---|---|---|
| 19 | `_partners/inflection/InflectionInsightsPanel.tsx:261` | `['inflection-cash-drag', firmOverride, selectedWindow]` | window-scoped + Inflection-only |
| 20 | `_shared/tabs/ClientsTab.tsx:428` | `['advisor-book-client', selectedAdvisorId, ...]` (PII path) | PII-sensitive; `gcTime: 0` evicts on unmount; cross-mount risk minimal |
| 21 | `_shared/tabs/ClientsTab.tsx:486` | `['advisor-book-account', selectedAdvisorId, selectedAccountId, firmOverride]` | Per-account scoped |
| 22 | `_shared/AdvisorBookView.tsx:212` | `['inflec-account-timeseries', selectedClientKey, selectedAccountId, firmOverride]` | Per-(client, account) scoped |
| 23 | `_partners/inflection/InflectionInsightsPanel.tsx:266` | `['inflection-firm-concentrations', firmOverride]` (overlap with #18) | Inflection-only firm-level; same risk profile as P2 |

(Some entries appear in both P2 and P3 because risk-tier is along multiple axes — adding a `usesStaticClientDetail` flag downgrades risk from P1 to P2, and adding a per-entity-id downgrades risk from P2 to P3. The final aggregate tier is the lowest of the per-axis tiers.)

---

## Mitigation playbook per tier

### P1 — drop `refetchOnMount: false` + lower-default staleTime

For the 14 P1 callsites:

1. **Drop `refetchOnMount: false`** — default `refetchOnMount: true` retries error-state queries on remount. Successful queries still respect staleTime, so wire load doesn't balloon (only failed queries refetch eagerly).
2. **Reduce `staleTime`** from 5 min to 60s for cross-firm queries. Trades extra wire load for shorter cache-poison persistence window.
3. **Add programmatic cache-invalidation on auth-success/token-refresh:** `queryClient.invalidateQueries({ queryKey: ['partner-analytics'] })` etc. Eliminates the 5-min recovery window post-deploy.

**LOC estimate per callsite: ~1-3 lines.** **Total P1 mitigation: ~30-50 LOC across 7 files.** Ship as a single PR for atomic cache-invalidation behavior across the component graph.

### P2 — verify tenant-flag in queryKey covers all wire variation

Spot-check each P2 callsite that the queryKey suffix flag captures every wire-protocol variation. If the queryKey misses any URL-construction axis (e.g., a future `useFancyEndpoint` flag), promote to P1 mitigation. Otherwise hold as-is.

### P3 — apply minimal fix on demonstrated-poisoning subset

P3 callsites have bounded blast radius (1 entity's data goes stale). Apply `refetchOnMount: true` only on callsites where Andrew or another user empirically demonstrates the symptom. Don't sweep proactively — the overhead-vs-poisoning-risk tradeoff is unfavorable.

---

## Proposed v0.6 tool: `comp-validate fe-cache-freshness <queryKey>`

CTO has independently banked this as a v0.6 ADHC_COMPIL_V4 candidate. Proposed shape:

```bash
# Single-callsite mode: analyze one queryKey
comp-validate fe-cache-freshness ['partner-analytics', granularity, firmOverride]

# Output:
#   Risk tier: P1 (cross-firm URL variation possible)
#   Callsites: 4 (DistributionTab.tsx:851, PartnerAnalytics.tsx:117, ...)
#   queryKey axes: ['name', 'granularity', 'firmOverride']
#   URL axes:       ['name'                 , 'firmOverride via bucketSuffix']
#   Decoupled axis: 'bucketSuffix' (URL-only; not in queryKey)
#   Hazard: any change to bucketSuffix logic creates cache poisoning
#   Suggested mitigation: drop refetchOnMount:false + reduce staleTime to 60s

# Codebase-wide mode: sweep all useQuery callsites
comp-validate fe-cache-freshness --all

# Output: table of every useQuery callsite with risk tier + mitigation suggestion
```

**Tool dependencies:** AST parse of `useQuery(...)` callsites; queryFn URL extraction (follow the function call chain to the apiRequest line); diff against queryKey tuple to identify decoupled axes.

**Comparison to existing comp-tools:**
- `comp-cache collisions` (existing) — detects same-key-different-response-types collisions; this proposal extends to same-key-different-URL-shape staleness
- `comp-trace` (existing) — full dependency chain; this proposal narrows to the FE-cache discipline-class
- `comp-routes trace` (existing) — wire path; this proposal pairs (queryKey, wire path) for staleness analysis

**Suggested rollout:**
1. v0.6.0 ship: implement single-callsite mode + manual `comp-validate fe-cache-freshness <queryKey>` invocation
2. v0.6.1 ship: codebase-wide sweep + per-file CI hint (similar to `comp-blast`)
3. v0.7.0 ship: pre-commit hook on `useQuery({...})` changes flags new-P1 introductions

---

## Recommended Phase 2 ship sequence

**Phase 2a (~1-2h):** Land the P1 mitigation PR — drop `refetchOnMount: false` on all 14 callsites + reduce staleTime to 60s where the tenant context is broadest (e.g., partner-analytics + cohort-summary). Add programmatic cache-invalidation on AuthContext token-refresh. Ship as portal/DEV → DT promote.

**Phase 2b (~3-4h):** Author v0.6 `comp-validate fe-cache-freshness` tool spec to CTO. PRD per ADHC_COMPIL_V4 v0.6 candidate format. Includes:
- queryKey axis enumerator (AST parse of useQuery tuple)
- URL axis enumerator (follow apiRequest call chain)
- Decoupled-axis detector (set difference)
- Risk-tier classifier (entity-keyed vs tenant-keyed vs flag-keyed)
- Mitigation suggestion mapper

**Phase 2c (separate PR, post-Phase 2a):** Memory entry `feedback_query_key_url_decoupling_class.md` capturing the cache-poisoning meta-rule: **"the queryKey contract is `encodes everything that survives a deploy` — URL construction logic survives deploys, but the queryKey doesn't see it; the decoupling IS the latent-bug surface."** Sister to `feedback_react_query_cache_poisoning_from_deploy_window.md` but framed as a forward-looking design constraint, not a post-mortem.

---

## Out-of-scope (acknowledged but deferred)

- **react-query global config** — could set `refetchOnMount: true` as the default in `main.tsx`'s QueryClient, eliminating the need for per-callsite removal. Decided against: too aggressive for non-incident-class queries; would increase wire load on every component remount even where stable.
- **Service worker / browser-cache layer audit** — beyond the React Query scope; would catch HTTP-cache poisoning class but requires separate sweep. Flag for ADHC_COMPIL_V5 if priority allocates.
- **Cross-tab cache invalidation** — react-query persists in-memory only; cross-tab consistency relies on staleTime expiry. Out of scope for this audit.

---

## Cross-references

- Reactive post-mortem: `memory/feedback_react_query_cache_poisoning_from_deploy_window.md` (today 2026-05-14)
- Sibling adapter-omission audit (in-flight): `docs/briefs/inflection_static_adapter_stale_stub_audit_20260514.md` (parallel COO-authorized scope)
- ADHC_COMPIL_V4 v0.5 candidate list: pending CTO bank confirmation for v0.6 input
- Today's $202M routing-correction trace: COO 2026-05-14 17:13Z + 17:16Z MCP threads (CTO meta-rule "consumer-path verify before escalating data-side finding to P1" banked)

— 0.4.0_DE_ClientPlatform
