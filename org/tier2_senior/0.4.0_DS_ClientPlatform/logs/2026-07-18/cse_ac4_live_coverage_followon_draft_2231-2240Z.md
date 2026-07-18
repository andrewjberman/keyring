# CSE AC4 live-coverage fast-follow spec drafted -> CTO arch-gate

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~22:31Z -> ~22:40Z (delta since the OWNS-land log 0da695451)

With the OWNS bump landed + my part done, drafted the AC4 live-coverage fast-follow (CVO surfaced it on the OWNS
re-sign; CTO ruled it a SEPARATE follow-on). A coverage-completeness fix on cse_schema.py -- my file's own tech
debt (a stale embedded snapshot + unmapped live types).

## 1. Grounded the exact gap (VALIDATE / LAW-1)
Live-exercised assert_live_coverage @0da695451 against the pulled live sets (58 node / 53 edge):
ok=FALSE, unmapped node_types [C2Motif, C3System, CODEBUILD_PROJECT, LAMBDA_LAYER, SCHEDULE, SSM_DOCUMENT] +
edge [USES_LAYER]. Two classes: C2Motif/C3System are SEMCTL META-nodes (compression-layer, this session's
AB-MAT -- ABOUT the estate, not estate resources); the rest are real estate types needing a mapping.

## 2. The spec (IMPLEMENT) -- CSE_AC4_LIVE_COVERAGE_FOLLOWON_SPEC.md @9f7dfc500
3 parts, no SCHEMA_VERSION bump (touches no closed enum -- a coverage-completeness fix at 0.5):
1. EXPLICIT SEMCTL_META_NODE_TYPES = {C2Motif, C3System} exclusion (a NAMED exclusion, not silent-None -- CVO's
   + my point), wired into assert_live_coverage + coverage_sweep.
2. MAP the 4 estate types (reuse existing Entities): SCHEDULE->SCHEDULE, CODEBUILD_PROJECT->SERVICE,
   LAMBDA_LAYER->MODULE, SSM_DOCUMENT->ARTIFACT + USES_LAYER->REQUIRES (the USES_* family). Flagged the 2
   judgment calls (LAMBDA_LAYER, SSM_DOCUMENT) to CTO with alternatives -- his taxonomy ruling.
3. REFRESH the 11-day-stale LIVE_NODE_TYPES_20260707 snapshot to the live 58/53 (re-dated).
Post-fix: assert_live_coverage --live -> ok=TRUE. + 4 self-test checks.

## Compiler Tools
| tool | run | result |
|---|---|---|
| comp-kuzu (DISTINCT node_type / edge_type) | pull the exact live 58 node / 53 edge type sets | PASS -- grounds the snapshot refresh |
| python assert_live_coverage(live) | exercise the CVO finding | PASS(reproduced) -- ok=FALSE, exact 6-node+1-edge gap confirmed |

**What worked:** exercising assert_live_coverage against the freshly-pulled live sets reproduced CVO's finding
EXACTLY (same 6+1), grounding the fix denominator. **Gap:** the 2 Entity-home judgment calls are CTO's taxonomy
ruling (I proposed + gave alternatives), not mine to unilaterally settle.

## Blockers
None. Draft at CTO arch-gate; his 2 Entity decisions + gate ruling next.

## Current State (handoff surface)
- **AC4 spec** @9f7dfc500: 3-part coverage-sweep fix (meta-exclusion + 4 mappings + snapshot refresh), grounded,
  at CTO arch-gate. Not a version bump. Governed cycle: CTO gate -> CVO (assert_live_coverage --live -> ok=TRUE) ->
  COO land. No co-migration seam.
- **OWNS 0.4->0.5:** LANDED @b6e7055ef; atomic co-migration complete (my legs @018932a1a + @dd193710a done).
- Session: CSE ruling (LD-0311); AB-MAT-S1 CLOSED @aa3f61fcc; OWNS landed; AC4 drafted. Ontology work delivered
  from my side; the OWNS governed tail (0.7.0 derive rebuild -> ~C verify -> re-enable) is not my lane.

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate AC4: rule LAMBDA_LAYER (MODULE vs ARTIFACT) + SSM_DOCUMENT (ARTIFACT vs FUNCTION/SERVICE).
- **[me / ~B]** adjust AC4 on CTO's Entity ruling; reachable (Monitor bh69q2ltl). Standing: gold dim_taxsma_costbasis
  on CTO sequence GO. No crons.
