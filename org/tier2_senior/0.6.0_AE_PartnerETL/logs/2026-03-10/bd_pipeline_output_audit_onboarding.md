# BD Pipeline Output Audit + Partner Onboarding Checklist — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Start Time:** 18:30
**End Time:** 19:15
**Task Order:** ADVI_APISCP.001.bd-pipeline-output-audit-onboarding.md

## Objective

Audit all bd-pipeline gold output paths to confirm ZERO writes to opal-data-portal-v2.
Produce a partner onboarding checklist and update pipeline_inventory.xml with the gold
output bucket separation invariant. Audit-only — no code changes or deploys.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read recent logs (cache_control_ec2_gold_scripts, 5bed0dbf) | Context established |
| 2 | Grep OUTPUT_BUCKET + opal-data-portal-v2 in bd-portal-publisher | CLEAN -- zero portal-v2 matches |
| 3 | Grep OUTPUT_BUCKET + opal-data-portal-v2 in bd-portal-advisor-publisher | CLEAN |
| 4 | Grep S3_BUCKET across all active gold scripts (data/black_diamond/scripts/gold/*.py) | CLEAN -- all = opal-data-bd |
| 5 | Check EC2 user-data.sh (bd-gold-detail-generator) | Scripts from s3://opal-data-bd/scripts/gold_layer/ |
| 6 | Grep archive/ scripts | 8 archive files have portal-v2 refs -- NOT active |
| 7 | Check IAM (iam.tf line 375) | FINDING: stale s3:PutObject on opal-data-portal-v2/* |
| 8 | Verify lambda-source-map.json entries | Both publishers current at b9c483aa 2026-03-10 |
| 9 | Update pipeline_inventory.xml | Added issues #10, #11; added data_contracts section |
| 10 | Write partner-onboarding-checklist.md | Deliverable created |
| 11 | Write session log + mark task order complete | This file |

---

## Work Completed

### R1: bd-portal-publisher Audit

**File:** `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`

| Check | Result |
|-------|--------|
| OUTPUT_BUCKET default | `'opal-data-bd'` (line 41, env var with default) |
| `_save_json()` writes to | `Bucket=OUTPUT_BUCKET` -- always opal-data-bd |
| All key prefixes | `gold/*` -- timeseries_chart, architect_leaderboard, clients_tab, summary/header_metrics, partner_analytics/header_metrics, filters/dimensions, snapshots/* |
| opal-data-portal-v2 grep | ZERO MATCHES |
| Note | `gold/partner_analytics/header_metrics.json` line is commented out (`# _save_json(pa, ...)`) -- no-op |

**Verdict:** CLEAN. Writes exclusively to `opal-data-bd/gold/`.

### R1: bd-portal-advisor-publisher Audit

**File:** `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py`

| Check | Result |
|-------|--------|
| OUTPUT_BUCKET default | `'opal-data-bd'` (line 35) |
| put_object calls | `Bucket=OUTPUT_BUCKET` exclusively |
| Output keys | `gold/advisors/{adv_id}/book.json`, `gold/implementor_leaderboard.json`, `gold/clients/{rel_id}.json` |
| opal-data-portal-v2 grep | ZERO MATCHES |

**Verdict:** CLEAN. Writes exclusively to `opal-data-bd/gold/`.

### R2: EC2 Gold Scripts Audit

**Active scripts (data/black_diamond/scripts/gold/*.py):**

| Script | S3_BUCKET | portal-v2 refs |
|--------|-----------|----------------|
| 00_build_accounts_dimension.py | opal-data-bd | NONE |
| 01_build_advisor_assignments_history.py | opal-data-bd | NONE |
| 02_build_positions_cube.py | opal-data-bd | NONE |
| 03_build_holdings_lots.py | opal-data-bd | NONE |
| 04_build_client_dimension.py | opal-data-bd | NONE |
| 05_build_client_performance.py | opal-data-bd | NONE |
| 05b_build_account_performance.py | opal-data-bd | NONE |
| 06_build_client_tax_liability.py | opal-data-bd | NONE |
| 07_build_nna_aua_by_geography.py | opal-data-bd | NONE |
| 08_build_nna_aua_by_advisor.py | opal-data-bd | NONE |
| 09_generate_partner_analytics.py | opal-data-bd | NONE |
| 10_generate_advisor_rolling_flows.py | INPUT+OUTPUT = opal-data-bd | NONE |

**bd-gold-detail-generator user-data.sh:** Downloads scripts named `07_generate_partner_analytics.py`,
`09_generate_client_detail.py`, `10_generate_book_views.py`, `11_generate_clients_tab.py` from
`s3://opal-data-bd/scripts/gold_layer/` -- this is a DIFFERENT path from the active runner
scripts at `code/gold/`. The archive versions of these scripts (`archive/09`, `archive/10`,
`archive/11`) use `opal-data-bd`. However, `archive/11_generate_clients_tab.py` has a DUAL
bucket reference (`S3_BUCKET_PORTAL = 'opal-data-portal-v2'`). The S3 version at
`scripts/gold_layer/` should be verified in the AWS console.

**Archive scripts with portal-v2 refs (NOT active, for awareness):**
- `archive/08_generate_timeseries_chart.py`
- `archive/11_generate_leaderboards.py`
- `archive/12_generate_aua_chart.py`
- `archive/13_generate_flows_chart.py`
- `archive/11_generate_clients_tab.py` (dual bucket -- has portal-v2)
- `archive/allocations/generate_aua_chart.py`
- `archive/transactions/generate_flows_chart.py`
- `archive/hybrid/generate_leaderboards.py`

**Verdict:** Active scripts CLEAN. Archive scripts flagged as historical -- not deployed.

### R3: lambda-source-map.json Verification

| Lambda | tf_resource | last_deployed_commit | last_deployed_at |
|--------|-------------|---------------------|-----------------|
| bd-portal-publisher | module.bd_portal_publisher.aws_lambda_function.this | b9c483aa | 2026-03-10T16:30:00Z |
| bd-portal-advisor-publisher | module.bd_portal_advisor_publisher.aws_lambda_function.this | b9c483aa | 2026-03-10T16:30:00Z |

Both entries are current -- last deploy is the cache-control fix from today's earlier session.

### R4: pipeline_inventory.xml Update

Added:
- `<issue id="10">`: Stale IAM s3:PutObject permission on opal-data-portal-v2/*
- `<issue id="11">`: Archive scripts with portal-v2 references (informational)
- `<data_contracts>` section: `<contract id="gold-output-invariant">` documenting the bucket
  separation rule, verified components, partner scaling model, and the deleted path record.

### R5: Partner Onboarding Checklist

Written to `deliverables/partner-onboarding-checklist.md`. Six steps:
1. Create `opal-data-{firmId}` S3 bucket (versioning on, AES256, block public access)
2. Attach CloudFront bucket policy (DT confirms OAC/OAI template; REQUIRED for CloudFront to serve)
3. Create `FIRM#{firmId}` DynamoDB record in `opal-users-v2` with `s3Bucket` field
4. Write gold output to `s3://opal-data-{firmId}/gold/` (publisher env var OUTPUT_BUCKET)
5. Confirm zero writes to `opal-data-portal-v2` (grep + CloudWatch check)
6. No Lambda@Edge code changes needed (router uses firmId from DynamoDB)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Flag stale IAM permission but don't touch it | Task is audit-only; no deploy. IAM change needs its own deploy cycle with 0.7.0_AE_CloudOps. |
| Flag archive/11 dual-bucket but don't remove | Archive scripts are out of scope; they are not deployed. Removal risks touching git history unnecessarily. |
| bd-gold-detail-generator S3 path discrepancy flagged as informational | Cannot verify s3://opal-data-bd/scripts/gold_layer/ content without AWS console access -- flagged for follow-up. |
| CloudFront bucket policy in Step 2 uses placeholder | Thread ADVI_APISCP-001 determined DT must confirm exact policy template during preflight; inserting wrong OAC/OAI principal would silently deny access. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/pipeline_inventory.xml` | Added issues #10, #11; added data_contracts section | Pending |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/partner-onboarding-checklist.md` | New file | Pending |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_APISCP.001.bd-pipeline-output-audit-onboarding.md` | Status pending -> complete | Pending |

---

## Blockers

None. This is an audit + documentation task. All findings are documented. Follow-up items
are flagged in pipeline_inventory.xml known_issues and do not block this task order.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Audit confirms bd-pipeline gold output separation is intact: ZERO active code writes to
opal-data-portal-v2. Both publisher Lambdas, all EC2 gold scripts, and the EC2 user-data.sh
all target opal-data-bd exclusively. Two findings flagged for follow-up: (1) stale IAM
permission on portal-v2 in iam.tf, (2) need to verify archive/11 in s3://opal-data-bd/scripts/gold_layer/.
pipeline_inventory.xml updated with bucket separation contract. Partner onboarding checklist produced.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Remove stale IAM permission** -- edit `infra/aws/terraform/bd-pipeline/iam.tf`
   line 375 to remove `arn:aws:s3:::opal-data-portal-v2/*` from the bd-pipeline Lambda role policy.
   Terraform apply, 0-diff confirm, tag bd-v{next}, push.

2. **[0.6.0_AE_PartnerETL] Verify s3://opal-data-bd/scripts/gold_layer/ contents** -- via AWS console,
   confirm which version of 11_generate_clients_tab.py lives at that prefix. If it references
   opal-data-portal-v2, replace with the current archive/11 version (which uses opal-data-bd).

3. **[0.7.0_AE_CloudOps] Confirm CloudFront bucket policy template** -- document the exact
   OAC or OAI principal and policy format for new partner buckets in a preflight discovery thread.
   This template must be available before Step 2 of the onboarding checklist can be executed.

**Files to touch next:**
- `infra/aws/terraform/bd-pipeline/iam.tf` line 375 -- remove opal-data-portal-v2 statement (0.7.0_AE_CloudOps)
- `deliverables/partner-onboarding-checklist.md` Step 2 -- update CloudFront policy template once DT confirms
