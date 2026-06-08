# PRD-request / Methodology Brief — Global Opal Graph: versioned, analyzable, agent-queryable

**Author:** 0.7.0_AE_CloudOps (CMPAWS build lead) · **Date:** 2026-06-08 · **Trigger:** Andrew-direct expansion of CMPAWS (sovereign session goal) into a versioned graph data-platform + the **global Opal graph** (cloud + portal frontend + inter-system edges).
**Status:** DRAFT methodology brief for CTO (formal PRD + schema) + COO (project registration + decomposition). Candidate code: `ADHC_GLOBGRPH` (COO/Andrew assign).
**Builds on:** `comp-aws` (CMPAWS, Wave-1 CVO-certified full-marks 2026-06-08) + the existing `comp-graph` portal/pipeline substrate (`org/modules/graph/`).

---

## 0. Andrew-locked decisions (2026-06-08)
1. **Stack posture = serverless-light** (no idle clusters). 2. **Versioning = Nessie git-branching** catalog over Iceberg. 3. **Structural graph first**; CloudTrail activity layer is a deliberate phase 2. 4. **Scope = the GLOBAL Opal graph** — begins with the cloud, expands to the portal web frontend + the inter-system edges that connect them. 5. Snapshot persistence as gzip tarball confirmed; dedicated S3 bucket wanted.

## 1. Vision
`comp-aws` establishes the **map** (a typed, ARN-keyed graph of the AWS cloud, reconciled live-vs-terraform-state). This project turns that map into a **living, versioned, queryable knowledge graph of all of Opal** — one graph from a React chart in the portal down through its API route, CloudFront behavior, Lambda@Edge, S3 data key, gold script, DynamoDB table, IAM role, KMS key, and the dollar cost — with **daily versioning, diff/delta analytics, and audit-grade time-travel**, indexed for **rapid agent traversal**.

Three concerns, three right-sized layers: **versioned STORAGE** (Iceberg + Nessie), **ANALYTICS/diff** (in-process for the tiny structural graph; Trino for the big activity layer), **fast QUERY** (embedded Kuzu graph DB).

## 2. The global graph = union of two existing substrates + inter-system edges
| Layer | Source | Node classes (examples) | Status |
|---|---|---|---|
| **AWS-resource** | `comp-aws` (CMPAWS) | S3_BUCKET, IAM_ROLE, EC2_INSTANCE, LAMBDA, EVENT_RULE, DYNAMODB_TABLE, CLOUDFRONT_DISTRIBUTION, KMS_KEY, ... (13 classes, 841 edges) | BUILT + Wave-1 certified |
| **Portal/pipeline** | existing `comp-graph` (`extract_routes`/`extract_api`/`extract_transforms`/`extract_pipeline`; comp-trace/blast/transform/routes/platinum) | PORTAL_COMPONENT, API_ROUTE, REACT_QUERY_KEY, S3_DATA_KEY, GOLD_SCRIPT, SILVER_SCRIPT, TRANSFORM | EXISTS (pipeline+portal layers) |
| **Inter-system edges** | NEW (this project) | n/a | NEW |

**Inter-system edge taxonomy (the stitch — CTO schema):** `CLOUDFRONT_DISTRIBUTION -[SERVES]-> PORTAL_BUNDLE`; `PORTAL_COMPONENT -[FETCHES]-> API_ROUTE`; `API_ROUTE -[ROUTES_TO]-> LAMBDA|APIGW`; `PORTAL_COMPONENT -[RENDERS]-> S3_DATA_KEY`; `S3_DATA_KEY -[DERIVES_FROM]-> GOLD_SCRIPT`; `GOLD_SCRIPT -[WRITES]-> S3_BUCKET`; `LAMBDA -[READS/WRITES]-> {S3_BUCKET|DYNAMODB_TABLE}`. comp-routes/comp-platinum already resolve much of the CloudFront->auth->S3-key->component path — this formalizes those as typed cross-layer edges into one store. This realizes CMPAWS-PRD sec6 ("comp-aws POPULATES the existing comp-graph") at full scope.

## 3. Versioning methodology (Nessie git-branching over Iceberg) — Andrew's choice
- **Iceberg tables** `graph_nodes` + `graph_edges` (+ later `graph_activity`), each row stamped `snapshot_ts / run_id / tf_commit / layer{aws|portal|pipeline|inter}`. Partitioned by `snapshot_date`. ARN (or resolved-id) is the stable node key; `(source, target, edge_type)` the edge key.
- **Nessie** is the transactional catalog providing **git semantics on the WHOLE graph**: every daily derive is an atomic **commit** across all tables (nodes+edges committed together = a coherent global-graph state, never a half-written graph); **tags** mark known-good audit baselines (`audit-baseline-2026-06-08`); **branches** model a proposed change's blast radius without touching `main`. This catalog-wide atomic versioning is *why* Nessie over plain Iceberg-table-branches — the global graph spans domains and must version as one unit.
- **Deployment (serverless-light reconciliation):** Nessie = one small **Fargate** task + **DynamoDB** backing store (the only non-zero-idle footprint, ~few $/mo, scale-to-zero-capable). Writes/reads via **pyiceberg** (native Nessie-catalog support) in-process. **No query cluster for the structural graph.** (Engine note: Athena talks Glue not Nessie, so Athena is NOT the structural-layer engine — pyiceberg+DuckDB in-process is; Trino-on-Nessie is deferred to the phase-2 activity layer. Fallback if zero-idle is later required: Iceberg-native Glue table branches/tags, losing catalog-wide atomic commits.)
- **Time-travel / audit:** "what did the global graph look like on date X / at ref Y" = a Nessie ref + Iceberg snapshot. Incident forensics: diff `main@incident-1h` vs `audit-baseline` -> exact blast radius + drift attribution.

## 4. Analytics / diff layer
Recomputed each commit, in-process (DuckDB over pyiceberg-loaded Arrow — the structural graph is ~few-hundred nodes):
- **`graph_changes`** — diff vs prior commit: `{snapshot_date, change_type: ADDED|REMOVED|MODIFIED, layer, entity: node|edge, key, class, drift_class_before->after, what_changed}`. The audit timeline.
- **`graph_metrics`** — per-day summary numbers + day-over-day deltas: per-class node/edge counts, drift-class distribution (DECLARED/LIVE-no-DECLARED/...), untyped count (must stay 0), inter-system edge counts, security-finding tallies (overperm/IMDSv2-optional/unencrypted/unmanaged-policy), and (phase 3) cost. **These are the "key summary number deltas."** Natural alarm surface: new LIVE-no-DECLARED resource, untyped>0, a node deleted, unmanaged-policy count rose, a portal->cloud edge broke.

## 5. Agent query layer (embedded Kuzu)
Build a Kuzu property-graph DB from the latest commit (nodes->node tables typed by class, edges->rel tables typed by verb). Embedded (single file, in-process, Cypher), rebuilt on demand from the latest snapshot (cheap), cached locally + S3-published. Agents traverse the **global** graph: *blast radius of bucket X up to the portal components that render it; every gold script feeding a given chart; shortest path portal-component->IAM-role; all unmanaged resources reachable from role Z.* Complements (does not replace) comp-trace/comp-blast — Kuzu is the unified indexed substrate for rapid-fire cross-layer insight.

## 6. Pipeline + where it runs
Scheduled `comp-aws derive` (+ a `comp-graph` portal/pipeline extract + the inter-system stitch) -> canonical JSON -> **(a)** gzip tarball -> S3 archive bucket, **(b)** rows -> Iceberg via pyiceberg, committed to Nessie `main` -> in-process `graph_changes` + `graph_metrics` -> Kuzu rebuild. Runner: scheduled **Fargate** task (clean, no 15-min cap, narrow read-only role) preferred over Lambda (would need a broad account-wide read grant + the derive parallelized under 15min). Reuses the EC2/Fargate scheduled-runner pattern.

## 7. Phasing
- **P1 (structural, now):** dedicated S3 snapshot bucket (Terraform, shared-infra) + comp-aws snapshot wired to it; Iceberg `graph_nodes`/`graph_edges` + Nessie (Fargate+DynamoDB); daily commit + `graph_changes`/`graph_metrics`; Kuzu build. AWS-resource layer only.
- **P2 (global):** fold in the comp-graph portal/pipeline layer + the inter-system edge taxonomy (CTO schema) -> one unified versioned graph + Kuzu.
- **P3 (enrich + activity):** per-resource cost (CUR/CE -> NFRA tie-in), security posture as node attrs, and the **CloudTrail activity layer** (`graph_activity`, the big-data table where Trino-on-Nessie earns its keep) — who-did-what-to-which-resource over time.

## 8. Cost / right-sizing (NFRA discipline)
Idle footprint = one small Nessie Fargate task + DynamoDB (~few $/mo) + S3 storage (pennies — years of ~50KB daily snapshots). No idle Trino/Spark/Kuzu server. Compute = the scheduled derive (minutes/day) + pay-per-query DuckDB/Trino-on-demand. The expensive scale only arrives with P3 CloudTrail activity, deliberately gated.

## 9. Open items for CTO (schema) + COO (decompose)
- **CTO:** the inter-system edge vocabulary (sec2) + the portal/pipeline node classes formalized into the CMPAWS schema (one closed vocabulary across all layers); the global node-identity rule across layers (ARN for cloud, resolved path/name for portal/pipeline).
- **CTO/Andrew:** confirm Nessie-on-Fargate vs the Glue-native-branch fallback; confirm Fargate-derive-runner vs Lambda.
- **COO:** register `ADHC_GLOBGRPH` (or assigned code); decompose P1 TOs; sequence vs the CMPAWS Wave-2 cert queue (this P1 reuses the comp-aws derive, so it can proceed in parallel once Wave-2 fan-out is CVO-paced).
- **CVO:** the versioned graph + `graph_changes` become a *new* audit substrate — the cert oracle for "the graph correctly versions" (snapshot N reproduces, diff N->N+1 is correct).

## 10. Why this matters (the audit case Andrew named)
A versioned global graph + diff history is the cloud's **black-box recorder**: when something breaks, query "what changed between the last-good baseline and the break" -> instant cross-layer blast radius + drift attribution, spanning portal-symptom -> API -> Lambda -> data-key -> gold-script -> bucket -> role. Today that's a multi-agent manual trace; this makes it one Cypher query against a time-traveled graph.
