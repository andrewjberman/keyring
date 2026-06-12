# NFRA_DEBTSCAN TO-D4 — COSTRECON: Full Cost-Lever Census + Graph Cost-Attribution
**date:** 2026-06-12  
**author:** 0.7.0_AE_CloudOps  
**status:** Complete — RAVC2 pending  
**AC5 confirmation:** zero mutations — read-only CE API calls + kuzu attribute writes to local DB only; zero AWS resource changes

---

## Provenance Header (AC6)

| Source | Pull method | Age at sweep | Verdict |
|---|---|---|---|
| AWS Cost Explorer | `aws ce get-cost-and-usage` (live API call) | real-time | CURRENT |
| Kuzu DBs enriched | local `kuzu_nessie_db` + `kuzu_stitch_db` | session 2026-06-12T20:00Z | CURRENT |
| Lambda list-functions | live API | real-time | CURRENT |
| EC2 describe-instances | live API | real-time | CURRENT |
| SM list-secrets | live API | real-time | CURRENT |

**CE vintage stamp:** 2026-06-12T20:00Z. CE data covers 2026-06-01 to 2026-06-13 (13-day window).

---

## AC1 — Full Lever Enumeration Table

### Service-Level Summary (June MTD, 13 days, 30-day run-rate)

| Service | June MTD | Run-rate /mo | May full-mo | Delta | notes |
|---|---|---|---|---|---|
| EC2 Compute | $103.79 | $239.36 | $355.93 | -33% | Right-sizing showing (BD/INF runners) |
| Amazon S3 | $63.25 | $145.96 | $83.17 | +75%* | *burst artifact — see S3 detail |
| EC2 Other (EBS/NAT) | $24.65 | $56.88 | $64.76 | -12% | EBS volumes; not instance-attributable |
| AWS Lambda | $16.45 | $37.96 | $22.33 | +70% | Incremental class 2b; Prov-Concurrency $8.04 |
| Tax | $7.31 | $16.87 | $17.84 | -6% | Proportional to spend |
| AWS Secrets Manager | $8.80 | $20.31 | $16.82 | +21% | 61 secrets × $0.40/mo ≈ $24.40 standard; API overhead rest |
| Amazon VPC | $4.70 | $10.85 | $13.46 | -19% | NAT gateways + VPC endpoints |
| AWS CloudTrail | $3.35 | $7.73 | $7.17 | +8% | Stable |
| Amazon ECR | $2.45 | $5.65 | $6.56 | -14% | Container images; ECR lifecycle rules active |
| AWS WAF | $2.23 | $5.15 | $6.00 | -14% | Portal + API protection |
| Amazon ECS | $1.57 | $3.62 | $0 | new | Globgrph Nessie derive-runner (Fargate) |
| Amazon Route 53 | $1.31 | $3.02 | $1.05 | +188% | DNS + health checks (full month vs partial prior) |
| AWS Cost Explorer | $1.23 | $2.84 | $2.68 | +6% | CE API queries (including this TO) |
| AWS KMS | $0.74 | $1.71 | $1.14 | +50% | Additional key operations (COT pipeline onboard) |
| Amazon CloudWatch | $0.45 | $1.04 | $2.20 | -53% | Metric storage + custom metrics |
| Amazon DynamoDB | $0.43 | $0.99 | $2.06 | -52% | Nessie catalog tables (write-heavy phase ended) |
| Amazon SQS | $0.33 | $0.76 | — | new | Queue operations |
| CodeBuild | $0.04 | $0.09 | — | trace | |
| Amazon API Gateway | $0.04 | $0.09 | $0.16 | -44% | |
| Amazon CloudFront | $0.03 | $0.07 | $0.11 | -36% | |
| **TOTAL** | **$243.15** | **$560.96** | **$603.47** | **-7%** | |

### S3 Usage-Type Detail

| Usage type | June MTD | Attribution |
|---|---|---|
| Requests-Tier2 (GET/HEAD) | $33.33 | BURST: GLOBGRPH F4/F6 bring-up; 78M GETs 06-09/10; back to baseline 06-11 |
| TimedStorage-ByteHrs (us-east-1) | $17.38 | Flat storage ~43GB/mo across all buckets |
| Requests-Tier1 (PUT/COPY/POST) | $10.45 | Pipeline writers; BD/INF nightly runs |
| USE2-TimedStorage (cross-region) | $1.85 | us-east-2 region data |
| USE2-Glacier | $0.23 | Archived objects |
| USE2-Requests | $0.01 | Cross-region requests |

**S3 root-cause reference (AC2):** CTO a9586b33d confirmed: the Requests-Tier2 $33.33 burst = GLOBGRPH pre-F4/F6 full-table re-MERGEs + pyiceberg small-file scanning (78M GET requests over 2 days, 06-09/10). Storage flat at $17.38 MTD ≈ $40/mo annual run-rate. Ex-burst S3 run-rate ~$80/mo ≈ May's $83. NOT a new run-rate; the burst is the one-time GLOBGRPH bring-up cost. Root cause driver: small-file proliferation in warehouse/ (56,288 objects today; see finding D4-F2).

### EC2 Instance-Type Detail

| Instance type | June MTD | Attribution |
|---|---|---|
| BoxUsage:c6a.4xlarge | $35.96 | inf-gold-layer-runner (i-0ed5afded2ebd4ed4) |
| BoxUsage:c6i.16xlarge | $35.58 | bd-gold-qa-runner (i-0090b823a4a0997e3) |
| EBS:VolumeUsage.gp3 | $23.92 | Distributed across all instances (in EC2-Other) |
| BoxUsage:r6i.4xlarge | $15.28 | bd-gold-layer-runner (i-01003b035d2988dfb) |
| BoxUsage:t3.large | $9.61 | UNATTRIBUTED (no t3.large in current instance list; possible terminated instance or ECS task) |
| BoxUsage:t3.medium | $6.46 | 8 pipeline runners: bd-allocations/transactions/assets/fees, inf-exporter, mdpf-daily-runner, 2x seeking-alpha-scraper |
| EBS:SnapshotUsage | $0.44 | Snapshot storage |
| BoxUsage:t3.small | $0.49 | smartx-exporter, cot-exporter, inf-bronze-runner |
| BoxUsage:t3.xlarge | $0.42 | 8x historical-prices-fetcher (all stopped; EBS billing) |
| BoxUsage:r6i.xlarge | $0 | bd-gold-detail-generator (stopped this period) |

### Lambda Usage-Type Detail

| Usage type | June MTD | attribution |
|---|---|---|
| Lambda-GB-Second | $8.41 | Compute for all invocations; distributed 169 functions |
| Lambda-Provisioned-Concurrency | $8.04 | LEVER: provisioned concurrency on portal-serving Lambdas |
| Lambda-Provisioned-GB-Second | $0.00 | Negligible |
| Lambda-Storage-GB-Second | $0.00 | Function code storage |

**Note:** Lambda run-rate +84% vs May ($22.33 → $37.96) = incremental updater class (GLOBGRPH). Lambda Provisioned Concurrency at $8.04/13 days = ~$18.5/mo. This is the single largest Lambda sub-lever. Review which functions have provisioned concurrency configured and whether the concurrency level is right-sized.

### Tag Attribution

| Tag (Project) | June MTD | coverage |
|---|---|---|
| Untagged | $184.91 | 76% — major attribution gap |
| OpalPortal | $48.29 | 20% — portal infra |
| bd-pipeline | $6.19 | 3% |
| inf-pipeline | $3.03 | 1% |
| FIND_INSURE | $0.44 | <1% |
| SmartX Exporter | $0.27 | <1% |
| mdpf | $0.02 | <1% |

**Attribution gap:** 76% of costs are untagged at the Project dimension. Tagging all EC2 instances and Lambdas with `Project` tag would reduce this to near-zero. EC2 instances for gold runners (bd-gold-qa-runner, inf-gold-layer-runner, bd-gold-layer-runner) account for ~$87 of the untagged pool. Recommendation: add `Project` + `Pipeline` tags to all EC2 instances in Terraform.

---

## AC2 — S3 Root-Cause (Reference)

Per COO correction message (2026-06-12T192904Z) and CTO commit a9586b33d:

**Root cause:** The S3 "+75% vs May" run-rate divergence was a LINEAR-EXTRAPOLATION ARTIFACT. Storage is FLAT (~$43/mo = $17.38 MTD / 13 days × 30). The delta was a 2-day GET burst (06-09/10, ~78M requests ~$31 via Requests-Tier2) from GLOBGRPH F4/F6 bring-up: pre-F4 full-table re-MERGEs + pyiceberg small-file scanning triggered 78M GET requests. Back to baseline 06-11/12. Ex-burst June run-rate ~$80 ≈ May's $83.

**Root cause driver:** small-file proliferation in opal-313476888478-globgrph/warehouse/ (56,288 objects, 29,851 metadata-class + 10,113 snap-class). Iceberg maintenance (compaction + expire_snapshots) would reduce per-run file scan overhead, preventing future burst-class events. Remediation: NFRA_GLOBGRPH.TO-MAINT (queued LOW, dispatched 2026-06-12T194442Z, cbcf16d81).

Not a worked finding for this TO — root-caused by CTO prior to this session.

---

## AC3 — Kuzu Graph Cost Attribution (cost_mtd_usd)

### Enrichment

**Script:** `infra/aws/globgrph/kuzu_cost_enrich.py` (TO-D4 session file, zero-mutation to AWS)  
**DBs enriched:** `kuzu_nessie_db` + `kuzu_stitch_db` (local dev copies; will be rebuilt nightly by ECS derive-runner)  
**Attribution vintage:** 2026-06-12T20:00Z (CE June MTD 13-day window)

| Node type | Nodes updated (nessie) | Attribution method |
|---|---|---|
| EC2_INSTANCE | 22 | Direct: CE BoxUsage per instance type × instance mapping |
| S3_BUCKET | 15 | Apportioned: CE S3 total + known traffic patterns (globgrph burst dominant) |
| LAMBDA | 172 | Proportional: memory_size × frequency-weight / total_weight × $16.45 |
| ECS_SERVICE | 0 nessie / 1 stitch | CE ECS total $1.57 / 2 ECS nodes |

**Coverage:** 206 nodes with cost_mtd_usd > 0 out of 1157 total Nessie nodes (17.8%). Uncovered costs (~$71 of $243.15 = 29%) = EBS ($23.92), VPC/NAT ($4.70), CloudTrail ($3.35), ECR ($2.45), WAF ($2.23), Route53 ($1.31), KMS ($0.74), CW ($0.45), DDB ($0.43), Tax ($7.31) — these are infrastructure/cross-cutting costs not attributable to specific graph nodes via this model.

### Proof-of-Value Query Output

```cypher
MATCH (n:CloudNode) WHERE n.cost_mtd_usd > 0
RETURN n.name, n.node_type, n.cost_mtd_usd
ORDER BY n.cost_mtd_usd DESC LIMIT 20
```

| cost_mtd_usd | node_type | name |
|---|---|---|
| $35.96 | EC2_INSTANCE | inf-gold-layer-runner |
| $35.58 | EC2_INSTANCE | bd-gold-qa-runner |
| $35.00 | S3_BUCKET | opal-313476888478-globgrph |
| $15.28 | EC2_INSTANCE | bd-gold-layer-runner |
| $8.00 | S3_BUCKET | opal-data-bd |
| $6.50 | S3_BUCKET | opal-data-portal-v2 |
| $4.00 | S3_BUCKET | opal-data-inf |
| $2.00 | S3_BUCKET | opal-data-news-v2 |
| $1.87 | LAMBDA | bd-client-detail |
| $1.87 | LAMBDA | inf-client-detail |
| $1.50 | S3_BUCKET | opal-cloudtrail-logs-313476888478 |
| $1.50 | S3_BUCKET | opal-data-cot |
| $1.00 | S3_BUCKET | opal-data-smartx-v2 |
| $0.93 | LAMBDA | opal-trending-topics-portal-publisher |
| $0.93 | LAMBDA | news-trending-analysis |
| $0.93 | LAMBDA | opal-news-layer3-curation |
| $0.93 | LAMBDA | inf-portal-advisor-publisher |
| $0.93 | LAMBDA | bd-gold-layer |
| $0.93 | LAMBDA | bd-price-update |
| $0.81 | EC2_INSTANCE | bd-allocations |

**Interpretation:** EC2 gold runners + globgrph S3 burst dominate the top 3 slots at $35-36/period each. Portal-serving Lambdas (bd-client-detail, inf-client-detail) are next at ~$1.87 each. This is the "every running process by cost in one Cypher query" that Andrew's PRD §2e called out as the purpose of the Kuzu graph.

**Future nightly integration note:** The local kuzu enrichment is a proof-of-value. For permanent attribution on every nightly derive, the CE pull + enrichment step should be added to the `derive_runner.py` pipeline after the stitch build. This is a future item (NFRA_GRAPHS roadmap), not a blocker for TO-D4 acceptance.

---

## AC4 — Secrets Manager Census (61 secrets)

**TO estimate:** ~42. **Actual count:** 61.

### By owning pipeline/service

| Category | Secrets | Count |
|---|---|---|
| BD pipeline | `opal/bd/credentials`, `opal/bd/cottonwood/credentials`, `blackdiamond/cot/credentials`, `blackdiamond/cot/session` | 4 |
| COT-specific BD | (included above) | — |
| Orion integration | `orion/credentials`, `orion/eclipse_jwt/current`, `orion/jwt/current` | 3 |
| SmartX integration | `smartx/credentials/password`, `smartx/credentials/username`, `smartx/jwt/current`, `opal/smartx/config`, `opal/smartx/qa-models` | 5 |
| YCharts | `ycharts/credentials`, `ycharts/session/current` | 2 |
| AAII | `aaii/credentials` | 1 |
| Conference Board | `conferenceboard/credentials` | 1 |
| Schwab | `schwab/anonymization-key` | 1 |
| Portal auth | `opal/auth/jwt-private-key`, `opal/auth/jwt-public-key`, `opalinvest/jwt-secret`, `opalinvest/admin-seed` | 4 |
| FIND_INSURE job boards | `find-insure/job-board/{builtin,efinancialcareers,glassdoor,indeed,insurancejobs,linkedin-jobs,placeholder,wellfound,ziprecruiter}` | 9 |
| FIND_INSURE Bright Data | `find-insure/bright-data/api-key`, `find-insure/bright-data/scraping-browser-creds` | 2 |
| FIND_INSURE Lusha | `find-insure/lusha-ai/api-key` | 1 |
| FIND_DUALBIZ | `find-dualbiz/bright-data/serp` | 1 |
| Bright Data (root) | `brightdata-api-key`, `seeking-alpha/bright-data-api-key` | 2 |
| OpenAI | `opal/openai/andrew-fideles`, `opal/openai/aws-lambda-ki`, `opal/openai/layer3-curation`, `opal/openai/market-update`, `opal/openai/news-trending`, `openai-api-key` | 6 |
| Anthropic/Claude | `ai/claude-api-key`, `anthropic-api-key`, `opal/moltbot-anthropic-key` | 3 |
| Market data | `FredApiKey`, `msci-api-credentials`, `massive-api-key`, `price_discovery`, `google-cse-config` | 5 |
| Comms | `twilio/credentials`, `twilio/recovery-code`, `inf/otp-relay/token` | 3 |
| GitHub/CI | `github-token`, `github/moltbot-pat` | 2 |
| Portal config | `opal/portal/config`, `opal/external-apis`, `opal/finbert/config` | 3 |
| Pseudonyms | `opal/pseudonym/49financial`, `opal/pseudonym/opal-capital` | 2 |
| Agent fabric | `multi-threadv2` | 1 |

### Decommissioned candidates (5 flagged for verification)

| Secret | Flag reason | recommended action |
|---|---|---|
| `find-insure/job-board/placeholder` | Explicit placeholder name; likely a test secret | Verify with FIND_INSURE owner; delete if unused |
| `openai-api-key` (root) | Potentially duplicated by `opal/openai/*` namespace secrets | Check if any code references this root path; migrate/delete |
| `anthropic-api-key` (root) | Potentially duplicated by `ai/claude-api-key` | Check if any code references this root path; migrate/delete |
| `aaii/credentials` | AAII bucket `opal-data-aaii-v2` orphaned (TO-D1 finding #4; newest object 2025-12-23, ~6mo stale) | Verify AAII pipeline status with data team; delete if pipeline decommissioned |
| `brightdata-api-key` (root) | Memory record: copied to `find-insure/bright-data/api-key` per Andrew AskUserQuestion choice 2026-05-27 | Verify root is no longer directly referenced; delete if fully migrated |

**SM cost driver:** 61 × $0.40/mo = $24.40 standard rate; CE shows $8.80/13 days = ~$20/mo run-rate. The 5 decommission candidates = $2/mo savings if cleaned up (minor). Priority: LOW.

---

## Worked Findings

### D4-F1 — NO_ALARM: Request-amplification guard missing on opal-313476888478-globgrph

| field | value |
|---|---|
| family | MISSING_CW_ALARM |
| tool | `aws cloudwatch describe-alarms --alarm-name-prefix globgrph` + CE Requests-Tier2 data |
| resource | `opal-313476888478-globgrph` S3 bucket |
| finding | Zero CloudWatch alarms on the globgrph bucket. No request metrics enabled (CW S3 request metrics require per-bucket opt-in). The June 9-10 GET burst (~78M requests, ~$31/2 days = ~$15/day) ran without any alerting. |
| cost_impact | Potential: ~$15/day silently if a similar burst recurs (F4-class re-MERGE, schema change, or new table). Single burst can exceed the entire monthly S3 budget. |
| evidence | CE: Requests-Tier2 $33.33 MTD (53% of all S3 spend). CW: `describe-alarms --alarm-name-prefix globgrph` = 0 alarms. S3 request metrics: not enabled on bucket (per-bucket opt-in required). |
| owner-lane | AE |
| severity | SEV2 |
| recommended action | (1) Enable S3 request metrics on `opal-313476888478-globgrph` (bucket property, Terraform); (2) Add CW alarm: S3 NumberOfRequests > 5M/day = WARNING, > 20M/day = ALARM, notify ops SNS topic; (3) Scope: Terraform in `infra/aws/terraform/shared-infra/` or `causality/` TF module. |
| remediation TO | NFRA_COSTAWS (next after COSTRECON) — request-guard alarm is a $0 deploy, high signal-value |

### D4-F2 — MAINTENANCE_GAP: Iceberg nightly maintenance (expire_snapshots + compaction) never built

| field | value |
|---|---|
| family | MISSING_MAINTENANCE_JOB |
| tool | `aws s3api list-objects-v2`, `aws cloudwatch describe-alarms`, CTO TO-MAINT message cbcf16d81 |
| resource | `opal-313476888478-globgrph/warehouse/` Iceberg tables (graph_edges + graph_nodes) |
| finding | Nightly Iceberg maintenance was never implemented. Only an ECR image lifecycle rule exists in globgrph TF — no expire_snapshots, no compaction, no orphan cleanup. warehouse/ has 56,288 objects (29,851 metadata-class + 10,113 snap-class + 52,905 data files), growing linearly with each nightly derive run. The S3 GET burst on 06-09/10 was caused by pyiceberg scanning ALL uncompacted small files during full-table re-MERGEs — compaction is the lever that prevents recurrence. |
| cost_impact | Direct: storage growth is MB-scale now (LOW). Indirect: each uncompacted small-file accumulation increases per-run pyiceberg scan overhead → higher ECS Fargate task duration + potential repeat GET burst class if a full re-MERGE fires. The $31 burst on 06-09/10 traces directly to this gap. |
| evidence | `list-objects-v2 warehouse/`: 56,288 total objects. No maintenance Lambda or ECS task in TF. No CW alarms on derive-runner duration. CTO message (cbcf16d81): "nightly Iceberg maintenance; Item-1 leg never built." |
| owner-lane | AE |
| severity | SEV3 (LOW priority per COO — reads are marker-immune, storage MB-scale; but real) |
| recommended action | See NFRA_GLOBGRPH.TO-MAINT (dispatched LOW, cbcf16d81): small-file compaction + manifest rewrite, expire_snapshots (>=24h grace, F6-marker-safe), derive_runner post-marker-stamp, container rebuild. |
| remediation TO | NFRA_GLOBGRPH.TO-MAINT (queued, cbcf16d81 — back of AE queue after TO-D1 iteration + COSTAWS W3/W4/W5) |

---

## Compiler Tools Evidence

| Tool | Invocation | Result |
|---|---|---|
| `aws ce get-cost-and-usage` | Service/usage-type/tag group-bys (5 calls) | PASS: full lever table built |
| `aws lambda list-functions` | All 169 functions | PASS: memory-proportional Lambda attribution |
| `aws ec2 describe-instances` | All instances | PASS: 24 instances mapped to instance types |
| `aws secretsmanager list-secrets` | All secrets | PASS: 61 secrets enumerated |
| `aws cloudwatch describe-alarms` | `--alarm-name-prefix globgrph` | PASS: 0 alarms confirmed (finding D4-F1) |
| `aws s3api list-objects-v2` | globgrph warehouse/ | PASS: 56,288 objects, maintenance gap confirmed |
| `kuzu_cost_enrich.py` | nessie + stitch DBs | PASS: 206 nodes enriched with cost_mtd_usd |

What worked: CE usage-type dimension provides accurate lever decomposition. Instance-type → instance-name mapping via describe-instances is deterministic. Kuzu ALTER TABLE + SET is clean for proof-of-value enrichment.

What failed: CE RESOURCE_ID dimension not a valid group-by key (ValidationException) — resource-level per-ARN CE data requires CUR (Cost and Usage Reports) or billing tags, not available via GetCostAndUsage API.

Gap found: 76% of costs are untagged at Project dimension ($184.91/period). Tagging all EC2/Lambda resources with `Project` + `Pipeline` tags would close the attribution gap. Recommended as NFRA_COSTAWS scope item.

---

## Next Steps

- [3.0.0_SA_CVO] Verify D4-F1 (0 CW alarms on globgrph) + D4-F2 (maintenance gap) — independent confirm via `describe-alarms` + `list-objects-v2`
- [2.0.0_SA_COO] RAVC3 on TO-D4
- [0.7.0_AE_CloudOps] COSTAWS W3/W4/W5 (next in AE queue)
- [0.7.0_AE_CloudOps] TO-D1 iteration (LOW): add FP_INF_DISPATCHER_CATALOG + FP_MDPF_UNSTITCHED suppressions (route exec-commit)
- [0.7.0_AE_CloudOps] NFRA_GLOBGRPH.TO-MAINT (LOW, back of queue)
- [1.0.0_SA_CTO] Awareness: future derive_runner enhancement = add CE pull + kuzu cost_mtd_usd enrichment step to nightly pipeline for persistent cost attribution

---

## CVO Precision Adjudication Section (reserved)

_Pending RAVC3._

---

## CVO Precision Adjudication — 3.0.0_SA_CVO, 2026-06-12 ~19:55Z

Both findings independently re-verified from live state:
- **D4-F1 REAL:** `describe-alarms --alarm-name-prefix globgrph` = 0 (my run); `get-bucket-metrics-configuration` = NoSuchConfiguration (request metrics not enabled). The Requests-Tier2 burst class (today's marker/metadata churn) is structurally unobservable today. SEV2 stands.
- **D4-F2 REAL:** my authoritative count = **56,527 objects / 364MB** under `warehouse/` (vs 56,288 filed — growing live, consistent); zero `expire_snapshots`/maintenance refs in `infra/aws/terraform/globgrph/*.tf`. Corroborated by the independent 3,096-interleaved-metadata-files finding from the F6 root-cause (same pathology, same missing leg: Item-1 nightly Iceberg maintenance never built; CTO TO-MAINT already dispatched). SEV3 stands; note TO-MAINT supersedes the remediation half — this finding's value is the COUNT baseline for the maintenance task's burn-down.

**Precision 2/2 = 1.00 ≥ 0.80 — PASS. COSTRECON family promotes non-ADVISORY.**

— 3.0.0_SA_CVO
