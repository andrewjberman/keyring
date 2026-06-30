# NFRA_GRAPHDEPTH — Decomposition / Cross-Tag MAP (the coordinating spine, NOT a parallel build)

**By:** 2.0.0_SA_COO~B (NFRA_COMP* program coordination) | **From:** CTO PRD docs/architecture/NFRA_GRAPHDEPTH_PRD.md (16ba4ae7d) + LD-0229/LD-0230
**For:** CTO RAVC before any dispatch. **Priority:** FOUNDATIONAL, sequence behind the ADVI_BREAKS firefight.

> CTO directive (explicit): GRAPHDEPTH is the **foundational-layer framing + the constitutional contract** that the in-flight GRAPHUNI(populate)/COMPUNIFY(govern)/tool(calibrate) work ALREADY serves. Decompose it as the COORDINATING SPINE over that work — **cross-tag, do NOT rebuild** (a parallel build would drift the program on the very depth axis this exists to unify). Only **P3 is net-new.**

## PRECEDENCE (CTO override 210952Z, Andrew-direct -- SUPERSEDES the "sequence behind / formalization" framing)
**NFRA_GRAPHDEPTH is #1 in the 0.8.0 comp-program queue.** It takes precedence over ALL other comp-program PRDs -- COMPDRIFT, COMPLEARN, and any further COMPUNIFY deepening -- because it is the FOUNDATIONAL LAYER they sit on: COMPUNIFY governs the grain schema THIS defines; COMPDRIFT's drift topology needs the depth coordinate to scope per-grain; COMPLEARN scores tools that must know their grain. None can be correctly built under an undefined depth axis. So **COMPDRIFT + COMPLEARN decomposition WAIT on GRAPHDEPTH** (this hard-gates my prior cap-pacing of them -- now a foundational dependency, not just capacity).
- **Scope of the precedence:** WITHIN the 0.8.0 comp-program lane only. The live ADVI_BREAKS/INFREF firefight (0.6.x/0.4.x/CVO lane) remains Andrew's standing operational P0, UNAFFECTED. GRAPHDEPTH becomes the **top CLAIM on CVO's fixture-attention the moment the firefight frees it** -- ahead of COMPUNIFY V1 / other comp-verifies.

## THE ~C / ~D WORK DIVISION (Andrew-direct, the populate/govern split formalized)
- **~D = SUBSTRATE POPULATION (the graph side):** derive + populate the depth ladders into the one head-pinned graph -- CONTAINS/OWNED_BY/RUNS drilldown + cross-stratum edges, `level` attributes, the fractal strata (Pipeline->Script->Function; Bucket->Key; EC2-RUNS->PipelineScript). Gold-tier-first (no-regression-critical), bronze/silver/ingestion net-new enriching, bounded materialization at fine grain. IS the GRAPHUNI P1 build on the depth axis -- one build, CVO-fixture-gated.
- **~C = SCHEMA GOVERNANCE + CALIBRATION (the map side):** own the grain_contract + the comp-coverage-check gate rules (7 stable_grain landed; 8/9 drilldown-seam + rollup-consistency folding now) + the tool depth-calibration (COMPUNIFY S4). ~C DEFINES + GATES the contract; ~D POPULATES against it; ~C's gate FAILs any ~D commit that re-types by depth or breaks a rollup.
- **THE SEAM (coupled by the contract, NOT racing):** ~C governs the edge_types registry + invariants; ~D's commit-time check IS ~C's gate. ONE shared grain schema, authored once (~C governs / ~D populates / COMPDRIFT carries the rollup seam) -- the one-taxonomy discipline.

## SYMBIOTIC /seams VALIDATION + the COMPREHENSIVE-BASELINE GATE (Andrew-direct 211250Z/211324Z -- load-bearing)
The govern<->populate seam is where the baseline's robustness is won or lost. Andrew-direct: ~C + ~D do NOT merely contract-couple (one-way gate) -- they actively **/seams the overlap TOGETHER, validating IN UNISON** (both sign the seam; a red seam STOPS + reconciles, never proceeds).
- **THE SEAM:** ~C's grain_contract edge_types registry + invariants <-> ~D's populated edges + `level` attrs + cross-stratum seams. 3-axis /seams: (1) MECHANICAL (the gate fires on the real populated edges; a re-type-by-depth is caught), (2) DECLARATIVE (the registry matches what is ACTUALLY populated -- no map-vs-territory drift either direction), (3) SEMANTIC (existential rollup-consistency holds on REAL edges; zero UNSUPPORTED/COARSE-INCOMPLETE).
- **CATEGORICAL / COMPREHENSIVE BAR (Andrew-direct):** the substrate must be COMPREHENSIVE + categorically dialed-in. The /seams validation must CATEGORICALLY cover EVERY stratum (compute/storage/infra + the infra<->compute cross-stratum seam), EVERY edge_type in the registry, EVERY populated grain `level`, EVERY cross-stratum drilldown. Spot-checks are insufficient.
- **THE GATE ON THE REST OF THE COMP LAYER (Andrew-direct "only once that is done can we proceed"):** COMPDRIFT + COMPLEARN + further-COMPUNIFY do NOT proceed until GRAPHDEPTH's substrate is COMPREHENSIVELY /seams-validated robust. COO~B HOLDS this gate. Cadence: populators + ~C /seams each population increment categorically before the next tier; verdicts -> COO~B.
- **CTO SHARPENING 1 -- ENUMERATED DENOMINATOR (makes "comprehensive" PROVABLE):** "every stratum/edge-type/grain/cross-stratum seam" must be an ENUMERABLE set, derived up-front from the grain_contract (edge_types registry + CONTAINS ladder) + the D1 derive spec = the full EXPECTED (stratum x edge-type x cross-stratum-seam) set that SHOULD exist. The /seams asserts coverage of ALL of it; an uncovered EXPECTED seam = NOT-GREEN (no-silent-caps applied to the validation itself: report covered-vs-expected). ~D's D1 audit + the ~A/~B stratum audits ARE the denominator -- point the /seams at it. RAVC to CTO before the /seams run.
- **CTO SHARPENING 2 -- CVO INDEPENDENT VERIFY on the gate-lift (NEVER#5):** producers' both-sign = PRODUCER attestation. The lift to COMPDRIFT/COMPLEARN requires CVO to INDEPENDENTLY confirm (a) the 3-axis /seams pass AND (b) coverage == the enumerated denominator (no silent gap). GATE-LIFT CONDITION = producers both-sign comprehensive /seams-GREEN AND CVO independent verify. COO~B holds the gate; CVO is the independent confirmer.
- **P3 = the END-TO-END INTEGRATION TEST (CTO note):** the cross-stratum trace (comp-blast script->EC2-runner->served) resolving correctly IS the capability proof the ladders+seams+rollup work in practice, not just in the gate.

## FLEET PARALLELIZATION (Andrew-direct -- ~A + ~B instantiated to parallelize the substrate)
The population (P1) is the parallelizable bulk; GOVERNANCE stays single (one schema, one governor -- splitting it fragments the taxonomy this exists to unify). Partition the population BY STRATUM (maps to the PRD §5 fractal strata), each populator owning one stratum's ladder + edge-types, all symbiotically /seams'd against ~C's ONE contract:

| Lane | Role | Scope | Sequence |
|---|---|---|---|
| **~C** | GOVERN (single) + CALIBRATION | the grain_contract + comp-coverage-check gate (rules 7/8/9, 9/9) + COMPUNIFY S4; the symbiotic /seams partner for EVERY populator; co-produces the enumerated denominator | throughout |
| **~D** | POPULATE -- COMPUTE stratum | Pipeline⊃Script⊃Function (CONTAINS) + CALLS + gold READS_S3/WRITES_S3. GOLD-FIRST = the no-regression D2 baseline (critical spine), then bronze/silver/ingestion compute enrichment | Phase A foundation (CVO-fixture-gated) -> Phase B enrich |
| **~A** | POPULATE -- STORAGE stratum | S3_BUCKET⊃S3Key⊃object (OWNED_BY/CONTAINS) -- the key-level S3 the compute IO points at. Coupled to ~D's gold IO (gold READS_S3 -> S3Key) -- they /seams that coupling | gold-tier keys with Phase A (coupled to ~D) -> deeper grain Phase B |
| **~B** | POPULATE -- INFRA + CROSS-STRATUM | EC2/Lambda (exist) + the NET-NEW stitchers EC2-RUNS->PipelineScript + LAMBDA-CONTAINS->handler (fuse infra<->compute islands). DEPENDS on ~D's compute (PipelineScript nodes must exist) | Phase B (after ~D gold-compute lands) |

**Sequencing:** Phase A (foundation, CVO-fixture-gated) = ~D gold-compute + ~A gold-tier storage keys (coupled, /seams'd) = the no-regression baseline. Phase B (parallel enrichment, after Phase A /seams-GREEN) = ~D compute-enrich + ~A storage-deepen + ~B infra cross-stratum seams; all per-increment symbiotically /seams'd against ~C.
**AUDIT-FIRST (mandate-first-OK, read-only, parallel):** on ~A/~B going live + my issued mandate, each runs a READ-ONLY stratum audit (storage / infra+cross-stratum -- like ~D's P0 D1 audit) -> contributes its slice of the ENUMERATED DENOMINATOR while the gold foundation lands. No graph mutation; parallel-safe with the firefight.
**Mandate-first + CTO-concur:** the ~A/~B parallelization is a P1-population partition refinement -> RAVC CTO before dispatch; ~A/~B work from COO~B's issued mandate (the audit TO, then Phase B), never pre-emption.

## The depth axis = the 2nd coordinate
Every investigation needs `(BREADTH, DEPTH)`: BREADTH = COMPUNIFY surfaces (where on the surface); DEPTH = this layer (what grain). The substrate is breadth-aware but depth-flat today. GRAPHDEPTH = granularity as a declared `level` on a stable CONTAINS ladder, scale-invariant type system. 4 invariants + 3 boundary conditions + 5 rulings (PRD §4/§9).

## PHASE -> WORK MAP (cross-tags; sources are authoritative, not re-authored here)

| GRAPHDEPTH phase | What | Status | CROSS-TAGGED TO (the real work — do NOT duplicate) | Lane |
|---|---|---|---|---|
| **P0 — depth contract + gate** | `level` schema + stable CONTAINS ladder + edge_types registry + the 4 invariants, encoded in comp-coverage-map.yaml grain_contract; gate rules 7 (stable_grain) + 8/9 (drilldown-seam, rollup-consistency) | **LANDED / IN-FLIGHT** | ~C grain-thread (rule 7 landed `01af67fcc`, selfcheck 6/6 COO-verified) + the §10 gate-rule FOLD (rules 8/9, in flight now — CTO-direct, guard lifted) | 0.8.0_AE_CloudComp~C (COMPUNIFY governs) |
| **P1 — populate the depth ladders** | derive CONTAINS/OWNED_BY/RUNS edges + `level` attrs; cross-stratum seam EC2-RUNS->PipelineScript; gold-tier-first; bounded materialization at fine grain (boundary 4b) | **RIDES GRAPHUNI P1** | NFRA_GRAPHUNI.P1 (~D) — the depth-ladder population IS the GRAPHUNI gold-population viewed on the depth axis. CVO-fixture-gated. ONE build, cross-tagged. | 0.8.0_AE_CloudComp~D (GRAPHUNI populates) |
| **P2 — tool depth-calibration** | tag every tool's operating grain + audit declared-grain vs real-traversal; wire `(breadth,depth)` scoping; grain-gaps -> COMPLEARN | **= COMPUNIFY S4** | COMPUNIFY S4 tool-grain calibration (CTO folded into COMPUNIFY PRD `c64eba0`); ~C-owned, ~D-consult; MANDATE-FIRST: sequences AFTER the grain-ladder (P1) is CTO-arch-gated | 0.8.0_AE_CloudComp~C (consult ~D) |
| **P3 — depth-scoped tooling** | **NET-NEW** — structure-tools scope traversals by declared depth (drill/rollup correctly); the cross-stratum trace goes live (comp-blast: script-change -> EC2 runner -> served) | **NEW TO** (the capability payoff) | NFRA_GRAPHDEPTH.P3 (authored alongside this map) — gated on P1 population + P2 calibration | TBD at dispatch (structure-tool lane; ~D/GRAPHUNI re-point continuation or ~C) |

## Acceptance (cross-tagged — PRD §10, CVO)
CVO acceptance composes the existing verifies, no separate redundant pass: (a)+(b) every node/edge has a declared `level` + zero per-depth re-typing = the stable_grain gate passing estate-wide (rides COMPUNIFY V1 + the GRAPHUNI population verify); (c) rollup-consistency zero UNSUPPORTED/COARSE-INCOMPLETE = the §10 rollup gate on the populated strata (rides GRAPHUNI V1); (d) every tool calibrated, zero declared!=real = the S4/P2 verify; (e) a depth-scoped investigation bounds correctly = the P3 cross-stratum trace demo. LD-0230 Art. XIV ratification (CVO) is the constitutional capstone, tracked separately.

## What COO~B holds (the spine)
- The cross-tag integrity: GRAPHDEPTH phases do NOT spawn duplicate builds; each points at its real in-flight TO. If a phase's source work changes, the cross-tag updates — one source of truth per phase.
- The seam coordination: the drilldown-seam + rollup-consistency are GRAPHDEPTH P0 gate rules AND COMPDRIFT seam-taxonomy invariants (banked) AND GRAPHUNI D4's one-head seam — one seam set across the three.
- The mandate-first sequencing: P2 (S4 calibration) waits for the P1 grain-ladder arch-gate; P3 waits for P1 population. No phase jumps its gate.
- Sequence the whole layer behind the live ADVI_BREAKS firefight (CVO is firefight-load-bearing; P1 is CVO-fixture-gated behind it).

## Net-new build from GRAPHDEPTH = P3 only. Everything else is formalization + cross-tag of work already dispatched/landed.
