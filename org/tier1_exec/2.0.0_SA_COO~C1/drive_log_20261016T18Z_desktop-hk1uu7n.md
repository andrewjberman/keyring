# Drive log -- 2.0.0_SA_COO~C1, ADVI_COTBKF, 2026-10-16 18Z to 19Z (written ~19:55Z, desktop-hk1uu7n)

One row per substantive tick: project | limb | round | TOs t/T | cells c/F | thread | act fired. Counts and ids only; no account, name or dollar value.

| tick | project | limb | round | TOs | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| ~18:20Z | ADVI_COTBKF | L9 / drain | 105 | 1/1 | 1/1 | n | worker ~195's patch and drift record verified (shape and plan checks pass; its drift counts equal the issuer's: 62 added, 45 billable and 130 portfolio-group changes, 122 multi-book accounts, 0 flag disagreements); merged @90831503eb; round-close-check MAY-CLOSE |
| ~18:35Z | ADVI_COTBKF | L4-R pair | 106 | - | - | n | COO half of the never-widen pair GIVEN @7a14b821b4 (blast radius with every prior version read, N = 1 writer, both gold readers, four branches, rollback per key); CTO half SIGNED with C-1 (msg 6968): no early dispatch, and the close read counts how many of the 122 multi-book accounts change portfolio_group between two consecutive builds |
| ~18:45Z | ADVI_COTBKF | L6 issue | 106 | 0/1 | 0/1 | n | issuance @5b64371c0c, `TO-CB-dc-1` (WORLD, the gate's floor for an infrastructure path; first attempt at SERVED refused), to `0.7.0_AE_CloudOps~FB1`; MSTR re-seated the lane 18:43:55Z (msg 6974) |
| ~19:22Z | ADVI_COTBKF | L7 execute | 106 | 0/1 | 1/1 | n | NUDGE: lane read LIVE and IDLE ("awaiting TOs") with the document still version 4; sent it the order path |
| ~19:30Z | ADVI_COTBKF | L7 / verify | 106 | 1/1 | 1/1 | n | lane reported done (msg 6998); independent reads: live default version 5 differs from version 4 by exactly the one added non-gating step after the holdings step, nothing removed; manifest and the 2026-08-19 partition unchanged, prefix still 1 key; root plan "No changes"; ssm.tf @4295288ac3; round-close-check MAY-CLOSE; the round stays open for the real run (the scheduled fire, about 2026-10-17 midday) |

**Decisions closed this hour.** (1) `opal-cot-silver-run` is at version 5 and merges `account_attributes` as a non-gating step. (2) The pair for the served gold move is signed and its conditions (C-1, no early dispatch) are recorded. (3) Round 105 closed; round 106's apply is done and its outcome is read at the fire.

**Owed.** The close read after the first scheduled silver fire and the gold run that follows (about 2026-10-17 midday): `dc1_fire_read.py fire`, then `snapshot` after each build and `compare` for C-1; dated wait on `schedule:cot-silver-run` until 2026-10-17 13:00Z. Andrew: name who confirms the pairs; send the one ask to Commonwealth; land the CRM archive. Bloomberg tranche result from `2.0.0_SA_COO~Q1` about 2026-10-17 15:00Z. Push state: LOCAL @e7d7275368 (origin box/dell1 last read 299c28236c at ~19:52Z).
