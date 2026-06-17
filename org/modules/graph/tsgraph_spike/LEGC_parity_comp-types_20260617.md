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

The regex `203` is a substring artifact (`name` is one of the commonest identifiers). The semantic version returns the **actual** readers of `BenchmarkModelData.name`. This is a large precision win and exactly the goal-1 fine-lineage payoff. **Verdict (precision): BETTER** — but the recall sweep (below) found gaps, so `fields` is NOT yet cutover-ready.

### comp-types `fields` RECALL SWEEP (result #4) — semantic precise but RECALL-INCOMPLETE
Semantic per-field reader count (RENDERS->field + FLOWS_TO-from-field) vs regex:
| field | regex | semantic | 
|---|---|---|
| BenchmarkModelData.name | 203 | 5 | BenchmarkModelData.code | 67 | 8 | BenchmarkModelData.returns | 27 | **0** |
| BenchmarkPeriodReturn.model | 28 | 1 | …spread | 16 | **0** | ModelPortfolioData.code/name/returns | 67/203/27 | **0/0/0** |

Precision: semantic kills the regex substring overcount (good). But the **0/low counts are a RECALL GAP**, confirmed against source:
- `ModelPortfolioData.*` = 0 FLOWS_TO — the OUTER benchmark adapter `{code: model.code, name: getCanonicalModelName(model.name), returns: Object.fromEntries(...)}` (ModelPortfolios.tsx:708) is **skipped by the FLOWS_TO ">=2-mappingish-props" heuristic** (only `code` is a property-access; `name`/`returns` are CallExpressions). A real, fixable extractor bug.
- `*.returns` / `*.spread` low — indexed-access reads (`model.returns[k]`) + computed reads aren't captured as field-readers.
- arbitrary `const x = obj.field` reads outside JSX/adapter need a field-level findReferences.
- **Verdict: NOT parity (recall-incomplete).** Path to fields parity: (1) fix the FLOWS_TO mappingish heuristic to include CallExpression-initialized props; (2) capture indexed-access field reads; (3) a `REFERENCES_FIELD` pass (findReferences per field — HEAVY, ~minutes over 4870 fields) for full read-recall. Deferred to the Leg-C resume (with the kind-aware work).

### comp-types `index` (type consumer SITES) — SEMANTIC **EQUIVALENCE-OR-BETTER** (gap closed, result #2)
- Regex: 44 sites — but ~37 are false (`tenantLayout.dataSources`, `layout.tabs.advisors.enabled`, `DEFAULT_LAYOUT` — unrelated substring hits). ~7 real (3 files: BenchmarkHeatmap, ReturnVolatilityScatter, ModelPortfolios).
- Result #1 (no REFERENCES_TYPE): only `DECLARES` pointed at the type → recall gap.
- **Result #2 — added the `REFERENCES_TYPE` pass** (Pass 9: TS `findReferencesAsNodes` per type → `module -[REFERENCES_TYPE]-> type`). Semantic consumers of `BenchmarkModelData` = **4 real** (portal-proxy.ts self-use + BenchmarkHeatmap.tsx + ReturnVolatilityScatter.tsx + ModelPortfolios.tsx):
  - **RECALL: complete** — covers all 3 regex true positives ✓✓✓.
  - **PRECISION: perfect** — **0** of the regex's ~37 false positives (no AdvisorIntelligence noise).
- **Verdict: EQUIVALENCE-OR-BETTER.** Recall == regex true-positives; precision strictly better (kills the substring false-positive flood). Cutover-ready pending CTO's broader-sample confirmation.

## Broader recall sweep (result #3) — 6 types, vs GREP ground truth (not the noisy regex)
`parity_sweep.py` compares the semantic `REFERENCES_TYPE` consumer-file set against `grep -rlwE "<type>" portal/src` (the authoritative by-name reference set — more reliable than parsing comp-types' noisy output). NOTE: a first pass mis-reported a delta because a Windows python-subprocess `grep` returned empty; re-run via the working Bash grep gave the real result below.

| type | grep (real by-name refs) | semantic REFERENCES_TYPE | recall | precision |
|---|---|---|---|---|
| BenchmarkModelData | 4 | 4 | PASS | PASS |
| ModelPortfolioBenchmarksResponse | 1 | 1 | PASS | PASS |
| BenchmarkPeriodReturn | 1 | 1 | PASS | PASS |
| ModelPortfolioData | 1 | 1 | PASS | PASS |
| BenchmarkHeatmapProps | 1 | 1 | PASS | PASS |
| ModelPortfolioPeriodReturn | 1 | 1 | PASS | PASS |

**EXACT PARITY on every sampled type** — semantic == the real by-name reference set (recall complete, precision perfect). Meanwhile the regex `comp-types index` reports 37–44 "consumer sites" per type (e.g. ModelPortfolioBenchmarksResponse: 37 = 1 import + 33 reference + 4 default-fallback; the real answer is 1 file). The semantic re-back is **exactly correct AND 4–37x less noisy**.

## Cutover decision (this increment)
- `comp-types index`: **PARITY MET (better) — recall-complete + precision-perfect across a 6-type ground-truthed sweep.** Recommend cutover pending CTO sign (the broader sweep is done; CTO can widen further if desired).
- `comp-types fields`: **NOT cutover-ready** — recall sweep (result #4) found confirmed recall gaps (FLOWS_TO mappingish-heuristic miss + indexed-access + arbitrary reads). Stays on regex; needs the 3 fixes above on the Leg-C resume. So the comp-types cutover this increment is **INDEX-only** (not the full-tool single sign COO hoped for — `fields` honestly isn't there yet).

## AC4 scale-watch (cost of the precision)
`REFERENCES_TYPE` (findReferences on 796 types) = ~21s; total cold full-portal ~54s (was ~15s). findReferences (language-service) is the cost driver. Acceptable for the nightly derive; CHEAP on incremental (changed-files only re-resolve their types). Queued refinements: scope findReferences to changed types on incremental; the RENDERS getSymbol caching.

## Next (Leg C, unblocked vs blocked)
- UNBLOCKED (done this increment): `REFERENCES_TYPE` pass → comp-types `index` parity MET. Next: broaden the recall sweep across a type sample + the `fields` recall sweep → CTO cutover review for comp-types.
- BLOCKED on AE props fix (in-flight, COO-GO'd): the kind-aware `comp-transform` re-back (ternary-audit / MISSING-UNUSED-with-conditions) + the goal-3 display-logic-bug analyses + AC5 — these need the dropped FLOWS_TO kind/condition.
