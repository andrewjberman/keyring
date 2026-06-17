# NFRA_TSGRAPH.P0 — Spike Report (measured go/no-go)

**Author:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-17 · **Status:** SPIKE COMPLETE — verdict **GO**
**Feeds:** 1.0.0_SA_CTO formal PRD (build-vs-buy). **Consult:** 0.7.0_AE_CloudOps (emit rails).
**TO:** `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/NFRA_TSGRAPH.P0...spike.md`
**Brief:** `docs/briefs/intra-typescript-semantic-graph-research-20260617.md` (b95089ea3)
**Code:** `org/modules/graph/tsgraph_spike/` (extractor.ts, smoke.ts, measure_full.ts, load_scratch_kuzu.py)

---

## 0. TL;DR

A compiler-grade TypeScript semantic substrate (ts-morph / TS Compiler API) is **viable, cheap, and
materially better than the regex baseline**, proven on the model-portfolios benchmark slice:

- **The brief's blocking premise is dissolved.** "ts-morph absent on this machine" was about the
  *Python graph machine*; the extractor runs fine **locally under `bun` against the portal's own
  tsconfig** (and on a GO, in portal CodeBuild — the inc-2b pattern). No new toolchain needed.
- **AC1 (resolves) — PASS.** Real `TypeChecker` symbol/type resolution. Program-wide: **100% of 8,558
  JSX tags** and **97% of sampled prop-accesses** resolve to declarations. The regex tools, on the
  *same slice*, fail outright (details §3).
- **AC2 (field-grain stitch) — PASS.** The `model` field is a fully-connected path of **resolved**
  edges, served-JSON → JSX render. The hard served↔TS-type seam is bridged by the fetch return type.
- **AC3 (emits into platform) — PASS.** Slice nodes/edges land in Kuzu (scratch, per Rule 20) on the
  **real `CloudNode`/`CloudEdge` schema**; a `comp-kuzu` Cypher returns the stitch path; keys join to
  the live cloud graph (DataFetch→Endpoint→**real Lambda/bucket ARN**) — fixing the D8 key-space class.
- **AC4 (measured) — full-portal cold index ≈ 7.2s; incremental ≈ 12.5 ms/file.** Trivially fits the
  nightly derive + 5-min trace-cache cadence.
- **Build-vs-buy: BUILD-primary (ts-morph).** SCIP would only buy the symbol/reference backbone that
  ts-morph already gives for free; the goal-critical React/data-flow layer must be hand-built either
  way. Defer SCIP to a P1+ scale decision.

**Verdict: GO** to P1 (full-portal extractor + re-back `comp-types`/`comp-transform` with parity checks).

---

## 1. Slice + field (CTO-confirmed)

- **Slice:** model-portfolios **benchmark** surface — firm-agnostic (no firm-conditional fork in the
  spine), the known D8-FP chain `yang-model-portfolio-benchmarks → opal-data-portal-v2 →
  opal-portal-data-proxy → fetch → render`.
- **Field proven (AC2 spine):** `model` (model-portfolio return) — unconditional adapter passthrough,
  same name end-to-end, **0** intermediate prop-pass hops, directly rendered.
- **AC1 exhibit field (semantic-only):** `spread` — served as `etf_spread`/`index_spread`, **renamed**
  to `spread` through a **ternary-gated** adapter. The fetch response type has *no* `spread` field.
- Files: `portal/src/api/portal-proxy.ts` (types + fetch), `portal/src/pages/ModelPortfolios.tsx`
  (useQuery + adapter useMemo + JSX), `portal/src/components/BenchmarkHeatmap.tsx` (render).

---

## 2. The §3 node/edge schema, emitted

Extractor output (`out/benchmark_slice.graph.json`): **66 nodes / 77 edges**, **1** visible-unresolved.

| Nodes (by label) | n | Edges (by label) | n |
|---|---|---|---|
| Field | 36 | HAS_FIELD | 36 |
| TypeDecl | 6 | FLOWS_TO | 9 |
| Prop | 7 | DECLARES | 9 |
| Module | 3 | HAS_PROP | 7 |
| ReactComponent / Component | 2 / 2 | HAS_TYPE | 3 |
| JSXElement / Expr | 2 / 2 | PROJECTS_TO | 2 |
| DataFetch / Endpoint | 1 / 1 | FETCHES / CALLS / RENDERS / REFERENCES / PROP_PASSES / INSTANTIATES | 1 each |
| S3Artifact / GoldScript | 1 / 1 | READS_S3 / DERIVES_FROM / IS_ENDPOINT / HAS_KEY / ASSERTS_TYPE | 1 each |
| Hook / ReactQueryKey | 1 / 1 | | |

Every edge is derived from a resolver call (`getSymbolAtLocation` / `getTypeAtLocation` / contextual
type / JSX tag symbol) — **not a string match**. Keys are consistent with the existing regex graph
(`component:`/`endpoint:`/`s3:`/`gold:`/`rqk:`, per `extract_api.py`/`extract_pipeline.py`/`cache_cli.py`).

---

## 3. AC1 — fidelity vs the regex baseline (empirical, same slice)

Each is an actual command run this session, not an assertion:

| What | Regex tool (today) | ts-morph semantic substrate |
|---|---|---|
| Find the sub-component | `comp-transform schema-check BenchmarkHeatmap` → **"Component not found"** (file-grain registry; sub-components invisible) | resolves `BenchmarkHeatmap` as a `ReactComponent` with 7 typed props |
| Cross-ref rendered fields vs response schema | `comp-transform schema-check ModelPortfolios` → **`[WARN] no types.ts found`** → gives up (types live in `portal-proxy.ts`, not co-located) | resolves the response type through the import graph regardless of file location |
| The adapter ternary | `comp-transform ternary-audit ModelPortfolios` → **"No variables found with union types"** → misses it entirely | captures **both** branches of `benchmarkType === 'index' ? … : …` with their conditions |
| Renamed field across adapter (`etf_spread`→`spread`) | invisible: regex matches field-name strings; the response type has no `spread`, so the link can't be made | `FLOWS_TO`: `ModelPortfolioPeriodReturn.etf_spread —[benchmarkType==='index'==false]→ BenchmarkPeriodReturn.spread` (rename=true), + the `index_spread` branch |
| Computed-key access `periodData = model.returns[dataKey]` | cannot type a computed property access | resolves via indexed-access type → `BenchmarkPeriodReturn \| null` |

Program-wide resolution (whole `portal/src`, `measure_full.ts`): **8,558/8,558 JSX tags (100%)**,
**2,456/2,522 sampled prop-accesses (97%)**, **1,011/1,099 function return types**. The regex substrate
resolves none of this structurally — it pattern-matches text.

**A live cost of the regex blindness:** the renamed+ternary `spread` path is exactly the class of
display-logic the OFC/cohort bug-model (brief §7) needs to traverse, and the regex `ternary-audit`
returns empty on it. (Note also a real semantic finding the spike surfaced: in **ETF mode the rendered
`spread` is *recomputed in-component* — `modelReturnValue − benchmarkReturnValue` — overriding the
adapter's `spread`; `BenchmarkHeatmap.tsx:592-595`. A regex tracer would report the served `etf_spread`
as the rendered value and be wrong. The semantic graph can model this as a guarded `FLOWS_TO`.)

---

## 4. AC2 — the field-grain stitch (`model`), each `→` a resolved edge

`fully_resolved = true`. The connected path (materialized as `STITCH` edges; one Cypher returns it):

```
GoldScript  gold:yang-model-portfolio-benchmarks
  → (produces; external/D8-FP map — VISIBLE-unresolved, see §6)
S3Artifact  s3:json/benchmarks/model_portfolio_benchmarks.json
  → READS_S3 (served URL literal RESOLVED from apiRequest('/api/general/benchmarks/...json'))
Endpoint    endpoint:getModelPortfolioBenchmarks
  → IS_ENDPOINT
DataFetch   getModelPortfolioBenchmarks   [portal-proxy.ts:807]
  → HAS_TYPE  ===  THE SEAM: served-JSON field == TS-type field, bridged by the fetch return type
                   apiRequest<ModelPortfolioBenchmarksResponse>  (§5 lever)
Field       ModelPortfolioPeriodReturn.model   [portal-proxy.ts:751]
  → FLOWS_TO (adapter useMemo, model: data.model — unconditional)   [ModelPortfolios.tsx:722]
Field       BenchmarkPeriodReturn.model   [portal-proxy.ts:700]
  → HAS_TYPE benchmarkData : BenchmarkModelData[]  /  PROP_PASSES  <BenchmarkHeatmap data={benchmarkData}>
Prop        BenchmarkHeatmap.data   [ModelPortfolios.tsx:2035]
  → type-structure → field ; render REFERENCES
Expr        periodData.model  (REFERENCES BenchmarkPeriodReturn.model)   [BenchmarkHeatmap.tsx:586/614]
  → RENDERS
JSXElement  renderDataCell(value, …)   [BenchmarkHeatmap.tsx:620]
```

The "hard seam" (served-JSON field → TS-type field) is bridged via the fetch's TS return type + the
React-Query key (`rqk:model-portfolio-benchmarks` resolved from the `queryKey` literal; `queryFn`
symbol-resolved to the fetch). This is the §5 design, working.

---

## 5. AC3 — emits into the platform; keyed consistently (D8 fix)

- **Schema fidelity (per AE's emit contract, msg 192324Z):** the globgrph derive ingests
  `CloudNode(node_id, node_type, …)` / `CloudEdge(source, target, edge_type, …)` where the *type*
  fields are **string discriminators** — so `Module/Symbol/Field/ReactComponent/DataFetch` +
  `REFERENCES/FLOWS_TO/FETCHES/RENDERS` land in the **same two tables, no schema change**. The scratch
  load uses exactly this schema, so the spike's Cypher is the same query that would run against
  Nessie→Kuzu.
- **Derive-ready emit:** `out/ts_semantic_benchmark_slice.producer.json` — AE's contract keys
  (`{id,type,…}` / `{source,target,edge_type,…}`) wrapped in the manifest with the
  `coverage.unresolved` no-silent-Unknown guard. On a GO, AE adds the S3-prefix ingestion leg
  (`producers/ts-semantic/<slice>.json`, his derive lane) and we co-verify.
- **The join works (D8 key-space fix), grounded against live state:** the cloud-side join targets are
  **present in the canonical Nessie graph** (queried this session, provenance *current*):
  `arn:aws:s3:::opal-data-portal-v2` (S3_BUCKET), `arn:aws:lambda:…:opal-portal-data-proxy` (LAMBDA),
  `opal-portal-data-proxy-api` (API_GW). In the scratch DB (one CloudNode space), `comp-kuzu` returns:
  ```
  DataFetch fetch:…:getModelPortfolioBenchmarks → Endpoint endpoint:getModelPortfolioBenchmarks
            → arn:aws:lambda:us-east-1:313476888478:function:opal-portal-data-proxy
  ```
  The semantic node keys join to the AWS ARNs exactly as `derive_stitch.py` does (name→ARN). This is
  the precise inverse of the 06-17 D8 FP (where `node_type:name` keys never met ARN keys).
- **Scratch honesty:** `comp-kuzu --db-path <scratch>` correctly reports **`UNKNOWN VINTAGE`** — the
  scratch DB is a frozen vintage (Rule 20), never quoted as the estate.
- **Division of labor (no over-claim):** the extractor resolves down to the served URL literal; the
  URL→S3-key and the precise CloudFront-vs-Lambda serving path are the **cloud/trace graph's** job
  (`comp-routes`/`derive_stitch`), recorded as one **VISIBLE-unresolved** item, not faked (§6).

---

## 6. The one visible-unresolved item (no silent Unknown)

`URL → S3-key + S3 → gold` mapping @ `endpoint:getModelPortfolioBenchmarks`: the proxy/CloudFront
routing and the producer are **not expressible in TS**; carried from the cloud/trace graph on
consistent keys. Marked VISIBLE in both the extractor output and the producer-JSON `coverage.unresolved`
— exactly the `comp-platinum` `url:(not resolved)` + inc-2b coverage-guard discipline. This is correct
behavior, not a gap to "fix" in the TS layer.

---

## 7. AC4 — measured index cost (extrapolated to full portal)

`measure_full.ts`, whole `portal/src` (374 files):

| Metric | Value |
|---|---|
| Program load (one-time, `createProgram` + type-check) | ~2.5 s |
| Full semantic walk (all 374 files) | ~4.7 s |
| **Cold full-portal index** | **~7.2 s** |
| Slice-only extract (3 files, warm program) | ~0.9 s |
| Per-file walk avg (→ incremental re-index, warm program) | **~12.5 ms/file (sub-second)** |
| Interfaces / fields resolved | 789 / 4,246 |
| Functions / return types resolved | 1,099 / 1,011 |
| JSX tag symbols resolved | 8,558 / 8,558 (100%) |

A ~7 s cold index and ~12 ms incremental re-index sit **comfortably** inside the nightly derive +
the 5-min trace-cache cadence (brief §8.6). Incrementality is a P1 optimization, not a v1 blocker.

---

## 8. Build vs buy — SCIP effort estimate (the §4 / §11.2 decision input)

- **What SCIP/scip-typescript would buy:** the symbol/reference backbone — roughly the `DECLARES` /
  `REFERENCES` / `IMPORTS` / `HAS_FIELD` / coarse `HAS_TYPE` edges (~the structural ~60% of edge
  volume), off-the-shelf as a stable protobuf, with cross-repo + incrementality built in.
- **What it does NOT buy:** the **goal-critical** layer — `FLOWS_TO` (def-use field-grain),
  `RENDERS`, typed `FETCHES`, `PROP_PASSES`, the adapter field-mapping resolution, JSX/React semantics.
  Those are ~13 edges here but they are the entire reason the 3 Andrew goals are reachable, and they
  must be hand-built on the Compiler API **regardless of SCIP**.
- **What the spike showed:** ts-morph already gives the backbone *for free* and *correctly* (smoke +
  100% JSX + 97% prop resolution), so SCIP's value is **scale/cross-repo**, not capability. Adopting
  SCIP costs a SCIP-protobuf→our-nodes transform **plus** still building the React layer — it does not
  shrink the hard part.
- **Recommendation:** **BUILD-primary (ts-morph), defer SCIP** to a P1+ decision gated on measured
  full-portal incremental-index pain. Given ~7 s cold / ~12 ms incremental, that pain is not in sight.

---

## 9. Verdict + handoff

**GO.** The substrate is real, cheap, and strictly better than regex; the field-grain stitch is
provable; the emit-into-platform leg is small and AE-owned with the contract already agreed.

- **P1 target:** full-portal extractor (incremental) → load into Nessie→Kuzu (AE wires the ingestion
  leg) → re-back `comp-types` + `comp-transform` on the real graph with **parity checks** vs the regex
  tools (no regressions). Resolve `endpoint:` sub-key convention (fn-name vs path) with AE at wire time.
- **P1 ideal stress-test (CTO-flagged):** the **NNA-attribution** chain (dual-attribution fork +
  inference + type-flow) — excluded from P0 as in-flux; it is exactly what the semantic graph should
  illuminate.
- **Verification discipline carried (brief §8.8):** the semantic graph is a minutes-stale labeled
  traversal surface, **never** a read-your-own-change substrate (F5). All spike claims were verified
  against the real portal source + the live Nessie graph, and the scratch Kuzu is labeled frozen.

---

*Grounding: every claim above is a command run or a file read this session — ts-morph smoke/extractor/
measure runs; `comp-transform` regex baseline; `comp-kuzu` against the canonical Nessie DB (provenance
current) and the scratch DB; the portal source at the cited file:line. Artifacts under
`org/modules/graph/tsgraph_spike/` (+ `out/benchmark_slice.graph.json`, `out/ts_semantic_benchmark_slice.producer.json`).*
