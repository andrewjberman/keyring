# Brief — Inflection Snapshot/Segment Analytics interval-asymmetric data gaps

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Audience:** 2.0.0_SA_COO (for decomposition into DS/AE/DE TOs)
**Trigger:** Andrew empirical 2026-05-14 12:17-12:18Z four-screenshot evidence pack
**Surface:** Inflection AdvisorIntelligence → Distribution tab → Segment Analytics → Snapshot view

---

## Empirical observations

Andrew toggled Snapshot Segment Analytics across all three intervals on the Inflection partner view (both ADV and GEO cohorts, NNA mode):

| Cohort | Interval | Surface state |
|--------|----------|---------------|
| ADV | **Month** | COMPLETE — donut shows 3 advisors (Peter 81.6% / Joe 8.2% / Patrick 10.2%); period strip 4 entries; right-panel NNA-Flows histogram populated with percentile markers + inflow/outflow split |
| ADV | **Quarter** | PARTIAL — donut shows 4 advisors (Patrick 100% selected, others 0.1%/-0.5%/0.0%); period strip 4 entries; **right-panel histogram MISSING** — placeholder "Select an advisor to view per-relationship NNA flow distribution" despite Patrick being the donut's highlighted segment |
| ADV | **Year** | EMPTY — "Analytics data unavailable" placeholder; entire panel blank |
| GEO | **Quarter** | PARTIAL — donut shows 6 states (CA $1.18M · 2.3%, HI $199K · 0.0%, etc.); period strip 4 entries; right-panel histogram MISSING — placeholder "Select a state to view per-relationship NNA flow distribution" |
| GEO | **Year** | EMPTY — "Analytics data unavailable" placeholder |

**Asymmetry pattern:** Month works fully → Quarter partially works (donut + period strip render; histogram doesn't auto-populate) → Year totally empty.

---

## Investigation findings

### Finding 1 — All 3 artifacts present on S3 with IDENTICAL top-level shape

```
s3://opal-data-inf/platinum/firm/partner_analytics_monthly.json    378,689 bytes
s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json  403,128 bytes
s3://opal-data-inf/platinum/firm/partner_analytics_annual.json     390,529 bytes
```

All three have:
- `views: { adv, aua, geo, nna }` (4 keys, identical)
- `views.nna.current: { adv, geo }` (2 keys, identical)
- `views.nna.current.adv: { distribution, donut, metrics }` (3 keys, identical)
- `views.nna.current.adv.donut.segments` length = 4 on all three
- `views.nna.current.adv.distribution.total` keys = `{count, histogram, inflow_count, inflow_percentiles, max, mean, min, outflow_count, outflow_percentiles, p25, p50, p75, percentiles, sum}` — identical superset

**The annual artifact is NOT structurally malformed at the gold-emit layer.** Same shape as monthly/quarterly.

### Finding 2 — Period keys differ per granularity (expected)

- Monthly: `views.nna.{current, m1, m2, m3}`
- Quarterly: `views.nna.{current, q1, q2, q3}`
- Annual: `views.nna.{current, y1, y2, y3}`

FE has explicit per-granularity period-key derivation at `DistributionTab.tsx:90-95` (`getHistoricalKeys(granularity)`). So the period-key suffix difference is anticipated.

### Finding 3 — FE empty-state gate fires when `analyticsData` is null

`DistributionTab.tsx:1020-1037`:
```tsx
{viewStyle === 'snapshot' ? (
  analyticsLoading ? <LoadingInline /> :
  analyticsData ? <SnapshotDistributionView ... /> :
  <p>Analytics data unavailable</p>
) : ...}
```

`analyticsData` is the result of `useQuery({ queryFn: () => getPlatinumPartnerAnalytics(granularity, firmOverride) })`. With `data: analyticsData = null` destructure default, the empty state fires when the query is in error state OR returns null.

### Finding 4 — Annual request must be failing in-browser despite valid S3 artifact

Combining (1)+(3): the annual artifact has correct shape on S3, but the FE's `analyticsData` resolves to null/undefined for annual. The query is **failing at the wire boundary** (request → response → parse), not at the consumer logic boundary.

Possible failure modes (need empirical narrowing):
- **(a) CloudFront `custom_error_response` returning SPA HTML for annual** — Lambda@Edge route mismatch on `partner_analytics_annual.json` could trigger 404/5xx; CF intercepts and returns the SPA index → `JSON.parse('<!doctype...')` fails → React Query treats as error → `data: null`.
- **(b) Shared-advisor-router Lambda@Edge** has a hardcoded allowlist of paths it routes for; `partner_analytics_annual.json` may not be in the list while monthly/quarterly are.
- **(c) NaN/Infinity in annual payload** — verified clean (0 occurrences); ruled out.
- **(d) Auth/session issue specific to the annual fetch** — unlikely since all three go through the same auth boundary.

### Finding 5 — Quarterly histogram missing is a SEPARATE bug

The quarterly screenshots show the donut + period strip rendering correctly (NOT an "Analytics data unavailable" state). The histogram in the right panel is empty with "Select an advisor/state to view per-relationship NNA flow distribution" placeholder.

In Month view, an advisor IS auto-selected (Patrick Scanlan highlighted in right-panel header) → histogram renders.

For Quarter view, no auto-selection happens → placeholder remains. Looking at `DistributionTab.tsx:809-816`:
```tsx
useEffect(() => {
  setGeoDrillLevel('state')
  setSelectedStateKey(null)
  setAdvDrillLevel('architect')
  setSelectedArchitectKey(null)
  // ...
}, [cohort, granularity])
```

**The granularity change resets `selectedArchitectKey` to null.** Toggling Month → Quarter clears the advisor selection; no re-selection happens automatically; histogram stays empty. Same code path runs for the cohort change but the user's manual selection on Month is wiped on Quarter switch.

### Finding 6 — Quarterly data shape is correct but visually unusual

Quarter ADV donut shows Patrick 100% / others 0.1%/-0.5%/0.0%. The `net_pct` math is `net / total_net`. If `total_net` over the quarter is dominated by Patrick (e.g., $721K with others netting near-zero offsetting flows), Patrick legitimately occupies 100% share. **Not a data bug** — the quarterly aggregate genuinely has different per-advisor NNA shapes than monthly. Worth a tooltip / explainer in the UI but not a data correctness issue.

---

## Hypothesis ranking

**Primary (most-likely-cause-of-Year-empty):**
H1 — **`shared-advisor-router` Lambda@Edge route allowlist gap** — the router constructs S3 paths for some `partner_analytics_*.json` suffixes but not `_annual`. Easy verify via CW logs on the Lambda@Edge for any `partner_analytics_annual.json` requests in the last hour.

**Secondary (failure-mode-candidates):**
H2 — CF `custom_error_response` returning SPA HTML on a Lambda@Edge 404/5xx; `JSON.parse` fails → null.
H3 — Browser cache poisoned with a stale 404 response from before annual artifact was published (DS~A `1d9848aab` ship today created annual artifact? Need to verify ship history).

**Quarterly-histogram bug (separate root cause):**
H4 — `DistributionTab.tsx:810-816` `useEffect` resets `selectedArchitectKey` on granularity change without re-populating from the new donut's top-segment. UX gap, not a data gap.

---

## Recommended TO decomposition

**Phase 1 — Empirical investigation (parallel, ~30 min each):**

1. **AE (CloudWatch metrics + Lambda@Edge logs)** — Pull last-hour CW metrics for `shared-advisor-router`; look for `partner_analytics_annual.json` 4xx/5xx responses for Inflection partner. Confirm or refute H1+H2. If 4xx: identify which route check rejects annual. If 5xx: pull Lambda exception logs.

2. **DT (route + behavior config)** — `comp-routes behaviors` audit; `comp-routes trace getPlatinumPartnerAnalytics` to map the CF path → Lambda@Edge → S3 bucket. Verify the route accepts all three `partner_analytics_{monthly,quarterly,annual}.json` patterns equally.

3. **DS~A or DS~C (artifact provenance)** — Confirm `partner_analytics_annual.json` ship lineage. Last gold-d chain (`chain_gold-d_20260514_141936`) produced all 3 artifacts at 14:20:26Z? If annual was produced LATER than monthly/quarterly OR has missing-key markers, that points to gold-side asymmetry.

**Phase 2 — Fix (gated on Phase 1 root cause):**

- **If H1/H2 (router/CF allowlist):** DT or AE fixes the routing config or `custom_error_response` rules; redeploys infrastructure-side. ~1-2h.
- **If H3 (cache poisoning):** AE invalidates CF cache for `partner_analytics_*` paths under `opal-data-inf`; DE adds defensive fetch retry on null response. ~30min.
- **If something else (e.g., DS-side ship missed annual emit):** DS retriggers gold-d chain with annual scope. ~30-60min.

**Phase 3 — Quarterly histogram auto-selection (separate, DE-owned, low priority):**

- DE — modify `DistributionTab.tsx:810-816` useEffect to NOT clear `selectedArchitectKey/selectedStateKey` on granularity change OR re-populate from new granularity's `donut.segments[0]` after clear. Single-file ~10-LOC change. Improves UX consistency. ~20min.

**Phase 4 — Quarterly data shape tooltip (DE, even lower priority):**

- DE — add tooltip on advisor donut explaining that per-advisor `net_pct` is share-of-total-firm-net, which can produce >100% / <0% per-segment values when aggregating positive/negative flows. ~15min, deferrable.

---

## Cross-references

- FE file: `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx:1020-1037` (empty-state gate); `:785-796` (analyticsData fetch); `:809-816` (granularity-change reset); `:90-95` (per-granularity period keys)
- FE adapter: `portal/src/api/endpoints/advisor-intelligence.ts:499-505` (getPlatinumPartnerAnalytics URL construction)
- L@E router: `infra/aws/lambda-edge/shared-advisor-router/index.mjs` (route allowlist + bucket construction)
- S3 artifacts: `s3://opal-data-inf/platinum/firm/partner_analytics_{monthly,quarterly,annual}.json` — all present at 2026-05-14 14:22:15-19Z (post chain_gold-d_20260514_141936)

## Compiler tools

| Tool | Status |
|------|--------|
| `comp-routes trace getPlatinumPartnerAnalytics` | RECOMMENDED for Phase 1.2 (DT) |
| `comp-routes behaviors` | RECOMMENDED for Phase 1.2 (DT) — surface CF `custom_error_response` rules that may mask 4xx → HTML |
| `comp-cache collisions` | Not applicable (single-key cache; already verified clean post-SHARED.006) |
| `aws s3 ls + jq` | DONE — empirical confirmation of artifact presence + shape parity |

## Andrew demo-readiness urgency

Year interval shows complete empty state — partner-visible regression. Quarterly histogram missing is UX gap but not blocking. Recommend Phase 1.1 (AE CW pull) as the fastest-to-diagnose probe; Phase 2 fix shape depends on what Phase 1 surfaces.

— 0.4.0_DE_ClientPlatform
