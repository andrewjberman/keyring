# Deploy Completion Record
**Date opened:** 2026-09-11T19:25:18.057131+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T194041Z
**Deploy:** news-layer3-curation: backfilled topics get a real <=45-char headline + the selection pass's relevance check (Andrew-direct 2026-09-11 'just fix the pre-existing defect')
**Authored by:** 0.1.0_DS_MarketIntelligence
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit d6913f1e9b | code committed BEFORE the upload and BEFORE the apply | d6913f1e9b (the fix) + 3b091aaf3c (this ledger's OPEN sentinel), both on CLOUD, both committed BEFORE the upload and BEFORE the apply. The sentinel's FIRST attempt failed (rc=128, message file unwritten by a shell-interpolated path); the deploy chain wrongly continued past it on a grep guard and re-applied the PREVIOUS bytes -- caught by comparing HEAD's blob sha to the live CodeSha256, and redone with a repository-verified commit check and a hash-pinned build. | CLOSED 20260911T193326Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/news-pipeline/opal-news-layer3-curation.zip | head-object content-sha256 equals a zip rebuilt from the COMMITTED blob | put-object VersionId a3tIkpIz9gUHzIo5KeGiwjWYY_T9oPCG; head-object Metadata.content-sha256 = bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=. Built from git show d6913f1e9b:<path> (PINNED hash, not HEAD~N -- another seat's commit had landed between steps), 144,267-byte blob, deterministic 1980-01-01 member; the built sha was asserted equal to an EXPECTED value computed in a separate step BEFORE upload. | CLOSED 20260911T193326Z |
| L3 | activation | terraform apply infra/aws/terraform/news-pipeline | plan shows ONLY this lambda, ONLY source_code_hash + s3_object_version | safe-apply -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. ONLY aws_lambda_function.layer3_curation; ONLY source_code_hash (DA8R9OMHOhYTxI9Nc76SH1lcNsNoPTylQYSLv2RkPms= -> bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=) and s3_object_version. No env change. | CLOSED 20260911T193326Z |
| L4 | verify | lambda get-function-configuration opal-news-layer3-curation | triple equality local zip == S3 metadata == live CodeSha256 | TRIPLE EQUALITY against the EXPECTED CONSTANT bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M= (not against the just-built value -- a check that compares X to X cannot fail): S3 Metadata.content-sha256 == live CodeSha256 == expected. The earlier false pass (3 of 3 on DA8R9O..) is recorded in L1. | CLOSED 20260911T193327Z |
| L5 | verify | live invoke on throwaway date 2099-01-05 | every backfilled row has a <=45-char headline, BLOCKED: RELEVANCE fires or not as the candidates warrant, 0 raw titles >45, 0 tracebacks, china slot still a true carrying topline | Rehearsal 6 on throwaway date=2099-01-06 against the LIVE bytes (CodeSha256 bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=, commit d6913f1e9b): curation 29,540 prompt tokens, 10+10 selected; merge collapsed bullish 10->7 and bearish 10->8 (same pre-existing step as rehearsal 4); 5 backfills, EVERY one with a GPT-written headline (42/37/38/40/38 chars) where rehearsal 4's were 78-char raw titles; 20 rows, 0 over 45, max 42; NO_SUPPORTING_NARRATIVE 0; TOPLINE_SOURCE warnings 0; tracebacks 0; china slot bullish-3 'OPEC Sees Oil Demand Growth Surge' still a true carrying topline. HONEST LIMITS: BLOCKED: RELEVANCE fired 0 times (no advice-column candidate this run) and HEADLINE_CAPPED fired 0 times (GPT wrote all five under 45) -- both mechanisms are proven by the rendered write_headline prompt and the offline exercise (cap on the two 78-char offenders -> 43/44), not by a live rejection yet. Provenance gap noted for follow-up: the wrapped topic's backfilled=True and topline_source_check are not persisted to the DynamoDB row, so the LOG, not the row, is the evidence of which 5 were backfilled. Test partition deleted after read. | CLOSED 20260911T194041Z |

## Log

- 20260911T192518Z OPENED by 0.1.0_DS_MarketIntelligence with 5 leg(s)
- 20260911T193326Z LEG L1 closed: d6913f1e9b (the fix) + 3b091aaf3c (this ledger's OPEN sentinel), both on CLOUD, both committed BEFORE the upload and BEF
- 20260911T193326Z LEG L2 closed: put-object VersionId a3tIkpIz9gUHzIo5KeGiwjWYY_T9oPCG; head-object Metadata.content-sha256 = bWvoG+WeKBa/b/S1NPHV2W1G2p1
- 20260911T193326Z LEG L3 closed: safe-apply -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed'. ONLY aws_lambda_function.layer3_curation; ON
- 20260911T193327Z LEG L4 closed: TRIPLE EQUALITY against the EXPECTED CONSTANT bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M= (not against the just-built v
- 20260911T194041Z LEG L5 closed: Rehearsal 6 on throwaway date=2099-01-06 against the LIVE bytes (CodeSha256 bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=
- 20260911T194041Z CLOSED -- all 5 legs proven
