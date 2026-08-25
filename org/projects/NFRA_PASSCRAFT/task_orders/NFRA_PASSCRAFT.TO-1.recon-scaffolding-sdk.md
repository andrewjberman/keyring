<task_order>
<id>NFRA_PASSCRAFT.TO-1</id>
<title>P1 -- the recon-scaffolding SDK: the 8-move checklist + the 12-shape hunt-order taxonomy + the archetype->probe map as a versioned reference, PLUS `comp-passcraft recon <tool>` that runs ONLY the mechanical moves and emits an evidence pack -- and STOPS at the verdict door (AC1/AC4 anti-harness invariant)</title>
<issued_to>0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn (0.8.0_AE_CloudComp is UNREGISTERED). base-CTO consumes the reference immediately for his live hand-run pass (this scaffolds that pass, does not replace it).</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the single arch-gate pass before any GO)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_PASSCRAFT, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: pending</status>
<dispatch>DISPATCHED 2026-07-10 by 2.0.0_SA_COO~A -> 0.8.0_AE_CloudComp, on Andrew's DIRECT spawn release ("Unblock immediately"). CTO~A arch-gate PASS on the TO set @ 8dfcf1e75. Agent-queue pointer: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_PASSCRAFT.TO-1.recon-scaffolding-sdk.md. ROUTE EVERY BUILD DIFF back to 1.0.0_SA_CTO~A for the arch-gate before it is treated as landed (CTO~A gates diffs, not just the TO set).</dispatch>
<priority>P1 -- FOUNDATION of the whole program. Its `ToolAudit` emission (TO-2) is TOOLGRAPH's node/edge source; the reference is consumable by base-CTO's live pass the moment it lands. `.tools/comp-passcraft` is a NEW tool (not an edit to an enforcer), so it does NOT inherit the `.tools/**->BASE_EXEC` daylight hold (PRD sec.6) -- build may start on spawn without waiting on the hold.</priority>
<project>NFRA_PASSCRAFT</project>

<context>
The hand-run front pass broke in three characteristic ways on tool-1 (NFRA_TOOLPASS sec.4): it re-derives its opening moves each tool; its findings are prose no downstream consumer can read; its accuracy depends on the author correctly recognizing a claim's class. We have the doctrine (TOOLPASS) and a killed harness (COMPASSURANCE) but NO scaffolding between them. TO-1 builds the scaffolding: a versioned reference + a MECHANICAL recon helper. It equips the human; it does not judge.
</context>

<scope>
1. **The 8 fixed opening moves as a checklist, each with a falsifier per step** (PRD sec.3a): read both layers (wrapper+backend); MAP THE WRITE SURFACE before running (the move that would have caught tool-1's gate-disabling D9); find the cache/oracle (shared? poisonable? frozen-fixture-as-measure?); enumerate the target universe FROM SOURCE + print the denominator; pick branch-coverage targets whose membership is verified FROM THE TARGET (R3); pre-stage revert-safety off the mutated store; establish ground truth from a NON-SHARING instrument (the TOOLPASS sec.6 assurance-oracle exemption); classify archetype -> load its lead probes.
2. **The 12-shape failure taxonomy as a hunt-order** (PRD sec.3b), each shape -> one-line early probe -> archetype: guard-asymmetry; success-token-bound-to-wrong-step; aging-oracle; terminal-honest/artifact-lies; mislabelled-control-flow; test-writes-prod; restore-in-finally; skip-on-missing-field; resource-blind; undiscriminating/constant-gate; vacuous-that-can-block; correct-but-unwired. Each probe EXPOSES A SMELL only; the verdict stays a hand-run paired test + falsifier.
3. **The archetype -> lead-probe map** (which probes to lead with per cluster).
4. **`comp-passcraft recon <tool>`** -- runs the MECHANICAL moves (read layers, grep the write surface, enumerate the universe, print denominators, slot ground-truth-per-target, emit branch-membership proofs) and emits an **evidence pack**. It STOPS AT THE VERDICT DOOR. It has NO verdict engine.
</scope>

<locked_invariants note="CTO~A arch-gate checks these -- non-negotiable">
  1. **THE ANTI-HARNESS INVARIANT (load-bearing, PRD sec.0):** PASSCRAFT templates the SCAFFOLDING -- recon, revert-safety, evidence capture, hunt-order, and the emission SCHEMA -- and NOTHING ELSE. The verdict stays hand-run. No component in this TO may compute a pass/fail. If a component reads like a harness, it is WRONG. A harness must encode the right answer to judge an output; if the right answer is computable it is a second implementation, and two implementations that agree may share a predicate (comp_route.py:761-766 passed forever seeded with a string that never reached the broken branch).
  2. **rc-check on every evidence command** (PRD sec.3c): a non-zero rc is `INVOCATION-ERROR`, not a verdict -- a failed read is not a negative observation.
  3. **self-write-surface only:** the recon session maps its OWN write surface; the front pass is READ-ONLY on the estate and touches no shared/other-agent state.
  4. **BOUNDARY (sovereign):** no bd / 49F / Schwab / opal-data-bd read or target. comp-blast's cache carries bd-backed nodes -- NAMES ONLY, never the data.
</locked_invariants>

<acceptance_criteria>
  - **AC1 (anti-harness, EXERCISED):** run `comp-passcraft recon <tool>` on a tool; the output contains an evidence pack and ZERO pass/fail verdict.
  - **AC4 (the mutant-kill on PASSCRAFT itself):** inject a tool with a KNOWN-DEFECTIVE verdict; PASSCRAFT must NOT auto-flag it (it has no verdict engine) AND must surface the archetype's lead probes that WOULD expose it. Shows the sec.0 line held.
  - **AC5 (class-agnostic):** the taxonomy + reference are cloud/language-neutral (the 12 shapes are structural, not Opal facts); demonstrate by tagging one non-comp scanner.
  - Session-log Compiler Tools section reproduces every recon run with observed output.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_PASSCRAFT_PRD.md @ 362272cce</ref>
  <ref type="doctrine">NFRA_TOOLPASS (CVO-owned) -- the front-pass doctrine + rail set; sec.0 anti-harness, sec.4 tool-1 failure classes, sec.6 assurance-oracle exemption</ref>
  <ref type="contract">NFRA_CSE -- the emission contract TO-2 conforms to</ref>
  <ref type="feeds">NFRA_TOOLGRAPH (TO-2's ToolAudit stream is its node/edge source)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>New `.tools/comp-passcraft` tool + a versioned reference doc. Read-only on the estate. No served artifact, pipeline, or producer.</no_reprocess_needed></data_reprocess_scope>
</task_order>
