# ADHC_GPTCST-002: Keyword Intelligence Cache Fix -- 0.5.0_AE_OpalETL

**Date:** 2026-03-10
**Start Time:** 18:30
**End Time:** 19:30

## Objective

Fix the keyword intelligence system so the pre-computed cache is used on subsequent requests.
Three targeted changes: (1) write-back on cache miss in portal_data_proxy, (2) MAX_KEYWORDS 20->10
to halve web search cost, (3) EventBridge fallback schedule updated + timing documented.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read portal_data_proxy get_keyword_intelligence() | Identified cache MISS path at line 1427, return at line 1673 |
| 2 | Read market-overview/lambdas.tf | portal_data_proxy used placeholder.zip + lifecycle.ignore_changes |
| 3 | Read keyword_intelligence_generator TF env vars | MAX_KEYWORDS = "20" in both TF and Python default |
| 4 | Read eventbridge.tf | Confirmed keyword_intelligence_daily DISABLED, schedule was cron(50 14,21) |
| 5 | Add _convert_floats() helper to portal_data_proxy | For float->Decimal before DynamoDB put_item |
| 6 | Add write-back block after live computation | Fire-and-forget, never blocks response |
| 7 | Change MAX_KEYWORDS default (Python + TF env var) | Both changed 20->10 |
| 8 | Update eventbridge.tf disabled rule schedule_expression | cron(50 14,21) -> cron(0 8,20); documented timing finding |
| 9 | Commit source changes | `00c8e10f` |
| 10 | Extract existing production zip, swap lambda_function.py, rezip | 8,388,559 bytes, SHA256: X1wdyxpaR15fYj84eN4DtzQSCa5SBPQzuvLgcknGvuE= |
| 11 | Upload new artifact to S3 | s3://opal-313476888478-lambda-artifacts/market-overview/opal-portal-data-proxy.zip |
| 12 | Migrate market-overview/lambdas.tf to S3-backed | Removed placeholder.zip + lifecycle.ignore_changes; added data.aws_s3_object + s3_bucket/key/version |
| 13 | Update lambda-source-map.json | artifact_sha256, deployed_commit, _note updated |
| 14 | Commit TF + source map | `ac405256` |
| 15 | terraform plan news-pipeline | 2 changes: keyword_intelligence_generator (env var), keyword_intelligence_daily (schedule) |
| 16 | terraform plan market-overview | 1 change: portal_data_proxy (code update via S3) |
| 17 | terraform apply news-pipeline | 0 added, 2 changed, 0 destroyed |
| 18 | terraform apply market-overview | 0 added, 1 changed, 0 destroyed |
| 19 | 0-diff both pipelines | No changes. Infrastructure is up-to-date. |
| 20 | Write CHANGELOG entries (manual, record-deploy skipped env-var-only changes) | Written to both CHANGELOG.json |
| 21 | Update pipeline_inventory.xml | market-overview-v1.6.0 |
| 22 | Commit + tag + push | `67340cfc`, tags news-v2.6.0 + market-overview-v1.6.0 |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| news-pipeline | `news-v2.6.0` | `ac405256` |
| market-overview | `market-overview-v1.6.0` | `ac405256` |

---

## Work Completed

### 1. portal_data_proxy Write-Back (Req 1)

Added `_convert_floats()` helper (float->Decimal) alongside existing `_convert_decimals()`.
Added write-back block in `get_keyword_intelligence()` between the payload dict construction
and the final `return cors_response(200, response_payload)`:

```python
try:
    item = _convert_floats(response_payload.copy())
    item['keyword'] = keyword_lower
    item['generated_date'] = today
    intelligence_table.put_item(Item=item)
    print(f"[keyword_intelligence] Cache WRITE: {keyword_lower} ({today})")
except Exception as e:
    print(f"[keyword_intelligence] WARN: cache write-back failed (non-fatal): {e}")
```

Key design choices:
- Uses same PK/SK schema as keyword-intelligence-generator (keyword lowercase + generated_date YYYY-MM-DD)
- `_convert_floats()` converts all floats to Decimal before put_item (DynamoDB requirement)
- try/except wraps entire block; failure logs WARN, response proceeds unmodified
- Response payload returned directly (no copy of cache item — avoids double Decimal conversion)

### 2. portal_data_proxy S3 Terraform Migration

The Lambda was using `filename = placeholder.zip` + `lifecycle.ignore_changes = [filename, source_code_hash]`
(code was deployed via a stale deploy.sh, never via Terraform). Migrated to S3-backed:
- Build method: extract existing production zip (Feb 23, with correct Linux pydantic_core wheels),
  replace lambda_function.py, rezip with PowerShell Compress-Archive
- IMPORTANT: Never rebuild with `pip install openai` on local machine — pydantic_core requires
  manylinux2014_x86_64 wheels. Always use the production zip as the base.
- Removed placeholder.zip and lifecycle.ignore_changes from lambdas.tf
- Added data.aws_s3_object.portal_data_proxy_artifact + s3_bucket/s3_key/s3_object_version

### 3. MAX_KEYWORDS 20 -> 10 (Req 2)

Changed in two places:
- `infra/aws/lambda/keyword_intelligence_generator/lambda_function.py`: Python default '20'->'10'
- `infra/aws/terraform/news-pipeline/lambdas.tf`: env var MAX_KEYWORDS "20"->"10"
TF env var takes precedence; Python default is a fallback. Both are now consistent at 10.

### 4. EventBridge Schedule + Timing Analysis (Req 3)

**Finding (documented per task order constraint):**
- news-trending-analysis fires at `cron(30 13,21 * * ? *)` = 13:30 UTC = 9:30 AM EDT (market open)
- keyword-intelligence-generator invoked async ~10-20 min after = ~13:50 UTC = ~9:50 AM EDT
- Pre-computed cache entries exist ~20 min AFTER market open
- Task order requirement: if cache entries exist before 9:30 AM ET, no schedule change needed
  (13:30 UTC = 9:30 AM EDT; pre-comp runs after this — so there IS a 20-min gap)

**Action taken:** Updated the DISABLED rule's `schedule_expression` from `cron(50 14,21 * * ? *)` to
`cron(0 8,20 * * ? *)` (8:00/20:00 UTC = 4 AM / 4 PM ET). Rule remains DISABLED — this is only
the intended fallback timing. The write-back from Req 1 mitigates first-user latency during the
9:30–9:50 AM EDT window.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| S3-migrate portal_data_proxy instead of deploy.sh | CLAUDE.md: Terraform is the only Lambda deployment mechanism. lifecycle.ignore_changes was a legacy workaround, not a sanctioned exception |
| Extract production zip as build base | pydantic_core needs Linux wheels. Cannot use local pip on Windows. Existing production zip has correct wheels. |
| Float->Decimal in write-back | DynamoDB requires Decimal for all numeric values. response_payload contains nested floats (sentiment_score, key_drivers avg_sentiment_estimate, etc.) |
| Copy payload before float conversion | Avoids mutating the payload that will be returned to the caller |
| Document EventBridge timing gap | Task order explicitly allowed skip with rationale. write-back (Req 1) mitigates the gap. Changing news-trending-analysis schedule would require a separate decision |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/portal_data_proxy/lambda_function.py` | _convert_floats helper, write-back block | Yes -- `00c8e10f` |
| `infra/aws/lambda/keyword_intelligence_generator/lambda_function.py` | MAX_KEYWORDS default '20'->'10' | Yes -- `00c8e10f` |
| `infra/aws/terraform/news-pipeline/eventbridge.tf` | Disabled rule schedule cron(50 14,21)->cron(0 8,20) + timing comments | Yes -- `00c8e10f` |
| `infra/aws/terraform/news-pipeline/lambdas.tf` | MAX_KEYWORDS env var "20"->"10" | Yes -- `00c8e10f` |
| `infra/aws/terraform/market-overview/lambdas.tf` | S3-backed migration (remove placeholder.zip + lifecycle.ignore_changes) | Yes -- `ac405256` |
| `infra/aws/lambda/ci/lambda-source-map.json` | portal_data_proxy SHA256 + commit + _note updated | Yes -- `ac405256` |
| `infra/aws/terraform/market-overview/CHANGELOG.json` | market-overview-v1.6.0 entry | Yes -- `67340cfc` |
| `infra/aws/terraform/news-pipeline/CHANGELOG.json` | news-v2.6.0 entry | Yes -- `67340cfc` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | market-overview-v1.6.0 | Yes -- `67340cfc` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Both deployments live and 0-diff confirmed. `opal-portal-data-proxy` now writes computed
keyword intelligence results to `opal-keyword-intelligence` DynamoDB on cache MISS, using the
same PK/SK schema as keyword-intelligence-generator. CloudWatch log pattern to confirm:
`[keyword_intelligence] Cache WRITE:` on first request, `[keyword_intelligence] Cache HIT:` on
second. `keyword-intelligence-generator` now pre-computes top 10 keywords (down from 20).
portal_data_proxy is now S3-backed in Terraform (market-overview-v1.6.0).

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Phase 3 cost tracking** -- OPENAI_USAGE lines now live on 4 deployed
   news-pipeline functions (news-v2.5.0). CloudOps can begin updating openai_cost_tracker.py
   to parse OPENAI_USAGE log format. Two remaining pre-Terraform functions (market-update-generator,
   opal-trending-image-generator) still pending Terraform integration -- flagged in ADHC_GPTCST-001 log.

2. **[Andrew] Verify write-back cache hit in CloudWatch** -- After next keyword intelligence
   request: confirm `[keyword_intelligence] Cache WRITE` followed by `[keyword_intelligence] Cache HIT`
   on second request for same keyword same day.

**Files to touch next:**
- None for AE on this work stream. Both pipelines are stable.

**Do NOT:**
- Rebuild portal_data_proxy zip with local `pip install openai` -- use production zip as base
- Re-enable keyword_intelligence_daily EventBridge rule without testing the chain invocation
