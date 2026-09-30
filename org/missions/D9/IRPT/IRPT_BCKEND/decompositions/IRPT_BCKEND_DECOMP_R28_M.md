# IRPT_BCKEND decomposition -- ROUND 28, WORKSTREAM ~M (2026-09-30, 2.0.0_SA_COO~M, on MDPF_SECCLASS release step 2)

Cut on MDPF_SECCLASS release step 2: ledger mdpf-secclass-backfill-20260930 CLOSED @f13cddd058. etf-classifications
grew 375 -> 2,309 rows (1,934 scheduled rows, 0 existing rows changed), on Andrew-direct 2026-09-30 ~02:2xZ
("bd-securities values can seed new rows. THey just don't overwrite existing rows."). That lifts the hold on the ~M
Holdings chain IB-mr-251 -> 261 -> 271 -> 272 (branch wk-IRPT_BCKEND-84, ruling @469c404474).

The chain's two halves (HOLDINGS_ETF_CLASSIFICATIONS for 251, HOLDINGS_AGGREGATES for 261) were measured before the
backfill, and 251's half before 271 changed its refusal into unclassified-by-name. A half is read from the producer's
own rule at signing, so this round re-measures and writes ONE release half for the whole chain.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-281` | The Holdings release packet: a real-build census at three firms on the held chain against the post-backfill table (moves against today's served snapshot, unclassified, GLD/PHYS/VXX, aggregates), and one release half covering 251+261+271+272 with its release order | FWD-5 (Holdings) | WORLD (reads table, firm buckets, served snapshots) | IB-mr-272 (the chain end); MDPF_SECCLASS release step 2 (landed) |

Chains: A = 272 -> 281 on slot `0.9.0_WK_IRPT_BCKEND~84` (same worktree; 281 measures the chain it releases).

**Release order the half must carry:**
1. The IAM apply: GetItem/Query on etf-classifications for the Holdings firm principals, the grant 251 drafted in
   holdings_refresh.tf. It is AE-lane and needs its own act.
2. Drain the branch to CLOUD.
3. The Holdings package re-mint and the directory bundle at MSTR's push.
4. The holdings Lambda redeploy with its re-staged contract (272).

All four come AFTER IB-mr-222 Part 2 reads the 2026-09-30 14:15Z scheduled fire. That fire proves the L0 re-mint on
today's packages, and a classifier change inside the same fire would blur that evidence.
