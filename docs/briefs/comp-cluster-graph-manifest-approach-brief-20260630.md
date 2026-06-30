# BRIEF: comp-cluster + graph-call-manifest registration approach (NFRA_TSGRAPH P2-3)

**Date:** 2026-06-30 | **Author:** 0.4.0_DE_ClientPlatform | **For:** 0.0.0_AB_MSTR
**Why:** Andrew steer -- MSTR is building a more developed approach; fold in what's reusable here.
**Status of the work:** built + verified locally; landing BLOCKED on a lane-discipline wall (see SS6).

## 1. What I built (P2-3)

`comp-cluster <Page>` -- a read-side comp-tool that renders the page-rooted **PAGE -> PANEL ->
DRILLDOWN** view of the portal component estate, querying the LIVE canonical Nessie->Kuzu graph
(Rule 20: query, never rebuild). It is the cloud-graph **generalization of comp-cache**: where
comp-cache surfaces React-Query *key* collisions, comp-cluster surfaces the full
component<->data-source coupling (the 6-source superset) + the drilldown subtree.

Modes:
- `comp-cluster AdvisorIntelligence` -> panel->drilldown tree (depth 1..4 + per-firm cohort fork) +
  per-cluster data-sources + cross-panel SHARES_SOURCE coupling
- `comp-cluster --list` -> every page + cluster counts + coverage
- `comp-cluster --coverage` -> page-tree coverage (118/119 assigned + 1 VISIBLE unresolved, 0 silent)
- `comp-cluster <Page> --json` -> structured

Reads the cluster layer materialized by P2-1 (extractor `org/modules/graph/tsgraph_spike/cluster_extract.py`)
-> P2-2 (AE derive into Nessie). Live graph carries: Page 15, PanelCluster 91; CLUSTERS 91,
CONTAINS_DRILLDOWN 241, SHARES_SOURCE 55.

## 2. Architecture (the reusable pattern)

- **Engine** `infra/aws/globgrph/comp_cluster_cli.py` MIRRORS `kuzu_cli.py`: opens the canonical DB
  (`_canonical.CANONICAL_DB_PATH`) read-only, calls `_canonical.ensure_fresh()` (auto-refresh on
  HEAD-advance), prints the `_provenance` header to stderr (current/BEHIND/UNKNOWN VINTAGE), results
  to stdout. So it inherits the whole freshness/provenance contract for free.
- **Wrapper** `.tools/comp-cluster` MIRRORS `.tools/comp-kuzu`: calls the engine + `comp_log_auto.py`
  (auto-logs to compiler-tools-log.md).
- **Query strategy:** the cluster layer is small (~106 nodes + ~387 edges), so I pull the whole layer
  in a handful of Cypher queries and assemble the tree in Python -- avoids Kuzu recursive-query
  complexity (the build lacks SPLIT()). Edge/node attrs live in the `props` JSON column (canonical
  CloudNode/CloudEdge schema: first-class cols = node_type/edge_type/layer/snapshot_ts/props), so
  depth/kind/cohort are parsed from props, not first-class columns.
- **Coverage computed independently from the live graph** (not trusting the extractor's report):
  denominator = Module nodes whose path is portal/src/pages/*.tsx (119); assigned = page .tsx whose
  ReactComponents appear as CONTAINS_DRILLDOWN endpoints; unresolved = the difference (enumerated
  VISIBLE, 0 silent). Reproduces 118/119 + 1 (Attribution/constants/holdings-shared.tsx).

## 3. graph-call-manifest.yaml registration approach

Two surfaces, kept in lockstep:
- **entries:** added `cloud.cluster.page_panel_drilldown` (use_case / canonical_call / tool / mode=query
  / layer=cloud / cost / freshness / rebuild_trigger / anti_pattern / status=canonical).
- **tools_index:** added a `comp-cluster: {does, subcommands, entries}` block.
- **Ledger relationship (key insight):** tools_index is a PROJECTION of the source-of-truth ledger
  `org/modules/graph/comp-coverage-map.yaml`. A tool in tools_index but absent from the ledger is DRIFT
  (CI guard `comp_coverage_view.py --verify`). ~C (0.8.0_AE_CloudComp~C, COMPUNIFY governor) had ALREADY
  registered comp-cluster in the ledger (granularity: cluster, distinct_from comp-cache) during the
  grain-map work -- so my manifest add is consistent, no drift (verify: 35/35 in ledger union of 47).

## 4. comp-which routing

Added a CURATED rule in `.tools/comp-which` (the `(keywords, label, [calls], desc)` tuple format) with
cluster-distinctive vocab (cluster/drilldown/cohort-fork/cross-panel/shares-source/...) so structural-tree
questions route to comp-cluster, not comp-transform's per-component schema-check. The manifest entry's
keywords also feed comp-which's fuzzy backstop. Routing regression test went 33/35 -> **34/35** (my change
fixed comp-cluster's self-routing; comp-transform unaffected).

## 5. Canonical edge vocabulary (CTO inv-2 ruling 22cb21116, DERIVE-not-EMIT)

The extractor emits node_types + containment/membership edges ONLY; it does NOT emit grain/level/
referenceable -- those DERIVE from the COMPUNIFY node_type->grain map (~C-owned). CTO ruling:
- CONTAINS_DRILLDOWN -> canonical CONTAINS at portal `component` level (depth IS the level; portal =
  4th CONTAINS producer); native producer label stays, the coverage-map canonicalizes.
- CLUSTERS (Page->grouping) + SHARES_SOURCE (coupling) = distinct edge_types.
- Nodes Page (page-grain/L1) + PanelCluster (cluster-grain/L2) registered referenceable (~C, 811398a28).

## 6. The lane-discipline finding (why landing is blocked -- relevant to how MSTR folds this)

The owned-paths pre-commit gate (block mode) BLOCKS me (a DE) on two of the four files:
- `infra/aws/globgrph/comp_cluster_cli.py` -> lane CLOUD_OPS_OR_ETL (AE-only).
- `org/modules/graph/graph-call-manifest.yaml` -> lane ANY_EXEC (CTO/COO/CVO only).
(`.tools/comp-cluster` + `.tools/comp-which` are `comp-`/`comp_` basename-exempt -> allowed.)

So a DE can author a comp-tool's logic + wrapper, but cannot land the engine into the AE infra lane or
register it in the exec-owned manifest. Options for MSTR's developed approach:
  (a) engine relocates to a DE/ANY-permitted comp-engine home (e.g. org/modules/graph/, where the other
      comp-* engines live -- but it imports _canonical/_provenance from infra/aws/globgrph, so it'd
      shell out to `comp-kuzu --json` instead of importing kuzu directly);
  (b) an exec/AE lands the infra engine + manifest entry (the TO's `<consult>DT</consult>` + COO's "DT
      consult" framing points here);
  (c) a lane grant for the comp-tool-authoring case.
This is a structural question your "more developed approach" may want to settle generally: who owns
comp-tool authoring vs comp-tool landing, given engines need infra-lane imports + exec-lane manifest reg.

## 7. Verification status (all PASS except the pre-existing comp-drift gap)

- comp-cluster AdvisorIntelligence -> real tree (matches the actual page: BooksTab/ClientsTab,
  AdvisorBookView, AdvisorAnalytics, AdvisorsTab leaderboard, the inflection cohort fork). PASS.
- comp-manifest-check -> exit 0. comp_coverage_view --verify -> clean (35/35). 
- comp-which routing test -> 34/35 (comp-cluster self-routes; lone FAIL = **comp-drift**, PRE-EXISTING,
  confirmed by stash-revert -- its self-query routes to comp-aws, no overlap with my keywords). Worth a
  separate fix (comp-drift unreachable via comp-which) -- flagging, not in P2-3 scope.

## 8. Reusable artifacts for MSTR

- The kuzu_cli-mirroring engine template (canonical DB + provenance + auto-refresh) for any new
  live-graph read-tool.
- The coverage-from-live-graph computation (independent of the producer's self-report).
- The manifest entry + tools_index + ledger-projection lockstep pattern.
- The comp-which curated-rule format + the routing regression test as the acceptance gate.
- Files in my working tree (uncommitted, lane-blocked): comp_cluster_cli.py, .tools/comp-cluster,
  .tools/comp-which (+rule), graph-call-manifest.yaml (+entry/tools_index). Available to lift wholesale.
