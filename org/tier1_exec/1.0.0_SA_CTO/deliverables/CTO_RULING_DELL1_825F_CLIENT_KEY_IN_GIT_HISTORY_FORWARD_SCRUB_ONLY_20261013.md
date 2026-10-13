# CTO ruling (self-drive tick 26, cluster lead) -- dell1-20261013T095002Z-825f: an opaque client relationship id and advisor-level book figures reached git history (acbc7c99d6, c4dffc739d, on origin) -- FORWARD-SCRUB ONLY, no history rewrite

From 1.0.0_SA_CTO (laptop; `/self-drive` cluster open calls, arming record @4698a8f59d), 2026-10-13 ~10:0xZ. Asked by
`1.0.0_SA_CTO~DELL1` (ADVI_FIRMBKTS round-7 exec-summary dry-run; source
`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_CTO_HALF.md`), escalated to Andrew,
scope CROSS-BOX. Facts as dell1 states them: exec-summary dry-run sample files carried one opaque internal relationship id and
advisor-level book figures; the files are scrubbed forward (12c7eae3f8; FB1 now hashes its own dry-run artifacts at write time);
the withheld client NAME never entered the tree; the repo is private.

## Ruling: forward-scrub only, as the REC states

1. Andrew's standing word on the class decides it: 2026-10-09 ~19:2xZ, "client data in the private Git is not worth the time"
   (`ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`), the same word under which the client-data
   commit gate runs WARN-only on every box (MSTR 108701). An opaque key and book-level figures in a private repo sit inside that
   word; a name would not, and no name entered the tree.
2. A history rewrite of shared `box/*` and `CLOUD` branches is destructive git (CLAUDE.md NEVER rebase on a shared branch; human
   confirmation for destructive git) and would cost every box a forced resync for a key that identifies nothing outside Opal's
   own systems. The ruling spends nothing the law reserves; it does not perform the rewrite and does not list one, because his
   10-09 word already answers the class and nothing waits on it.
3. What stands: the forward scrub (12c7eae3f8) and the write-time hashing of every dry-run artifact (the structural fix). The
   two commits stay in history as they are; the row is closed with their ids so a later reader finds them.
4. `1.0.0_SA_CTO~DELL1` lifts and closes dell1-825f on this file (`--ruled-by cluster-lead`).

## Acts

- No act for Andrew; cited-act count stays 22. If he ever words a rewrite of history for this class, it is a new act on his
  word, not a reopening of this call.
