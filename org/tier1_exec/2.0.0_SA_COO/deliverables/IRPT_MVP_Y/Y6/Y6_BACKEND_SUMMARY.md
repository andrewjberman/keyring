# Y-6 -- backend side of each page run (2.0.0_SA_COO~Y)

The page side (submit, page READY, open to sections) is `2.0.0_SA_COO~D`'s record:
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/yh/Y6_RELIABILITY_20261005.md`. This file is the backend
side: the server's READY (`live_walk/job_terminal_wait.py`) and the YCharts resident's journal milestones
(`live_walk/backend_join.py --journal`, joined by window). Per-run files sit beside it.

| Run | Case | REQ | Submit hop server | Release (read-back "calculating") | READ_BACK_DONE | Vendor requests | Server READY | Submit to server READY |
|---|---|---|---|---|---|---|---|---|
| 1 | Aproxy #1 | REQ-777d7546 | 6.46 s | 05:01:33Z | 05:16:40Z (+15m07s) | 4 + 5 | 05:18:26Z | 17m07s |
| 2 | Aproxy #2 | REQ-14fe69cf | 6.38 s | 06:41:09Z | 06:56:16Z (+15m07s) | 4 + 5 | by 07:00:01Z | -- (page READY 06:58:51Z) |
| 3 | Bproxy #1 | REQ-724a493e | (no HAR: run killed) | 07:19:48Z | 07:34:55Z (+15m07s) | 4 + 5 | 07:38:14Z | 18m40s |
| 4 | Bproxy #2 | REQ-1352d8c1 | 6.35 s | 08:23:50Z | 08:38:57Z (+15m07s) | 4 + 5 | 08:41:43Z | 18m07s |
| 5 | Cproxy #1 (Multi-Comp) | REQ-e7af8e8a | -- | 09:22:12Z (read-back 202 WAF challenge) | 09:37:18Z (+15m06s) | 5 + 5 | 09:40:23Z | 18m27s |
| 6 | Cproxy #2 (Multi-Comp) | REQ-01c90366 | -- | 09:49:21Z (read-back 202 WAF challenge) | 10:04:28Z (+15m07s) | 5 + 5 | 10:07:22Z | 18m17s |

**What the backend shows (runs 1-6):**
1. **Every job spends 15m07s in the resident's fixed read-back release.** `READ_BACK_LEASE_TTL_S = 900`
   (`ycharts/generate/recipe.py:688`, CTO batch 97 item 4) takes about 15 of each run's 17-19 minutes; the
   vendor's own calls and the PDF and certification take about 3. The read-back after the release answers `available`
   on its FIRST poll every time (`polls=1`), so when YCharts actually finished calculating is not measured. The firewall window it waits out lies in (122, 660] s
   (`WAF_WINDOW/`, staged to measure after Y-6).
2. **The page's list misses (runs 3 and 4) were local transit**, not the server. In run 4, 66 of 467 hops were over 15 s
   in the browser, with START queues up to 27 s, while every Lambda answered in under 7 s. The cause was the walker
   host's dev proxy under CPU load (~D 105223).
3. **The history route's server time is 3.3-7 s** for one page of 25 (irpt-status). Next-list.
4. **A Multi-Comp job sends 5 vendor requests before its read-back, and the read-back draws the firewall challenge** (runs 5
   and 6: `READ_BACK_PENDING:WAF_CHALLENGE`, status 202) where an Overview or Comparison read-back answers `calculating`. This
   fits the count model: the upload's resolve calls plus 5 job requests put the read-back at the window's 7th. The 900 s
   release absorbs it: READY on the first read-back after it, as in runs 1-4. The page side (~D): open to sections 10.3 s
   for a 104-card Multi-Comp, against 1.4-2.0 s for a 60-card Overview.
