# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-04 02Z-03Z and 18Z-20Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (until 21:11:58Z); IRPT_YCDGEN FULL (issuer ~Y). The laptop slept from about 03:22Z to
18:3xZ.

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 03:18 | IRPT_BCKEND~Y Y-4 V1 | REQ-0d97252f READY 03:18:02Z; check gate elapsed_s 15.6; ledger irpt-y4-20261003 CLOSED | 0f7f6fba81 |
| 18:38 | IRPT_BCKEND~Y | ~D msg 104915: answered that the job is READY server-side and the page's UNAVAILABLE is S318 | msg to ~D |
| 18:42 | IRPT_YCDGEN L7-close | close run 1: stopped at the first write (firm fence). Row S1 BLOCKING | 8daaf100b2 |
| 18:5x | IRPT_YCDGEN | remedy: Cottonwood research principal plus the runner's assume; packet; CTO half asked | 9a01678592, bd21077c42, 4e03aecc26 |
| 19:14 | IRPT_YCDGEN | CTO half batch 239. Before-read, ONE safe-apply (2 add, 1 change), after-read WITH the bucket policy | b9f350b215 |
| 19:25 | IRPT_YCDGEN | close run 2: 6 kept, run.json, then WAF stop at step 7 | 9abe43df79 |
| 19:3x | IRPT_YCDGEN | amendment: --min-gap-s | f9f0d95cad (e463284e2d) |
| 19:44 | IRPT_YCDGEN | close run 3: same stop at step 7 (request-shaped). Layout built, report stored, ledger CLOSED, S2 disarms S1 | 517d7eee13 |
| 19:5x | IRPT_YCDGEN | looked at the report: the scatter's 400 body printed as content. Two layout amendments, report rebuilt and re-stored | 2eda34c580, b3ba844560 (9fbd1ecbdf) |
| 20:41 | IRPT_YCDGEN L8 | drain-end packet to 3.0.0_SA_CVO (blob 5e28ad4eca) | 70a35ee9dc |
| 20:4x | IRPT_YCDGEN FWD-1 | signed link printed to Andrew in the terminal (C-DELIVERY; not stored) | this log |

Next: the CVO's L9 on m-1.AC2 and FWD-1, then the CTO's round-1 analysis (five candidates in the packet). Y-2 and
Y-6 on the session, one at a time. S318 (prospect dates for corrected uploads).

Parked: the worktree C:/Users/AndrewBerman/Desktop/wk-ycdgen-2 holds untracked .scratch/ and a portal pointer, and its
branch is merged. Removing it needs a force; owner ~Y, un-parks on a look at its .scratch/.
