# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-aa-5: the withheld classification and the initialism casing redeployed, compare equals the table

**Date:** 2026-10-11 (GO 17:30Z, msg 4043; baseline 17:56-18:01Z; apply 18:03:15Z; function LastModified 18:03:44Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-aa-5.redeploy-the-scoped-api-carrying-the-withheld-classification-and-the-initialism-casing
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10)

## Objective

One code redeploy of `opal-amgt-scoped-api` at build pin `b3512d18fb` (the scratch branch `scratch/r95-aa5-pin`: the live pin
`15b7af1601` plus exactly `scoped_amgt.py` and `monthly_chatter.py`): a table row whose name disagrees with the registered name
serves no classification (SAN FP, CSL AU), CSL AU's series name stops being Carlisle's, and `CSL` and `JD` join the declared
initialisms. Read against the pair's 39-path table.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin by name: on the scratch branch, `15b7af1601` an ancestor, the diff exactly two
   files. Created a DETACHED worktree at the pin and ran the GO's instruments there: `r94_admission_table.py` (2 members at the
   half's blobs) and `r94_naming_replay.py` (YES, 88 calls, 0 differ).
2. Captured the rollback package (hash-checked equal to the live CodeSha256), re-hashed the wheels (6 of 6), read the source-map
   entry, and swept every live worktree's open deploys (59 worktrees, 1129 entries). One entry in the shared tree is not mine:
   C1's `amgt-corpus-r47-aw10`, a new key in `research_template`; the pin's `team_sheet.py` does not name that table and `/thesis`
   serves the stored dossier's team sheet, so it is outside this act's routes. Stated in the ledger and to the issuer.
3. Built at the pin offline: 408 files, 406 identical, CHANGED 2, ADDED 0, off-list 0, both changed members byte-equal to the pin.
4. Ran the four table scripts in local mode against the pin worktree: 3 + 6 + 24 + 6 = 39 paths = the half. Recorded a 527-request
   baseline immediately before the apply.
5. Uploaded with read-back, planned untargeted and read the plan JSON (1 of 53), applied through `safe-apply`, sent the CodeSha256 and
   apply time at once, replayed the baseline and compared path by path.
6. AC1-AC3 PASS; the record step; the ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin | PASS | 2 members; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| r94_*_table.py x3, r95_series_by_ticker_table.py | local-mode prediction | PASS | 39 = the half |
| aa5_capture.py | capture, replay, compare | PASS | ff4_capture plus series-by-ticker, coverage, compare of the movers |
| r95_classification_census.py, r95_casing_deployed.py, r94/r89/r92 checks | AC1-AC3 | PASS | exit 0 |

**What worked:** recording the baseline of every request the table names, including the 4 by-ticker series requests the ranked-list
script does not make, before the apply; reading the sentinel of another seat's open write against the pin's own bytes instead of
either ignoring it or holding the act.
**What failed:** my first wheel-record parse read a 0 denominator (the record carries a bytes column between hash and name); the 0
was printed beside the 6 and fixed before the leg was closed. A grep over a scratchpad glob was read by the rail as a repo search.
**Gap found:** the half's table counts 24 series paths for the by-ticker series; the ranked-list script also reports 4 paths for the
same SAN FP series. They are one set, not 28; the leg text says so.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceeded with C1's aw10 entry open | half condition 4 is about writes to this function or the stored objects the routes read; the pin's bytes show the packaged code does not read `research_template`; the entry and the reasoning are in L2 and in the issuer message |
| Counted the 4 list-series paths inside the 24 | same series (SAN FP, the two PRICE lists), asked two ways |
| Sent the CodeSha256 before the compare ran | the GO asks it for C1; a STOP would go to the same seat first |

## Files Modified

- `org/critical_paths/change_management/20261011T1732Z_amgt-resapp-r95-aa5-classification-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 91708f372b)
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~C1]` Post-act read against the function this act leaves; their round-47 corpus files wait for their own pair.
2. `[2.0.0_SA_COO~R1]` Keep `scratch/r95-aa5-pin` until a merged-pin redeploy supersedes it; the worktree `C:/tmp/aa5-build` is left in place for the user to clear (a recursive deletion).
3. `[box-sync / MSTR]` Push the local commits.
