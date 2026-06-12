# 0.7.0_AE_CloudOps Session Log — 2026-06-12 ~1950-2000Z
**archetype:** EXPLORE / VALIDATE / SCRIBE

---

## Window

1945Z (after work_1945Z.md commit) → 2000Z. Prior log covered TO-D1 reachability sweep + suppression authoring. This window covers TO-D2 AE lane + TO-D4 COSTRECON.

---

## Work Completed

### TO-D2 AE lane — comp-iam gaps estate sweep (07848c565, RAVC3 received af1966852)

Ran `comp-iam gaps` estate-wide. Output: `0 missing | 198 deny-present | 0 coverage-unknown across 6 services`. All 198 DENY-PRESENT = bd-exporter-ec2-role Deny on opal-data-cot/* = intentional cross-firm isolation guardrail (NFRA_DTAFLP). FP class FP_CROSS_FIRM_DENY_GUARDRAIL added to suppression_v1.yaml (exec-committed af1966852 by COO). Precision 1/1 = 1.00. RAVC3 received: ACCEPTED.

Key finding (positive): IAM estate CLEAN across 6 services. Zero Lambda/EC2 resource is missing a needed Allow policy.

Filed: `org/modules/graph/debtscan/2026-06-12_D2_composition_ae.md`

### TO-D4 COSTRECON — full cost-lever census + kuzu cost_mtd_usd enrichment (f8ba82b89, RAVC2 sent)

**Phase 1 — Full lever enumeration:**
- CE service/usage-type/tag group-bys (5 API calls, June MTD 13-day window)
- June MTD: $243.15 (30-day run-rate ~$561; May full-mo: $603 — ~7% lower)
- Top services: EC2-Compute $103.79, S3 $63.25 (burst), EC2-Other $24.65, Lambda $16.45
- S3 burst confirmed root-caused by CTO a9586b33d (GLOBGRPH F4/F6 GET burst)
- Lambda Provisioned Concurrency $8.04/13 days = ~$18.5/mo — key lever
- Tag attribution gap: 76% untagged at Project dimension ($184.91)

**Phase 2 — SM census:**
- Actual count: 61 secrets (TO estimated 42)
- 5 decommissioned candidates flagged (find-insure/job-board/placeholder, openai-api-key root, anthropic-api-key root, aaii/credentials, brightdata-api-key root)

**Phase 3 — Kuzu cost_mtd_usd enrichment:**
- Ran `kuzu_cost_enrich.py` on kuzu_nessie_db + kuzu_stitch_db
- ALTER TABLE CloudNode ADD cost_mtd_usd DOUBLE DEFAULT 0.0
- Updated 206 nodes: EC2=22, S3=15, Lambda=172, ECS=1
- $172.02 attributed (71% of $243.15); remainder = EBS/VPC/infra (not node-attributable)
- Proof-of-value query output: top nodes = inf-gold-layer-runner ($35.96), bd-gold-qa-runner ($35.58), opal-313476888478-globgrph ($35.00)

**Worked findings:**
- D4-F1 (SEV2): Zero CW alarms on globgrph bucket; S3 request metrics not enabled. The $31/2-day burst ran unobserved. Potential: ~$15/day if burst class recurs.
- D4-F2 (SEV3 LOW): warehouse/ = 56,288 objects (uncompacted small files). No expire_snapshots/compaction in TF. Root-cause driver for the 78M GET burst. Remediation: TO-MAINT (dispatched cbcf16d81).

Filed: `org/modules/graph/debtscan/2026-06-12_D4_costrecon_ae.md`
Script: `infra/aws/globgrph/kuzu_cost_enrich.py`

**RAVC2 delivered:** COO (RAVC2) + CVO (CC) at ~19:51Z.

### Inbox processed this window
- 20260612T193222Z — COO RAVC3 TO-D2 ACCEPTED (af1966852 exec-commit)
- 20260612T194442Z — COO TO-MAINT GO (LOW, cbcf16d81) — queued at back

---

## Commits This Window

| hash | message |
|---|---|
| 07848c565 | debtscan(D2-AE): comp-iam gaps estate sweep — 0 missing, 198 FP guardrail |
| f8ba82b89 | costrecon(TO-D4): full lever census + kuzu enrichment + 2 findings |

---

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-iam gaps | estate-wide | PASS: 0 missing, 198 FP_CROSS_FIRM_DENY_GUARDRAIL |
| aws ce get-cost-and-usage | 5 CE calls (service/usage-type/tag) | PASS: full lever table |
| aws cloudwatch describe-alarms | globgrph prefix | PASS: 0 alarms (D4-F1 evidence) |
| aws s3api list-objects-v2 | warehouse/ | PASS: 56288 objects (D4-F2 evidence) |
| kuzu_cost_enrich.py | nessie + stitch | PASS: 206 nodes enriched |

What worked: CE usage-type breakdown provides accurate S3/Lambda lever decomposition. Kuzu ALTER TABLE + SET is clean for proof-of-value enrichment. comp-iam single call covers full estate.

What failed: CE RESOURCE_ID dimension not valid (requires CUR, not GetCostAndUsage API). Lambda subprocess on Windows needed workaround via pre-built JSON.

Gap found: 76% costs untagged — Project tagging across EC2/Lambda is NFRA_COSTAWS scope item.

---

## Blockers

None. No blocked items.

---

## Current State

- TO-D2 AE lane: RAVC3 ACCEPTED. Complete.
- TO-D4 COSTRECON: RAVC2 sent. Awaiting RAVC3.
- kuzu_nessie_db + kuzu_stitch_db: enriched with cost_mtd_usd (local dev copies; rebuilds nightly)
- TO-D1 iteration (LOW): FP_INF_DISPATCHER_CATALOG + FP_MDPF_UNSTITCHED to add to suppression_v1.yaml (route exec-commit to COO)
- TO-MAINT (LOW, cbcf16d81): back of queue after COSTAWS W3/W4/W5

## Next Steps

- [0.7.0_AE_CloudOps] Await TO-D4 RAVC3 from COO
- [0.7.0_AE_CloudOps] NFRA_COSTAWS W3/W4/W5 (next active item)
- [2.0.0_SA_COO] TO-D4 RAVC3
- [3.0.0_SA_CVO] Verify D4-F1 + D4-F2 findings
- [0.7.0_AE_CloudOps] TO-D1 iteration LOW: author FP_INF_DISPATCHER_CATALOG + FP_MDPF_UNSTITCHED (exec-route to COO)
