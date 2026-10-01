# 2.0.0_SA_COO~H drive log -- 2026-09-30 05Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b). Lease: FULL. Round 25, L7 -> close.

| time | act |
|---|---|
| ~05:0xZ | `o-5` attempt 2 recorded @`2747a7d0fb`. AMENDMENT 2 @`5facb19f57`: act 3 is `upload-harvest`, ft is no-write, and AC2 is re-grounded on FWD-3's words. CTO re-sign @`7db8b9a744`, carried @`e576c64a06`. |
| ~05:1xZ | `o-5` act 3: 22 articles and 10 listings uploaded, 57 new objects under bbg/wsj only, AC1 and AC2 PASS. Drained @`366757825d`, complete @`aa587798c4`. |
| ~05:2xZ | `o-4` dispatched on `wk-hvst-r25-64` @`aa587798c4`. Its act wrote 3 sa silver parts (`part-20260930T052800Z`); AC1 and AC2 PASS. The worker is finishing. |
| ~05:3xZ | ANDREW-DIRECT: a mention count per article wherever articles are displayed. |

**The ANDREW-DIRECT item:**
- The backend already carries it: `mention_count` on 304 of 304 served rows, served per article on `/timeline/day`.
- Recorded @`8135566a29`, and the MCP was relayed to `2.0.0_SA_COO~D`, which owns the frontend.
- Gap: the 22 new `o-5` articles get a count at the paired mention rebuild, carried as a round-26 item.
