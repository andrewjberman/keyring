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
1. **Layer placement** for the gold-pipeline node class (new `pipeline` layer vs aws code sub-layer) — affects the derive/extract pipeline mapping. *[CTO ruled: new `pipeline` layer.]*
2. **S3 grain model** — extend S3_BUCKET with child S3Key nodes, or a parallel S3Artifact class? (comp-blast S3_ARTIFACT and platinum S3Key are the same underlying object at the same grain — derive once.) *[CTO ruled: one S3Key class, `OWNED_BY` S3_BUCKET, derived once.]*
3. **Route join** — store the denormalized full-stack record, or derive by traversal once the terminus exists? *[CTO ruled: derive by traversal, no denorm.]*
4. **Edge-grain disambiguation** — gold READS_S3/WRITES_S3 vs Kuzu's existing portal READS/WRITES must stay distinct `edge_type`s so a traversal doesn't cross grains. *[CTO ruled: distinct edge_types; seam-taxonomy invariant for COO~B.]*

---

## 8. AMENDMENT (Andrew-direct 2026-06-30) — the `pipeline` layer is the FULL process architecture, not gold-only
The gold layer is the **heaviest** sub-population but NOT the whole layer. The `pipeline` layer must capture the entire tier ladder across all pipelines.

**Grounded current coverage (the gap is bigger than gold):**
- TraceGraph (comp-blast/trace/xref cache) is ~99% gold-only: `black_diamond/gold` 723 + `inf/gold` 603, + token mdpf (gold 6 / backfill 8 / feeders 3 / bronze 1). **ZERO silver, ZERO bronze, ZERO cot.**
- comp-pipescript `_build_dag` covers `bd-gold / bd-silver / inf-gold / inf-silver / inf-manual-api` — gold + silver for bd/inf only; **no bronze, no ingestion, no cot/mdpf.**
- extract_pipeline.py docstring = "authoritative I/O mapping for **gold** scripts" (gold-anchored; `[bronze]`/`[silver]` are labels, not built DAGs).

**The real architecture (on disk): 4 pipelines × the tier ladder.**
| Tier | Role | Example scripts | Status |
|---|---|---|---|
| **ingestion / feeders** | external → S3 raw (lineage SOURCE) | `mdpf/feeders/wsb_49f_smartx_model_aua.py`, `inf/bronze/pull_eclipse_portfolios.py`, `bronze/orchestrator.py` | **net-net-new** (no tool extracts it) |
| **bronze** | raw → bronze conversion | `bd/bronze/convert_schwab_acc_to_parquet.py`, `convert_schwab_lots_to_silver.py` | **net-new** |
| **silver** | dedup + dtype standardization | `bd/silver/build_bd_assets_dim.py`, `build_interpolated_prices.py` | partial (comp-pipescript bd/inf only) |
| **gold** | business logic (heaviest) | `A_00.accounts_dimension`, `INF_D_00.*` | audited (§3) |

(Pipelines: **bd, inf, cot, mdpf**. cot + mdpf are near-entirely absent from current extraction.)

**Derive-spec changes:**
- Generalize the node class `GoldScript`/`GoldScriptFunction` → `PipelineScript`/`PipelineFunction` with declared attributes **`tier` ∈ {ingestion,bronze,silver,gold}** and **`pipeline` ∈ {bd,inf,cot,mdpf}**.
- Add **ingestion-source** extraction (the feeders/orchestrators) — the lineage origin.
- The grain-pure `READS_S3`/`WRITES_S3` edges carry **cross-tier lineage** (ingest→bronze→silver→gold via S3 keys) — that chain IS the process architecture.
- Extractor scope: extract_pipeline.py generalizes from gold-anchored to **tier-agnostic across all 4 pipelines** + new ingestion extraction.

## 9. AMENDMENT (Andrew-direct 2026-06-30) — STABLE node/edge definitions across granularities (the governing invariant)
**The core discipline as we dive deeper: granularity is a DECLARED DIMENSION, never an ad-hoc re-typing.** A deeper dive (script→function→statement; bucket→key→object) ADDS instances within a FIXED node/edge type system — it must never fork the schema. This is the NFRA_TSGRAPH node-schema discipline + the COMPUNIFY `{concern, granularity, surface, distinct_from}` node schema, applied to the pipeline layer.

**The proven pattern (TSGRAPH, grounded at head):** TSGRAPH carries a stable containment hierarchy where coarse→fine grain is expressed by STABLE edge types, not by re-typing nodes: `MS_FOLDER -CONTAINS-> MS_FILE` (5,411), `Module -DECLARES-> Component/TypeDecl` (1,344), `TypeDecl -HAS_FIELD-> Field` (4,269), `Component -CONTAINS_DRILLDOWN-> sub-component` (241). The node concept stays stable per level; the edge DEFINITION is grain-stable.

**Applied to the pipeline layer (the schema-stability contract):**
1. **Granularity = declared attribute + containment edges, not new types.** `PipelineNode` family with `{tier, level ∈ pipeline/script/function, pipeline}`; a stable `CONTAINS` ladder (`Pipeline -CONTAINS-> Script -CONTAINS-> Function`) lets you zoom depth without re-typing. Add a deeper level (e.g. statement) = a new `level` value + CONTAINS edges, NOT a new node type.
2. **Edge types defined once by SEMANTIC, stable across grain.** `CALLS` = fn→fn at any depth; `READS_S3`/`WRITES_S3` = the same producer/consumer relation whether the endpoint is a script or a function (disambiguate by node grain, the edge semantic is fixed). CTO ruling 4 (distinct edge_type per grain) generalizes into a STABILITY contract: define an edge type by its semantic, keep it stable as levels are added — never overload one type across two semantics, never split one semantic into ad-hoc per-depth types.
3. **Governance coupling:** these definitions live in the COMPUNIFY map's node schema (the ~C S0 apex, `comp-coverage-map.yaml`) so granularity + non-redundancy are gate-checked. GRAPHUNI (substrate) POPULATES the stable definitions; COMPUNIFY (map) GOVERNS them — the coupling Andrew identified.
4. **The risk this kills:** if each deeper dive invents node/edge types, you get semantic fragmentation inside one physical graph — the exact failure GRAPHUNI/COMPUNIFY exist to prevent. Stable, granularity-parameterized definitions = the contract that makes diving deeper safe.

*Routed to CTO (elevates ruling 1 + requests ratification of the schema-stability contract) + COO~B (program + the COMPUNIFY node-schema coupling). Build stays CVO-fixture-gated.*

---

## 10. AMENDMENT (Andrew-direct 2026-06-30) — the FRACTAL-granularity model + the missing drilldown seams
**Each layer is a granularity STRATUM; a coarse resource node drills down into its fine internal structure via stable drilldown edges. The same shape repeats fractally at every level.** This is the concrete mechanism under amendments 8+9.

**Grounded keystone example (EC2 ↔ pipeline):** the 31 `EC2_INSTANCE` nodes ARE the named pipeline runners — `inf-gold-qa-runner`, `mdpf-daily-runner`, `cot-exporter`, `canonical-schwab-runner`, `inf-bronze-runner`, `historical-prices-fetcher`, `bd-49f-auto-login`, `astn-wsjft-scraper`. At the RESOURCE grain (all Kuzu holds today) they edge to `READS/WRITES S3_BUCKET`, `READS_SECRET`, `HAS_PROFILE`. But INTERNAL to `inf-gold-qa-runner` is the whole sequence of `INF_*` Python scripts (raw→processed). The drilldown edge `EC2 -RUNS-> PipelineScript` **DOES NOT EXIST** (verified: the EC2's only edges are resource-grain). That missing edge is the fractal seam between the aws-resource stratum and the pipeline-compute stratum.

**The fractal chains to build (drilldown = the new seams):**
```
EC2_INSTANCE -RUNS-> PipelineScript -CONTAINS-> PipelineFunction -CALLS-> ... -READS_S3/WRITES_S3-> S3Key
S3_BUCKET   -CONTAINS/OWNED_BY-> S3Key        (CTO ruling 2 -- same fractal pattern, object grain)
LAMBDA      -CONTAINS-> handler functions
```

**Grain-consistency rollup invariant — EXISTENTIAL AGGREGATION (CTO-ratified semantics, NOT 1:1 equality):** a coarse edge EXISTS iff at least one fine edge rolls up to it — `EC2 READS S3_BUCKET` is supported iff EXISTS a PipelineFunction inside it (via `RUNS`+`CONTAINS`) that `READS_S3` some `S3Key OWNED_BY` that bucket (the coarse edge = the OR-rollup of the fine edges). Two checkable defect classes: **(i) UNSUPPORTED** — a coarse edge with ZERO supporting fine edges (the coarse claim has no fine basis); **(ii) COARSE-INCOMPLETE** — a fine edge whose rolled-up coarse target is ABSENT (the coarse stratum is missing an edge the fine layer implies). A contradiction in either direction = a grain defect. Generalized COMPDRIFT seam invariant (cross-grain rollup parity) — banked into COO~B's seam-taxonomy.

**The two-phase action (Andrew):**
1. **GRAPHUNI builds the fractal substrate** (~D lane) — the `RUNS`/`CONTAINS`/`OWNED_BY` drilldown edges stitch the resource stratum to the compute stratum; these are net-new seams.
2. **THEN the COMPUNIFY tool-calibration sweep** (~C map + ~D + CTO arch) — tag every comp-tool with the grain it operates at + returns, verify the set spans the ladder with no grain-confusion: `comp-aws` = resource; `comp-pipescript` = script/IO; `comp-blast/trace/xref` = function; `comp-platinum` = cross-grain traversal. ~C's `comp-coverage-map.yaml` already carries `granularity` as a node-schema field — this populates + gate-checks it. *Cross-lane; routed to CTO for decomposition + the GRAPHUNI<->COMPUNIFY grain-calibration coupling.*

---

## 11. CTO RATIFICATION REFINEMENTS (authoritative — the gate tests P1 builds against)
Both amendments (8+9) RATIFIED by CTO (msg 205242Z). Two authoritative refinements thread into the build + gate:

**A. Population phasing (sequencing guard, NOT a scope cut).** The SCHEMA is the full ladder from the start (so we never re-type — that IS Amendment 2). The POPULATION phases by tier:
- (i) **GOLD tier = no-regression-CRITICAL** — it's what the 4 structure-tools traverse today + the D2 fixture baseline. Land it FIRST (or same-pass if clean).
- (ii) **bronze / silver / ingestion = net-new ENRICHING lineage** — can't regress the tools' answers (the caches never held it). Enriches; phases after gold.
- The full-ladder ambition must NOT delay the gold-tier re-point D2 needs. Full-ladder SCHEMA from the start; POPULATION phases without re-typing.

**B. Ruling-4 <-> Amendment-2 reconciliation (the explicit gate test).** They are COMPLEMENTARY, not in tension — ruling 4's distinction is by SEMANTIC, not depth. The gate test:
> different RELATION/semantic -> different `edge_type`; SAME relation at different depth -> SAME `edge_type` + a `level` attribute; NEVER split one semantic by depth.
- `READS_S3` (S3-object producer/consumer) stays distinct from portal-field `READS` (different SEMANTIC).
- `READS_S3` stays ONE type whether the endpoint is a script or a function — `level` carries the grain.

**C. Governance gate (confirmed).** GRAPHUNI POPULATES the stable defs; COMPUNIFY GOVERNS them. The `comp-coverage-check` gate (one_home = surface|seam x granularity x concern) extends with the `level`/granularity dimension + the no-split-by-depth stability rule. ~C threads the stability contract into the COMPUNIFY node-schema gate; COO~B coordinates (also a COMPDRIFT seam invariant). The substrate<->map coupling, gate-enforced.
