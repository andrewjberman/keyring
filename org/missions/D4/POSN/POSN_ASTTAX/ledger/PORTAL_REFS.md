# POSN_ASTTAX -- PORTAL BRANCH REFS (round 5)

APPEND-ONLY. One line per worker branch committed INSIDE the portal submodule behind the
frontend freeze. The freeze bars the gitlink move, any promote and any DEV/PROD push; it
never barred source writes. The round's ONE drain ref is `refs/drains/posn-5-portal` and the
COO (`2.0.0_SA_COO~Z`) drains each branch below onto it. NOTHING HERE MOVES A GITLINK.

| branch | head | cut from (pin) | drain ref | worker | TO | at |
|---|---|---|---|---|---|---|
| `wk-posn-5-22-portal` | `c475e31e7014cb7e18ccf0c1cb6a335ad0720044` | `e85f6eb84f3a1771a37011a7e77e372570bad02a` | `refs/drains/posn-5-portal` | `0.9.0_WK_POSN_ASTTAX~22` | `POSN_ASTTAX.TO-V5-1` (AT5-s-5, F1) | 2026-09-14 |
