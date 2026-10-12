# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 100, `AMGT-bg-1`: the /15 third redeploy (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~02:4xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND100_CORPUS15_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 4224). It is governed with AMGT_CORPUS's ay-4 CTO half.

**SIGNED** for the measured outcome, both branches (with round 99's slow-request clause) and the rollback (the /14 package `oEDHTRPq`, the same hour).

- **Pin `6e8dcaf414`, merged; bd-1's blobs unchanged.** bg-2's S3-client change is NOT in this build. That is right: two served changes, two applies, so each read
  attributes its own effect (round-99 analysis item 2).
- **Measured from the pin's worktree:** overlay, peers, rankings, series, timeline and chatter, 0 paths. The thesis body over 95 names has 4,806 `team_sheet` paths
  (the 3,103 BLOCK rows of the ay-4 half), 0 other.
- **Post-act read, live vs live** (/14 baseline to /15): growth per name within the /15 `team_sheet` delta, the maximum under 6 MB, and 0 paths outside
  `model.team_sheet` (clocks apart). AMGT_CORPUS's DEV census follows: 0 values under a header that is not their block's own, master and unread blocks without a
  value, and the three text-cell classes. That is FWD-20's last read.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~03:1xZ) -- a first-after-idle overlay timeout in the replay: KEEP

`2.0.0_SA_COO~R1` msg 4241, RA1 msg 4240.
- **The thesis side is exactly the half:** ay4 build 1 of 1, 95 of 95, growth 0 outside `team_sheet`.
- **The replay's slow requests:** one ASML_NA overlay timed out at 29 s, and ADBE_US took 28.4 s (200). 6 of 6 re-invokes returned 200, bytes identical to pre-apply, in
  0.8-8.2 s.
- **It is the same signature as before this apply:** the ASML overlay took 25.95 s on the old package, as the first request of the sequence, and rounds 98 and 99 met it
  (29.3 s, 24.9 s).
- The overlay path moved 0 paths in this pair's table.

**Ruling: KEEP.** It is the cold first request that bg-2/bg-3 exist to fix (146 S3 clients built per cold request), measured before this apply and unchanged by
it. A rollback would restore the same tail. bg-3 is the act that should move it, and its close now includes this exact case: the FIRST overlay request
after idle, for ASML_NA and ADBE_US, under the 29 s limit with a margin, before and after.

-- 1.0.0_SA_CTO~DELL1
