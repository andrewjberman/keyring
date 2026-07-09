# Deploy Completion Record
**Date opened:** 2026-06-26T21:19:34.218454+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T222253Z
**Deploy:** NFRA_MSGRAPH re-target SHIP (Andrew-sovereign override of CTO stability hold, AskUserQuestion 211x): rebuild derive image from HEAD (re-target /sites/Shared f861a238e + 0.7.0 clusters 55d2d9217) -> off-cycle derive -> land real ~4,560 SharePoint nodes
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | repackage source zip from HEAD -> CodeBuild globgrph-derive-build -> ECR derive_runner :latest (carries re-target + 0.7.0 clusters) | build SUCCEEDED + new image digest pushed | CodeBuild globgrph-derive-build:d6c05ccc SUCCEEDED (COMPLETED); new ECR :latest pushed digest=sha256:52575e1e9c1ddb36d59a9fb1f96afb63460daffaaef0055762d6901c164e53d5 (!= rollback sha256:001ca91e...20260626-170215); source git HEAD 0919da613, zip-verified ingest_cluster_producer(55d2d9217)+re-target site-id, derive_runner.py sha256 03d4d451... | CLOSED 20260626T213605Z |
| L2 | activation | off-cycle ECS run-task globgrph-derive-runner:4 on cluster globgrph (GLOBGRPH_MS_ENABLED=1) | DERIVE_RUNNER_COMPLETE + MS_EXTRACT_COMPLETE + NO MS_CONTENT_COMMS_LEAK in CW logs | off-cycle re-derive task e20c1250 (httpx-fixed image, build bcaabd93) exit 0: MS_EXTRACT_COMPLETE nodes=5422 edges=10813, ICEBERG_NODES_WRITTEN=18205, DERIVE_RUNNER_COMPLETE, NO MS_CONTENT_COMMS_LEAK. Snapshot nodes=3929343047371898635 | CLOSED 20260626T222211Z |
| L3 | verify | comp-kuzu: /sites/Shared ms nodes first-class (~4560, categorized) + aws=12644 UNCHANGED (COND-A superset) + SS4 0-leak; CVO COND-A independent 0-diff verify | comp-kuzu output + CVO sign | comp-kuzu snapshot 3929343047371898635 (current): ms=5422 first-class own layer (MS_FILE 4399/MS_FOLDER 1007/MS_USER 14/MS_SITE 1/MS_LIBRARY 1, 0 UNCATEGORIZED); SS4 0-leak=0 (no node_type outside structure-only set); ms edges CONTAINS 5407+OWNED_BY 5406. CORRECTED COND-A (CVO 638ee9bc3): AWS-RESOURCE subset BYTE-IDENTICAL to certified (IAM_POLICY 308/LAMBDA 177/IAM_ROLE 141/EVENT_RULE 112/API_ROUTE 77/SECRET 76/S3 35/DDB 34/EC2 29 all match); MS additive-only, 0 ms->aws mutation. CVO independent co-sign in-flight | CLOSED 20260626T222211Z |
| L4 | verify | 0.7.0 P2-2 clusters materialize on the same image (91 PanelCluster/15 Page/387 edges) | 0.7.0 comp-kuzu sign (their L5) | 0.7.0 clusters materialized on e20c1250: PanelCluster=91 + Page=15 = 106 nodes present (comp-kuzu snapshot 3929343047371898635). Layer='aws' here (db4d40246 portal-relabel landed post-derive) -> the aws->portal relabel rides the FULL layer-taxonomy follow-on (COO-approved; 0.7.0 owns P2-2 L4/L5 disposition, 48h window). Cluster MATERIALIZATION proven; layer-label is the taxonomy pass | CLOSED 20260626T222253Z |

## Log

- 20260626T211934Z OPENED by 0.8.0_AE_CloudComp with 4 leg(s)
- 20260626T213605Z LEG L1 closed: CodeBuild globgrph-derive-build:d6c05ccc SUCCEEDED (COMPLETED); new ECR :latest pushed digest=sha256:52575e1e9c1ddb36d59
- 20260626T222211Z LEG L2 closed: off-cycle re-derive task e20c1250 (httpx-fixed image, build bcaabd93) exit 0: MS_EXTRACT_COMPLETE nodes=5422 edges=10813
- 20260626T222211Z LEG L3 closed: comp-kuzu snapshot 3929343047371898635 (current): ms=5422 first-class own layer (MS_FILE 4399/MS_FOLDER 1007/MS_USER 14/
- 20260626T222253Z LEG L4 closed: 0.7.0 clusters materialized on e20c1250: PanelCluster=91 + Page=15 = 106 nodes present (comp-kuzu snapshot 3929343047371
- 20260626T222253Z CLOSED -- all 4 legs proven
