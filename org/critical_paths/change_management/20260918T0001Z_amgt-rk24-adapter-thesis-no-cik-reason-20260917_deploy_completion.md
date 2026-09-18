# Deploy Completion Record
**Date opened:** 2026-09-18T00:01:46.554972+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T001702Z
**Deploy:** AMGT-rk-24 adapter: FILINGS_PREFIX + _read_filing_source_object + drafting_reason merge on the thesis route. Lambda deploy 2 of 4, batch B. Co-signed CTO 533f216c74 / COO 6b7d4f2341, HALF 3.
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | PRE-ACT live get_function_configuration: CodeSha256 iGmDkRbA6ZenF0CHAgU7nwNZkmdUEzMKRdBEJsDlbP0= (this act's own predecessor, rk-23's live deploy), LastModified 2026-09-17T23:33:34Z, CodeSize 783126, MemorySize 512, Timeout 29, one layer, Env unchanged. Pre-deploy census: 13 of 13 GET routes -> 200. AC1 BEFORE (name 2317_TT_Equity, sampled first of 237 unresolved names): drafting_reason='no drafted document at s3://opal-data-harvest/drafting/v1/2317_TT_Equity.json: NoSuchKey: ...' (generic S3 message), drafting_status ABSENT. BUILD: build-and-upload-scoped-amgt.sh, uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip, local sha256 Jicv6u3NnACRmmtJbwWRtHLKXNd6WbRYePR3hUino90=, VersionId Dr.wKlgx7zNmVcXpue7AQW0V0LU5IuCQ. Targeted plan: 0 to add, 1 to change, 0 to destroy, naming ONLY module.scoped_amgt_api.aws_lambda_function.this. APPLY (HALT_ACK=1, safe-apply.sh -target): Apply complete! Resources: 0 added, 1 changed, 0 destroyed. POST-ACT live config: CodeSha256 Jicv6u3NnACRmmtJbwWRtHLKXNd6WbRYePR3hUino90= (matches uploaded artifact exactly), LastModified 2026-09-18T00:12:01Z, CodeSize 783851, layer/memory/timeout/env unchanged. Post-deploy census: 13 of 13 GET routes -> 200, LOST=[] GAINED=[]. AC1 AFTER (same sampled name, same live call): drafting_reason="filing_identity.source is 'none': no cik and expected form to fetch by" -- the filings store's own classed no-CIK reason, drafting_status ABSENT unchanged. Matches AC1's <expect> exactly: PASS. Targeted 0-diff replan: No changes. Your infrastructure matches the configuration. Verified no-premature-inclusion before build: SCORES_PREFIX/read_scores/bundle[as_of_date]/bundle[scores] all absent from the built artifact (rk-25/rk-30 not yet due). | CLOSED 20260918T001702Z |

## Log

- 20260918T000146Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260918T001702Z LEG opal-amgt-scoped-api closed: PRE-ACT live get_function_configuration: CodeSha256 iGmDkRbA6ZenF0CHAgU7nwNZkmdUEzMKRdBEJsDlbP0= (this act's own predece
- 20260918T001702Z CLOSED -- all 1 legs proven
