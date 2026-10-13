# Deploy Completion Record
**Date opened:** 2026-10-13T13:37:00.463405+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-f-1 (ADHOC.canon-r6-fold-deploy, WORLD): four named gold scripts to opal-data-mdpf code/scripts/gold/, the mdpf-gold-lambda package at pin 51cfc93ea8 with MDPF_GOLD_COMMIT set to the full built SHA in the same apply, one qa_local dry run, the emitter package untouched (control read). Keys: code/scripts/gold/mdpf_gold_consolidator.py, dim_mdpf_account_distribution.py, dim_mdpf_aum_metrics.py, mdpf_revamp_model_crosswalk.py. Lambda: mdpf-gold-lambda. Source edit: infra/aws/terraform/mdpf-pipeline/gold-lambda.tf MDPF_GOLD_COMMIT value and its comment only (prior value 88e974ca10237b6555bcda633ca83a54e4a5dcc9). Consumers of the global served objects s3://opal-data-assets/portal/gold/mdpf/global/*: the portal MDPF views (catalog entries portal_mdpf_*), the opal-assets-mdpf-portal-publisher lambda, and the gold lambda's own category-views phase; enumeration is not exhaustive. GO: 2.0.0_SA_COO~D1 msg 4846 (W8-S4 read @0c2611c918).
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before print: whole-tree equality, prior ETag and VersionId of the four keys, function CodeSha256/LastModified/environment, deployed BUILD_MANIFEST commit, Scheduler input verbatim, 16 served objects with ETag VersionId sha256, control key and tax-prelude store VersionIds, emitter CodeSha256 | all recorded and printed |  | OPEN |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/mdpf_gold_consolidator.py (D1 named file) | mdpf-code-equality --files exit 0 named_not_equal 0 |  | OPEN |
| L3 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_account_distribution.py (D1 named file) | NAMED EQUAL |  | OPEN |
| L4 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aum_metrics.py (D1 named file) | NAMED EQUAL |  | OPEN |
| L5 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/mdpf_revamp_model_crosswalk.py (D1 named file) | NAMED EQUAL |  | OPEN |
| L6 | tf-lambda | aws_lambda_function.mdpf_gold (D2: build_package.py --pin 51cfc93ea8, upload, gold-lambda.tf MDPF_GOLD_COMMIT, one targeted safe-apply) | plan moves only code and MDPF_GOLD_COMMIT; four sha256 equal the pin; env equals the full pin SHA equals the manifest source_vintage.commit |  | OPEN |
| L7 | activation | the one qa_local dry run of mdpf-gold-lambda (schedule input plus qa_local true), after the day's fire manifest | 200, green, errors empty, 16 of 16, 16 baseline objects byte-equal, stores and control key same VersionId, emitter CodeSha256 unchanged |  | OPEN |
| L8 | verify | after print, changed-name report (nothing deployed from it), emitter control read after the last act | four D1 names EQUAL; emitter unchanged |  | OPEN |

## Log

- 20261013T133700Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 8 leg(s)
