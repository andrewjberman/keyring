# Deploy Completion Record
**Date opened:** 2026-10-14T12:06:57.424256+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261014T123111Z
**Deploy:** IRPT_ANLREQ TO-DELETE-C449: delete every version of ONE synthetic stored input (case D2, tenant 49financial) in the intake store under Andrew's approval of open call dell2-20261014T044915Z-c449; the key is selected by the full 64-hex input id, exactly one key required, each version deleted by VersionId, NoSuchKey read back; the D3 input and every other object stay
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L | verify | list-object-versions on irpt/49financial/state/normalized_portfolios/ in opal-data-irpt; keys containing the full 64-hex id; exactly 1 key; versions and delete markers counted | key count 1 and version count printed | list-object-versions opal-data-irpt prefix irpt/49financial/state/normalized_portfolios/ read whole (not truncated): 11 versions, 0 delete markers, 11 distinct keys; keys containing the full 64-hex of the D2 input id: exactly 1; that key has 1 version (LastModified 2026-10-14T04:23:53Z, 4586 B, IsLatest, not a delete marker), inside the D2 sitting window; the other 10 keys untouched. Open-deploy markers: 47 worktrees listed, 47 read, 807 marker rows, 148 distinct blobs, 0 naming the intake store (opal-data-irpt, normalized_portfolios, c449). Selection note: the key address carries the id's 64-hex (the content sha256 leaf), not the portfolio_ prefix. | CLOSED 20261014T120748Z |
| D | s3-prefix | delete each version and delete marker of the one key by VersionId, one call per version | each call result printed, deleted equals versions before |  | OPEN |
| R | verify | head-object without VersionId answers 404; list-object-versions for the exact key returns 0 versions and 0 delete markers within a bounded 5 minute window | HEAD NoSuchKey and VERSIONS_AFTER 0 |  | OPEN |

## Log

- 20261014T120657Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261014T120748Z LEG L closed: list-object-versions opal-data-irpt prefix irpt/49financial/state/normalized_portfolios/ read whole (not truncated): 11 
- 20261014T123111Z CLOSED -- REFUSED BY GATE before apply, world untouched: REFUSAL (s3api delete-object by VersionId on the one selected key in opal-data-irpt, 2026-10-14 ~12:08Z): AccessDenied, user cloudops-dell2-agent-user is not authorized to perform s3:DeleteObjectVersion with an explicit deny in an identity-based policy cloudops-dell-agent-deploy-policy (statement DenyS3DeletesOnProductionData, s3:DeleteObject* on opal-data-*, no Condition; policy v7 read live). NO
