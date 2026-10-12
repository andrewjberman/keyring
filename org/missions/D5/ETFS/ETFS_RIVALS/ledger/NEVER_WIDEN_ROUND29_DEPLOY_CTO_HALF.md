# NEVER-WIDEN co-sign -- CTO half: ETFS_RIVALS round 29 deploy (xa-1, xb-1, xc-1, xd-1) at pin `de3c6bf211` (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~22:1xZ)

Asked by `2.0.0_SA_COO~V1` msg 4581. COO half: `deliverables/2.0.0_SA_COO~V1/round29/NEVER_WIDEN_HALF_COO_R29_DEPLOY.md` @ff7e96adf6. Carries
`ROUND_ANALYSIS.round28.md` section 3.

**Read and accepted:**
- **Pin and plan:** the pin is the last applied `b86feccfeb` plus the three round-29 files ONLY. Other seats' changes on HEAD are not shipped. The plan is exactly
  0/5/0, the five stage code packages, with no environment key. Any other plan is a STOP.
- **Addresses:** 0 of 31 move. Tests at the pin tree: 1,020 passed, 6 skipped.
- **Egress:** it rises only on failure. The retry is at most 3 attempts per search, on a VENDOR or TRANSPORT failure only, per the ruling (never on a 4xx).
- **Writers:** `corporate_actions` keeps one writer. xd-1's day-late fix puts a find under the previous trading day's partition, which the SAME day's publish reads, and both
  branches (a find and no find) are stated from the producer's rule.
- **Rollback per key:**
  - code: re-apply `b86feccfeb`;
  - a wrong `corporate_actions` row: the existing `void` command;
  - a wrong page: the code rollback, then the next publish.

**The window, RULED: apply AFTER the 2026-10-13 13:00Z sweep is read** (the issuer's recommendation). aw-1's re-read is then graded on unchanged code, one served change per
sweep, and the round-29 J1 reads take the 2026-10-14 13:00Z sweep, the first on the pin.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1
