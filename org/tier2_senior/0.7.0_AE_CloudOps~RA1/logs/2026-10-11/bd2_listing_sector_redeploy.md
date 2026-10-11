# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-bd-2: the withheld listing's own sector served by listing key, compare equals the table

**Date:** 2026-10-11 (GO 20:14Z, msg 4096; baseline 20:40-20:46Z; apply 20:47:18Z; function LastModified 20:47:47Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bd-2.redeploy-the-scoped-api-carrying-the-listing-sector-on-the-scratch-pin
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10)

## Objective

One code redeploy of `opal-amgt-scoped-api` at build pin `08d5ea2920` (the scratch branch `scratch/r97-bd2-pin`, PARENTED on the
live build input `b3512d18fb`, plus exactly `scoped_amgt.py` and `monthly_chatter.py`): where a table row is withheld, the entry
carries the listing's own sector read from its stored model block by key, with its source and as-of date. Read against the
pair's 41-path table.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin by name: on the scratch branch, parent equal to `b3512d18fb`, the diff exactly
   two files. Detached worktree at the pin; `r94_admission_table.py --pin b3512d18fb` showed the two members at the half's blobs;
   the naming replay read YES (81 calls, 0 differ).
2. Captured the rollback package (hash-checked equal to the live CodeSha256), re-hashed the wheels (6 of 6), read the source-map
   entry and swept every live worktree's open deploys (60 worktrees, 1150 entries). One entry in the shared tree is not mine:
   C1's `amgt-corpus-r47-aw3`, OPEN, re-writing the 95 research dossiers at /13. The pin's `dossier.py` (byte-equal to the live
   package's) picks among /12 objects while any exists, so it is not served; stated in the ledger and to the issuer.
3. Built at the pin offline: 408 files, CHANGED 2, ADDED 0, off-list 0, both changed members byte-equal to the pin.
4. Ran the four table scripts and the sector census in local mode against the pin worktree: 0 + 8 + 24 + 9 = 41 paths = the half.
   Recorded a 527-request baseline immediately before the apply.
5. Uploaded with read-back, planned untargeted and read the plan JSON (1 of 53), applied through `safe-apply`, sent the CodeSha256 and
   apply time at once, replayed the baseline and compared path by path: 41 paths, 28 clock paths, 0 corpus, 0 outside.
6. AC1-AC3 PASS; the record step; the ledger closed; both scratch branches read after the apply.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin, --pin b3512d18fb | PASS | 2 members; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| r94_*_table.py x3, r95_series_by_ticker_table.py, r97_sector_serve_census.py --where local | prediction | PASS | 41 = the half; 6 of 6 |
| aa5_capture.py | capture, replay, compare | PASS | the instrument the scripts cannot be after an apply |
| r97 / r95 / r94 / r89 / r92 checks | AC1-AC3 | PASS | exit 0 |

**What worked:** the aa-5 instruments and ledger shape reused without edits; reading the in-flight AMGT_CORPUS write against the pin's
own pick rule instead of holding the act or ignoring the entry; the compare read the as-of dates against the stamps the census
read from S3.
**What failed:** nothing in the act. One note: the prediction's 24 series paths and the ranked-list script's 6 series paths are the
same SAN FP series asked two ways, counted once.
**Gap found:** none new.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceeded with C1's aw3 entry open | half condition 4 is about objects the routes serve; the /12 pick rule never serves a /13 object while a /12 one exists; a corpus-class path in the compare would have been a STOP, and there was none |
| Sent the CodeSha256 before the compare ran | the GO asks it for C1; a STOP would go to the same seat first |
| Left the scratch branches in place | GO condition 3: the deployed bytes stay reproducible from a ref |

## Files Modified

- `org/critical_paths/change_management/20261011T2015Z_amgt-resapp-r97-bd2-listing-sector-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit f72641b968)
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~C1]` Post-act read against the function this act leaves; their /13 redeploy must carry bd-1's two blobs unchanged.
2. `[2.0.0_SA_COO~R1]` Keep both scratch branches until the merged-pin redeploy supersedes them; `C:/tmp/bd2-build` is left in place for the user to clear (a recursive deletion).
3. `[box-sync / MSTR]` Push the local commits.
