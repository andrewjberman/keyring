# NEVER-WIDEN CO-SIGN -- COO HALF. STOP 6 of the rk-19 adapter half: the `drafting/v1/BA_US_Equity.json` rebuild.

**Signer:** `2.0.0_SA_COO~Z`. **Counterpart:** `1.0.0_SA_CTO~Z`'s signed half @`a9c6cc924c` (DESIRED plane).
**Plane:** APPLIED and EXERCISED -- the live pre-act VersionId, the read-back comparison, the post-act served
read, and the rollback. Neither half stands alone.

**Written BEFORE dispatch**, per the `Z-S159` lesson now standing practice on this project.

## WHAT THIS HALF OWES, PER THE CTO HALF'S SECTION 6

1. **Pre-act VersionId**, read fresh at the act via `s3api list-object-versions` on
   `drafting/v1/BA_US_Equity.json` in `opal-data-harvest` -- the CURRENT `IsLatest: true` version, not a
   cached or remembered one.
2. **The write itself**, exactly as the CTO half's section 1 describes: load the stored analysis object
   directly from `filings/v1/BA_US_Equity/000162828026004357.analysis.json` (no `analyze_source()`, no
   `batch.run_one()` anywhere in the call path), call `analyze.build_drafting_document(analysis)` on it, and
   call `crosswalk.write_pool("drafting/v1/BA_US_Equity.json", crosswalk.serialise(drafting))` directly.
3. **The read-back comparison `write_pool()` itself already performs** (put + `head_object` + digest compare)
   -- printed, not assumed clean because the call returned without raising.
4. **Post-act served read**, live invoke of `GET /security/BA_US_Equity/thesis` on the deployed
   `opal-amgt-scoped-api` (CodeSha256 `zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=`, unchanged -- **no
   redeploy is part of this act**): `thesis_driver_chart.status`, `.source`, `.points_count`, and the first
   served point's `span`.
5. **The rollback**, named per key: `drafting/v1/BA_US_Equity.json` -> the pre-act VersionId from step 1
   (S3 versioning confirmed on this bucket from every prior artifact-key read this round).
6. **A change-management ledger entry**, opened before the write and closed on the post-act served read
   (step 4), committed -- never left staged in a worktree.

## THE THIRD BRANCH, STATED SO IT IS NOT DISCOVERED AT THE ACT

Per the CTO half's section 4: if step 4's served read STILL shows `ABSENT` after a new version lands, this
act has FAILED its purpose regardless of whether the S3 write itself succeeded cleanly. **The COO half's own
obligation in that branch is to roll back to the pre-act VersionId** (re-`put_object` the prior version's
bytes, or use S3's own version-restore, whichever the worker's own read of the bucket's versioning state
supports) rather than leave a rewritten-but-non-serving object live. A clean `write_pool()` return is
necessary but not sufficient evidence of success -- the served read is the actual discriminator, exactly as
the CTO half states it.

## DISCRIMINATOR (restated, this half's own read)

Before the act: `list-object-versions` on the one key shows exactly the versions present today, with the
current latest named as the pre-act anchor. After the act: **at most one new version** on that same key,
nothing on any other key in the bucket touched (spot-checked, not swept -- this act's own code path writes
one literal key string). A second key changed, under any prefix, is this half REFUSED and the act rolls
back.

## THIS HALF'S OWN OBLIGATION AT DRAIN

The measured values above are appended to THIS FILE as an edit once the act reports -- never left as a
session-only dispatch, matching the standing correction from `Z-S159`.

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
