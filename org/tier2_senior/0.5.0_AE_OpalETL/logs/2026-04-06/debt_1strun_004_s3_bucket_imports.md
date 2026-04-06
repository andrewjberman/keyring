# DEBT_1STRUN.004 -- S3 Bucket Imports

**Date:** 2026-04-06
**Agent:** 0.5.0_AE_OpalETL
**Task Order:** DEBT_1STRUN.004.ae-s3-bucket-tf-imports.md
**Project:** DEBT_1STRUN
**Status:** COMPLETE (7/9 imported, 2 deferred)

---

## Summary

Imported 7 non-trade S3 buckets into their appropriate TF pipelines. 2 buckets deferred (us-east-2 region mismatch). All 3 affected pipelines at 0-drift.

---

## Imported Buckets (7)

| Bucket | Pipeline | Versioning | Website |
|--------|----------|------------|---------|
| opalinvest-portal | shared-infra | No | No |
| opal-cloudfront-logs-313476888478 | shared-infra | No | No |
| opal-cloudtrail-logs-313476888478 | shared-infra | No | No |
| opal-analytics-dashboard | shared-infra | Enabled | Yes (index.html + error) |
| opal-ci-staging | shared-infra | No | No |
| opal-market-data-v2 | market-overview | Enabled | No |
| opal-data-trade-submissions | trade-pipeline | Enabled | No |

All have AES256 encryption and public access blocked.

## Deferred Buckets (2) -- us-east-2

| Bucket | Pipeline | Issue |
|--------|----------|-------|
| opal-market-update | market-overview | In us-east-2, requires aliased provider |
| opal-data-schwab | bd-pipeline | In us-east-2, requires aliased provider |

Both need `provider "aws" { alias = "us_east_2"; region = "us-east-2" }` and `provider = aws.us_east_2` on the resource. Documented in TF comments. Escalate to CTO for cross-region provider pattern decision.

## Deletion Candidates (5) -- NOT deleted, documented only

| Bucket | Objects | Size | Assessment |
|--------|---------|------|-----------|
| opal-code-factorscanner-v2 | 2 | 58MB | Superseded by lambda-artifacts |
| opal-code-smartx-v2 | 2 | 48MB | Superseded by lambda-artifacts |
| opal-lambda-code-archive | 2 | 108MB | Superseded by lambda-artifacts |
| smartx-exports-ajb327-20250118 | 0 | 0B | Empty, one-time export |
| opal-infrastructure-snapshots | 0 | 0B | Empty |

## Investigation Results (4)

| Bucket | Objects | Size | Assessment |
|--------|---------|------|-----------|
| opal-data-aaii-sentiment | 3 | 91KB | Identical to opal-data-aaii-v2 (duplicate) |
| opal-data-aaii-v2 | 3 | 91KB | Identical to opal-data-aaii-sentiment (duplicate) |
| ajb-workflow | 0 | 0B | Empty, personal bucket |
| opal-313476888478-wyncht | 4 | 89KB | HTML reports, low activity |

## Pipeline Status After Apply

| Pipeline | Changes | Post-Apply Drift |
|----------|---------|-----------------|
| shared-infra | 0 add, 5 change, 0 destroy | None (0-drift) |
| market-overview | 0 add, 1 change, 0 destroy | None (0-drift) |
| trade-pipeline | 0 add, 1 change, 0 destroy | None (0-drift) |

## Tags

| Pipeline | Tag |
|----------|-----|
| shared-infra | shared-infra-v1.6.0 |
| market-overview | market-overview-v1.6.9 |
| trade-pipeline | (already at trade-pipeline-v1.0.0 from .003) |

## Commits

| Commit | Message |
|--------|---------|
| 1a48e169 | feat(s3): add 9 bucket resources across 4 TF pipelines (pre-import) |
| 1ddfc278 | infra(s3): import 7 buckets, deferred 2 us-east-2 |
