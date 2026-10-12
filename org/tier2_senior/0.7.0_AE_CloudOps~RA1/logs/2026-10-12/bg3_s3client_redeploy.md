# 0.7.0_AE_CloudOps~RA1 -- 2026-10-12 -- AMGT_RESAPP AMGT-bg-3: the one-S3-client build applied, no served byte moved, cold first request recorded

**Date:** 2026-10-12 (GO 04:05Z, msg 4263; captures 04:10-04:16Z; apply 04:17:52Z; function LastModified 04:18:21Z; quiet period 04:30:35Z-04:48Z; ledger closed after AC1-AC3 and both cold pairs)
**Task Order:** AMGT_RESAPP.TO-AMGT-bg-3.redeploy-the-scoped-api-carrying-the-one-s3-client-from-a-merged-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 11 of 11; the cold-first-request arm read and recorded)

## Objective

The second apply of round 100: `opal-amgt-scoped-api` from the MERGED pin `ba22af15f5`, whose one change is `AMGT-bg-2`'s
`scoped_amgt.py` (one S3 client per container, pool 32; `9b13bf0371d4` -> `9f72b58aa87e`). The act must move no served byte, and
the CTO's cold-first-request arm asks for the first overlay request of `ASML_NA_Equity` and `ADBE_US_Equity` after the apply and
after a quiet period of at least 15 minutes, each 200 and under 27 s.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin is on the first-parent line. Detached worktree; `r94_admission_table.py --pin
   6e8dcaf414` showed exactly ONE member differing at the half's blobs.
2. Captured the rollback package (hash-checked), re-hashed the wheels (6 of 6), read the source-map entry, swept 66 worktrees (1273
   entries): only this seat's entry in the shared tree.
3. Built at the pin offline: 408 files, CHANGED 1 (`scoped_amgt.py`), ADDED 0, off-list 0.
4. Captured, in sequence and single-threaded, the 528-request timed route baseline (its first request is the cold pre-apply
   reference: ASML_NA overlay 28.04 s) and the 95 live Thesis payloads (local, uncommitted), finishing at 04:16:13Z.
5. Uploaded with read-back, planned untargeted (1 of 53), applied through `safe-apply`; the FIRST reads after the apply were a
   simultaneous cold pair (24.0 s and 23.8 s, 200, identical); told the issuer and asked for a HOLD.
6. Single reader: the timed replay (status moved 0, only clocks changed, 0 over 20 s, median 0.39 s), the thesis capture and
   `ay4_compare` (95/95, 95/95, every name's growth 0), AC1 and AC3.
7. Quiet period, verified from the invocation record (0 invocations 04:31-04:47Z); then the cold pair again: ASML_NA 27.81 s (the
   band the half records; three identical re-invokes), ADBE_US 24.01 s.
8. Read the function's own REPORT lines for the cold requests and counted pool warnings by phase; the hold released; the record
   step; the ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act |
| r94_admission_table.py | at the pin, --pin 6e8dcaf414 | PASS | 1 member |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| aw4_capture.py / ay4_compare.py | pre and post | PASS | growth 0 for every name; local, uncommitted |
| bf1_capture.py | timed capture, replay, compare | PASS | clocks only |
| cold_pair.py | simultaneous cold pair x2 | PASS, RECORDED | the arm |
| r97 / r95 / r94 / r89 / r92 checks | AC1, AC3 | PASS | exit 0 |

**What worked:** measuring the cold arm as a simultaneous pair so both names reach a cold container, replay FIRST after the apply
so nothing warmed the function before it, and proving the quiet period from the invocation record rather than asserting it;
reading the function's own REPORT lines, which separated init (about 0.65 s) from handler time (22-26 s) and put a count on the
pool warnings.
**What failed:** nothing in the act. One finding that is not a failure of the act but of its premise: the box measurement's 8.5-9.2 s
cold request does not reproduce on Lambda (26.1 s after quiet vs 26.2 s before), while pool warnings went 78 -> 0 and warm
requests got faster. The half had said the box could not show the Lambda effect.
**Gap found:** the cold cost on Lambda is not the pool-full path (0 warnings, handler time unchanged); stated in the instance for the
issuer's close.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Replay first after the apply, thesis capture second | the arm asks for the FIRST overlay request after the apply; a 95-name capture would have warmed the function |
| A simultaneous pair for the cold arm | a sequential pair warms the second name (ADBE read 0.94 s as position 3 in the baseline) |
| Recorded the 27.81 s reading, did not call it a pass of "under 27 s" | the half defines the 27 to under 29 s band as RECORDED; the margin was not met and the record says so |

## Files Modified

- `org/critical_paths/change_management/20261012T0406Z_amgt-resapp-r101-bg3-s3client-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the derived compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit a33bcba12c)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_bg3/thesis_pre.json`, `.scratch_bg3/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` Round 101's day-after read (invocations over 20 s and pool warnings against 53 and 49) grades the cell; this act's window shows warnings 0 and the cold handler time unchanged.
2. `[2.0.0_SA_COO~R1]` Remove the pin worktree; `C:/tmp/bg3-build` is the user's to clear (a recursive deletion).
3. `[box-sync / MSTR]` Push the local commits.
