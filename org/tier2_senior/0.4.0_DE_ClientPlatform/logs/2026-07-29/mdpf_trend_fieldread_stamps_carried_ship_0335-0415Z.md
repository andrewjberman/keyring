# 0.4.0_DE_ClientPlatform — Global trend field-read + as-of stamps + carried idiom SHIPPED (0335-0415Z delta)
**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE

## Window
Delta since the 0335Z log. Drivers: COO carried-point APPROVAL 033922Z (+heavier border), Andrew-direct
~0340Z ("I want the fucking MDPF page sorted immediately for global aum-timeseries") via CTO 034050Z,
Andrew-direct as-of-stamp rulings (~0345Z via COO 034711Z + 034843Z correction: "WHATEVER THE DATA'S
AS-OF IS, THAT IS THE DATE DISPLAYED"), operator mid-turn instruction to nudge DT+CTO with results.

## Shipped (portal DEV f6c1181247512ea473d018fa82b50ae2baac25b9, pushed ~0400Z; CTO-VALIDATED 040618Z,
## COO D4 PASS 040506Z -- COO half CLOSED; DT Oracle-1 + second promote pending)
One commit, three ruled changes (COO ships-together):
1. TREND FIELD-READ: Global aggregate rows = artifact opal_aggregate_aua per date; Non-Model band =
   non_model_aua per date; both tooltips anchor on producer total via total_aua rows (daily tooltip
   DOM-verified $1.95B, was composed $1.91B; Non-Model $278M artifact basis); Q-end priorLevels = oaa
   at last real point <= quarter end. DELETED: by_model client-sum, getNonModelAumForDate roll-forward
   (both builders), YANG deep-tail (oaa-model) derive + MDPF_ESTIMATE_BASIS_END, non_model_assets.json
   fetch, legacy aum-timeseries fetch (last consumer was a stamp-fallback leg), Global graceful-degrade
   trend branch, 3 dead helper fns. isLoading re-keyed to canonical fetch SETTLING. Pre-cut control:
   identity oaa == model_aua + non_model_aua verified to the cent on all 426 valued dates.
2. CARRIED-POINT IDIOM (approved build from prior window + heavier band border per COO).
3. AS-OF STAMPS: Portfolio Analytics footer = as_of_last via PanelFooter dataAsOf prop (CAUGHT in own
   render: the timestamp prop parses date-only as UTC midnight -> "July 26th 8:00p" for 07-27 data --
   NEVER#11 class, fixed + documented); per-element "Model detail as of X - Client Holdings as of Y"
   beside it; Non-Model (Last update) = last real non_model_aua period; Global methodology string
   corrected (page no longer rolls anything forward -- old string would be a false methodology claim).

Exercised: happy path (live platinum fixture) all limbs; forced-failure control (canonical dead +
legacy alive) => headline em-dash + AUA Trend panel ABSENT entirely (COO: "strongest control run
tonight"). typecheck clean / lint 0 errors / provenance guard PASS / SURFACE_ACK ^-anchored in the
pushed message.

## Census amendment (workspace 72c80472d5, pushed @ 2af488ee1c)
COO's D4 review of MY OWN control screenshots exposed an under-disclosed finding, accepted without
qualification: the Q-cell `enterpriseQ ?? metricsData.priorLevel` is a LIVE FALLBACK doing a SILENT
BASIS SWITCH (Q2 renders $1.77B canonical-alive vs $1.76B canonical-dead) -- upgraded to census C6,
ranked TOP of the teardown wave's client half, above B1-B4. +C7: getNonModelAssets() portal-proxy.ts
:399-406 now aims at the object AE~A deleted ~0352Z (fetcher at a 404), same wave.

## Shared-worktree merge episode (workspace CLOUD)
compiler-tools-log.md conflicted on push; a CONCURRENTLY-STAGED resolution in the shared tree embedded
a live conflict marker (>>>>>>>) -- refused to conclude it; rebuilt the union CLEAN from both parents
with marker assertions, concluded via the documented GIT_COMMIT_AUTHOR_OVERRIDE (audited) because the
merge tree carries a COO log file authored by the REMOTE side, pushed 2af488ee1c. Auto-appended tool
rows (MSTR/CTO/DE hook lines) swept in a chore commit to unblock the merge.

## MCP traffic
~10 handled this window. Significant: COO 033922Z approval + as-of finding; CTO 034050Z Andrew-direct
build order; COO 034711Z stamps-in-scope + 034843Z correction; my push notifications to DT 040241Z /
CTO 040256Z / COO D4 package 040321Z (operator-ordered nudges); COO D4 PASS 040506Z; CTO validation
040618Z; my census-amend confirm 040710Z.

## Blockers
None. Two external waits, evidence-cited, owners named: DT Oracle-1 + second promote (CTO stand-by
order: fix immediately if CI/oracle throws); second-change members GATED on that promote + Andrew's
render (CTO: do not start).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-surface-check (pre-commit, blocking) | pairedProvenanceRead.ts + ModelPortfolios.tsx | PASS w/ SEV1 ack | fired on headline+benchmark surfaces; SURFACE_ACK audited + carried ^-anchored in the pushed message |
| provenance-read-guard | src/** | PASS | after readGlobalEnterpriseSeries added (non_model_aua read lives INSIDE the allowlisted module) |
| ui-smoke | /portfolios x4 | PASS | happy + forced-fail + hoverlast DOM oracle ($1.95B) + stamp-fix re-render (caught the UTC-midnight off-by-one) |
What worked: the identity pre-verification (426/426 to the cent) before deleting the composition; the
forced-fail control as the census instrument (it caught C6). What failed: first stamp attempt used the
PanelFooter timestamp prop (UTC-midnight off-by-one) -- caught in the screenshot, which is the
/frontend-dev law working. Gap: none new.

## Current State (zero-prior-context)
- portal DEV == origin/DEV == f6c11812 (working tree CLEAN). PROD at 1f363956 / v2.1.149 (first
  promote); second promote of f6c11812 is DT's, pending Oracle-1.
- workspace CLOUD == origin/CLOUD == 2af488ee1c (census amend + log sweep + clean union merge).
- Global MDPF page: headline + trend + band + tooltips + Q priorLevels + stamps ALL field-reads of
  platinum/mdpf/global/aggregate-aua-timeseries.json; no legacy fetches remain on the page except
  aum-metrics.json (B1: donut model slices, Q cell deltas, counts -- queued second change) and
  account-distribution.json (bell curve).
- Second-change queue (CTO-sequenced, gated on promote + Andrew render): C6 Q-cell basis-switch
  (top), FactorTilts catch-zeros, codeMap interim (canonicaliser + N-of-N loud assert; blends
  declared-excluded + labeled), B1 teardown, C7 dead fetcher deletion.

## Next Steps
1. [0.2.0_DT_PortfolioAnalytics] Oracle-1 on served bundle + second promote -- I fix immediately on
   any throw (CTO order).
2. [0.4.0_DE_ClientPlatform] on promote + Andrew render: await CTO GO for second-change members.
3. [2.0.0_SA_COO] D4 closed its COO half; nothing waiting on me.
