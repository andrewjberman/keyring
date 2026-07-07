# Session — NFRA_CSE.P1 build (the SEMCTL unblocker): semantic-algebra + CSE contract + fail-closed validator — lane B

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**TO:** NFRA_CSE.P1 (COO-dispatched, the SEMCTL critical-path unblocker)
**Window:** ~0946Z -> ~1140Z 2026-07-07
**Commits:** 1389aafab, 4fd19de39, f98d4ff77 (build); COO landed the canonical.

## Summary
Built the authoritative Canonical Semantic Event contract + versioned semantic algebra + fail-closed validator for the Semantic Control Plane (NFRA_SEMCTL). CSE-P1 is THE unblocker: FEDOBS + COMPILERKIT read this contract; nothing federated works without it. DONE + landed canonical; both peer gates PASSED.

## What was built (org/modules/graph/cse_schema.py, canonical; built in DS deliverables lane then COO-landed via SoD)
Against CTO's authoritative algebra-design v0.1 (NFRA_CSE_algebra_schema_v0.1.md, 63b3b9015) -- unify-not-build:
- VERSIONED ALGEBRA (schema_version 0.1): 4 governed-extensible enums -- Entity(27: org + concrete infra Lambda/S3Bucket/IAMRole/IAMStatement/Schedule/SecretRef/ReactComponent/JSXElement/Hook/GraphScope/Tool/Tier), Relationship(23), Transformation(10), Qualifier(8). Add-a-primitive = version-bump + coverage-sweep.
- CSE CONTRACT (S2): producer/compiler/transformation/qualifiers/MANDATORY-provenance/execution_meta + head.marker_head (AC6 -- pins the GLOBGRPH marker-HEAD at emission).
- FAIL-CLOSED VALIDATOR (LAW-1 teeth): off-enum REJECT-not-coerce; provenance-evidence mandatory (LAW 2); confidence float[0,1] mandatory; Concept(untyped) ONLY valid with confidence<=0.34 (LOW_CONFIDENCE_MAX) -- an inferred type on a low subject = the GraphRAG failure the validator blocks; fidelity (comp_ladder decompress or invalid).
- AC3 DUAL-VOCAB MAPPING: node_type (all 52 live) + nid-prefix (s3:/component:/field:/stmt:/...) -> Entity; edge_type (all 52 live) -> Relationship. Fail-closed on any gap (mirrors NODE_TYPE_LAYER_GAP).
- AC5 FIDELITY BIND: to_ladder_node()+cse_fidelity_ok() REUSE comp_ladder.fidelity_check (imported, not re-authored).
- AC4 mapping-totality-vs-LIVE (assert_live_coverage, snapshot + --live fresh-pull) + AC1 coverage_sweep (COMPUNIFY wire flagged P2) + confidence_band()/inference_smell() (CTO guidance: mid-band typed = soft-inference smell).
- S6 STORE (0.5.0_AE consult 28cf707f9): emit-vs-commit split, partition=(source,event_date), one-marker-commit (C0/C1 version-consistency = AC6 free), firm-scope-via-qualifier, graph_contracts registry id.
- RUNNABLE self-test (__main__): 10/10, re-runnable (CTO condition a).

## Two grounding catches (the session's through-line, banked fabric-wide)
1. AC4 LIVE-INVENTORY CATCH: CTO's condition "verify totality vs the LIVE distinct types, NOT your hardcoded count" caught a REAL gap -- I'd mapped ~24 of the graph's 52 live edge_types. Pulled the actual comp-kuzu inventory -> completed all 52+52 (defensible many-to-one C0->C1 compression). 28 unmapped edge_types prevented from shipping silently-incomplete.
2. CVO HYGIENE FINDING (self-applied): my --live mode SILENTLY fell back to the snapshot on pull-failure -- the honest-missing-never-silent-default invariant violated on the validator's OWN live-check. Fixed: comp-kuzu --json + JSON parse + FAIL-LOUD (LivePullError), --live now genuinely pulls 52+52 or errors. (Ties to the same session's DI-7 account_type false-premise catch -- ground against reality, not a name/count/default.)

## Gates
- CTO arch-gate: PASS (design-conformance verified at source; CTO INDEPENDENTLY re-ran the self-test 10/10). 3 reconciliation rulings applied (float+0.34+inference-smell; mapping-totality=P1/round-trip=P2; local-sweep=P1/COMPUNIFY=P2).
- CVO exercise-cert: PASS (re-ran + 8/8 CVO-own adversarials incl. the subtler Concept+mid-band(0.5) smuggled guess; independently pulled live 52+52 -> 0 unmapped). + the hygiene finding (fixed).
- COO canonical land: DONE (COO diff-verified vs source, caught a stale first-land, re-landed the hygiene-fixed f98d4ff77; canonical == source confirmed).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-kuzu | CloudNode/CloudEdge DISTINCT node_type/edge_type | PASS | the LIVE AC4 ground-truth (52+52); the catch that surfaced the 24-vs-52 edge gap |
| comp-kuzu | table_info/show_tables | PASS | found node_type is a CloudNode property (not a Kuzu label) |
| comp-grep/comp-glob | NODE_TYPE_LAYER, kuzu_cli.py, CloudNode types | PASS | located the reference vocab + the wrapper's underlying CLI |
| ds-commit-gate | cse_schema.py (each rev) | PASS | py_compile+AST+ruff clean (fixed E702 one-liners + F401) |
| python <file> | runnable self-test | PASS | 10/10 default + --live genuine-pull |

**What worked:** comp-kuzu --json was the decisive AC4 tool (pulled the real live inventory; its structured output enabled the hygiene fix). comp_ladder reuse made AC5 a runnable bind, not a re-author.
**What failed:** bare `comp-kuzu`/`aws` subprocess from Python on Windows (WinError 2 -- it's a bash wrapper); resolved by invoking via `bash .tools/comp-kuzu`.
**Gap found:** none new (the two grounding catches were caught + fixed, not gaps left).

## Blockers
None. CSE-P1 DONE + landed.

## Current State
- org/modules/graph/cse_schema.py = the authoritative CSE contract + algebra (schema_version 0.1), canonical (COO-landed, == my source f98d4ff77). Runnable self-test 10/10. FEDOBS||COMPILERKIT read it now (unblocked).
- The validator enforces LAW 1 (reject-not-coerce, honest-low-not-guess) + LAW 2 (provenance-mandatory, comp_ladder decompress) as runnable gates.

## Next Steps
1. **[0.5.0_AE_OpalETL]** P2 store-landing writer on the Item-2b (CloudTrail->EventBridge->Lambda->Nessie-commit) pattern against the published contract (partition cols + emit-vs-commit split + one-marker-commit are pinned in the schema).
2. **[NFRA_FEDOBS / NFRA_COMPILERKIT owners]** start against the published contract (parallel, no P2/P3 dependency).
3. **[0.4.0_DS_ClientPlatform~B / P2]** the AC4 structural round-trip diff (re-materialize mapped CSEs -> diff vs live Kuzu) = the P2 materializer's CVO-cert; the COMPUNIFY machine-checked coverage-wire = P2 reuse-more.
