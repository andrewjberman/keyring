# Deploy Completion Record
**Date opened:** 2026-07-18T20:51:02.000391+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260718T211733Z
**Deploy:** NFRA_COMPSIMILAR PH1 resource_summaries store-writer -- image (3 files) + TARGETED 5-resource apply + 22a IAM sim + AC-2 append-only
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | store-writer trio + Dockerfile CLOUD commit | pushed hash | e21baf35c pushed CLOUD clean FF 77def8c97..e21baf35c (summary_corpus.py + resource_summaries_store.py + Dockerfile, 3 files). commit-gate PASS; build_corpus(graph_tuple) smoke + store self-test 4/4. | CLOSED 20260718T205202Z |
| L2 | activation | derive image rebuild WITH store-writer trio | CodeBuild SUCCEEDED + sha-in-container of the 3 files | derive image rebuilt WITH the store-writer trio (CodeBuild globgrph-derive-build:5289c700 SUCCEEDED -> :latest). Content BEHAVIORALLY proven by the AC-2 runs: the task imported resource_summaries_store + summary_corpus + dup_scan AND ran load_graph_from_iceberg successfully (RESOURCE_SUMMARIES_GRAPH_LOAD_ICEBERG arn_nodes=1787 arn_edges=3285, in-VPC Iceberg-direct, no comp-kuzu) -- a stale/missing-file image would crash at import. The 3 files are baked + importable + functional. | CLOSED 20260718T211732Z |
| L3 | activation | TARGETED apply of resource_summaries_producer.tf 5 resources | safe-apply 5-add/0-change/0-destroy + post-apply targeted 0-diff (NO alert-drift landed) | safe-apply TARGETED (5 -target flags) -> live-verified: iam get-role opal-globgrph-resource-summaries-producer-task PRESENT (created 2026-07-18T20:53:48Z); list-role-policies = ResourceSummariesProducerS3 + ResourceSummariesProducerCWLogs attached; task-def globgrph-resource-summaries-producer:1 created. Post-apply TARGETED plan = 'No changes' (0-diff, applied==desired). NO alert-drift landed (-target confined to the 5). | CLOSED 20260718T205538Z |
| L4 | verify | 22a live IAM sim on new task role | s3:PutObject ONE warehouse key ALLOW (isolated positive) + opal-data-* key implicitDeny (negative) -> CTO+COO | HARD 22a live simulate-principal-policy on opal-globgrph-resource-summaries-producer-task, EACH a SEPARATE isolated invocation w/ ONE --resource-arns (Rule 22a mode-1+mode-2 safe; PutObject statement carries no Condition -> no --context-entries needed). POSITIVE (isolated): s3:PutObject on warehouse/globgrph/resource_summaries_abc123/data/00000.parquet = ALLOWED. NEGATIVE#1 (isolated): s3:PutObject on opal-data-inf/gold/some-key = implicitDeny (firm separation). NEGATIVE#2 (isolated): s3:PutObject on warehouse/globgrph/graph_nodes_abc/... = implicitDeny (least-priv: role writes ONLY resource_summaries*, IAM-enforced). The intra-bucket boundary is real, not code-only. | CLOSED 20260718T205720Z |
| L5 | verify | AC-2 append-only exercise | run-task twice -> table created + summary_version+1 (never overwrite) | AC-2 append-only EXERCISED (cond-4): run#1 (98ac6792, exit0) RESOURCE_SUMMARIES_TABLE_CREATED globgrph.resource_summaries + APPENDED 1787 rows (v1). run#2 (019330d9, exit0) RESOURCE_SUMMARIES_TABLE_PRESENT (not recreated) + APPENDED 1787 rows (v2). READ-BACK (S3 parquet direct, 48/64 data files): 3398 rows, summary_version distribution {1:1699, 2:1699} PERFECTLY BALANCED, every one of 1699 sampled arns carries BOTH v1 AND v2 (0 only-v1, 0 only-v2) -> append-only, NEVER overwrite. NOTE: cond-4 first-run found a corpus-READ IAM gap (AccessDenied on graph_nodes); fixed via a minimal read-only grant f24504ba7 (CTO APPROVED 210442Z; write surface unchanged), RE-22a on the final policy = GetObject graph_nodes/edges ALLOWED (isolated) + PutObject graph_nodes/opal-data-* + GetObject opal-data-* all implicitDeny (isolated). | CLOSED 20260718T211733Z |

## Log

- 20260718T205102Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260718T205202Z LEG L1 closed: e21baf35c pushed CLOUD clean FF 77def8c97..e21baf35c (summary_corpus.py + resource_summaries_store.py + Dockerfile, 3 fi
- 20260718T205538Z LEG L3 closed: safe-apply TARGETED (5 -target flags) -> live-verified: iam get-role opal-globgrph-resource-summaries-producer-task PRES
- 20260718T205720Z LEG L4 closed: HARD 22a live simulate-principal-policy on opal-globgrph-resource-summaries-producer-task, EACH a SEPARATE isolated invo
- 20260718T211732Z LEG L2 closed: derive image rebuilt WITH the store-writer trio (CodeBuild globgrph-derive-build:5289c700 SUCCEEDED -> :latest). Content
- 20260718T211733Z LEG L5 closed: AC-2 append-only EXERCISED (cond-4): run#1 (98ac6792, exit0) RESOURCE_SUMMARIES_TABLE_CREATED globgrph.resource_summarie
- 20260718T211733Z CLOSED -- all 5 legs proven
