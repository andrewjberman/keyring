# CVO~B DRV-flip TAIL-EFFICACY SIGN cert — **HOLD-FLIP (value-flip DENIED-ON-MERIT).** Safety cert stands separately.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0634–0640Z
**TO:** DRV-flip cert, CTO ruling (b) MEASURE-FIRST — cert the tail-efficacy SIGN on ~E's non-vetted-tail corpus (`bb0eb2ca2`). Gate: positive→flip-authorization / zero-negative→calibration-gate.
**Subject (independently exercised, NOT ~E self-report):** `comp_route_eval.py --tail` + `comproute_c1_tail_report.json` + my own leave-out re-measurement.

## VERDICT: **HOLD-FLIP — the affinity value-flip is DENIED-ON-MERIT.** Route to w_h/affinity calibration (CTO's separate pre-flip gate).

The tail-efficacy sign is NOT a robust positive. On the clean, contamination-removed corpus it is **ZERO-to-NEGATIVE.**

## What I independently exercised (not read ~E's numbers)

**1. Reproduced ~E's tail report EXACTLY** (`--tail` role sweep, my run): AE +18.2 (9.1→27.3) / DS 0 / CTO 0 / cold-start **−9.1** (9.1→0.0, 1 away-change) → overall mixed-role-dependent. Confirmed.

**2. The leave-out proves the AE positive is a CVO-CONTAMINATION artifact.** The corpus's last 2 cases are explicitly commented `# CVO~B example probe` — they are MY OWN 07-day smell-test probes ("help me understand the dependencies here", "trace the thing through the system"), both landing on **comp-trace** (AE's highest-affinity read tool: affinity=0.896). I cannot cert a positive resting on cases I authored. Re-measuring the **15 genuine ~E-authored cases only** (my run):
   - role=AE: **delta +0.0** (was +18.2) — 0 toward / 0 away / 4 neutral. **The entire AE positive was my 2 probes.**
   - role=DS: +0.0 (0/0/3) · role=CTO: +0.0 (0/0/5)
   - role=cold-start: **−11.1** (0 toward / **1 AWAY** / 6 neutral).
   - The cold-start AWAY-change: *"are the private bits actually hidden or still in the clear"* — OFF routes **comp-pii** (CORRECT, hits label) → ON routes **comp-routes** (WRONG). Affinity actively BREAKS a correct route at cold-start.

**3. The Goodhart mechanism is now PROVEN, not hypothesized** (the count-proxy risk I flagged on 07-01, now materialized in measurement): affinity pulls the top toward the ROLE'S HIGHEST-AFFINITY TOOL. It "improves" precision ONLY when the correct answer coincidentally IS that tool (my 2 probes → comp-trace, an AE-favorite) and it HURTS when the correct answer is a different tool (cold-start comp-pii→comp-routes). So the measured +18.2 was affinity picking its favorite, not recovering intent.

**4. ~E's honesty was exemplary and is RAVC-validated.** ~E proactively self-flagged the contamination + the Goodhart concentration + the cold-start negative; my independent leave-out CONFIRMS every self-flag. This is the rare case of a builder surfacing the weakness in their own evidence — accepted as sound.

## Honesty-gate on ~E's 15 genuine tail labels: BLESSED (defensible)
All 15 map to correct/near-correct tools for genuinely oblique phrasings (comp-freshness×4, comp-pipescript×4, comp-pii×4, comp-validate×3). Labels are honest — softer than the fixture BY NATURE OF THE TAIL (the affinity-actable band is intrinsically narrow, N=9 scored/role). A minor note (non-blocking): the pipescript-labeled cases ("who depends on this output") admit comp-blast as a near-equivalent; widening wouldn't change the sign (those are neutral wrong→wrong at every role).

## Two separable findings (do NOT conflate with the flip decision)
- **SAFETY cert STANDS (independent, GREEN):** E1 structural gate holds in EVERY arm/role — affinity only reorders READ tools, 0 write_path surfaced. The flip is SAFE. It is simply not VALUE-JUSTIFIED yet.
- **Router-quality (affinity-independent):** base tail precision ~9-11% regardless of arm — the router is weak on oblique/vague phrasings. A separate router-quality item, not a flip blocker.

## Consequence for the record
Per CTO's gate, a mixed / role-dependent / cold-start-NEGATIVE sign is NOT robust-positive → **the value-flip is not authorized.** The 3 downstream (TH-C clause-B, COMPPROOF-C1 close, COMPLEARN-consumption) that were "unblocked on DRV-flip green" do NOT get a green flip here — they are gated on the w_h/affinity CALIBRATION pass (the separate pre-flip gate), not on this cert. The honest close of C1 basis-b: **affinity, as currently weighted, does not improve the ambiguous tail on merit; calibrate w_h before re-testing the sign.**

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_eval.py --tail` (my run) | reproduce ~E's tail sign role-sweep | PASS — AE +18.2/DS 0/CTO 0/cold −9.1, matches bb0eb2ca2 exactly |
| leave-out re-measure (15 genuine cases, my python) | strip my 2 contaminating probes; re-measure sign per role | AE +0.0 / DS +0.0 / CTO +0.0 / cold **−11.1** (1 away: comp-pii→comp-routes) |
| per-case direction decomposition (my run) | prove AE positive = 2 comp-trace changes = Goodhart | CONFIRMED — both my probes TOWARD comp-trace (AE-favorite); 0 genuine toward |

What worked: identifying that the corpus's AE-positive rested on cases I myself authored (CVO-contamination) and excluding them — the leave-out collapsed the positive to zero and exposed a cold-start NEGATIVE, turning a "small positive" into an honest HOLD. The Goodhart mechanism (affinity→role-favorite-tool) is now measured, not asserted. Gap: none — the sign is cleanly certified negative-on-merit; the flip correctly HOLDS for w_h calibration.

— 3.0.0_SA_CVO
