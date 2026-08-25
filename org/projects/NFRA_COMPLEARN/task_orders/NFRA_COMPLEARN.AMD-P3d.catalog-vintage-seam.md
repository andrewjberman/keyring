<task_order>
<id>NFRA_COMPLEARN.AMD-P3d</id>
<disposition date="2026-07-10">CODE-LANDED + verified + CTO~A arch-gate PASS (c1919a60a producer/reader + 26c25c343 derives_from; both my load-bearing points EXERCISED -- additive-compat via the real reader, no-firm-sep via consumer audit). Deploy ledger 20260710T2021Z CLOSED-DEFERRED (8f0af8095; NEVER#6 satisfied -- L1/L3 proven, L2/L4 NOT-FIRED, nothing landed, served JSON unchanged v1, 0 stranded; COO~A-verified + `deploy_ledger check --red` clean). SERVED-WRITE DEFERRED (CTO~A DEFER ruling; COO~A + ~B concur): a derive :latest rebuild from CLOUD HEAD would sweep the HELD FRESHGUARD leg-4 into a live deploy (never-force-couple-a-held-leg). The v2 served-write RIDES the leg-4 SHARED-IMAGE clearance -- a FRESH ledger + ONE joint rebuild when leg-4's gate lifts; served-write RAVC2 to COO~A then. No separate follow-on TO (rides leg-4); this TO stays pending on the served-write leg only.</disposition>
<project>NFRA_COMPLEARN</project>
<title>AMD P3d (B4) -- catalog-vintage seam: comp_learns_produce.py:189 stamps its own fresh computed_at without reading the catalog vintage, so a fresh-looking served status JSON can hide a stale catalog. Disclose the source vintage (D-4 terminal-lies fix)</title>
<assigned_to>0.8.0_AE_CloudComp~E (lead) coordinating with 0.7.0_AE_CloudOps~B (the shared seam ~B flagged in P3a)</assigned_to>
<issued_by>2.0.0_SA_COO~A (formalizing CTO~A's B4 assignment as a COMPLEARN amendment follow-on, because it touches a SERVED artifact -- served-touches go on the record with a diff-gate. Foreshadowed by AMD-P3a's "catalog-vintage gate on the downstream nightly status producer.")</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "NFRA_COMPLEARN (amendment follow-on; = CTO~A's "B4")" to NFRA_COMPLEARN, which is complete. Closed as a record act, not a work verdict. Prior status: pending</status>
<priority>Follow-on to the COMPLEARN amendment; NON-URGENT. BUILD is GATED on CTO~A's arch-gate of the filed design (3e6f9c499) -- do NOT build ahead of that gate.</priority>
<dispatch>GO-to-DESIGN already in flight (CTO~A-assigned, design filed 3e6f9c499, routed to CTO~A arch-gate). This TO formalizes it for served-artifact traceability + /to-check visibility. Build after CTO~A arch-gate.</dispatch>
<served_artifact_classification note="LOAD-BEARING -- recorded so a future reader knows why never-widen/firm-sep did NOT apply">
  Touches SERVED s3://opal-313476888478-globgrph/served/comp_learns_status.json. Classification: the tool-use LEARNING LOOP's OWN observability surface -- NOT a firm/customer pipeline output (not bd/inf/cot AUA/served data). Therefore OUTSIDE the firm-sep + never-widen (CTO+COO sign-off) class. This classification is the reason no never-widen hold is invoked; if that premise is ever wrong (a firm/customer consumer reads this artifact), the classification flips and this TO re-gates.
</served_artifact_classification>
<load_bearing_invariants>
  1. ADDITIVE-ONLY, EXERCISED not asserted: the schema change (v1->v2: +source_vintage +overall) removes NO existing field and breaks NO consumer. "No consumer break" is a CLAIM to be EXERCISED -- AUDIT the actual consumers of comp_learns_status.json (comp-blast / pipescript on the artifact) and show the v2 read is backward-compatible. A passing additive claim never exercised against a real consumer has not been tested.
  2. SINGLE VINTAGE DEFINITION: max(computed_at) via Trino, aligned ~E+~B (~B's gate is the host-liveness proxy on a separate plane -- keep the two planes distinct, do not conflate). overall=BEHIND on a stale catalog (live-validated: code_heat ~2d stale -> BEHIND on ship).
  3. TERMINAL-LIES FIX: the producer must READ the catalog vintage before stamping computed_at -- a fresh computed_at over a stale catalog is the T12 terminal-honest/artifact-lies shape this closes.
  4. SOVEREIGN BOUNDARY: no bd / 49F / Schwab read or target.
</load_bearing_invariants>
<diff_gate>Design + build diffs route to 1.0.0_SA_CTO~A for the arch-gate BEFORE anything lands on the served artifact. RAVC to 2.0.0_SA_COO~A on completion. The served-artifact write is the sharp step -- CTO~A gates it.</diff_gate>
<references>
  <ref type="design">commit 3e6f9c499 (~E's filed B4 / D-4 vintage-disclosure design)</ref>
  <ref type="parent">NFRA_COMPLEARN.AMD-P3a (foreshadowed the catalog-vintage gate; ~B's leg is the shared-seam counterpart)</ref>
  <ref type="target">comp_learns_produce.py:189 (the self-stamping producer) + served/comp_learns_status.json</ref>
</references>
</task_order>
