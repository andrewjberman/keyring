# News Scanner rollback
**archetype:** IMPLEMENT

Authority and scope: CHANGELOG.md. Final live hashes are in RELEASE_MANIFEST.json; original hashes are in BASELINE_MANIFEST.json.

1. Run `python org/tier1_exec/4.0.0_SA_CRO/deliverables/NEWS_SENTIMENT_FIX_20261019/rollback.py verify`. It verifies all four exact baseline package hashes. Backups are under `.runtime/news-sentiment-fix-20261019/backup`; retain this directory until the repair is accepted.
2. For backend rollback, run `rollback.py stage-code` first. It refuses any Lambda or artifact whose hash differs from this release. `stage-code --execute` stages the exact original package bytes at the existing versioned artifact keys, with conditional S3 writes. It does not activate them.
3. Plan the news-pipeline targets `aws_lambda_function.finbert_batch_processor`, `aws_lambda_function.trending_analysis`, `aws_lambda_function.layer3_curation` and market-overview target `module.trending_topics_publisher.aws_lambda_function.this`. Review the saved plans: code-only updates, no deletions or unrelated configuration changes. Apply each through `.tools/safe-apply.sh`, then compare all four live CodeSha256 values with BASELINE_MANIFEST.json. The batch remains managed through its new versioned Terraform declaration; original code bytes restore its previous behavior.
4. Article enrichment is additive; previous code ignores news_context and original FinBERT fields are unchanged. For optional removal of this repair's journaled attributes, run `rollback.py data`, then `data --execute`. Every field restore checks its exact after-image and uses a DynamoDB condition; a subsequent writer causes a refusal. Never restore a whole article row or delete an article.
5. For current curated topics, restore journaled fields in the same way, then run the restored publisher. This regenerates current portal data using the old contract and avoids overwriting newer articles with an old complete S3 snapshot. S3 before-images remain available for forensic comparison.
6. For frontend rollback, create a new candidate from current origin/PROD and invert only the News Scanner feature changes (the exact feature and release hashes are recorded in the final receipt). Use the canonical chosen-set /prod-deploy procedure; never reset or force-push PROD. Confirm CI and the served bundle. A stale production base or concurrent release must be reviewed rather than overwritten.
7. Record executed steps, package/readback hashes, data conflicts and final live status in CHANGELOG.md and the deploy-completion ledger. A failed rollout is either completed or rolled back in-session; do not label a partly applied release complete.

The rollback tool defaults to read-only verification. Scheduled enrichments made after the bounded migration may retain additive context, which old code ignores. Rollback is not a claim to undo subsequent unrelated news ingestion or curation.

## Pinned release and exercised recovery

- Frontend feature: 0d5aa361d039bc80e4fc6d1567b0f938d873ed42. Production release: 8cd45f623bdfae12ac6e4cfcfc8e0d74325ed4c3, portal-v2.1.243, CI 39294118121 success. Invert the feature changes on a fresh current PROD candidate, not the release merge itself.
- Backend source: batch b4e7c36602, curation 5edd941fce, trending and publisher 6d16b9b93f. All four original zip archives and after-image checks verified after final activation.
- At 17:30Z, the first live headline-only result failed acceptance. Conditional data rollback restored six article attributes and four topic fields, and the publisher withdrew that result. The final deterministic headline gate was then deployed and validated. Code rollback has been prepared and verified without activating old code.
- During validation, the old curation guard allowed four SDK-retried executions to regenerate today's topic set. All finished before final migration. The new guard was exercised successfully against 20 existing rows. There is no complete before-image of the old topic set; the conditional journals restore the bounded repair's fields only, not the entire regeneration.
- Preserve `.runtime/news-sentiment-fix-20261019/backup/`, `journals/`, `first-live-rejection/` and `release.json`. These private local files contain exact rollback material; committed manifests prove hashes but do not replace the zip archives or DynamoDB wire before-images.
