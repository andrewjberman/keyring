# POSN_AGGFIX -- PORTAL BRANCH REFS (round 1)

APPEND-ONLY. One line per worker branch committed INSIDE the portal submodule. The round's ONE drain ref is
`refs/drains/aggfix-1-portal`, created by the COO (`2.0.0_SA_COO~Z`) at the first portal drain. Every worker branch is cut from portal
`edf85ce503` (origin/PROD, the tree Andrew checked live 2026-09-15) or from the drain ref at its hand-over, and the pin is recorded here.
NOTHING HERE MOVES A GITLINK; the DEV to PROD promote and any push are Andrew's word (C-PORTAL-PROMOTE).

| branch | head | cut from (pin) | drain ref | worker | TO | at |
|---|---|---|---|---|---|---|
| wk-aggfix-1-3-portal | 63edeeeb51 | edf85ce503 (origin/PROD) | refs/drains/aggfix-1-portal (created by 2.0.0_SA_COO~Z at drain) | 0.9.0_WK_POSN_AGGFIX~3 | POSN_AGGFIX.TO-B1-1 | 2026-09-15T19:48:40Z (portal commit time, UTC) |
