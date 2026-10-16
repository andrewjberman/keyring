# Deploy Completion Record
**Date opened:** 2026-10-16T13:41:20.691914+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-300: APPLY the signed 49 Financial reporting-gold pair (packet sha256 d2c27ac2bdc5, COO half @c17e5d10b9, CTO half @89ca7c661c); APPLIER 0.7.0_AE_CloudOps~DB2: build and upload a NEW VERSION of the irpt-49f-reporting-gold-lambda bundle, plan EXACTLY 0 add / 2 change / 0 destroy (the ONE s3:prefix value irpt/49financial/gold/filled_report_values/* added on ListExactlyTheSixGoldPrefixes, and the function by CODE attributes only), ONE safe-apply outside 11:35Z to 12:00Z, the hop-1 FIRST WRITE of 2026-10-15, a ONE-DAY backfill of 2026-10-15, the flip count, then the republish of the series (only after the publish pair ledger is CLOSED); both schedules untouched; NO delete; ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each pinned file; packet blob, sha256 and both halves; marker scan over every live worktree; live reads equal to the packet section 3 | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip equal to the packet build line, import smoke rc 0, then a NEW VERSION of the artifact key; built equals landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | tf-lambda | fmt -check, init, validate, saved plan EXACTLY 0 add / 2 change / 0 destroy on the policy and the function, the policy change the one list value, naming gate 0 REFUSE, ONE safe-apply, replan No changes, read-backs, stamp | plan line, apply line, replan line, read-backs |  | OPEN |
| L4 | verify | Act 3 hop-1 FIRST WRITE: ONE synchronous event day 2026-10-15; one filled partition; memory at most 6553 MB, duration at most 720000 ms | the event result and the LIST of the filled prefix |  | OPEN |
| L5 | verify | Act 4 ONE-DAY backfill 2026-10-15 and the flip count; rows equal, claim on every row, PARTIAL on exactly the floor-start accounts, value columns identical, the four other tables unchanged; no non-floor flip | the before and after reads and the flip counts |  | OPEN |
| L6 | verify | Act 5 the republish of the series on irpt-49f-reporting-publish-lambda (only after the publish pair ledger is CLOSED) and the receipt; pair_count, partial_with_pair and no_claim_count as expected | the shard REPORT lines, the LIST counts, the counts |  | OPEN |

## Log

- 20261016T134120Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)
