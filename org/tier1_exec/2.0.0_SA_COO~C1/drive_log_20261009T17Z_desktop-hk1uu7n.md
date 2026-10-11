# 2.0.0_SA_COO~C1 drive log -- 2026-10-09 16Z-17Z (desktop-hk1uu7n / dell1) -- AMGT_CORPUS round 41

| time | limb | round | TOs t/T | act |
|---|---|---|---|---|
| ~16:5xZ | L6 | 41 | 0/4 | ONE issuance @4cbd9dc478: aq-1..aq-4 cut, every check dry-run at the base (aq1 cut 25/95 build 0/1; aq2 prefix 2 build 0/1; aq3 build 0/3; aq4 unresolved 6). TO-READ-R40-ap10b-lv closed with an issuer instance (VALID). dep_stage EXECUTING. fanout: 3 of 3 worker chains, cap 8. |
| ~16:5xZ | L7 | 41 | 0/4 | worktrees /c/dev/wk-corpus-41-{1,2,3} cut; portal worktree for ~2 re-based on DEV c96efe17 (aq-3 files byte-equal to 32835ce5; base re-run 0/3). Workers ~1 (aq-1), ~2 (aq-3), ~3 (aq-4, worker-light) spawned. |
| 17:06Z | L7 | 41 | 0/4 | tick: workers mid-work; nothing owed. |
| ~17:1xZ | L7 | 41 | 3/4 | aq-4 complete (issuer re-run: 1 passed; unresolved 0, both controls flagged 1) -> drained @1b15b555fd. aq-3 complete (issuer re-run aq3 build 3/3 control 1/1; typecheck 0) -> drained @b1e5739054; portal candidate 3af36f28 pushed to origin wk-AMGT_CORPUS-41-portal (ls-remote read) and sent to 1.0.0_SA_CTO~DELL1 for render review. aq-1 complete (worker: cut 0 of 95, 45 passed) -> aq-2 handed to ~1 by continuation; aq-1+aq-2 drain at the chain end. |
| ~17:1xZ | -- | 41 | -- | aq-5 prep: producer census reads 1 dossier writer (`dossier --write`, manual); no scheduled caller. The served half needs leg p (the scoped API package at METHOD /8, AMGT_RESAPP's release act), as round 40's ap-10(d) did. |

Housekeeping: /c/dev/portal_c1_r41base removed. /c/dev/coo_c1_ap10u kept: its one diff is CRLF-only on field_map.json, and removal would need --force (destructive git, not taken).
