# NFRA_ONTOLOGY.AB-MAT-S1 -- canonical A+B motif catalog built + materialize emitted; C2 solid, C3 gap SURFACED to COO

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~14:07Z -> ~14:41Z (delta since the CSE-ruling log 0f8716861)

COO GO (140733Z, Andrew-direct NFRA headline; CTO SoD gate OPEN 140326Z) -> step 1/4 of the A+B materialization
chain. Built the canonical A+B motif catalog (13 detectors), ran it + emergence live, emitted the materialize
records. C2 layer done + verified; C3 emergence over-merged -> surfaced to COO per the TO's own <if_mismatch>.

## 1. What I built (IMPLEMENT)
- `NFRA_MOTIF_P1_canonical_ab_catalog.py` (NEW, my deliverables) -- 13 canonical detectors (9 Plane-A + 4
  Plane-B) per ~C's binding spec @7892f3fbc. A canonical SIBLING of the debt catalog (TO allows it): keeps the
  CVO-certed + already-ingested debt layer untouched, adds A+B additively. Reuses (never forks) the debt
  module's comp_kuzu runner, GraphUnavailable fail-loud, AC3_THRESHOLD, system_node_id, + the REAL comp_ladder
  fidelity gate. self-test 7/7 (fidelity positive + latent negative control + resolve-form + emergence +
  inherited-naming + collision-safe/stable node_id). commit-gate clean.
- `motif_c2c3_materialize_ab.json` (NEW) -- the emitted materialize records (13 C2Motif + 1 C3System + 5091
  CONTAINS edges).
- Both @fbfa06590 (pushed CLOUD).

## 2. C2 layer -- DONE + VERIFIED (the core deliverable) (VALIDATE)
- 13 A+B C2Motif nodes, all recurrence >= AC3, all fidelity-PASS.
- 5079 C2->C1 CONTAINS edges. **CTO acceptance cond 1 EXERCISED: 4201/4201 (100%) distinct C2->C1 targets
  resolve to a store node; denominator 4201.** Independent exercise -- targets built from per-detector MATCH
  queries, verified against a SEPARATE full node_id pull (20334 store nodes). No c1:D{n}: discriminator exists
  (A+B detectors match estate nodes directly: ARNs / '<type>:...'), so the 07-08 comp-kuzu 0-row trap does not
  arise; resolve is BOTH by-construction AND by the independent check.
- **CTO acceptance cond 2 confirmable: no new node_type** -- live counts C2Motif=6, C3System=1 already in
  NODE_TYPE_LAYER; I emit only those two types, so derive_runner.relabel_layers_by_node_type won't trip.
- **Recurrence MEASURED live @HEAD 8797848286033539361 (Rule 22 -- not echoed).** Corrected 3 spec errors:
  a-store=232 (spec 28902, impossible: bounded by S3Key=232), a-serve CDN-leg=9 (spec 228: bounded by
  ORIGIN+USES_OAI=9 on 1 CLOUDFRONT_DISTRIBUTION), a-watch=21 (spec 184/71/50: MONITORS total=28), a-orch=28
  (spec 62). Other 9 match the spec breakdowns. -> flag ~C for the spec recurrence column (routed via COO).

## 3. C3 layer -- the SURFACE (COORDINATE) -- TO Phase-3 <if_mismatch>
- The certed connected-components union-find OVER-MERGES 12/13 motifs into 1 supersystem + b-dataflow singleton.
  Cause: LAMBDA(189)/S3_BUCKET(39)/EC2(33)/PipelineScript(133) INSTANCES are shared across capabilities -> a
  transitive partition collapses them. = the SAME degenerate shape as the debt system, not the spec's 3-5.
- Root: the spec's Sec-2 ~3-5 are an OVERLAPPING domain-resource-type COVER (a-access in object-data AND
  compute; b-io in object-data AND pipeline). A connected-components PARTITION cannot represent overlapping
  systems. The cover model CHANGES what "C3 system" means -> ~C (vocabulary) + CTO (arch-gate), NOT my call.
- Computed + surfaced the domain cover (in the json, NOT emitted as nodes): object-data{a-store,a-access,
  a-serve,b-io}, compute{a-access,a-table,a-grant,a-event,a-api,a-watch,a-orch,b-run}, pipeline-code{b-struct,
  b-run} = 3. Real finding: table-data + identity are SINGLE-motif (only a-table touches DynamoDB, only a-grant
  touches IAM) -- the spec's 5-way split assumed clustering the estate does not have.
- SURFACED to COO @144120Z with the decision: ingest the C2 layer now (solid); route the C3 model (partition-1
  vs cover-~3) to ~C/CTO; I re-emit C3 within minutes on their ruling. Did NOT unilaterally emit the cover
  (= splitting around the gate).

## Compiler Tools (reproduces every TO <run>)
| tool (TO phase) | run | observed | vs <expect> |
|---|---|---|---|
| comp-kuzu-inc (Phase-1 freshness) | refresh projection to HEAD | HEAD 8797848286033539361, age 0.0h, pin==HEAD | PASS (not UNKNOWN VINTAGE, not frozen scratch) |
| comp-kuzu node_type dist (Phase-1 no-refreeze) | DISTINCT n.node_type + count | C2Motif=6, C3System=1 PRESENT; all A+B node types resolve | PASS (both in NODE_TYPE_LAYER -> no new node_type) |
| comp-kuzu edge_type dist | DISTINCT e.edge_type + count | all 13 detectors' edge types present (CONTAINS/OWNED_BY/READS/WRITES/ASSUMES/HAS_POLICY/EMITS_TO/TRIGGERS/ROUTES_TO/MONITORS/INVOKES/RUNS/READS_S3/WRITES_S3/FLOWS_TO/...) | PASS |
| probe_ab.py (comp_kuzu per detector) | measure recurrence of all 13 | all 13 non-zero + >= AC3; 3 spec numbers corrected | PASS (grounded, not echoed) |
| module --self-test | gate logic (no live graph) | 7/7 | PASS |
| module --print (live emit) (Phase-2 resolve + Phase-3 evidence) | build 13 motifs, emerge, emit json, resolve-check | 13 C2Motif, resolve 4201/4201, fidelity PASS, C3=1 (over-merge) | C2 PASS; C3 mismatch -> SURFACED to COO |
| commit-gate.sh | py_compile + AST + ruff on the module | clean (1 ruff F401 fixed: unused decompress import) | PASS |

**What worked:** measuring recurrence live caught 3 spec errors (a-store 28902 was impossible); the resolve
self-check via a separate full-node pull is a genuine independent exercise, not a by-construction assertion.
**What failed / caught:** self-test-1 caught my split of the single a-serve motif into two (10A instead of 9A)
-> merged to compound sub-queries; the resolve IN-list crashed on WinWerror 206 (command too long) -> rewrote
to a full-node-set intersection in python. **Gap surfaced:** the certed connected-components emergence is
degenerate for densely-shared infra -- a real C3-model question for ~C/CTO (partition vs overlapping cover).

## Blockers
None hard on me. C2 layer complete + reported. C3 model + 0.7.0 ingest are COO's (run-owner) next steps;
the C3 model ruling is a ~C/CTO gate I cannot make. Reachable for the ruling.

## Current State (handoff surface)
- **Emitted:** motif_c2c3_materialize_ab.json @fbfa06590 -- 13 C2Motif + 1 C3System (connected-components) +
  5091 CONTAINS. C2->C1 resolve 4201/4201. Ready for 0.7.0 ingest (C2 layer).
- **C3 decision PENDING at COO -> ~C/CTO:** partition (1 supersystem, emitted) vs overlapping domain-cover
  (~3 operational systems, computed + surfaced in the json's c3_emergence_note, NOT emitted as nodes). I re-emit
  on the ruling (ab_domain_view already implemented).
- **Chain:** step 1 (me) emit DONE + reported to COO; step 2 = 0.7.0 ingest (COO spawns via MSTR); step 3 = CVO
  round-trip cert (re-exercises resolve); step 4 = ~C verifies the A+B layer vs spec @7892f3fbc.
- Prior this session: CSE-owner ruling @d16e269bf (accepted+folded @352549fb0); OWNS 0.4->0.5 bump awaits CTO gate.

## Next Steps
- **[2.0.0_SA_COO]** owns the run: ingest the C2 layer via 0.7.0; route the C3 model (partition vs cover) to
  ~C/CTO; relay the 3 recurrence corrections to ~C for the spec.
- **[0.8.0_AE_CloudComp~C + 1.0.0_SA_CTO]** (via COO) rule the C3-system model: connected-components partition
  (what "C3 system" means today) vs overlapping domain-resource-type cover (the spec's Sec-2 candidates). I
  re-emit C3 within minutes on the ruling.
- **[me / ~B]** reachable (Monitor bh69q2ltl). Re-emit C3 on the ruling; support 0.7.0/CVO on ingest/cert. No crons.
