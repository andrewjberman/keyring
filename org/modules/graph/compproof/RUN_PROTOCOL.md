# NFRA_COMPPROOF B -- blind-run PROTOCOL (who does what; the harness is ready)

The B1 harness (corpus.py + corpus_loader.py + harness.py + blind_run.py) is built + accepted. This
is the turnkey run protocol for the blind-RUN (AC#3). **Isolation (the hard gate): author != solver
!= judge.** ~D (author) built the sealed corpus + runs the aggregation DRIVER only -- never solves or
judges. Per CTO arch-lead (141830Z): run a **pre-flip BASELINE now**, re-run **post-flip**; the
pre->post delta measures the default-router flip's solvability improvement (harness SS1.4 trend line).

## Roles + steps

1. **MSTR (spawn-executor)** -- for each incident, spawn a FRESH agent (no memory, no corpus, no
   prior-B result) with `corpus_loader.solver_view(incident)` as its ENTIRE prompt (the answer-free,
   DIFF-GATE-verified payload). The solver reaches for the root cause via the live graph + comp-tools
   and returns `{concluded_root_cause, traversal_path, confidence}`. Collect into:
   ```json
   solver_results = { "B-01": {"concluded_root_cause": "...", "traversal_path": ["..."], "confidence": "low|med|high"}, ... }
   ```
   (case_id B-NN is the opaque id; MSTR does NOT need the incident identity -- just spawn per case_id
   with its solver_view. The case_id->incident map is judge-side.)

2. **CVO~B (TO-B2 judge)** -- for each solved case, given `corpus_loader.judge_view(incident)` (the
   sealed root_cause + how-found) + the solver's concluded-root-cause + path, score the 3 axes:
   ```json
   judge_axes = { "B-01": {"reach": "yes|narrowed|no", "usability": "usable|too-slow|fell-back", "grounding_resilience": "resist|trip"}, ... }
   ```
   Rubric (harness.score_run): SOLVED = reach==yes AND usable AND resist; MISS = reach==no OR
   grounding==trip (recorded a success-shaped-wrong as truth); else PARTIAL. Edge cases on the
   PARTIAL-vs-MISS line -> flag CTO (arch-lead on the run).

3. **~D (author, DRIVER only)** -- run the aggregation over the provided inputs (no solve/judge):
   ```
   python org/modules/graph/compproof/blind_run.py --solver-results solver_results.json \
          --judge-axes judge_axes.json --out report.json
   ```
   Emits: per-incident verdict + aggregate SOLVED/PARTIAL/MISS % + a gap-charter per MISS/PARTIAL
   (feeds Workstream D) + PENDING for any not-yet-run case (never a silent MISS). Re-runnable: the
   flip is a substrate change -> re-run post-flip; the pre->post delta is the flip's solvability lift.

## Sequencing (CTO refinement)
- BASELINE (now, current backstop-router substrate): start ADVI_BREAKS #1 (B-01) to validate the loop
  end-to-end, then the 20. Does NOT wait on the DRV-flip.
- RE-RUN (post-shadow-flip, default-router substrate): the same 20 -> delta = the flip's solvability
  improvement. (C1/COMPROUTE-eval stays post-flip; B1 benefits from BOTH runs.)
- CVO~B is hot on the flip cert; the SOLVES (MSTR) can run now + bank solver_results; CVO judges when
  free -- the solve and the judge decouple cleanly (the driver reports PENDING until both land).

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1). 2026-07-01.
