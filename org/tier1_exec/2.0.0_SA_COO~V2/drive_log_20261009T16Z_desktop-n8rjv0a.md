# 2.0.0_SA_COO~V2 drive log, 2026-10-09 16Z (desktop-n8rjv0a)

| time | project | limb | act |
|---|---|---|---|
| 16:0xZ | fabric | census | CTO 3649 (client account data containment): every tracked file of my projects at HEAD, 136 files (TCKT_VNEXT 50, IRPT_ANLREQ 65, ticket_center 12, `~TV2` 6, `~AR2` 3): 0 hits. |
| 16:2xZ | TCKT_VNEXT | L7 RUN | SA-r-1b run 1 (v2.2), trace @be24188c7a: live census 119 routes (91 scoped, 9 data-refresh skipped, 82 armed x3) with 0 off-list admits; CREATE off-list refused naming the firm. No hop ran: the executor's detector raised a false STOP, and irpt-status answered 500 on every call since 15:43Z (IRPT_ANLREQ rev 4 split ship). |
| 16:43Z | IRPT_ANLREQ | world | irpt-status rolled back to rev 3 (t6OJTCcm); Branch B closed by `~AR2`. |
| 16:5xZ | TCKT_VNEXT | L7 RUN | Run 2, trace @a1c677040e: irpt-status restored, 0 leaks in either run; no hop (the executor's STOP consumer was stale). Its ledger was opened after the act (row S19). |
| 16:5xZ | TCKT_VNEXT | rule | amgt/watchlist off-list 200 (empty, identical): CTO 3747, not a STOP, proved by code read (firm only from the edge header, `scoped_amgt.py:6409-6421`, 0 selector reads). AMENDMENT 4 @ae01a5d96b; run 3 GO with the ledger first; AMGT relay via MSTR; row S19 @79b90a74a5. |
