# Deploy Completion Record
**Date opened:** 2026-10-08T05:17:24.583783+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T062828Z
**Deploy:** AMGT_HARVST served gold rebuild #9: the two gold chatter tables rebuilt on the merged list and matcher of rounds 61 to 63; 21 pairs removed by name, 4 true (pair: COO half 5584dce45a, CTO half d4eb3dc22f; COO~Z msg 31581 BEFORE bb-18)
**Authored by:** 2.0.0_SA_COO~H
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | round64/gold_rebuild9.act.py with the CTO half's C2 BNP counts in its record | commit hash | 60d3abcb5d (act script with bnp_before / bnp_after in its record; commit gate clean) | CLOSED 20261008T052157Z |
| L2 | verify | the act's own gate run (dry, PUTS 0) | RULE (rebuild #9): HOLDS and PUTS SENT: 0 in the act record's gate lines | act record gold_rebuild9.act_20261008T052038Z.json gate lines at 05:53Z: RULE (rebuild #9): HOLDS, PUTS SENT 0; removed by name 21 of 21, MENTION LOST 0 | CLOSED 20261008T062828Z |
| L3 | verify | amgt/harvest/gold/article_security_mention and chatter_daily: one new part each | the two newest part keys in the act record's after block, read back by a list | s3api list (UTC): article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet 7,696,668 B 06:12:53Z; chatter_daily/date=2026-10-08/part-20261008T061255Z.parquet 446,715 B 06:19:01Z; each the newest of its table; rebuild #8's parts still listed | CLOSED 20261008T062828Z |
| L4 | verify | the rule on the WRITTEN parts, with BNP's pair count before and after | act record result DONE with verify.holds true, or ROLLED BACK with both digests equal to BEFORE | act record result DONE, verify.holds true on the written parts: mention 48,025 -> 48,358, lost 0, removed by name 21 of 21, unexplained 0; daily 67,760 -> 68,002, gone 0, other 0; BNP_FP_Equity pairs 237 -> 238, on the form alone 2 -> 2 (the same two keys); no rollback | CLOSED 20261008T062828Z |

## Log

- 20261008T051724Z OPENED by 2.0.0_SA_COO~H with 4 leg(s)
- 20261008T052157Z LEG L1 closed: 60d3abcb5d (act script with bnp_before / bnp_after in its record; commit gate clean)
- 20261008T062828Z LEG L2 closed: act record gold_rebuild9.act_20261008T052038Z.json gate lines at 05:53Z: RULE (rebuild #9): HOLDS, PUTS SENT 0; removed 
- 20261008T062828Z LEG L3 closed: s3api list (UTC): article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet 7,696,668 B 06:12:53Z; chatter_
- 20261008T062828Z LEG L4 closed: act record result DONE, verify.holds true on the written parts: mention 48,025 -> 48,358, lost 0, removed by name 21 of 
- 20261008T062828Z CLOSED -- all 4 legs proven
