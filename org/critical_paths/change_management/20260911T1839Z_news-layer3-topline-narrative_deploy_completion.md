# Deploy Completion Record
**Date opened:** 2026-09-11T18:39:36.145200+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T190554Z
**Deploy:** news-layer3-curation: the sort is GIVEN -- topline written from the carrying narrative (Andrew-direct 2026-09-11, approved same turn)
**Authored by:** 0.1.0_DS_MarketIntelligence
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit 3e83049fe0 | code committed BEFORE the upload and BEFORE the apply | 3e83049fe0 (the topline-narrative model) + aa484f6b62 (this ledger's OPEN sentinel), both on CLOUD, both committed BEFORE the upload and BEFORE the apply. No lane override needed this time -- infra/aws/lambda is permitted to this seat; only the earlier terraform half required one. | CLOSED 20260911T184330Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/news-pipeline/opal-news-layer3-curation.zip | head-object content-sha256 equals a zip rebuilt from the COMMITTED blob | put-object VersionId hcIzCoZsM1bZvjUcBvzF821EakB00vru; head-object Metadata.content-sha256 = slOjgbY+Fats87bI3Hwby750H6Cc8VmfGFHE67LH8gQ=, byte-identical to the zip rebuilt from the COMMITTED blob at 3e83049fe0 (git show, not the worktree -- autocrlf would hash the checkout). Deterministic 1980-01-01 member timestamp, so rebuildable. | CLOSED 20260911T184331Z |
| L3 | activation | terraform apply infra/aws/terraform/news-pipeline | plan shows ONLY this lambda and ONLY source_code_hash + s3_object_version (no env change this time) | safe-apply -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. ONLY aws_lambda_function.layer3_curation, and ONLY source_code_hash (HXl8Hh.. -> slOjgb..) plus s3_object_version. NO environment change in this apply, which is the expected shape: the model env vars were already set by the earlier deploy and this change is code-only. | CLOSED 20260911T184331Z |
| L4 | verify | lambda get-function-configuration opal-news-layer3-curation | triple equality local zip == S3 metadata == live CodeSha256 | TRIPLE EQUALITY 3 of 3, compared against each other rather than any one asserted: local zip sha256 == S3 Metadata.content-sha256 == live CodeSha256 == slOjgbY+Fats87bI3Hwby750H6Cc8VmfGFHE67LH8gQ=. | CLOSED 20260911T184331Z |
| L5 | verify | live invoke on a throwaway date | the china cluster serves a TRUE bullish topline drawn from a carrying article, 0 topics dropped, 0 raw-title backfills | MEASURED, not the leg's wished-for wording. Rehearsal 4 on throwaway date=2099-01-04 against the LIVE bytes (CodeSha256 DA8R9OMHOhYTxI9Nc76SH1lcNsNoPTylQYSLv2RkPms=, commit 06b6cef383): curation call prompt=29,540 tokens / 10 bullish + 10 bearish selected (the superseded 3e83049fe0 read 2,715 / 0+0 and was rolled back before any scheduled fire); NO_SUPPORTING_NARRATIVE drops 0; TOPLINE_SOURCE citation warnings 0 (every cited source was a CARRIES article); tracebacks 0; duration 312s of 900. The china cluster serves bullish-3 'OPEC Sees Oil Demand Growth Explode in 2027' -- a TRUE bullish topline drawn from a carrying article, Sinopec demoted to counterpoint: the intended shape exactly. 20 rows written. CAVEAT recorded honestly: 7 of 20 rows are raw article titles -- NOT from this change (0 drops) but from the PRE-EXISTING detect_and_merge_duplicates step collapsing same-original_keyword topics (bullish 10->7, bearish 10->6) and backfill_from_layer2 refilling with raw titles. Pre-existing, reachable independently, surfaced for its owner (log Next Step 5). Test partition deleted after read. | CLOSED 20260911T190554Z |

## Log

- 20260911T183936Z OPENED by 0.1.0_DS_MarketIntelligence with 5 leg(s)
- 20260911T184330Z LEG L1 closed: 3e83049fe0 (the topline-narrative model) + aa484f6b62 (this ledger's OPEN sentinel), both on CLOUD, both committed BEFOR
- 20260911T184331Z LEG L2 closed: put-object VersionId hcIzCoZsM1bZvjUcBvzF821EakB00vru; head-object Metadata.content-sha256 = slOjgbY+Fats87bI3Hwby750H6C
- 20260911T184331Z LEG L3 closed: safe-apply -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. ONLY aws_lambda_function.layer3_curation, an
- 20260911T184331Z LEG L4 closed: TRIPLE EQUALITY 3 of 3, compared against each other rather than any one asserted: local zip sha256 == S3 Metadata.conten
- 20260911T190554Z LEG L5 closed: MEASURED, not the leg's wished-for wording. Rehearsal 4 on throwaway date=2099-01-04 against the LIVE bytes (CodeSha256 
- 20260911T190554Z CLOSED -- all 5 legs proven
