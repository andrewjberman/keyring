# DEBT_1STRUN.002 -- Lambda Source Map Registration

**Date:** 2026-04-06
**Agent:** 0.5.0_AE_OpalETL
**Task Order:** DEBT_1STRUN.002.ae-lambda-source-map-registration.md
**Project:** DEBT_1STRUN
**Status:** COMPLETE

---

## Summary

Registered 24 previously unmapped Lambda functions in `infra/aws/lambda/ci/lambda-source-map.json`. Source map now covers 134/134 non-test Lambda functions (100% coverage, up from 77%).

Also fixed 2 structural issues: moved `deck-generation` from orphaned top-level entry into `functions` block, and removed orphaned `opal-partners-data` duplicate.

---

## Entries Added (24)

### Trade Subsystem (11) -- all EXTERNAL, no repo source
- trade-auth-handler (python3.11)
- trade-authorizer (python3.11)
- trade-dashboard-api (python3.11)
- trade-identifier-cache (python3.11)
- trade-parquet-batch-export (python3.11)
- trade-recon-api (python3.11)
- trade-recon-auth (python3.11)
- trade-recon-authorizer (python3.11)
- trade-recon-processor (python3.11)
- trade-submission-handler (python3.11)
- trade-workflow-handler (python3.11)

### Security/Infrastructure Monitoring (4)
- access-anomaly-scanner -- source: infra/aws/lambda/access-anomaly-scanner
- cost-anomaly-scanner -- source: infra/aws/lambda/cost-anomaly-scanner
- ec2-auto-shutdown-enforcer -- source: infra/aws/lambda/ec2-auto-shutdown-enforcer (has local TF, needs S3 migration)
- ec2-runtime-monitor -- EXTERNAL

### Market Update (3) -- all EXTERNAL
- market-update-data-aggregator (python3.12)
- market-update-exporter (python3.12)
- market-update-generator (python3.12)

### Other (5)
- bd-allocation-file-checker -- EXTERNAL, TF in bd-pipeline with lifecycle ignore_changes
- opal-bd-transaction-consolidator -- source: infra/aws/lambda/bd_transaction_consolidator
- infrastructure-daily-snapshot -- source: infra/aws/lambda/infrastructure-daily-snapshot
- opal-session-analytics -- EXTERNAL
- opal-cloudfront-market-generator -- EXTERNAL, Node.js, TF in market-overview with lifecycle ignore_changes

### Structural Fix (1)
- deck-generation -- moved from orphaned top-level to inside functions block

---

## Structural Cleanup

- Removed orphaned `opal-partners-data` top-level entry (duplicate of entry inside `functions`)
- Moved `deck-generation` from top-level into `functions` block
- Replaced Unicode em dash in deck-generation `_note` with ASCII `--`

---

## Test Lambda Candidates (NOT registered -- flagged for deletion)

- test-yfinance-simple
- yfinance-aapl-test (runtime=None, broken)

---

## Coverage

| Metric | Before | After |
|--------|--------|-------|
| Functions in source map | ~110 | 134 |
| AWS Lambda total (audit) | 136 | 136 |
| Test candidates (skip) | 2 | 2 |
| Coverage | ~77% | 100% |
| EXTERNAL (no repo source) | 0 | 18 |

---

## Files Changed

| File | Action |
|------|--------|
| `infra/aws/lambda/ci/lambda-source-map.json` | +24 entries, structural fix |
| `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-04-06/debt_1strun_002_source_map_registration.md` | This log |
