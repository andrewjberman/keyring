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
- `comp-types fields`: semantic better on precision; **stay on regex until a recall sweep** confirms no true-positive is missed across the field set, then cut over (CTO sign).

## AC4 scale-watch (cost of the precision)
`REFERENCES_TYPE` (findReferences on 796 types) = ~21s; total cold full-portal ~54s (was ~15s). findReferences (language-service) is the cost driver. Acceptable for the nightly derive; CHEAP on incremental (changed-files only re-resolve their types). Queued refinements: scope findReferences to changed types on incremental; the RENDERS getSymbol caching.

## Next (Leg C, unblocked vs blocked)
- UNBLOCKED (done this increment): `REFERENCES_TYPE` pass → comp-types `index` parity MET. Next: broaden the recall sweep across a type sample + the `fields` recall sweep → CTO cutover review for comp-types.
- BLOCKED on AE props fix (in-flight, COO-GO'd): the kind-aware `comp-transform` re-back (ternary-audit / MISSING-UNUSED-with-conditions) + the goal-3 display-logic-bug analyses + AC5 — these need the dropped FLOWS_TO kind/condition.
