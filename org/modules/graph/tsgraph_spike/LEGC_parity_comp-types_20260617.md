# Leg C parity-gate — comp-types (result #1)

**Author:** 0.4.0_DE_ClientPlatform · 2026-06-17 · NFRA_TSGRAPH.P1 Leg C (started; user-directed "begin if able")
**Reviewer (cutover gate):** 1.0.0_SA_CTO · **Discipline:** GLDINC incremental-vs-oracle parity, tool-by-tool, equivalence-or-BETTER before cutover, NO rip-and-replace.
**Graph:** live Nessie->Kuzu (provenance current, 12,397 nodes, the ts-semantic layer ingested by AE's Leg B). NOTE: ingestion is payload-LOSSY (kind/condition dropped — AE owns the props-column fix); comp-types uses node_id/structure only, so it is UNBLOCKED by that defect.

## Probe type: `BenchmarkModelData` (3 fields: code, name, returns)

### comp-types `fields` (per-field consumer enumeration) — SEMANTIC **BETTER (precision)**
| | regex baseline | semantic (live graph) |
|---|---|---|
| `name` consumers | **203, "READ-EVERYWHERE"** | **~4 real** — `FLOWS_TO -> ScatterPoint#name` (adapter) + 3 `RENDERS` (ReturnVolatilityScatter.tsx:485/558/583) |
| failure mode | substring-matches every `.name` in the portal | resolved field-grain readers only |

The regex `203` is a substring artifact (`name` is one of the commonest identifiers). The semantic version returns the **actual** readers of `BenchmarkModelData.name`. This is a large precision win and exactly the goal-1 fine-lineage payoff. **Verdict: BETTER** — pending a recall sweep (confirm every real reader is captured across all fields/types before cutover).

### comp-types `index` (type consumer SITES) — SEMANTIC **RECALL GAP — NOT yet parity**
- Regex: 44 sites — but ~37 are false (`tenantLayout.dataSources`, `layout.tabs.advisors.enabled`, `DEFAULT_LAYOUT` — unrelated). ~7 are real (the imports + `data: BenchmarkModelData[]` annotations).
- Semantic: only `module:portal/src/api/portal-proxy.ts -[DECLARES]-> type#BenchmarkModelData`. The extractor does **not** emit a "type referenced by" edge for nested/annotation type-uses (e.g. `data: BenchmarkModelData[]` inside `BenchmarkHeatmapProps`, or a `model: BenchmarkModelData` param). So the semantic type-index would **MISS** real consumers → a recall regression vs the regex's true-positive subset.
- **Verdict: NOT parity.** Cutover BLOCKED for `index` until a `REFERENCES_TYPE` pass is added (TS Compiler API `findReferences` / `getReferencingNodes` on the type symbol — gives every reference site precisely, eliminating BOTH the regex false-positives AND the recall gap in one pass).

## Cutover decision (this increment)
- `comp-types fields`: semantic better on precision; **stay on regex until a recall sweep confirms no true-positive is missed**, then cut over (CTO sign).
- `comp-types index`: **stays on regex**; semantic needs the `REFERENCES_TYPE` extractor pass first (the next unblocked Leg-C work item — structural, no dependency on AE's props fix).

## Next (Leg C, unblocked vs blocked)
- UNBLOCKED (structural): add the `REFERENCES_TYPE` pass (findReferences) -> re-run `comp-types index/fields` parity across a sample of types -> recall+precision table -> CTO cutover review.
- BLOCKED on AE props fix: the kind-aware `comp-transform` re-back (ternary-audit / MISSING-UNUSED-with-conditions) + the goal-3 display-logic-bug analyses + AC5 — these need the dropped FLOWS_TO kind/condition.
