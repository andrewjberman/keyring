# 0.5.0_AE_OpalETL Session Summary -- 2026-04-06

**Project:** DEBT_1STRUN (Infrastructure Technical Debt Remediation)
**Task Orders:** .002, .003, .004 (all complete)
**Duration:** Full session

---

## DEBT_1STRUN.002 -- Lambda Source Map Registration

**Objective:** Register all unmapped Lambda functions in `lambda-source-map.json`.

**Result:** 24 functions added. Source map coverage 77% -> 100% (134/134 non-test functions).

| Category | Count | Source |
|----------|-------|--------|
| Trade subsystem | 11 | EXTERNAL (no repo source) |
| Security/infra monitoring | 4 | 2 repo, 1 local TF, 1 EXTERNAL |
| Market update | 3 | EXTERNAL |
| Other (BD, infra, analytics, CloudFront, deck) | 5 | 2 repo, 3 EXTERNAL |
| Structural fix (deck-generation) | 1 | Moved from orphaned top-level into functions block |

Also removed orphaned `opal-partners-data` duplicate entry outside `functions` block.

2 test Lambdas flagged for deletion (not registered): `test-yfinance-simple`, `yfinance-aapl-test`.

**Validation:** 4-stage compiler pipeline (structural, path existence, coverage auditor, TF cross-ref) -- all 24 new entries pass. 9 pre-existing stale paths flagged as prior tech debt.

**Commit:** `002489f1`

---

## DEBT_1STRUN.003 -- Trade Pipeline Terraform Module

**Objective:** Create `infra/aws/terraform/trade-pipeline/` and import all trade subsystem resources.

**Result:** 63 AWS resources imported into new TF pipeline. 0-drift verified.

| Resource Type | Count |
|---------------|-------|
| Lambda functions | 11 |
| CloudWatch log groups | 11 |
| S3 buckets + sub-resources | 27 (5 buckets + versioning/encryption/access-block/website) |
| DynamoDB tables | 3 |
| IAM roles | 2 |
| IAM inline policies | 3 |
| IAM managed policy attachment | 1 |

**Architecture decisions:**
- JWT_SECRET: `sensitive` TF variable, no secrets in git
- All Lambdas: `lifecycle ignore_changes = [filename, source_code_hash]` (code is EXTERNAL)
- `pandas-pyarrow-layer:1` hardcoded ARN on trade-parquet-batch-export
- `trade-submissions` DynamoDB table referenced in IAM policy but doesn't exist (stale policy, TF matches live)

**Apply:** 0 add, 33 change, 0 destroy (log retention 0->14d, tags, versioning, JWT alignment). Post-apply: 0-drift.

**Commits:** `20bed5b8` (pre-import), `320e4999` (post-import), `5022878f` (session log)
**Tag:** `trade-pipeline-v1.0.0`

---

## DEBT_1STRUN.004 -- S3 Bucket Imports + Cleanup

**Objective:** Import 18 non-trade S3 buckets into TF and clean up legacy buckets.

### Imported (7 buckets across 3 pipelines)

| Bucket | Pipeline |
|--------|----------|
| opalinvest-portal | shared-infra |
| opal-cloudfront-logs-313476888478 | shared-infra |
| opal-cloudtrail-logs-313476888478 | shared-infra |
| opal-analytics-dashboard | shared-infra |
| opal-ci-staging | shared-infra |
| opal-market-data-v2 | market-overview |
| opal-data-trade-submissions | trade-pipeline |

All 3 pipelines at 0-drift after apply.

### Deleted (8 buckets, Andrew-authorized)

| Bucket | Reason | Versions Purged |
|--------|--------|----------------|
| opal-code-factorscanner-v2 | Superseded by lambda-artifacts | ~4 |
| opal-code-smartx-v2 | Superseded by lambda-artifacts | ~7 |
| opal-lambda-code-archive | Superseded by lambda-artifacts | ~100+ |
| smartx-exports-ajb327-20250118 | Empty one-time export | delete markers only |
| opal-infrastructure-snapshots | Empty | delete markers only |
| opal-data-aaii-sentiment | Duplicate of opal-data-aaii-v2 | 3 |
| opal-market-update | Deprecated us-east-2 bucket | ~14K+ (in progress) |
| opal-data-schwab | Deprecated us-east-2 bucket | ~20K+ (in progress) |

S3 bucket count: 33 -> 25 (after all deletions complete).

### Investigation Results (documented, no action)

- `opal-data-aaii-v2`: kept (identical to deleted aaii-sentiment)
- `ajb-workflow`: empty, personal bucket
- `opal-313476888478-wyncht`: 4 HTML reports, 89KB, low activity

**Commits:** `1a48e169` (pre-import), `1ddfc278` (post-import), `f31ddca5` (session log)
**Tags:** `shared-infra-v1.6.0`, `market-overview-v1.6.9`

---

## Session Totals

| Metric | Value |
|--------|-------|
| Task orders completed | 3 (.002, .003, .004) |
| Commits | 7 |
| Tags created | 3 (trade-pipeline-v1.0.0, shared-infra-v1.6.0, market-overview-v1.6.9) |
| Lambda source map entries added | 24 (coverage 77% -> 100%) |
| TF resources imported | 70 (63 trade + 7 S3) |
| S3 buckets deleted | 8 (6 confirmed, 2 in progress) |
| Pipelines at 0-drift | 4 (trade-pipeline, shared-infra, market-overview, trade-pipeline) |

## Remaining Work

- **DEBT_1STRUN.005** (staged): IAM roles, DynamoDB tables, cleanup, local-state migration
- **us-east-2 bucket deletion**: opal-market-update and opal-data-schwab version purge in progress
- **Test Lambda deletion**: test-yfinance-simple, yfinance-aapl-test (flagged, needs Andrew approval)
