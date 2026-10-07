# Deploy Completion Record
**Date opened:** 2026-10-07T16:49:27.700165+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-65 (C-CASH-TOKEN, PRD v0.16): the cash-token _shared module released from the LAPTOP to its TWO firm copies, in the same window as 0.0.0_AB_MSTR's merge of q/dell1/secclass-r11-held-e65 (candidate 16092a4806, md5 3f1e6be8910952f33c88bf100c610ab6). TREE DEVIATION, STATED: the merge IS on origin (16092a4806 is an ancestor of origin/CLOUD efc2e63467, whose tip is 'merge(0.0.0_AB_MSTR): laptop CLOUD commits into the trunk') but the SHARED laptop CLOUD is 459 commits behind and does not carry it, and the shared-tree sync is 0.0.0_AB_MSTR's act, not this seat's. So steps 1, 2 and 4 all run from a scratch worktree detached at origin/CLOUD efc2e63467 -- the same technique TO-DEPLOY-e42 directed for the same reason. STEP 1 at that worktree: the file on disk reads 3f1e6be8910952f33c88bf100c610ab6. STEP 2 at that worktree: 8 of 8 keys read, ZERO STOPs -- both moving keys live at base cfe898d1 with the order's exact rollback VersionIds, both carriers MATCH (bd a7820a20, cot cb10e3cd) and all four unchanged members MATCH (3a033c04 and 4cc11d3e in both buckets), so the 459-commit difference touches none of the eight keys. TWO MOVING KEYS: opal-data-bd code/gold/lib/_shared/etf_classification_scheduled.py, rollback VersionId P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg; and opal-data-cot same key, rollback VersionId 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1. Both read ETag cfe898d1b8677c0765a7f5ee8026761c (31,082 B) before the act. ROLLBACK per key: aws s3api copy-object --copy-source <bucket>/<key>?versionId=<that id> back over the key; and for any cash_token row an E_18 run wrote in between, delete that row by its key from the run log (input=cash_token). Halves: COO @00e7bf2cb5 SIGNED, CTO af8fa774f3 SIGNED-with-the-act-corrected (merge PLUS an explicit safe-deploy, because the push gate ships _shared members only beside a gold script). Window 9h because the verify leg cannot close before the BD 23:00Z E_18 run.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 9.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-bd code/gold/lib/_shared/etf_classification_scheduled.py -- MOVES ETag cfe898d1 -> 3f1e6be8; rollback VersionId P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg | comp-pipescript deployed MATCH row + head-object ETag 3f1e6be8910952f33c88bf100c610ab6 |  | OPEN |
| L2 | s3-prefix | opal-data-cot code/gold/lib/_shared/etf_classification_scheduled.py -- MOVES ETag cfe898d1 -> 3f1e6be8; rollback VersionId 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1 | comp-pipescript deployed MATCH row + head-object ETag 3f1e6be8910952f33c88bf100c610ab6 |  | OPEN |
| L3 | verify | the SIX byte-identical re-uploads the one safe-deploy run also makes (the two carriers E_18.detect_new_securities.py in bd and A_00.accounts_dimension.py in cot, plus etf_classification.py and etf_classifications_dynamodb.py in BOTH buckets) -- each must come back at the SAME ETag it had before, so the act moves two keys by content and none by content outside those two | head-object ETag per key equal to the pre-act value: bd carrier a7820a205692444dadb59e526200bff6, cot carrier cb10e3cd255db2c58363b6b911aef6cc, etf_classification.py 3a033c04678f1c96d116b641545b17bb both buckets, etf_classifications_dynamodb.py 4cc11d3e74486730febb7e6b4a0ba916 both buckets |  | OPEN |
| L4 | verify | the FIRST BD E_18 run after the upload (bd-gold-nightly-fallback cron(0 23 ? * MON-SAT) UTC -> bd-gold-trigger, so 2026-10-07T23:00Z) read for its cash_token plan lines (CTO condition 3): every row written names its key; any row whose class is not cash/Cash, or whose key is not a cash token, triggers rollback of the key AND the row | the run id, its cash_token plan lines, and the per-row class check |  | OPEN |

## Log

- 20261007T164927Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
