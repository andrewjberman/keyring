# POSN_ASTTAX -- PORTAL BRANCH REFS (round 5)

APPEND-ONLY. One line per worker branch committed INSIDE the portal submodule behind the
frontend freeze. The freeze bars the gitlink move, any promote and any DEV/PROD push; it
never barred source writes. The round's ONE drain ref is `refs/drains/posn-5-portal` and the
COO (`2.0.0_SA_COO~Z`) drains each branch below onto it. NOTHING HERE MOVES A GITLINK.

| branch | head | cut from (pin) | drain ref | worker | TO | at |
|---|---|---|---|---|---|---|
| `wk-posn-5-22-portal` | `c475e31e7014cb7e18ccf0c1cb6a335ad0720044` | `e85f6eb84f3a1771a37011a7e77e372570bad02a` | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V5-1` (AT5-s-5, F1) | 2026-09-14 |
| `wk-posn-5-22-portal` | `6c0deebd9121d5e955943d5a7507de51a102f480` | `e85f6eb84f3a1771a37011a7e77e372570bad02a` | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V5-1` (AT5-s-5, F1, ~19:0xZ amendment) | 2026-09-14 |
| `wk-posn-5-22b-portal` | `d93e79187135ff33dc9db2746a6fb64c70672062` | `6c0deebd9121d5e955943d5a7507de51a102f480` (= `refs/drains/posn-5-portal`) | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V6-1` (AT5-s-6, F2) | 2026-09-14 |
| `wk-posn-5-22c-portal` | `ea64113ba9ff44d0a329d1e1dae978bb3c8946fd` | `d93e79187135ff33dc9db2746a6fb64c70672062` (= `refs/drains/posn-5-portal`) | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V7-1` (AT5-s-7, F3) | 2026-09-14 |
| `wk-posn-5-22c-portal` | `dd1d33c6db84037fe8bcb8a8d19a819d9a250cbf` | `d93e79187135ff33dc9db2746a6fb64c70672062` (= `refs/drains/posn-5-portal`) | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V7-1` (AT5-s-7, F3, ~23:3xZ re-cut: the etfAdapter.ts:134 hunk ruled in by Z-S110) | 2026-09-14 |
