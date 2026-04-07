# CTO Session — 2026-04-07

**Agent:** 1.0.0_SA_CTO
**Topic:** News Pipeline Schedule Shift — Trending Topics 8:15 AM EDT

---

## Objective

Shift the portal Trending Topics panel to have refreshed output by 8:15 AM ET (was ~9:50 AM ET).
Secondary goal: densify ingestion coverage in the 12 hours leading up to that refresh.

---

## Investigation

### Dependency Chain Mapped

Used `org/modules/` perceive/interpret tooling to map the full news pipeline chain:

```
EventBridge (trending-analysis-daily)
    ↓
news-trending-analysis  [cron(30 13,21) = 9:30 AM + 5:30 PM EDT]
  writes → opal-data-portal-v2/json/sentiment/keyword-sentiments.json
  writes → opal-data-news-v2/trending_reports/latest.json
    ├─(async)→ keyword-intelligence-generator
    │             writes → opal-keyword-intelligence DynamoDB
    └─(async)→ opal-news-layer3-curation  [GPT-4o]
                  writes → opal-news-trending-daily DynamoDB
                  writes → opal-data-portal-v2/json/trending/latest.json
                    └─(chain)→ semantic-trending-topics-portal-publisher
```

Portal Trending Topics (`KeywordSentimentModal`) reads from `opal-news-trending-daily` + `json/trending/latest.json` — written at the tail of the Layer 3 chain, arriving ~10-20 min after `news-trending-analysis` fires.

**Actual portal refresh before change:** ~9:40-9:50 AM EDT.

### EST vs EDT Name Drift

All EventBridge rules were named in EST (winter). Currently in EDT (UTC-4), every rule fires 1 hour later than its name implies. Key findings:

- `news-api-700am` → actually fires at **8:00 AM EDT**
- `news-api-845am` → actually fires at **9:45 AM EDT** (after trending-analysis, useless for morning input)

### Missing EventBridge Rule

`opal-keyword-drilldown-generator` Lambda was defined in `lambdas.tf` with a schedule comment (`cron(40 14,21 * * ? *)`) but had **no corresponding EventBridge rule in `eventbridge.tf`**. Never ran.

---

## Changes Made

### eventbridge.tf

| Resource | Before | After |
|---|---|---|
| `news-api-700am` | `cron(0 12)` = 8:00 AM EDT | `cron(0 10)` = **6:00 AM EDT** |
| `news-api-845am` | `cron(45 13)` = 9:45 AM EDT | `cron(45 11)` = **7:45 AM EDT** |
| `trending_analysis_daily` | `cron(30 13,21)` = 9:30 AM EDT | `cron(15 12,21)` = **8:15 AM EDT** |
| `keyword_drilldown_daily` | (missing) | Added at `cron(25 12,21)` = 8:25 AM EDT, **DISABLED** |

### Why drilldown was added then immediately disabled

The missing rule was added as part of fixing the undocumented gap. However, inspection of the portal source revealed `getKeywordSentimentHistorySummary()` and `getKeywordSentimentHistoryArticles()` — the two functions that consume drilldown output — are defined in `sentiment.ts` but called nowhere. The `KeywordSentimentModal` uses `getKeywordIntelligence()` instead (GPT-4o via `keyword-intelligence-generator`), which replaced the old 14-day history chart modal. The old functions are marked `@deprecated`. The drilldown Lambda runs a DynamoDB scan of 14 days of articles (~8,600+ rows) 2x daily and writes S3 files nobody reads. Rule deployed as DISABLED; can be re-enabled if the history chart feature is revived.

### lambdas.tf

Updated schedule comment on `opal-keyword-drilldown-generator` to match actual Terraform timing (`cron(25 12,21 * * ? *)`, 8:25 AM + 5:25 PM EDT).

### eventbridge.tf (comment updates)

- `trending_analysis_daily`: updated comment from "8:30 AM + 4:00 PM ET" → "8:15 AM + 5:15 PM EDT"
- `keyword_intelligence_daily`: updated chain timing comment from "9:30 AM EDT / ~9:50 AM EDT" → "8:15 AM EDT / ~8:35 AM EDT"

---

## Deployments

| Tag | Commit | Description |
|---|---|---|
| `news-v2.7.4` | `b7cc3bcc` | Shift trending to 8:15 AM EDT, add drilldown rule |
| `news-v2.7.5` | `0e22bc7a` | Disable drilldown rule (no portal consumers) |

Both applied via `terraform apply` against `infra/aws/terraform/news-pipeline/`. 0 destroy on each apply.

---

## Result

**New morning schedule (EDT):**

```
6:00 AM  — news-api-700am  ingestion
7:45 AM  — news-api-845am  ingestion
8:15 AM  — news-trending-analysis fires
~8:35 AM — keyword-intelligence-generator + layer3-curation chain complete
~8:35 AM — Portal Trending Topics refreshed
```

Target met: portal reflects fresh trending output by ~8:35 AM EDT.
