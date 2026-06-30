# NFRA_GRAPHUNI.P0 — D1 COVERAGE AUDIT + per-tool GAP-LIST (= the P1 derive spec)

**TO:** NFRA_GRAPHUNI.P0 (org/projects/NFRA_GRAPHUNI/task_orders/NFRA_GRAPHUNI.P0.d1-audit-gaplist.md)
**Author:** 0.8.0_AE_CloudComp~D (Andrew-provisioned graph-unification build lane)
**Date:** 2026-06-30
**Status:** DELIVERED — read-only audit complete, ZERO mutation. RAVC2 -> COO~B, cc CTO + CVO.
**Scope guard honored:** AUDIT + gap-list ONLY. No derive, no re-point, no cache retirement (D2/D3/D4 await CTO PRD).

---

## 0. Grounding (the two sides of the diff)

| Side | Artifact | Vintage / head | Census |
|---|---|---|---|
| **Unified graph (target)** | Kuzu `kuzu_nessie_db` (Nessie-backed, marker-headed) | HEAD **current** (pin == marker HEAD); built 2026-06-30T19:34:59Z (age ~1h); nodes snapshot 1832939377093282234 | **18,216 nodes / 30,481 edges** |
| **comp-blast/trace/xref cache** | `.comp-graph/graph.json` (`TraceGraph`) | built 2026-06-29T17:49 | 2,143 nodes / 2,766 edges |
| **comp-platinum cache** | `.comp-graph/platinum.{routing,dataflows,dag.bd,dag.inf,dag.cot}.cache` (pickle `CachePayload.obj`) | fingerprinted (routing built 2026-06-30T14:08) | RoutingTable + 3 PipelineDAGs + dataflows list |

Provenance header read on every comp-kuzu call (Rule 20): **current**, pin == marker HEAD — the authoritative baseline, not a stale/scratch vintage.

---

## 1. Baseline — what the unified Kuzu graph HOLDS at the marker head

All 18,216 nodes carry one Kuzu label `CloudNode`; the class discriminator is the `node_type` + `layer` properties.

**Nodes by layer (node_type):**
- **aws (1,451):** IAM_POLICY 312, LOG_GROUP 200, LAMBDA 169, IAM_ROLE 145, EVENT_RULE 116, EVENT_SOURCE 82, API_ROUTE 77, SECRET 76, CW_ALARM 64, S3_BUCKET 35, DYNAMODB_TABLE 34, EC2_INSTANCE 31, SECURITY_GROUP 23, INSTANCE_PROFILE 17, SERVICE_PRINCIPAL 16, SNS_TOPIC 13, S3_BUCKET_POLICY 9, KMS_KEY 8, SQS_QUEUE 5, API_GW 5, VPC_ENDPOINT 3, ECS_TASK_DEFINITION 3, ROUTE53_RECORD 3, + 5 singletons (LOAD_BALANCER, ECS_CLUSTER, IAM_USER, CLOUDFRONT_DISTRIBUTION, STATE_MACHINE).
- **ms (5,427):** MS_FILE 4403, MS_FOLDER 1007, MS_USER 15, MS_SITE 1, MS_LIBRARY 1.
- **portal (11,338):** Field 4969, JSXElement 2205, JSXRender 1433, TypeDecl 807, ReactComponent 442, Module 374, Prop 359, Component 199, Endpoint 125, Hook 111, DataFetch 106, PanelCluster 91, ReactQueryKey 57, ServedURL 45, Page 15.

**Edges (`edge_type`, top):** CONTAINS 5411, OWNED_BY 5410, HAS_FIELD 4269, RENDERS 2447, READS_FIELD 2110, PROP_PASSES 1382, DECLARES 1344, INSTANTIATES 1298, REFERENCES_TYPE 1129, FLOWS_TO 961, READS 646, WRITES 543, PROJECTS_TO 442, HAS_POLICY 407, ... IS_ENDPOINT 106, ROUTES_TO 77, HAS_ROUTE 77, FETCHES 109, SERVED_FROM 29, READS_URL 48, INVOKES 40, TRIGGERS 113, EMITS_TO 119, PUBLISHES_TO 30 (48 edge types total).

**Decisive observations (the gap mechanism):**
- The portal layer is **frontend (JSX/TS) component-level** — this is the NFRA_TSGRAPH fold (ReactComponent / CONTAINS_DRILLDOWN / Component / Endpoint / DataFetch).
- The aws layer is **infra-resource-level** (Lambda, IAM, S3 **bucket**, EventBridge rule).
- **There is NO Python data-pipeline backend in the graph at all** — confirmed empirically: a name-match query for `A_00 | B_01 | INF_D_00 | accounts_dimension | canonical_holdings` returned **0 rows**; a query for `CALLS | IMPORTS | CALLS_FUNCTION` edge types returned **0 rows**.
- S3 is **bucket-granular** (node names = bucket names only); there is no key/artifact-level S3 node.

---

## 2. Cache side — what each tool TRAVERSES

### 2a. TraceGraph (`graph.json`) — comp-blast / comp-trace / comp-xref
- **Nodes (2,143):** GOLD_SCRIPT **1,340** (of which **1,204 are function-level**, `function_name` set, IDs like `gold:A_00.accounts_dimension:_list_txn_keys`; 136 script-level), LAMBDA 298, S3_ARTIFACT 288, ENDPOINT 133, EVENTBRIDGE 62, COMPONENT 22.
- **Edges (2,766):** **CALLS 1,624** (function->function), READS_S3 501, WRITES_S3 408, TRIGGERS 143, FETCHES 90.
- All 1,158 distinct CALLS endpoints resolve to node keys — a **complete function-level call graph of the gold (Python) data pipeline** + its key-level S3 IO.

### 2b. Platinum caches — comp-platinum (full-stack chain)
`CachePayload.obj` dataclasses in `org.modules.graph.extract_routes` / `extract_pipeline`:
- **RoutingTable** (`platinum.routing.cache`): `origins`(CloudFrontOrigin)×7, `behaviors`(CloudFrontBehavior)×23, `rewrite_rules`(RewriteRule)×10, `api_gw_routes`(ApiGatewayRoute{route_key,method,path,lambda_name,tf_file,pipeline})×21, `endpoints`(EndpointFunction)×123, `components`(ComponentBinding)×22, **`routes`(Route)×60 — the JOINED full-stack walk** url_pattern→cf_behavior→cf_origin→auth_edge→api_gw_route→lambda_handler→**s3_key**→endpoint_function→components.
- **ComponentDataFlow** list (`platinum.dataflows.cache`): component→`FetchBinding`{fetch_function, data_variable, response_type, hook_type, line, query} — the component→fetch→response shape.
- **PipelineDAG ×3** (`platinum.dag.{bd,inf,cot}.cache`): `scripts`(ScriptIO{script_id,group,run_order,reads,writes,read_keys,write_keys,pipeline})×30, **`s3_keys`(S3Key{constant_name,s3_path,is_prefix,is_function})×103**, `chains`×7, `groups`×4, `_writers`×82, `_readers`×83, `_implicit_writers`×11 — **the gold-script ↔ S3-key producer/consumer DAG**.

---

## 3. THE PER-TOOL COVERAGE GAP-LIST (this IS the P1 derive spec)

### comp-blast / comp-trace — gap = the ENTIRE gold-pipeline function graph
| Class the cache holds | In Kuzu? | Net-new fill |
|---|---|---|
| GOLD_SCRIPT **function-level** nodes (1,204 fn + 136 script) | **NO** (0 gold nodes) | **NET-NEW** node class — Python data-pipeline functions + scripts (file_path, function_name, run_order, group, pipeline, source_sha) |
| **CALLS** edges fn→fn (1,624) | **NO** (0 CALLS edges) | **NET-NEW** edge class — the function call graph |
| READS_S3 / WRITES_S3 at gold-**key** grain (909) | partial/diff-grain (Kuzu READS/WRITES are portal-field + bucket level) | **NET-NEW** at the gold-script→S3-key grain |
| S3_ARTIFACT (key-level, 288) | **NO** (Kuzu S3 = bucket-level only) | **NET-NEW** key/artifact-granular S3 |
| TRIGGERS EventBridge→gold (143) | partial (Kuzu TRIGGERS=113 are infra event_rule→lambda) | fill the gold-pipeline trigger edges |

### comp-xref — gap = SAME substrate as comp-blast (no separate index)
**Key finding:** `cli.py` confirms comp-xref reads the **same** `_CACHE_FILE = .comp-graph/graph.json`. Its symbol cross-reference (`_xref_symbol_lookup`) is a **lens over the TraceGraph function-level nodes** (definition site = the function node; reference sites = its CALLS / READS_S3 / WRITES_S3 edges). **There is NO separate symbol-index class to derive** — once the function-level GOLD_SCRIPT nodes + CALLS edges land (the comp-blast fill), comp-xref's symbol lookup is satisfiable over the same substrate. *Out of scope (do not fill):* comp-xref explicitly does not index the COMP_LEARNS corpus.

### comp-platinum — gap = the GOLD/backend HALF of the chain (front half already in Kuzu)
The **front half** (component→endpoint→fetch→lambda→bucket) **largely EXISTS** in Kuzu (portal Component/Endpoint/DataFetch/ReactQueryKey/ServedURL + aws LAMBDA/API_GW/CLOUDFRONT + edges IS_ENDPOINT/ROUTES_TO/FETCHES/INVOKES/SERVED_FROM/READS_URL) — and overlaps NFRA_TSGRAPH (see §4). The gaps:
| Class the cache holds | In Kuzu? | Net-new fill |
|---|---|---|
| **PipelineDAG**: ScriptIO + S3Key + chains/_writers/_readers (the S3-key→gold producer/consumer half = the chain's TERMINUS) | **NO** (chain dead-ends at the bucket; 0 gold nodes) | **NET-NEW** — shares the comp-blast gold-script node class; adds the producer/consumer DAG edges |
| **S3Key** (s3_path-granular, 103/firm) | **NO** (Kuzu = S3_BUCKET only) | **NET-NEW** key-level S3 (same fill as comp-blast S3_ARTIFACT — one shared class) |
| **Route** joined full-stack record (url→…→s3_key→…→gold) | pieces present, but un-traversable to gold + no key-level S3 binding | becomes **traversable end-to-end** once gold + key-S3 land. **CTO ruling needed:** store the denormalized join, or derive it via traversal? |

---

## 4. NFRA_TSGRAPH overlap — DE-DUP guidance for P1 (Ruling: do not double-derive)
NFRA_TSGRAPH is actively folding **component-level** into the portal layer — already present at head: ReactComponent 442, CONTAINS_DRILLDOWN 241, PanelCluster 91, Component 199, Endpoint 125, DataFetch 106, ReactQueryKey 57, ServedURL 45. comp-platinum's **front half overlaps this**. **P1 must NOT re-derive component-level** — TSGRAPH owns it. P1's net-new is strictly the **gold/backend half + key-level S3**.

---

## 5. Consolidated P1 derive spec (framed for Ruling 2 — ONE shared head-pinned graph for all four tools)
The unified graph must additionally hold (net-new, gold/backend half only):
1. **NODE** `GoldScriptFunction` (~1,204 fn) + `GoldScript` (~136 script) — Python data-pipeline backend. *CTO ruling: new `pipeline` layer, or an aws code sub-layer?*
2. **NODE** key-level `S3Artifact` / `S3Key` (s3_path-granular, ~288 artifacts; ~103-key-per-firm DAG) — refine/extend the existing bucket-level S3 (e.g. `S3Key OWNED_BY S3_BUCKET`).
3. **EDGE** `CALLS` (gold-fn→gold-fn, ~1,624) — the function call graph.
4. **EDGE** `READS_S3` / `WRITES_S3` at the gold-script→S3-key grain (~909) — pipeline IO. *Keep distinct from Kuzu's existing portal-field-level READS/WRITES — do not conflate the grain.*
5. **EDGE** gold-pipeline `TRIGGERS` (EventBridge→gold, ~143) if distinct from the infra-level trigger edges.
6. The platinum full-stack **Route** chain becomes end-to-end-traversable once (1)+(2) land; CTO to rule store-vs-traverse on the joined record.

**One-line:** the single net-new fill across all four tools is the **gold (Python) data-pipeline backend graph — function nodes + CALLS + key-level S3 IO — plus key-granular S3**. The frontend/component half (NFRA_TSGRAPH) and the aws-infra half (globgrph) already exist.

---

## 6. Acceptance-criteria attestation
- **AC1 — per-tool gap-list:** §3 (comp-blast/trace function-level, comp-xref = same substrate, comp-platinum full-stack gold half), with NFRA_TSGRAPH overlap noted (§4). The consolidated derive spec is §5.
- **AC2 — ZERO graph mutation, ZERO cache mutation:** every comp-kuzu call was a read `MATCH ... RETURN` (no CREATE/MERGE/SET/DELETE); every cache read was Python read-mode / `pickle.load` (no writes). `graph.json` + the platinum caches are byte-unchanged. (comp-kuzu's own provenance/marker self-heal + the comp-which rail dedup log are tool-internal telemetry, not graph/cache content.)
- **AC3 — RAVC2:** to COO~B, cc CTO (gap-list = the complete D1 derive spec per Ruling 1) + CVO (pairs with the P0-CVO fixture). Compiler-tools reproduction in the session log.

## 7. Residual unknowns / for CTO's D1 ruling
1. **Layer placement** for the gold-pipeline node class (new `pipeline` layer vs aws code sub-layer) — affects the derive/extract pipeline mapping.
2. **S3 grain model** — extend S3_BUCKET with child S3Key nodes, or a parallel S3Artifact class? (comp-blast S3_ARTIFACT and platinum S3Key are the same underlying object at the same grain — derive once.)
3. **Route join** — store the denormalized full-stack record, or derive by traversal once the terminus exists?
4. **Edge-grain disambiguation** — gold READS_S3/WRITES_S3 vs Kuzu's existing portal READS/WRITES must stay distinct `edge_type`s so a traversal doesn't cross grains.
