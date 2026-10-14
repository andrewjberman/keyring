# Deploy Completion Record
**Date opened:** 2026-10-14T22:42:54.501604+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-p-1 (ADHOC.canon-r9-gold-trend-groups-deploy, WORLD): the mdpf-gold-lambda package rebuilt at pin 8e2dd0fb369043d5f23dca2d02dba7d51cfabd6f (the Global gold timeseries serves the Variant 1 Trend groups: client_supervised_aua, etf_strategies_aua, alt_strategies_aua, carried_dates; the Muni SMA member leaves the category tree) with MDPF_GOLD_COMMIT set to the full built SHA in the same apply (infra/aws/terraform/mdpf-pipeline/gold-lambda.tf value and its comment only; prior value 9592daf75c7469d212242cd63850c735f6f53238), the package object s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip (prior VersionId ueXrxiM.u9Fves_JXUJO037JmTm9Yj.R, ETag 2c61772b8aee3785803adbc00c7d921c), the two conditional code/ keys code/scripts/gold/mdpf_gold_consolidator.py and code/scripts/gold/mdpf_category_registry.py in s3://opal-data-mdpf/ (D1, only under leg 2g), one qa_local dry run. The aggregate library and dim_mdpf_aum_metrics.py are NOT copied; the emitter and the publisher are untouched. Consumers of the global served objects s3://opal-data-assets/portal/gold/mdpf/global/*: the portal MDPF views (catalog entries portal_mdpf_*), the opal-assets-mdpf-portal-publisher lambda, and the gold lambda's own category-views phase; enumeration is not exhaustive. GO: 2.0.0_SA_COO~D1 msg 5941 (pin named); pair COO half 54da2eb87d (authored 2e1455010e by 2.0.0_SA_COO~D1, sha256 30cb2718...), CTO half d996228e93 (conditions C1, C2). Deadline: D2 and D4 done by 2026-10-15 12:44Z.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 2a-2h re-measured (GO, pin on origin with controls, content checks at the pin, halves signed, clock/runner/lambda state, FIRMBKTS, sentinels across every live worktree, runner layout, SMArtX inputs and the IAM simulation), before print (whole-tree equality, D1 keys' prior ETag/VersionId, function, deployed manifest commit, package object, Scheduler input, 16 served objects, overwrite keys, control key, tax stores, workbook listing, emitter) | all recorded and printed |  | OPEN |
| L2 | verify | D1 disposition for the two code/ keys under leg 2g (done via safe-deploy and read back, or NOT DONE with the reason and the listing) | C2 as the order states it for whichever branch 2g selects |  | OPEN |
| L3 | activation | aws_lambda_function.mdpf_gold (D2: build_package.py --pin 8e2dd0fb36, checks of the built zip, upload, gold-lambda.tf MDPF_GOLD_COMMIT, one targeted safe-apply) | plan moves only code and MDPF_GOLD_COMMIT; changed modules equal the pin; aggregate library and aum_metrics equal 9592daf75c; env equals the full pin SHA equals the manifest source_vintage.commit |  | OPEN |
| L4 | activation | the one qa_local dry run of mdpf-gold-lambda (schedule input plus qa_local true), after D2 | 200, green, errors EMPTY (no global entry), 16 of 16, 16 baseline objects and 5 overwrite keys byte-equal, stores and control key same VersionId, emitter CodeSha256 unchanged |  | OPEN |
| L5 | verify | after print, changed-name report (nothing deployed from it), emitter control read after the last act | D1 names (if D1 ran) EQUAL; aggregate library DIFFER stated as known; emitter unchanged |  | OPEN |

## Log

- 20261014T224254Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 5 leg(s)
