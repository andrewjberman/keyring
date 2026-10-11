# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-ss-4: SAP's stored driver re-verified under the scale rule

**Date:** 2026-10-11 (GO 11:44Z; step 1 11:48:21Z; ledger closed after AC1/AC2)
**Task Order:** AMGT_RESAPP.TO-AMGT-ss-4.reverify-and-splice-sap-under-the-scale-rule
**Status:** COMPLETE (AC1 and AC2 PASS; ledger CLOSED 8 of 8)

## Objective

Round 92 held `SAP_GY_Equity` out of the stored-driver write because its three verified points mix EUR millions with EUR
billions. `AMGT-ss-2` makes the verifier hold such a set whole; this act writes that result for ONE name: the analysis object
then the drafting object.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin (blobs 3 of 3, ss-2 and qq-3 ancestors); recorded the VersionIds of all
   24 objects of the 12 names before any write (SAP's two equal the half's).
2. Re-ran the day's table: `r93_scale_table.py` (11 equal, SAP 1 -> 0) and the 12-row dry re-verification (equal to the
   table 12 of 12); the dry splice before step 1 moved only the provenance key.
3. Step 1 (SAP only): 1 -> 0 points, 3 held. Step 2 dry run: `served_validator=True`, moved keys the two. Step 2 write:
   `SPLICED 1 of 1`.
4. Re-headed all 24: 2 VersionIds moved, 22 unchanged (ASML's and BABA's included); drafting diff only the two keys; served
   SAP 1 -> 0, ASML 0 -> 0, BABA 2 -> 2. AC1 YES (R1, R2, R5), AC2 YES.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L8, close | PASS | opened before step 1 |
| r93_scale_table.py | the GO-day table | PASS | T1, T2 |
| analyze.reverify_stored_thesis_driver | dry x12, write x1 | PASS | 12 of 12 equal the table |
| drafting_build --splice-driver | dry, then write | PASS | SPLICED 1 of 1 |
| r92_driver_reverified.py / r89 checks | AC1, AC2 | PASS | exit 0 |

**What worked:** the pre-act record of every object's VersionId made "ASML and BABA untouched" a compare and not a claim;
AC1's instrument already took `--write-set`, so round 92's lesson held without an amendment.
**What failed:** nothing.
**Gap found:** none new.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Recorded all 12 names' VersionIds, not only SAP's | bound 8 says ASML and BABA are not touched; a read-back is the proof |
| Stated the sweep's one hit as my own old checkout | a printed hit left unexplained reads as another seat's open deploy |

## Files Modified

- `org/critical_paths/change_management/20261011T1147Z_amgt-resapp-r93-ss4-sap-driver-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the VersionId record, pre-act drafting bytes, proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~R1]` Round 93 close. 2. `[1.0.0_SA_CTO~DELL1]` Round 94's first cell (D1-S23). 3. `[box-sync / MSTR]` Push
the local commits.
