# Deploy Completion Record
**Date opened:** 2026-09-18T00:31:14.663824+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T004339Z
**Deploy:** AMGT-rk-25: thesis bundle re-exposes drafting_provenance.filing_date as as_of_date. Lambda deploy 3 of 4, batch B. Co-signed CTO 533f216c74 / COO 6b7d4f2341, HALF 4.
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | PRE-ACT live config: CodeSha256 Jicv6u3NnACRmmtJbwWRtHLKXNd6WbRYePR3hUino90= (rk-24's live deploy), LastModified 2026-09-18T00:12:01Z, CodeSize 783851, layer/memory/timeout/env unchanged. Pre-deploy census: 13 of 13 GET routes -> 200. BEFORE: BA_US_Equity as_of_date=None, HOLLOW_NONEXISTENT_KEY_Equity as_of_date=None (both absent, pre-fix). BUILD: build-and-upload-scoped-amgt.sh, uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip, local sha256 fkKLVfsAsgXk0Swo/XMAjf+OncnOe0ApEogC0WPYmeU=, VersionId vpRwtAevDHAJ6LkBLpIZ_TGssTY8XU4k. Targeted plan: 0 to add, 1 to change, 0 to destroy, naming ONLY module.scoped_amgt_api.aws_lambda_function.this. APPLY (HALT_ACK=1, safe-apply.sh -target): Apply complete! Resources: 0 added, 1 changed, 0 destroyed. POST-ACT live config: CodeSha256 fkKLVfsAsgXk0Swo/XMAjf+OncnOe0ApEogC0WPYmeU= (matches uploaded artifact exactly), LastModified 2026-09-18T00:40:12Z, CodeSize 784068, layer/memory/timeout/env unchanged. Post-deploy census: 13 of 13 GET routes -> 200, LOST=[] GAINED=[]. AC1 AFTER: BA_US_Equity as_of_date=2026-01-30, equals drafting_provenance.filing_date exactly -- PASS. AC2 AFTER: HOLLOW_NONEXISTENT_KEY_Equity (planted negative control) as_of_date=None, never fabricated -- PASS. Targeted 0-diff replan: No changes. Your infrastructure matches the configuration. Verified no-premature-inclusion before build: SCORES_PREFIX/read_scores/bundle[scores] all absent (rk-30 not yet due). | CLOSED 20260918T004339Z |

## Log

- 20260918T003114Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260918T004339Z LEG opal-amgt-scoped-api closed: PRE-ACT live config: CodeSha256 Jicv6u3NnACRmmtJbwWRtHLKXNd6WbRYePR3hUino90= (rk-24's live deploy), LastModified 2026-09
- 20260918T004339Z CLOSED -- all 1 legs proven
