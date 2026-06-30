# NFRA_COMPUNIFY grain-thread -- the cross-macro stable-grain contract threaded into the gate (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Current State

Post-arc follow-on (CTO-directed via COO~B, ratified 2026-06-30T20:52Z; scope-guarded 20:57Z). The cross-macro STABLE-GRAIN CONTRACT (CTO amendments 8+9) is now threaded into comp-coverage-map.yaml + enforced as a gate rule. Committed 01af67fcc (B6 live-fired PASS "...grain stable"). COMPUNIFY GOVERNS it, GRAPHUNI (~D) populates to it, COMPDRIFT (COO~B) seams on it -- aligned ONCE so the three never drift.

**Landed in `org/modules/graph/comp-coverage-map.yaml`:**
- `grain_contract` section: the 4 principles verbatim (different relation -> different edge_type; same relation/different grain -> same type + a `level` attr; never split a semantic by depth; node grain = declared attr on a stable CONTAINS ladder) + `node_grain_ladder` (CONTAINS, levels estate..field) + a SEED `edge_types` registry (CONTAINS/READS/READS_S3/WRITES_S3/DEPLOYS/SERVES; each relation -> ONE edge_type + a `levels` attribute). This is where ~D's P1 population adds edge_types/levels (one head).
- `pending_extensions`: the fractal-section-10 model (drilldown seams + rollup consistency) recorded as COMMITTED-NOT-RATIFIED (ref 85129b12f), seam left OPEN, NOT built (per the scope-guard -- build only ratified 8+9).
- `schema.node_fields.granularity` doc'd as the same stable-grain-attribute principle.

**Landed in `org/modules/graph/comp_coverage_check.py`:**
- `stable_grain` gate rule (the 7th): FAILs (a) a relation split across >1 edge_type (per-depth re-typing), (b) an edge_type missing its `levels` attr, (c) a name-encoded grain level. `_check_stable_grain` checker registered in `_CHECKERS`.
- selfcheck injection (e): a relation re-typed by depth -> FAIL. selfcheck now 6/6 green.

**EXTENSIBILITY (scope-guard honored):** the gate is fold-ready BY CONSTRUCTION -- comp-coverage-check enumerates `gate_contract.rules` + dispatches by id, so the pending sec-10 rules fold in as new rule entries + checker fns, NEVER an engine refactor. Did NOT build against the unratified fractal model.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check selfcheck | the gate, now 6 injected-behavior cases | PASS | clean PASS + unplaced/silent-overlap/stale-projection FAIL + no-checker UNVERIFIABLE + the NEW grain-re-typing -> FAIL. All 6 correct. |
| comp-coverage-check check | clean ledger (7 rules incl stable_grain) | PASS | "...projection current, grain stable" -- 6 distinct relations, each one edge_type + levels. |
| comp-coverage-check (B6 live) | fired by safe-commit on the grain-thread commit | PASS | the wiring proved the new rule in the real commit path. |
| ds-commit-gate.sh | comp_coverage_check.py | PASS | py_compile + AST + ruff py39 clean. |

**What worked:** the "gate reads its own contract" design made this a pure FOLD -- adding the stable-grain invariant was one grain_contract section + one rule entry + one checker fn + one selfcheck case, zero engine change. That same property is exactly what makes the pending sec-10 fractal rules a future fold (the scope-guard's requirement, satisfied by construction).
**What failed / gap found:** none -- the seed edge_types were clean-grain on the first pass (each relation distinct, each with a levels domain). The name-encoding heuristic correctly does NOT false-flag READS_S3 vs READS ('s3' is not a grain-ladder level -- it's a genuinely different relation, ruling 4).

## MCP Traffic

3 dispatches. Significant: COO~B grain-thread dispatch (CTO-directed) + COO~B scope-guard (build 8+9, design extensible for sec-10, fold-not-refactor); my RAVC2 -> COO~B (cc CTO + ~D) on the 8+9 thread.

## Blockers

**None.** The grain-thread is complete + gate-enforced + selfcheck-proven. The sec-10 fractal fold is a future task (CTO ratifies -> COO~B brings me the drilldown/rollup rules -> they fold in). No open handoff on this thread.

## Next Steps

1. **[0.8.0_AE_CloudComp~D]** populate edge_types/levels into grain_contract against the contract; `comp-coverage-check check` PASS = grain-stable; a re-type-by-depth FAILs B6 at commit.
2. **[1.0.0_SA_CTO]** (arch-awareness) the 8+9 reconciliation is now a gate rule; when you ratify sec-10, its drilldown/rollup rules fold in (no engine refactor).
3. **[2.0.0_SA_COO~B]** COMPDRIFT seams on grain_contract edge-grain stability; bring me the sec-10 rules on ratify.
4. **[0.8.0_AE_CloudComp~C]** grain-thread complete. Still holding NFRA_COMPUNIFY V1 (CVO) + the manifest regen (COO~B) from the S0->S3 arc. Event-driven; available for the sec-10 fold or any new dispatch. No cron.
