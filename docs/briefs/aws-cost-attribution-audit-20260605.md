# AWS Cost-Attribution Audit — first-pass live map (2026-06-05)

**Author:** 1.0.0_SA_CTO (ws CTO) | **Trigger:** Andrew-direct ("deep audit of all AWS
activity... fan out and look everywhere... ultimately a PRD for formalized cost reduction;
in the meantime just know where everything is"). Priority = **full attribution first**.
**Scope:** account 313476888478, all 17 enabled regions. COO + 0.6.0/0.7.0 AEs fanning out
in parallel — this is the CTO-altitude attribution layer; converge here. Maps to **NFRA W1**.

---

## 0. ROOT FINDING — why nobody can see where the money goes

**Every cost-allocation tag is INACTIVE.** `aws ce list-cost-allocation-tags` returns ~75
keys (Project, Pipeline, Environment, System, Macro, Owner, ...) all `Status=Inactive`.
Consequence: **Cost Explorer cannot group spend by any tag** — a CE group-by `Project`
returns the entire spend under a single blank `Project$` bucket. Resources ARE tagged at
the EC2 level, but those tags are invisible to billing.

Compounding problems:
- **The most expensive resources are UNTAGGED for Project.** bd-gold-layer-runner +
  bd-gold-qa-runner (c6i.16xlarge, ~$232/mo = the single biggest line) have NO `Project` tag.
- **Duplicate keys with different casing** both exist: `Project` vs `project`, `Pipeline`
  vs `pipeline`, `owner` vs `Owner`, `service` vs `Service`. Splits attribution.
- **Inconsistent Environment values:** `production` / `Production` / `qa` / mixed.

**Implication for the PRD:** activating cost-allocation tags is forward-only (no historical
backfill). The sooner Project/Pipeline/Environment/System are activated + a tagging standard
enforced, the sooner per-project attribution exists. This is NFRA W1 critical action #1.
Until then, attribution below is by **instance-name inference**, not billing-grade.

---

## 1. Spend trend — a structural step-up since April (not a runaway spike)

| Month | Spend |
|---|---|
| March | $421.87 |
| April | **$813.71** (spike) |
| May | $603.47 |
| June (5d) | $101.78 -> **~$610/mo run-rate** |

Daily spend is a flat ~$20/day now (range $11-37). The "hemorrhaging" is a **level shift**:
baseline jumped ~$420 -> ~$600-800/mo in April and never came back. Find what onboarded in
April (new pipeline / runner cadence / data growth).

## 2. Cost structure (~$610/mo run-rate)

| Bucket | ~$/mo | % | Attribution |
|---|---|---|---|
| **EC2-Compute** | ~$376 | 62% | 2 nightly gold pipelines dominate (see §3) |
| **S3** | ~$85 | 14% | ~96% is ONE bucket: opal-data-bd 2.4TB (§4) |
| **EBS (EC2-Other)** | ~$63 | 10% | 822GB in-use (mostly stopped-instance vols) + 44GB orphan |
| Lambda | ~$21 | 3% | 50 functions |
| Secrets Manager | ~$17 | 3% | only 10 secrets — high API-call volume; minor |
| VPC | ~$13 | 2% | no NAT gateways; likely endpoints/PrivateLink |
| CloudTrail / ECR / WAF | ~$20 | 3% | routine |
| CW / DynamoDB / KMS / Route53 / Tax | ~$15 | 2% | routine |

## 3. Compute attribution by pipeline (inferred from instance Name)

| Pipeline / system | Instances | ~$/mo | State / note |
|---|---|---|---|
| **bd-gold (49Financial nightly)** | bd-gold-layer-runner + bd-gold-qa-runner (**c6i.16xlarge x2**, ~$232) + bd-gold-detail-generator (r6i.xlarge) + bd-allocations/transactions/assets/fees (t3.medium x4) | **~$250** | ephemeral nightly ~04:00 UTC; STOPPED between runs. **#1 cost. UNTAGGED for Project.** Single biggest right-sizing lever (NFRA W3). |
| **inf-gold (Inflection nightly)** | inf-gold-layer-runner (**c6a.4xlarge**, ~$126) + inf-gold-qa-runner (c6a.2xlarge) + inf-bronze-runner (t3.small) | **~$130** | ephemeral nightly ~13:00 UTC; observed spinning up + self-stopping live during audit = working as designed. #2 cost. |
| **demo-transform (ADVI_DEMOV1/DEMOAUTH)** | demo-transform-runner (t3.large) | ~$60 if left up | **LEAK: running 13d continuous, AutoShutdown=None.** Mid-.002-run today; stop after completion. |
| **inf-exporter** | inf-exporter (t3.medium) | ~$30 | **SUSPECT: running 34d continuous, AutoShutdown=None.** Persistent service or forgotten? Needs owner confirm. |
| **historical-prices** | historical-prices-fetcher (**t3.xlarge x8**) | ~$0 stopped | UNTAGGED (no Project/Env). Why 8 retained? EBS waste; cleanup candidate. |
| **mdpf / smartx / scrapers** | mdpf-daily-runner, smartx-exporter, seeking-alpha-scraper x2, moltbot | small | mostly stopped; scrapers + moltbot UNTAGGED. |

## 4. S3 attribution (~$85/mo)

| Bucket | Size | ~$/mo |
|---|---|---|
| **opal-data-bd** | **2,396 GB** | **~$55** (96% of all S3) |
| opal-data-inf | 88 GB | ~$2 |
| opal-data-demo | 16 GB | small |
| opal-data-portal-v2 | 16 GB | small |
| (27 other buckets) | <5GB each | rounding |

S3 cost is almost entirely **opal-data-bd at 2.4TB**. Investigate retention: old date-
partitions, bronze/silver dupes, versioning bloat, no lifecycle policy. Likely meaningful
savings via a lifecycle/expiry policy (NFRA W4).

## 5. Confirmed waste — do-now, low-risk (separate from the big levers)

1. **demo-transform-runner** up 13d -> stop after .002 finishes (don't kill mid-run).
2. **inf-exporter** up 34d -> confirm owner; stop if not a needed persistent service.
3. **44 GB orphaned EBS** (4 `available` volumes: 8+8+8+20) -> pure waste, delete.
4. **2 Elastic IPs on STOPPED instances** (seeking-alpha-scraper, bd-gold-layer-runner)
   -> idle IPv4 ~$3.6/mo each, release.
5. **22 stopped instances retaining EBS** (incl. two 200GB vols ~$32/mo + 8x t3.xlarge
   historical-prices) -> snapshot-and-delete unneeded volumes / terminate dead instances.

## 6. Ruled out (NOT the leak)

EBS snapshots (only 1, 30GB), self AMIs (only 1), NAT gateways (zero), all 16 non-us-east-1
regions (clean — nothing running anywhere but us-east-1).

## 7. Lever ranking for the cost-reduction PRD

| Lever | ~$/mo at stake | Risk | Owner |
|---|---|---|---|
| Right-size / Spot the **bd-gold c6i.16xlarge** nightly | up to ~$200 | medium (don't break nightly) | NFRA W3 / 0.7.0 AE |
| **opal-data-bd 2.4TB** lifecycle/retention policy | tens of $ | low-med | NFRA W4 / DS+AE |
| Right-size **inf-gold c6a.4xlarge** nightly | up to ~$100 | medium | NFRA W3 |
| **Activate cost-allocation tags + tagging standard** | enables ALL future attribution | none | NFRA W1 (do first) |
| Kill the 2 leaked runners + orphan EBS + idle EIPs | ~$50-100 | low | NFRA W4 hygiene |

**Bottom line:** ~62% of the bill is two nightly gold pipelines (bd >> inf); bd-gold alone
is ~40% of total. The small leaks are real but ~$50-100/mo; the money is in right-sizing the
gold runners + opal-data-bd retention. And none of it is *attributable in billing* until
cost-allocation tags are activated — that's the first PRD action.

---
*First-pass live recon; numbers are CE/CloudWatch-derived (UnblendedCost, 30-35d windows).
Hand off to NFRA for the formalized cost-reduction PRD.*
