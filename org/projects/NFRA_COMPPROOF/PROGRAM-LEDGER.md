# NFRA_COMPPROOF -- PROGRAM LEDGER (the ONE home)

**Owner:** 2.0.0_SA_COO~B (decomposition + coordination) | **Arch:** 1.0.0_SA_CTO
**PRD:** docs/architecture/NFRA_COMPPROOF_PRD.md (v1.0, 3d78e1f5b) | **B-harness arch:** docs/architecture/NFRA_COMPPROOF_B_HARNESS_DESIGN.md (1315f9a03)
**Thesis (PHASE-2):** when a real problem walks in, does the substrate SOLVE it -- and does the loop make itself smarter, on its own? B is the spine.
**Anti-drift self-consistency (binding):** ONE home (`org/modules/graph/compproof/` + this ledger), one owner, disjoint verbs -- the validator must not itself drift.
**STAFFING GUARD:** ~B (0.8.0_AE_CloudComp~B) is OFF-LIMITS (Andrew-direct -- it's the validation subject); staffed from ~A/~C/~D/~E + CVO~B/CVO.

## TO ROSTER

| TO | Workstream | Owner | Status | Gate / sequencing |
|---|---|---|---|---|
| **B1** | benchmark harness (corpus-loader+strip / blind-solver spawn / 3-axis scorer / gap-charters) | ~D build + CTO arch-lead | **DISPATCHED** | the SPINE, first (seeds C+D). Build to arch 1315f9a03. Isolation VOID-on-violation = HARD gate. |
| **B2** | blind-run scoring (independent judge, isolation-enforce) | CVO~B | **HELD** | after B1 delivers the harness + blind-runs |
| **A1** | seam+process spot-check sweep (breadth, keeps B honest) | CVO~B + COO~B-scoped (N=12 seams/4 procs) | **DISPATCHED** | concurrent on live; wave-close (GRAPHUNI/GRAPHDEPTH already closed) |
| **C1** | COMPROUTE efficacy eval (precision@1/recall, honesty-gate) | ~E + CVO honesty-gate | **HELD** | AFTER the default-router SHADOW-FLIP (else evals the superseded backstop) |
| **D1** | COMPLEARN autonomy audit | CVO~B | **DONE -- NOT-GREEN** (verdict ACCUMULATES-BUT-INERT, 736f6307f) | D2 stays FENCED; COMPLEARN fix-charter (roll-up below). COUPLING: the DRV default-router flip closes the loop. |
| **D2** | self-extension spike (auto-propose a tool spec) | DE under CTO | **FENCED** | behind D1-GREEN; PROPOSED-NOT-DEPLOYED; RV-0026 sovereign surface |

## ARCH-GATES (binding on every TO)
1. **BLIND-SOLVER ISOLATION = HARD gate** (author != solver != judge; VOID-on-violation; root-cause diff-gate). If weak, B voids.
2. **3-axis rubric:** REACH x USABILITY x GROUNDING-RESILIENCE (the success-shaped-but-wrong probe).
3. **Ground on LIVE/SERVED, never self-report or PRD Status:** -- could-not-verify is itself a finding.
4. **Do NOT invent incidents** -- top-20 capped corpus (5402f130b) only.
5. **D2 leash:** propose-not-deploy; CL-reactivation = SOVEREIGN surface, never self-authorized.

## SEQUENCING
`B1` first (seeds C's intent-set + D's gap-feed) -> `A1`/`D1` concurrent-now, `B2` after B1's blind-runs -> `C1` after the default-router flip -> `D2` behind D1-GREEN. All report into THIS ledger.

## GAP-CHARTER ROLL-UP (from B + A FAILs)
(populated as B/A land -- every MISS/PARTIAL + every A-FAIL charters here, feeding D)
- **COMPLEARN autonomy (D1, 2026-07-01, CVO~B verdict 736f6307f) = ACCUMULATES-BUT-INERT (NOT-GREEN)** -- the dead-ratchet-that-looks-alive. GROUNDED (live artifacts): producer deployed + EventBridge enabled BUT served tool_activity is single-vintage 06-30 (no autonomous 07-01 04:00Z refresh -- a manual seed); affinity-cache learned from a ONE-TIME 00:46Z batch, frozen since; 0/236 live routing decisions apply a learned affinity + 0/236 outcomes captured. **MECHANISM (grounded, not inferred):** the learned-affinity CONSUMER is the DEFAULT-ROUTER, which is NOT flipped (DRV pending) -- so the TRAINS->DECIDES feedback loop is STRUCTURALLY OPEN (accumulate works, consume isn't live). **FIX-CHARTER:** (a) confirm/fix the nightly autonomously refreshes (fresh vintage + ecs run-history); (b) close the flywheel -- capture live outcomes; (c) behavior-change activates when the DRV default-router flips to consume the affinity. **KEY COUPLING:** DRV-GREEN + closed-flywheel is what flips D1 to "learns" -- the Andrew-direct default-router flip is ALSO COMPLEARN's autonomy unlock. **D2 STAYS FENCED** until D1-GREEN.

## STATUS
2026-07-01: PRD landed (3d78e1f5b) + B-harness arch (1315f9a03); decomposed into the 6 TOs above; B1/A1/D1 dispatched, B2/C1/D2 held on their gates. Seed baseline = ~B's 4e9f0258d (VALIDATED_WITH_GAPS; its E1/E2 = the first MISS/PARTIAL).
