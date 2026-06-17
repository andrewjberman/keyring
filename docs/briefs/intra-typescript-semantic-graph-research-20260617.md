# Research Brief — Intra-TypeScript Semantic Graphing (NFRA_TSGRAPH seed)

**Author:** 1.0.0_SA_CTO · **Date:** 2026-06-17 · **Status:** RESEARCH (Andrew-direct; seeds a possible NFRA_TSGRAPH project under the graph platform)
**Sibling of:** NFRA_GRAPHS (graph-tooling reconciliation), NFRA_GLOBGRPH (versioned global graph). This extends the *frontend* layer of that platform.

---

## 0. The ask (verbatim intent)

Expand our graphing functions to:
1. **Fine lineage** — extremely fine tracking from backend/database all the way INTO the TypeScript (field/prop-grain, not artifact/component-grain).
2. **Data-consumption clusters** — identify clusters of components connected by pulling the same data.
3. **TS lexical/semantic model** — audit + model how TypeScript actually works as intra-language node-edges, so we can assess frontend bugs / logic issues by graph traversal.

---

## 1. Executive summary

**The platform already has the right SHAPE** — three graphs (CLOUD = AWS-infra via Kuzu/Nessie; TRACE = repo/code via `graph.json`; CROSS-LAYER STITCH = `PortalComponent -[:FETCHES]-> ApiRoute -[:ROUTES_TO]-> Lambda -[:WRITES]-> S3`), a versioned Nessie/Iceberg→Kuzu store with a freshness/HEAD oracle, and a ~30-tool `comp-*` query surface.

**The frontend layer is the bottleneck, and the cause is a documented substrate limitation.** Every frontend graph tool (`extract_api.py`, `transform_cli.py`, `types_cli.py`, `comp-cache`, `comp-platinum`, `comp-adapter-audit`) parses TSX with **Python regex/heuristics**. `comp-tools.yaml` states it outright: *"Python regex approach (ts-morph absent on this machine)"*, *"regex-based portal grep; no ts-morph required."* Regex cannot resolve imports, types, symbols, control-flow, re-exports, prop-drilling, context, or hook composition. So our intra-TS graph is **coarse** (whole-`COMPONENT` / whole-`ENDPOINT` nodes), **brittle** (syntax-fragile), and **semantically blind**.

**This reframes the project.** Goal 3 is not "extend the regex tools" — it is **"introduce a compiler-grade TypeScript semantic substrate."** Once that substrate exists, goals 1 and 2 largely fall out as *queries/analyses over a richer graph* rather than new bespoke parsers. The single highest-leverage move is: **stand up a TS-Compiler-API/ts-morph (or SCIP) extractor that emits a fine-grained semantic graph into the same Nessie→Kuzu platform, stitched to the existing cloud + trace graphs.**

**Today's live evidence this is the right gap:** the 2026-06-17 D8 surface-scan false-positive (adjudicated this session) was *caused by exactly this* — the canonical derive graph is AWS-infra-only, the portal-AST lives in a separate coarse `node_type:name`-keyed build, and the two key-spaces never intersect. A real semantic portal graph keyed consistently with the estate graph dissolves that class of problem.

**Recommendation:** scope an `NFRA_TSGRAPH` project; P0 = a spike proving a TS-semantic extractor + the field-grain stitch on one page-slice; then re-back the existing `comp-*` frontend tools on the real graph and layer the cluster + bug-query analyses on top. **Blocking decision for Andrew:** the "ts-morph absent on this machine" toolchain constraint must be resolved (a Node/TS toolchain for the graph machine, or a CI/CodeBuild-hosted extractor — note the portal itself already runs bun + @typescript-eslint, so the toolchain exists *in the portal repo*, just not in the Python graph tooling).

---

## 2. Current state (grounded, not assumed)

### 2.1 The three graphs + stitch (the good news)
- **CLOUD** — `comp-aws derive` → Nessie/Iceberg → `comp-kuzu`. `CloudNode`/`CloudEdge` (LAMBDA, S3_BUCKET, ROLE, ...). Nightly + intraday; provenance-headed; HEAD-oracle freshness.
- **TRACE** — `comp-build` → `graph.json` (5-min cache); `comp-trace`/`comp-blast`/`comp-xref`. Repo/code deps (imports, fetches, reads/writes) at **file/function grain**.
- **STITCH** (P2-STITCH, landed 2026-06-11, `derive_stitch.py`) — joins trace+cloud: `COMPONENT/ENDPOINT` (regex-extracted) → `LAMBDA`/`GOLD_SCRIPT`/`S3`. `comp-kuzu` Cypher answers `component → lambda → bucket` per firm.

### 2.2 The frontend extraction (the bottleneck)
All Python, all regex/heuristic over `*.tsx`/`*.ts`:
- `org/modules/graph/extract_api.py` — emits `component:{rel_path}` (`COMPONENT`) + `endpoint:{fn_name}` (`ENDPOINT`) nodes + `FETCHES` edges. **The frontend node model: file-grain components, function-grain endpoints. No symbols/types/props/hooks/statements.**
- `transform_cli.py` (`comp-transform`) — regex field-render analysis: which response **fields** a component renders (MISSING/UNUSED), `ternary-audit` for cohort/mode branches. *Real field-grain signal, but per-component and regex-derived, not a connected graph.*
- `types_cli.py` (`comp-types`) — *"~5s regex portal grep"* type-consumer index. No real type resolution.
- `comp-cache` — React Query cache-key collisions (**components sharing a key share data** — the goal-2 seed).
- `comp-adapter-audit` — adapter field-threading (live S3 + regex).
- `comp-platinum` — component→gold full-stack trace, *"static heuristic, inf producer-incomplete."*
- `comp-routes` — CloudFront→origin→Lambda serving path.

### 2.3 What the regex substrate cannot do (the cap on all 3 goals)
- Resolve an `import`/re-export to the actual definition (no symbol resolution).
- Know a value's **type** (no type-checker) → can't follow a field through an adapter, a generic, or a union.
- Follow **control flow** (ternaries, guards, early returns) beyond a single-file heuristic → the OFC cohort-bug class lives here.
- Track **prop-drilling / context / hook composition** (React data-flow is not lexically local).
- Distinguish a real edge from a string coincidence (regex false-positives/negatives; the D8 key-space mismatch is a cousin).

---

## 3. The target — a TypeScript semantic graph model (Goal 3 core)

Model TS the way the **compiler** sees it: a typed AST + symbol graph + type graph, enriched with React semantics. Proposed node/edge schema (emitted into Nessie→Kuzu alongside `CloudNode`/`PortalComponent`):

**Nodes** (fine grain): `Module/File`, `Symbol` (the resolved declaration — the unit `find-references` uses), `TypeDecl` (interface/type/enum), `Function`, `ReactComponent`, `Hook` (use* call-site + custom hooks), `Prop`, `StateVar` (useState/useReducer), `ContextDef`/`ContextUse`, `JSXElement`, `DataFetch` (fetch/apiRequest/useQuery call-site, with its key + return type), `Field` (a property of a type/object), `Statement`/`Expr` (only where bug-analysis needs it — control-flow nodes).

**Edges** (semantic, resolved — not string-matched): `IMPORTS`/`EXPORTS`, `DECLARES`, `REFERENCES` (symbol use→def), `CALLS`, `INSTANTIATES` (JSX `<Child/>` → component), `HAS_TYPE`/`TYPE_OF`, `EXTENDS`/`IMPLEMENTS`, `HAS_FIELD`, `FLOWS_TO` (data/def-use: assignment, return, prop-pass, destructure), `RENDERS` (JSX → field/expr), `FETCHES` (component/hook → endpoint, **typed**), `PROVIDES_CONTEXT`/`CONSUMES_CONTEXT`, `PROP_PASSES` (parent JSX → child prop), `HOOK_DEP` (useEffect/useMemo dep array → symbol).

This *is* goal 3: a queryable intra-language node-edge model. It subsumes the current `COMPONENT`/`ENDPOINT` nodes as a coarse projection, and it is keyed consistently so it stitches to the cloud graph (fixing the D8-class key-space mismatch).

---

## 4. Substrate options (build vs buy) — the load-bearing decision

| Option | What it gives | Cost/risk | Fit |
|---|---|---|---|
| **TS Compiler API** (`ts.createProgram` + `TypeChecker`) | Ground truth: full typed AST, symbol/type resolution, `getSymbolAtLocation`, `findReferences`, control-flow graph. Node-based. | Build the extractor + walk; verbose API; we own it. | **Primary recommendation** for the semantic emitter — it's the same engine `tsserver`/`tsc` use, so "what the language actually does" is authoritative. |
| **ts-morph** | Ergonomic wrapper over the Compiler API (same fidelity, far less boilerplate). | A dependency; the very thing flagged "absent on this machine." | **Recommended authoring layer** if we resolve the toolchain — fastest path to a correct extractor. |
| **SCIP / scip-typescript** (Sourcegraph) | An off-the-shelf **precise** index: symbols + definitions + references + cross-repo, emitted as a stable protobuf. LSIF's successor. | Index format → we transform SCIP→our nodes/edges; less React-semantic (it's general symbol/ref). | **Strong backbone** for the symbol/reference layer (REFERENCES/DECLARES) — buy the hard name-resolution, build the React-semantic layer on top. |
| **Stack Graphs** (GitHub) | Incremental, precise name-resolution-as-graph. | Newer; TS support maturity to validate. | Optional — name resolution only. |
| **tree-sitter** | Fast, incremental **syntax** parsing. | **No types/semantics** — syntax only. | Useful for cheap structural passes / incremental reparse; NOT a semantic substitute. |
| **CodeQL / Glean** | Code-as-database with a real dataflow library. | Heavy; ecosystem lock-in; learning curve. | Over-scoped for v1; revisit if we want industrial dataflow/taint. |

**Recommended substrate:** a **Node extractor on the TS Compiler API (authored via ts-morph)**, optionally seeded by **SCIP for the symbol/reference backbone**, emitting our node/edge schema as JSON → the existing Iceberg/Nessie→Kuzu write-path. This reuses *all* of the platform's versioning/freshness/query investment; only the *frontend extractor* is new. (The portal already has the TS toolchain — bun + @typescript-eslint — so the extractor can run **in the portal repo's CI/CodeBuild**, mirroring the inc-2b drift-producer pattern we just shipped, rather than needing ts-morph on the Python graph machine.)

---

## 5. Goal 1 — fine backend→TS lineage (field/prop grain)

**Extend the stitch from component-grain to field/prop grain.** Target chain (each `→` a resolved edge, not a heuristic):

`gold-field → served-artifact-field → fetch-return-type-field → adapter-mapping → hook-data → component-prop → (prop-pass)* → JSX-render-of-field`

- **Backend side** (already in cloud/trace): gold script → S3 artifact. *Enrich with the artifact's field schema* (we already validate artifact shape in `comp-validate`/`comp-adapter-audit` — promote the field list to graph nodes).
- **The seam** (data-fetch boundary — the hard join): connect a served JSON **field** to the TS **type field** that consumes it. Resolution levers: (a) the fetch's TS return type (Compiler API gives the exact `Field` set); (b) the adapter function's field-mapping (def-use `FLOWS_TO` from raw→mapped); (c) the React Query **key** as the cache-identity linkage (we already have `comp-cache` keys). Where the URL is a dynamic string, fall back to the route-pattern + the type (the same `url:(not resolved)` honesty `comp-platinum` already prints — keep it visible, never silent).
- **Frontend side** (new, from the semantic graph): hook→component prop→sub-component prop (`PROP_PASSES`)→`RENDERS`(field). The Compiler API resolves the prop types + the destructuring + the render expressions.

**Payoff:** "if gold field `X.y` changes / disappears, exactly these components + render-sites break" — at field grain, per firm. This is the real version of what `comp-transform` MISSING/UNUSED approximates today per-component.

---

## 6. Goal 2 — component data-consumption clusters

Model the **bipartite component↔data graph** (components × data-sources) where a data-source is {gold artifact | served key | endpoint | React-Query key | shared hook | shared type}. Edges = "component consumes source" (from the fine lineage of §5).

- **Seed already exists:** `comp-cache collisions` (components sharing a React Query key literally share cached data) is a primitive cluster signal. Generalize it.
- **Clustering:** run community detection (label propagation / Louvain — Kuzu can export to a graph-analytics pass, or compute over the projected bipartite adjacency) to surface **clusters of components bound by shared data**.
- **Use cases:** blast radius ("change artifact A → cluster C of N components"); cohesion/coupling audit (a component pulling from many unrelated clusters = a refactor smell); shared-state corruption risk (the cache-key class); cohort/firm asymmetry (a cluster that resolves on one firm but not another — the D7 anomaly class, made precise).

---

## 7. Goal 3 — bug/logic assessment by traversal (what the model buys)

Each maps to a graph query over the §3 model:
- **Type-flow breaks / `any`-erosion** — `HAS_TYPE` to `any` on a `FLOWS_TO` path from a typed fetch (the debtscan found 7× `any` in `endpoints/portfolio.ts`); flag silent `any` widening. (Today `typed_field_count=0` is a manual `comp-adapter-audit` read.)
- **Dead / unused** — `Symbol`/`Field`/`Prop`/`Component` with no inbound `REFERENCES`/`RENDERS`/`INSTANTIATES` (real dead-code, not regex-guessed).
- **Prop-drilling smells** — long `PROP_PASSES` chains; a prop threaded N levels unchanged = a context candidate.
- **Cohort/mode logic bugs (the OFC class)** — `RENDERS`/`FLOWS_TO` gated by a ternary/guard `Expr`; surface cohort branches that fall through to the wrong path. This is `ternary-audit` made control-flow-real.
- **Hook-dependency issues** — `HOOK_DEP` array vs the symbols actually referenced in the effect/memo (missing/extra deps = stale-closure bugs).
- **Cross-firm conditional asymmetry** — firm-conditional `Expr` sites where one firm's path renders a field and the other's doesn't (precise version of the D7 firm-asymmetry anomaly).
- **Render-guard logic** — `RENDERS` under a null/loading guard vs the data's actual nullability type (the 555%-class *display* bugs live near here, though PMTRDX itself was a unit bug).

---

## 8. The hard problems (honest — these bound the design)

1. **Structural typing** — TS types are structural, not nominal; "the same type" is a shape, not an identity. The `Symbol`/`TypeDecl` graph must record both the declaration *and* structural-assignability edges, or `comp-types`-style "who consumes this type" stays fuzzy. The Compiler API's checker handles this; a naive AST walk does not.
2. **Control-flow sensitivity** — a field's nullability/type narrows inside guards. Field-grain bug analysis needs at least basic CFG/narrowing (the Compiler API exposes flow nodes; use them, don't re-derive).
3. **Dynamic dispatch / HOCs / render-props / `as`-casts** — React patterns that defeat static resolution. Policy: resolve what's resolvable, **mark the rest `unresolved` and VISIBLE** (the platform's existing "no silent Unknown" discipline — same as `comp-platinum`'s `url:(not resolved)` and the inc-2b coverage guard we shipped today).
4. **Non-lexical data-flow** — context, global stores, event buses. Model `PROVIDES/CONSUMES_CONTEXT` explicitly; accept residual runtime-only flows as a recorded gap.
5. **The fetch boundary** — string URLs, dynamic keys, double-wrapped `apiRequest`. Triangulate (type + key + route-pattern); never assert a false edge.
6. **Scale / incrementality** — a full `createProgram` over the portal is seconds-to-minutes; design for **incremental** re-index (changed files + their dependents), mirroring the trace graph's 5-min cache + the nightly derive. SCIP/Stack-Graphs are built for this if the hand-rolled walk is too slow.
7. **Migration, not big-bang** — the regex tools *work today* and are battle-tested (D7 anomaly pilot). Re-back them on the semantic graph **tool-by-tool with parity checks** (same discipline as the GLDINC incremental-vs-oracle parity), don't rip-and-replace.
8. **Verification discipline (unchanged platform law)** — the semantic graph is a *minutes-stale, labeled* traversal surface, **never** a read-your-own-change verification substrate. Verify a just-made change against the built artifact / running app, not the graph (the F5 rule). Carry the same provenance-header + HEAD-oracle freshness contract.

---

## 9. Integration with the existing platform (reuse, don't rebuild)

- **Emit into Nessie/Iceberg → Kuzu** — the semantic graph is just new node/edge tables in the versioned store; `comp-kuzu` Cypher queries it; the freshness/HEAD-oracle + provenance header apply unchanged.
- **Stitch to cloud + trace** — `DataFetch`/`endpoint` → `Lambda` → `gold` → `S3` is the existing P2 stitch, now extended *upward* to field/prop grain.
- **Re-back the `comp-*` frontend tools** — `comp-types` (real type-consumers, not regex), `comp-transform` (real render-field graph), `comp-platinum` (real component→gold, retiring the heuristic producer-resolution residual), `comp-cache` (generalized to clusters). Same CLIs, real substrate.
- **Fixes the D8 class** — a properly-keyed semantic portal graph means the critical-surface scan can diff portal surfaces like-for-like instead of the AWS-only-vs-merged-baseline key-space mismatch we hit today.
- **Run-site** — the extractor runs where the TS toolchain is: portal-repo CI / CodeBuild (the inc-2b drift-producer pattern), writing to S3 → the nightly derive picks it up. Avoids the "ts-morph absent on the Python graph machine" blocker entirely.

---

## 10. Phased roadmap (proposed)

- **P0 — Spike (prove the spine).** Stand up a ts-morph/Compiler-API extractor on ONE page-slice (e.g., a model-portfolios or advisor page). Emit the §3 nodes/edges for that slice; prove the **field-grain stitch** (one gold field → one rendered field, end to end) and the symbol/type resolution. Output: a go/no-go on the substrate + a measured index cost. *Low cost, high information.*
- **P1 — Semantic graph + re-back two tools.** Extractor over the full portal (incremental); load into Nessie→Kuzu; re-back `comp-types` + `comp-transform` on the real graph with **parity checks vs the regex tools** (no regressions). Resolve the toolchain/run-site decision.
- **P2 — Clusters (Goal 2).** Build the component↔data bipartite projection + community detection; ship a `comp-cluster` view (generalizing `comp-cache collisions`). Blast-radius + cohesion use-cases.
- **P3 — Bug/logic query library (Goal 3).** Ship the §7 analyses as canonical `comp-*` / Cypher use-cases (type-flow breaks, dead code, prop-drilling, cohort-logic, hook-deps, firm-asymmetry). Fold the highest-signal ones into the commit-gate / critical-surface scan.
- **P4 — Full fine lineage + integration (Goal 1).** Field/prop-grain stitch across the whole portal; retire the heuristic `comp-platinum` producer-resolution; integrate into the nightly derive + the D8 critical-surface scan with proper keying.

Each phase gates on a parity/verification check (platform discipline) and ends with an honest coverage number (the "no silent Unknown / cannot-assess is visible" rule, exactly like the inc-2b drift producer).

---

## 11. Decisions for Andrew

1. **Toolchain / run-site** (BLOCKING) — accept running the TS extractor in portal-repo CI/CodeBuild (recommended; sidesteps "ts-morph absent on the graph machine"), or provision the Node/TS toolchain on the graph machine?
2. **Build vs buy substrate** — Compiler-API/ts-morph extractor we own (recommended primary) vs adopt SCIP/scip-typescript for the symbol backbone (recommended as a complement)? Or hold for a P0 spike to decide on measured evidence (recommended)?
3. **Scope of the lexical model** — React-focused (components/hooks/props/fetches/render — covers the 3 goals) vs full general-TS semantic graph (broader, heavier)? Recommend React-focused v1, general-TS as the substrate naturally provides it.
4. **Project shape** — spin this up as `NFRA_TSGRAPH` under the graph platform (sibling to NFRA_GRAPHS/GLOBGRPH), starting at the P0 spike? CTO recommends yes.

---

*Grounding: graph-call-manifest.yaml; org/modules/graph/{extract_api,transform_cli,types_cli}.py; comp-tools.yaml ("ts-morph absent on this machine"); infra/aws/globgrph/derive_stitch.py; the 2026-06-17 D8 surface-scan FP adjudication. External technique survey from CTO knowledge (TS Compiler API, ts-morph, SCIP/LSIF, Stack Graphs, tree-sitter, CodeQL) — a deeper external lit-review + a measured P0 spike refine the substrate choice.*
