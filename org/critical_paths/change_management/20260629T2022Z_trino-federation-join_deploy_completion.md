# Deploy Completion Record
**Date opened:** 2026-06-29T20:22:27.358541+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T210035Z
**Deploy:** Milestone-2 FULL federation: bind code_heat (Glue+hive over ~B's parquet, in-place) + the cross-catalog JOIN graph_nodes(iceberg) x code_heat(hive). NFRA Trino-fed Andrew#1.
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply: Glue db+table (code_heat, partition-projection) + trino_task glue-read IAM + trino task-def adds code_heat hive catalog (4 add/1 change/1 destroy) | apply complete + 0-diff re-plan | safe-apply complete 20260629T2024Z: 4 added (glue db globgrph + glue table code_heat + trino_task_glue_read policy + new task-def rev) / 1 changed (ecs service -> new task-def) / 1 destroyed (old task-def rev). 0-diff re-plan PASS. HALTGT pass. commit e94fa790c. | CLOSED 20260629T202325Z |
| L2 | verify | Trino redeploys healthy w/ the code_heat catalog; SELECT count from code_heat returns (~21527) | task HEALTHY + code_heat count query | rev5 Trino HEALTHY with the code_heat hive+glue catalog loaded (explicit Glue partitions repo=ajb_workspace+portal). SELECT count(*) FROM code_heat.globgrph.code_heat = 21527 (matches ~B's verified row count exactly), state FINISHED. Parity signal queryable through Trino: SELECT DISTINCT repo,repo_head_sha,computed_at = 2 vintage triples (ajb 15e3a25b.., portal adda3e0e.., computed_at 1782763452) -- the seam-6 git-side signal LIVE. Required glue:BatchGetPartition (added 2fa1e829d, IAM-propagation-confirmed live). | CLOSED 20260629T204818Z |
| L3 | verify | cross-catalog JOIN graph_nodes x code_heat on graph_path returns hot/cold-per-asset rows (milestone-2 headline) | JOIN query output | FULL FEDERATION PROVEN: cross-catalog JOIN iceberg.graph_nodes (g) x code_heat (ch) ON substr(g.node_id,8)=ch.graph_path WHERE node_id LIKE 'module:%' = 374 portal source files matched (== ~B's 374/374). Hot/cold-across-asset-AND-code distribution: cold=312 (avg_score 0.131), warm=50 (0.625), hot=12 (0.933), all FINISHED no error. JOIN key grounded on source (graph_nodes 8-field schema: module: prefix in node_id not name; path in props) + ~B confirm. This is 'hot/cold across an asset AND its code in one query' -- the headline. | CLOSED 20260629T210035Z |

## Log

- 20260629T202227Z OPENED by 0.8.0_AE_CloudComp with 3 leg(s)
- 20260629T202325Z LEG L1 closed: safe-apply complete 20260629T2024Z: 4 added (glue db globgrph + glue table code_heat + trino_task_glue_read policy + new
- 20260629T204818Z LEG L2 closed: rev5 Trino HEALTHY with the code_heat hive+glue catalog loaded (explicit Glue partitions repo=ajb_workspace+portal). SEL
- 20260629T210035Z LEG L3 closed: FULL FEDERATION PROVEN: cross-catalog JOIN iceberg.graph_nodes (g) x code_heat (ch) ON substr(g.node_id,8)=ch.graph_path
- 20260629T210035Z CLOSED -- all 3 legs proven
