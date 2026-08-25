<task_order>
<id>NFRA_COMPLEARN.P0</id>
<title>NFRA_COMPLEARN P0 -- the tool_activity BEHAVIOR CATALOG + 3-month SEED BACKFILL: ETL the 3 behavior logs into an Iceberg table bound as the 3rd Trino catalog on the LIVE globgrph-trino federation; dense from iteration 1.</title>
<issued_to>0.8.0_AE_CloudComp~E (dedicated COMPLEARN lane, MSTR-spawned per the cap-call). DEPTH-INDEPENDENT -- runs in parallel with the GRAPHDEPTH substrate (zero substrate dependency).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPLEARN is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-29. Closed as a record act, not a work verdict. Prior status: staged -- dispatch on ~E spawn (MSTR ALLOCATION-REQUEST 222838Z) + grant landed</status>
<priority>P0 -- the highest-leverage depth-INDEPENDENT start; the COMPLEARN loop's foundation; runs all night, uninterrupted (the reason it gets a dedicated lane, not a GRAPHDEPTH populator that pivots).</priority>
<project>NFRA_COMPLEARN</project>
<dependencies>NONE on the depth axis (behavior-plane ETL). The globgrph-trino federation is LIVE (iceberg + code_heat catalogs) -- ADD tool_activity as the 3rd catalog by REUSE, do NOT re-stand-up. The seed corpus exists (COO~B-verified: ~9.8K rolling-log rows + 1,472 session-log Compiler-Tools sections + 64 telemetry files + comp-which-rail.log).</dependencies>

<context>
NFRA_COMPLEARN (LD-0225) = the tool-USE verb of the NFRA_COMP* program -- a self-learning loop over our own tool-use. The 3-plane Trino federation (Behavior x Estate x Change) gains its missing Behavior plane = tool_activity. This P0 builds that catalog + the dense 3-month seed backfill so the loop has signal from iteration 1 (Andrew refinement #1). PRD: docs/architecture/NFRA_COMPLEARN_PRD.md (§2, §6, §8 P0) + brief docs/briefs/nfra-complearn-brief-20260630.md (§3, §6). The scorer/loop (P2-3) is gated on the COMPUNIFY coverage map + grain calibration (later); the CATALOG (P0) + federated views (P1) stand alone in value + are depth-independent.
</context>

<scope>
  1. LAND tool_activity as an Iceberg/Parquet table in the globgrph warehouse (same bucket as code_heat), bound as the 3RD Trino catalog beside iceberg (Estate) + code_heat (Change) -- REUSE the live globgrph-trino federation (0.8.0_AE_CloudComp built it; add a catalog, don't re-stand-up).
  2. ETL the 3 behavior streams into tool_activity (normalize to a common schema):
     - org/compiler-tools-log.md (~9.8K structured rows DATE|AGENT|TO_ID|TOOL|COMMAND|RESULT -- the attributed ledger).
     - org/mcp/agent_telemetry/*.jsonl (64 files; {ts,agent,tool,kind,session_id}; legacy tool:"?" rows NEED normalizing -- the known Phase-0 cost).
     - org/mcp/comp-which-rail.log ({ts,action,tool,term,matches,...} -- the rail-escape/on-rails-primitive log; a RUN-GREP with no rich-tool hit on a hot path = a tool-demand event; the richest coverage-gap signal).
  3. SEED BACKFILL (Andrew refinement #1, one-time historical ETL): backfill from the 3-month corpus -- the 8.6K rolling-log rows (2026-04-09->06-30) + the 1,472 session-log `## Compiler Tools` sections (the agent-annotated "gap found" lines are the HIGHEST-value training signal; no automated stream captures them). Dense from iteration 1, not forward-only.
  4. JOIN keys (so Trino can later federate Behavior x Estate x Change): (repo,path) Behavior<->Change(code_heat); target_path->graph_nodes Behavior<->Estate(iceberg); firm/layer derived dims.
  5. PRINCIPLES (PRD §5): READ-ONLY over the source logs (never mutate them) + vintage-stamped (computed_at column, a derived snapshot like code_heat); ATTRIBUTION-CORRECT (reuse the race-free per-session SERIAL/TO_ID resolution the comp_log_auto fix established, so role/TO/firm dims are trustworthy).
</scope>

<acceptance_criteria>
  1. tool_activity Iceberg table LIVE in the warehouse + bound as the 3rd Trino catalog (queryable in globgrph-trino beside iceberg + code_heat); REUSE-not-restand-up evidenced.
  2. All 3 behavior streams ETL'd + normalized (agent_telemetry tool:"?" rows resolved); the 3-month seed backfill loaded (rolling-log rows + the session-log gap-annotations).
  3. Read-only over the source logs (evidenced); vintage-stamped (computed_at); attribution-correct (SERIAL/TO_ID).
  4. RAVC2 to COO~B (cc CTO + MSTR). This is the substrate P1 (federated views + comp-learns-status dashboard) reads + the loop (P2) scores against.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPLEARN_PRD.md (§2,§6,§8 P0)</ref>
  <ref type="brief">docs/briefs/nfra-complearn-brief-20260630.md (§3 seed corpus, §6)</ref>
  <ref type="substrate">the LIVE globgrph-trino federation (memory project_trino_federation_layer_live) -- add tool_activity as catalog #3</ref>
  <ref type="seed-grounding">COO~B verified the corpus dimensions early-session (~9.8K rolling rows / 1,472 session logs / 64 telemetry / comp-which-rail.log present)</ref>
</references>
</task_order>
