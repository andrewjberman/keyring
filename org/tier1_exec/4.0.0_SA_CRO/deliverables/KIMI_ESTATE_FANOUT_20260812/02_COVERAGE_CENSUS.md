# FANOUT 02 — Coverage standing, C2/C3 over the estate (verbatim agent report, received 2026-08-12 ~20:20Z)

**Agent scope:** where deterministic coverage stands NOW; what 100% deterministic+inferential
requires; cascade-budget arithmetic per substrate. **Evidence class: agent-derived; GROUND-CHECKED at
the CRO seat same hour — the zero-vocabulary-overlap claim verified with positive controls (7 and 11
hits in-home, 0 cross-hits both directions), and the ceiling arithmetic reproduced exactly
(8,179/20,616 = 39.7%; 4,184/20,616 = 20.3%).**

**Graph vintage for every MEASURED-NOW figure:** `kuzu_nessie_db`, **20,639 nodes / 41,253 edges**,
nodes snapshot-id `8659974776412827892`, built `2026-08-12T18:25:51Z`, Nessie HEAD current.

---

## 0. The finding that reframes the rest: there are THREE disjoint C2/C3 populations

| Population | Grain | Count | Where it lives | In the live graph? |
|---|---|---|---|---|
| **A.** 12 canonical motif families | chains | 12 families / 135 chains | `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:35-95` | **NO** — prose catalog only |
| **B.** 19 C2Motif + 4 C3System class nodes | node-membership | 19 / 4 | live graph, `layer='semctl'` | **YES** |
| **C.** 6,138 motif instances + 1,255 C3 structures | instances | 6,138 / 1,255 | `…/kimi_subdivision_harness/c2_instances.json`, `c3_structures.json` (2026-08-07) | **NO** — persisted JSON, never landed |

**A and B share ZERO vocabulary.** Population A's families: `scheduled-ingest, staged-transform,
orchestrated-compute, fanin-quorum, publish-serve, scheduled-publish, generative-publish, api-serve,
edge-route, access-guard, enrichment-writeback, watchdog-observe` (`:36-95`). Population B's:
`a-store, a-access, a-table, a-grant, a-event, a-api, a-serve, a-watch, a-orch, b-struct, b-run,
b-io, b-dataflow` + 6 defect detectors (MEASURED-NOW, 23-row comp-kuzu listing). **Not one name
overlaps.** Every coverage percentage the estate quotes measures **B**; the canonical catalog
everyone reads describes **A**.

The cascade doc names this itself: *"the 4-vs-14-vs-1255 confusion all came from legislation standing
in for construction"* — `SUBSTRATE_MODEL_AND_DETERMINISTIC_CASCADE_20260811.md:75`.

## 1. Where 79.3% / 13.2% come from — live-reproducible today

**Origin (PERSISTED-FROM-2026-08-06):** `SYSTEM_DEFINITIONS.yaml` `Substrate_Side` entry. **No
comp-tool computes it** — it is a direct graph measurement, re-run by this agent.

**MEASURED-NOW** — distinct C0 nodes that are the target of a `CONTAINS` edge from any
`C2Motif`/`C3System` node. **Grain = C0 NODES.**

| Substrate | covered | nodes | % | 08-06 persisted | drift in 6 days |
|---|---|---|---|---|---|
| portal | **1,495** | **11,338** | **13.2%** | 1495/11338 = 13.2% | **0 / 0** |
| aws | 1,398 | 2,055 | 68.0% | — | — |
| pipeline | 1,291 | 1,337 | 96.6% | — | — |
| **BACKEND** (aws+pipeline) | **2,689** | **3,392** | **79.3%** | 2693/3396 = 79.3% | −4 / −4 |
| ms | **0** | **5,886** | **0.0%** | not reported | — |
| **ESTATE** | **4,184** | **20,616** | **20.3%** | not reported | — |

*(Estate denominator excludes the 23 semctl C2Motif/C3System nodes — the covering objects.)*
**Coverage has not moved in six days.** The headline figures reproduce to the decimal.

**Second instrument (PERSISTED-FROM-2026-08-07, instance grain, 13 AB detectors only):**
`kimi_subdivision_harness/c2_instances.json` → `counts.coverage_triple_by_side`:

| Side | covered_X | in_detector_scope_Y | on_side_Z | pct_of_scope | pct_of_side |
|---|---|---|---|---|---|
| BACKEND | 2,755 | 2,936 | 3,393 | **93.8%** | 81.2% |
| FRONTEND | 1,479 | 5,245 | 11,338 | **28.2%** | 13.0% |
| KNOWLEDGE | 0 | **0** | 5,851 | `null` | 0.0% |

**The middle term (in-detector-scope) is the load-bearing one and it is absent from every circulated
figure.** BACKEND is at 93.8% *of what a detector even looks at*; FRONTEND at 28.2%. The 79.3-vs-13.2
spread conflates "detector ran and missed" with "no detector exists for this node type."

## 2. UNASSIGNED-RESIDUE — 8 chains of 138 (5.8%). Grain = CHAINS, not nodes.

Declared at `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:169-177` (`chain_count: 8`). MEASURED-NOW against
`org/modules/graph/estate-coverage-resolver.json` (138 threads, `last_review: 2026-07-30`) — exact,
both encodings present: `sentiment_query_api`(family null), `test-yfinance-simple`(null, explicit-out),
`yfinance-aapl-test`(null, explicit-out), `ycharts-session`(null), `canonical-schwab`(null, in-scope),
`etfs-reports-pipeline`("UNASSIGNED"), `ceo-daily-wsjft-digest`("UNASSIGNED"), `ticket-center-api`
("UNASSIGNED").

Full C3.i family distribution over 138 chains (MEASURED-NOW): bd-medallion 19, yang-datapipeline 14,
partners-portal-infra 13, inf-medallion 12, pm-tool 12, news-seeking-alpha 12,
graph-and-ops-and-casefind 11, market-analytics 9, causality-ai 8, fred-and-generated-outputs 8,
trade-submission 7, **null 5**, smartx 3, **UNASSIGNED 3**, cot-and-mdpf 2.

**Two OTHER residues exist, routinely conflated with this one:**
- **C2 chain residue, 18 of 135 (13.3%)** — `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml:338-359`, enumerated
  by name; predates the resolver's move to 138 (its own denominator note `:335-337`).
- **Instance residue, 1,103 of 6,138 (18.0%)** — `c3_structures.json` →
  `counts.instances_with_no_catalog_anchor: 1103`, plus `domains_unpromoted_single_motif: 617`.

Three residues, three grains (chains / chains / instances), three denominators. None is a subset of
another.

## 3. The FRONTEND gap — only 2 of 13 detectors touch portal at all

MEASURED-NOW from `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_MOTIF_P1_canonical_ab_catalog.py`
(the `AB_CATALOG` the Kimi harness reads verbatim at runtime):
- `a-serve` subquery 2 (`:115`): constituents `DataFetch, Endpoint, ServedURL`
- `b-dataflow` (`:151-153`): constituents `Field, Field`

That is the entire portal surface of the detector catalog. **4 node types → 5,245 nodes**, exactly
the persisted `in_detector_scope_Y` for FRONTEND. The other **11 of 15 portal node types (6,093
nodes, 53.7% of portal) have no detector referencing them:** JSXElement 2205 · JSXRender 1433 ·
TypeDecl 807 · ReactComponent 442 · Module 374 · Prop 359 · Component 199 · Hook 111 · PanelCluster
91 · ReactQueryKey 57 · Page 15.

**Below motif grain by design? Overwhelmingly NO — one exception.** `NFRA_ONTOLOGY_RULE_BANK.yaml:218-231`
role-maps every uncovered portal type except one: `Sink: [JSXRender, JSXElement]` (3,638 nodes) ·
`Container: [Module, …, PanelCluster, Page]` (480) · `Consumer: [DataFetch, Hook, ReactQueryKey]`
(168) · `Store: [… Prop …]` (359) · `contextual: [… Component, ReactComponent …]` (641). **The single
design-declared exclusion:** `scope_out: [TypeDecl, Type, Symbol, Concept]` (`:231`) — TypeDecl, 807
nodes, definitional axis (D8), correctly out.

So of 6,093 uncovered portal nodes, **807 are declared out and 5,286 are role-mapped-but-undetected.**
The bank already carries grounded edge counts for the biggest block: `RENDERS n:2447` and
`PROP_PASSES n:1382` (`:645-646`), both `verdict: additive` — the frontend relations are ratified; no
motif consumes them. Independent confirmation it is a gap, not a boundary: the cascade doc's own step
2 (*"Extend the anchor catalog to the CODE substrates (portal + codebase)"*,
`SUBSTRATE_MODEL…:59-60`) and §3 (*"files/modules/components as anchors… today UNCOVERED"* `:41-43`).

## 4. The MS gap — 5,886 nodes, zero detectors, zero anchors, zero coverage. Declared.

- In any detector's constituent list: **0 of 5,886.** No `MS_*` type in the 24-type `_detector_types`
  list nor any `constituents` tuple.
- In `ANCHOR_CATALOG` (`NFRA_MOTIF_P1_canonical_ab_catalog.py:307-313`): **0** — five domains, seven
  types, all backend.
- Covered in the live graph: **0** (the distinct-target query returned rows for portal/aws/pipeline
  only).

Declared, not discovered: `c2_instances.json` → `grounding.knowledge_unreachable`, verbatim:
*"KNOWLEDGE is DECLARED-BUT-UNREACHABLE -- 0 detectors touch the 5,828 ms nodes; its emptiness is a
coverage fact, not an estate fact."* (5,828 was the 08-07 count; MEASURED-NOW 5,886, +58.)

MS types ARE role-mapped in the bank (`MS_FILE`→Store `:220`, `MS_FOLDER/MS_LIBRARY/MS_SITE`→Container
`:226`, `MS_USER`→contextual `:230`, `Custodian` derived from `MS_USER owns MS_FILE` `:110`). So ms is
*mapped and undetected* — same class as portal, at 0% instead of 13.2%.

## 5. How membership IS represented

MEASURED-NOW: ONE node label (`CloudNode`), ONE edge label (`CloudEdge`); membership is
`(CloudNode {node_type:'C2Motif'|'C3System'})-[CloudEdge {edge_type:'CONTAINS'}]->(CloudNode)` with
`edge.props.layer` = `"C2i->C1"` / `"C3->C2"` in the emitters. Queryable — that is how §1 was
produced.

Membership edge census (25 rows, top targets): Field 1353 · PipelineFunction 1235 · LAMBDA 561 ·
S3Key 456 · IAM_POLICY 405 · PipelineScript 319 · IAM_ROLE 175 · EVENT_RULE 110 · API_ROUTE 82 ·
EVENT_SOURCE 81 · Endpoint 56 · DataFetch 50 · ServedURL 45 · EC2_INSTANCE 38 · S3_BUCKET 32 ·
CW_ALARM 20 · INSTANCE_PROFILE 17 · DYNAMODB_TABLE 16 · SERVICE_PRINCIPAL 12 · ReactComponent 8 ·
API_GW 5 · CLOUDFRONT_DISTRIBUTION 1 · STATE_MACHINE 1 · KMS_KEY 1, plus **C3System-CONTAINS->C2Motif
= 12**.

Structural facts:
1. **Only 12 of 19 C2Motif nodes belong to a C3System** — 7 motifs C3-orphaned at class grain.
2. **The live C3 layer is 4 nodes** (`compute-orchestration`, `object-data`, `pipeline`,
   `firm-conditional-display`/EmergentSystem) — NOT the canonical 14, NOT the harness 1,255.
3. **ReactComponent 8 covered in-graph but absent from the 08-07 `_detector_types`** — from the 6
   defect detectors, which the Kimi `AB_CATALOG` excludes. The two instruments do not share a
   detector set.

## 6. Cascade budget arithmetic — labeled ARITHMETIC, per substrate

Budget: `DETERMINISTIC >=90% -> INFERENTIAL <=9% -> USER_DESCRIBED <=1%`, binds ESTATE-WIDE with
per-substrate splits DECLARED.

### 6a. At C0-NODE grain (ceiling = if every node any detector looks at were covered)

| Substrate | nodes | in detector scope | **ceiling** | covered now | >=90% needs | verdict |
|---|---|---|---|---|---|---|
| pipeline | 1,337 | 1,337 | **100.0%** | 1,291 (96.6%) | 1,203 | **ACHIEVABLE — already over** |
| aws | 2,055 | 1,597 | **77.7%** | 1,398 (68.0%) | 1,850 | **impossible** — 253 short of ceiling |
| portal | 11,338 | 5,245 | **46.3%** | 1,495 (13.2%) | 10,204 | **impossible** — 4,959 short of ceiling |
| ms | 5,886 | 0 | **0.0%** | 0 (0.0%) | 5,297 | **impossible** — 5,297 short of ceiling |
| **ESTATE** | **20,616** | **8,179** | **39.7%** | **4,184 (20.3%)** | **18,554** | **impossible** |

**ARITHMETIC CONCLUSION: >=90% deterministic at C0-node grain is achievable on exactly ONE substrate
of four (pipeline).** Estate-wide the ceiling is 39.7% against a 90% budget — the budget exceeds the
ceiling by 50.3 points, i.e. **10,375 nodes no detector or anchor currently references.** Closing it
is a *catalog-extension* quantity, not a *detector-tuning* quantity: 5,286 role-mapped portal nodes +
5,886 ms nodes + 458 out-of-scope aws types.

### 6b. At MOTIF-INSTANCE grain (the grain the cascade doc actually used)

PERSISTED-FROM-2026-08-07, `c3_structures.json` → `counts`: anchored 5,035/6,138 = **82.0%**
deterministic (doc: *"82% is short of the 90%+ target"* `:39-40`; gap = 487 instances).
`by_substrate_side: {"BACKEND": 1255}` — **all 1,255 C3.i structures are BACKEND; portal 0, ms 0**
(doc verbatim `:43`). `by_domain: {pipeline 847, object-data 242, identity 149, table-data 16,
compute-orchestration 1}`.

**The two grains disagree by 62 points (82.0% vs 20.3%) and both are correct.** Instance-grain
measures "of the motif instances we found, how many anchored" — a denominator produced by the
detectors themselves. Node-grain measures "of the estate, how much is reachable" — a denominator
independent of the instrument. **The 90/9/1 budget as written does not say which one it binds**, and
the two answers are on opposite sides of it.

## Labeling summary

- **MEASURED-NOW** (graph built 2026-08-12T18:25:51Z): §1 coverage figures, node/layer/type counts,
  §2 residue enumeration, §3 detector-scope arithmetic, §4 ms zero, §5 membership census, §6a.
- **PERSISTED-FROM-2026-08-07**: the coverage triple, 6,138 instances, 1,255 structures, 1,103
  unanchored, §6b.
- **PERSISTED-FROM-2026-08-06**: the origin 2693/3396 + 1495/11338 pair (reproduced today at
  2689/3392 and 1495/11338).
- **PERSISTED-FROM-2026-07-30**: 12 families / 135-chain census / 18-chain C2 residue; the 138-thread
  resolver.
- **INFERRED**: nothing. Every causal claim is source-confirmed to a constituent list or an anchor
  catalog literal, cited by file:line.

**Key paths:** `org\modules\graph\NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` ·
`org\modules\graph\NFRA_ONTOLOGY_RULE_BANK.yaml` · `org\modules\graph\estate-coverage-resolver.json` ·
`infra\system\ontology\SYSTEM_DEFINITIONS.yaml` ·
`org\tier2_senior\0.4.0_DS_ClientPlatform\deliverables\NFRA_MOTIF_P1_canonical_ab_catalog.py` ·
`org\tier1_exec\3.0.0_SA_CVO\deliverables\kimi_subdivision_harness\` ·
`org\tier1_exec\4.0.0_SA_CRO\deliverables\SUBSTRATE_MODEL_AND_DETERMINISTIC_CASCADE_20260811.md`
