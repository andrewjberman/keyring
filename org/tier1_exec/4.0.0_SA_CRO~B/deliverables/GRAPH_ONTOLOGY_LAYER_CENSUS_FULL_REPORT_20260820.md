<!-- genesis-surface: ATOM_LAYER0 -->
# GRAPH ONTOLOGY LAYER CENSUS — FULL REPORT

**Seat:** `4.0.0_SA_CRO~B` (CRO~B)
**Requested by:** Andrew-direct, 2026-08-20
**Program:** ATOM_LAYER0, Path B — resolution / representation census
**Status:** COMPLETE; final reconciliation includes Pass 3 and C7, with no shared graph or ontology mutation
**Initial evidence pin:** `8d5532311db24dea0452f1e36f478da3e0276587`
**Delivery revalidation pin:** `9b4151ac4576d4a6d09aafd30e37a30e63e6eb61`
**Definition reconciliation pin:** `00edd984c7` (`SYSTEM_DEFINITIONS` v3.15)
**Pass 3 code-grain pin:** `b30b05d006` (assessment vintage `f36d572be864e56b9175caac06b01f62fc141e2a`)
**C7 process-generated D3 pin:** `f9e4ff4459` (input vintage `b30b05d006`)
**Live graph observation window:** 2026-08-20 18:29–19:01Z

---

## 0. Executive conclusion

The ontology is conceptually one system but operationally served from three representation planes:

1. **Ratified canon** — stable definitions and declared class/name populations in
   `SYSTEM_DEFINITIONS.yaml`, `NFRA_ONTOLOGY_RULE_BANK.yaml`, and
   `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml`.
2. **Persisted graph state** — Iceberg `graph_nodes` and `graph_edges` on Nessie `main`, projected
   into local Kuzu as the generic `CloudNode` / `CloudEdge` dialect.
3. **Resolver-served world model** — `estate-coverage-resolver.json` plus canon, assembled by
   `comp-estate` into vertical, structure, matrix, and chain views.

The C ladder describes progressively composed structure:

```text
C0 facts -> C1 interactions -> C2 recurring motifs -> C3 systems
                                                    ├─ C3.i discovered deterministic structures
                                                    └─ C3.ii declared semantic verticals
```

The D rails describe the fidelity carried between adjacent C rungs:

```text
C3
 ^  D3 contract / obligation
C2
 ^  D2 path / flow
C1
 ^  D1 value / grain
C0
```

The central physical fact is that Iceberg does **not** have one table per ontology layer. C0, C2,
and C3.i are all represented as rows in `graph_nodes`; C1 and D1 are represented in
`graph_edges`; C2/C3 membership is represented through `CONTAINS` edges. C3.ii and D2 are primarily
resolver/canonical views, not dedicated Iceberg tables. D3 now has three explicitly distinct
carriers: generic ontology `contract_record` YAML, the narrower Iceberg `graph_contracts` value
surface, and C7's process-generated production-influence closure population. The C7 population is
Git-snapshotted JSON plus a C1 observation envelope; it is not an Iceberg table and is not enforcing.

At delivery vintage the Iceberg/Kuzu substrate is healthy and marker-current, but live C2/C3.i
**instance-grain composition is absent**: the graph contains 19 static `C2Motif` rows and 4 static
`C3System` rows, while both instance-grain counts are zero. The static rows also lack the intended
`grain: class|instance` discriminator.

The C3.ii roster drift observed at the initial pin was corrected while this census was in progress:
the delivery pin has 29 canonical and 29 resolver names with no name-set difference. Final
reconciliation then closed the original definition-home defects: C3.i now declares
`overlapping-domain-cover`, C3.ii names the counted plane, and C0/C1 explicitly resolve by live
derivation. The canonical plane has 29/29 chain-bearing verticals; the resolver manifest has rows for
26/29. The three remaining names are therefore zero-manifest-row, not canonically chainless.

Two secondary served surfaces still lag those repaired homes. `comp-estate --layers` retains
`union-find` wording outside the C3.i authority block, and `comp-estate --matrix` renders the three
zero-manifest-row verticals as `DECLARED-BUT-CHAINLESS`. They are current display/provenance defects,
not evidence that the repaired definition or canonical membership reverted.

Pass 3 added the code-carrier plane: 59/59 fixed-population engines have AST/direct-read receipts;
10 concept-binding rows were generated, 9 unresolved `CODE_REDECLARATION` rows span 6 engines, one
binding resolved, and 52 engines have no binding row. C7 then consumed all 10 binding rows with
trigger and inventory inputs to produce 175 D3 closure rows: 172 `REACHED`, 2 `NOT_REACHED`, one
explicit source-denominator `UNKNOWN`, and zero production `FAILED`.

---

## 1. Scope and method

This report answers, for C0, C1, C2, C3.i, C3.ii, D1, D2, and D3:

- What does the layer/rail mean in prose?
- What is its machine-readable logical shape?
- Where is it physically stored?
- How is it snapshotted in the Iceberg/Nessie graph?
- What do agents actually see through `comp-kuzu` and `comp-estate`?
- Where do ratified shape, persisted shape, and served shape diverge?

Evidence was taken from the authoritative ontology files, writer and loader code, live read-only
Iceberg parity, the branch-head marker, Kuzu queries, `comp-estate` views, the C2/C3 liveness
instrument, the resolver JSON, generic D3 estate-contract files, the Iceberg `graph_contracts`
reader, the Pass 3 code-grain census, and the C7 process-generated closure package.

No ontology, shared graph, contract registry, resolver, or product source was modified by this
seat for the census or C7. The definition changes recorded in the final reconciliation were later
owner acts; C7 wrote only its component-local compiler, generated artifacts, and evidence package.

---

## 2. One cohesive model

### 2.1 The ladder and the dual C3 projection

```text
                                    SAME CHAIN GROUND SET
                         ┌─────────────────────────────────────┐
                         │ { thread_id, family, named_thread,  │
                         │   producers, served_artifacts, ... }│
                         └──────────────┬───────────┬──────────┘
                                        │           │
                                  family│           │named_thread
                                        ▼           ▼
                         C3.i DETERMINISTIC       C3.ii SEMANTIC
                              STRUCTURE                VERTICAL
                         discovered from wiring   declared by naming act
                         “what it structurally is” “what business calls it”
                                        \           /
                                         \  matrix /
                                          \       /
                                           ▼     ▼
                                      C2 motif instances
                                             │
                                  recurrence over C1 paths
                                             │
                                             ▼
                                      C1 interactions
                                             │
                                      edges over C0
                                             │
                                             ▼
                                         C0 facts
```

C3.i and C3.ii are not a parent and child. They are two projections over the same chain ground set.
Each chain’s `family` resolves into C3.i through the canonical `legacy_family_key` map; its
`named_thread` resolves into C3.ii. `comp-estate --matrix` is the reconciliation instrument.

### 2.2 The rails are not rungs

```text
 C3  system / vertical
  ▲
  │ D3  What obligation binds this path or system?
  │     cadence · completeness · canonical source · layer grammar · lifecycle
 C2  recurring motif shape
  ▲
  │ D2  What journey does the value take?
  │     ordered directed hops · per-hop transform · cadence borrowed from D3
 C1  directed interaction
  ▲
  │ D1  What travels, at what resolution?
  │     artifact -> partition -> row -> field
 C0  fact / object
```

The C ladder answers **what exists and how it composes**. The D rails answer **what information,
flow, timing, and obligation are carried between the rungs**.

---

## 3. C-layer census

### 3.1 C0 — facts

#### Meaning

C0 is the floor: every addressable thing represented as one graph row. Examples include Lambdas,
S3 buckets and keys, DynamoDB tables, schedules, pipeline scripts/functions, TypeScript fields,
React components, and Microsoft graph objects. Ownership is single; participation in paths and
systems may be many.

The ontology describes C0 as role-typed facts. Physically, `node_type` is stored while the abstract
ontology role is generally derived from C1 edge patterns; role is not a dedicated Iceberg column.

#### Machine-readable physical shape

```json
{
  "node_id": "string, required",
  "arn": "string|null",
  "node_type": "string, required",
  "name": "string|null",
  "layer": "aws|portal|ms|pipeline|semctl|null",
  "drift_class": "string|null",
  "source": "string|null",
  "snapshot_ts": 1787191224719,
  "props": "{\"type-specific\":\"JSON payload\"}"
}
```

`props` is a JSON string rather than a typed nested struct. All producer-specific attributes not
mapped to fixed columns land there through the writer’s no-silent-drop guard.

#### Physical home

- Iceberg: `globgrph.graph_nodes` — 9 columns.
- Kuzu: `CloudNode(node_id PK, arn, node_type, name, layer, drift_class, source, snapshot_ts, props)`.
- Agent query dialect: `(n:CloudNode)` followed by a predicate on `n.node_type`.

#### Live example

```json
{
  "node_type": "LAMBDA",
  "name": "opal-trending-topics-portal-publisher",
  "layer": "aws",
  "drift_class": "DECLARED",
  "source": "full-derive",
  "snapshot_ts": 1787191224719,
  "props": {
    "handler": "lambda_function.lambda_handler",
    "runtime": "python3.11",
    "owner_pipeline": "market-overview",
    "tf_managed": true
  }
}
```

#### Snapshot behavior

C0 rows are overwritten in the nightly full derive or touched by the scoped incremental updater.
The row carries producer observation time in `snapshot_ts`; the table has a distinct Iceberg
snapshot ID and `last_write_iso` in the branch-head marker.

---

### 3.2 C1 — interactions

#### Meaning

C1 connects C0 atoms. This is the point where an inventory becomes a graph. Every upper C rung is
an aggregation or view over C1 paths.

The graph stores concrete producer verbs such as `FLOWS_TO`, `WRITES`, `READS_FIELD`, `TRIGGERS`,
and `CONTAINS`. The ten abstract ontology relations (`produces`, `consumes`, `derives-from`,
`depends-on`, `contains`, `triggers`, `guards`, `governs`, `denies`, `owns`) are read-time adapter
bindings in the rule bank; they are not physical Kuzu relationship types.

#### Machine-readable physical shape

```json
{
  "src_id": "required C0 identity",
  "dst_id": "required C0 identity",
  "edge_type": "FLOWS_TO",
  "layer": "aws",
  "snapshot_ts": 1787191224719,
  "props": {
    "srcField": "BenchmarkModelData.name",
    "dstField": "name",
    "kind": "passthrough",
    "rename": false,
    "condition": null,
    "via": "mapping portal/src/components/ReturnVolatilityScatter.tsx:354",
    "resolution": "getSymbol on field-read prop access -> declaring type (TypeChecker)"
  }
}
```

#### Physical home

- Iceberg: `globgrph.graph_edges` — 6 columns.
- Kuzu: `CloudEdge(FROM CloudNode TO CloudNode, edge_type, layer, snapshot_ts, props)`.
- Agent query dialect: `(a:CloudNode)-[e:CloudEdge]->(b:CloudNode)` plus an `e.edge_type` predicate.

Kuzu does not create one relationship label per concrete verb. An agent querying
`MATCH (a)-[:WRITES]->(b)` is querying a schema that does not exist and may receive a misleading
empty result.

#### Snapshot behavior

C1 has its own Iceberg table snapshot, independent of `graph_nodes`. Node and edge snapshots may
therefore have different IDs and last-write times while still belonging to the current Nessie
branch state.

---

### 3.3 C2 — recurring motifs

#### Meaning

C2 is the first rung that generalizes. A C2 motif is a recurring multi-hop C1 path shape admitted
at recurrence `>= 2`. The shape itself has no time and no per-hop transform; those belong to D2.

The primary class population is the 12 canonical agnostic motif families. Defect/deviation motifs
are a subset, not the definition of the layer.

#### Canonical class shape

```yaml
c2_motif_families:
  scheduled-ingest:
    shape: "Trigger(cron) -> Producer -> Store(raw/bronze)"
    canon_binding: "..."
    meaning: "Cadence-driven acquisition into raw storage."
    first_pass_recurrence: 2
```

The delivery-vintage canonical class denominator is 12.

#### Current static graph shape

```json
{
  "node_id": "motif:a-access",
  "node_type": "C2Motif",
  "name": "AAccessMotif",
  "layer": "semctl",
  "source": "semctl-c2c3-materialize",
  "props": {
    "motif_type": "AAccessMotif",
    "plane": "A",
    "recurrence": 742,
    "n_instances": 224,
    "tier": "canonical"
  }
}
```

#### Intended instance-grain shape

```json
{
  "node_id": "motifi:<family>:<member-hash>",
  "node_type": "C2Motif",
  "props": {
    "grain": "instance",
    "family": "scheduled-ingest",
    "motif_type": "...",
    "plane": "A|B|...",
    "shape_matched": "...",
    "substrate_side": ["AWS"],
    "side_status": "RESOLVED|PARTIAL|UNRESOLVED",
    "members_unresolved": 0,
    "members_total": 3,
    "member_types": ["EVENT_RULE", "LAMBDA", "S3_BUCKET"],
    "member_pairs": [["node-id", "node-type"]],
    "members": ["node-id-1", "node-id-2", "node-id-3"]
  }
}
```

Each instance creates `CONTAINS` edges from the motif node to its C1/C0 constituents. The instance
ID is deterministic over the sorted member set.

#### Physical home

C2 has no dedicated Iceberg table. It uses:

- `graph_nodes`, selected by `node_type='C2Motif'`;
- `graph_edges`, using `CONTAINS` edges from motif to member;
- the `grain` property inside `props` to distinguish class and instance populations.

#### Current live census

```json
{
  "C2Motif": 19,
  "C2Motif[instance]": 0
}
```

All 19 rows are from `semctl-c2c3-materialize`. Sampled and current queryable rows omit `grain`.
Therefore the live graph contains a static/legacy C2 materialization, not an honestly discriminated
class-plus-instance population.

---

### 3.4 C3.i — deterministic structures

#### Meaning

C3.i discovers systems from shared C2 constituents. It answers: “What structural machine emerges
from the wiring?” Membership is computed, never manually declared.

The ruled model is **overlapping-domain-cover keyed by anchor node**. Connected-components or
union-find is a known-failed model because it over-merges shared infrastructure into one
supersystem.

#### Canonical naming shape

```yaml
c3_deterministic_structures:
  sys-bd-medallion:
    kind: FIRM-MEDALLION
    legacy_family_key: bd-medallion
    meaning: "The 49F/BD firm data refinery..."
    chain_count: 19
    spans_verticals: [advi-bd]
```

The delivery-vintage canonical denominator is 14 entries, including `UNASSIGNED-RESIDUE`.

#### Intended instance-grain shape

```json
{
  "node_id": "sysi:<domain>:<anchor-hash>",
  "node_type": "C3System",
  "props": {
    "grain": "instance",
    "domain": "object-data",
    "anchor_node": "node-id",
    "anchor_type": "S3_BUCKET",
    "model": "OVERLAPPING-DOMAIN-COVER",
    "member_motif_count": 4,
    "substrate_side": ["AWS"]
  }
}
```

Each structure creates `CONTAINS` edges from the C3 node to its C2 motif instances. A motif may join
multiple structures because the cover is overlap-allowed.

#### Current static graph shape

The live graph carries four `C3System` rows:

- `object-data`
- `compute-orchestration`
- `pipeline`
- `EmergentSystem`

Example:

```json
{
  "node_id": "system:object-data:ff0f4d26",
  "node_type": "C3System",
  "name": "object-data",
  "source": "semctl-c2c3-materialize",
  "props": {
    "anchor_types": ["S3Key", "S3_BUCKET"],
    "member_motifs": ["motif:a-store", "motif:a-access", "motif:a-serve", "motif:b-io"],
    "model": "overlapping-domain-cover",
    "recurrence": 4,
    "system_type": "object-data"
  }
}
```

These are anchor/category structures, not the 14 named `sys-*` catalog rows.

#### Current live census

```json
{
  "C3System": 4,
  "C3System[instance]": 0
}
```

The four static rows omit `grain`; no current instance-grain C3.i population is materialized.

#### Definition status after owner repair

At the original delivery pin, `SYSTEM_DEFINITIONS.yaml` and
`comp-estate --definitions C3.i` still said “deterministic union-find over shared constituents.”
The owner repair at `764c41fdbb`, carried through registry v3.15 at `00edd984c7`, now declares the
ruled and implemented overlapping-domain-cover model, anchor-node keyed, with 14 structures.

One non-home explanatory surface remains stale: `comp-estate --layers` serves
`C0_C1_C2_C3_C4_SYSTEM_LAYERS.md`, whose aggregation line and invariant prose still say
`union-find`. The definition authority is repaired; the secondary guide is not. Evidence:
`SYSTEM_DEFINITIONS.yaml:193-198 @00edd984c7` versus
`C0_C1_C2_C3_C4_SYSTEM_LAYERS.md:111,143 @00edd984c7`.

---

### 3.5 C3.ii — semantic verticals

#### Meaning

C3.ii is the declared business-semantic projection of the C3 grain. It answers: “What business
function do we say these chains comprise?” A vertical exists only by naming act; structural
emergence may propose but cannot admit one.

C3.i and C3.ii partition the same chain ground set through a dual key:

```json
{
  "thread_id": "bd-allocation-file-watchdog",
  "family": "bd-medallion",
  "named_thread": "advi-bd"
}
```

- `family -> legacy_family_key -> C3.i structure`
- `named_thread -> C3.ii vertical`

#### Canonical shape

```yaml
c3_ii_semantic_verticals:
  invariant: "DECLARED, never discovered"
  verticals:
    advi-bd:
      systems: [sys-bd-medallion]
      chain_count: 19
```

#### Resolver shape

```json
{
  "schema_version": 1,
  "generated_at": "2026-08-20T18:59:22.857342+00:00",
  "named_threads": ["advi-bd", "advi-inf", "..."],
  "resources_by_named_thread": {
    "security-scanner": ["resource-name", "..."]
  },
  "threads": [
    {
      "thread_id": "bd-allocation-file-watchdog",
      "named_thread": "advi-bd",
      "family": "bd-medallion",
      "owning_tool": "none",
      "status": "explicit-out",
      "reachability_status": "frontend-orphan",
      "description": "...",
      "producers": ["..."],
      "served_artifacts": ["..."],
      "frontend_resolution": "..."
    }
  ]
}
```

#### Physical home

C3.ii is not a current Iceberg node population. It lives in:

1. `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` for declared names and canonical system spans;
2. `estate-coverage-resolver.json` for named chain instances and agent traversal;
3. `comp-estate --matrix`, which compiles the dual-key join at invocation.

#### Delivery-vintage census

```text
canonical vertical names       29
resolver named_threads         29
name-set difference             0
resolver manifest thread rows 135
canonical chain-bearing        29
manifest-row-bearing           26
zero-manifest-row               3  (ceo-digest, etf-reports, ticketing)
matrix structures              14
```

The W-15 one-touch landed during the census and synchronized the name set: retired `attribution`
was removed, `observability` was admitted and populated, and `model-portfolios` was merged into
`mdpf`. The initial-pin 30-vs-30-but-different roster is therefore historical evidence, not the
delivery-vintage state.

The definition-home residue is closed. Registry v3.15 states that the three named verticals each
have canonical `chain_count: 1` but zero manifest thread rows. The matrix still prints
`DECLARED-BUT-CHAINLESS`, so its footer conflates canonical admission with resolver-row presence.
The correct current distinction is 29/29 canonical chain-bearing versus 26/29
manifest-thread-row-bearing. Evidence: `SYSTEM_DEFINITIONS.yaml:199-204 @00edd984c7` and
`opal_estate_infrastructure.py:653 @00edd984c7`.

---

## 4. Iceberg, Nessie, and Kuzu snapshot mechanics

### 4.1 Physical table schemas

```text
globgrph.graph_nodes      9 columns
  node_id REQUIRED string
  arn optional string
  node_type REQUIRED string
  name optional string
  layer optional string
  drift_class optional string
  source optional string
  snapshot_ts optional int64
  props optional JSON-as-string

globgrph.graph_edges      6 columns
  src_id REQUIRED string
  dst_id REQUIRED string
  edge_type REQUIRED string
  layer optional string
  snapshot_ts optional int64
  props optional JSON-as-string

globgrph.graph_contracts  13 columns; ensure-only
  contract_id REQUIRED string
  surface
  artifact_keys[]
  canonical_writer
  canonical_producer
  source_of_truth
  period_defs map<string,string>
  models[]
  forbidden_writers[]
  enforcement struct
  ratified_by[]
  ratified_at
  active boolean
```

### 4.2 Commit and marker flow

```text
AWS / portal / MS / pipeline extractors
                  │
                  ▼
          in-memory graph rows
                  │
       nightly full overwrite
       or scoped incremental write
                  │
          Nessie branch: main
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
Iceberg graph_nodes    Iceberg graph_edges
 independent snapshot  independent snapshot
       │                     │
       └──────────┬──────────┘
                  ▼
 warehouse/_branch_head.main.json
 {Nessie hash, metadata locations,
  snapshot IDs, per-table last-write}
                  │
                  ▼
        marker-pinned Iceberg read
                  │
                  ▼
       local Kuzu projection + manifest
       CloudNode / CloudEdge
                  │
                  ▼
              comp-kuzu
```

The full derive overwrites `graph_nodes` and `graph_edges` through PyIceberg against the Nessie
`main` branch. The incremental updater may make scoped table changes. Each table therefore has its
own Iceberg snapshot ID.

After a successful commit, `_provenance.stamp_marker` resolves the current table objects and writes:

```json
{
  "nessie_commit_hash": "...",
  "committed_at_iso": "...",
  "writer_id": "...",
  "table_metadata": {
    "graph_nodes": {
      "metadata_location": "s3://...metadata.json",
      "snapshot_id": 123,
      "last_write_iso": "..."
    }
  }
}
```

The marker, not newest-S3-object mtime, is the dev-box HEAD oracle. The Kuzu loader reads the
marker-pinned node and edge metadata files, scans those Iceberg snapshots, deduplicates nodes by
`arn` when present or raw `node_id` otherwise, loads `CloudNode` and `CloudEdge`, and writes a local
build manifest containing the source snapshot IDs. `comp-kuzu` prints that manifest and compares
its pin to marker HEAD before returning query results.

### 4.3 Current snapshot census

```json
{
  "nessie_commit_hash": "1a6da6e0870aa9d33e5dd394e50df910b30bb2309db8dff400429111ecd16daa",
  "writer_id": "incremental_updater",
  "graph_nodes_snapshot": 2492549419883349362,
  "graph_edges_snapshot": 5048107528270383466,
  "graph_contracts_snapshot": 7372628383041021108
}
```

Delivery revalidation returned:

```text
graph_nodes      MATCH  schema 9 columns; fresh
graph_edges      MATCH  schema 6 columns; fresh
graph_contracts  MATCH  schema 13 columns; ensure-only, vintage N/A
```

The current Kuzu projection is marker-current at **20,729 nodes / 41,407 edges**.

`graph_contracts` has an old last-write date by design. It is ensure-only and does not participate
in the nightly node/edge freshness cadence.

### 4.4 C2/C3 composition snapshot flow

```text
committed graph_nodes / graph_edges snapshot N
                         │
                         ▼
                in-container temporary Kuzu
                         │
                         ▼
                 c2_individuate.compose
                         │ in-memory envelope
                         ▼
                    c3_cover.compose
                         │
           envelope stamps source snapshot IDs
                         │
                         ▼
 fold C2/C3 nodes + CONTAINS edges into graph commit N+1
```

This creates an intentional one-derive lag: the C2/C3 instances in commit `N+1` were composed from
the committed graph at `N`. The source snapshot IDs must therefore ride inside each composed node’s
`props`; otherwise liveness cannot compare like-for-like vintages.

The composer is best-effort. If its module, reader, or query path fails, the derive logs the failure
and proceeds without the instance grain. The current zero-instance census is consistent with that
degraded-but-visible branch.

---

## 5. What agents see

### 5.1 `comp-kuzu`

`comp-kuzu --schema` teaches agents the actual physical dialect:

```text
nodes: (n:CloudNode), filter n.node_type
edges: [e:CloudEdge], filter e.edge_type
```

Every query prints:

- local DB path and node/edge count;
- source kind (`nessie`);
- node and edge snapshot IDs;
- node metadata key;
- local build timestamp and age;
- marker-HEAD comparison;
- per-table last-write status.

This is the agent’s direct view of persisted Iceberg state.

### 5.2 `comp-estate --layers`

This serves `C0_C1_C2_C3_C4_SYSTEM_LAYERS.md` verbatim. It is a stable map and derivation guide,
not a direct graph query. Residual wording inside it still says `union-find` even though the C3.i
authority and implementation say overlapping-domain-cover. Agents must treat `--definitions C3.i`
and its `resolves_via` authority as controlling until the guide is repaired.

### 5.3 `comp-estate --definitions <term>`

This reads `SYSTEM_DEFINITIONS.yaml` and applies its schema gate. At final reconciliation:

- C0 and C1 are `DERIVED-BY-NATURE`; their count is the live query, with header-vs-query parity at
  one vintage. The 2026-08-20 adjudication measured 20,729=20,729 nodes and 41,407=41,407 edges.
- C3.i resolves to the 14-entry canonical structure block and correctly names
  overlapping-domain-cover.
- C3.ii resolves to the nested 29-entry vertical block and distinguishes 29 canonical
  chain-bearing names from 26 manifest-thread-row-bearing names.
- D2 and D3 now carry explicit `resolves_via` pointers into their rule-bank homes.

### 5.4 `comp-estate --list`

This serves the resolver’s vertical/chain population. After the W-15 regeneration it sees 29 names
and 135 chains.

### 5.5 `comp-estate --matrix`

This is the most faithful current C3 reconciliation view. It:

1. reads `c3_deterministic_structures` live from canonical YAML;
2. creates `legacy_family_key -> sys-*` mapping;
3. reads every resolver chain;
4. joins `chain.family -> C3.i` and `chain.named_thread -> C3.ii`;
5. emits both system-to-vertical and vertical-to-system spans;
6. reports declared-but-chainless names.

Current output remains **14 structures × 26 manifest-row-bearing verticals over 135 resolver
thread rows**. Its footer calls the other three `DECLARED-BUT-CHAINLESS`; registry v3.15 proves that
label is plane-ambiguous because all three have canonical `chain_count: 1`. Read the matrix as a
resolver-manifest traversal, not a complete canonical chain census.

### 5.6 `comp-estate --structure <sys-name>`

This is the C3.i descent view. It renders:

```text
C3.i named structure
  -> C3.ii vertical grouping
     -> D2 chain ID
        -> C2 motif family
```

For `sys-bd-medallion`, the current resolver view returns 19 chains under `advi-bd`, with each
chain’s C2 motif or honest `UNCLASSIFIED` residue.

### 5.7 `comp-estate <vertical>`

This is the C3.ii descent view. It renders each chain as:

```text
status / owner
C3.i structure | C2 motif
description
producers
  -> served artifacts
  -> frontend resolution
  -> reachability verdict
```

Those prose-rich chain blocks are the agent-visible D2 representation. They are not raw ordered
Iceberg edge lists.

### 5.8 C2/C3 liveness instrument

`c2c3_liveness_acceptance.py --snapshot` is the positive-controlled physical census:

```json
{
  "C2Motif": 19,
  "C3System": 4,
  "C2Motif[instance]": 0,
  "C3System[instance]": 0
}
```

This is the decisive current answer about materialized instance grain.

### 5.9 Pass 3 and C7 agent artifacts

The code-carrier census and D3 closure are not implicit `comp-kuzu` views. Agents see them as
explicit, Git-pinned machine artifacts:

```text
Pass 3 scan script
  -> 59-engine receipts + 10 concept-binding rows
  -> C7 CODE_BINDING adapter

trigger-map + census descriptors
  -> C7 TRIGGER_TARGET / INVENTORY_DESCRIPTOR adapters

all normalized seeds
  -> generic closure traversal
  -> 175-row D3 population
  -> C1 Observation_Record envelope
```

The Pass 3 YAML is the adjudicated census; its JSON is the direct AST scan receipt. The C7 JSON is
accepted only when every row's `row_id`, `generation_run_id`, and `generated_by` recompute from the
pinned inputs. A planted hand-authored row is rejected. Agents therefore see a generated population
with provenance, not an unexplained spreadsheet or a silently empty graph query.

---

## 6. D-rail census

### 6.1 D1 — value / grain

#### Meaning

D1 answers: “The graph says A interacts with B — what value actually travels, and how finely is it
resolved?” Its ordered grain is:

```yaml
grain_axis:
  ordered: [artifact, partition, row, field]
```

- `artifact`: whole bucket, table, topic, queue, or log group.
- `partition`: dated/keyed slice, represented today by `S3Key` instances.
- `row`: declared but not materialized as graph nodes.
- `field`: `Field` and `Prop` nodes and field-flow edges.

#### Machine shape

D1 has no table and no row of its own. It rides inside a C1 edge:

```json
{
  "edge_type": "FLOWS_TO",
  "props": {
    "srcField": "MarketTickerData.entity_type",
    "dstField": "entity_type",
    "kind": "recompute/guarded",
    "rename": false,
    "condition": null,
    "via": "mapping portal/src/api/endpoints/market.ts:249",
    "resolution": "getSymbol on field-read prop access -> declaring type (TypeChecker)"
  }
}
```

The grain is usually inferred from the carrier:

```text
READS_FIELD / FLOWS_TO / PROP_PASSES -> field
S3Key                                -> partition atom
WRITES / READS / WRITES_S3           -> artifact
row                                   -> forward / unmaterialized
```

The ratified `EdgeKind` values are `passthrough`, `rename`, and `recompute_guarded`; the current
producer may serialize the last as `recompute/guarded`.

#### Physical home and snapshot

D1 is snapshotted inside `graph_edges.props` with the carrying C1 row. A loader that omits `props`
can preserve the edge while silently destroying all D1 meaning.

---

### 6.2 D2 — path / flow

#### Meaning

D2 is an instantiated C2 motif with direction, per-hop transformation, and contracted time:

```text
motif = recurring shape
D2 path = shape + ordered direction + D1 transform per hop + D3-sourced cadence
```

#### Logical machine shape

```json
{
  "hops": [
    {
      "relation": "produces|consumes|derives-from",
      "grain": "artifact|partition|row|field",
      "transform_at_hop": "passthrough|rename|recompute_guarded"
    }
  ],
  "direction": "native directed edge order",
  "cadence": "D3 contract or forward/undeclared"
}
```

Cadence is not a native `FLOWS_TO` property. The graph supplies a control skeleton through schedules
and `RUNS` / `TRIGGERS` / `INVOKES`, but the promised time is a D3 obligation.

#### Current implemented representation

D2 has no Iceberg table and no first-class Kuzu node/edge type. It is represented through:

1. ordered traversal over C1 `CloudEdge` rows;
2. the resolver’s denormalized chain records;
3. `comp-estate` chain blocks, where `producers -> served -> frontend` are the human-readable hops.

Example chain record:

```json
{
  "thread_id": "bd-allocation-file-watchdog",
  "named_thread": "advi-bd",
  "family": "bd-medallion",
  "owning_tool": "none",
  "status": "explicit-out",
  "reachability_status": "frontend-orphan",
  "description": "Daily ops watchdog...",
  "producers": ["bd-allocation-file-checker (...)"],
  "served_artifacts": ["SNS arn:..."],
  "frontend_resolution": "none (ops alerting)"
}
```

#### Snapshot behavior

The underlying topology is Iceberg-snapshotted in `graph_edges`. The named semantic chain view is a
separate checked-in resolver snapshot with `generated_at` and `last_review`. Runtime upstream
vintage is neither of those: it must be probed from the actual artifact.

Therefore:

```text
freshness = D2 path + D3 cadence + live upstream vintage + trading calendar
```

Freshness is never merely wall-clock age of a graph row or static artifact mtime.

---

### 6.3 D3 — contract / obligation

#### Meaning

D3 is the governed intent that binds a motif, path, or system. Its obligation types are:

- `delivery_cadence`
- `completeness`
- `canonical_source`
- `layer_grammar`
- lifecycle obligations and derivations

Intent must come from a governance level above the artifact. A subject naming itself as its own
intent source is the denominator-is-its-own-configuration defect and is rejected.

#### Generic ontology `contract_record`

```yaml
"<subject-identity>":
  intent_source: "governed source above the artifact"
  obligation: [delivery_cadence, completeness]
  lifecycle_class: PERMANENT
  revalidate_by: "..."
  locality: global

  # optional
  successor: null
  expiry_condition: null
  cadence: "..."
  vintage_probe: "..."
  describes: "free-text subject description"
```

Required fields:

```yaml
[intent_source, obligation, lifecycle_class, revalidate_by, locality]
```

Optional fields:

```yaml
[successor, expiry_condition, cadence, vintage_probe, describes]
```

Lifecycle enum:

```yaml
[PERMANENT, TRANSIENT, EVENT_CREATED, DORMANT, LEGACY, RETIRED, UNDECLARED]
```

`lifecycle_class` is producer-asserted, never inferred from absence or naming patterns.
`UNDECLARED` is the only value an observer may write because it declines to assert a life shape and
authorizes nothing.

#### Generic instance storage

Generic instances live in:

- `org/modules/graph/estate-contracts/mdpf.contracts.yaml` — 7 subject declarations;
- `org/modules/graph/estate-contracts/model-portfolios.contracts.yaml` — 7 subject declarations.

The files are keyed by subject identity and are not loaded into `graph_nodes` or `graph_edges`.

#### Separate Iceberg `graph_contracts` surface

The Iceberg table named `graph_contracts` is a different, narrower value/surface contract schema:

```json
{
  "contract_id": "benchmark-model-portfolios",
  "surface": "critical-surfaces:model_portfolios.benchmark ...",
  "artifact_keys": ["s3://..."],
  "canonical_writer": "yang-pipeline-lambda-role",
  "canonical_producer": "...",
  "source_of_truth": "...",
  "period_defs": {"1M": "trailing-1-calendar-month -> as-of"},
  "models": ["UST", "ST", "INT", "LTC", "LTA"],
  "forbidden_writers": ["..."],
  "enforcement": {
    "iam_backstop": "...",
    "surface_gate": "...",
    "value_check": "..."
  },
  "ratified_by": ["Andrew"],
  "ratified_at": "<commit/hash>",
  "active": true
}
```

It currently has three active rows:

- `peers-model-portfolios`
- `aum-model-portfolios`
- `benchmark-model-portfolios`

It is marker-stamped and Iceberg-snapshotted, but:

- it is ensure-only and never overwritten by the nightly graph derive;
- it is not loaded into Kuzu;
- it is read directly from Iceberg by `contract_engine.py` and contract-surface tools;
- it is not schema-equivalent to the generic D3 `contract_record` registry.

Calling both “D3 contracts” without naming the schema and carrier is an ontological grain error.

#### Process-generated C7 production-influence population

C7 adds a third D3 carrier at a different grain: one generated closure row per declared
production-influence seed. It does not replace either contract schema above.

```json
{
  "schema": "nfra_epistemy.c7.d3_population/0.1.0-proposed",
  "generation": {
    "generated_by": "nfra_epistemy.c7.influence_closure",
    "compiler_source_sha256": "sha256:...",
    "generation_run_id": "sha256:...",
    "input_manifest": {
      "input_commit": "b30b05d00675f0b3758d1ed8ccbedf0004b901f5",
      "blobs": {"path": "git-blob"},
      "adapter_denominators": {"pass3_rows": 10, "trigger_target_edges": 162}
    }
  },
  "rows": [
    {
      "row_id": "sha256:...",
      "seed_id": "sha256:...",
      "edge_kind": "CODE_BINDING|TRIGGER_TARGET|INVENTORY_DESCRIPTOR",
      "source_node": "...",
      "target_node": "...",
      "closure_state": "REACHED|NOT_REACHED|UNKNOWN|FAILED",
      "path_witness": ["sha256:..."],
      "source_ref": "path#line @ commit",
      "generation": {
        "generated_by": "nfra_epistemy.c7.influence_closure",
        "generation_run_id": "sha256:..."
      }
    }
  ]
}
```

The fixed input denominator is:

```text
10  Pass 3 CODE_BINDING seeds
162 materialized trigger-target seeds
  2 inventory-descriptor frontier seeds
  1 explicit trigger-map denominator residue
---
175 generated D3 rows
```

Production states are 172 `REACHED`, 2 `NOT_REACHED`, 1 `UNKNOWN`, and 0 `FAILED`. The one
`UNKNOWN` preserves the source map's declared-154 versus keyed-153 trigger difference. The two
inventory descriptors are `NOT_REACHED` because the pinned inputs declare descriptor frontiers but
contain no pinned live inventory result. `FAILED` was exercised by a scratch malformed-edge mutant,
not manufactured in the production population.

Physical storage and snapshot semantics:

- population: `NFRA_EPISTEMY.C7-CLOSURE/generated/d3_population.json`;
- observation: `generated/d3_population.observation.json`, validated by the landed C1 implementation;
- execution evidence: `evidence/acceptance_results.json`;
- Git snapshot: `f9e4ff4459`, over exact input Git objects at `b30b05d006`;
- Iceberg status: not loaded, not marker-stamped, not Kuzu-served, and not enforcing.

The snapshot identity is therefore the Git commit plus input blob manifest, compiler-source hash,
generation-run ID, and population digest. Two independent same-input compilations must be
byte-identical before the guarded writer emits the artifacts. Evidence:
`00_COMPONENT_SPEC.md:13-38 @f9e4ff4459` and `S0_GROUND_READ.md:24-41 @ed742cd929`.

---

## 7. Representation and divergence register

### R1 — C2/C3.i instance grain absent from the current graph

**Status:** CURRENT, measured.
**Evidence:** 19 total `C2Motif`, 4 total `C3System`, zero instance-grain for both.
**Meaning:** the graph exposes static C2/C3 rows but not the intended live composed population.
**Failure direction:** an agent may mistake a clean zero for “no instances exist” when the instance
producer did not land.
**Control:** always run `c2c3_liveness_acceptance.py`; never use a bare instance count.

### R2 — `grain` discriminator absent on live static C2/C3 rows

**Status:** CURRENT, measured.
**Meaning:** the intended `class|instance` discriminator does not describe the current static rows.
The total population cannot honestly be partitioned by grain from persisted data.

### R3 — C3.i union-find wording

**Status:** DEFINITION HOME REPAIRED; SECONDARY GUIDE RESIDUE CURRENT.
**Owner repair:** `SYSTEM_DEFINITIONS.yaml` and the rule bank's `c3_dual_partition.c3_i` now say
overlapping-domain-cover, anchor-node keyed (`764c41fdbb`; current registry v3.15 `00edd984c7`).
**Remaining conflicting surface:** `comp-estate --layers` still serves union-find wording from
`C0_C1_C2_C3_C4_SYSTEM_LAYERS.md:111,143`.
**Consequence:** an agent using the guide but not the definition authority can still select the
known-failed over-merging algorithm.

### R4 — C3.ii chain-plane wording

**Status:** DEFINITION HOME REPAIRED; MATRIX RENDER RESIDUE CURRENT.
**Canonical plane:** 29/29 declared verticals are chain-bearing.
**Resolver-manifest plane:** 26/29 have thread rows; `ceo-digest`, `etf-reports`, and `ticketing`
have zero manifest thread rows.
**Remaining conflicting surface:** `comp-estate --matrix` still renders those three as
`DECLARED-BUT-CHAINLESS`, omitting the plane discriminator.

### R5 — initial C3.ii roster drift closed during the census

**Initial pin `8d5532311d`:** canonical and resolver both counted 30 but differed one-for-one:
resolver-only `attribution`, canon-only `observability`; `model-portfolios` still stood separately.
**Delivery pin `9b4151ac45`:** canonical and resolver both count 29 with equal name sets;
`attribution` retired, `observability` present, `model-portfolios` merged into `mdpf`.
**Disposition:** CLOSED at delivery; retained here because it proves a matching count is not a roster
parity check.

### R6 — generic D3 contracts and Iceberg `graph_contracts` are distinct schemas

**Status:** CURRENT structural distinction.
**Risk:** a consumer may treat the Iceberg table as the materialized form of generic
`contract_record`, silently losing lifecycle, intent-source, locality, cadence, and revalidation
semantics.
**Rule:** always name both schema and carrier.

### R7 — ontology representation is distributed by design

**Status:** CURRENT architecture, not itself a defect.
**Risk:** tools can present one plane as the whole ontology unless they print provenance.
**Required reading:** distinguish canon, physical graph snapshot, resolver snapshot, and runtime
artifact observation on every answer.

### R8 — code-grain ontology copies remain in six comp engines

**Status:** CURRENT at Pass 3 assessment vintage `f36d572be864e56b9175caac06b01f62fc141e2a`.
**Denominator:** 59/59 engines read; 10 binding rows; 9 unresolved `CODE_REDECLARATION` rows across
6 engines; 1 resolved; 52 engines with no binding row.
**Meaning:** these code locations carry ontology vocabulary without a resolved authority binding
and are future two-home risks. They are census findings, not owner-code edits.
**Control:** retain the Pass 3 AST/direct receipts and route each row to its candidate owner;
`resolves_via` authoring remains a separate fenced act.

### R9 — C7 D3 is generated but not graph-materialized

**Status:** PROCESS-GENERATED, VALIDATED, NOT ENFORCING.
**Denominator:** 175/175 rows validate process origin; two same-input runs are byte-identical.
**Meaning:** C7 closes the population-generation gap for the declared input bundle, but the output
is a Git artifact and C1 observation, not an Iceberg/Kuzu population.
**Control:** never claim that `comp-kuzu` serves this D3 population; cite `f9e4ff4459` and its input
manifest until a separately gated registry/materialization act occurs.

---

## 8. Current-vintage census table

| Object | Canon / logical population | Physical carrier | Final-reconciled measured state | Agent surface |
|---|---|---|---|---|
| C0 facts | role-typed objects | Iceberg `graph_nodes`; Kuzu `CloudNode` | Kuzu total 20,729 nodes, including upper-rung reifications | `comp-kuzu` |
| C1 interactions | 10 abstract relations over concrete verbs | Iceberg `graph_edges`; Kuzu `CloudEdge` | Kuzu total 41,407 edges | `comp-kuzu` |
| C2 class | 12 canonical motif families | canonical YAML; static `C2Motif` rows | 19 static rows, no `grain` | canon + `comp-kuzu` |
| C2 instance | recurring path matches | intended `C2Motif props.grain=instance` + `CONTAINS` | 0 current | liveness instrument |
| C3.i class | 14 named structures | canonical YAML / resolver mapping | 14 in matrix | `comp-estate --matrix` |
| C3.i physical static | anchor/category systems | `C3System` in `graph_nodes` | 4 static rows, no `grain` | `comp-kuzu` |
| C3.i instance | anchor-node overlapping cover | intended `C3System props.grain=instance` | 0 current | liveness instrument |
| C3.ii declared | 29 semantic verticals | canonical YAML | 29 | canon / definitions |
| C3.ii canonical chain-bearing | declared verticals with canonical `chain_count` | canonical YAML | 29/29 | canon / definitions |
| C3.ii manifest-row-bearing | resolver rows grouped by `named_thread` | resolver JSON | 26/29 over 135 rows; 3 zero-row names | `comp-estate --matrix` |
| D1 | value/grain | `graph_edges.props` + carrier-derived grain | no dedicated table | `comp-kuzu`, `comp-estate` descent |
| D2 | directed timed path | C1 traversal + resolver chain | 135 denormalized chain records | `comp-estate <vertical>` |
| D3 generic | obligation + lifecycle | `estate-contracts/*.contracts.yaml` | 14 declarations across 2 files | YAML readers / contract lint |
| `graph_contracts` | narrower value-surface contract | ensure-only Iceberg table | 3 active rows; schema MATCH | contract engine / surface tools |
| D3 influence closure | one generated row per declared C7 influence seed | Git JSON + C1 envelope | 175 rows: 172 reached, 2 not reached, 1 unknown, 0 failed | C7 compiler / acceptance package |
| Code-carrier bindings | concept-bearing code occurrences in fixed Pass 3 engines | Pass 3 YAML + AST receipt JSON | 59/59 read; 10 rows; 9 unresolved across 6 engines | Pass 3 scan and census |

---

## 9. Conclusions and recommended controls

### 9.1 What is sound now

- Iceberg `graph_nodes`, `graph_edges`, and `graph_contracts` match their canonical schemas.
- The branch-head marker and Kuzu projection agree on current node/edge snapshot pins.
- C0/C1 machine shapes are explicit, agent-queryable, and now declared `DERIVED-BY-NATURE` with
  header-vs-query parity at one vintage.
- The C3.ii canonical and resolver name sets are aligned after W-15.
- The C3.i definition home now matches the ruled overlapping-domain-cover implementation.
- C3.ii's definition home now distinguishes canonical chain-bearing from manifest-row-bearing.
- `comp-estate --matrix` exposes the structure/vertical dual key, subject to its footer wording
  residue.
- D1, D2, and all three D3 carriers have explicit logical and physical identities.
- Pass 3 gives every engine in its 59-engine population a direct receipt.
- C7's 175-row D3 population is process-generated, provenance-bound, C1-wrapped, and deterministic.

### 9.2 What remains materially unresolved

1. **C2/C3.i instance composition is not live in the current graph.** The desired instance schema
   exists in code, but the current snapshot contains zero instances and unstamped static rows.
2. **Two secondary C3 displays lag the repaired homes.** `--layers` still says union-find and the
   matrix footer still calls three zero-manifest-row verticals chainless.
3. **D3's three carriers need explicit names at every consumer boundary.** Generic ontology
   contracts, Iceberg value-surface contracts, and C7 influence-closure rows are different grains.
4. **Nine code redeclarations remain unresolved across six comp engines.** Pass 3 measured and
   routed them; this seat did not edit owner code.
5. **C7 is not yet an Iceberg/Kuzu or enforcement surface.** It is a validated Git population
   awaiting any separately authorized registry/materialization decision.

### 9.3 Recommended controls

The original definition-home recommendations were implemented by owner acts at v3.12-v3.15. The
remaining controls below are recommendations only; this seat did not modify shared serving code.

1. Make C2/C3 liveness acceptance a required post-derive gate or explicitly classify the instance
   layer as disabled. A best-effort skip must never be interpreted as an empty estate.
2. Bring `comp-estate --layers` and the matrix footer into parity with the repaired authority homes;
   the latter should say `ZERO-MANIFEST-THREAD-ROWS`, not `DECLARED-BUT-CHAINLESS`.
3. Retain a roster-equality gate, not only a count gate, between canonical C3.ii names and resolver
   `named_threads`. R5 demonstrates that equal counts can conceal one-for-one name drift.
4. Require agent outputs to print the carrier and vintage: canon commit, resolver `generated_at`,
   Iceberg snapshot IDs, or live artifact observation time as applicable.
5. Give all three D3 carriers unambiguous serving names: “ontology contract_record,” “Iceberg
   value-surface contract,” and “C7 influence-closure population.”
6. Preserve `props` as a required fidelity carrier throughout every production Kuzu load path; a
   props-less projection retains topology while erasing D1 and C2/C3 discriminators.
7. Route the nine Pass 3 code-redeclaration rows to their candidate owners without combining that
   work with the separately fenced `resolves_via` drive.
8. Keep C7 non-enforcing until Base executes the registry decision and CTO gates any architecture or
   materialization change.

---

## 10. Evidence index

### Ontology authority

- `infra/system/ontology/C0_C1_C2_C3_C4_SYSTEM_LAYERS.md`
- `infra/system/ontology/SYSTEM_DEFINITIONS.yaml`
- `infra/system/ontology/LAYER_FIELD_ANATOMY.md`
- `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`
- `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml`

Final definition reconciliation uses `SYSTEM_DEFINITIONS` v3.15 at `00edd984c7`. The load-bearing
repairs landed at `764c41fdbb` (C3.i/C3.ii/D2/D3), `7dfde8710c` (C3.ii plane correction), and
`d7fb8e5c54` (C0/C1 derived-by-nature declarations).

### Resolver and agent surfaces

- `org/modules/graph/estate-coverage-resolver.json`
- `org/modules/graph/estate-coverage-manifest.yaml`
- `org/modules/graph/opal_estate_infrastructure.py`
- `org/modules/graph/estate_infrastructure_cli.py`

### Iceberg/Nessie/Kuzu mechanics

- `infra/aws/globgrph/derive_runner.py`
- `infra/aws/globgrph/_provenance.py`
- `infra/aws/globgrph/kuzu_nessie_load.py`
- `infra/aws/globgrph/kuzu_incremental_refresh.py`
- `infra/aws/globgrph/iceberg_parity.py`
- `infra/aws/globgrph/trino_catalog_parity.py`
- `infra/aws/globgrph/c2c3_liveness_acceptance.py`

### C2/C3 composition

- `org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/c2_individuate.py`
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/c3_cover.py`
- `infra/aws/globgrph/motif_c2c3_materialize.json`
- `infra/aws/globgrph/motif_c2c3_materialize_ab.json`

### D3 carriers

- `org/modules/graph/estate-contracts/README.md`
- `org/modules/graph/estate-contracts/mdpf.contracts.yaml`
- `org/modules/graph/estate-contracts/model-portfolios.contracts.yaml`
- `org/modules/graph/contract_engine.py`
- `infra/aws/globgrph/derive_runner.py::_graph_contracts_schema`
- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE/generated/d3_population.json @f9e4ff4459`
- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE/generated/d3_population.observation.json @f9e4ff4459`
- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE_PROOF_OF_SPEC.json @f9e4ff4459`

### Code-grain census

- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_POPULATION_20260820.yaml @76ba5fec3d`
- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_GRAIN_20260820.yaml @b30b05d006`
- `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ATOM_LAYER0_PASS3_CODE_GRAIN_SCAN_RESULTS_20260820.json @b30b05d006`

### Read-only commands exercised

```text
python org/modules/graph/opal_estate_infrastructure.py --layers
python org/modules/graph/opal_estate_infrastructure.py --definitions C0
python org/modules/graph/opal_estate_infrastructure.py --definitions C1
python org/modules/graph/opal_estate_infrastructure.py --definitions C3.i
python org/modules/graph/opal_estate_infrastructure.py --definitions C3.ii
python org/modules/graph/opal_estate_infrastructure.py --list
python org/modules/graph/opal_estate_infrastructure.py --matrix
python org/modules/graph/opal_estate_infrastructure.py --structure sys-bd-medallion
python org/modules/graph/opal_estate_infrastructure.py advi-bd --head 35
python infra/aws/globgrph/kuzu_cli.py --schema
python infra/aws/globgrph/kuzu_cli.py --json <C0/C1/C2/C3 queries>
python infra/aws/globgrph/c2c3_liveness_acceptance.py --snapshot
python infra/aws/globgrph/iceberg_parity.py
python -c "... contract_engine.load_contracts(active_only=False) ..."
python org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE/scripts/run_acceptance.py
python .tools/proof-of-spec-check.py org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE_PROOF_OF_SPEC.json C7-1,C7-2,C7-3,C7-4,C7-5,C7-6
```

---

## 11. Terminal statement

The graph ontology is not merely a taxonomy document. It is a runtime composition across canon,
Iceberg/Nessie snapshots, Kuzu projections, resolver snapshots, and live artifact probes. A correct
answer must identify which plane supplied it and must carry that plane’s vintage.

The system's intended conceptual model is coherent. The observed physical state is healthy at C0/C1
and at the Iceberg schema/marker seam, aligned at the C3.ii name-set seam after W-15, and incomplete
at C2/C3.i instance grain. The authoritative C3 definition defects found in the original census were
repaired; two secondary render surfaces still lag. Pass 3 makes code-carrier drift measurable, and
C7 makes the declared production-influence D3 population reproducibly generable without pretending
that it is already an Iceberg, Kuzu, registry, or enforcement surface.

An agent can now answer every requested question by naming both object and plane: the prose meaning,
machine shape, physical carrier, snapshot identity, and serving path. Where those planes disagree,
this report preserves the disagreement instead of smoothing it away.

**Report complete — `4.0.0_SA_CRO~B`, 2026-08-20.**
