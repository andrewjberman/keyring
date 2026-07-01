# CVO~B GRAPHDEPTH P3 cert (depth-scoped tooling) -- GREEN

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0551-0555Z
**Trigger:** ~C landed GRAPHDEPTH.P3 comp-depth (3e8d457a9 + drilldown-derive 08dc06ebe); COO~B close-gate 2. Reads full() (the unified marker-head estate) DIRECTLY -- independent of the GRAPHUNI P2 trace-graph re-point fork.
**Grounded** by independently exercising comp-depth on the live marker-head (head 5434137157015633165), not ~C's self-report.

## VERDICT: **GREEN** -- depth-scoped tooling is grain-correct, size-invariant, provenance-current, on the ONE head. Close GRAPHDEPTH.

## SIZE-INVARIANT depth x breadth (the P3 acceptance) = CONFIRMED
The SAME `comp-depth blast gold:D_02.advisor_client_detail:main`, breadth-reachable CONSTANT at 826, scoped by `--grain` to 3 DISTINCT correct subsets:
- `--grain function` -> **575** of 826 reachable
- `--grain object`   -> **175** of 826 reachable
- `--grain resource` -> **4**   of 826 reachable
ONE tool, ONE `--grain` arg, NO per-grain type fork (the anti-pattern GRAPHDEPTH exists to prevent). The 3 grain-subsets are disjoint slices of the breadth-reachable (575+175+4=754 of 826 are fn/obj/res-grain; the other 72 are other grains) -- correct scoping, not a re-typing.

## D4 provenance-EVERY-CALL = CONFIRMED
Every comp-depth invocation prints `[marker-head: current | head=5434137157015633165]` -- the D4 one-head oracle fires per-call, so a depth query can never silently read a stale/divergent vintage (the exact anti-drift guarantee; head == the Phase-B marker I verified at landing).

## Grain CORRECTNESS = CONFIRMED
- 52/52 node_type_grain bridge match (my prior read-handle grain co-verify was GREEN; re-confirmed by the correct differentiation above -- functions land at function-grain, objects at object-grain, resources at resource-grain).
- Drilldown DERIVED from grain_contract.drilldown_seams + strata (08dc06ebe), not hardcoded -> no future-stratum drift (a new stratum extends the contract, not the tool).
- Rollup delegates to the shared comp_coverage_check.rollup_defects (existential-aggregation, the one canonical definition -- no divergent rollup semantics).

## Scope (honest)
Size-invariance confirmed on the P3 acceptance target (D_02.advisor_client_detail:main); the property (grain-scoping differentiates, one-tool-no-fork) is demonstrated + provenance-current is universal per-call. GRAPHDEPTH depth-scoping reads full() directly, so it is UNAFFECTED by the GRAPHUNI (b) re-point fork (which concerns the trace-graph breadth tools comp-blast/trace/xref).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_depth_cli.py blast --grain {function,object,resource}` | independent size-invariant grain-scoping on the marker head | PASS -- 575/175/4 distinct correct subsets, breadth 826 constant, no type fork |
| comp-depth provenance header (per call) | D4 one-head oracle | PASS -- current, head=5434137157015633165 every call |
| comp-kuzu (EC2 id fetch for drill) | ground the drill target | PASS -- (a random EC2 with no RUNS drills to 0 functions = correct, not a defect) |

What worked: the 3-grain differentiation on ONE target with a CONSTANT breadth (826) is the clean proof of size-invariant depth x breadth -- one tool + a `--grain` attribute, never a per-depth type fork (the stable-grain contract enforced end-to-end). Provenance-every-call structurally prevents a stale-vintage depth read.

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN -> 2-step close GRAPHDEPTH.
2. **[3.0.0_SA_CVO~B]** GRAPHUNI (b) per-tool re-point gate remains (fixture-bar (b)-PASS already delivered; I gate ~D's per-tool head-pinned re-point vs fresh-build_graph + D4 one-head). (a) true-unification coverage-equivalence proof = the tracked finish I own.

-- 3.0.0_SA_CVO
