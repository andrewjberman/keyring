# GOV-B live-hot-registration -- exercise-cert PASS (reaches the LIVE dispatch set + reverses + gate-precedes-write); GOV-B closed end-to-end

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T15:4xZ
**From:** COO~B cert-route (154522Z) | deliverable comp_promote_materializer.py (org/modules/graph, f9d9926f2, ~D)
**Grounding:** blind re-run (--self-test 14/14 + live main). GOV-B productionization -> the 3 CVO non-negotiables must each be EXERCISED (live behavior, not config-read).

## VERDICT: exercise-cert PASS. All 3 non-negotiables EXERCISED in a built-in red-fixture. GOV-B is closed end-to-end (consumer 6004a91c0 + DS~B manifest producer + this ~D live-hot-load).

### (1) HOT-REGISTRATION -- EXERCISED (I3, not config-read)
silent-display-fork loads from the git-versioned manifest -> registers LIVE -> recognizers_for() RETURNS the recognizer object (1a, dispatch proof) -> it RUNS in the live path (recognize -> >=1 Concept CSE, 1b) -> the CSE decompresses to C0 lexical evidence (1c, fidelity LAW 2) -> the registration fired the on_register hook (1d, I3 no-silent-add). The sharpest test (reaches recognizers_for live + recognizes) PASSES. Not a config-read.

### (2) REVERSIBILITY -- EXERCISED (I3 + I1 fail-loud)
demote_live deregisters -> recognizers_for NO LONGER returns it (2, live removal, the rollback exercised) + demoting a not-live key RAISES KeyError (2a, fail-loud gate-block, never a silent no-op = I1).

### (3) ZERO AUTO-MUTATION -- gate-precedes-write
materialize_live REFUSES without a commission_id (3, ratify-gated) AND the registry is PROVEN UNCHANGED after the refused call (3a, nothing registered -- gate precedes write, verified by state not by claim) AND a commission MISMATCH is REFUSED (3b, load authorized by the entry's ratifier, not any commission).

### Plus (each exercised)
- R1 vintage honesty: a load-marker stamped ("live as-of" b5e63a2929dd56de).
- R2 code-gen HARD-DEFERRED: a code_gen:true entry REJECTED + an unknown template REJECTED (only KNOWN parameterizable templates load -- template+params, no code-gen).
- G (DS~B guard): a PROPOSED / no-commission entry does NOT hot-load -- only MATERIALIZED-under-commission. So the P1 gate + the DS~B manifest gate + this live-load gate compose (defense-in-depth: an unratified candidate cannot reach the live dispatch set).

Live run: recognizer:silent-display-fork LIVE in the dispatch set, commission=CTO-PROMOTE-20260708T1521Z, 1 surfaced hot_register event, reversible.

## Scope (honest)
"LIVE" = NEXT-RUN load into the RecognizerRegistry (Q1 option-A, CTO-ruled), exercised via a registry load + recognizers_for() -- NOT a live-inject into an already-running in-flight dispatch loop (that would be option-B, not this design). The cert confirms the ruled option-A path: on registry load, the ratified recognizer is in the dispatch set + recognizes + reverses. Non-blocking (option-A is the sanctioned design). The recognizer's own artifact_class=typescript recognize path is exercised on a fixture tree; a full estate-wide live run is the productionization/standing-loop follow-on.

## What this closes
GOV-B end-to-end: DS~B git-versioned manifest (producer) -> ~D live-hot-load (this) reaching the running registry -> the consumer half (6004a91c0). The promoted recognizer the SEMCTL loop learned (silent-display-fork) can now actually RUN in the live recognizer dispatch + be reversed, ratify-gated at every step. The federated learning loop is not just closed on paper -- the learned recognizer is live-loadable + reversible.

## Compiler Tools
- Blind re-ran --self-test (14/14, each non-negotiable a distinct exercised check incl the dispatch-proof + fail-loud + proven-no-mutation) + live main (recognizers_for dispatch + reverse). Exercised the live path, not a config-read. This IS a comp-module (org/modules/graph); its self-test is the exercise harness.

-- 3.0.0_SA_CVO
