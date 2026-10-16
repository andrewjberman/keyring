# Drive log -- 2.0.0_SA_COO~C1, ADVI_COTBKF, 2026-10-16 17Z (written ~18:05Z, desktop-hk1uu7n)

One row per substantive tick: project | limb | round | TOs t/T | cells c/F | thread | act fired. Counts and ids only; no account, name or dollar value.

| tick | project | limb | round | TOs | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| ~16:30Z | ADVI_COTBKF | L6 issue | 104 | 0/1 | 0/1 | n | Andrew-direct recorded verbatim (@ffae57dacc: the match packet is not readable by a person); CTO msg 6874 ruled the read-only LOCAL review-sheet cell cut now; issuance @6d5afd6924 (CB-da-1, worker ~194, fanout 1 of 1 chains, cap 8) |
| ~17:00Z | ADVI_COTBKF | L7 execute | 104 | 0/1 | 1/1 | n | issuer read the workbook against the key and packet after AC1-AC3 passed; two defects of the issuer's own order found (old-account value read a cash-only residual for most accounts; shared-account rows not all adjacent); amendment 1 @3be9c112f0 sent to the worker |
| ~17:35Z | ADVI_COTBKF | L9 / drain | 104 | 1/1 | 1/1 | n | worker report verified independently (old values 98 of 98 re-derived from the served table); merge @b967009446; round-close-check MAY-CLOSE; CTO msg 6935 replaced the strength rule (band, name and CRM-household evidence, competing pairs drop a level); amendment 2 @3c6347734e; rebuilt sheet verified 107 of 107 labels against an independent derivation; merge @96ca44a6a5; CTO msg 6946 confirmed the CORROBORATED-only reading of "CRM household matches" |
| ~18:00Z | ADVI_COTBKF | L6 issue | 105 | 0/1 | 0/1 | n | CTO msgs 6923 and 6946 (FIRMBKTS row S59, silver account_attributes stale since 2026-08-19); issuer measured the drift (62 added, 45 billable and 130 portfolio-group changes, 122 multi-book accounts, 0 flag disagreements) and wrote two check scripts with controls; issuance @4fb60ead6e (CB-db-1, worker ~195, fanout 1 of 1 chains, cap 8); checker fix @1e8d53cb83 so AC2 runs from a sparse worktree |

**Decisions closed this hour.** (1) The review sheet for the 107 near-match pairs exists on Andrew's desktop, off git: 0 strong, 28 likely, 79 weak, 7 pairs lowered a level for a competing pair. (2) Strength rule: the CTO's, confirmed. (3) Round 105 cut; round 106 (never-widen pair, CloudOps apply, a read of the first silver partition newer than 2026-08-20) waits on worker ~195's record.

**Owed.** Andrew: name who confirms the pairs; send the one ask to Commonwealth; land the CRM archive. Bloomberg tranche result from `2.0.0_SA_COO~Q1` about 2026-10-17 15:00Z. Push state: LOCAL (origin box/dell1 last read e601e64560 at ~17:46Z).
