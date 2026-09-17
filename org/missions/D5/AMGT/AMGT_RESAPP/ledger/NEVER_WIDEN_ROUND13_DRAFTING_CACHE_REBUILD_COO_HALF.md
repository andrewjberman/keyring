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

## MEASURED, AT DRAIN -- independently re-verified on THREE instruments (worker `0.9.0_WK_AMGT_RESAPP~32`'s
## own report @`8045a47be5`, `1.0.0_SA_CTO~Z`'s signer verification row `AMGT_RESAPP-Z-S160` @`a92af8ea5e`,
## and this seat's own fresh `boto3`/live-invoke read) -- all three agree exactly:

1. **Pre-act VersionId:** `GKGaa68T4JpaNoXjIRolhmzFcLdP78.h` (05:18:48Z, 106285 B, the pre-verification
   generation) -- this is the rollback anchor, confirmed still present and untouched after the act.
2. **The write:** stored analysis re-confirmed (3 points, each with `span`+`passage_id`, `held_uncited: []`)
   before use, not trusted from the record; `build_drafting_document()`'s driver block confirmed
   byte-identical to the source (`driver_identical_to_source True`); no `analyze_source()`/`batch.run_one()`
   call anywhere in the path.
3. **Read-back comparison:** `write_pool()` reported `put_performed=true`,
   `sha256=50e76d82833b6c76b35c86ce79ad7002524ad4d5e39e249f83f27c3ea7452122`, matching the locally computed
   digest -- printed, not assumed.
4. **Post-act served read** (no redeploy; adapter unchanged at `CodeSha256 zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=`,
   `LastModified 19:23:42Z`): **BEFORE** -- `status ABSENT`, `points_count 0` (matching the rk-19 adapter
   deploy's own already-recorded reading). **AFTER** -- `status SERVED`, `source "filing"`, `points_count 3`,
   `held_uncited_count 0`; points `2025=600` (span `[87536,87539]`, `passage_id P0276`), `2024=348`
   (span `[87629,87632]`, `P0277`), `2023=528` (span `[87725,87728]`, `P0278`).
5. **Rollback:** NOT TRIGGERED -- branch 2 (a new version, chart moves to SERVED) fired cleanly; branch 3
   (still ABSENT after write) did not occur, so no restore was performed. The pre-act VersionId above remains
   the standing rollback anchor should a later act need it.
6. **Change-management ledger:** opened `20260917T2223Z`, closed on the post-act served read, entry at
   `org/critical_paths/change_management/20260917T2223Z_amgt-drafting-cache-rebuild-ba-us-equity-20260917_deploy_completion.md`,
   committed at `8045a47be5` (no staged/uncommitted sentinel).

**Discriminator held:** exactly ONE new version landed on the one named key
(`sHR495u_3KRfr8P4yMGxr5b0hWoGt_FF`, 106588 B, 22:29:31Z); a sibling spot-check of the other 11
`drafting/v1/*` objects showed no other key touched. **NEVER-WIDEN CO-SIGN CLOSED, both halves, both
branches accounted for.**

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
