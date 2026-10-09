# CTO RULING -- AMGT_RESAPP's two Bloomberg asks go to dell1's backfill queue as research-page requests (2026-10-09 ~01:3xZ)

**Ruled by:** `1.0.0_SA_CTO~Z`, on the laptop `1.0.0_SA_CTO`'s relay (bus 102b731c, msg 32216: "rule the two CROSS-BOX forks ...
or file each with .tools/xadj.py open"). **The calls:** `sitez-20261009T011758Z-107a` (ABNB's model-block Bloomberg pull, carried
from rounds 78 and 79) and `sitez-20261009T011759Z-493c` (one Bloomberg identity read of `ICT US Equity`: ID_ISIN, ID_SEDOL1,
ID_BB_GLOBAL, EXCH_CODE). This seat had first HELD both for Andrew's per-use word.

## Ruling: neither is held for Andrew, and neither runs ad hoc. Both are filed as requests on dell1's backfill demand queue.

## Why

Andrew has already worded the route for Bloomberg asks like these. Record
`ANDREW_DIRECT_20261008_224xZ_BACKFILL_QUEUE_ENDPOINT_CONFIRMED_PRIORITY_BBG_YAHOO_ONLY.md`, VERBATIM:

> "1.) Yes. 2.) Production daily pulls includes ETF Positioning. Then Current clients and new client onboarding. Then rival funds
> history ... Then research pages. Then finally former clients last. 3.) Only BBG and Yahoo for now."

`ANDREW_DIRECT_20261008_230xZ_SITEZ_OPEN_CALLS_ANSWERED_RELAY.md` adds that daily Bloomberg price asks belong to "dell1's backfill
queue". Both asks are research-page data for AMGT_RESAPP, which is his priority 4, from Bloomberg, a source his item 3 names. So the
vendor use is his word, through that queue in that order. A one-off pull outside the queue would be a use no word of his names, so
it is not run.

## How

- `2.0.0_SA_COO~Z`, or DELL1's RESAPP COO after the move, files each ask on the queue as a research-page request. The ICT read names
  the four fields and the deciding question: one key or two, `ICT_US_Equity` vs `ICT_PM_Equity`. The ABNB ask is one model-block
  pull.
- The Bloomberg call itself runs on site Z, the only box with the Terminal, as the queue's named producer, inside `bbg_budget`.
- Until the queue serves them, row Z-S369 stays UNRESOLVED with its stated reason, and ABNB's model block stays as stored.

-- 1.0.0_SA_CTO~Z
