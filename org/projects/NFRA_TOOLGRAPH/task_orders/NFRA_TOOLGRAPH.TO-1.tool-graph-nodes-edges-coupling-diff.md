<task_order>
<id>NFRA_TOOLGRAPH.TO-1</id>
<title>P1 -- the tool graph: the tracked node table (at a COMMITTED census path, LEAD-1) + the mechanical SHARES_SUBSTRATE / WRITES / INVOKED_BY edge computation + the declared-vs-actual coupling diff that SEEDS a known undeclared edge</title>
<issued_to>0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn. **MEASURE-ONLY -- starts on spawn, NOT behind the `.tools/**->BASE_EXEC` daylight hold** (imports-grep + coupling diff are read-only; nothing here edits an enforcer).</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_TOOLGRAPH, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: pending</status>
<dispatch>DISPATCHED 2026-07-10 by 2.0.0_SA_COO~A -> 0.8.0_AE_CloudComp, on Andrew's DIRECT spawn release ("Unblock immediately"). CTO~A arch-gate PASS on the TO set @ 8dfcf1e75. Agent-queue pointer: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_TOOLGRAPH.TO-1.tool-graph-nodes-edges-coupling-diff.md. Runs IN PARALLEL with PASSCRAFT-TO-1 (needs no ToolAudit). ROUTE EVERY BUILD DIFF back to 1.0.0_SA_CTO~A for the arch-gate before it is treated as landed.</dispatch>
<priority>P1 -- immediately useful (the real scanner-ripple map) BEFORE any assurance wiring. Standalone: needs no ToolAudit, so it can run IN PARALLEL with PASSCRAFT-P1. The declared-vs-actual coupling diff is the load-bearing move (the hidden ripple `comp-coverage-map.yaml` exists to catch).</priority>
<project>NFRA_TOOLGRAPH</project>

<context>
The comp-tools are nodes in the same C0-C3 SEMCTL ontology at the DEPTH grain "scanner" -- the brain's own sensory organs as nodes the brain can reason about. The scanner-coupling graph (a trace_graph fix ripples to 5 tools) is recomputed by hand today and exists as NO artifact. TO-1 makes it a first-class, mechanically-computed graph.
</context>

<scope>
1. **C0 -- the node set.** The tracked tool census, seeded by PASSCRAFT.TO-3's 3 backfilled CSEs. **LEAD-1 (folded here per CTO~A mandate): the census MUST live at a COMMITTED, version-controlled path.** The current `scratchpad/comp_tool_census.py` citation is gitignored + absent -- a citation-without-a-vintage; relocate it to a committed path and cite `file:line @ commit-ish`. Each tool-node carries on-disk / registration / description-source / `archetype` / `domain` / `susceptible_to[]` (from PASSCRAFT).
2. **C1 -- the edges.** `SHARES_SUBSTRATE` via a MECHANICAL imports-grep across all backends; `WRITES` (tool -> the marker/manifest/cache it mutates); `INVOKED_BY` (tool -> its gate/hook/CI wiring, or `UNWIRED`).
3. **THE LOAD-BEARING MOVE -- the declared-vs-actual coupling diff:** diff the DECLARED coupling (`comp-coverage-map.yaml` overlap groups) against the ACTUAL import graph. An UNDECLARED shared backend is the finding.
4. **C2 -- archetype clusters:** nodes sharing a substrate share a failure mode (the PASSCRAFT taxonomy); the cluster predicts which probes to lead with.
5. **AC0 denominator reconciliation (from NFRA_TOOLCHECK AC-0, folded):** the tool census carries ONE reconciled denominator with its derivation, not the five unreconciled numbers (67 disk / 40 matrix / 29 yaml / ~41 manifest / "~55" described). Print the denominator of the node set.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **THE COUPLING-DIFF GATE MUST BE SHOWN ABLE TO GO RED:** seed a KNOWN undeclared edge and prove the diff flags it. A gate that only passes on the current tree has NOT been shown able to fire (AC1).
  2. **COMMITTED CENSUS PATH (LEAD-1):** no gitignored/scratchpad citation; the node table lives at a version-controlled path with a vintage.
  3. **MEASURE-ONLY, no enforcer edit:** TO-1 computes + reads; it does not edit `.tools/`. It is NOT gated on the daylight hold.
  4. **BOUNDARY (sovereign):** comp-blast's cache carries bd-backed nodes -- node NAMES/edges only, never the bd data.
</locked_invariants>

<acceptance_criteria>
  - **AC1:** the coupling diff reproduces EVERY declared overlap group AND flags a SEEDED undeclared shared backend (the go-red proof).
  - **AC6 (class-agnostic):** the node/edge model admits a non-comp scanner (a future org recognizer) with no schema fork.
  - The node census lives at a committed path with a reconciled, printed denominator.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_TOOLGRAPH_PRD.md @ 362272cce (sec.3 C0/C1/C2, sec.4 P1, sec.5 AC1/AC6, LEAD-1)</ref>
  <ref type="ontology">NFRA_SEMCTL C0-C3 (the scanner-grain node model)</ref>
  <ref type="node-seed">NFRA_PASSCRAFT.TO-3 (the 3 backfilled ToolAudit CSEs seed the node set)</ref>
  <ref type="declared-coupling">org/modules/graph/comp-coverage-map.yaml (the DECLARED overlap groups the diff tests against)</ref>
  <ref type="denominator">NFRA_TOOLCHECK AC-0 (the five-number denominator to reconcile)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Read-only graph computation (imports-grep + coupling diff) + a committed census table. No enforcer edit, no served artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
