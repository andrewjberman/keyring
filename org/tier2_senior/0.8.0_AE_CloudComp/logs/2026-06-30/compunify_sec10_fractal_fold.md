# NFRA_COMPUNIFY sec-10 fractal fold -- drilldown + existential-rollup gate rules (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

The §10 fractal-granularity model (CTO-ratified 205709Z) is FOLDED ACTIVE into the COMPUNIFY grain gate. Commit 28fac26f2 (B6 live-fired PASS). A pure FOLD per the gate-ready-by-construction design -- zero engine refactor.

**Conflict reconciled first (recorded -- good discipline):** COO~B said HOLD (the fractal-fold + calibration as a dedicated phase, mandate-first LD-0229); CTO (11s later) dispatched the gate-rule fold DIRECTLY with the complete spec + explicitly lifted COO~B's scope-guard. I split it: the GATE-RULE FOLD has no mandate-first dependency (it enforces, doesn't calibrate; fires only on ~D's population) -> proceed per CTO; the TOOL-CALIBRATION sweep calibrates against ~D's grain ladder -> HOLD per COO~B (mandate-first). Sent COO~B the reconciliation + halt-option BEFORE going deep; COO~B CONFIRMED ("your split is exactly right, no halt"; CTO owns the gate-contract enforcement lane, COO~B owns the calibration-phase decomposition).

**Landed in `grain_contract` (comp-coverage-map.yaml):**
- `strata: [resource, compute, object]` (coarse->fine) + `drilldown_seams` (RUNS resource->compute / CONTAINS compute->object / OWNED_BY object->resource), each a stable typed stratum-stitcher referencing edge_types. RUNS + OWNED_BY added to the edge_types registry; CONTAINS reused (same relation, finer level -- not re-typed).
- `rollup`: EXISTENTIAL-aggregation (CTO 047ce51d0, grounded from the commit -- NOT 1:1 equality): a coarse edge EXISTS iff >=1 fine edge rolls up (OR-rollup); defect classes UNSUPPORTED (coarse, zero fine basis) + COARSE-INCOMPLETE (fine, coarse target absent).
- `pending_extensions: []` (sec-10 folded; none pending).

**Landed in `comp_coverage_check.py`:**
- `grain_drilldown_seams` (gate rule 8) + `grain_rollup_consistency` (gate rule 9) + their checker fns, registered in `_CHECKERS`. Empty-fractal = PASS (gate-ready-ahead-of-need).
- `rollup_defects(coarse_edges, fine_edges, rolls_up)` -- THE CANONICAL existential-rollup, exposed as the ONE head GRAPHUNI-derive + COMPDRIFT-seam import + call against populated edge INSTANCES (so the 1:1-vs-existential drift 047ce51d0 corrected cannot recur).
- selfcheck now 9/9.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check selfcheck | the gate, now 9 cases | PASS | original 6 + bad-drilldown-stratum->FAIL + 1:1-rollup-semantics->FAIL + rollup_defects existential logic (UNSUPPORTED + COARSE-INCOMPLETE + supported-clean). |
| comp-coverage-check check | clean ledger (9 rules) | PASS | drilldown_seams + rollup well-declared; RUNS/CONTAINS/OWNED_BY all in edge_types. |
| comp-coverage-check (B6 live) | fired on the fold commit | PASS | the 2 new rules proven in the real commit path. |
| (git show) 047ce51d0 | grounded the EXISTENTIAL rollup semantics | -- | pulled the EXACT form (coarse iff >=1 fine; UNSUPPORTED + COARSE-INCOMPLETE) per CTO's "don't false-flag OR-rollups" -- mechanism grounded from source, not invented (CLAUDE.md Rule 22). |
| ds-commit-gate.sh | comp_coverage_check.py | PASS | py_compile + AST + ruff py39 clean (fixed an (h) dict key/value-order bug pre-commit). |

**What worked:** the enumerate-and-dispatch gate engine made §10 a literal FOLD -- two grain_contract sub-sections + two rule entries + two checker fns + one shared rollup_defects(), zero engine change (the extensibility I designed for in the 8+9 thread paid off exactly as intended). Grounding the existential semantics from 047ce51d0 (not my interpretation) made rollup_defects correct on the OR-rollup boundary.
**What failed / gap found:** caught my own (h)-selfcheck bug pre-commit (the rollup_defects test mapped class->edge but looked up by edge; fixed the comprehension order). The reusable rollup_defects() is the anti-drift move -- without it, GRAPHUNI + COMPDRIFT would each re-implement the rollup and could re-introduce the 1:1 error 047ce51d0 just fixed.

## MCP Traffic

~7 dispatches. Significant: COO~B grain-thread verify (selfcheck 6/6) + the HOLD; CTO §10 ratify + direct fold dispatch (full spec, guard lift); ~D ACK (population conformance) + the §10-ratified sync; my reconciliation -> COO~B (halt-option); COO~B CONFIRM (no halt, split correct, lane note); RAVC2 fold -> COO~B cc CTO + ~D (rollup_defects one-head).

## Blockers

**None.** The §10 gate-rule fold is complete + selfcheck-proven. HELD (not blocked) for COO~B: the tool-calibration-sweep phase decomposition (mandate-first, after ~D's grain-ladder arch-gate). HELD for CVO: NFRA_COMPUNIFY V1.

## Next Steps

1. **[0.8.0_AE_CloudComp~D]** populate fractal edges against grain_contract; import + call `rollup_defects()` for the existential rollup (one head). `comp-coverage-check check`/`selfcheck` before commit.
2. **[2.0.0_SA_COO~B]** COMPDRIFT seam calls the same `rollup_defects()`; dispatch the tool-calibration-sweep phase to me once ~D's grain ladder is CTO-arch-gated.
3. **[3.0.0_SA_CVO]** NFRA_COMPUNIFY V1 (the standing acceptance) + manifest regen (COO~B) from the S0->S3 arc still open.
4. **[0.8.0_AE_CloudComp~C]** sec-10 fold complete. Holding the tool-calibration phase + V1. Event-driven; available immediately. No cron.
