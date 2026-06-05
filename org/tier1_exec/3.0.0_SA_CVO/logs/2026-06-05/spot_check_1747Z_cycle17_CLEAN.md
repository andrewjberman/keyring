# /spot-check cycle 17 — CLEAN (MDLP I1+I2 deploying + FIND_DUALBIZ registration-watch)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1747Z · checkpoint acdc751f9 -> 67f15d8fa

8 non-CVO commits — MDLP_DISTFIX I1+I2 deployment + new FIND_DUALBIZ. No drift, no prod-shipped consumer artifact, no fix.
- **MDLP_DISTFIX I1+I2 deploying**: AE source-map register (67f15d8fa Rule-4) + event-gated producers on smartx-ingestion (d24e98545) + re-point per-firm (5f925adfd); DS per-firm built+validated "reconciles w/ Global to the cent" (d3251944a). Producers re-pointed+registered, still deploying -> VERIFY-ON-LAND at closeout.
  - **SHARP-TEST NOTE for the MDLP closeout-verify (Step 2.5 identity-masking)**: "reconciles to the cent" = aggregate-identity-masking class — a per-firm<->Global reconciliation can PASS internally-consistent while per-component values are wrong (residual absorption). Closeout-verify MUST check per-component plausibility (I1 cross-partner union MEMBERS + I2 per-firm freshness), NOT accept the reconciliation as correctness proof. Banked for closeout.
- **FIND_DUALBIZ** (NEW Andrew-direct): COO caught (2b12da95c) as unregistered + new-vs-FIND_INSURE-phase ambiguity, scope-routing before mis-frame registration. COO mid-decision, NOT drift. REGISTRY-row watch when it registers (recurring-pattern, COO 2-step adopted).
- LD-0157 impl (75ee3fc6a): triaged cycle 16; CVO loops left armed.
- FIND_DUALBIZ DS B1-PoC validated (69d3c93a5/5f925adfd): investigation, OUT-scope; substance plausible (disclosure-footer reverse-search, Ramer/Refined confirmed).

CLEAN — no findings, no fix. Checkpoint advances.
