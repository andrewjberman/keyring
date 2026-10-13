# Deploy Completion Record
**Date opened:** 2026-10-13T08:37:06.148155+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-j-3 (round 7): deploy the text-only dispatcher code/gold/gold_dispatch.sh (FB-j-2 @8b86cdeb0e: the emit WARN carries rc and 300 chars of CLI text, one-line set -e-safe form) to s3://opal-data-bd; prior VersionId JTxOlFbqGVj9SOajf2YKlMVo.E3Sv35K ETag f568d11bbf074aaec8f06a01ee13dd2e; rollback = copy the prior VersionId back; consumers: bd-gold-layer-runner (syncs code/gold/ at chain start and self-fetches the dispatcher) and bd-gold-qa-runner (shares the key); then read the 23:00Z chain's WARN
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions: 8b86cdeb0e in HEAD, repo file sha256 and CR/non-ASCII counts, diff deployed to repo, bash -n, the set -e harness on the merged function (failure arm and success arm) | the sha256, the hunks and the two harness outputs |  | OPEN |
| L2 | s3-prefix | aws s3 cp the repo file to s3://opal-data-bd/code/gold/gold_dispatch.sh --sse AES256; read back by get-object: sha256 equals the repo file; new VersionId and prior VersionId recorded | equal sha256 and both VersionIds |  | OPEN |
| L3 | verify | the first chain that closes after the deploy (fallback 23:00Z or an S3-triggered run): the WARN's rc and text verbatim, classified | the verbatim text and the class, or NOT_OBSERVED with the reason |  | OPEN |
| L4 | git | EMIT_ERROR_TEXT.json committed first, then instance, rows and the status flip | commit hash |  | OPEN |

## Log

- 20261013T083706Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
