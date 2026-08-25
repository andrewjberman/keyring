<task_order>
<id>NFRA_PASSCRAFT.TO-2</id>
<title>P2 -- the `ToolAudit` CSE schema + emitter (NFRA_CSE-conformant), wire the front-pass recon to emit it, and fold the accuracy fixes into the checklist (R0 ONLY IF CVO rules it lands -- TO-R0)</title>
<issued_to>0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn. Sequences behind TO-1 (the recon helper it wires the emitter into).</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_PASSCRAFT, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: pending</status>
<dispatch>DISPATCHED 2026-07-10 by 2.0.0_SA_COO~A -> 0.8.0_AE_CloudComp, on the PASSCRAFT-TO-1 + TOOLGRAPH-TO-1 landing (15c8524a4, CTO~A arch-gate PASS). Agent-queue pointer: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_PASSCRAFT.TO-2.toolaudit-cse-schema-emitter.md. TO-2 does NOT gate on R0 -- build the emitter; the OPTIONAL R0 fold is DEFERRED (TO-R0 is HELD off CVO's lane -- do NOT route it, do NOT assume R0 lands). Route diffs to 1.0.0_SA_CTO~A.</dispatch>
<priority>P2 -- sequences behind TO-1; its output (the ToolAudit CSE stream) is what TOOLGRAPH.TO-2 (the Assurance plane) reads. The emitter is provenance-carrying; the schema is the envelope, never the judgment.</priority>
<project>NFRA_PASSCRAFT</project>

<context>
TO-1's recon emits an evidence pack in prose-adjacent form. TO-2 gives it a MACHINE-READABLE, provenance-carrying envelope so a hand-run pass FEEDS the graph (a ToolAudit CSE per tool) instead of evaporating. The envelope templates the SHAPE, never the VALUE -- a ToolAudit in a structured envelope is still a hand-authored judgment.
</context>

<scope>
1. **The `ToolAudit` CSE schema** (PRD sec.3d): `{tool, archetype, shared_substrate[], domain, susceptible_to[], axis:{mechanical,declarative,semantic}, rail:{R1..R7}, verdict, class, evidence_ref, falsifier, oracle, vintage}` -- NFRA_CSE-conformant, provenance-carrying, decompressing to its cited evidence (the comp-ladder fidelity gate).
2. **The emitter:** wire the TO-1 front-pass recon to emit a valid ToolAudit CSE per pass. The `verdict`/`class` fields are HAND-AUTHORED inputs to the envelope -- the emitter serializes them, it does NOT compute them (anti-harness invariant holds one layer up).
3. **base-CTO's continuous coordinates:** his front-pass recon emits `archetype` + `shared_substrate` + `domain` continuously going forward (PRD sec.3d, his sec.5 proposal, Andrew-confirmed) so every future tool feeds its C0/C1/C2 coordinates at pass-time.
4. **The accuracy fixes folded into the checklist** (PRD sec.3c): rc-check-on-every-evidence-command (INVOCATION-ERROR != verdict); self-write-surface. **R0 is DEFERRED to TO-R0 (CVO ruling) -- this TO MUST NOT assume R0 lands; treat it as a PROPOSED rail. If CVO rules R0 in, fold the QUESTION-class tag into the emitter; if CVO rules R1-read-it-correctly, do not.**
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **ANTI-HARNESS (PRD sec.0):** the emitter serializes a hand-authored verdict; it has NO verdict engine. The schema is the envelope, never the judgment.
  2. **FIDELITY:** a ToolAudit CSE must decompress to its cited evidence (comp-ladder fidelity gate) -- an envelope that cannot reproduce its evidence_ref is invalid.
  3. **R0 = PROPOSED, not assumed** (see scope 4). CVO owns the ruling (TO-R0).
  4. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target; names only.
</locked_invariants>

<acceptance_criteria>
  - **AC2 (fidelity):** a hand-run pass emits a valid ToolAudit CSE that decompresses to its cited evidence (comp-ladder fidelity gate).
  - **AC3 (R0 IF-LANDED, exercised):** if CVO rules R0 in, the recon helper class-tags its own output -- a DYNAMIC claim it cannot answer from source is emitted `INFERRED`/`NOT-CHECKED`, never `OBSERVED`. (If CVO rules R0 out, AC3 is satisfied by R1's existing self-classification; record which.)
  - The emitter is NFRA_CSE-conformant (schema-validated on emit).
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_PASSCRAFT_PRD.md @ 362272cce (sec.3c accuracy fixes, sec.3d the CSE)</ref>
  <ref type="contract">NFRA_CSE -- the emission contract (schema conformance + provenance)</ref>
  <ref type="gate">NFRA_PASSCRAFT.TO-R0 (CVO R0 ruling) -- hard dependency for the R0 fold ONLY; the rest of TO-2 does not gate on it</ref>
  <ref type="feeds">NFRA_TOOLGRAPH.TO-2 (Assurance plane reads the ToolAudit stream)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Schema + emitter wired into the new comp-passcraft tool. Read-only on the estate.</no_reprocess_needed></data_reprocess_scope>
</task_order>
