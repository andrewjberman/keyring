# NFRA_TSGRAPH.P2-1 -- page-rooted component-cluster extractor (PAGE->PANEL->DRILLDOWN)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Session:** 2026-06-18 (~16:15-16:50Z) · **Agent:** 0.4.0_DE_ClientPlatform · **TO:** NFRA_TSGRAPH.P2-1 (LEAD, pending) · **Commit:** `fbf8549b1`

## Current State

Spawned for the NFRA_TSGRAPH P2/P3 DE lane. Startup clean (registered, watcher armed task `bgehtd449`,
P1 already closed by COO per CTO 2-step, extract_routes handoff closed by CTO). COO GO'd P2-1 (the LEAD;
P2-2/P2-3 gate on it). Built + validated + committed the cluster extractor.

**What landed (`fbf8549b1`):**
- `org/modules/graph/tsgraph_spike/cluster_extract.py` -- the P2-1 cluster extractor. An ADDITIVE post-pass
  over the P1 full-portal emit (`out/portal_full.graph.json`, whose portal-node counts == the LIVE canonical
  Nessie census -- verified). Rides the live HEAD-current substrate (Rule 20, no rebuild); the cutover-signed
  P1 ts-morph extractor is untouched.
- `load_clusters_scratch.py` -- loads base ReactComponent + the additive layer into a scratch Kuzu on the
  EXACT platform schema (CloudNode/CloudEdge) for the Phase-2 mandate validation.
- `out/portal_clusters.producer.json` -- the P2-2 AE derive interface (106 nodes / 386 edges, additive).
- `out/portal_clusters.report.json` -- coverage + per-page panel->drilldown report.

**Model (Andrew-steered, PRD section 9):**
- **L1 Page (15)** -- feature-dir route-root per `portal/src/pages`.
- **L2 PanelCluster (91)** -- **dominant-source community detection**: each data-bearing file joins the cluster
  keyed by its MOST-DISTINCTIVE (lowest page-local fan-in) data source; presentational files attach to their
  dominant render-ancestor by majority vote (non-merging). This replaced two failed approaches -- (a) pure
  connected-components and (b) hub-threshold union-find -- both of which collapsed AdvisorIntelligence into one
  20-25 member giant cluster because source-rich tab files (DistributionTab ~3900 lines of useQuery) transitively
  chain every panel. Dominant-source assignment has no transitive chaining -> real panels separate.
- **L3 Drilldown** -- `CONTAINS_DRILLDOWN` render subtree (depths 1-4), `*Modal`/`*Detail` + per-firm `_partners`
  cohort FIRST-CLASS (cohort + kind + depth on the edge).
- **SHARES_SOURCE (55)** -- cross-panel coupling (shared data source OR shared non-ubiquitous type); generalizes
  `comp-cache collisions` (RQ-key-only) to the 6-source superset.

**Validation (AdvisorIntelligence, the richest page -- AC2):** decomposes into the real panels -- Books family
(AdvisorBookView + AdvisorBookAccountModal/ClientDetail + Tax/Fee panels, d1->d4 nesting), Advisors/Leaderboard,
Analytics (AdvisorAnalytics + charts), Distribution, PartnerAnalytics, cohort wrappers. Tree matches the real
component structure.

**Coverage (AC4):** 119/119 page `.tsx` PROCESSED -- 118 clustered, 1 VISIBLE-unresolved
(`Attribution/constants/holdings-shared.tsx` -- a constants `.tsx` with no JSX-returning component), 0 silent.
The no-silent-Unknown guard fires on a real non-component file rather than absorbing it into a hollow singleton.

**Schema (the P2-2 AE interface, sent 164715Z):** additive `node_type {Page, PanelCluster}` +
`edge_type {CLUSTERS, CONTAINS_DRILLDOWN, SHARES_SOURCE}` on CloudNode/CloudEdge -- no schema break.
CONTAINS_DRILLDOWN targets the EXISTING `rc:{path}#{name}` ReactComponent nodes (join key; AE MERGEs, no dup nodes).

## Blockers
None. P2-1 TO held at `pending` (NOT complete) -- full close = after AE P2-2 materializes the layer + I
verify the cluster edges present on the LIVE canonical graph (the PRD acceptance spans P2-1+P2-2). RAVC2
checkpoint sent to COO (164747Z, CC implied), schema to AE (164715Z).

## Next Steps
- **[0.7.0_AE_CloudOps]** P2-2: materialize the additive layer via the derive runner (re-zip the 6
  Dockerfile-COPY'd files before start-build per the globgrph S3-source-ZIP gotcha). Ping me with any schema concern BEFORE building.
- **[0.4.0_DE]** On P2-2 materialize: verify cluster edges on the LIVE comp-kuzu canonical surface (HEAD current),
  re-test the recursive `CONTAINS_DRILLDOWN*0..` form there (the local kuzu pkg segfaults on it). Then full P2-1 RAVC2 close.
- **[0.4.0_DE]** ADVI_NNAATTR TO-2 -- standing by for COO GO (parallel/next ready task).
- **[2.0.0_SA_COO]** P3-2 stays gated on P3-1 (CVO catalog pending, 37 classes checkpointed).

## Compiler Tools

| Tool | Run | Result vs `<expect>` |
|---|---|---|
| `comp-kuzu` (Phase-1 census) | `MATCH (n) RETURN n.node_type AS kind, count(*)` (corrected from the TO's `labels(n)[0]`, which returns empty on this single-table CloudNode schema) | PASS -- Field 4969 / Component 199 / RENDERS 2447 / PROP_PASSES 1382 / READS_FIELD 2110 / FLOWS_TO 961 / FETCHES 109 -- matches `<expect>` exactly. Header `current` (pin==marker HEAD, built 13:13Z age 3.1h). |
| `comp-cache collisions` (Phase-1) | `comp-cache collisions` | PASS -- 5 shared-RQ-key groups (all AdvisorIntelligence: advisor-nna-canonical x3, firm-leaderboard x4, partner-analytics x2, timeseries-overview x2, advisor-book-view x2). Generalized to the 6-source `SHARES_SOURCE` superset (not RQ-key-only) per the `<if_mismatch>` guidance. |
| `comp-kuzu` (Phase-2, scratch) | `load_clusters_scratch.py` -> platform-schema scratch Kuzu; per-page `Page -CLUSTERS-> PanelCluster`; CONTAINS_DRILLDOWN depth distribution; cohort/kind props; SHARES_SOURCE sample | PASS -- 15 pages/91 clusters; depths 1(111)/2(103)/3(23)/4(4); 72 two-hop + 27 three-hop CONTAINS_DRILLDOWN chains traverse; cohorts {inflection:23,49financial:3,demo:3,cottonwood:2}. **FINDING:** the locally-installed `kuzu` python pkg SEGFAULTS (exit 139) on recursive-rel traversal (`-[*0..]->` with a `rels(path)` edge-type filter) -- same build-limitation class as the TO-noted `SPLIT()` absence; validated nesting via bounded explicit joins instead. Recursive form to be tested on the comp-kuzu canonical surface (different/newer build) post-materialize. |
| `ruff` (gate, py39 pin 0.15.11) + `py_compile` | `ruff check --target-version py39` + `py_compile` on both .py | PASS -- 0 errors (fixed F841 unused var + F541 f-string). |
| Phase-3 (after commit) coverage | `coverage.unresolved` over the 119-file page tree | PASS -- 119/119 processed, 1 enumerated VISIBLE-unresolved with reason, 0 silent. Output byte-stable (md5 identical across 3 runs after fixing a vote-tiebreak + set-iteration nondeterminism). |

All P2-1 `<compiler_tools_mandate>` `<run>`s reproduced above with observed output vs `<expect>`.
