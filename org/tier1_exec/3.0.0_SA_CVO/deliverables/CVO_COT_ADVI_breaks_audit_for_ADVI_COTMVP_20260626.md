# CVO Breaks-Audit: Cottonwood (COT / ADVI_COT*) data + portal -> seed PRD ADVI_COTMVP

**Owner:** 3.0.0_SA_CVO | **Date:** 2026-06-26 | **Dispatch:** Andrew-sovereign (via 0.0.1_UA_mstools) | **To:** 1.0.0_SA_CTO
**Method:** pipescript advi-cot + comp on COT platinum + source-read of the live portal component/layout/endpoint.
**Grounding discipline:** Rule 22 -- each causal claim cites its grounding; INFERRED is labeled and is NON-actionable as proof.

## Architecture (grounded -- pipescript advi-cot + s3)
- Producer: `cot-bd-session-trigger` (4-phase EventBridge SM) + `cot-exporter` EC2 -> `data/cot/scripts/{bronze,silver,gold}`.
- Served (cottonwood = `opal-data-cot/platinum/firm/`, firm-scoped by the advisor-intelligence Lambda FIRM_CONFIG):
  `partner_analytics_{annual,quarterly,monthly}.json`, `timeseries_overview.json`, `timeseries_chart.json`,
  `header_metrics.json`, `cumulative_chart.json`, `mix_summary.json`, `dashboard.json`, `clients-tab-slim.json`.
- Frontend: `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` ("Assets Overview" header panel,
  INTERVAL toggle Month/Quarter/Year), tenant layout `_partners/cottonwood/layout.ts`, endpoints `api/endpoints/advisor-intelligence.ts`.
- Cottonwood tenant shape (layout.ts): `barChart.stacked=false`, `auaDonut.source='gold_aua'` => **49F-pattern single-series** (NOT the Inflection stacked path); `tabs.partnerAnalytics.defaultViewMode='geo'`, `routes.defaultTab='distribution'`.

---

## SYMPTOM 2 -- /books tab has no display path  [ROOT CAUSE: GROUNDED]
**Location:** `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts:58-72`.
**Grounded root cause (source-confirmed, layout.ts):** /books is **deliberately disabled for COT v1** --
`tabs.books.enabled=false`, `advisorDrill.enabled=false`, `advisors.enabled=false`, and `routes.tabs` exposes
ONLY `distribution`. The cited reason (OUTCOME-B, ADVI_PRTORG §6.1 + §5-A.1): COT v1 has **no segmentable advisor
dimension** -- 2 founder joint-coverage rep codes account for ~96% of AUA, so the Books tab (built around
advisor-drill) has no drill targets. This is by-design, not a bug.
**Fix shape for the PRD:** two options for pod4 -
  (A) a **firm-level Books view** that does NOT require the advisor-drill dimension (revenue-ops / tax-cost-basis /
      fee-efficiency / concentration panels already exist as 'standard' in the layout -- render them firm-aggregated,
      no advisor breakdown); OR
  (B) keep disabled until the COT advisor dimension materializes (the layout's REVISIT-LATER path -- flip the flags,
      zero structural change). Recommend (A) for ADVI_COTMVP if a books surface is wanted in v1; the panels are
      already standard-configured, only the advisor-drill is unavailable.

---

## SYMPTOM 1 -- PartnerAnalytics YEAR + QUARTER views do not display  [easy causes RULED OUT w/ grounding; exact blank needs browser repro]

### What is RULED OUT (each grounded):
1. **NOT missing data.** All 3 granularity artifacts are served + populated (s3 ls + content pull, 2026-06-26 11:12):
   `partner_analytics_annual.json` (120KB, aua seg=3 / geo seg=13 / ofc seg=1), `partner_analytics_quarterly.json`
   (120KB, same populated views), `timeseries_overview.json` with `aua.{annually:1, quarterly:1, monthly:3}` rows,
   each carrying `categories:['NMNC','NMEC']`. Year/quarter data EXISTS at the source.
2. **NOT an endpoint naming mismatch.** `getPlatinumPartnerAnalytics` (advisor-intelligence.ts:368) maps
   `granularity==='annually' ? 'annual' : granularity` -> `partner_analytics_annual.json` (the served name). Correct.
3. **NOT the `.quarters` schema landmine.** All 3 `inflecTimeseriesChart.quarters` accesses (PartnerAnalytics.tsx
   :381,405,422 -- cottonwood's `timeseries_chart.json` has NO `quarters` key, a divergent schema) are GATED behind
   `usesStackedBars`, which is FALSE for cottonwood (layout `barChart.stacked=false`). So this path never executes
   for COT -> no crash here. (It IS a latent landmine for any future COT path that flips stacked on -- see below.)
   For non-stacked COT, `allSortedAuaPeriods` falls to the `timeseries_overview` fallback (:458-459) which returns
   the year/quarter data -> the static trace shows the AUA bar SHOULD render a single $401M bar for year/quarter.

### CONFIRMED concrete defects in the vicinity (source/served-grounded -- fix regardless):
- **(D1) Stock/flow unit inconsistency in NMNC across granularities (timeseries_overview.json, served).**
  annually 2026 NMNC=$401,437,408.55, NMEC=0; quarterly 2026-Q2 NMNC=$401,437,408.55 (IDENTICAL), NMEC=0;
  monthly 2026-04 NMNC=$168,717.70 (n=3 monthly points). The annual/quarter figure is ~2,380x the April monthly
  figure and annually==quarterly to the cent -> year/quarter report a STOCK (the cumulative AUA booked as "new
  money" for a just-onboarded firm) while monthly reports incremental FLOW. NMEC=0 across all grans (no existing-
  client mass). This is a producer (D_00/D_01) NMNC semantics bug -- a year/quarter bar of $401M next to ~$0.5M of
  monthly flow will read as wrong/broken to a user even though it "displays."
- **(D2) `timeseries_chart.json` schema divergence.** COT emits `{aua,nna,adv,geo,ofc,...}` with NO `quarters` key;
  the shared component's Inflection path expects `.quarters`. Inert today (gated by stacked=false) but a
  cross-tenant-code TRAP: any COT layout/feature change that enables stacked bars will hit an unguarded
  `undefined.length` at :381 -> hard render crash. Recommend the PRD harden these to optional-chaining +
  schema-guard regardless.
- **(D3) Data-sufficiency / young-tenant UX.** COT has ~3 months of history -> Year view = exactly 1 bar (2026),
  Quarter view = exactly 1 bar (2026-Q2). A single bar with no time series reads as "not displaying" vs the
  3-bar monthly view. If this is the user-perceived symptom, the fix is a UX treatment (insufficient-history
  message, or auto-select monthly / disable year+quarter until >=N periods), not a data fix.

### The exact blank: INFERRED, needs pod4 browser repro (NOT asserted as proof)
The static trace of the primary AUA-bar path (PartnerAnalytics.tsx:379-475, 1080) does NOT reproduce a hard blank
for non-stacked COT -- the data flows and the render gate (`aggregatedAuaData.length>0 && barCategories.length>0`)
is satisfied. So the user-visible blank is most plausibly one of (INFERRED, ranked):
  (a) the **GEO donut / GEO view** at year/quarter granularity (COT `defaultViewMode='geo'`, lands on Distribution
      tab) -- a different render path than the AUA bar I traced; check the GEO `views.geo` snapshot per-period at
      year/quarter in `partner_analytics_{annual,quarterly}.json`;
  (b) a **runtime fetch/scope failure** in the deployed env (CloudFront error-rule masking a JSON 4xx, or X-Firm-Id
      JWT scope) -- not visible in static source; OR
  (c) the **D3 single-bar** perception above.
**pod4 repro recipe:** load the COT tenant ADVI page as a cottonwood-scoped user, open DevTools Network+Console,
toggle Interval Year -> Quarter -> Month, and capture (i) which view (AUA bar / GEO donut / NNA) is blank, (ii) the
exact failing request or thrown error, (iii) the served JSON the component received. That pins the exact line; I did
not assert it because the served artifacts + static trace do not ground a specific blank, and Rule 22 forbids an
inferred mechanism standing as root cause.

---

## Recommended ADVI_COTMVP scope (for CTO)
1. **D1 (producer NMNC stock/flow)** -- highest correctness value; year/quarter showing a $401M stock-as-NMNC bar
   is the most likely "looks broken." Fix the COT gold NMNC aggregation to a consistent stock-or-flow semantic across
   grans (align to the 49F exemplar's convention).
2. **Symptom 2 /books** -- decide (A) firm-level books view vs (B) await advisor dimension.
3. **D2 schema-guard hardening** -- optional-chain the `.quarters` accesses + add a tenant-schema guard (prevents a
   future COT crash).
4. **D3 young-tenant UX** -- insufficient-history treatment for year/quarter.
5. **pod4 browser repro** to pin Symptom-1's exact blank view/line (recipe above) before coding the fix.

Grounding artifacts: served pulls (partner_analytics_*, timeseries_overview/chart), layout.ts, advisor-intelligence.ts:368,
PartnerAnalytics.tsx:379-475/730/1080, pipescript advi-cot. cottonwood ETFS cert (separate) unaffected.
