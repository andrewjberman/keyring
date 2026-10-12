# Deploy Completion Record
**Date opened:** 2026-10-12T06:09:33.450349+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-CT-x-1 AMENDMENT 3 (WORLD): idempotent re-put of s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py, identical bytes, under named commit d5cd8a81c45fee2f154d8541f2002495a836d1ed, then deploy_readback_check.py; no content change to any deployed object
**Authored by:** 0.7.0_AE_CloudOps~CT1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | repo blob at HEAD 1b1f7c76a5 versus the live S3 object, sha256 both printed, previous VersionId recorded | equal sha256 and length, both digests and the VersionIds |  | OPEN |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py re-put with the same bytes (s3api put-object) | post-put object sha256 equals the repo blob; head-object fields; new VersionId |  | OPEN |
| L3 | git | the named commit d5cd8a81c4 published on the scratch ref origin/dell1/readback-20261012T0608Z only | ls-remote read of the ref; box/dell1 and CLOUD do not contain it |  | OPEN |
| L4 | verify | named_commit recorded in this entry by named_commit_check.py --record | the NAMED-COMMIT-LEDGER line |  | OPEN |
| L5 | verify | deploy_readback_check.py read-back on the named commit | the DEPLOY-READBACK last line with on_trunk=False objects_equal=1/1 |  | OPEN |

## Log

- 20261012T060933Z OPENED by 0.7.0_AE_CloudOps~CT1 with 5 leg(s)
