# Deploy Completion Record
**Date opened:** 2026-10-09T14:44:28.884670+00:00
**Status:** OPEN
**Deploy:** MDPF_STRATID W2 ST-w-5/ST-w-6: rebalancer_schemas + opal_strategy_matcher (reads the S3 ETF list, fail closed) reach the runner's code/scripts/silver via the box/dell1 push
**Authored by:** 2.0.0_SA_COO~S1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | safe-merge of wk-MDPF_STRATID-w2-5 into box/dell1, then the box/dell1 push by 0.0.0_AB_MSTR~DELL1 or box-sync | ls-remote shows origin box/dell1 descending from the merge commit |  | OPEN |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/silver/ rebalancer_schemas.py and opal_strategy_matcher.py uploaded by the pre-push gate | content of each S3 object equals git show <merge>:<path> |  | OPEN |
| L3 | verify | next scheduled MDPF run after L2: the slice path reads the S3 list and serves the same figures | runner log shows no strategy-config error; served Cottonwood by_model sma members equal the prior run's member set |  | OPEN |

## Log

- 20261009T144428Z OPENED by 2.0.0_SA_COO~S1 with 3 leg(s)

## Amendment 2026-10-09 ~14:50Z (2.0.0_SA_COO~S1)

The box/dell1 push (origin a66006c2e4) carried ff8b8452f0, but the pre-push gate HELD
`data/assets/scripts/silver/rebalancer_schemas.py` ("no OPEN change-management ledger names it") because this entry named the files
without their repo path; `data/assets/scripts/silver/opal_strategy_matcher.py` was not in the gate's list. Nothing was uploaded:
S3 `code/scripts/silver/rebalancer_schemas.py` is still the 2026-10-05 object (14,493 B), and `opal_strategy_matcher.py` does not exist
there, so the runner is unchanged and consistent. Both files are already on origin/CLOUD, so a re-push would not re-evaluate them.
The deploy moves to an explicit act, `MDPF_STRATID.TO-APPLY-W2-b`: `data/assets/scripts/silver/opal_strategy_matcher.py` FIRST, then
`data/assets/scripts/silver/rebalancer_schemas.py` (the schemas import the matcher; the reverse order would break the runner's import).
