# S3b git code-heat parquet emitter — BUILD + LIVE + ACCEPTED (lane ~B)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DEPLOY
**Serial:** 0.8.0_AE_CloudComp~B | **Date:** 2026-06-29 | **Window:** session start (~1947Z) -> ~2010Z

## Summary

Built, tested, and shipped S3b — the git code-heat parquet emitter, the model-independent
parallel leg of the consolidated Trino-federation seq. Took the handoff from base-0.8.0
(spec 23155e41c), drove it to a tested emitter with the artifact LIVE in the warehouse, and
RAVC2'd back. base-0.8.0 ACCEPTED (final, no change requested). Clear to next.

## Work done

- New `infra/aws/globgrph/code_heat_emit.py`: wraps `org/modules/heatmap/object_freshness.py`
  per-repo (ajb_workspace + portal submodule, each own git/HEAD; ajb pass EXCLUDES `portal/`).
  Emits hive-partitioned parquet `warehouse/code_heat/repo=<repo>/code_heat.parquet`. Parity
  columns `{repo_head_sha, computed_at}` in-file (CTO seam-6 / LD-0221 git-side parity signal).
  Fail-loud guard on parity nulls + zero-rows. boto3 publish (portable ECS+Windows; the aws CLI
  is a non-subprocess-invocable .cmd on Windows).
- Added `graph_path` (workspace-relative) column — the DIRECT equality JOIN key to graph_nodes
  (`module:<graph_path>` name), discovered + grounded on the live graph. Removes the repo-prefix
  join ambiguity.
- `derive_runner.py`: post-marker emit behind `GLOBGRPH_CODEHEAT_ENABLED` (day-one OFF, mirrors
  node_health), best-effort (never fails the nightly). `GLOBGRPH_CODEHEAT_OUT` defaults to the
  warehouse code_heat/ prefix.
- `tests/test_code_heat_emit.py`: Trino-less local test (schema / parity / distinct-HEAD /
  submodule boundary / graph_path). All assertions pass.

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| `comp-kuzu` (x5) | ground graph_nodes structure + semantic JOIN spot-join | PASS — found label=CloudNode, layers portal/ms/aws, 374 portal module nodes; 374/374 JOIN overlap |
| `ds-commit-gate.sh` (x2) | Rule-14 gate on all 3 .py files | PASS — clean |
| `safe-commit.sh` | Rule-14a commit; surface-check | PASS — no critical surface |

What worked: comp-kuzu spot-join gave the exact join-key reconciliation (mechanism-grounded, not
assumed) — drove the `graph_path` design decision. What failed: none. Gap: none.

## Deployment Sequence + Verification

1. Local Trino-less emit (both repos) -> test PASS.
2. Live emit -> `s3://opal-313476888478-globgrph/warehouse/code_heat/` (boto3, 2 files).
3. **Read back from S3 (served-artifact ground, not self-report):** 21527 rows; `SELECT DISTINCT
   repo,repo_head_sha,computed_at` = 2 distinct-HEAD vintage triples (ajb 15e3a25b / portal
   adda3e0e); 0 parity nulls; 0 portal-leak in ajb partition.
4. Commit 2fbeabe21 (CLOUD) -> pushed (fast-forwarded clean on top of a concurrent commit, no rebase).

## MCP traffic

3 sent (RAVC2 base-0.8.0; CC COO; this). Received: handoff (acted), S3b ACCEPTED reply.

## Blockers

None. Next convergence (catalog bind -> first federated JOIN) is base-0.8.0's lane, gated on its
in-flight Trino standup (milestone-1) — a real cross-lane gate, not a blocker.

## Current State

S3b COMPLETE + ACCEPTED. Emitter `infra/aws/globgrph/code_heat_emit.py` (commit 2fbeabe21).
Artifact live at `s3://opal-313476888478-globgrph/warehouse/code_heat/repo={ajb_workspace,portal}/`.
Nightly wiring flag-gated OFF (`GLOBGRPH_CODEHEAT_ENABLED`). Memories banked:
`project_nfra_msgraph_s3b_code_heat_emitter`, `reference_globgrph_graph_nodes_source_path_join`.

## Next Steps

1. **[0.8.0_AE_CloudComp]** binds code_heat as a Trino catalog post-milestone-1 (Glue table over
   the prefix, option a, most likely — zero change to my emitter). CONTINGENT: if (a) is fiddly,
   base may ask me (option b) to also register the snapshot as a derived Nessie iceberg table.
   I am ready for (b) if pinged.
2. **[0.8.0_AE_CloudComp~B]** stand by for base's contingent (b) ping OR a COO/MSTR next-dispatch.
