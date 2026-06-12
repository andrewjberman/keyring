# 0.7.0_AE_CloudOps -- work tick 2026-06-12 ~1945Z

**archetype:** EXPLORE
**secondary_archetypes:** VALIDATE, SCRIBE

## Window

~1930Z session restart (RAVC3 ACCEPTED, D8-AE Part B COMPLETE) -> ~1945Z. Context-exhausted session resumed; TO-D1 [GO] received from COO.

## Commits this window

- `03ea4aed1` debtscan(D1): Phase 1+2+3 reachability sweep ledger (2026-06-12_D1_reachability_candidates.md)

## NFRA_DEBTSCAN TO-D1 — Phase 1+2+3 Complete

### Phase 1 — Entry-Point Enumeration + Sweeps

**Kuzu schema discovery:** Node table = CloudNode (node_id, arn, node_type, name, layer, drift_class, source, snapshot_ts); Edge table = CloudEdge (edge_type, layer). Primary key = node_id (not id — corrected after initial query failure).

**Edge types present:** READS(566), WRITES(517), HAS_POLICY(355), ASSUMES(170), READS_SECRET(158), EMITS_TO(101), TRIGGERS(97), ENCRYPTS_WITH(35), INVOKES(26), NOTIFIES(26), HAS_PROFILE(23), MONITORS(16), PUBLISHES_TO(15), GRANTS(13), SUBSCRIBES(5), ORIGIN(5), LOGS_TO(5), USES_OAI(4), DEAD_LETTERS_TO(3), USES_OAC(1)

**Nessie entry-point set (99 nodes):** 98 EVENT_RULE + 1 CLOUDFRONT_DISTRIBUTION (EVTSA9VEHNZVH). 61 Lambdas EventBridge-reachable via TRIGGERS. 1 orphaned EVENT_RULE: `opal-globgrph-derive-runner-nightly` (targets ECS, not Lambda — FP_ECS_TRIGGER).

**Stitch entry-point set (127 nodes):** adds 6 API_GW + 3 SCHEDULE + 19 SSM_DOCUMENT.

**Known coverage gaps:** API_GW→Lambda edges absent (0 API_GW outbound edges); ECS TRIGGERS not modeled; Lambda@Edge TRIGGERS not modeled; EC2 SSM invocation not modeled.

**Nessie forward sweep — 259 isolated nodes:**
- LOG_GROUP: 190 (FP_LOG_GROUP_IMPLICIT_LOGS)
- SECRET: 40 (FP_SECRET_RUNTIME_ACCESS)
- S3_BUCKET: 9 (6 FP_INFRA_BUCKET + 3 investigate)
- S3_BUCKET_POLICY: 7 (FP_BUCKET_POLICY_NO_RESOURCE_EDGE)
- KMS_KEY: 5 (pending investigation)
- DYNAMODB_TABLE: 3 (2 FP_NESSIE_INTERNAL_DDB + 1 NEEDS-VERIFY: opal-partner-demo)
- SNS_TOPIC: 2 (trade-pipeline-ses-bounces, trade-pipeline-ses-complaints — REAL candidates)
- CW_ALARM: 2 (FP_CW_ALARM_IMPLICIT_MONITOR: exec-summary-*)
- EC2_INSTANCE: 1 (seeking-alpha-scraper — FP_EC2_SSM_INVOKED, likely)

**Stitch backward sweep:**
- 6 isolated S3_DATA_KEY: consolidated/smartx_allocations.parquet, json/mdpf/global/aggregate-aua-timeseries.json, json/portfolios/aum-timeseries.json, security-reports/*_security_report.txt, seeking-alpha/analysis/manifests/*/layer25_dedup_report.json, views/account_distribution.json
- 36 orphaned script-level GOLD_SCRIPT: 21 E_* diagnostic (FP_DIAG_ADHOC), 2 test/shadow (FP_TEST_SCRIPT), ~6 FP_RUN_SCRIPT_SUBPUBLISHER, remainder NEEDS-VERIFY
- opal-data-cot: written-not-read FP — has CloudFront ORIGIN edge (FP_S3_CF_ORIGIN)

**Key findings:**
- `bd-time-machine` Lambda: 0 TRIGGERS, 0 INVOKES inbound; READS+WRITES opal-data-bd; ASSUMES bd-time-machine-lambda-role. Confirmed REAL per memory ("never built; exploratory").
- `trade-pipeline-ses-bounces/complaints` SNS: 0 edges; peer SNS topics have modeled subscribers; ADHC_CDNCOHT teardown possible orphan. LIKELY-REAL.
- `opal-data-aaii-v2`, `opal-data-etfs`: 0 Lambda edges; yang ETF Lambda reads portal-v2 not these buckets. NEEDS-VERIFY (EC2 runner check).
- `INF_D_04b.client_publishers`: orphaned script-level GOLD_SCRIPT (likely _run_script subpublisher, FP_RUN_SCRIPT_SUBPUBLISHER).

### Phase 2 — Suppression Config

`org/modules/graph/debtscan/suppression_v1.yaml` authored on disk. 14 classes documented + 3 Day-0 known findings. File is exec-only (owned-paths hook blocked AE commit); routed to COO for exec commit in RAVC2.

### Phase 3 — CVO Precision Sample

10 findings filed in `2026-06-12_D1_reachability_candidates.md`. Committed at `03ea4aed1`.

| # | finding | verdict |
|---|---|---|
| 1 | bd-time-machine Lambda | CONFIRMED REAL |
| 2-3 | trade-pipeline-ses SNS (x2) | LIKELY-REAL |
| 4-5 | opal-data-aaii-v2, opal-data-etfs S3 | NEEDS-VERIFY |
| 6 | opal-partner-demo DDB | NEEDS-VERIFY |
| 7-8 | INF_A_-1, INF_A_02 GOLD_SCRIPT | NEEDS-VERIFY |
| 9-10 | views/account_distribution.json, json/portfolios/aum-timeseries.json | NEEDS-VERIFY |

## RAVC2

Sent to 2.0.0_SA_COO + CC 3.0.0_SA_CVO. Requested:
1. CVO adjudication of precision sample (>=0.80 gate for non-ADVISORY promotion)
2. Exec commit of suppression_v1.yaml (COO or CTO)
3. TO-D2 AE lane pre-authorized (queued after RAVC2)

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-kuzu (nessie) | CALL show_tables; CALL table_info CloudNode/CloudEdge; entry-point enumeration; isolation sweep; targeted investigations (bd-time-machine, trade-ses, aaii/etfs, SNS, DDB, EC2) | PASS — valid provenance, zero mutations |
| comp-kuzu (stitch) | GOLD_SCRIPT script-level orphan sweep; S3_DATA_KEY isolation; PORTAL_COMPONENT check; edge semantics discovery | PASS — valid provenance, zero mutations |

What worked: graph schema discovery (node_id not id; CloudNode not Node); regexp_full_match for two-colon filter; SUBSCRIBES edge distribution to confirm trade-ses SNS truly has no subscribers.
What failed: initial queries used wrong property name `id` (corrected first try). REPLACE() function unavailable in Kuzu (used regexp_full_match instead).
Gap found: API_GW→Lambda edges entirely absent from graph — 60+ API-invoked Lambdas appear as orphans. Suppressed as FP_API_LAMBDA class. Documented for graph build improvement.

## Current State

- TO-D1: COMPLETE. Ledger committed `03ea4aed1`. RAVC2 sent to COO + CVO.
- suppression_v1.yaml: authored on disk, routed for exec commit.
- TO-D2 AE lane: queued (pre-authorized; start after TO-D1 RAVC2 ack).
- D8-AE blocking-flip: first gate opportunity tonight at 02:00Z nightly run.
- OPEN: TO-D2 comp-iam gaps → NFRA_OPLMCP.01 → NFRA_COSTAWS W3/W4/W5.

## Next Steps

- [3.0.0_SA_CVO] Adjudicate precision sample
- [2.0.0_SA_COO] Exec-commit suppression_v1.yaml
- [0.7.0_AE_CloudOps] TO-D2 AE lane: comp-iam gaps estate sweep
