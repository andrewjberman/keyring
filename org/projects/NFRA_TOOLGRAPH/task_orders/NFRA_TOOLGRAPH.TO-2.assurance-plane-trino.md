<task_order>
<id>NFRA_TOOLGRAPH.TO-2</id>
<title>P2 -- the Assurance plane: land the `ToolAudit` verdicts + the standing COMPASSURANCE matrix (R1-R7 x layer) as Trino-queryable, vintage-stamped state -- as EVIDENCE, Deny-fenced from mutating the graph (the FEDOBS boundary)</title>
<issued_to>0.8.0_AE_CloudComp (build: graph/federation). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn + PASSCRAFT.TO-2 (the ToolAudit source must exist). **MEASURE/READ side starts now; the plane WRITES as evidence only -- see the Deny-fence invariant.**</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_TOOLGRAPH, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: staged</status>
<priority>P2 -- sequences behind PASSCRAFT-P2 (needs the ToolAudit stream). The plane is a 4th federation plane (or quality columns on `tool_activity` keyed by tool), read by TO-3's quality-sensor wire + quality-adjusted JOIN.</priority>
<project>NFRA_TOOLGRAPH</project>

<context>
The fabric already reserves two places for a tool-quality verdict (comp_tool_health's EFFECTIVE axis + PROMOTE's gate) but nothing writes assurance into them. The Assurance plane makes the ToolAudit verdicts + the COMPASSURANCE matrix (R1-R7 x layer, PROVEN/DEFECT/UNKNOWN) Trino-queryable, vintage-stamped like `code_heat`. It is EVIDENCE, written the way FEDOBS writes evidence -- never a graph mutation.
</context>

<scope>
1. Land the `ToolAudit` verdicts (from PASSCRAFT) + the standing COMPASSURANCE matrix as Trino-queryable state, vintage-stamped like `code_heat` -- a 4th federation plane, OR quality columns on `tool_activity` keyed by `tool`.
2. The Behavior(demand) x Assurance(quality) x Change(heat) planes become JOIN-able (TO-3 consumes this for the quality-adjusted worklist).
3. Read side (querying the plane) is exercise-only and starts on spawn.
</scope>

<locked_invariants note="CTO~A arch-gate checks these -- LOAD-BEARING">
  1. **ASSURANCE IS EVIDENCE, NOT TRUTH (the FEDOBS boundary):** the Assurance-plane writer role is Deny-blocked from PutObject to `graph_nodes` / `edges` / `cse` / `tool_activity`. PROMOTE ALONE materializes truth; assurance is written like FEDOBS writes evidence. The `fedobs.tf` Deny-overrides-Allow boundary is INHERITED, not re-derived.
  2. **VERIFY THE FENCE ON LIVE, NOT DESIRED (AC5):** prove the Deny with `aws iam simulate-principal-policy` against the EXACT resource ARNs (graph_nodes/edges/cse/tool_activity), WITH a positive control on a resource the writer role DOES hold (CLAUDE.md Rule 22a -- comp-iam models (action) not (action,resource); a config-read is NOT a behavioral claim).
  3. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target.
</locked_invariants>

<acceptance_criteria>
  - **AC5 (assurance is evidence, not truth):** the Assurance-plane writer role is Deny-blocked from PutObject to graph_nodes/edges/cse/tool_activity, VERIFIED by `simulate-principal-policy` + positive control (live-grounded, not comp-iam-DESIRED-alone).
  - The plane is Trino-queryable + vintage-stamped; the Behavior x Assurance x Change JOIN returns.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_TOOLGRAPH_PRD.md @ 362272cce (sec.3 the ASSURANCE plane, sec.4 P2, sec.5 AC5)</ref>
  <ref type="boundary">fedobs.tf Deny-overrides-Allow (the inherited evidence-not-truth fence) -- NFRA_FEDOBS</ref>
  <ref type="source">NFRA_PASSCRAFT.TO-2 (the ToolAudit stream) -- hard prerequisite</ref>
  <ref type="iam-discipline">CLAUDE.md Rule 22a (simulate-principal-policy + positive control for a NEW resource ARN)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Evidence plane in Trino (read + evidence-write, Deny-fenced from graph mutation). No served pipeline artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
