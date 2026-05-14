# AE 0.7.0 Session Log — YANG_ALLOC_CLEANUP 2026-05-14
**Date:** 2026-05-14
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Boot ~13:15Z; COO suggested yang-generate-allocation-summary investigation (DRIFTD.002 parity-gap cleanup #4 of 4); my discretion pickup; COO GO at 13:21Z
**Status:** COMPLETE — branch (c) dead-code cleanup shipped in one commit; no functional change to deployed Lambda

---

## TL;DR

DRIFTD.002 surfaced yesterday that `yang-generate-allocation-summary` source_dir contained two `.py` files not registered in `lambda-source-map.json` `files[]`. Investigation showed dead code: `lambda_function.py` never imports either module, `comp-iam` confirms zero DynamoDB ops, the deployed S3 zip contains only `lambda_function.py`. The orphans plus a stale `deploy.sh` were pre-CLAUDE.md-Rule-1-era leftovers. Shipped a single-commit delete of 3 files; no Terraform change, no zip rebuild, no apply, no tag bump.

---

## Investigation Evidence

### lambda_function.py import scan
```
$ grep -nE '^(import|from)\s+(etf_classification|etf_classifications_dynamodb)' lambda_function.py
(no matches)
$ grep -n 'etf_class|importlib|__import__|exec|eval' lambda_function.py
(no matches)
```
Full read of 375 lines: imports json, gzip, boto3, pickle, logging, datetime, typing. Logic = hardcoded asset-class reclassification (Cash→Fixed Income, Hedge→Equity) + hardcoded `BENCHMARK_ALLOCATIONS` dict. Zero ETF classification path.

### comp-iam service (pre-delete baseline)
```
SERVICE: yang-generate-allocation-summary  [lambda]
  IAM role: yang-pipeline-lambda-role
  OPERATIONS (4):
    s3:GetObject  [GRANTED]  via lambda_function.py:79  (LATEST.json read)
    s3:GetObject  [GRANTED]  via lambda_function.py:132 (model PKL load)
    s3:GetObject  [GRANTED]  via lambda_function.py:148 (holdings_attribution_data.json)
    s3:PutObject  [GRANTED]  via lambda_function.py:364 (allocation_summary.json upload)
```
Zero DynamoDB ops → `etf_classifications_dynamodb.py` not invoked.

### Deployed zip on S3
```
$ aws s3api head-object --bucket opal-313476888478-lambda-artifacts \
    --key yang-pipeline/yang-generate-allocation-summary.zip
{
  "ContentLength": 4155,
  "ETag": "91442526302c8e1ec6b17dbaf15290bc",
  "Metadata": {"content-sha256": "q9udBA2L2Wn3lZgfxKUEwX17RTNvIZx5N2uziS/o0Hg="}
}

$ unzip -l /tmp/yga.zip
  Length      Date    Time    Name
   15404  2020-01-01 00:00   lambda_function.py
```
Deployed zip contains ONLY `lambda_function.py`. Last modified 2026-05-04, matches source-map `last_deployed_commit cdc2271c4` + `last_deployed_at 2026-05-04T18:55:40Z`. Terraform-managed path is correct.

### Cross-reference scan
```
$ grep "yang-generate-allocation-summary/(etf_classification|deploy\.sh)"
(5 matches — all in old session logs Jan-Mar 2026)
```
No active Lambda/script references these files from this source_dir.

### Root cause: stale `deploy.sh`
```bash
#!/bin/bash
# infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/deploy.sh
zip -j function.zip lambda_function.py etf_classification.py etf_classifications_dynamodb.py
aws lambda update-function-code --function-name yang-generate-allocation-summary ...
```
Pre-CLAUDE.md-Rule-1 deploy script. Violates Rule 1 (Terraform-only), Rule 3 (deps→Layer), Rule 4 (source-map). When Terraform deploys took over, `files: ["lambda_function.py"]` was correctly written but orphan `.py` + `deploy.sh` files were never swept.

---

## Decision Tree Result

**Branch (c) dead-code cleanup.** Single-commit delete of:
- `etf_classification.py` (26406 bytes) — never imported
- `etf_classifications_dynamodb.py` (6609 bytes) — never imported; zero DDB
- `deploy.sh` (519 bytes) — stale, violates Rule 1

No source-map change. No Terraform change. No zip rebuild. No apply. No tag bump.

---

## Ship

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-delete `comp-iam service` baseline | 4 ops; s3:GetObject×3 + s3:PutObject; zero DDB |
| 2 | Pre-delete deployed-zip `unzip -l` | Only `lambda_function.py` (15404 bytes) |
| 3 | Pause + RAVC2 to COO with evidence + auth request | GO granted at 13:24Z |
| 4 | `rm` 3 files from source_dir | 3 files deleted |
| 5 | Post-delete `ls` source_dir | Only `lambda_function.py` remains |
| 6 | Post-delete `comp-iam service` | IDENTICAL to pre-delete (4 ops; zero DDB) |
| 7 | safe-commit.sh single commit | `75f2cd94e` — 3 files changed, 820 deletions |
| 8 | git push origin CLOUD | fd11a33c2..75f2cd94e CLOUD -> CLOUD |
| 9 | safe-deploy pre-push hook | OK: no deploy-scope script files, nothing to do |

**Commit:** `75f2cd94e cleanup(yang-generate-allocation-summary): remove dead pre-Rule-1 source-dir files`

**No tags pushed** — no functional change in deployed code.

---

## Acceptance Gate Evidence

| Gate (per COO 13:24Z) | Result |
|------|--------|
| 1. DRIFTD.002 parity-check on yang-generate-allocation-summary → PASS | PASS by construction — source_dir now contains only `lambda_function.py` which IS in `files: ["lambda_function.py"]`. No need to invoke build-and-upload.sh (would also re-upload identical S3 zip). |
| 2. `comp-iam service yang-generate-allocation-summary` post-delete identical to pre-delete (4 ops; zero DDB) | PASS — both runs printed identical 4-operation output. |
| 3. Next nightly EventBridge invocation identical to today | PENDING — verify tomorrow AM ET; deployed zip contents unchanged → no behavioral delta expected |

---

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-pipescript io yang-generate-allocation-summary` | Pre-write (AE mandate) | "Unknown script" — tool scope is BD-gold scripts, not Lambdas; logged for compliance |
| `comp-iam service yang-generate-allocation-summary` (pre + post) | Pre-write baseline + post-delete acceptance gate | Pre: 4 ops; Post: 4 ops (IDENTICAL); zero DDB confirms etf_classifications_dynamodb.py unused |
| Manual grep `^(import|from)\s+(etf_classification|etf_classifications_dynamodb)` on lambda_function.py | Confirm dead-code branch | Zero matches |
| `aws s3 cp` + `unzip -l` of deployed artifact | Empirical proof of deployed state | Only lambda_function.py (15404 bytes raw, 4155 zipped) |

---

## Broader Observation Surfaced to COO

4 sibling Lambdas have similar duplicated `etf_classification.py` + `deploy.sh` patterns:
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/`
- `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/`
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/`
- `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/`

These siblings DO import `etf_classification` (per grep), so cleanup is NOT trivial deletion. Right structural fix is Layer migration: centralize to `infra/aws/lambda/layers/yang-classification-deps/` + source-map points 4 consumers at layer ARN.

**COO routing:** deferred to ADHC_DRIFTD v0.2 scope candidate when project reactivates (currently `status: monitoring`). Same root-cause class (pre-Rule-1 era source-dir bundling) so v0.2 PRD frames both classes together. COO will note in `ADHC_DRIFTD.json` next housekeeping wave.

---

## RAVC Trail

| Step | Direction | Time | Content |
|------|-----------|------|---------|
| 1 (Boot inbox) | AE 0.6.1 → me 13:10Z | Ack at 13:11Z | Phantom 13:02Z chain attribution check — NOT MINE; clean loop close |
| 2 (Boot inbox) | COO → me 13:18Z | Ack at 13:18Z | Sanity check on phantom — NOT MINE; offered comp-iam/comp-routes assist if Lambda principal surfaces |
| 3 (Discretion pickup) | me → COO 13:20Z | GO 13:21Z | yang-generate-allocation-summary investigation pickup |
| 4 (Pre-destructive pause) | me → COO 13:23Z | GO 13:24Z | Branch (c) dead-code; auth request to delete 3 files |
| 5 (Closure) | me → COO this commit | Pending | RAVC5 with acceptance evidence + commit hash |

---

## Current State

| Project / TO | Status |
|--------------|--------|
| YANG_ALLOC_CLEANUP | SHIPPED — `75f2cd94e` on CLOUD; deployed Lambda unchanged |
| DRIFTD.002 parity-gap cleanup #4 of 4 | CLOSED |
| Sibling Lambdas (yang-positioning, etf-returns, holdings-attribution, opal-partners-data) Layer migration | DEFERRED to ADHC_DRIFTD v0.2 |
| Phantom 13:02Z chain attribution | PENDING — AE 0.6.1 CloudTrail trace; not blocking |

---

## Next Steps (handoff for next session)

1. **Tomorrow AM ET (2026-05-15):** verify yang-generate-allocation-summary nightly EventBridge fire ran clean. CloudWatch log group `/aws/lambda/yang-generate-allocation-summary`. Acceptance gate #3.
2. **Phantom 13:02Z chain:** standing offer to COO for comp-iam/comp-routes narrowing if AE 0.6.1 surfaces a Lambda principal or SSM operator from CloudTrail.
3. **Layer migration (ADHC_DRIFTD v0.2):** when project reactivates, prepare TO to centralize `etf_classification.py` to `infra/aws/lambda/layers/yang-classification-deps/` + retrofit 4 consumer Lambdas via layer ARN reference.
4. **DRIFTD.002 cleanup count:** 4 of 4 surfaced gaps now resolved (`bd-price-update` fork-merge backups, `opal-infrastructure-monitor` typing_extensions vendor, `seeking-alpha-news-scraper` backfill script, `yang-generate-allocation-summary` THIS commit). Project-level DRIFTD.002 surface is fully drained.

---

## Session Status: COMPLETE — single-commit dead-code cleanup; deployed Lambda unchanged; all acceptance gates PASS except gate-3 (deferred to tomorrow AM observation)
