# NFRA_COMPPROOF — Lane / Staffing Note (pre-PRD)

**Owner:** 2.0.0_SA_COO~B (comp-program operational lane) | **Charter:** MSTR LD-0234 (Andrew-direct, brief 94b60a27f) | **Noted:** 2026-07-01
**Status:** CHARTERED, shape MSTR-accepted. Formal PRD + TO decomposition ride POST-ADVI_BREAKS-cutover (CTO authors PRD, hands to COO~B for decomposition). This note is a pre-decomposition placeholder so the constraints survive to that point.

## HARD STAFFING CONSTRAINT (Andrew-direct 2026-07-01)
**0.8.0_AE_CloudComp~B is OFF-LIMITS for COMPPROOF** — busy on Andrew's directed end-to-end estate-graph + comp-* traversal validation. Do NOT task ~B with any COMPPROOF workstream. **Staff COMPPROOF from ~A / ~C / ~D / ~E** (+ 3.0.0_SA_CVO~B for the verify-heavy workstreams A/C-Goodhart-gate). (~B's own validation output is a natural SEED for workstream B, but ~B is not assigned COMPPROOF work.)

## Shape (MSTR-accepted, per CTO 053340Z)
- ONE macro NFRA_COMPPROOF for A/B/C/D1; **D2 (self-extension spike) FENCED** as a gated sub (own kill-criteria + PROPOSED-NOT-DEPLOYED + RV-0026 CL-fabric sovereign-surface).
- **A** = seam/process spot-check sweep (CVO / verify-channel; rides the wave-close, does NOT preempt GRAPHUNI/GRAPHDEPTH/Phase-B).
- **B** = THE SPINE: incident-regression graph-solvability benchmark (blind-test agents reach root cause via graph+comp-tools on the REAL record, start ADVI_BREAKS; SOLVED/PARTIAL/MISS -> gap charters + standing suite). **Rubric = REACH x USABILITY** — a correct-but-unusable-under-load tool = FUNCTIONAL MISS (e.g. the comp-pipescript/comp-freshness inf-sweep timeout = PARTIAL-tending-MISS). **Blind-solver isolation: author != solver != judge (HARD TO-gate).**
- **C** = COMPROUTE efficacy eval (precision@1 / recall on a labeled intent-set from B + rail.log; CVO Goodhart gate).
- **D** = COMPLEARN autonomy audit (D1: loop real vs dead ratchet, live EventBridge->Fargate artifacts) + D2 self-extension spike (fenced).

## Sequencing
- **B first** (seeds C's intent-set + D's gap-feed); A/C/D1 concurrent on live artifacts; D2 gated behind D1.
- COMPPROOF sequences AFTER the COMP* closes it validates — **already satisfied**: COMPROUTE Stage-1 CLOSED (12c7aa1f4) + COMPLEARN CLOSED (bdc6d01a6) this session, so C consumes the live comp_route.py + comp-which flywheel and D1 reads the live scheduled-loop artifacts.
- A rides wave-close; does NOT preempt the in-flight GRAPHUNI/GRAPHDEPTH finish.

## On decomposition (post-cutover)
CTO hands the PRD -> COO~B decomposes into first-wave TOs (B-first) -> RAVC MSTR the first wave. Apply the ~B-exclusion above; staff from ~A/~C/~D/~E + CVO~B. Encode blind-solver isolation as a hard TO-gate on B.
