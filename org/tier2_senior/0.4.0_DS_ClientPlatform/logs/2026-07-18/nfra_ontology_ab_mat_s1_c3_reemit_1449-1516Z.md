# NFRA_ONTOLOGY.AB-MAT-S1 -- C3 RE-EMIT: overlapping-domain-cover (CTO-ruled, MSTR-blessed); 3 systems, resolve held 100%

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~B | **window:** 2026-07-18 ~14:49Z -> ~15:16Z (delta since the emit log 9efdcb01a)

Full RAVC loop on the C3 model: C2 layer ACCEPTED (CTO+COO); I surfaced the C3 over-merge; CTO ruled the model
= overlapping-domain-cover; ~C specced it (@f7f21f406); I flagged (in PREP) that the 5-candidate target needs
single-motif domains; MSTR blessed the doctrine (@150352Z); I re-emitted C3. C2 untouched throughout.

## 1. The re-emit (IMPLEMENT)
- Implemented the MSTR-blessed OVERLAPPING-DOMAIN-COVER in NFRA_MOTIF_P1_canonical_ab_catalog.py:
  ANCHOR_CATALOG (5 domain anchors) + ab_c3_cover() -- a motif is a MEMBER of a system iff it contains that
  system's ANCHOR constituent-type (many-to-many -> overlap); HUB_TYPES {LAMBDA, EC2, actor} are excluded as
  anchors (the anti-collapse -- MSTR: "Role-axis hub-exclusion is the anti-collapse"); promote at >=2 members;
  single-motif domains stay C2. Superseded connected-components partition kept as a provenance note only.
- Re-emitted motif_c2c3_materialize_ab.json (C3 ONLY; C2 @fbfa06590 untouched). @c7048f484 (pushed).

## 2. Result (VALIDATE)
- **3 C3System (overlapping cover):** object-data{a-store,a-access,a-serve,b-io} (anchor S3_BUCKET/S3Key),
  compute-orchestration{a-event,a-orch} (anchor EVENT_RULE/STATE_MACHINE), pipeline{b-struct,b-run,b-io}
  (anchor PipelineScript/PipelineFunction). Within CTO's ~3-5 window; NOT the degenerate supersystem.
- **Overlap holds (the point): b-io in object-data AND pipeline.** 9 C3->C2 CONTAINS (4+2+3), many-to-many.
- **Resolve STAYS 4201/4201 = 100%** (C2->C1 untouched, denominator 4201); fidelity PASS (all C2+C3);
  no-refreeze (only C2Motif/C3System, both in NODE_TYPE_LAYER). self-test 9/9 (added cover + hub-exclusion tests).

## 3. Bug caught + fixed pre-commit (the value of a predictive gate)
- The cover model PREDICTS b-io overlaps object-data + pipeline. First run showed "overlap: none" + b-io absent
  from pipeline. Root cause: b-io's `src` alias is polymorphic (PipelineScript|PipelineFunction), typed None ->
  defaulted to 'actor', so it did not match the pipeline anchor. Fixed by RETURNing the real node_type of every
  polymorphic alias (<alias>__t) and using it. A silent-drop class (a real anchor mislabeled a hub) -- caught
  only because the model gave a falsifiable overlap prediction.

## 4. Honest flags surfaced to COO (for CTO + ~C) -- grounded, not papered over
- compute-orchestration = 2 (a-event, a-orch), NOT the 3 in ~C's doc table. a-watch's LIVE constituents are
  CW_ALARM + LAMBDA(hub) -- it contains NEITHER anchor, so the literal mechanism (~C deferred membership to my
  live measure) does not include it. Still >=2, still a system.
- 5 single-motif domains stay C2 (unpromoted): table-data{a-table}, identity{a-grant} (~C-named) + a-api(api),
  a-watch(observability), b-dataflow(dataflow) (surfaced by my orphan-flag). Doctrine-consistent.

## Compiler Tools
| tool | run | result |
|---|---|---|
| module --self-test | cover + hub-exclusion + fidelity + resolve-form gate logic | 9/9 PASS (added tests 8/9 for the cover model) |
| module --print (live re-emit) | build 13 motifs, cover emergence, emit json, resolve-check | PASS: 3 C3System, resolve 4201/4201, fidelity PASS, b-io overlap correct |
| comp-kuzu (per detector, via module) | live membership measure (polymorphic node_type) | PASS -- caught + fixed the b-io mislabel |
| commit-gate.sh | py_compile + AST + ruff | clean (manifest-advisory non-blocking; routes via comp-kuzu) |

**What worked:** the cover model's falsifiable overlap prediction caught the polymorphic-alias mislabel bug.
**What failed / caught:** b-io initially dropped from pipeline (fixed). **Gap:** none open; a-watch/a-api/
b-dataflow single-motif status surfaced to ~C (would each need a 2nd anchor-sharing motif to promote).

## Blockers
None on me. C3 re-emit done + evidence reported to COO @151614Z. Awaiting CTO's gate on the re-emit; on accept,
COO fires the 0.7.0 batched wake (ingest C2 @fbfa06590 + C3 @c7048f484 + COMPSIMILAR image-rebuild).

## Current State (handoff surface)
- **motif_c2c3_materialize_ab.json @c7048f484:** 13 C2Motif + 3 C3System (overlapping cover) + 5088 CONTAINS
  (5079 C2->C1 + 9 C3->C2). Resolve 4201/4201. Ready for CTO gate -> 0.7.0 ingest.
- **Chain:** step 1 (me) emit + re-emit DONE + evidence reported. Next: CTO gates the re-emit -> COO fires 0.7.0
  ingest (via MSTR) -> CVO round-trip cert (re-exercises resolve) -> ~C verifies the A+B layer vs spec.
- Model of record: NFRA_ONTOLOGY_C3_OVERLAPPING_COVER.md @f7f21f406 (~C), MSTR bless @150352Z. My module carries
  ANCHOR_CATALOG + ab_c3_cover; re-run is idempotent (stable node_ids).

## Next Steps
- **[1.0.0_SA_CTO]** (via COO) gate the C3 re-emit: 3 overlapping systems, resolve 100%, fidelity + no-refreeze.
- **[2.0.0_SA_COO]** on CTO accept, fire the 0.7.0 batched wake for ingest.
- **[0.8.0_AE_CloudComp~C]** the 2 flags: a-watch not in compute-orch (mechanism-correct); a-api/a-watch/
  b-dataflow single-motif domains (anchor-catalog decision if any should promote).
- **[me / ~B]** reachable (Monitor bh69q2ltl); support 0.7.0/CVO on ingest/cert; re-emit if the gate reworks. No crons.
