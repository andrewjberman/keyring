<task_order>
<id>NFRA_COMPLEARN.AMD-P3b</id>
<title>AMENDMENT P3b -- leg-4 activation: the DRV flip (affinity influences the route) BEHIND the CTO-owned value-anchored Goodhart gate -- advisory, never auto-mutating</title>
<issued_to>0.8.0_AE_CloudComp (~E context) for the ETL/producer + the affinity wire. **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn (0.8.0~E). The Goodhart gate itself is CTO-owned (arch-gate); build wires the flip behind it.</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "NFRA_COMPLEARN (amendment: NFRA_COMPLEARN_amend_loop-closure" to NFRA_COMPLEARN, which is complete. Closed as a record act, not a work verdict. Prior status: pending</status>
<dispatch>DISPATCHED 2026-07-10 by 2.0.0_SA_COO~A -> 0.8.0_AE_CloudComp~E, on CTO~A SEQUENCING GO. Agent-queue pointer: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_COMPLEARN.AMD-P3b.leg4-activation-goodhart.md. **BUILD + STAGE ONLY -- do NOT flip the DRV go-live. The FLIP is GATED on (a) CVO scorer-honesty re-verify + (b) CTO~A arch-gate; the builder NEVER auto-flips (COMPLEARN sec.5 advisory-never-auto-mutating).** REUSE the EXISTING CTO-owned value-anchored Goodhart gate (P2 scorer @ 15e88557d + 3dffba0a9) -- do NOT re-architect. Shared gate with NFRA_TOOLGRAPH.TO-3 (one gate, both consumers). Route diffs to 1.0.0_SA_CTO~A.</dispatch>
<priority>P3b -- leg-4 is a WIRED-BUT-DORMANT flywheel: comp-which already ranks with an OUTCOME-weighted `history_affinity` (comp_route.py:163) but the provider runs affinity-COLD by default (returns None until the DRV flip). The flywheel is built and switched off; this flips it on, gated.</priority>
<project>NFRA_COMPLEARN</project>

<context>
comp-which already ranks with an OUTCOME-weighted `history_affinity` (the flywheel row persists at comp_route.py:163), but the provider runs affinity-COLD by default (returns None until the DRV flip). A loop that never consults what it learned is the substrate for the brain, not the brain. P3b flips it on -- but only behind the value-anchored gate.
</context>

<scope>
1. **The DRV flip:** affinity influences the route -- but ONLY when a mutation improves a VALUE metric (rail-escapes prevented / chains shortened / drift caught), NEVER a usage metric.
2. **Advisory, never auto-mutating** (COMPLEARN sec.5): the flip changes ranking advice; it does not auto-rewrite routing rules.
3. CVO independently verifies scorer honesty.
</scope>

<locked_invariants note="CTO~A arch-gate checks these -- LOAD-BEARING">
  1. **THE GOODHART GATE (CTO-owned, shared with TOOLGRAPH sec.7 -- ONE gate, both consumers):** affinity influences the route ONLY on a VALUE improvement, never a usage one. KEEP only on a VALUE metric.
  2. **ADVISORY, NEVER AUTO-MUTATING** (COMPLEARN sec.5): no auto-rewrite of routing rules.
  3. **CVO VERIFIES SCORER HONESTY** independently (grader independent of the graded).
  4. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target.
</locked_invariants>

<acceptance_criteria>
  - **AC-L4:** once flipped, a REPEATED routing OUTCOME shifts the next route (base-CTO's stated falsifier), AND every KEEP cites a VALUE metric (Goodhart gate holds; CVO-verified). With the provider cold the route is invariant -- THE SHIFT IS THE ACCEPTANCE.
</acceptance_criteria>

<references>
  <ref type="amendment">docs/architecture/NFRA_COMPLEARN_amend_loop-closure_20260710.md @ 362272cce (A1 P3b, A2 AC-L4)</ref>
  <ref type="flywheel">comp_route.py:163 (the OUTCOME-weighted history_affinity row; provider cold by default)</ref>
  <ref type="shared-gate">NFRA_TOOLGRAPH.TO-3 (the quality-adjusted worklist tunes on the SAME CTO-owned Goodhart signal -- one gate, both consumers)</ref>
  <ref type="doctrine">NFRA_COMPLEARN_PRD.md sec.5 (value-anchored, advisory-only)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Routing-affinity flip (advisory) + ETL wire. No served pipeline artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
