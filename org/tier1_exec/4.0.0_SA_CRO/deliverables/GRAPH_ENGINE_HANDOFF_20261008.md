# HANDOFF -- the shared graph's engine decision (Kuzu is archived)

**UPDATE 2026-10-08 ~17:4xZ -- ANDREW HAS RULED: (a), stay on Kuzu for now.** Verbatim, in the last addendum of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
@9932790e65: "4.) A for now, also i dont think its actually frozen youre just not accounting for the stitch functions."
**Correction that follows:** "archived" applies to the Kuzu SOFTWARE package (no new releases after 0.11.3). The served
graph's DATA is not frozen. Measured from the projection manifests, 2026-10-01..10-08: 290 projections; a full nightly
build every night; the stitch layer (`derive_stitch.py`, stitch-codebuild) re-derived nightly at ~03:01Z on every night
10-03..10-08, while 10-01 and 10-02 carried the 09-30 stitch. Read "frozen" below as "the engine gets no upstream
fixes", never as "the graph is stale". The seat this handoff was written for owns only a LATER trial (LadybugDB),
if Andrew asks for one. Nothing here blocks folding the activity records into the served graph on Kuzu.

**From:** `4.0.0_SA_CRO`, 2026-10-08 ~17:0xZ. **To:** the CRO seat Andrew spawns for it. **Order:** Andrew, verbatim in
`ANDREW_DIRECT_20261008_170xZ_CALL1_HOOK_EVERY_BOX_YES_CALL2_ENGINE_TO_NEW_CRO.md` (same folder): "Call 2, i will spawn
another CRO agent to drive this, just write a handoff on it."

## The decision Andrew owns

What the shared graph runs on, given that its engine's makers have stopped maintaining it. The CTO's draft PRD outcome
is FWD-7 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/GRAPH_COHERENCE_ENDPOINT_DRAFT_20261008.md`. It is DONE when the
choice is written down with Andrew's word on it, stating plainly that Kuzu is no longer updated and what each option
costs the other outcomes.

My recommendation, carried on the card Andrew passed to you: **(a) stay on Kuzu 0.11.3 for now and run one ad-hoc trial
build of the same projection on LadybugDB**, then decide on what that trial shows.

## What is known

| Fact | Claim | Source |
|---|---|---|
| Kuzu archived 2025-10-10. PyPI banner: "This project has been archived by its maintainers, and is no longer receiving any updates." Last release 0.11.3, 2025-10-10. | READ | pypi.org/project/kuzu, read 2026-10-08 ~15:4xZ |
| The cloud worker pins `kuzu==0.11.3` and refuses any other minor version ("Cypher dialect is the contract"). | READ (sub-search) | `projection_worker.py:303` |
| **The Kuzu database is disposable.** Each projection is built from the Iceberg tables `graph_nodes` and `graph_edges` (Nessie `main`): full nightly at about 02:1xZ (849-985 s), incremental after CloudTrail events (33-76 s). Switching engines therefore moves no data. The cost is the loader, the refresh, the server and the comp-tools' Cypher. | READ | `kuzu_nessie_load.py:162-175`; `kuzu_incremental_refresh.py`; projection manifests 10-04..10-08 |
| The schema is one node table `CloudNode(node_id, arn, node_type, name, layer, drift_class, source, snapshot_ts, props)` and one edge table `CloudEdge`. A kind is a property, not a label. 29,586 nodes, 63,213 edges. | READ | `comp-kuzu`, 2026-10-08 |
| Clients that speak Cypher to it: `comp-kuzu`, `comp-find --corpus aws`, `comp-describe`, `comp-depth`, through the gateway `mcp.opalinvest.dev/graph/cypher` (bearer `opal/mcp/graph-read-token`). | READ (sub-search) | research @f4cac7f3dc section 3.3 |
| LadybugDB is the most active fork: v0.21.2 on 2026-10-01, v0.21.1 on 09-30, v0.21.0 on 09-29. Its release notes do not mention Kuzu 0.11 migration. v0.20.0 added "GQL in an extension". Its site calls it "DuckDB for graphs". | READ (releases page); the rest from secondary sources | github.com/LadybugDB/ladybug/releases |
| Other forks: RyuGraph (Predictable Labs; activity possibly stalled after 2026-01), Bighorn (Kineviz; activity disputed), Vela Partners' fork (concurrent multi-writer). | secondary, NOT verified | web search 2026-10-08 |
| Kuzu's 0.11 single-file format is not a stable interchange format. Migrate by logical export and import, which for us means rebuilding from Iceberg. | secondary | oneuptime.com, 2026-08-12 |
| A security note: an engine with no upstream fixes is riskier when untrusted users can submit Cypher. Ours takes Cypher from bearer holders only, read-only. Widening the bearer to the Dells (fast fix F1, `2.0.0_SA_COO~C`) widens the set of submitters to trusted seats. | INFER | -- |

## Options, as I would frame them for Andrew

1. **Stay on 0.11.3, pinned (CHOSEN, Andrew ~17:4xZ).** Costs nothing now. Risk: no fixes; a Python, OS or runtime upgrade may break the wheel.
2. **Move to LadybugDB.** Cost: the loader, the refresh and the server, plus re-testing every comp-tool's Cypher. Run it
   first as one ad-hoc QA build. A standing side-by-side build would be a shadow pipeline (CLAUDE.md NEVER), so it is
   not an option.
3. **Serve the same questions as SQL over Trino.** No graph engine at all. Cost: every Cypher client is rewritten, and
   Trino is in-VPC only, so the gateway would need to proxy it.

## How it touches the activity build

It does not block it. The activity layer (`.tools/fabric-activity.py`, being built by `4.0.0_SA_CRO`) stores its
records as JSON in `s3://opal-313476888478-globgrph/fabric/activity/v1/` and joins them to the graph at query time.
Folding those records into the served graph waits on this decision, so whichever engine wins inherits one more loader
input, not a migration.

## Not read

- No trial of any fork. The forks' GitHub commit histories beyond LadybugDB's releases page. The licence of each fork.
- `projection_worker.py` and `projection_server.py` beyond the pins and headers.
