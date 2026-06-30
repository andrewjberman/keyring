# NFRA_GRAPHUNI.P0-B — INFRA + CROSS-STRATUM denominator slice (~B)

**TO:** NFRA_GRAPHUNI.P0-B (org/projects/NFRA_GRAPHUNI/task_orders/NFRA_GRAPHUNI.P0-B.infra-crossstratum-audit.md)
**Author:** 0.8.0_AE_CloudComp~B (GRAPHDEPTH by-stratum fleet — INFRA + CROSS-STRATUM populator)
**Date:** 2026-06-30
**Status:** DELIVERED — READ-ONLY audit, ZERO graph mutation. RAVC2 -> COO~B, cc CTO + ~C + ~D + ~A.
**Scope guard honored:** AUDIT + denominator slice ONLY. No derive, no edge population, no mutation. Phase-B population (the cross-stratum stitchers) DEPENDS on ~D's compute (PipelineScript nodes) + ~A's storage (S3Key nodes) existing.

---

## 0. Grounding + VINTAGE (read this first — the graph is stale)

| Side | Artifact | Vintage | Census |
|---|---|---|---|
| **Unified graph (Kuzu/Nessie)** | `kuzu_nessie_db`, marker-headed | comp-kuzu local build **06-30 19:34:59Z** (provenance "current, pin == marker HEAD") — **BUT data vintage = the `graph_nodes` Iceberg snapshot of 2026-06-29 22:11** (latest commit; nothing since ~23h) | 18,216 nodes / 30,481 edges |
| **Live AWS (ground truth)** | live estate, this session | now (06-30 ~21:40Z) | EC2 **31**, Lambda **174** |

**The vintage caveat is load-bearing (Andrew-probed 06-30 21:35Z):** comp-kuzu's `age: 1.9h` is the LOCAL re-materialization age, NOT the data age. The underlying `graph_nodes` Iceberg table last committed **2026-06-29 22:11** — `graph_edges` is nightly-derive-only (06-26/-27/-28/-29 ~22:08–22:11; tonight's pending). So the graph CONTENT is ~23h old. **Proof:** the 4 Lambdas deployed TODAY (`opal-{cot,inf}-value-parity`, `opal-{cot,inf}-served-guard`, 15:40–20:13Z) = **0 rows** in the graph; live Lambda **174** vs graph **169**. The incremental-updater (`opal-globgrph-incremental-updater`) is firing (~20×/3h, 0 errors, SQS depth 0, DLQ 0) but every batch logs `BATCH_END nodes_written=0` — a silent no-op; no `graph_nodes` commit since 06-29 22:11. (See §4 F3 — flagged to COO~B + 0.7.0, the globgrph lane.)

**Consequence for this denominator:** infra **node counts** are grounded on **LIVE AWS** (174 Lambda / 31 EC2), not the graph's stale 169. The **structural** conclusions (the cross-stratum edge types `RUNS`/`CALLS`/`READS_S3`/`WRITES_S3` = **0**) are SCHEMA facts, unaffected by vintage — verified 0 rows at the marker head.

**Read-only attestation:** every comp-kuzu call was `MATCH … RETURN` (no CREATE/MERGE/SET/DELETE). Live-AWS calls were `list-functions` / `describe-instances` / `s3 ls` / `cloudwatch get-metric-statistics` / `logs filter-log-events` (read-only). Zero mutation.

---

## 1. THE INFRA STRATUM (resource grain) — EXISTS

### 1a. Infra node census (the resource-grain denominator)
Grounded `comp-kuzu` (aws layer, 1,451 nodes) + live deltas:

| node_type | graph (06-29 vintage) | live | note |
|---|---|---|---|
| **LAMBDA** | 169 | **174** | +5 live (4 are today's value-parity/served-guard; graph stale) |
| **EC2_INSTANCE** | 31 | **31** | match — the pipeline runners (§2a) |
| S3_BUCKET | 35 | — | the rollup coarse target (READS/WRITES); ~A owns S3Key drilldown |
| DYNAMODB_TABLE | 34 | — | |
| IAM_ROLE | 145 | — | LAMBDA ASSUMES (169), EC2 HAS_PROFILE->INSTANCE_PROFILE (30) |
| IAM_POLICY | 312 | — | |
| INSTANCE_PROFILE | 17 | — | EC2 binding |
| EVENT_RULE | 116 | — | EC2/Lambda EMITS_TO/TRIGGERS |
| EVENT_SOURCE | 82 | — | |
| SECURITY_GROUP | 23 | — | Lambda IN_VPC |
| SECRET | 76 | — | EC2 READS_SECRET 85 / Lambda 159 |
| SNS_TOPIC | 13 | — | PUBLISHES_TO |
| SQS_QUEUE | 5 | — | |
| KMS_KEY | 8 | — | ENCRYPTS_WITH |
| API_GW / API_ROUTE | 5 / 77 | — | |
| LOG_GROUP | 200 | — | Lambda LOGS_TO |
| CW_ALARM | 64 | — | |
| S3_BUCKET_POLICY | 9 | — | |
| SERVICE_PRINCIPAL | 16 | — | |
| ECS_TASK_DEFINITION / ECS_CLUSTER | 3 / 1 | — | |
| VPC_ENDPOINT / ROUTE53_RECORD | 3 / 3 | — | |
| LOAD_BALANCER / IAM_USER / CLOUDFRONT_DISTRIBUTION / STATE_MACHINE | 1 each | — | singletons |

### 1b. Existing resource-grain coarse edges (the rollup coarse targets — they EXIST at BUCKET grain)
| from | edge_type | to | count |
|---|---|---|---|
| EC2 | READS | S3_BUCKET | 69 |
| EC2 | WRITES | S3_BUCKET | 47 |
| EC2 | READS_SECRET | SECRET | 85 |
| EC2 | READS / WRITES | DYNAMODB_TABLE | 30 / 30 |
| EC2 | HAS_PROFILE | INSTANCE_PROFILE | 30 |
| EC2 | EMITS_TO / PUBLISHES_TO / ENCRYPTS_WITH | EVENT_RULE / SNS / KMS | 4 / 4 / 4 |
| LAMBDA | READS | S3_BUCKET | 303 |
| LAMBDA | WRITES | S3_BUCKET | 259 |
| LAMBDA | READS / WRITES | DYNAMODB_TABLE | 244 / 207 |
| LAMBDA | ASSUMES | IAM_ROLE | 169 |
| LAMBDA | READS_SECRET | SECRET | 159 |
| LAMBDA | INVOKES | LAMBDA | 13 |
| LAMBDA | LOGS_TO / ENCRYPTS_WITH / IN_VPC | LOG_GROUP / KMS / SECURITY_GROUP | 7 / 7 / 1 |

These are coarse, **bucket-grain** `READS`/`WRITES`. The net-new fine edges (§2) drill them to **key grain** (`READS_S3`/`WRITES_S3` -> `S3Key`); the rollup invariant binds coarse<->fine (§2 R1). See §4 F2 — the coarse edge_type (`READS`) vs the fine (`READS_S3`) needs ~C reconciliation.

---

## 2. THE CROSS-STRATUM STITCHERS (NET-NEW — the keystone; **0 today**, grounded)

The fractal seams that fuse the infra island to ~D's compute island + ~A's storage island. **Verified 0 at the marker head** (`RUNS`/`CALLS`/`READS_S3`/`WRITES_S3` all returned 0 rows). Each is N-party per the spanned strata (CTO sharpening 212036Z) — flagged so the /seams sign-off set is known.

| # | Stitcher | edge_type | stratum-pair | today | expected magnitude | **/seams sign-off** |
|---|---|---|---|---|---|---|
| **S1** | `EC2_INSTANCE -RUNS-> PipelineScript` | RUNS | resource→compute | 0 | per pipeline-runner (§2a) | **~B + ~D + ~C** (tri) |
| **S2** | `LAMBDA -CONTAINS-> handler` | CONTAINS | resource→object | 0 | 174 lambdas → handler fn | **~B + ~D + ~C** (tri) |
| **S3** | `LAMBDA -READS_S3/WRITES_S3-> S3Key` | READS_S3 / WRITES_S3 | resource→object | 0 at key grain (303/259 exist at bucket grain) | **327 edges**, 87 lambda-only keys + 13 shared | **~B + ~A + ~C** (tri); 13 shared = **~B + ~D + ~A + ~C** (four) |
| **R1** | rollup `EC2/LAMBDA READS S3_BUCKET` (coarse) **⇐** `PipelineFunction READS_S3 S3Key` (fine) | existential (RUNS+CONTAINS+OWNED_BY) | resource⇄object | coarse exists (69+303), fine=0 → **all coarse UNSUPPORTED today** | OR-rollup per `rollup_defects()` | **~B + ~D + ~A + ~C** (four) |

`producer_by_pair` (for ~C to encode): `{resource→compute: ~B (RUNS)}`, `{resource→object[lambda]: ~B (CONTAINS, READS_S3/WRITES_S3)}`. Distinct from ~D's `{compute→object: ~D}`.

### 2a. The EC2-RUNS keystone map (which runner runs which pipeline) — 31 instances / 23 distinct roles
The expected `EC2 -RUNS-> PipelineScript` set, at runner→pipeline/tier grain. Per-script targets are **Phase-B** (depend on ~D's PipelineScript nodes). **No-silent-caps: the 2 non-pipeline EC2 are declared as RUNS-exclusions** so the rollup never false-demands a RUNS edge.

| runner role | inst. | pipeline | tier | expected RUNS |
|---|---|---|---|---|
| inf-bronze-runner | 1 | inf | bronze | yes |
| inf-gold-layer-runner | 1 | inf | gold | yes |
| inf-gold-qa-runner | 1 | inf | gold-QA | yes |
| inf-exporter | 1 | inf | export/platinum | yes |
| bd-gold-layer-runner | 1 | bd | gold | yes |
| bd-gold-qa-runner | 1 | bd | gold-QA | yes |
| bd-gold-detail-generator | 1 | bd | gold (detail) | yes |
| bd-allocations / bd-assets / bd-fees / bd-transactions | 4 | bd | silver/gold (per-domain) | yes |
| bd-49f-auto-login | 1 | bd | ingestion (49F BD session) | yes (feeder) |
| canonical-schwab-runner | 1 | bd/schwab | ingestion (49F canonical converters) | yes |
| cot-exporter | 1 | cot | export | yes |
| mdpf-daily-runner | 1 | mdpf | gold (daily) | yes |
| historical-prices-fetcher | **8** | prices | ingestion (parallel shards) | yes (×8 instances, 1 role) |
| etfs-reports-reporter | 1 | etfs | reporting | yes |
| smartx-exporter | 1 | smartx | export | yes |
| orion-crawl-harness | 1 | orion | ingestion (crawl) | yes |
| seeking-alpha-scraper | **2** | seeking-alpha | ingestion (scrape) | yes (×2 instances, 1 role) |
| astn-wsjft-scraper | 1 | astn/wsjft | ingestion (scrape) | yes |
| **m365-mcp-gateway** | 1 | — | (MS gateway service host) | **NO — RUNS-exclusion** |
| **quartz-si2-spike** | 1 | (spike) | (experimental) | **NO/transient — RUNS-exclusion (confirm w/ ~D)** |

Counts: 31 instances, 23 distinct names; ~21 pipeline-runner roles (29 instances), 2 non-pipeline (m365-mcp-gateway, quartz-si2-spike).

### 2b. The LAMBDA cross-stratum slice (the ~D/~A reattribution — COO~B 214237Z)
Per ruling A (stratum-pair attribution), ~D reclassified its `READS_S3`/`WRITES_S3`: of 903, only 576 are compute-grain (~D); **327 are LAMBDA-ENDPOINT** (resource→object, from `infra/aws/lambda/*` nodes) = **my** slice.
- **327** lambda `READS_S3`/`WRITES_S3` edges (resource→object) — `producer_by_pair {resource→object: ~B}`.
- **87** lambda-ONLY S3Keys + **13** shared (compute+lambda). The S3Key NODE is **~A's** (bucket-qualified `<bucket>/<normalized-key>`, ~C canonical id 02286234a); the **bucket attribution comes from the lambda PATH** (`infra/aws/lambda/{firm}-pipeline`) which **I** own. ~B+~A co-sign the convergence /seams (my edge target id == ~A's S3Key node id, zero dangle/dup). The 87 are the lambda-producer subset of ~D's 142 no-gold-writer keys (firm_qualified.json).

---

## 3. THE N-PARTY /seams SIGN-OFF MATRIX (the denominator's purpose)
Each cross-stratum seam is validated by ALL spanned strata + ~C; a RED from any spanned stratum STOPS (N-sign, not 2-sign). The CHECK is single-sourced (`rollup_defects()` one-head, 28fac26f2); only the SIGN-OFF is N-party.

| seam | spanned strata | sign-off set |
|---|---|---|
| S1 EC2-RUNS->PipelineScript | infra + compute | {~B, ~D, ~C} |
| S2 LAMBDA-CONTAINS->handler | infra + object(compute) | {~B, ~D, ~C} |
| S3 LAMBDA-READS_S3/WRITES_S3->S3Key (87 lambda-only) | infra + storage | {~B, ~A, ~C} |
| S3' the 13 shared (compute+lambda) keys | infra + compute + storage | {~B, ~D, ~A, ~C} |
| R1 rollup EC2/LAMBDA READS S3_BUCKET ⇐ fn READS_S3 S3Key | infra(coarse) + compute(fine) + storage(key) | {~B, ~D, ~A, ~C} |

---

## 4. FINDINGS / SMELL PASS

- **F1 — EC2 name non-uniqueness (RUNS grain decision):** 31 instances, 23 distinct `name`s (`historical-prices-fetcher` ×8, `seeking-alpha-scraper` ×2). The node identity is per-instance (instance-id); `name` is the Name tag, non-unique. **Decision needed (~D populator + ~C governor):** is `EC2 -RUNS-> PipelineScript` keyed on the runner ROLE (one RUNS-set per role, instance multiplicity an attribute) or per-instance (8 identical RUNS-sets for the 8 hist-prices instances)? Recommend role-level with an instance-count attribute (the script binding is per-role).
- **F2 — coarse edge_type overload (rollup binding):** the existing coarse `EC2/LAMBDA READS S3_BUCKET` uses edge_type **`READS`**, which the grain_contract registry attributes to **producer=portal** (`relation=reads, levels=[field,object]`). The fine rollup target is **`READS_S3`** (producer=graphuni-gold). For the existential rollup to bind coarse⇄fine cleanly, **~C must rule** whether the coarse infra S3-read should be `READS_S3[level=bucket]` (same-semantic, grain-stable with the fine per Amendment-2) rather than `READS` (currently overloaded with the portal-field semantic). This is a DECLARATIVE registry-vs-territory item on the rollup keystone.
- **F3 — GRAPH FRESHNESS GAP (the big one; bears on every count):** the estate-topology graph is **~23h stale on the node side** (latest `graph_nodes` commit 06-29 22:11; today's 4 deploys absent; live Lambda 174 vs graph 169). The `opal-globgrph-incremental-updater` fires (~20×/3h) with 0 errors / 0 backlog but `nodes_written=0` every batch — a silent no-op. Data-plane events are correctly excluded by design (management-events only, S3→bucket grain, `lambda_function.py` L105/L256); but today's CONTROL-plane deploys also aren't landing. ROOT not yet grounded (no-delta vs creation-events-not-arriving vs upsert-drop). **Lane = globgrph/comp-tools (0.7.0); flagged to COO~B + 0.7.0.** I grounded this slice's counts on LIVE state to compensate.
- **F4 — non-pipeline EC2 (RUNS exclusions):** `m365-mcp-gateway` (the always-on MS MCP gateway service host) and `quartz-si2-spike` (experimental/spike) are NOT pipeline-script runners — declared `RUNS`-exclusions so the rollup doesn't false-demand a RUNS edge (confirm `quartz-si2-spike` standing with ~D).

---

## 5. ACCEPTANCE-CRITERIA ATTESTATION
- **AC1 — the infra + cross-stratum denominator slice:** §1 (infra stratum nodes + existing coarse edges) + §2 (the 3 net-new stitcher families S1/S2/S3 + the rollup R1) + §3 (spanned strata per stitcher = the N-party /seams sign-off set). Complete + disjoint by stratum-pair (lambda resource→object slice held distinct from ~D's compute→object; the 87+13 keys attributed by ruling A).
- **AC2 — ZERO graph mutation, evidenced:** §0 read-only attestation (all `MATCH … RETURN`; live-AWS reads only).
- **AC3 — the EC2-RUNS keystone mapped:** §2a (23 runner roles / 31 instances → pipeline/tier → expected RUNS; 2 declared exclusions). The cross-stratum seam that fuses infra⇄compute.
- **AC4 — RAVC2 to COO~B (cc CTO + ~C + ~D + ~A):** on commit. Composes into the enumerated denominator COO~B RAVCs to CTO before the /seams run.

## 6. RESIDUAL UNKNOWNS / for ~C + CTO + the fleet
1. **RUNS grain** — role-level vs per-instance (F1). ~C governor + ~D populator.
2. **Coarse-read edge_type reconciliation** — `READS` (current, portal-attributed) vs `READS_S3[level=bucket]` for the rollup coarse target (F2). ~C governor.
3. **The 13 shared compute+lambda S3Keys** — canonical (bucket,key) node ids + four-party sign-off; coordinate with ~A + ~D (in flight).
4. **The graph freshness gap** (F3) — disposition by 0.7.0/globgrph; whether Phase-B population should gate on a fresh derive (so we don't populate onto a 23h-stale node set missing today's resources).
5. **`quartz-si2-spike`** standing — transient vs a real runner (confirm ~D).

---

*Authored 0.8.0_AE_CloudComp~B 2026-06-30 per NFRA_GRAPHUNI.P0-B (COO~B GO 212419Z, GRAPHDEPTH by-stratum fleet, Andrew-direct/CTO-concurred 212036Z). READ-ONLY, zero mutation. The infra + cross-stratum slice of the enumerated denominator; pairs with ~D's compute slice (P0 gap-list) + ~A's storage slice (P0-A). Phase-B population gated on ~D compute + ~A storage existing.*
