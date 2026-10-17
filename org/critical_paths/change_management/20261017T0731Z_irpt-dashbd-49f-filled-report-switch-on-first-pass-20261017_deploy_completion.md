# Deploy Completion Record
**Date opened:** 2026-10-17T07:31:21.633859+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-328 (the 49F filled-report switch-on pair, round 150, IB-pr-551 hop 2): a new publish bundle (code only, 0/1/0), the one environment variable FILLED_REPORT_PASS (0/1/0), a dry run in seven shards, ONE canary, the mint leg and ~S2's V leg, the full pass in seven shards, the after-read. Gate 0(c): no open leg on the publish function, the reporting-publish root or the reporting prefix at the worktree census.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | function-map artifact_sha256 for irpt-49f-reporting-publish-lambda, the one lambda.tf environment line, plus this ledger sentinel and the receipt, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | the publish artifact key: a NEW VERSION built == landed == the packet hash 4SF81dqn.. (17 members); the rollback version oXM0wQg8.. kept | new VersionId |  | OPEN |
| L3 | tf-lambda | TWO safe-applies of reporting-publish, each exactly 0 add 1 change 0 destroy: the code attributes, then the one environment variable; each with a clean re-plan; the exact OFF probe between them | plan counts, replan No changes, probe_off |  | OPEN |
| L4 | verify | the dry run in seven shards writes nothing (object count equal before and after) | shard table |  | OPEN |
| L5 | s3-prefix | ONE canary written (a new object under client=<id>/filled_report.json) and ~S2's V leg graded; both synthetic rows removed and read ABSENT twice if minted | canary digest, grades |  | OPEN |
| L6 | s3-prefix | the full pass in seven shards equal to the dry run's sums; the prefix gains exactly the would-be total minus 1 | full table |  | OPEN |
| L7 | verify | the after-read and the receipt: counts, function, policy, schedules | record and criteria |  | OPEN |

## Log

- 20261017T073121Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
