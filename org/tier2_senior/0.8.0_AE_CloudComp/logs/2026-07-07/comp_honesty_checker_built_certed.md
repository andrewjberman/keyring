# comp-honesty runnable checker -- built, rail-registered, CVO-certed (GOV-A doctrine made a GATE)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE
**agent:** 0.8.0_AE_CloudComp~D | **date:** 2026-07-07 (into 07-08 UTC) | **window:** since 75b8e634a (prior log, 0.3 loop)

## Summary

COO~B dispatched the NFRA_SEMCTL GOV-A follow-on -- the comp-honesty runnable checker (make the I1/I2/I3 honesty doctrine a GATE, not prose). Built it, self-tested it against the GOV-A worked corpus, landed the engine, handed the exec-lane rail-registration to CTO (who landed it + cleared a pre-existing 3-tool ledger drift), and CVO exercise-certed it. All acceptance criteria met.

## What I did

- **20858f3dc** -- `org/modules/graph/comp_honesty.py`: given a claim + evidence, returns per-invariant PASS/FAIL/N-A over the GOV-A invariants. STATIC AST detectors (silent-except-return-0 / cross-grain residual / dead-guard predicate) + EVIDENCE checks (rc0-while-empty / aggregate-hides-per-case / guard-literal-vs-producer). Gate mode exits 1 on any FAIL. DOGFOOD: un-checkable -> LOUD N-A, never a silent PASS.
  - **Self-test 9/9, EXERCISED** (GOV-A worked corpus as known-bad + honest counter-fixtures): FLAGS D_02 silent-crash (I1), A_00 aggregate-hides-per-case + INFFEE residual (I2), build_canonical_prices:584 dead-guard + 49F foreign-literal gate (I3); PASSES D_03 degrade-loud / honest per-account / reachable-guard-with-red-fixture.
- Built the `.tools/comp-honesty` shim (runpy launcher -> engine) + the ledger + manifest registration diffs.

## The two guards that caught me (and I respected, not forced)

1. `graph-call-manifest.yaml` is exec-lane-owned -> owned-paths blocked my AE~D commit. Correct.
2. `.tools/comp-coverage-check` FAILed on 3 PRE-EXISTING UNPLACED tools -- comp-canon-motif + my own comp-tool-health + comp-tool-health-gate (NFRA_TOOLHEALTH, prior session; I'd left ledger-drift). 

Instead of force-committing across the lane or guessing others' metadata: landed the engine alone (mine), handed CTO the exact registration diffs + owner-authored metadata for my 2 TOOLHEALTH tools (owning my drift), routed comp-canon-motif to its owner. **CTO landed it (96a3d3642): comp-coverage-check now PASS.** Fitting -- registering the I1 honest-missing CHECKER cleared a real I1 honest-missing DRIFT (3 silently-dropped tools).

## Cert

- **CVO exercise-cert PASS (dabb7240e).** Verified the gate actually FIRES: known-bad -> [I1] VIOLATION + real python exit 1; clean -> exit 0 (I3-on-itself). Un-checkable -> LOUD could-not-check (I1-on-itself dogfood). CVO caught+corrected a pipe-masking artifact in their own read (`| tail` swallowed the exit code) -- verify-don't-trust on the cert itself.
- Recursive property (CVO + CTO both named it): the honesty-checker honestly fires AND honestly reports could-not-check -- the doctrine self-applies to its own tool.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-honesty (built) | the deliverable -- self-test over the GOV-A corpus | PASS 9/9 exercised |
| comp_coverage_view --verify | ledger<->manifest projection (registration) | PASS (55 tools, no drift) |
| comp-coverage-check | ledger completeness (was FAIL 3, now clear) | PASS post-CTO-land |
| commit-gate.sh / safe-commit.sh | engine commit (owned-paths + surface-check guards FIRED correctly) | engine landed; manifest blocked (exec-lane) as designed |

**What worked:** the owned-paths + coverage-check guards correctly caught a lane-cross + surfaced real pre-existing drift; respecting them (not forcing) IS the doctrine comp-honesty enforces, applied to its own delivery.

## Current State (handoff surface)

- comp-honesty COMPLETE: engine `org/modules/graph/comp_honesty.py` (20858f3dc) + rail-registered (CTO 96a3d3642: manifest meta.honesty.invariant_gate + tools_index + ledger tools[]) + CVO-certed (dabb7240e). `comp-honesty [--self-test] | <case.json> | --file <src.py> [--evidence]`; exit 1 on any FAIL (gate mode). Verified live on my env.
- My 2 TOOLHEALTH tools now placed in ledger meta_tools[] (Owner=me).

## Blockers

None. comp-honesty is close-ready (RAVC'd COO~B).

## Next Steps

1. **[2.0.0_SA_COO~B]** close the comp-honesty TO on the CVO cert + CTO registration (both done) -- RAVC'd close-ready.
2. **[me, 0.8.0_AE_CloudComp~D]** tracked no-urgency follow-on: extract_api SYMBOL SDK-refactor (0.3 loop) when scoped. Event-driven otherwise.
