# Deploy Completion Record
**Date opened:** 2026-09-16T16:06:56.126058+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260916T162203Z
**Deploy:** ROLLBACK of AMGT-rk-2's opal-amgt-scoped-api redeploy (15:19:34Z, regressed GET /overlay and /thesis 200->500) to the co-signed pre-act state; the 15:19Z act itself ran with NO ledger entry (rk-2's grant never named this directory -- issuer defect)
**Authored by:** 2.0.0_SA_COO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-rollback GET route census of opal-amgt-scoped-api (8 GET of 11 routes) | census JSON: 5 of 8 GET answering 200, CodeSha256 Di6/6ju9 | 16:07:51Z census (census.py GET-only over scoped_amgt_route_table(), 11 routes, 8 GET): 5 of 8 GET 200; /overlay 500, /thesis 500, /print 500; CodeSha256 Di6/6ju9ReLmabolbWs/kni6BZsFsbqXfTLvMxuC8UI= CodeSize 749036 LastModified 15:19:34Z | CLOSED 20260916T162202Z |
| L2 | activation | s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip latest <- version 5M.rKCFSTdIVAzuXRDpeyoropkYR1Wts | new latest VersionId with bytes sha256 and content-sha256 metadata == 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk= | copy_object of VersionId 5M.rKCFSTdIVAzuXRDpeyoropkYR1Wts (source bytes sha256 verified 9ubWPnhz... before copy) -> new latest VersionId UZh83hiETFezzNhKe5Jeo54S8SeisAKw, 747396 B, metadata content-sha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=, bytes sha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk= | CLOSED 20260916T162203Z |
| L3 | activation | aws_iam_role_policy.scoped_amgt_api_grants both limbs back to the nine co-signed prefixes | get_role_policy read: GetObject ARNs and ListBucket s3:prefix each exactly the nine | iam get_role_policy opal-amgt-scoped-api-role / opal-amgt-scoped-api-grants after apply: LIMB 1 GetObject prefixes 9, equal to the co-signed nine, model_block absent; LIMB 2 ListBucket s3:prefix 9, equal to the nine, model_block absent | CLOSED 20260916T162203Z |
| L4 | verify | post-rollback GET route census + Lambda CodeSha256 read-back | CodeSha256 == 9ubWPnhz and GET-200 set restored (overlay and thesis 200) | 16:19:54Z census: 7 of 8 GET 200 (restored /overlay 24929 B and /thesis 70499 B; lost none; /print 500 pre-existing G3); CodeSha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk= CodeSize 747396 LastModified 16:18:57Z; env keys HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE | CLOSED 20260916T162203Z |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply (HALT_ACK=1 after 0 STOP-class lines in 550) from worktree C:/tmp/coo-amgt-rk2-rollback of saved targeted plan: Apply complete 0 added, 2 changed, 0 destroyed; targeted replan No changes. Your infrastructure matches ; deployed CodeSha256 9ubWPnhz... == uploaded artifact sha; verify-on-served = L4 census | CLOSED 20260916T162203Z |

## Log

- 20260916T160656Z OPENED by 2.0.0_SA_COO~Z with 5 leg(s)
- 20260916T162202Z LEG L1 closed: 16:07:51Z census (census.py GET-only over scoped_amgt_route_table(), 11 routes, 8 GET): 5 of 8 GET 200; /overlay 500, /t
- 20260916T162203Z LEG L2 closed: copy_object of VersionId 5M.rKCFSTdIVAzuXRDpeyoropkYR1Wts (source bytes sha256 verified 9ubWPnhz... before copy) -> new 
- 20260916T162203Z LEG L3 closed: iam get_role_policy opal-amgt-scoped-api-role / opal-amgt-scoped-api-grants after apply: LIMB 1 GetObject prefixes 9, eq
- 20260916T162203Z LEG L4 closed: 16:19:54Z census: 7 of 8 GET 200 (restored /overlay 24929 B and /thesis 70499 B; lost none; /print 500 pre-existing G3);
- 20260916T162203Z LEG opal-amgt-scoped-api closed: safe-apply (HALT_ACK=1 after 0 STOP-class lines in 550) from worktree C:/tmp/coo-amgt-rk2-rollback of saved targeted pla
- 20260916T162203Z CLOSED -- all 5 legs proven
