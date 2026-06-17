# SEAM: extractor_full.ts (producer)  ->  portal_full.graph.json (emitted semantic graph)   (scale: MESO)
**validated against:** the live portal TS source (ground-truth territory) · **archetype:** VALIDATE
**run:** 0.4.0_DE_ClientPlatform · 2026-06-17 · NFRA_TSGRAPH.P1 Leg A integrity check (user-directed `/seams`)

## Seam definition
- **Side A (producer):** the full-portal ts-morph extractor — its 8 passes emit §3 nodes/edges.
- **Side B (artifact):** `out/portal_full.graph.json` — the emitted semantic graph (11,130 nodes / 12,911 edges).
- **Boundary / contract:** every emitted edge is a CLAIM about the portal source — a `FLOWS_TO`/`PROP_PASSES`/`RENDERS`/`FETCHES`/`HAS_TYPE` must correspond to a real, resolved TS construct; no false edges; every genuine unknown is VISIBLE (no-silent-Unknown). Ground truth = the actual portal `.tsx/.ts` source (for a static code-semantic extractor the source IS the live territory; the graph is not yet in Nessie — that's Leg B).

## Axis verdicts
| Axis | Verdict | Evidence | Delta (finding) |
|---|---|---|---|
| MECHANICAL | **BROKEN -> repaired -> SOUND** | sharp test found **41 dangling edges** (40 `FETCHES`->`endpoint:{fn}` nodes never emitted + 1 `FLOWS_TO`->external type) + a `queryFn` mis-resolution (`endpoint:FEATURES`, grabbed the first identifier not the call callee, from `ExecutiveSummary.tsx:107`). Repaired (commit below): queryFn now resolves the **call callee**; a finalization stub-pass materializes any missing endpoint as a VISIBLE `stub:true` node. Re-verified: **0 dangling**, `FEATURES` gone, 22 stubs visible. | false edges -> now 0; 2 hard queryFns now honestly unresolved-visible (hook_fetch 109/111) rather than 1 false `FEATURES` edge |
| DECLARATIVE | **PASS (clarified)** | the per-category coverage `attempted/resolved` (e.g. renders 1530/3264) counts EVERY candidate site incl. not-applicable ones (a `{localVar}` render, a prop on a library component), so `attempted-minus-resolved` (4625) is NOT the silent-Unknown gap — only the 639 `unresolved[]` entries are genuine unknowns/stubs. Added `meta.coverage_note` + `metrics.stub_count` so the metric self-documents (knowledge parity restored: a reader can no longer misread 4625 as silently-dropped). | believed "coverage denominator = should-resolve"; actually includes not-applicable — corrected in the artifact |
| SEMANTIC | **PASS** | 3/3 ground-truth spot-checks against source are correct: `PlatinumAccountTimeseriesPoint.nna_canonical -> nna [rename]` == `AdvisorBookView.tsx:490` (`nna: p.nna_canonical`); `<Tooltip content={...}>` PROP_PASSES == `BenchmarkHeatmap.tsx:413`; `RENDERS modelColor.primary` == `BenchmarkHeatmap.tsx:491` (`${modelColor.primary}`). Plus the P0 benchmark `model`/`spread` stitch (independently verified) + kind-discriminator sharp tests (0 rename-with-equal-names, 0 passthrough-with-condition). The resolved payloads are the RIGHT content. | none |

## Knowledge-parity delta
- **Believed:** the full-portal graph was clean field-grain truth (per the Leg-A-v1/depth RAVC2s).
- **True (was):** 41 edges were false (dangling), and `hook_fetch 111/111` over-counted a mis-resolved `FEATURES` edge as resolved. The coverage denominator could be misread as a 4625-item silent-Unknown gap.
- **Now:** repaired in the extractor — 0 dangling, false `FETCHES` removed, stubs + coverage semantics VISIBLE/self-documenting. Record corrected by fixing the code (I own it, DE-primary lane) + this report on the record.

## Verdict
**SOUND** (post-repair). Pre-repair: BROKEN@MECHANICAL (false/dangling edges). The resolved-edge content was always correct (SEMANTIC PASS); the defect was emitting edges to non-existent nodes + one mis-resolution — both now fixed and re-verified against the live source.

## Residual / unknowns
- 2 `queryFn`s (incl. `ExecutiveSummary.tsx:107`) now resolve to nothing under the stricter call-callee logic — VISIBLE-unresolved (hook_fetch 109/111), not false edges. A later refinement could resolve direct-ref/aliased queryFns; conservatism (no false edge) is the right default for now.
- The graph is NOT yet live in Nessie->Kuzu (Leg B, AE) — this seam validates the EXTRACTOR's output fidelity against source; the LIVE-graph stitch (DataFetch->Lambda-ARN against real Nessie) is re-validated at Leg B co-verify + the Leg C parity-gate.
- Perf: RENDERS `getSymbol`-per-prop-access keeps cold ~15s (AC4 scale-watch; caching queued).

## Compiler Tools
Validation was extractor-output-vs-source (ts-morph TypeChecker is the resolver under test); grounded with direct portal-source reads (`AdvisorBookView.tsx:490`, `BenchmarkHeatmap.tsx:413/491`) + structural sharp tests over the emitted graph (dangling/kind-contradiction/coverage-accounting). `comp-kuzu` against the live Nessie graph is deferred to Leg B (graph not yet ingested).
