# /spot-check cycle 18 — CLOSURE 2-STEP DRIFT (INFMVP + KEEPWARM) routed P2 + MDLP/MDPF verify-on-land

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1807Z · checkpoint 77e97eec4 -> 99959bbfb

## FINDING (P2, routed to CTO+COO) — closure 2-step incomplete on 2 closes
CTO close commit `99959bbfb` (Andrew-direct ruling) flipped ADVI_INFMVP + ADHC_KEEPWARM JSON status=complete but left the Closure Discipline 2-step INCOMPLETE on both:
| Project | JSON status | JSON completed | REGISTRY row | Gap |
|---|---|---|---|---|
| ADVI_INFMVP | complete | **MISSING** | still in **Active** (L29, in-progress narrative) | +completed date; move Active->Completed |
| ADHC_KEEPWARM | complete | **MISSING** | still in **Active** (L23, in-progress narrative) | +completed date; move Active->Completed |
- This is the JSON-flipped-but-REGISTRY-lags drift the Closure Discipline exists to catch (ADVI_ROLGAT f959fbcb precedent lagged days uncaught).
- **Disposition = ROUTE not FIX:** project-CLOSURE 2-step (Active->Completed move + completed-date + ship-evidence closure-notes) is closure-AUTHORSHIP (CTO/COO lane), distinct from my fix-scope (REGISTRY row drift / Blocking-column propagation). On a lane boundary the verifier surfaces, not authors. P2 (substantively closed + CVO-validated, metadata-incomplete not a blocker).
- Ship evidence for the Completed-table notes (from the ruling, for CTO/COO): INFMVP = all F1-F5 CVO-validated + Andrew smoke (F4b non-blocking follow-on); KEEPWARM = backend verified + FE PROD-live + CVO v2.1.114 warm-ping-on-PROD e2e-warm-smoke satisfied (that last is MY surface-3 verify = the close evidence).
- CLASS NOTE: same 2-step-drift family as the registration drift (COO already fixing structurally w/ register-helper) — recommend the close-flow get the same atomic JSON+REGISTRY treatment.

## Verify-on-land / nightly (queued, no action now)
- **MDLP_DISTFIX I1+I2 smartx deploy COMPLETE** (a3ad9a933): "Global 7301/$1.492B + per-firm reconcile to cent, daily 11:30Z live." VERIFY-ON-LAND when served account_distribution.json refreshes. SUBSTANCE DELTA to sense-check: deploy 7301/$1.492B vs PRD I1 estimate ~7427/$1.516B = ~126 accts/~$24M lower — verify whether legit (live-feed vs estimate / daily movement) or partial-union, at the served artifact. + the identity-masking guard (cycle 17): check per-component members, not just the to-cent reconcile.
- MDPF_COUNTS FIX deployed Parts 1+2+3 (6ac537655, mdpf-daily-runner, C1-validates-nightly): verify-on-nightly.
- FIND_DUALBIZ pipeline codified (e3d4337f1): investigation/build OUT-scope; COO still mid-registration (cycle 17 watch).

## Verdict
1 finding routed (closure 2-step drift -> CTO+COO P2); 2 verify-on-land queued (MDLP deploy w/ substance-delta + identity-masking guard; MDPF nightly). Checkpoint advances.
