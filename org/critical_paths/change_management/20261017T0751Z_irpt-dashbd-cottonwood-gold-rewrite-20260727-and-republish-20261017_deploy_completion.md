# Deploy Completion Record
**Date opened:** 2026-10-17T07:51:49.783173+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-329 (round 150, GOLD0727): ONE Cottonwood gold day (2026-07-27) rewritten through the function's own rewrite event (a new version; the 3-row version kept), a dry run first, the pre-write diff with hard STOP lines, a dry build, ONE canary, then the republish of the Cottonwood series (new versions at the same keys). Gate 0(b): no open leg on the Cottonwood account-return-daily or reporting-publish function, the gold prefix or the published prefix at the worktree census.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before reads: the gold day, the full day, the gold totals, the 939 series prefixes with object and version counts, code hashes and schedules | before block |  | OPEN |
| L2 | verify | the dry run of the rewrite event writes nothing (gold object and version counts equal before and after) | dry block |  | OPEN |
| L3 | s3-prefix | the ONE gold-day rewrite (a new version; the 3-row version kept; no other partition moves) | rewrite block |  | OPEN |
| L4 | verify | the pre-write diff inside its STOP lines (only the next day's three fields may change; nothing removed; refused 0) | prewrite block |  | OPEN |
| L5 | s3-prefix | ONE canary republish compared in memory with the previous version | canary block |  | OPEN |
| L6 | s3-prefix | the full republish: 939 published, refused exactly 40, same objects, new versions | publish_full block |  | OPEN |
| L7 | verify | the after-read and the receipt | record and criteria |  | OPEN |

## Log

- 20261017T075149Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
