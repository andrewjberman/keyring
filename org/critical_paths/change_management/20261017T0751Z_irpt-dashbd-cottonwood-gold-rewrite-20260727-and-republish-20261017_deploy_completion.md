# Deploy Completion Record
**Date opened:** 2026-10-17T07:51:49.783173+00:00
**Status:** CLOSED -- UNEXECUTED -- stopped at step 3 (the 2026-07-27 gold day reads 3 rows, outside the band; issuer msg 10403); 0 writes, 2 read-only dry events; closed 20261017T081143Z
**Deploy:** IRPT_DASHBD TO-DB-b-329 (round 150, GOLD0727): ONE Cottonwood gold day (2026-07-27) rewritten through the function's own rewrite event (a new version; the 3-row version kept), a dry run first, the pre-write diff with hard STOP lines, a dry build, ONE canary, then the republish of the Cottonwood series (new versions at the same keys). Gate 0(b): no open leg on the Cottonwood account-return-daily or reporting-publish function, the gold prefix or the published prefix at the worktree census.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before reads: the gold day, the full day, the gold totals, the 939 series prefixes with object and version counts, code hashes and schedules | before block | before reads taken and equal to the packet's section 2 (day 3 rows / 2 versions, full day 879 rows, 939 prefixes, gold 3391 objects) | CLOSED 20261017T081141Z |
| L2 | verify | the dry run of the rewrite event writes nothing (gold object and version counts equal before and after) | dry block | dry run read-only twice (the first run's row count was not kept; both wrote nothing, objects 3391/versions 3457 equal): the day reads 3 rows, outside the band 840-920: STOP | CLOSED 20261017T081141Z |
| L3 | s3-prefix | the ONE gold-day rewrite (a new version; the 3-row version kept; no other partition moves) | rewrite block | NOT EXECUTED: the order stopped at step 3 (issuer msg 10403: the function reads fact_allocations, whose 2026-07-27 partition holds 3 rows; the gold day cannot be rebuilt until the carrier re-lands that table); 0 writes | CLOSED 20261017T081141Z |
| L4 | verify | the pre-write diff inside its STOP lines (only the next day's three fields may change; nothing removed; refused 0) | prewrite block | NOT EXECUTED (closed unexecuted per msg 10403) | CLOSED 20261017T081141Z |
| L5 | s3-prefix | ONE canary republish compared in memory with the previous version | canary block | NOT EXECUTED (closed unexecuted per msg 10403) | CLOSED 20261017T081142Z |
| L6 | s3-prefix | the full republish: 939 published, refused exactly 40, same objects, new versions | publish_full block | NOT EXECUTED (closed unexecuted per msg 10403); no republish, no rollback needed | CLOSED 20261017T081142Z |
| L7 | verify | the after-read and the receipt | record and criteria | one-line record COT_GOLD_REWRITE_UNEXECUTED.txt written and committed | CLOSED 20261017T081142Z |

## Log

- 20261017T075149Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261017T081141Z LEG L1 closed: before reads taken and equal to the packet's section 2 (day 3 rows / 2 versions, full day 879 rows, 939 prefixes, gold 3
- 20261017T081141Z LEG L2 closed: dry run read-only twice (the first run's row count was not kept; both wrote nothing, objects 3391/versions 3457 equal): 
- 20261017T081141Z LEG L3 closed: NOT EXECUTED: the order stopped at step 3 (issuer msg 10403: the function reads fact_allocations, whose 2026-07-27 parti
- 20261017T081141Z LEG L4 closed: NOT EXECUTED (closed unexecuted per msg 10403)
- 20261017T081142Z LEG L5 closed: NOT EXECUTED (closed unexecuted per msg 10403)
- 20261017T081142Z LEG L6 closed: NOT EXECUTED (closed unexecuted per msg 10403); no republish, no rollback needed
- 20261017T081142Z LEG L7 closed: one-line record COT_GOLD_REWRITE_UNEXECUTED.txt written and committed
- 20261017T081143Z CLOSED -- all 7 legs proven
