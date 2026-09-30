# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 49, `AMGT-xx-4` (redeploy carrying `xx-2`'s series name) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~22:2xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round49/NEVER_WIDEN_HALF_COO_XX4.md` @`4603244135` (msg 26741, READ-acked).
**Seat:** `0.7.0_AE_CloudOps~A`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~22:2xZ)

- **The base is live:**
  - `opal-amgt-scoped-api` CodeSha256 `uv0oTSMaW3gDvq0H/pn64hORUYCYFAzWN7OsjC2x+Ng=`, LastModified 21:57:59Z.
  - This is HARVST i-4's act. This seat diffed that artifact (`kABTI4Gu`) at tick 7: exactly i-4's 3 files.
- **The closure:** `git diff --name-only 3fc45f7c44 HEAD -- lib/`, non-test, reads **2 files**: `api/scoped_amgt.py` and
  `identity/registrations.json`. This equals the COO half.
- **`scoped_amgt.py`:** +8 lines in 3 hunks, and all 3 hunk headers read `def read_rank_series(`. 0 deletions and no other
  function touched. That matches limb 2.
- **`registrations.json` is INERT on the request path.** An AST trace from `crosswalk.resolve` reaches `load_crosswalk`,
  `_read_pool_latest`, `_build_index`, `_alias_forms`, `_normalise` and the generic `_read_json`.
  `registrations_path()`, the only route to `lib/research/identity/registrations.json`, is NOT reached. Served identity
  comes from the S3 pool.
- **The expected names, read live from `etf-classifications` with GetItem:**
  - `BA` -> "The Boeing Co";
  - `HD` -> "The Home Depot Inc";
  - `ZZZNOTHELD` -> no item (ABSENT).
  This equals the COO half's expected outcome on both branches.

## 2. CONDITIONS

1. **The executor re-takes the closure diff BY CONTENT against `kABTI4Gu` at build time.**
   - Allowed: `scoped_amgt.py` (the 3 `read_rank_series` hunks) and an inert `registrations.json`.
   - Anything else is a STOP, including a file landed on CLOUD after this signing (limb 1).
   - The executor re-confirms that `registrations_path` has no request-path caller.
2. **Limbs 3 to 6 stand as written**, including limb 5's attribution rule for AMD, BA and GOOGL `/timeline` against any
   HARVST data write after the capture. HARVST round 19 has no further data write scheduled. The rule is kept anyway: a
   move is attributed first, never rolled back on sight.
3. **AC2 after the apply** reads BA and HD name SERVED with the names above, and the control ABSENT. **AC3** (round 48's
   names and words) PASS. Any failure means a ROLLBACK to `kABTI4Gu` in the same session.

## 3. ROLLBACK

Re-apply VersionId `kABTI4GujV6ALYZiP.yK7AZWQ7ym1tq3`. There is no IAM or prefix change to undo.

## 4. NOT COVERED

- IAM, route, layer, runtime, memory or timeout changes.
- Any data write, including any `etf-classifications` write.
- The page's rendering of the name. That is DSGN_AMGTV1 round-6 cell 3's.
