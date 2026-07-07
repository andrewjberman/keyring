# CVO~B TH-C clause-B close-loop cert — **PASS (causal chain + neg control independently verified).** NFRA_TOOLHEALTH closes. + TSGRAPH override exercised PASS.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0910–0918Z
**Subject (independently exercised):** `clause_b_close_loop_exercise.py` (~D `08266a3ea`) on the LIVE comp_route engine + real capability provider, role=AE — built to my COMPPROOF-D1 scope ruling (w_s vehicle; causal-chain-not-coincidence). Blind re-run + my OWN causal-isolation probes. Governed by my ruling that the w_s(surface_prior) delta counts for clause-B (it's TH-C's own PROMOTE mechanism).

## VERDICT: **PASS — the close-the-loop is PROVEN.** A health verdict demonstrably changes live routing, attributable solely to its commission. NFRA_TOOLHEALTH closes (clause-A + clause-B both verified).

### The causal chain — each link independently verified (not the exercise's self-reported TRUE)
1. **VERDICT:** comp-depth → PROMOTE (the real comp_tool_health_gate classifier). ✓
2. **COMMISSION:** comproute-route-proposal, knob = `comp_route.surface_prior` (the w_s term) — TH-C's OWN promote mechanism (I verified this in the clause-A self-test: `promote → surface_prior_bump`). ✓
3. **APPLY:** surface_prior += 0.9 on affinity_key **TRINO** — and I INDEPENDENTLY confirmed `comp-depth.affinity_key == 'TRINO'`, so the bump correctly targets comp-depth's prior (not a mismatch). comp-depth prior 0.3 → 1.0. ✓
4. **FLIP:** top-1 → comp-depth, comp-depth rank 6 → 0. And I INDEPENDENTLY confirmed the PRE baseline: routing "how deep is the dependency chain" at role=AE puts **comp-depth at rank-6 (NOT top-1)** — so the flip to rank-0 is a GENUINE change, not a pre-existing top-1. ✓
5. **NEGATIVE CONTROL:** without the effective seed → comp-depth verdict = RETIRE → emits no route-altering commission → no bump → no flip. `control_holds = True`. The flip is CONTINGENT on the PROMOTE verdict. ✓
6. **ISOLATION:** role/intent/engine identical PRE vs POST; single-cap bump — only comp-depth's prior changed (0.3→1.0). The delta is attributable SOLELY to the commission.

`caused_by_commission = (verdict_ok AND w_s_vehicle AND route_delta AND control_holds) = TRUE`. Close-loop proven.

### Clause-A (cross-reference, blind-verifiable)
comp_tool_health_gate.py --self-test = 11/11 (I ran it earlier this session): advisory / zero auto-mutation / value-anchored / 3-axis grounding. Clause-A DISPATCH honesty stands.

### Honest scope / disclosed dependency (accepted, ~D transparent)
- The VERDICT's `EFFECTIVE=True` input is SEEDED via the proven seam because TH-A's live effectiveness feed isn't joined yet. The classifier + commission + bump + flip are all REAL and exercised; only one INPUT (effectiveness) to the classifier is seeded. So the close-loop MECHANISM is proven end-to-end; when TH-A's live feed joins, the same proven mechanism fires on live effectiveness. TH-A live-join is a tracked follow-on, NOT a clause-B blocker (clause-B proves the loop closes; TH-A makes the verdict live-driven). Disclosed by ~D, accepted.
- Minor observation (transparency, non-material): my independent baseline top-1 was comp-freshness vs the exercise's comp-chainrun — both place comp-depth at rank-6, so the causal claim (6→0 on the bump) holds; the displaced-cap identity varies with near-tie disambiguation context. Not a finding.
- Scope honored: D1's affinity-inertness (0/236 learned-affinity, 736f6307f) stays explicitly OUT of clause-B — it's COMPLEARN's separate flywheel concern (w_h), per my ruling. Clause-B is the w_s loop.

## Disposition
TH-C clause-A (DISPATCH honesty, 11/11) + clause-B (close-the-loop causal chain + neg control, verified) both PASS → **NFRA_TOOLHEALTH closes** on this cert. The health verdict demonstrably changes live routing via TH-C's own w_s mechanism, contingent on the verdict (neg control). TH-A live-feed join tracked as the follow-on that makes the verdict input live.

### Also this turn: TSGRAPH override exercised PASS (closes the residual on cert b4ffd39)
The TSGRAPH override escape-hatch (killed mid-run earlier) re-ran to completion: perturbed baseline + `COMP_DETECT_GATE_OVERRIDE` → **rc=0** + "OVERRIDE: fold gate bypassed (audited)" + `org/mcp/comp-detect-gate-override.log` grew (2→3 lines, recording the exact D1 finding + reason). Baseline restored (git clean). So the TSGRAPH cert's one code-grounded-only residual (override) is now EXERCISED — all three enforcement properties (block / fail-open / audited-override) are confirmed.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `clause_b_close_loop_exercise.py --json` (blind re-run, my run) | reproduce the verdict→w_s→flip chain + neg control | caused_by_commission=TRUE; control_holds=TRUE |
| `comp-depth.affinity_key` + baseline route (my python) | independent causal check: bump targets comp-depth; PRE not-already-top1 | key='TRINO' (correct target); comp-depth baseline rank-6 (genuine flip) |
| `comp_tool_health_gate.py --self-test` (earlier) | clause-A honesty | 11/11 |
| override re-run (bhhj9thw6) | exercise the TSGRAPH audited-override | rc=0 + OVERRIDE + audit-log grew; baseline restored |

What worked: independently grounding whether the bump targeted the RIGHT cap (comp-depth.affinity_key='TRINO' — verified, not a coincidental mislabel) and whether the PRE state was genuine (comp-depth rank-6, not already top-1) — so the close-loop flip is real, not staged. Accepted the disclosed EFFECTIVE-seed dependency honestly (mechanism proven; TH-A live-join tracked). Gap: none blocking — TOOLHEALTH closes; TH-A live-feed join is the tracked follow-on for a live-driven verdict.

— 3.0.0_SA_CVO
