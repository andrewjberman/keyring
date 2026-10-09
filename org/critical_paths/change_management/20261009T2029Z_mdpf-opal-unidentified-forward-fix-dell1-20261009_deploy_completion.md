# Deploy Completion Record
**Date opened:** 2026-10-09T20:29:03.205895+00:00
**Status:** OPEN
**Deploy:** Forward fix for the opal_unidentified.py packaging gap (row MDPF_CANON-D1-S3 / MDPF_STRATID-D1-S7): F1 runner first-mint, F2 the gold package row, rebuild, re-upload, re-apply, green qa_local read
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | s3-prefix | opal-data-mdpf code/scripts/silver/opal_unidentified.py -- first mint of data/assets/scripts/silver/opal_unidentified.py (blob af78ac7bd6eacb3069200140be1ab2046c927627, sha256 6b9c1d7fff26dc9f7ce150426ce90ed3281dc8a1ba8511c765c23b97241304d7), authorized by 2.0.0_SA_COO~S1 msgs 3132 and 3137 under MDPF_STRATID.TO-APPLY-R2 forward-fix amendment @213fb7215c | read the served object back: ContentLength and sha256 equal to the pinned blob, and the prior 404 named as the control |  | OPEN |
| F2-BUILD | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-gold-lambda.zip -- the package rebuilt after the one build_package.py row (ADHOC.canon-r1-gold-redeploy-backfill AMENDMENT 2 @1dd9a375cb), carrying opal_unidentified.py as a zip member | the zip lists opal_unidentified.py and its member bytes equal the pinned blob; the served object reads back equal to the local build |  | OPEN |
| F2-VERIFY | verify | the gold Lambda's qa_local read of the rebuilt bytes | 16 of 16 A4 objects, errors [] -- the arms the 20:14:51Z run failed; plus zero writes measured as a pre/post set difference with the denominator printed |  | OPEN |
| mdpf-gold-lambda | tf-lambda | aws_lambda_function.mdpf_gold | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T202903Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 4 leg(s)
