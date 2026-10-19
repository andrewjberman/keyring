# News Scanner contextual sentiment deployed - 4.0.0_SA_CRO~D1CDX
**archetype:** IMPLEMENT
**Date:** 2026-10-19
**Task Order:** ad-hoc NEWS_SENTIMENT_FIX_20261019; Andrew-direct full implementation and egress authority
**Status:** COMPLETE
**Window:** Current News Scanner session through 17:50Z release closure; latest prior base-seat log was 2026-10-06, another lane.

## Objective

Explain and repair the bullish FinBERT labels inside the bearish coal topic. Preserve original scores, assess available article text in market context, disclose missing evidence, align the UI with topic selection, validate the deployed result and provide conditional rollback.

## Compiler Tools

| Tool | Command / concern | Result | Note |
|------|-------------------|--------|------|
| comp-which | News Scanner sentiment flow and deployment evidence | PARTIAL | Routed initial inspection; final audit question had no curated match and explicitly admitted raw search |
| comp-estate | News runtime surfaces | PASS | Helped locate deployed resources |
| comp-find | News Scanner source lookup | FAIL | Timed out; not used as negative evidence |
| comp-transform | ExecutiveSummary schema/fields | FAIL | Resolved different ExecutiveSummaryPanel; not accepted as this component's validation |
| comp-routes | News routes | PARTIAL | Desired-plane result, not live proof |
| comp-blast | News schema surface | FAIL | Command unavailable; recorded repository gap |
| comp-pulse diff | safe-commit, days=7 top=8 | PARTIAL | Generic filenames match unrelated INF, AMGT and opal-assets claims; citations read, actual source/build/live checks retained |
| comp-tagauthz | safe-apply scoped plans | PASS | Zero candidate tag collisions for these code-only updates |

**What worked:** Estate discovery and scoped deploy parity checks located and verified the four runtime packages. The compiler router correctly disclosed missing coverage for final receipt inspection.

**What failed:** Component lookup mismatch, timeout and unavailable blast tool. Crossbox deploy check repeatedly timed out in WARN mode; it was not treated as a clean readiness result. Existing client-account hash-list absence also means that optional commit check did not run.

**Gap found:** The compiler does not establish actual sentiment input coverage or rendered topic/article consistency. Exact source inspection, bounded live invocation, S3 readback and viewed browser output supplied those checks.

## Work Completed

1. Canonical exact-seat load and measured readiness passed all nine checks. Launcher helpers remained launcher-owned; canonical suffixed inbox was empty. Two old unrelated unsuffixed research messages surfaced through the deploy halt gate; read and left in place, documented HALT_ACK used. Explicit Andrew authority superseded CRO's default read-only scope, with audited ownership override and no permission-registry edit.
2. Live baseline proved FinBERT input was title plus at most 500 summary characters, not fetched article bodies. Nikkei had no summary, raw +0.9444; the UI averaged raw confidence into a green +0.5461 topic despite bearish curation. The original six entries contained five unique URLs.
3. Source 6d16b9b93f added bounded article retrieval, coverage/provenance, strict evidence quotes, broad-market impact with beneficiaries, mixed/insufficient outcomes and URL deduplication. The batch writes only additive news_context and preserves raw FinBERT. Trending, curation and publisher propagate the contract. Portal uses topic direction and discloses article evidence.
4. Live acceptance rejected a headline-only Nikkei bullish result. Conditional data rollback restored six article fields and four topic fields and republished at 17:30Z. Source b4e7c36602 deterministically gates headline-only evidence to insufficient before a model call and rejects old directional headline caches.
5. Curation fix 5edd941fce replaces Scan(Filter date, Limit=1) with consistent partition Query and fails closed on lookup errors. Scoped safe-apply activated the final package. Live force_refresh=false now returns skipped=true and preserves all 20 current rows exactly.
6. Final four live CodeSha256 values match RELEASE_MANIFEST.json, Active/Successful. Final scoped Terraform news and publisher plans show no changes. Deployment records: a16d4e78e9 news, 84d8cd212e publisher. Source map parity checked; no IAM or schedule changes.
7. Final published coal topic is bearish, five unique articles: two bearish with article text, one mixed with article text, Nikkei and Seeking Alpha insufficient with headline only. All 20 published topics agree with their directional groups and contain no repeated URLs within the displayed list. The stale reported-topic count was conditionally changed from six to five.
8. Portal PROD 8cd45f623bdfae12ac6e4cfcfc8e0d74325ed4c3, portal-v2.1.243, CI 39294118121 SUCCESS. One chosen candidate 0d5aa361d039bc80e4fc6d1567b0f938d873ed42, /market. Main portal stays DEV at a48fa073c2bdc166cd1b27e3eae7a9f354e8e767; DEV was not pushed. Both temporary worktrees removed and pruned. Workspace records stay LOCAL; shared branch was not pushed by this seat.
9. Validation: 21 Python regressions, 9 frontend assertions, TypeScript/build and 8 live model cases passed; five exact source URLs exercised. Viewed production assets with actual S3 payload fixture: red BEARISH, five articles, Nikkei Uncertain/Headline only. This is a served-asset browser check with auth stub, not authenticated HTTP end-to-end coverage. Model cases are a small regression set, not a general accuracy estimate.
10. Rollback tool verified all four original package hashes, all four current live/artifact matches and ten conditional data fields. Data rollback was exercised; code rollback was prepared and read-only verified. Audit and receipt committed in 6fbf4a738b. Preserve private .runtime/news-sentiment-fix-20261019 backups and journals; manifests alone cannot restore bytes.
11. Workspace portal-pointer commit e4c15984e2 is LOCAL against measured origin/box/dell1 b1de25614a07ed25ecb1bdea112f5ec6c2c8cdbc. All four deployment-ledger legs closed with proof and the sentinel removed. COO freeze-release receipt: 20261019T175033Z_4.0.0_SA_CRO_D1CDX_COMPLETE__News_Scanner_repair__release_s.md, filesystem plus broker. First message exceeded the broker's 150-word cap and wrote nothing; shortened report delivered successfully. Two significant outbound messages: release-window opening and completion, both required by prod-deploy.

## Postmortem

The intended curation no-op probe exposed the existing Scan/Limit defect and regenerated today's topics. SDK timeout retries started four executions before the exact local probe process was stopped. All four completed by 17:41:56Z before final repair. Raw article records were not deleted. A complete original topic-set snapshot was not captured, so whole-topic-set restoration is not claimed. The guard is fixed, its read-error path is tested, future invokes disable retries and use an appropriate timeout, and the regenerated final set was validated. This validation mistake and the first rejected model result are explicitly retained in CHANGELOG.md and FIRST_LIVE_REJECTION.json.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Headline-only means insufficient | Live model outputs varied on the same sparse evidence; a deterministic guard prevents unverified directional claims |
| Preserve raw FinBERT separately | Language sentiment and broad-market impact answer different questions; original records remain auditable |
| Explicit body/summary/headline coverage | Restricted Nikkei content cannot be presented as read |
| Bounded scheduled backfill | Existing cadence and latency bounds remain; no claim of complete historical rescoring |
| Conditional rollback | Never overwrite a subsequent writer or restore whole article records |

## Files Modified

| File / group | Change | Committed |
|--------------|--------|-----------|
| infra/aws/lambda/finbert_batch_processor/ | Context extraction/contract, bounded enrichment, headline evidence gate | 6d16b9b93f, b4e7c36602 |
| infra/aws/lambda/news_trending_analysis/, news_layer3_curation/, trending_topics_portal_publisher/ | Context propagation, deduplication, topic direction, curation idempotence | 6d16b9b93f, 5edd941fce |
| infra/aws/terraform/news-pipeline/finbert-batch.tf | Canonical versioned code artifact and reversible activation | 6d16b9b93f |
| infra/aws/lambda/ci/function-map/ and scoped Terraform CHANGELOG.json files | Package/source pins and deployed parity | 84d8cd212e, a16d4e78e9 |
| tests/news_sentiment/ | Extraction, evidence, classification and migration regressions | 6d16b9b93f, b4e7c36602, 5edd941fce |
| portal/src/lib/newsSentiment.ts, API market types, ExecutiveSummary, scripts/test-news-sentiment.ts | Direction consistency, coverage labels, frontend assertions | Feature 0d5aa361; PROD 8cd45f62; DEV a48fa073 |
| deliverables/NEWS_SENTIMENT_FIX_20261019/ | Authority, change journal, baselines, release/validation receipts, migration and rollback tools | 6347d7ff87, 6d16b9b93f, b4e7c36602, 6fbf4a738b |

## Blockers

None for this repair. Restricted publisher bodies remain unavailable and are honestly labeled; this does not block correct abstention.

## Current State

The repair is live in the four named AWS Lambdas and portal-v2.1.243. S3 opal-data-portal-v2/json/trending/latest.json contains the corrected coal example and 20 direction-consistent topics. Committed deliverables/NEWS_SENTIMENT_FIX_20261019/CHANGELOG.md, RELEASE_MANIFEST.json, VALIDATION_RECEIPT.json and ROLLBACK.md are the durable evidence; exact before-images and zip archives remain in the ignored runtime directory. The existing batch schedule gradually enriches older articles; unassessed legacy stories are not presented as verified article-level directional assessments.

## Next Steps

No further implementation is required for this repair. Retain rollback material. [0.0.0_AB_MSTR] Carry the local workspace records through the ordinary integration flow; do not push this seat's shared branch directly. [2.0.0_SA_COO] Production freeze release is reported through canonical codex-send under .claude/skills/prod-deploy/SKILL.md; it does not ask for additional approval.
