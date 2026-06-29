# Trino federated query layer -- LIVE end-to-end (Andrew #1 ASAP)
**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, DIAGNOSE, COORDINATE
**Serial:** 0.8.0_AE_CloudComp | **Window:** session start ~1904Z -> 2110Z | **Date:** 2026-06-29

## Summary

Took the heat/analytics **Trino federation** from fragmented-design-no-owner to **LIVE serving federated queries** in ~2h. Named owner (Andrew via MSTR/COO/CTO). Both milestones delivered + accepted by COO + CTO + relayed to Andrew:
- **M1:** Trino single-node Fargate stood up on opal-globgrph; first iceberg query SERVED -- `SELECT count(*) FROM iceberg.globgrph.graph_nodes` = **18203**, FINISHED.
- **M2:** cross-catalog **JOIN** iceberg `graph_nodes` x git `code_heat` = **374 portal source files** classified hot/cold across asset AND code (COLD 312 / WARM 50 / HOT 12) in one Trino query -- the headline.

## What I built / deployed

- **trino.tf** (new): single-node Trino as a Fargate service on the `opal-globgrph` ECS cluster (FARGATE-only; co-located w/ Nessie). Config-injected on stock `trinodb/trino:470` (no custom image). Pinpoint task role (warehouse READ-ONLY + Glue read + ssm-exec only). `iceberg` catalog via Nessie REST `/iceberg/main`; `code_heat` catalog via hive+Glue.
- **glue_code_heat.tf** (new): Glue external table over ~B's git code-heat parquet (`warehouse/code_heat/repo={ajb_workspace,portal}/`), read IN PLACE; **explicit `aws_glue_partition`** per repo (Trino 470 rejects Glue partition projection).
- **node_health/taxonomy**: pre-existing (this session only consumed it). Design doc `deliverables/NFRA_MSGRAPH/S3_heat_federation_and_layer_taxonomy_design.md` + new `S3b_code_heat_parquet_emitter_BUILD_SPEC.md` (handed to ~B).
- **Deploy ledgers** (both CLOSED clean 3/3, nothing stranded): `trino-federation-standup`, `trino-federation-join`.

Commits: `23155e41c` (parity-AC+spec), `63bd2fe28` (trino.tf), `bc5fbb225` (node.id+/iceberg/main), `e94fa790c` (Glue catalog), `955ba557a` (projection-flag, reverted), `eb6098434` (explicit partitions), `2fa1e829d` (BatchGetPartition), `738acdba5` (ledger close). All author-lined 0.8.0_AE_CloudComp, on origin/CLOUD.

## Deployment Sequence + Verification (actual output)

- safe-apply trino.tf: `Apply complete! 11 added, 0 changed, 0 destroyed` -> 0-diff re-plan `No changes`.
- First iceberg query: `data:[[18203]]`, state=FINISHED, 4.2s (query 20260629_201200_00000_vfm3i).
- code_heat count: `[[21527]]` (== ~B's verified rows). Parity DISTINCT: 2 vintage triples (ajb 15e3a25b.., portal adda3e0e.., computed_at 1782763452).
- Final JOIN: `matched=374`; bands `["cold",312,0.131]["warm",50,0.625]["hot",12,0.933]`, FINISHED no error.
- Snapshot cross-check (seam-5 finding): Trino/Nessie current graph_nodes snapshot = 5612831170965463937 != ~B's metadata.json read 1845507532511214963 -> newest-S3-metadata != Nessie-current.

## DIAGNOSE (every transient root-caused on logs/source, Rule-22 -- not guessed)

1. task exit 100 = `node.id` (stock image -> $HOSTNAME=ip-x.ec2.internal dots illegal) -> set node.id. 2. iceberg URI needed `/iceberg/main` (mirror proven writer). 3. code_heat 0 rows = Trino 470 ignores Glue projection + no auto-discovery -> explicit partitions. 4. `glue:BatchGetPartition` missing (IAM; propagation-confirmed live). 5. JOIN key: `module:` is in **node_id** not name; path in `props['path']` on `node_type='Module'` (kuzu name=node_id-fallback differs from iceberg) -- grounded on the 8-field iceberg schema + ~B confirm.

## Bind decision (SETTLED)

CTO blessed iceberg-snapshot, then **REVERSED -> KEEP GLUE** (my grounded lean): Glue reads parquet in place = zero-dup + auto-refresh + more faithful to "git not materialized"; seam-6 reads parquet directly so 2-catalog surface doesn't burden parity. No migration.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which | route federation-doc + nessie-topology + trino-presence questions | PASS (routed/backstop) |
| comp-iam (live get-role-policy) | ground-truth BatchGetPartition landed live (fresh-IAM exception, rail-marked) | PASS -- confirmed |
| safe-apply / safe-commit / deploy_ledger | every deploy gated; 2 ledgers opened+closed 3/3 | PASS |

What worked: comp-which backstop + the rail-checked live-IAM read (the documented fresh-IAM exception). What failed: comp-which routed federation-state questions to the manifest backstop (no rich tool for "is service X stood up" -- raw search legitimately needed, rail-marked). Gap: no comp-tool surfaces "is an ECS/Fargate service materialized" or "Trino catalog binding vs live iceberg" (the latter IS NFRA_COMPDRIFT seam-5/6, now in build by ~B).

## Current State

Trino federation LIVE: service `globgrph-trino` (task-def rev :5) HEALTHY on cluster `opal-globgrph`, DNS `trino.opal-globgrph.local:8080` (in-VPC only). Catalogs: `iceberg` (graph_nodes/edges/contracts via Nessie) + `code_heat` (Glue hive over parquet). Query mechanism = in-VPC one-shot Fargate run-task -> REST -> CloudWatch (no session-manager-plugin locally). All grounded facts banked in `memory/project_trino_federation_layer_live.md`.

## Next Steps

1. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** S5 served-wiring decision (routed, non-gating): comp-heat ALREADY EXISTS (CTO-owned, git-local) -> federation net-new = the graph x code-heat JOIN. Decide (A) extend comp-heat w/ a `federated` subcommand vs (B) sibling `comp-fed`; transport (1) run-task-pattern v0 vs (2) persistent endpoint. My lean A+1 now. I have the query module ready.
2. **[0.8.0_AE_CloudComp~B]** seam-5/6 parity: coordinated; gave the 3-table grain correction (layer is a column on graph_nodes, NOT 4 catalogs) + the vintage-resolution finding (resolve current via Nessie, not newest-S3-metadata). node_health NOT yet materialized -> add to seam-5 when GLOBGRPH_HEALTH_ENABLED flips.
3. **node_health flip** (S1 tail): enable on a nightly after L6 + RAVC COND-A 0-diff (0.7.0/derive lane + cadence-gated).

## Blockers
None. The #1 priority is COMPLETE. S5 is non-gating polish awaiting a CTO/COO owner-decision I requested (legitimate gate, not assumption-blocked).
