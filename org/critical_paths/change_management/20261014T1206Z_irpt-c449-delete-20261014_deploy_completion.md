# Deploy Completion Record
**Date opened:** 2026-10-14T12:06:57.424256+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-DELETE-C449: delete every version of ONE synthetic stored input (case D2, tenant 49financial) in the intake store under Andrew's approval of open call dell2-20261014T044915Z-c449; the key is selected by the full 64-hex input id, exactly one key required, each version deleted by VersionId, NoSuchKey read back; the D3 input and every other object stay
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L | verify | list-object-versions on irpt/49financial/state/normalized_portfolios/ in opal-data-irpt; keys containing the full 64-hex id; exactly 1 key; versions and delete markers counted | key count 1 and version count printed |  | OPEN |
| D | s3-prefix | delete each version and delete marker of the one key by VersionId, one call per version | each call result printed, deleted equals versions before |  | OPEN |
| R | verify | head-object without VersionId answers 404; list-object-versions for the exact key returns 0 versions and 0 delete markers within a bounded 5 minute window | HEAD NoSuchKey and VERSIONS_AFTER 0 |  | OPEN |

## Log

- 20261014T120657Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
