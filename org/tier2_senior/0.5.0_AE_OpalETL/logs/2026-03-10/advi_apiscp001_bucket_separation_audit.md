# ADVI_APISCP.001: Bucket Separation Audit -- 0.5.0_AE_OpalETL

**Date:** 2026-03-10
**Start Time:** 19:45
**End Time:** 20:00

## Objective

Audit yang-pipeline, news-pipeline, and market-overview publisher S3 write targets.
Confirm all Opal-owned pipelines write exclusively to opal-data-portal-v2 with zero
overlap against opal-data-{firmId} partner bucket patterns. Document the invariant.

---

## Work Completed

### Audit Method

Grep for `Bucket` and `opal-data` across all publisher Lambda source files in:
- `infra/aws/lambda/v2_portal/yang_pipeline/**/*.py` (20+ Lambdas)
- `infra/aws/lambda/news_trending_analysis/lambda_function.py`
- `infra/aws/lambda/news_layer3_curation/lambda_function.py`
- `infra/aws/lambda/semantic-trending-topics-portal-publisher/lambda_function.py`
- `infra/aws/lambda/v2_portal/01_market_overview/lambdas/**/*.py` (5 Lambdas)

Cross-checked against `opal-data-bd`, `opal-data-49`, `opal-data-nna`, `opal-data-partner`,
`opal-data-firm` patterns — zero matches in any of the above.

### Findings by Pipeline

#### yang-pipeline (20 Lambdas)

Every Lambda uses `BUCKET = 'opal-data-portal-v2'` as a module-level constant.
All S3 put_object calls use this variable exclusively. Confirmed writes to:
- `opal-data-portal-v2/json/` — portfolio, valuation, macro, correlation outputs
- `opal-data-portal-v2/json-tiered/` — tiered outputs
- `opal-data-portal-v2/cache/fred/` — FRED cache (refresh-fred-cache Lambda)
- `opal-data-portal-v2/manifests/` — generate-manifest Lambda

No yang Lambda references any opal-data-{firmId} bucket.

#### news-pipeline (3 relevant Lambdas)

| Lambda | Write targets | Read/intermediate |
|--------|--------------|-------------------|
| news-trending-analysis | `opal-data-portal-v2/json/sentiment/keyword-sentiments.json` (TopicCloud) | reads `opal-data-news-v2` (trending reports) |
| news_layer3_curation | DynamoDB (opal-news-trending-daily) + chained invoke to publisher | reads `opal-data-news-av` (trending report) |
| semantic-trending-topics-portal-publisher | `DEST_BUCKET = 'opal-data-portal-v2'` (`json/semantic-trending/latest.json`) | reads `opal-data-news-v2` |

`opal-data-news-v2` and `opal-data-news-av` are internal news pipeline staging buckets —
news Lambdas READ from these, they do NOT write portal-facing data there.
No news Lambda writes to any opal-data-{firmId} pattern.

#### market-overview (5 Lambdas)

| Lambda | Write target |
|--------|-------------|
| opal-trending-topics-portal-publisher | `DEST_BUCKET = 'opal-data-portal-v2'` |
| opal-market-overview-tiered-generator | `DEST_BUCKET = 'opal-data-portal-v2'` (json-tiered/) |
| opal-market-regime-classifier | `S3_BUCKET = 'opal-data-portal-v2'` (json/market/) |
| opal-market-rsi-tiered-generator | `METRICS_BUCKET = 'opal-data-portal-v2'` |
| opal-portal-fear-greed-fetcher | `opal-data-portal-v2` (json/sentiment/fear-greed-index.json) |

Zero market-overview Lambda references any opal-data-{firmId} pattern.

### Negative Confirmation (Partner Bucket Isolation)

Searched across ALL three pipeline source trees for:
- `opal-data-bd` — 0 matches
- `opal-data-49` — 0 matches
- `opal-data-nna` — 0 matches
- `opal-data-partner` — 0 matches
- `opal-data-firm` — 0 matches

Partner bucket writes exist exclusively in BD pipeline (`bd-portal-publisher`) and
PartnerETL — neither is in scope for this audit. Separation is clean.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No code changes required | Audit confirms invariant already holds. Constraint in task order: audit + doc only. |
| Document internal buckets separately | opal-data-news-v2 / opal-data-news-av are pipeline-internal (read path only from portal-facing Lambdas); documenting them prevents future confusion about their role |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | Added `<bucket_separation_invariant>` block with 3 rules + per-pipeline write paths | Yes |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADVI_APISCP.001.opal-pipeline-bucket-audit.md` | status: pending -> complete | Yes |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Bucket separation invariant confirmed and documented in pipeline_inventory.xml.
Yang-pipeline (20 Lambdas), news-pipeline (3 publishers), and market-overview (5 Lambdas)
all write exclusively to opal-data-portal-v2. Zero writes to any opal-data-{firmId} pattern.
Internal staging buckets (opal-data-news-v2, opal-data-news-av) are read-path only.

---

## Next Steps

No follow-up required from AE on this work stream. The invariant is documented.

**Do NOT:**
- Modify PartnerETL pipelines — 0.6.0_AE_PartnerETL owns those
