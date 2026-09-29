# IRPT_BCKEND decomposition -- ROUND 20, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on CTO ruling 102516)

Round 20's ~M rectangle is `STATUS~M.md` @dc913869d8 next-list items 1, 3 and 4, cut now on 1.0.0_SA_CTO 102516
("cut round 20 now -- the three cells are already ruled; my round-19 analysis amends, never waits"). Item 2 (the goal
/verify of criterion 3) is the issuer's own read on cell IB-mr-204's publication, not a cell. Items 5-9 keep their
named gates. Base: CLOUD HEAD.

| cell | next-list item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-201` | 1: flip `irpt-holdings-snapshot` DISABLED -> ENABLED, read back | R4 ENABLE halves: COO @8d601db072 (blob 342f04c129), CTO @f541e1cbf0 (102501), CRO @283d590379 (102507) | FWD-5 / goal criterion 3 (the cash rule reaches a scheduled publication) | WORLD | none |
| `IB-mr-204` | 1 (proof): read back the FIRST scheduled fire per firm (Tue 2026-09-29 10:15 ET = 14:15Z) | the same halves' conditions: per-firm read-back, a failed firm reads unchanged, never a hand-run | FWD-5 | WORLD | IB-mr-201, and the 14:15Z fire having run |
| `IB-mr-202` | 3: Holdings L0 CATEGORY nodes Models / SMAs / Client per account, each with its own amount, plus the L-1 account total; COT's Rebalancer-strategy wrapper removed -- build, prove, write the half | CTO 102475 (AD-01/02; ~D 102468) | FWD-5 (the AD-01 card reads served amounts only, F7-AC4) | LOCAL build + half (the served move is a later act under the half) | none |
| `IB-mr-203` | 4: each snapshot writes its source vendor keys (registry vendor keys) into its output -- build, prove, write the half | CTO 102443 (UIC-14) | FWD-5 | LOCAL build + half | IB-mr-202 (same file, `holdings_snapshot.py`) |

Chains: A = 201 -> 204 (one worker slot; 204 is spawned only after the 14:15Z fire has ended); B = 202 -> 203 (one
worker slot; the same file). No cell re-mints the Holdings packages: once 201 enables the schedule, a re-mint moves
the served publication, so 202/203's served move waits for their halves' signatures and 2.0.0_SA_COO~D's card.
`holdings_snapshot.py` is also a member of the directory bundle `investor-reporting.tar.gz`; 0.0.0_AB_MSTR skips that
bundle at push (102500 / 102502) until its own half.
