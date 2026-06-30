# INFREF FE headline repoint (_fresh -> canonical) + NFRA_TSGRAPH.P2-1 verified-complete

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-30 · **Window:** session start -> now

**Portal DEV commit:** `ad97d915`
**Workspace CLOUD commit:** (this log + P2-1 TO status flip)

## Summary

Two threads driven to close this session:
1. **INFREF FE repoint (Andrew-direct, COO-dispatched).** Repointed the AdvisorIntelligence
   PartnerAnalytics headline AUA tile off the being-removed `header_metrics_fresh.json` (INF_D_00e)
   onto canonical `getHeaderMetrics().total.aua`; removed the dead `getHeaderMetricsFresh` fn +
   `HeaderMetricsFreshResponse` type. FE-first ordering with ~A (de-risked the stale-_fresh window).
   Committed + pushed to DEV, CI green, CVO value-safe across all firms.
2. **NFRA_TSGRAPH.P2-1 (GO'd 2026-06-18, HIGH).** On resuming I found it already built+materialized
   (my prior commits `fbf8549b1` + `b47839cff`); VERIFIED it end-to-end against the LIVE Nessie graph
   (Rule 20: queried, not rebuilt). All 6 acceptance criteria MET; DERIVE-not-EMIT (COO~B at-parity
   contract) confirmed aligned with no re-architecture. TO self-marked complete; grain-map handoff to ~C.

## Thread 1 -- INFREF FE repoint

### Files Modified
| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx | headline AUA query `getHeaderMetricsFresh()` -> `getHeaderMetrics()`; `auaDonutTotal` prefers `headerMetrics.total.aua` (was `freshHeader.total_aua_fresh`); queryKey `['header-metrics', firmOverride]` shares cache w/ ClientsTab | Yes - DEV `ad97d915` |
| portal/src/api/endpoints/advisor-intelligence.ts | removed dead `getHeaderMetricsFresh()` fn + `HeaderMetricsFreshResponse` type (PartnerAnalytics was sole caller; repo-wide grep confirmed 0 others) | Yes - DEV `ad97d915` |

### Why / ordering
`header_metrics_fresh` (INF_D_00e) was the "frozen-but-fresh" workaround with a known false-freshness
defect; the freeze root is fixed (ADVI_BREAKS TO-2: INF_D_04 sole writer of `header_metrics.json`,
reliably fresh). FE-first ordering coordinated with ~A: tile off `_fresh` BEFORE the producer stops
emitting -> zero stale window. ~A's backend half (INF_D_00e removed from orion-gold-dispatch.sh + script
git-rm'd) is held uncommitted, folds into the inf-refactor cutover. Both halves RAVC-closed.

### Field-choice validation (CVO, value-grounded)
The nested `.total.aua` was the cross-firm-CORRECT field: 49F + cot have top-level `total_aua = None`
(value lives only in nested `total.aua`); had the repoint gone to top-level `total_aua`, 49F + cot would
render None and break. CVO grounded all 3 firms served: inf $202,125,678.08 / 49F $1,816,267,427.27 /
cot $432,464,116.36 -- all sane. Repoint VALUE-SAFE across firms; cross-firm residual CLOSED.
Residual: CVO live-rendered pixel pass on opalinvest.dev (creds-gated, CVO lane) -- data verdict HIGH-confidence landed.

## Thread 2 -- NFRA_TSGRAPH.P2-1 (page-rooted PAGE->PANEL->DRILLDOWN cluster extractor)

Extractor = `org/modules/graph/tsgraph_spike/cluster_extract.py` (additive post-pass over the P1
ts-morph emit `out/portal_full.graph.json`; emits Page/PanelCluster + CLUSTERS/CONTAINS_DRILLDOWN/SHARES_SOURCE
on the CloudNode/CloudEdge string-discriminator schema). Already materialized into canonical Nessie.

### Acceptance criteria -- VERIFIED against the LIVE HEAD-current graph
| AC | Result |
|----|--------|
| AC1 emit (page-rooted) | Page 15, PanelCluster 91; CLUSTERS 91, CONTAINS_DRILLDOWN 241, SHARES_SOURCE 55. Live census == local emit exactly (zero drift). PASS |
| AC2 community detection | 15 pages, sensible distribution (PortfolioManagement 18, TradeSubmission 13, AdvisorIntelligence 11). AI cluster:0 = 8 files over 15 sources spanning the 6-source superset. PASS |
| AC3 drilldown depth + cohort first-class | depth 1..4 (111/103/23/4); per-firm cohort populated (inflection 23, 49financial 3, demo 3, cottonwood 2). Carried in CloudEdge `props` JSON (canonical pattern). PASS |
| AC4 coverage 119/119, 0 silent | 118 assigned + 1 VISIBLE unresolved (`Attribution/constants/holdings-shared.tsx`, constants .tsx w/ no ReactComponent). PASS |
| AC5 additive schema | CloudNode/CloudEdge string discriminators + props; no schema break. PASS |
| AC6 session-log comp-tools | this section. PASS |

### DERIVE-not-EMIT alignment (COO~B at-parity #1)
Confirmed at the code level: `cluster_extract.py` emits node_types {Page,PanelCluster} + containment/
membership edges ONLY; NO `grain`/`level`/`referenceable` on nodes. The COMPUNIFY node_type->grain map
(~C-owned) derives grain; LEVEL derives from CONTAINS structure. No re-architecture needed -- the 4
COO~B sharpenings are framing, structure was already sound + at-parity (CTO parity-check 222927Z).
Grain-map registration of {Page,PanelCluster} + referenceable-target gate (rule 11) dispatched to ~C.

## Compiler Tools
| Tool | Target | Result | vs expect |
|---|---|---|---|
| `comp-kuzu` "MATCH (n) RETURN ... count" | node census | provenance: HEAD current (pin==marker), 18266n/30543e, age <0.1h. node_type breakdown: Field 4969, MS_FILE 4408, ... Component 199, PanelCluster 91, Page 15 | PASS (graph LIVE+current; rode it per <if_mismatch>) |
| `comp-kuzu` edge_type census | edge census | CONTAINS 5416 ... CONTAINS_DRILLDOWN 241, CLUSTERS 91, SHARES_SOURCE 55 | PASS (P2 edges materialized) |
| `comp-kuzu` per-page CLUSTERS | AC2 | 15 pages; AdvisorIntelligence 11 clusters (PortfolioManagement 18 top) | PASS |
| `comp-kuzu` edge/node `props` dump | AC3 schema model | CONTAINS_DRILLDOWN props={"cohort":null,"depth":2,"kind":"nested"}; PanelCluster props carry memberFileCount/sources/sourceCount. CloudEdge cols = edge_type/layer/snapshot_ts/props | PASS (attrs in props JSON, canonical) |
| `comp-cache collisions` | Phase-1 step2 + INFREF | 6 shared keys; `['header-metrics',firmOverride]` shared PartnerAnalytics<->ClientsTab (intended) | PASS |
| `comp-transform schema-check` | PartnerAnalytics (INFREF) | PASS -- all rendered fields match; 11 UNUSED pre-existing, none introduced | PASS |
| `bun run typecheck` (tsc -b --noEmit) | portal (INFREF) | exit 0 | PASS |
| `bunx eslint` (2 files) | portal (INFREF) | exit 0 | PASS |

**What worked:** comp-kuzu live-graph queries verified P2-1 acceptance without a rebuild (Rule 20);
comp-cache surfaced the intended ClientsTab cache-share that guarantees headline/Books consistency.
**What I'd note:** edge/node attrs in this unified schema live in a `props` JSON column (not first-class
Kuzu columns) -- `r.depth` fails; the data is in `r.props`. Worth a comp-kuzu helper for props-JSON
field extraction (the graph lacks SPLIT(); JSON-field query ergonomics are a small gap).

## Blockers
None. INFREF: only CVO's pixel-render residual (CVO lane, creds-gated). P2-1: complete; ~C grain-map
registration is a forward-coordination handoff, not a P2-1 gap.

## Next Steps
- **[3.0.0_SA_CVO]** live-rendered pixel pass of the inflection headline on opalinvest.dev (DEV) when creds/bandwidth allow -- final INFREF confirmation.
- **[0.8.0_AE_CloudComp~C]** register {Page,PanelCluster} grain in the COMPUNIFY node_type->grain map + confirm CONTAINS_DRILLDOWN/SHARES_SOURCE clear the referenceable-target gate (rule 11).
- **[0.4.0_DS_ClientPlatform~A]** backend INF_D_00e removal lands with the inf-refactor cutover (FE already off _fresh); `header_metrics_fresh.json` S3 object = Andrew-confirm cleanup-delete (now unread).
- **[2.0.0_SA_COO~B]** P2-3 (CLI query) / P3 sequencing vs my ADVI lane -- your + Andrew's call; P2-1 schema contract locked for downstream.
- **[0.4.0_DE, me]** event-gated; holding for next dispatch / P2-3-P3 GO or an ADVI task.
