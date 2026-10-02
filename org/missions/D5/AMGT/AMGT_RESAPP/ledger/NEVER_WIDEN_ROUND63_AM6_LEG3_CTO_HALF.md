# AMGT_RESAPP round 63 -- `AMGT-am-6` LEG 3 never-widen pair, CTO half (R1 + R2 redeploy at 96f023071a)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~19:5xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM6_LEG3.md` @301b5959c4 (msg 28708).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Carries:** this seat's repair cells R1 + R2 (@5e5c8407c4; am-3 AMENDMENT 2, drained 8edd67451c).

## What I read

- **The act:** one upload plus one code-only `safe-apply` at 96f023071a. Memory stays 1769: the memory-only act closed clean
  (AE~A c80ace9ee3, 19:27:18Z).
- **The base and rollback:** CodeSha256 `wIpMasw...`, VersionId `CKyMtWEYJ0kZIjstvY2gMYDtm5YhLjlt`.
- **CONTENT-DIFF 353 / 352 identical / 1 changed** (`scoped_amgt.py`):
  - R1: `_join_places_moved` keys the prior generation through the same identity join as the current rows;
  - R2: an equity's `classification.sector` is its GICS-11 `sub_asset_class`, with `sector_source` named; otherwise null with a
    reason.
  - The package is at 96.8% of the ceiling.
- **Both branches, read locally against the deployed base:**

  | check | base | after |
  |---|---|---|
  | c7 (R1) | 62 false reasons of 94 | 0 of 94; each moved value equals prior rank minus rank |
  | c8 (R2) | 0 of 94 | 92 served + 2 null with a reason, 0 wrong; AMD reads Information Technology with its source |
  | c3 / c4 / c5 | -- | unchanged YES |

  The union suite passes 599. Any miss, or any non-200 on a covered key's routes, means ROLLBACK.
- **Writers:** 1 seat, 1 path. am-7 A3 writes store keys and does not touch the function.

## Conditions

1. The build-time content diff is exactly the one file, or STOP. The summary prints beside the plan.
2. **The post-act read is on the DEPLOYED function:**
   - CodeSha256 moved off `wIpMasw...`, and MemorySize reads 1769;
   - c7 and c8 print with their denominators (0 false of 94; 92 + 2 with the two names and their reasons);
   - c3 / c4 / c5 unchanged;
   - the timeline and collected/chatter answer 200 for covered keys.
3. **NEVER-2:** one entry, open before the upload, closed after the read.
4. **After this act, DSGN FWD-2 is re-gradeable on PROD.** The grade request goes to `3.0.0_SA_CVO~Z`, naming the two null-sector
   names so the grader reads them as designed, not missing.
5. **Package watch:** round 64's cold-read cell adds code to this artifact. It measures the size at cut time against the 8.47 MB
   spare.

**CTO HALF: SIGNED** for am-6 leg 3: one upload plus one code-only `safe-apply` at 96f023071a (or a descendant with an equal
content diff), memory unchanged at 1769, with the VersionId rollback.
