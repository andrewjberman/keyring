# Deploy Completion Record
**Date opened:** 2026-10-08T21:16:03.644727+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T235151Z
**Deploy:** AMGT_HARVST served gold rebuild #10, act 2 on the FROZEN list (R28, msg 31945): the capitalised-headline rule served, list = rebuild #9's 242 (round72/securities.universe.r72.json); pair COO 9d0a2abf9c + gate amend baf0db7af6, CTO fee6ba8438; dry run 3 HOLDS 19:33Z
**Authored by:** 2.0.0_SA_COO~H
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | GATE: gold_rebuild10.signing.py run by the act on the frozen list, no write | RULE (rebuild #10): HOLDS and PUTS SENT 0 | act 3 (relaunched 22:08:24Z in-session after act 2 pid 31672 was killed in its gate at 21:48:25Z by kill-maint ORPHAN, nothing written): GATE printed RULE (rebuild #10): HOLDS, PUTS SENT: 0; mention 48,358 -> 52,282, gone 3 all named, lost 0, unexplained 0; daily 68,002 -> 68,002, other 0 (gold_rebuild10.act3.out) | CLOSED 20261008T225809Z |
| L2 | s3-prefix | amgt/harvest/gold/article_security_mention/ and chatter_daily/ date=<as_of>: one new part each | the two written keys with bytes, from the act record | act 3 record org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round72/gold_rebuild10.act_20261008T220825Z.json: s3://opal-data-harvest/amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261008T225527Z.parquet 8,290,713 bytes LastModified 23:27:01Z; s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-10-08/part-20261008T232700Z.parquet 453,573 bytes 23:33:40Z (head_object read 23:4xZ). Rollback per key: rebuild #9's parts (part-20261008T055319Z / part-20261008T061255Z) written again as the newest (COO half AMENDMENT 1) | CLOSED 20261008T235149Z |
| L3 | verify | VERIFY: the rule on what was written against the BEFORE snapshot | removed by name 3 of 3, lost 0, unexplained 0, daily gone 0 other 0 | VERIFY on the written parts (act 3 23:40:30Z, rc 0): holds true; mention 48,358 -> 52,282, gone 3 = removed by name 3 of 3, lost 0, unexplained 0; daily 68,002 -> 68,002, gone 0, other 0; result 'DONE: the rebuild-#9 rule holds on the written parts' | CLOSED 20261008T235150Z |
| L4 | verify | CTO half C2: one read of BP's feed on the served route | bbg:TLG1WZKGZAIP00 absent from BP's feed; row Z-S102 closes on this read | C2 read 23:49:23Z on the served route scoped_amgt.read_feed (the API's own read; it read part-20261008T225527Z, 52,282 rows): BP_US_Equity SERVED 16 items and BP/_LN_Equity SERVED 16 items, bbg:TLG1WZKGZAIP00 and the title 'Bond Traders Bet on Fed Delivering 25 BP Rate Increase' ABSENT from both. Control: under rebuild #9's part, HVST-bj-1's walk (0.9.0_WK_AMGT_HARVST~115/BJ1_FEED_WALK.md:40) listed it in BP's feed dated 2026-09-16, inside today's window 2026-09-09..2026-10-06. File org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round72/gold_rebuild10.c2_bp_feed_read.out | CLOSED 20261008T235150Z |

## Log

- 20261008T211603Z OPENED by 2.0.0_SA_COO~H with 4 leg(s)
- 20261008T225809Z LEG L1 closed: act 3 (relaunched 22:08:24Z in-session after act 2 pid 31672 was killed in its gate at 21:48:25Z by kill-maint ORPHAN, n
- 20261008T235149Z LEG L2 closed: act 3 record org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round72/gold_rebuild10.act_20261008T220825Z.js
- 20261008T235150Z LEG L3 closed: VERIFY on the written parts (act 3 23:40:30Z, rc 0): holds true; mention 48,358 -> 52,282, gone 3 = removed by name 3 of
- 20261008T235150Z LEG L4 closed: C2 read 23:49:23Z on the served route scoped_amgt.read_feed (the API's own read; it read part-20261008T225527Z, 52,282 r
- 20261008T235151Z CLOSED -- all 4 legs proven
