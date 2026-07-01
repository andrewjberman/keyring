# NFRA_COMPPROOF.B1 -- the B benchmark harness SPINE built + self-tested (lane ~D)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State
COO~B dispatched B1 (the SPINE of NFRA_COMPPROOF -- the program proving itself: for each real
incident, from the symptom ONLY, can a blind agent reach the true root cause TODAY via graph +
comp-tools?). Built it to CTO's arch (NFRA_COMPPROOF_B_HARNESS_DESIGN.md 1315f9a03). Committed
51196d3a9 (pushed), one home org/modules/graph/compproof/ under the COO~B-landed lane grant (38142e83b).

**BUILT + SELF-TESTED (structural ACs met):**
- `corpus.py` -- the PINNED top-20 (5402f130b) in the authored 5-field schema (ADVI_BREAKS #1 worked
  example + 19), each verified vs its citation. Solver-visible = symptom+date; SEALED = root_cause +
  how-found + failure_class. + the success-shaped-wrong CLASS probe (not a numbered slot).
- `corpus_loader.py` -- emits SOLVER-VIEW (opaque case_id B-NN + symptom + estate + tool-surface ONLY)
  + SEALED JUDGE-VIEW. **DIFF-GATE: root_cause NOT-IN solver_view for ALL 20 (AC#1 PASS 20/20).**
  The gate iterated to correctness: caught real leaks (the descriptive id `INF_SPARSE_CUMSUM` +
  `failure_class` -> excluded from solver-view) then false-positives (the FIXED scaffolding
  estate/tools/task words like 'freshness'/'head'/'symptom' -> the gate checks INCIDENT-SPECIFIC
  content only, distinctive-term, exact-token). The gate WORKING is the proof.
- `harness.py` -- the HARD isolation gate (author!=solver!=judge AND root_cause-not-in-payload,
  VOID-on-violation, STRUCTURAL) + spawn-payload builder + 3-axis scorer (REACH x USABILITY x
  GROUNDING-RESILIENCE; SOLVED needs all 3; MISS on can't-reach OR mis-grounding-trip) + the
  success-shaped-wrong canary + gap-charter emitter (MISS/PARTIAL -> filed charter, feeds D) +
  aggregate + a standing re-runnable self-test. SELF-TEST PASS: ADVI_BREAKS #1 -> PARTIAL + charter
  (matches arch sec-4), isolation VOIDs on author==solver, scorer/aggregate correct.

**AC#3 (the 20-incident blind RUN) = HANDED OFF (the execution phase).** I'm the AUTHOR -- isolation
BARS me from solving OR judging. Per the arch: MSTR spawns a FRESH agent per incident with
spawn_payload(incident) ONLY (answer-free, gate-verified); CVO (TO-B2) judges each vs the sealed
judge-view via score_run's 3 axes. I did NOT self-spawn solvers (that would blur author!=solver --
the whole point of B). RAVC'd COO~B + CC CTO (arch) + CVO~B (B2 judge).

## Compiler Tools
| tool | use | result |
|---|---|---|
| comp-which | route "how to spawn an isolated blind-solver" (arch already specifies MSTR-spawn) | PASS -- isolation mechanism grounded from the arch doc |
| corpus_loader (self-test) | AC#1 STRIP DIFF-GATE across the 20 | PASS 20/20 (iterated: caught id+failure_class leaks + scaffolding false-positives) |
| harness (self-test) | AC#2 isolation VOID-on-violation + AC#4 scorer/charter/aggregate + ADVI_BREAKS #1 | PASS -- payload answer-free, VOID on author==solver, ADVI_BREAKS -> PARTIAL + charter |
| ds-commit-gate | pre-commit (3 files) | PASS (fixed 1 unused import) |

**What worked:** the DIFF-GATE iterating to correctness IS the deliverable's proof -- it caught its
own author's leaks (descriptive id, failure_class) before the strip could pass, exactly the
adversarial-isolation discipline B measures. **Gap found:** none in-scope; the blind-RUN execution is
a staffing-gated phase (MSTR+CVO), not a build gap.

## Blockers
None assumption-blocked. AC#3 blind-run is staffing-gated (MSTR spawns solvers, CVO~B B2 judges) --
a declared external phase, not a block. I'm author-barred from the solve/judge by design.

## Next Steps
1. **[2.0.0_SA_COO~B]** sequence the blind-RUN: MSTR spawns a fresh solver per incident (spawn_payload
   only); CVO~B (B2) judges. The harness provides payload + isolation-gate + scorer + charter.
2. **[3.0.0_SA_CVO~B]** TO-B2: judge each solver's concluded-root-cause + path vs the sealed judge-view
   (score_run 3 axes) -> aggregate coverage %.
3. **[0.8.0_AE_CloudComp~D] (me)** author-support: harness fixes, the ADVI_BREAKS reference run,
   aggregate/charter wiring; then the deferred queue ((a)+E2 derive-fidelity / GRANTS_S3 / code_heat
   / NFRA_INFRPT retire-tail) on COO~B sequencing.
