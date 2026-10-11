# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-qq-4: ASML and BABA stored drivers re-verified and spliced

**Date:** 2026-10-11 (GO 09:43Z; step 1 09:48:08Z; step 2 09:48Z; amended AC1 re-run and ledger closed after msg 3719)
**Task Order:** AMGT_RESAPP.TO-AMGT-qq-4.reverify-the-stored-drivers-and-splice-them-into-the-drafting-objects
**Status:** COMPLETE (AC1 as amended and AC2 PASS; ledger CLOSED 8 of 8)

## Objective

Two ordered store writes for the two names the pair's table changes: re-verify the stored thesis-driver points in the
analysis objects (`filings/v1`), then splice only `thesis_driver` and its provenance into the drafting objects
(`drafting/v1`). SAP_GY_Equity HELD (EUR millions beside EUR billions).

## The act
**archetype:** DEPLOY

1. Read both halves and the amended order; verified the run pin (blobs 3 of 3, qq-3 and pp-2 in the pin) and swept every
   live worktree's open deploys (0 naming either prefix).
2. Recorded the VersionIds of all 24 objects of the 12 names before any write. Re-ran the pair's dry run on the day:
   stored and expected points equal the table 12 of 12; changed set {ASML, BABA} plus the held SAP.
3. Step 1 for the two keys, step 2 dry run (served_validator=True, moved keys exactly the two), step 2 write
   (SPLICED 2 of 2) with the pre-act drafting bytes saved first.
4. Re-headed all 24 objects: 4 VersionIds moved, 20 unchanged; drafting diff only the two keys; served ASML 1 -> 0,
   BABA 0 -> 2, SAP 1 -> 1.
5. AC1 as written read NO on R1's "at least one expected-changed name" (empty after the write by construction). Reported;
   the issuer amended the check (`--write-set`); the amended AC1 re-ran literally on a checkout at the amendment and reads YES.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L8, close | PASS | entry opened before step 1 |
| analyze.reverify_stored_thesis_driver | dry run x12, write x2 | PASS | 12 of 12 equal the table |
| drafting_build --splice-driver | dry run, then --pre-act-dir write | PASS | SPLICED 2 of 2 |
| r92_driver_reverified.py | AC1, first-written then amended | NO then YES | the first form could not read YES post-write |
| r89 checks | AC2 | PASS | exit 0 |

**What worked:** recording every object's VersionId before the first write, so "no other key moved" was a 24-row compare
and not an assertion; running the splice dry run both before and after step 1 (before: only the provenance key would move,
which is why the driver itself moves only after step 1).
**What failed:** nothing in the act. The acceptance check had a state-dependent class that its own docstring half-states.
**Gap found:** an acceptance check for a WRITE should take the write set as an input from the start (now `--write-set`).

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not flip on AC1's first NO | the criterion as written did not pass; the equivalent evidence is mine to present, the waiver or amendment is the issuer's |
| Left leg L7 open until the amendment | a closed leg claims proof; the amended check was not yet in force |
| Wrote the pre-act drafting bytes into the deliverables folder | the rollback is by VersionId, but the bytes make the diff reproducible without the bucket |

## Files Modified

- `org/critical_paths/change_management/20261011T0947Z_amgt-resapp-r92-qq4-stored-driver-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the VersionId record, pre-act drafting bytes,
  the AC1 finding and the proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[1.0.0_SA_CTO~DELL1]` D1-S22 (the verifier rule for mixed scales), then SAP under its own pair. 2. `[2.0.0_SA_COO~R1]`
Round 92 close. 3. `[box-sync / MSTR]` Push the local commits.
