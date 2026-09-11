# Deploy Completion Record
**Date opened:** 2026-09-11T17:12:24.312718+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T180957Z
**Deploy:** news-layer3-curation: DIRECTION-CONSISTENCY GATE + both OpenAI passes to gpt-5.6-sol (Andrew-direct 2026-09-11 'just commit/deploy'; /open-calls CALL1+CALL2 approved)
**Authored by:** 0.1.0_DS_MarketIntelligence
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit bc7514c173 | code committed BEFORE the upload and BEFORE the apply | bc7514c173 (code) + 76dcff5718 (terraform env + this ledger's OPEN sentinel), both on CLOUD, both committed BEFORE the S3 upload and BEFORE the apply. The terraform half required GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL (audited): infra/aws/terraform is AE lane, this seat is DS; authority is Andrew-direct 'just commit/deploy the updates'. | CLOSED 20260911T174122Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/news-pipeline/opal-news-layer3-curation.zip | head-object Metadata.content-sha256 equals the zip rebuilt from COMMITTED source | put-object VersionId 9Fa6_vu7CrObA9PItgVCx94tQoLfvqwG; head-object Metadata.content-sha256 = FWeKNAniiHAIdnpOQgz6fgsJcaZ42l+6cJKGDc9+uZE=, byte-identical to the zip rebuilt from the COMMITTED blob at bc7514c173 (git show, NOT the worktree -- autocrlf would hash the checkout). 39665 bytes, 1 member, deterministic 1980-01-01 timestamp so it is rebuildable. | CLOSED 20260911T174122Z |
| L3 | activation | terraform apply infra/aws/terraform/news-pipeline | plan shows ONLY this lambda: source_code_hash + s3_object_version + GPT_MODEL/ANALYSIS_GPT_MODEL env; baseline read 'No changes' before the act | safe-apply (halt-gate + comp-tagauthz passed) -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. The ONLY resource touched is aws_lambda_function.layer3_curation; differing attributes are s3_object_version, source_code_hash, last_modified, and the two env vars (GPT_MODEL gpt-4o->gpt-5.6-sol, ANALYSIS_GPT_MODEL added). Baseline plan at this tip read 'No changes' BEFORE the upload, so the apply could carry nothing else. | CLOSED 20260911T174123Z |
| L4 | verify | lambda get-function-configuration opal-news-layer3-curation | live CodeSha256 == S3 content-sha256 == locally built zip sha256 (triple equality), and Environment shows both models | TRIPLE EQUALITY 3 of 3, compared against each other rather than any one asserted: local zip sha256 == S3 Metadata.content-sha256 == live CodeSha256 == FWeKNAniiHAIdnpOQgz6fgsJcaZ42l+6cJKGDc9+uZE=. Live Environment shows GPT_MODEL=gpt-5.6-sol and ANALYSIS_GPT_MODEL=gpt-5.6-sol. LastModified 2026-09-11T17:34:10Z. | CLOSED 20260911T174124Z |
| L5 | verify | terraform plan infra/aws/terraform/news-pipeline | No changes. Your infrastructure matches the configuration. | terraform plan on infra/aws/terraform/news-pipeline -> 'No changes. Your infrastructure matches the configuration.' Run AFTER the second apply (the flag-not-drop redeploy at 494b80e867 / sha HXl8HhPKq7CXFNX8KUkdfreYpj5quXBrg31cLMaoR7I=), so it grades the FINAL state, not the first one. RUNTIME CONFIRMATION beyond the hash: two live invokes against throwaway partitions 2099-01-01/02 (force_refresh) -- the function imports and runs on gpt-5.6-sol on BOTH passes; the deterministic gate fired exactly once ('china oil demand', support=0 oppose=2, dropped) and the six model direction_check flags logged '(flag only, not dropped)'. Backfills fell 6 -> 1. Both test partitions deleted (0 rows remain in each); the live 2026-09-11 partition still reads 19 rows, untouched. | CLOSED 20260911T180957Z |

## Log

- 20260911T171224Z OPENED by 0.1.0_DS_MarketIntelligence with 5 leg(s)
- 20260911T174122Z LEG L1 closed: bc7514c173 (code) + 76dcff5718 (terraform env + this ledger's OPEN sentinel), both on CLOUD, both committed BEFORE the S
- 20260911T174122Z LEG L2 closed: put-object VersionId 9Fa6_vu7CrObA9PItgVCx94tQoLfvqwG; head-object Metadata.content-sha256 = FWeKNAniiHAIdnpOQgz6fgsJcaZ
- 20260911T174123Z LEG L3 closed: safe-apply (halt-gate + comp-tagauthz passed) -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. The ONLY 
- 20260911T174124Z LEG L4 closed: TRIPLE EQUALITY 3 of 3, compared against each other rather than any one asserted: local zip sha256 == S3 Metadata.conten
- 20260911T180957Z LEG L5 closed: terraform plan on infra/aws/terraform/news-pipeline -> 'No changes. Your infrastructure matches the configuration.' Run 
- 20260911T180957Z CLOSED -- all 5 legs proven
