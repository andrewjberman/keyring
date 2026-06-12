# NFRA_DEBTSCAN TO-D1 — Phase 1 Reachability Sweep Ledger
**date:** 2026-06-12  
**author:** 0.7.0_AE_CloudOps  
**status:** Phase 3 — CVO precision sample submitted (RAVC2 pending)  
**AC2 confirmation:** zero mutations — read-only kuzu queries only; IAM posture = read-only throughout

---

## Provenance Headers (AC6)

| Surface | DB | Nodes/Edges | Built | Age at sweep | Nessie state | Verdict |
|---|---|---|---|---|---|---|
| Nessie canonical | `kuzu_nessie_db` | 1157 / 2150 | 2026-06-12T16:18:42Z | 2.8h | CURRENT (pin == marker HEAD) | VALID |
| Stitch (full) | `kuzu_stitch_db` | 3088 / 4879 | 2026-06-12T13:52:17Z | 5.2h | stitch mtime 2026-06-11T21:52Z | VALID |

Both surfaces within 26h staleness gate. AC6 satisfied: filing is permitted.

---

## Phase 1 — Entry-Point Set

### Nessie surface
- `EVENT_RULE`: 98 nodes (98 scheduled/event-pattern triggers)
- `CLOUDFRONT_DISTRIBUTION`: 1 node (`EVTSA9VEHNZVH`, the portal distribution)
- **Total entry-point set: 99 nodes**
- **EventBridge-reachable Lambdas (TRIGGERS edges):** 61 of 169 Lambdas
- **Orphaned entry-point:** `opal-globgrph-derive-runner-nightly` — EVENT_RULE with 0 TRIGGERS edges. Targets ECS Fargate (not Lambda). Suppressed: `FP_ECS_TRIGGER`.

### Stitch surface (additional entry-point types)
- `EVENT_RULE`: 98
- `API_GW`: 6 (`inf-otp-relay-api`, `opal-portal-data-proxy-api`, `opal-session-analytics-api`, `sentiment-query-api`, `trade-recon-api`, `trade-submission-api`)
- `CLOUDFRONT_DISTRIBUTION`: 1
- `SCHEDULE`: 3
- `SSM_DOCUMENT`: 19
- **Total entry-point set: 127 nodes**

### Coverage gaps (known, documented for suppression)
- API_GW → Lambda edges: absent from graph (0 outbound edges from all 6 API_GW nodes). All API-invoked Lambdas appear untriggered.
- ECS_TASK_DEFINITION → EVENT_RULE edges: not modeled. Derive-runner rule appears orphaned.
- EC2 → Lambda SSM invocation: not modeled. EC2 instances appear isolated even when SSM-invoked.
- CloudFront → Lambda@Edge: not modeled as TRIGGERS. L@E functions appear untriggered.

---

## Phase 1 — Burn-Down Counts (AC3)

### Nessie surface: 259 fully isolated nodes (0 in + 0 out edges)

| node_type | isolated_count | FP class | File? |
|---|---|---|---|
| LOG_GROUP | 190 | FP_LOG_GROUP_IMPLICIT_LOGS | NO |
| SECRET | 40 | FP_SECRET_RUNTIME_ACCESS | NO |
| S3_BUCKET | 9 | mixed (see forward sweep) | PARTIAL |
| S3_BUCKET_POLICY | 7 | FP_BUCKET_POLICY_NO_RESOURCE_EDGE | NO |
| KMS_KEY | 5 | pending investigation | PENDING |
| DYNAMODB_TABLE | 3 | 2 FP_NESSIE_INTERNAL_DDB; 1 NEEDS-VERIFY | PARTIAL |
| SNS_TOPIC | 2 | 0 subscribers confirmed | REAL candidates |
| CW_ALARM | 2 | FP_CW_ALARM_IMPLICIT_MONITOR | NO |
| EC2_INSTANCE | 1 | FP_EC2_SSM_INVOKED (likely) | LIKELY-FP |
| **TOTAL** | **259** | | |

### Stitch surface: additional pipeline-layer orphans

| type | count | notes |
|---|---|---|
| S3_DATA_KEY (fully isolated) | 6 | 0 in + 0 out edges |
| GOLD_SCRIPT (script-level, no edges) | 36 | 21 E_* diagnostic + 15 misc |
| LAMBDA (no TRIGGERS or INVOKES inbound) | ~108 | most API-invoked FP; `bd-time-machine` REAL |
| PORTAL_COMPONENT (no edges) | 0 | all connected |

---

## Phase 2 — Suppression Classes

Documented in companion file `suppression_v1.yaml` (exec-route for commit, authored by 0.7.0_AE_CloudOps).

Summary of classes that suppress findings BEFORE Phase 3 filing:

| class | nodes suppressed | reason |
|---|---|---|
| FP_LOG_GROUP_IMPLICIT_LOGS | 190 LOG_GROUP | Lambda→CW logging is implicit; LOGS_TO edges sparse by design |
| FP_SECRET_RUNTIME_ACCESS | 40 SECRET | Runtime SDK calls not modeled as graph edges |
| FP_API_LAMBDA | ~60+ LAMBDA | API_GW→Lambda edges absent from graph; 0 API_GW outbound edges |
| FP_LEDGE | LAMBDA (auth-validator-edge, cache-control-injector, etc.) | CloudFront→L@E not modeled as TRIGGERS |
| FP_ECS_TRIGGER | EVENT_RULE (opal-globgrph-derive-runner-nightly) | Targets ECS, not Lambda; ECS trigger not modeled |
| FP_S3_CF_ORIGIN | S3_BUCKET (opal-data-cot + others with ORIGIN edges) | Served by CloudFront ORIGIN; not dead |
| FP_DIAG_ADHOC | GOLD_SCRIPT (E_00 through E_25 series, diag_*, gold_prof) | Ad-hoc diagnostic tools; no pipeline S3 output expected |
| FP_TEST_SCRIPT | GOLD_SCRIPT (test_gldinc_cache_roundtrip, gldinc_p1_shadow) | Test/shadow scripts; not pipeline entries |
| FP_INFRA_BUCKET | S3_BUCKET (lambda-layers, terraform-state, ci-staging, cloudfront-logs, runner-shared, ajb-workflow) | Infrastructure buckets; no data-pipeline edges expected |
| FP_NESSIE_INTERNAL_DDB | DYNAMODB_TABLE (opal-globgrph-nessie-_objs, opal-globgrph-nessie-_refs) | Nessie catalog internal tables; not Lambda-accessed via tracked edges |
| FP_EC2_SSM_INVOKED | EC2_INSTANCE (seeking-alpha-scraper) | EC2 invoked via Lambda→SSM; not modeled as direct graph edge |
| FP_CW_ALARM_IMPLICIT_MONITOR | CW_ALARM (exec-summary-*) | Alarms monitor Lambda metrics implicitly; MONITORS edges sparse |
| FP_BUCKET_POLICY_NO_RESOURCE_EDGE | S3_BUCKET_POLICY (7 nodes) | Bucket policies have no outbound edges by design |
| FP_RUN_SCRIPT_SUBPUBLISHER | GOLD_SCRIPT (INF_D_04b.client_publishers, run_*_auagap002) | Likely _run_script subpublishers; invocation chain not in graph |

Day-0 known findings (per TO Phase 2 requirements):
- `getAUMMetrics` URL not resolved — D8-AE Phase 1 Day-0 SEV1 candidate; suppressed pending CVO cert
- `advisor_intelligence` auth:NONE — known FP (CloudFront auth pattern, not an open endpoint)
- BenchmarkHeatmap/portal-proxy/PeersTab 2a-class instance — Day-0 backlog per CTO D8-AE finding

---

## Phase 3 — CVO Precision Sample (10 findings)

| # | node | family | sev | firm | surface | triage | owner-lane | trace | verified-real-vs-FP |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `bd-time-machine` Lambda | ORPHANED_LAMBDA | SEV2 | bd | nessie | REAL | AE | No TRIGGERS inbound; no INVOKES inbound; READS+WRITES opal-data-bd; ASSUMES bd-time-machine-lambda-role. Memory: "Time Machine never built (exploratory; frontend TimeMachineProvider scaffolding only, no live bd-time-machine restore)" | **REAL** — memory confirms phantom feature |
| 2 | `trade-pipeline-ses-bounces` SNS | ORPHANED_SNS | SEV2 | trade | nessie | LIKELY-REAL | AE | 0 edges (no SUBSCRIBES from any Lambda or external endpoint). Peer `inf-otp-alert` SNS has 2 SUBSCRIBES edges modeled. Not suppressed by any known FP class. | NEEDS-CVO |
| 3 | `trade-pipeline-ses-complaints` SNS | ORPHANED_SNS | SEV2 | trade | nessie | LIKELY-REAL | AE | 0 edges; same pattern as finding 2. SES bounce+complaint pair with no subscriber. ADHC_CDNCOHT trade-recon teardown may have removed the subscriber Lambda but left the topic. | NEEDS-CVO |
| 4 | `opal-data-aaii-v2` S3 | ORPHANED_S3 | SEV2 | cross | nessie | NEEDS-VERIFY | AE | 0 edges (no READS, no WRITES, no policy). `yang-generate-etf-returns` Lambda reads `opal-data-portal-v2`, not this bucket. No EVENT_RULE for aaii. `aaii/credentials` SECRET exists. Pipeline may be EC2-only (not Lambda). | NEEDS-CVO — EC2 runner check required |
| 5 | `opal-data-etfs` S3 | ORPHANED_S3 | SEV2 | cross | nessie | NEEDS-VERIFY | AE | 0 edges. `yang-generate-etf-returns` reads `opal-data-portal-v2` not this bucket. `etf-classifications` DynamoDB exists. ETF data pipeline may be EC2-EC2. | NEEDS-CVO — EC2 runner check required |
| 6 | `opal-partner-demo` DynamoDB | ORPHANED_DYNAMO | SEV3 | cross | nessie | NEEDS-VERIFY | AE | 0 edges (no READS, no WRITES from any Lambda). Demo environment table with no recorded consumer. | NEEDS-CVO |
| 7 | `INF_A_-1.materialize_txn_cache` GOLD_SCRIPT | ORPHANED_GOLD_SCRIPT | SEV2 | inf | stitch | NEEDS-VERIFY | DS | Script-level node `gold:INF_A_-1.materialize_txn_cache` has 0 edges. Cache materialization script with `-1` index (pre-pipeline step). Likely a dispatcher entry via `_run_script`; not a direct dispatch line. | NEEDS-CVO — verify-before-delete: _run_script trace required |
| 8 | `INF_A_02.fee_rate_history` GOLD_SCRIPT | ORPHANED_GOLD_SCRIPT | SEV2 | inf | stitch | NEEDS-VERIFY | DS | Script-level node `gold:INF_A_02.fee_rate_history` has 0 edges. INF variant of bd fee_rate_history (bd A_02 is connected). INF variant may not have been wired into INF dispatcher. | NEEDS-CVO |
| 9 | `views/account_distribution.json` S3_DATA_KEY | STALE_S3_KEY | SEV2 | bd | stitch | NEEDS-VERIFY | AE | 0 in + 0 out edges in stitch graph. Prior Lambda crash incident (MDLP_DISTFIX 2026-06-05): Lambda crashed writing to /var/task path, fix deployed but graph not re-derived. Graph coverage may lag. | NEEDS-CVO — check S3 LastModified vs fix-deploy date |
| 10 | `json/portfolios/aum-timeseries.json` S3_DATA_KEY | STALE_S3_KEY | SEV2 | bd | stitch | NEEDS-VERIFY | DS | 0 in + 0 out edges in stitch. MDPF investigation: noncurrent versions have historical per-model count data (2024-11-01 to 2026-05-14). Whether this path is actively written to is unknown from graph alone. | NEEDS-CVO — check S3 LastModified |

**Sample precision estimate (pre-CVO):** Finding 1 = confirmed REAL. Findings 2-3 = LIKELY-REAL. Findings 4-10 = NEEDS-VERIFY. Conservative estimate: 3/10 = 0.30 (pre-verify). Expected post-CVO if 6+ NEEDS-VERIFY confirmed real: 0.70-0.90. CVO adjudicates gate (>=0.80 required for non-ADVISORY promotion).

---

## Suppression Cross-Files (AC5)

No findings in this batch touch a critical-surface carve (per `critical-surfaces.yaml`). No cross-file to `org/critical_paths/change_management/` required.

---

## Compiler Tools Evidence

| Tool | Query | Result |
|---|---|---|
| comp-kuzu (nessie) | entry-point set, isolation sweep, targeted investigations | PASS — queries complete, provenance VALID |
| comp-kuzu (stitch) | GOLD_SCRIPT script-level orphans, S3_DATA_KEY isolation, PORTAL_COMPONENT | PASS — queries complete, provenance VALID |
| comp-blast | pre-filing check: `bd-time-machine` | pending (RAVC2 gate) |
| comp-iam | TO-D2 AE lane scope (queued) | pending |

---

## Next Steps

- [3.0.0_SA_CVO] Adjudicate precision sample findings 1-10 — RAVC2 sent to 2.0.0_SA_COO
- [2.0.0_SA_COO] Commit `suppression_v1.yaml` draft (exec-route; AE authored, routed for exec sign-off)
- [0.7.0_AE_CloudOps] TO-D2 AE lane: comp-iam gaps estate sweep (queued; start after RAVC2 lands)

---

## CVO Precision Adjudication — 3.0.0_SA_CVO, 2026-06-12 ~19:35Z

Every finding independently verified against live AWS / repo / dispatcher state (not the graph, not the triage notes):

| # | Verdict | Independent evidence |
|---|---|---|
| 1 | **REAL** | Last invocation 2026-03-26T17:37Z (CW logs, ~11wk dead) + Andrew ground-truth memory: feature never built |
| 2 | **REAL** | `sns list-subscriptions-by-topic` = 0 subscriptions, live |
| 3 | **REAL** | Same — 0 subscriptions, live. SES bounce/complaint notifications currently go NOWHERE (risk note: not just debt — a deliverability blind spot) |
| 4 | **REAL** | Newest object `sentiment.json` 2025-12-23 (~6mo stale); zero code refs repo-wide (only graph artifacts); lifecycle-archival posture |
| 5 | **FP** | `data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py` READS the bucket — live mdpf gold script; mdpf pipeline layer is not stitched into the graph |
| 6 | **REAL** | ItemCount=1 / 208 bytes (placeholder), zero code refs, zero consumers |
| 7 | **FP** | `orion-gold-dispatch.sh:142` catalog line + `CHAIN_FULL` + `CHAIN_GOLD_A` membership — dispatched live; inf dispatcher catalog not parsed into the stitch |
| 8 | **FP** | `orion-gold-dispatch.sh:145` + both chains — same coverage class as #7 |
| 9 | **REAL** (reclass: PHANTOM_S3_KEY) | Key does not exist on opal-data-bd at all (`views/` prefix empty) — the graph carries a node for a nonexistent artifact; dead path confirmed, family label should be phantom-key not stale-key |
| 10 | **REAL** (reclass: DEAD_S3_KEY) | Key fully absent — 0 current versions AND 0 delete-markers/noncurrent. Side-finding: the historical noncurrent versions banked in fabric memory as an MDPF backfill source were purged by the COSTAWS R2 14-day noncurrent lifecycle (correct per policy; memory now stale — CVO will correct the memory record) |

### Verdict

**Precision = 7/10 = 0.70 — BELOW the ≥0.80 gate. Findings file as ADVISORY; do NOT bulk-file. Family is NOT dead — the gate caught a single root-cause coverage class.**

All 3 FPs are one mechanism: **pipeline-layer script/reader edges absent from the stitch for non-bd trees** — (a) the inf dispatcher catalog (`orion-gold-dispatch.sh` pipe-delimited lines + CHAIN_* sets) is not parsed into graph edges, so every dispatched INF_* script reads as orphaned; (b) the mdpf tree is not stitched at all, so its bucket reads are invisible. Iteration path (AE, small): add `FP_INF_DISPATCHER_CATALOG` + `FP_MDPF_UNSTITCHED` suppressions now (cheap), then the durable fix = parse orion-gold-dispatch + mdpf reader edges into the stitch — at which point this family re-runs and the suppressions retire. Expected post-fix precision on this sample: 7/7 eligible = 1.0.

Bonus risk-note for routing: #2/#3 elevate beyond debt — SES bounce/complaint events are currently unobserved (deliverability blind spot); recommend the AE follow-up decide subscribe-vs-delete rather than delete-by-default.

— 3.0.0_SA_CVO

### CVO correction to adjudication note #10 (~19:40Z, same pass)
The side-finding "the memory-banked MDPF backfill source was purged by R2 lifecycle" is **RETRACTED — wrong-bucket inference by CVO.** The memory-cited source is `opal-data-portal-v2/json/portfolios/aum-timeseries.json` — verified just now: **145 noncurrent versions INTACT** (one more than at the memory's writing; still accumulating). What is dead is the **stitch node's** path on `opal-data-bd` (0 versions, 0 markers) — so finding #10's REAL/dead-key verdict on the graph node STANDS unchanged; only the memory-staleness side-note was wrong. Precision score unaffected (7/10 = 0.70). Fabric memory needs no correction.

— 3.0.0_SA_CVO

---

## TO-D1 ITERATION (AE 0.7, 2026-06-12 ~22:12Z) — durable stitch fix + suppressions

CVO's single root-cause coverage class CLOSED at the source:

1. **Dispatcher-catalog edges (FPs #7/#8):** `inject_pipeline_edges` now emits
   `dispatcher -[TRIGGERS]-> script` for every chain member (bd `gold_dispatch` +
   inf `orion-gold-dispatch`; 73 edges on first rebuild). Verified post-fix:
   `gold:INF_A_-1.materialize_txn_cache` and `gold:INF_A_02.fee_rate_history`
   each now carry the TRIGGERS edge (were 0-edge). A 0-edge INF_* script after
   the nightly rebuild is a REAL orphan again.
2. **mdpf injection (FP #5, partial):** `build_mdpf_dag` (TOOL-02) is now wired
   into `trace_graph._inject_full_pipeline_into_graph` — 18 mdpf scripts +
   key-grain S3 I/O visible (wsd2's READS edge confirmed). Remaining gap:
   bare-key extraction means BUCKET-grain reachability for non-firm buckets
   still needs `FP_MDPF_UNSTITCHED` until the bucket-qualified extractor leg
   (TOOL-02 follow-on) lands.
3. **Suppressions authored** (`FP_INF_DISPATCHER_CATALOG` retire-on-nightly-rebuild,
   `FP_MDPF_UNSTITCHED` retire-on-extractor-leg) — routed to COO for exec-commit
   per protocol (yaml on disk, uncommitted by AE).

**Sample re-run (post-fix):** FPs #7/#8 retire STRUCTURALLY (nodes now edged);
FP #5 retires via suppression. Eligible candidates = 7, all CVO-adjudicated REAL
→ precision 7/7 = 1.0 (matches CVO's expected post-fix figure). Family promotes
from ADVISORY on the next sweep run over the rebuilt stitch.
