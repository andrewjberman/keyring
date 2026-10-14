# Deploy Completion Record
**Date opened:** 2026-10-13T08:37:06.148155+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T012602Z
**Deploy:** ADVI_FIRMBKTS TO-FB-j-3 (round 7): deploy the text-only dispatcher code/gold/gold_dispatch.sh (FB-j-2 @8b86cdeb0e: the emit WARN carries rc and 300 chars of CLI text, one-line set -e-safe form) to s3://opal-data-bd; prior VersionId JTxOlFbqGVj9SOajf2YKlMVo.E3Sv35K ETag f568d11bbf074aaec8f06a01ee13dd2e; rollback = copy the prior VersionId back; consumers: bd-gold-layer-runner (syncs code/gold/ at chain start and self-fetches the dispatcher) and bd-gold-qa-runner (shares the key); then read the 23:00Z chain's WARN
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions: 8b86cdeb0e in HEAD, repo file sha256 and CR/non-ASCII counts, diff deployed to repo, bash -n, the set -e harness on the merged function (failure arm and success arm) | the sha256, the hunks and the two harness outputs | 8b86cdeb0e in HEAD (3c7e37846d); repo file sha256 7acefe6dcf6dcb05c25b709db047ca5fb5c184539621b22ccd0b844c31f7b167, 76046 bytes, 0 CR, 0 bytes above 127; bash -n clean; diff deployed to repo 2 hunks 7 lines all inside emit_chain_complete; set -e harness on the merged function: failure arm prints WARN rc=255 with the region text and REACHES the next statement (exit 0), success arm prints emitted and reaches it (exit 0) | CLOSED 20261013T083806Z |
| L2 | s3-prefix | aws s3 cp the repo file to s3://opal-data-bd/code/gold/gold_dispatch.sh --sse AES256; read back by get-object: sha256 equals the repo file; new VersionId and prior VersionId recorded | equal sha256 and both VersionIds | aws s3 cp --sse AES256 at 2026-10-13T08:37:32Z; new VersionId l53CmF0sCt.tgKYlr.JPiAl0_tqH._yB ETag c5e6e57b7a3d6c765c80d376c530578d size 76046; read back by get-object sha256 7acefe6dcf6d... equals the repo file; prior VersionId JTxOlFbqGVj9SOajf2YKlMVo.E3Sv35K (rollback: copy it back) | CLOSED 20261013T083806Z |
| L3 | verify | the first chain that closes after the deploy (fallback 23:00Z or an S3-triggered run): the WARN's rc and text verbatim, classified | the verbatim text and the class, or NOT_OBSERVED with the reason | chain:full started 2026-10-13T23:00:43Z (runner launch 23:00:11Z by bd-daily-trigger-lambda-role = the nightly fallback), closed 2026-10-14T01:20:24Z COMPLETE exit 0; cumulative log gold_incremental_2026-10-14_20261014_012024.log carries the new-form WARN between the perf_report archive (011437Z) and the CDNCOHT invalidation (01:14:38Z): rc=255 You must specify a region. You can also configure your region by running aws configure. Class NO_REGION. The 7 older WARN lines in the same window carry no text (pre-deploy code). | CLOSED 20261014T012601Z |
| L4 | git | EMIT_ERROR_TEXT.json committed first, then instance, rows and the status flip | commit hash | EMIT_ERROR_TEXT.json and the j3_chain evidence committed first; instance, row and the status flip in the next commit (hashes in the report) | CLOSED 20261014T012602Z |

## Log

- 20261013T083706Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261013T083806Z LEG L1 closed: 8b86cdeb0e in HEAD (3c7e37846d); repo file sha256 7acefe6dcf6dcb05c25b709db047ca5fb5c184539621b22ccd0b844c31f7b167, 7604
- 20261013T083806Z LEG L2 closed: aws s3 cp --sse AES256 at 2026-10-13T08:37:32Z; new VersionId l53CmF0sCt.tgKYlr.JPiAl0_tqH._yB ETag c5e6e57b7a3d6c765c80
- 20261014T012601Z LEG L3 closed: chain:full started 2026-10-13T23:00:43Z (runner launch 23:00:11Z by bd-daily-trigger-lambda-role = the nightly fallback)
- 20261014T012602Z LEG L4 closed: EMIT_ERROR_TEXT.json and the j3_chain evidence committed first; instance, row and the status flip in the next commit (ha
- 20261014T012602Z CLOSED -- all 4 legs proven
