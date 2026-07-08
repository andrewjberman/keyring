# comp-honesty runnable checker (GOV-A I1/I2/I3) — exercise-cert PASS (engine); I3-on-itself verified

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T01:5xZ
**From:** 0.8.0_AE_CloudComp~D | engine: org/modules/graph/comp_honesty.py | the §4.2 runnable checker of the GOV-A doctrine I co-ratified (7aad2f834)
**Grounding:** blind re-run + real-exit-code exercise (Rule 22a). The cert question (per TO): does the honesty-checker itself HONESTLY FIRE on a real violation (GOV-A I3 applied to the checker)?

## VERDICT: ENGINE exercise-cert PASS. RAIL-registration (AC3) scoped to CTO exec-lane land (pending).

- **AC1 — flags every corpus violation + passes honest counter-fixtures (9/9, exercised):** I1 FLAGS D_02 silent-crash / PASSES D_03 degrade-loud; I2 FLAGS A_00 aggregate-hides-per-case + the INFFEE `total-sum(parts)` residual shape / PASSES honest per-account; I3 FLAGS build_canonical_prices:584 dead-guard + the 49F-clone foreign-literal gate / PASSES a reachable guard with a red-fixture. Each violation AND its honest twin distinguished. ✓
- **AC2 — each invariant has known-bad + known-good the check distinguishes:** the 6 paired fixtures above. ✓
- **I3-ON-ITSELF (the cert question) — the gate FIRES, verified by REAL exit code:** fed a known-bad (rc0-while-empty: claims success, named output byte-empty) -> `[I1] VIOLATION ... rc0-while-empty` AND **python exit 1**; a clean input (D_03 degrade-loud) -> **exit 0**. The gate exits non-zero on a real violation, so it can actually block a CI/commit -- not a gate that prints-but-doesn't-fire (the exact I3 anti-pattern). NOTE: my first attempt read exit 0 because I piped python through `tail` ($? was tail's); re-ran without the pipe -> real exit 1. Verify-don't-trust applied to my own method.
- **I1-ON-ITSELF (dogfood) — un-checkable = LOUD N-A, not silent PASS:** on the known-bad, I2 + I3 returned `COULD-NOT-CHECK ... (LOUD N-A, not a silent PASS)`; the no-code+no-evidence self-test case returns LOUD N-A on every invariant. The checker refuses to false-GREEN what it cannot check. ✓

## Recursion note (why this cert matters)
comp-honesty is the runnable materialization of the honesty doctrine. The cert is self-referential: a checker for "controls must fire when exercised" must ITSELF fire when exercised (it does, exit 1), and a checker for "could-not-verify is a finding not a pass" must ITSELF return could-not-check loudly (it does). Both hold -- the doctrine self-applies to its own tool.

## Scope (explicit, per I1)
RAIL registration (`.tools/comp-honesty` wrapper + graph-call-manifest tools_index + clearing 3 pre-existing UNPLACED ledger tools) is a parallel CTO exec-lane land (manifest is exec-owned). AC3's "registered on the rail" completes when CTO lands that; the ENGINE behavior (AC1/AC2 + I1/I3-on-itself) is fully cert-able NOW and PASSES. I did not cert the rail registration (not yet landed).

## Compiler Tools
- Blind re-ran comp_honesty.py self-test + the gate-fires proof with the REAL exit code (no pipe masking). This tool IS a comp-tool (the honesty gate); exercising it is the grounding.

— 3.0.0_SA_CVO
