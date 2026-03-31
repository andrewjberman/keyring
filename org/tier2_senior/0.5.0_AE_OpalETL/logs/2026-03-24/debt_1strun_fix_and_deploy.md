# DEBT_1STRUN Fix and Deploy Session -- 0.5.0_AE_OpalETL

**Date:** 2026-03-24
**Task Order:** DEBT_1STRUN.001.scan.md (scan) + ad-hoc fix authorization from Andrew
**Project:** DEBT_1STRUN
**Scope:** Yang pipeline, news pipeline, market-overview Lambda code + Terraform review + deploy

---

## Session Summary

Completed the full DEBT_1STRUN cycle for 3 Lambda pipelines: scan, plan, fix, review, deploy, tag, push. Also fixed a long-standing Windows build tooling issue in `build-and-upload.sh`.

---

## Phase 1: Scan (delivered as separate log)

Produced `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-03-24/debt_1strun_scan.md` with 102 findings across yang Lambda (35), news Lambda (25), market-overview Lambda (13), Terraform modules (13), and EC2 services (16).

---

## Phase 2: Yang Pipeline Fixes

### Plan
- Reviewed all 35 findings, verified each against actual code
- Confirmed dead imports (pickle in trigger, timedelta in etf-returns, argparse in positioning) were actually USED -- scan was wrong. Only numpy (2 files) and pickle in seed-etf-classifications were truly dead
- Confirmed iam.tf `us-east-2` for secrets is CORRECT (generate-volatility Lambda accesses secrets in us-east-2)
- Confirmed yang-lambda module defaults are correct as-is for single-account workspace
- Deferred: Lambda Layer extraction for ETF classification, env var parameterization, SFN definition templating

### Commits (5 code + 1 CI + 1 record)

| Commit | Message | Files |
|--------|---------|-------|
| `5095281b` | fix(yang): replace Unicode emoji/arrows with ASCII in 15 Lambda files (CLAUDE.md rule 13) | 15 |
| `739616d2` | fix(yang): replace deprecated datetime.utcnow() with datetime.now(timezone.utc) in 13 files | 13 |
| `0ee8232a` | fix(yang): remove dead numpy imports from factor-tilts and macro-timeseries | 2 |
| `35f4b5dc` | fix(yang): replace bare except with specific types in peer-performance safe_float() | 1 |
| `282c0ed0` | fix(yang): converge 3 copies of etf_classification.py to canonical values | 3 |
| `2ba20c26` | ci(yang-pipeline): upload artifacts for DEBT_1STRUN code cleanup | 1 (source map) |
| `4bcafe30` | ci: record deploy yang-pipeline @ 2ba20c26 [skip ci] | 1 (source map) |

### Deploy
- **Tag:** `yang-v2.3.2` (previous: `yang-v2.3.1`)
- **Terraform:** 0 add, 28 change, 0 destroy. 0-diff verified.

### Reviewer Notes (0.7.0_AE_CloudOps)
- PASS. One functional `R-squared` dict key (`'R2'`) retained in factor-tilts as it matches upstream data format.

---

## Phase 3: News Pipeline Fixes

### Plan
- Reviewed all 25 findings, verified each against actual code
- Dead files (lambda_function_old.py, lambda_function_fixed.py, backup file) do NOT exist on disk -- already cleaned up
- Vendored packages (package/, _build_tmp/) do NOT exist on disk -- already cleaned up
- deployment.zip (17.8MB) still exists but deferred (requires confirming S3-backed deploy is operational)
- text_cleaner.py duplication confirmed: 2 identical copies, defer Layer extraction
- Source map mojibake: appeared in Read tool but git showed no diff (encoding layer artifact)

### Commits (3 code + 1 CI + 1 record)

| Commit | Message | Files |
|--------|---------|-------|
| `2d8fb741` | fix(news): replace Unicode emoji/arrows/math symbols with ASCII in 8 Lambda files (CLAUDE.md rule 13) | 8 |
| `60a8848e` | fix(news): remove dead imports (sys, subprocess, Dict) from news-ingestion-scheduler | 1 |
| `53a834c8` | fix(news): replace deprecated datetime.utcnow() with datetime.now(timezone.utc) in 3 files | 2 |
| `23a51483` | ci(news-pipeline): upload artifacts for DEBT_1STRUN code cleanup | 1 (source map) |
| `11c8c879` | ci: record deploy news-pipeline @ 23a51483 [skip ci] | 1 (source map) |

### Deploy
- **Tag:** `news-v2.7.2` (previous: `news-v2.7.1`)
- **Terraform:** 0 add, 7 change, 0 destroy. 0-diff verified.

### Reviewer Notes (0.7.0_AE_CloudOps)
- PASS with 2 hygiene issues: (1) commit 1B included utcnow changes for news_ingestion_scheduler that were attributed to commit 2A in the plan -- commit boundary leak from parallel agent editing the same file. (2) CRLF-to-LF normalization on text_cleaner.py was an undocumented side-effect of commit 1A. Neither affects correctness.

---

## Phase 4: Market-Overview Fixes

### Plan
- Reviewed all 13 findings, verified each against actual code
- Non-ASCII/emoji: CLEAN -- 0 hits across all 5 functions
- Bare except: CLEAN -- 0 bare except blocks found (scan was wrong or fixed by another agent)
- Dead import (random.choice in fear-greed-fetcher): FALSE POSITIVE -- import doesn't exist
- RSI duplication: INTENTIONALLY DIFFERENT -- Wilder's smoothing (tiered, prices) vs SMA (regime, returns). Different algorithms for different use cases. Not a bug.
- Only actionable item: datetime.utcnow() in market-regime-classifier (7 occurrences)
- Reviewer caught that `timezone` was NOT already imported (plan initially claimed it was). Verified before editing -- added to import line.

### Commits (1 code + 1 CI + 1 record)

| Commit | Message | Files |
|--------|---------|-------|
| `d9266899` | fix(market-overview): replace deprecated datetime.utcnow() with datetime.now(timezone.utc) in market-regime-classifier | 1 |
| `0eb827ca` | ci(market-overview): upload artifacts for DEBT_1STRUN code cleanup | 1 (source map) |
| `81372f5b` | ci: record deploy market-overview @ 0eb827ca [skip ci] | 2 (source map + CHANGELOG) |

### Deploy
- **Tag:** `market-overview-v1.6.4` (previous: `market-overview-v1.6.3`)
- **Terraform:** 0 add, 6 change, 0 destroy. 0-diff verified.

---

## Phase 5: Build Tooling Fix

### Problem
`build-and-upload.sh` fails on Windows Git Bash because bun cannot resolve MSYS2 `/tmp/` paths. Previous workaround: a throwaway `deploy-wrapper.sh` in `C:/Windows/Temp/` that patched the script on-the-fly. Not sustainable.

### Fix

| Commit | Message | Files |
|--------|---------|-------|
| `ece75a07` | fix(ci): make build-and-upload.sh portable on Windows (TMPDIR + node preference) | 1 |
| `6c77831c` | docs: add Windows build notes for build-and-upload.sh (TMPDIR + node) | 3 |

**Changes to `build-and-upload.sh`:**
- All 5 `mktemp` calls and `ZIP_PATH` now use `${TMPDIR:-/tmp}` instead of hardcoded `/tmp/`
- JSON tool detection reordered: node > bun > python3 (bun has MSYS2 path resolution bug)
- Arrow Unicode replaced with ASCII `->`

**Documentation updated:**
- `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md` -- new section 2b: Windows Git Bash build instructions
- `START_HERE.md` -- one-line Windows note in Lambda deployment section
- `org/tier2_senior/0.5.0_AE_OpalETL/prompt.md` -- Windows build note after existing build gotcha
- `memory/MEMORY.md` -- updated stale PowerShell workaround note to reference canonical fix

**Usage on Windows:**
```bash
export TMPDIR="C:/Windows/Temp"
export PATH="/c/Users/AndrewBerman/Downloads/node-v24.13.0-win-x64/node-v24.13.0-win-x64:$PATH"
bash infra/aws/lambda/ci/build-and-upload.sh <pipeline>
```

---

## Deploy Summary

| Pipeline | Tag | Lambdas Updated | Terraform Result |
|----------|-----|-----------------|------------------|
| yang-pipeline | `yang-v2.3.2` | 28 | 0 add, 28 change, 0 destroy |
| news-pipeline | `news-v2.7.2` | 7 | 0 add, 7 change, 0 destroy |
| market-overview | `market-overview-v1.6.4` | 6 | 0 add, 6 change, 0 destroy |

**Total: 41 Lambda functions deployed.** All 0-diff verified. All tags pushed to remote.

---

## Deferred Items (Future Task Orders)

### Yang Pipeline
1. ETF Classification Lambda Layer -- extract canonical `etf_classification.py` + `etf_classifications_dynamodb.py` into shared Layer
2. Positioning inline dict cleanup -- investigate if inline dicts (lines 28-266) can import from shared module
3. Environment variable parameterization -- move hardcoded S3 bucket, table, distribution ID to TF-managed env vars
4. SFN definition templating -- replace 28 hardcoded ARNs with `templatefile()`

### News Pipeline
1. deployment.zip removal -- 17.8MB binary in repo, confirm S3-backed deploy is operational
2. text_cleaner.py Lambda Layer -- deduplicate 2 identical copies
3. keyword-intelligence-generator Layer migration -- move vendored openai to news-trending-deps layer
4. Orphaned IAM roles (3) -- audit usage before deletion
5. Broad managed policies on opal-news-lambda-role -- scope down after access audit
6. EventBridge dual targets (7 rules) -- investigate whether dual invocation is intentional

### Market-Overview
1. Hardcoded buckets (3 of 5 functions) -- low priority, all use same bucket
2. RSI algorithm documentation -- document why two different RSI implementations exist

### EC2 Services (not started)
1. seeking-alpha-scraper: 7 duplicated variants, no EC2 Terraform
2. smartx-exporter: emoji in logs, dead supervisor v1, stale TODOs
3. moltbot: stale branch reference (DEV vs CLOUD)

---

## Key File Paths

| File | Purpose |
|------|---------|
| `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-03-24/debt_1strun_scan.md` | Original scan (102 findings) |
| `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-03-24/debt_1strun_fix_and_deploy.md` | This session log |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DEBT_1STRUN.001.scan.md` | Task order |
| `infra/aws/lambda/ci/build-and-upload.sh` | Patched build script (ece75a07) |
| `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md` | Updated with section 2b |
| `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | Yang deploy record |
| `infra/aws/terraform/news-pipeline/CHANGELOG.json` | News deploy record |
| `infra/aws/terraform/market-overview/CHANGELOG.json` | Market-overview deploy record |
