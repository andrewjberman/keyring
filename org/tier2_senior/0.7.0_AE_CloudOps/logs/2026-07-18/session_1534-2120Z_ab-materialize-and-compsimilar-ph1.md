# NFRA batched wake: A+B canonical-motif materialize (WS-1) + COMPSIMILAR PH1 store-writer (WS-2) -- both COMPLETE

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE
**agent:** 0.7.0_AE_CloudOps (MSTR-spawn, COO C3-chain valve) - **date:** 2026-07-18 - **window:** ~15:34Z -> ~21:20Z
**TO:** COO batched NFRA wake (152757Z): WS-1 A+B materialization ingest (Andrew-direct headline) + WS-2 COMPSIMILAR PH1 store-writer (CTO plan-gate PASS 141857Z + 4 conditions)

## Summary

Two governed workstreams, both closed. In EACH, the first-run EXERCISE caught a material defect that a
config-read could not have -- WS-1's 79% edge-materialization gap and WS-2's corpus-READ IAM gap -- both
root-caused (Rule 22: source + live + log), fixed producer-side, re-exercised to clean, and hardened with
CTO-ratified standing invariants. 5 commits, 2 deploy-ledgers closed, 3 independent applied confirmations
on WS-1 (mine + DS~B + pending CVO/~C).

## WS-1 -- A+B canonical-motif ADDITIVE materialize into the semctl C2/C3 layer (COMPLETE, triple-confirmed)

Ingest the discovered A+B canonical-motif layer (C2 @fbfa06590 / C3 @c7048f484 -- 13 C2Motif + 3 C3System
overlapping-domain-cover + 5088 CONTAINS) into the LIVE semctl layer via the GOVERNED promotion path.

- **ADDITIVE, not replace** (COO-confirmed 155710Z; DS~B design): extended the ONE governed producer
  `ingest_c2c3_motif_producer` (derive_runner.py) to fold BOTH governed emit specs -- the 07-08 debt layer
  (kept UNTOUCHED, CVO-certed) + the 07-18 A+B layer. Disjoint node_ids -> clean union. Post-ingest live
  TOTAL C2Motif=19 (6+13) / C3System=4 (1+3); the "3" A+B is the contribution, not a total. Offline
  self-test 20/20 -> 22/22. Commit **8547b069d**.
- **APPLIED-vs-DESIRED GAP FOUND (the value of exercising):** first re-derive materialized only 4017/5079
  C2->C1 edges (79%). Root cause (source-confirmed): the producer resolved C2->C1 targets against the
  derive's SHORT in-memory node "id" (comp_aws_cli: EC2=InstanceId, LAMBDA=FunctionName, ...), but DS~B's
  emit targets use the CANONICAL ARN = comp-kuzu node_id (kuzu PK "arn-if-present-else-node_id",
  kuzu_nessie_load.py:145). Diverges for AWS-estate types -> estate-target edges dropped to
  VISIBLE-unresolved (never dangling; consistent, just incomplete). Pre-existing seam (debt materialize
  never hit it -- its ts_semantic targets carry no arn), NOT the additive change.
- **FIX (producer-side, CTO-BLESSED "fix the producer never the emit"):** index the present-set by
  n["arn"] || n["id"] (the canonical id-space the emit + final graph use). Re-derive: 4017 -> 5077/5079
  (+1060). The 2 remaining misses = genuine estate DRIFT (a deleted CW alarm + an ephemeral IAM inline-role,
  both confirmed ABSENT live). Commit **78a5fddbe**.
- **CTO SEMCTL CONTRACTS (3, all exercised):** canonical-id contract (in-producer doc); MANDATORY
  denominator report (edges_resolved=X/Y + LOUD C2C3_MOTIF_RESOLVE_INCOMPLETE WARN <100% -- fired live
  2/5124); generated NEGATIVE-control self-test (id-only DROPS estate-ARN edges 3630/5124 + arn-index
  recovers 5124/5124). Commit **88cc492ef**.
- **APPLIED CLOSE:** live @ HEAD nodes_snap=1276252256517924052 -- C2Motif=19/C3System=4, C2->C1 5077/5079
  (2 = explained drift), b-io overlap (object-data + pipeline), fidelity PASS, no-refreeze. DS~B's
  INDEPENDENT applied re-verify = PASS (set-diffed the same 2 drift targets). Deploy-ledger
  ab-canonical-motif-materialize CLOSED (4 legs). CVO cert + ~C re-census pending (COO-fired).

## WS-2 -- COMPSIMILAR PH1 resource_summaries store-writer (COMPLETE, gate-close routed to CTO)

Per CTO plan-gate PASS 141857Z + 4 binding conditions.

- **COND-1 in-VPC corpus-build path (the gating unknown) -- RESOLVED via CTO option-B:** summary_corpus
  read the graph by subprocessing comp-kuzu (needs a local Kuzu DB absent in the derive container). Took the
  cleaner option -- read graph_nodes/graph_edges DIRECTLY from Iceberg via the store's Nessie RestCatalog
  (pyiceberg is in the image; kuzu is not). `summary_corpus.build_corpus(graph_tuple=)` made
  source-agnostic (dev-box comp-kuzu path byte-identical); `resource_summaries_store.load_graph_from_iceberg()`
  mirrors the two comp-kuzu queries. LIVE: arn_nodes=1787 arn_edges=3285 loaded in-VPC, no comp-kuzu.
  Commit **e21baf35c** (+ Dockerfile 3-file COPY).
- **COND-2 TARGETED apply -- LANDED:** safe-apply -target the 5 resources ONLY (NO alert-drift). Plan
  5-add/0-change/0-destroy; live-verified; post-apply targeted 0-diff.
- **CORPUS-READ IAM GAP (cond-4 first-run exercise caught it):** AC-2 run#1 exit 1 -- AccessDenied on
  graph_nodes metadata read; the least-priv role was scoped to resource_summaries* only. My 22a tested the
  WRITE path but missed the GetObject the code needs FIRST. Minimal read-only fix (GetObject on
  graph_nodes*/graph_edges*, write surface UNCHANGED), CTO-APPROVED 210442Z. Commit **f24504ba7**.
- **COND-3 22a -- CLEAN on the final policy** (each isolated, ONE --resource-arns): GetObject
  graph_nodes/edges ALLOWED; PutObject graph_nodes + PutObject/GetObject opal-data-* all implicitDeny.
- **COND-4 AC-2 append-only -- EXERCISED + read-back PROVEN:** run#1 create+append v1 (1787); run#2
  present-not-recreated + append v2 (1787); S3-parquet read-back: summary_version {1:1699, 2:1699} balanced,
  every sampled arn has BOTH versions, never overwrite. Deploy-ledger compsimilar-ph1-store-writer CLOSED
  (5 legs). Gate-close evidence routed to CTO 211810Z.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-kuzu` / `comp-kuzu-inc` / `comp-kuzu-full` | WS-1 live-state grounding (pre/post-ingest counts, edge resolve, b-io overlap, node-id forms); provenance-header vintage discipline (caught SERVED-STALE inc-mode, advanced via -full) | PASS (Rule 20 header read every call) |
| `commit-gate.sh` | 5 .py commits (derive_runner x3, summary_corpus, resource_summaries_store) | PASS all |
| `safe-commit.sh` | 5 commits, pathspec-scoped, risk-reflex read | PASS (2 timed out on surface-check but landed) |
| `safe-apply.sh` | WS-2 TARGETED applies (5-resource + read-grant), HALTGT-gated | PASS (5-add then 1-change, 0-diff verified) |
| `deploy_ledger.py` | 2 ledgers open->close-leg->close (NEVER#5) | PASS (4 legs + 5 legs) |
| `terraform.exe plan` | targeted plans (5-resource, policy-change) pre-apply review | PASS (clean, no alert-drift) |
| `aws iam simulate-principal-policy` | 22a + re-22a, ISOLATED one-resource-arn each (Rule 22a) | PASS (positive allowed + negatives implicitDeny) |
| live AWS grounding (Rule 22a) | ecs run-task/wait/describe, ecr, codebuild, iam get-role, s3 cp+ls, CloudWatch (PowerShell for /ecs leading-slash) | PASS |

**What worked:** exercising the path (not reading config) caught BOTH material defects -- the WS-1 79%
edge-gap (derive log denominator) + the WS-2 corpus-read AccessDenied (AC-2 first-run). The sha-in-container
image discriminator (Rule 22a) proved bakes independent of resolvedSourceVersion. **What failed / caught:**
my WS-2 22a tested writes only and missed the read the code depends on -- lesson banked (enumerate the state
space the CODE touches, reads AND writes, before choosing controls; a write-only 22a can't catch a read-gap).
**Gap found:** the c2c3 producer's present-set id-space seam (now closed + guarded by the denominator report);
the store-writer role's corpus-read grant (now added, write-least-priv preserved).

## Blockers

None. Both workstreams complete. Remaining follow-ons are on OTHERS: CVO round-trip cert (WS-1) + ~C
re-census + CTO gate closes (both) -- all COO-coordinated; I am reachable for any rework.

## Current State (handoff)

- **WS-1 LIVE:** semctl C2/C3 layer at HEAD nodes_snap=1276252256517924052 -- C2Motif=19 (6 debt + 13 A+B) /
  C3System=4 (1 debt + 3 A+B: object-data/compute-orchestration/pipeline). derive image
  opal-globgrph-derive-runner:latest carries the additive+arn-fix+denominator producer (derive_runner.py
  ingest_c2c3_motif_producer, C2C3_MOTIF_SPEC_PATHS = both motif_c2c3_materialize{,_ab}.json baked). Nightly
  derive re-emits it persistently. The 2 unresolved C2->C1 targets are genuine estate drift, not a seam.
- **WS-2 LIVE:** globgrph.resource_summaries Iceberg table created + 2 append-only versions (1787 arns each).
  Task-def globgrph-resource-summaries-producer:1 (image :latest, cmd `python /app/resource_summaries_store.py
  --build-append`), role opal-globgrph-resource-summaries-producer-task (RW resource_summaries* + READ-ONLY
  graph_nodes*/graph_edges*, denies everything else incl opal-data-*). No schedule (PH1 on-demand). Corpus
  built in-VPC by reading Iceberg directly (no comp-kuzu/kuzu in-container).
- **The derive image was rebuilt 3x this session** (WS-1 additive, WS-1 arn-fix, WS-1 denominator) + 1x for
  WS-2 (store-writer trio). Current :latest = the WS-2 rebuild (5289c700), which INCLUDES all WS-1 producer
  changes (they were committed before it).
- Commits (all pushed CLOUD): 8547b069d, 78a5fddbe, 88cc492ef (WS-1); e21baf35c, f24504ba7 (WS-2).

## Next Steps

- **[3.0.0_SA_CVO]** WS-1 round-trip cert on HEAD 1276 (re-exercises resolve); WS-2 store-writer if in scope.
- **[0.8.0_AE_CloudComp~C]** WS-1 re-census (structure + edge denominator) vs spec @7892f3fbc; WS-2 corpus
  quality / PH2 motif-enrichment (canon-patterns.yaml is PH2-gated, degrades best-effort in-container now).
- **[1.0.0_SA_CTO]** close the COMPSIMILAR store-writer gate on the WS-2 exercised evidence (routed 211810Z);
  signal the WS-1 APPLIED close on CVO/~C all-clear.
- **[2.0.0_SA_COO]** both owned surfaces done; fire CVO + await ~C; next tasking. 3 pre-wake TOs
  (DATA_PLATFORM DC1/DC2 crawls, NFRA_COMPLEARN AMD-P3a) still pending -- confirm still-active before I start.
- **[0.4.0_DS_ClientPlatform~B]** WS-1 applied re-verify PASS delivered; standing.
