<task_order>
<id>NFRA_PASSCRAFT.TO-3</id>
<title>P3 -- backfill the 3 completed tool-passes (comp-portal-thread, comp-aws, comp-blast) as `ToolAudit` CSEs to seed NFRA_TOOLGRAPH's node set</title>
<issued_to>0.8.0_AE_CloudComp (build, emitting the CSEs) with base-CTO consult (he ran the 3 hand passes; the verdict fields are his authored judgments, transcribed not recomputed). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn + TO-2 (the emitter must exist).</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_PASSCRAFT, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: staged</status>
<priority>P3 -- sequences behind TO-2 (needs the emitter). Immediately valuable: it seeds TOOLGRAPH.TO-1's node set with 3 REAL, evidence-carrying tool-nodes (comp-aws + comp-blast are two of the hardest already-audited tools).</priority>
<project>NFRA_PASSCRAFT</project>

<context>
Three tool-passes are already complete as prose (comp-portal-thread, comp-aws, comp-blast). Backfilling them as ToolAudit CSEs converts evaporated hand-work into the first three graph nodes -- the seed corpus TOOLGRAPH's node set is built on. This is TRANSCRIPTION of existing hand-authored verdicts into the envelope, NOT a re-audit.
</context>

<scope>
1. For each of the 3 completed passes, emit a valid `ToolAudit` CSE (via TO-2's emitter) carrying the pass's already-authored verdict, class, axis findings, rail results, evidence_ref, falsifier, oracle, and vintage.
2. Each CSE must decompress to the ORIGINAL pass's cited evidence (fidelity gate) -- if it cannot, the original evidence_ref was under-specified; surface that as a finding, do not fabricate.
3. Hand the 3 seeded CSEs to TOOLGRAPH.TO-1 as its node seed.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **TRANSCRIPTION, not re-audit:** the verdict fields are base-CTO's authored judgments transcribed into the envelope. No new verdict is computed (anti-harness).
  2. **FIDELITY:** each backfilled CSE decompresses to the original pass's evidence; a CSE that cannot is INVALID (surface, don't fabricate).
  3. **BOUNDARY (sovereign):** comp-blast's cache carries bd-backed nodes -- backfill the tool-PASS of comp-blast (names/structure only), NEVER the bd data behind it.
</locked_invariants>

<acceptance_criteria>
  - 3 valid ToolAudit CSEs emitted, each fidelity-decompressing to its source pass's evidence.
  - The 3 CSEs are consumed by TOOLGRAPH.TO-1 as the node seed (hand-off verified).
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_PASSCRAFT_PRD.md @ 362272cce (sec.4 P3)</ref>
  <ref type="dependency">NFRA_PASSCRAFT.TO-2 (the emitter) -- hard prerequisite</ref>
  <ref type="feeds">NFRA_TOOLGRAPH.TO-1 (node seed)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Transcription of 3 existing hand passes into CSEs. Read-only on the estate.</no_reprocess_needed></data_reprocess_scope>
</task_order>
