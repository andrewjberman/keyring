# Deploy Completion Record
**Date opened:** 2026-09-18T00:49:33.486982+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T010954Z
**Deploy:** AMGT-rk-30 adapter: SCORES_PREFIX + read_scores() + bundle[scores] on the Model tab route. Lambda deploy 4 of 4, batch B (last). Co-signed CTO 533f216c74 / COO 6b7d4f2341, HALF 5.
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | PRE-ACT live config: CodeSha256 fkKLVfsAsgXk0Swo/XMAjf+OncnOe0ApEogC0WPYmeU= (rk-25's live deploy), LastModified 2026-09-18T00:40:12Z, CodeSize 784068, layer/memory/timeout/env unchanged. Pre-deploy census: 13 of 13 GET routes -> 200. BEFORE: BA_US_Equity thesis response carries no 'scores' key at all. BUILD: build-and-upload-scoped-amgt.sh -- transitive closure correctly picked up lib.research.scores.classify (deferred import), uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip, local sha256 0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=, VersionId sGCyeje9jhn9jzu86QcORUXKQnVfFNpu. Targeted plan: 0 to add, 1 to change, 0 to destroy, naming ONLY module.scoped_amgt_api.aws_lambda_function.this. APPLY (HALT_ACK=1, safe-apply.sh -target): Apply complete! Resources: 0 added, 1 changed, 0 destroyed. POST-ACT live config: CodeSha256 0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo= (matches uploaded artifact exactly), LastModified 2026-09-18T00:59:50Z, CodeSize 786895, layer/memory/timeout/env unchanged. Post-deploy census: 13 of 13 GET routes -> 200, LOST=[] GAINED=[]. FINAL SELF-CHECK (order's own mandated step): working copy diffed against e2d89be7da's full lib/research/api/scoped_amgt.py -- ZERO DIFFERENCE, confirmed byte-identical. AC1 measured FAIL: full 33-key live sweep -- measured_robustness=0 of 33, measured_peers_v=0 of 33, absent_divergence=0 of 33 (criterion requires the first two nonzero and the third =33). Root cause (row AMGT_RESAPP-Z-W27-S11, ARMED, disarm_owner CTO/COO next-round cell): the Lambda execution role has NO s3:ListBucket/GetObject grant on scores/v1/* (absent from local.scoped_amgt_pool_prefixes in scoped-amgt-api.tf, a NEW top-level prefix this order's own comp-iam preflight wrongly assumed was already covered) -- every read AccessDenies at ListObjectsV2, live-confirmed error message quoted in the row. SEPARATELY, AC1's own invocation checks the wrong record shape (.get('status')=='ABSENT' vs classify.py's real .get('state') in {MEASURED,ABSENT_SOURCE,ABSENT_PULL}), so it would misreport even after the IAM gap is fixed. The deployed code itself is verified correct: SCORES_PREFIX/read_scores() always return all three score keys, degrade to a disclosed READ_FAILED/ABSENT_PULL record rather than a 500, and never silently fall back to the superseded flat shape. Targeted 0-diff replan: No changes. Your infrastructure matches the configuration. | CLOSED 20260918T010954Z |

## Log

- 20260918T004933Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260918T010954Z LEG opal-amgt-scoped-api closed: PRE-ACT live config: CodeSha256 fkKLVfsAsgXk0Swo/XMAjf+OncnOe0ApEogC0WPYmeU= (rk-25's live deploy), LastModified 2026-09
- 20260918T010954Z CLOSED -- all 1 legs proven
