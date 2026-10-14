# Deploy Completion Record
**Date opened:** 2026-10-14T16:06:25.671769+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-h-1 + CN-l-1 (ADHOC.canon-r7-gold-deploy, WORLD): ONE named gold script to opal-data-mdpf code/scripts/gold/ (key code/scripts/gold/dim_mdpf_aum_metrics.py), the mdpf-gold-lambda package at pin 9592daf75c with MDPF_GOLD_COMMIT set to the full built SHA in the same apply (infra/aws/terraform/mdpf-pipeline/gold-lambda.tf value and its comment only; prior value 51cfc93ea84ac56ee6d14327125bfc53fc53c930), one qa_local dry run; the aggregate library is NOT copied to code/ and the emitter package is untouched (control read). Consumers of the global served objects s3://opal-data-assets/portal/gold/mdpf/global/*: the portal MDPF views (catalog entries portal_mdpf_*), the opal-assets-mdpf-portal-publisher lambda, and the gold lambda's own category-views phase; enumeration is not exhaustive. GO: 2.0.0_SA_COO~D1 msg 5644 (issuance commit 7d075c6ef6; pair COO half abe47dcaaa, CTO half 8d6f9cdba3).
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 2a-2g re-measured, /opt/mdpf layout read, before print (whole-tree equality, prior ETag and VersionId of the D1 key, function CodeSha256/LastModified/environment, deployed BUILD_MANIFEST commit, Scheduler input, 16 served objects, A4 newest keys, control key and tax-prelude store VersionIds, emitter CodeSha256) | all recorded and printed |  | OPEN |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aum_metrics.py (D1 named file) | mdpf-code-equality --files exit 0 named_not_equal 0 |  | OPEN |
| L3 | activation | aws_lambda_function.mdpf_gold (D2: build_package.py --pin 9592daf75c, upload, gold-lambda.tf MDPF_GOLD_COMMIT, one targeted safe-apply) | plan moves only code and MDPF_GOLD_COMMIT; changed-module sha256 equal the pin; registry file in the zip; env equals the full pin SHA equals the manifest source_vintage.commit |  | OPEN |
| L4 | activation | the one qa_local dry run of mdpf-gold-lambda (schedule input plus qa_local true), after D2 | 200, green, errors empty, 16 of 16, 16 baseline objects byte-equal, stores and control key same VersionId, emitter CodeSha256 unchanged |  | OPEN |
| L5 | verify | after print, changed-name report (nothing deployed from it), emitter control read after the last act | the one D1 name EQUAL; aggregate library DIFFER stated as known; emitter unchanged |  | OPEN |

## Log

- 20261014T160625Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 5 leg(s)
