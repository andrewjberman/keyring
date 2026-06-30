# NFRA_COMPLEARN P0 -- tool_activity Behavior catalog LANDED + live-verified (lane ~E)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Serial:** 0.8.0_AE_CloudComp~E (dedicated NFRA_COMPLEARN build lane, MSTR-spawned per the cap-call, Andrew-provisioned)
**Date:** 2026-06-30
**Window:** session start (~2235Z) -> ~2352Z

## Summary

First session of lane ~E. Started cold (fresh lane, not registered), commissioned as the dedicated
NFRA_COMPLEARN build lane via COO~B's GO. Built + landed **NFRA_COMPLEARN.P0**: `tool_activity` =
the 3rd Trino catalog (the Behavior plane) on the LIVE globgrph federation, by REUSE (no
re-stand-up). End-to-end in one session: ETL -> S3 materialize -> Glue table -> Trino catalog roll
-> live-query verify -> RAVC2. P0 ACCEPTED by COO~B + affirmed by CTO; P1 GO received.

## What was built

Three new modules + two TF changes (the code_heat catalog #2 pattern, mirrored for catalog #3):

- `infra/aws/globgrph/tool_activity_emit.py` (commit 0e1f02944) -- ETLs 4 behavior streams into one
  normalized 22-col parquet, hive-partitioned by `source`, boto3-published to the warehouse. READ-ONLY
  over the source logs; parity cols (repo_head_sha/computed_at); derived dims (role from serial,
  firm/layer/repo/target_path as JOIN keys). Hardened the telemetry parser for BOTH schema
  generations (old `{agent, tool:"?"}` + new `{serial, tool_name}`) -- ~A's seed parser dropped the
  old-gen rows; mine keeps them.
- `infra/aws/terraform/globgrph/tool_activity.tf` (commit 0a51867f6) -- aws_glue_catalog_table in the
  EXISTING `globgrph` Glue DB (reuses aws_glue_catalog_database.code_heat -> the Trino task role's
  `table/globgrph/*` grant already covers it: ZERO IAM widening), 22 cols grounded on the live parquet
  footer, partition key `source`, 5 explicit aws_glue_partition.
- `infra/aws/terraform/globgrph/trino.tf` (commit 0a51867f6) -- added the 3rd catalog block
  (`tool_activity.properties`, hive/glue, identical connector to code_heat.properties) to the task-def
  container command.
- `infra/aws/globgrph/tool_activity_parity.py` (commit 0a51867f6) -- NFRA_COMPDRIFT seam-6 binding,
  VINTAGE-PRIMARY tri-state (current/BEHIND/UNVERIFIABLE), mirrors code_heat_parity.py.
- drift-topology.yaml seam-6 binding registration -- owned-paths BLOCKED for AE (lane=ANY_EXEC);
  RAVC'd the exact block to COO~B, who landed it (commit 2e796cd -- flips the seam-6 tool_activity leg
  GAP->COVERED).

## Deployment Sequence + Verification (deploy ledger 20260630T2302Z, CLOSED -- all 5 legs proven)

- L1 git: 0e1f02944 (emitter) + 0a51867f6 (Glue/Trino/parity) + 17b9d7bb9 (ledger) pushed to CLOUD.
- L2 S3 emit: `python tool_activity_emit.py` -> 5 parquet to s3://opal-313476888478-globgrph/warehouse/tool_activity/source=*/; 125,162 rows.
- L3 Glue: TARGETED `safe-apply ... -target=aws_glue_catalog_table.tool_activity -target=aws_glue_partition.tool_activity` -> 6 added. (Targeted because the full plan showed 12-add/2-change/1-destroy -- 5 of those were another agent's UNAPPLIED held ADVI_BREAKS TO-6 item2d/item2e; a bare apply would have swept held firefight controls into a live apply. COO~B affirmed: "targeting was the whole ballgame.")
- L4 Trino roll: TARGETED `safe-apply ... -target=aws_ecs_task_definition.trino -target=aws_ecs_service.trino` -> 1 added/1 changed/1 destroyed (task-def :5->:6, service rolled). Rollout COMPLETED, zero-downtime (old task served until new healthy).
- L5 LIVE Trino verify (ECS-Exec, taskDef :6 -- had to download session-manager-plugin, not installed):
  - `SHOW CATALOGS` -> tool_activity present BESIDE iceberg + code_heat. Startup log: "Added catalog tool_activity using connector hive".
  - `SELECT source, count(*) GROUP BY source` -> telemetry 108,846 / rolling_log 8,904 / rolling_log_summary 103 / session_log 5,741 / rail 1,568 = 125,162 (exact emit match).
  - FEDERATION: `tool_activity JOIN code_heat ON target_path = graph_path` -> 5,502 matched rows (the 3-plane Behavior x Change works at query time).
  - gap_text rows = 259; rail demand RUN-GREP 509 / RUN-GLOB 154 / DENY 175 queryable.
  - seam-6 parity vs LIVE S3 = `current` (vintage 0.47h, head_advanced -- expected).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | "what depends on/reads the globgrph trino federation" | PASS | Rule-20 dep check pre-roll: routed TRINO surface -> comp-kuzu/comp-graph (on-demand query consumers, NOT a served customer surface) -> low-blast roll confirmed |
| comp-which | (HUD nudges, multiple) | PASS | rail HUD fired on Bash aws/grep; format-sampling of specific known files is the raw-search exception (Rule 21) -- estate/dep questions went through comp-which |
| ds-commit-gate.sh | tool_activity_emit.py / tool_activity_parity.py | PASS | py_compile + AST + ruff clean on both .py before commit |
| safe-commit.sh | x4 commits | PASS | surface-check clean; owned-paths correctly BLOCKED drift-topology.yaml (org/modules ANY_EXEC) -> SoD handoff to COO~B |
| safe-apply.sh | targeted Glue + targeted Trino | PASS | HALT-gate passed both; -target isolated my 7 resources from held item2d/2e |
| deploy_ledger.py | open/close-leg x5/close | PASS | NEVER-law deploy-completion ledger opened at start, closed all 5 legs proven |

**What worked:** plan-before-apply caught the held-firefight-control sweep risk; the code_heat catalog #2 pattern transferred cleanly to catalog #3; ECS-Exec live SQL gave the sharpest queryable proof.
**What failed:** session-manager-plugin not installed (had to download the standalone bundle for ECS-Exec). MSYS path-conversion mangled the leading-`/` CloudWatch log-group arg -> used PowerShell.
**Gap found:** no comp-tool fronts the globgrph Trino federation for a "is catalog X queryable / show catalogs" check -- the verification was raw `aws ecs execute-command` + manual plugin setup. A `comp-trino` / `comp-federation` surface (SHOW CATALOGS + a SELECT smoke) would be a real lift (this is itself a COMPLEARN demand signal -- a hot-path inspection with no tool).

## MCP traffic

~12 messages. Significant: COO~B GO COMPLEARN P0 (the commission) -> RAVC2 P0 LANDED -> COO~B ACCEPTED + GO P1. CTO cc affirm (4 arch notes + the P0-1-stands-alone/P2-scorer-gated distinction). ~A handoff (parser code + warehouse template) acked. ~C gap-map handoff (3 supply-side grain-gaps) acked + banked for P2. RAVC1 plan-surface to COO~B (the item2d/2e finding) -> AFFIRMED.

## Files Modified

See commit messages: 0e1f02944, 0a51867f6, 17b9d7bb9. drift-topology.yaml landed by COO~B (2e796cd).

## Current State

NFRA_COMPLEARN.P0 COMPLETE + ACCEPTED. The Behavior plane is LIVE: `tool_activity` is the 3rd Trino
catalog on globgrph-trino (taskDef globgrph-trino:6, ECS service running on cluster opal-globgrph),
queryable beside iceberg (Estate) + code_heat (Change). Data at
`s3://opal-313476888478-globgrph/warehouse/tool_activity/source=*/tool_activity.parquet` (125,162
rows, refreshable by re-running tool_activity_emit.py). seam-6 parity binding registered + COVERED.
No core-doc update (no pipeline_inventory.xml for this lane; globgrph federation is infra, not a firm
pipeline). Deploy ledger CLOSED. Nothing stranded, nothing blocked.

## Next Steps

1. **[0.8.0_AE_CloudComp~E / self]** P1 (GO received from COO~B): federated Trino views
   (Behavior x Estate x Change) + comp-learns-status dashboard (reclaim the dead shim, repoint to the
   live federation, read-only status surface). Substrate-only -- NO scorer (P2). Design the view
   persistence (Trino task role is Glue READ-ONLY -> likely a committed SQL view-library + reader, vs
   an IAM grant for glue:CreateTable). RAVC2 COO~B, cc CTO.
2. **[1.0.0_SA_CTO]** P2 scorer-honesty (the Goodhart gate) is yours when P2 dispatches; the substrate
   carries outcome columns (gap_text/action/matches/result) but the SCORER must anchor on
   escapes-prevented/chains-shortened, never usage-counts (CTO arch-note #3 caveat).
3. **[3.0.0_SA_CVO~B]** P2 gap-map ground-truth + scorer-honesty verify (gated on the COMPUNIFY
   substrate /seams-GREEN).
4. **[0.8.0_AE_CloudComp~C]** the S4 AUDIT-part grain-gaps feed my P2 worklist when they surface.

## Blockers

None. P2 (scorer/gap-map) is gated on the COMPUNIFY map + substrate /seams-GREEN by DESIGN (CTO gate
distinction), not a blocker. P0-1 stand alone + depth-independent.
