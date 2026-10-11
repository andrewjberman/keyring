# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-ff-5: SAP's stored driver on the unit's scale

**Date:** 2026-10-11 (GO 13:05Z; step 1 13:11:38Z; amended AC1 re-run and ledger closed after msg 3890)
**Task Order:** AMGT_RESAPP.TO-AMGT-ff-5.reverify-and-splice-sap-on-the-units-scale
**Status:** COMPLETE (AC1 as amended and AC2 PASS; ledger CLOSED 8 of 8)

## Objective

Round 93 left `SAP_GY_Equity` with 0 points (a mixed-scale set held whole). `AMGT-ff-3` shows such a set on the series unit's
scale when the filing states the conversion. Two ordered store writes for ONE name: the analysis object, then the drafting
object.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin (blobs 3 of 3, ff-3 an ancestor); recorded the VersionIds of all 24
   objects of the 12 names (SAP's two equal the half's); swept every live worktree.
2. Re-ran the day's table (`r94_rescale_table.py`: SAP 0 -> 3, 11 equal) and the 12-row dry re-verification. Printed the
   three points with their stated and shown scales and read them against the filing's own words (2024 stated on both scales).
3. Step 1: 0 -> 3 points. Step 2 dry run: `served_validator=True`, moved keys the two. Step 2 write: `SPLICED 1 of 1`.
4. Re-headed all 24: 2 VersionIds moved, 22 unchanged; drafting diff only the two keys; served SAP 0 -> 3, ASML 0, BABA 2.
5. AC1 as written read NO, and so did `r94_locator.py` L5: the production re-verification is not idempotent on a rescaled
   point. Reported with the cause; the CTO ruled ACCEPT; the issuer amended AC1 to read the served route against the table;
   re-run literally at the amendment: YES.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L8, close | PASS | opened before step 1 |
| r94_rescale_table.py | the GO-day table | PASS | T1, T2 |
| analyze.reverify_stored_thesis_driver | dry x12, write x1 | PASS | 12 of 12 equal the table |
| drafting_build --splice-driver | dry, then write | PASS | SPLICED 1 of 1 |
| r92_driver_reverified.py / r94_locator.py | AC1 as first written; locator | NO | defect D1-S24, not a state defect |
| r94_sap_served.py / r89 checks | amended AC1, AC2 | PASS | exit 0 |

**What worked:** printing the points' stated and shown scales against the filing before step 1 (round 91's lesson applied);
re-running the verifier from the pin as well as the shared tree, which showed at once the cause was not the checkout.
**What failed:** nothing in the act. The check I was given re-ran a non-idempotent verifier on the object the act wrote.
**Gap found:** row D1-S24: the verifier does not read `stated_value`. Until the round-95 cell lands, SAP's analysis object
is not re-verified by anyone; this seat ran only dry runs after step 1.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Re-ran AC1 and the locator from the pin as well as the shared tree | a NO from one checkout could have been a stale tree; the same blob in both removed that doubt before I reported |
| Did not roll back on the NO | Branch 2 had no trigger; the served state was the signed Branch 1 and the verifier, not the object, was wrong |
| Wrote the do-not-re-verify statement into the closing leg | the CTO's addendum asks for it in the entry, and a hand-run producer command is the failure mode |

## Files Modified

- `org/critical_paths/change_management/20261011T1310Z_amgt-resapp-r94-ff5-sap-rescale-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` VersionId record, pre-act drafting bytes, the finding,
  the proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[1.0.0_SA_CTO~DELL1]` Round 95's first cell: the verifier locates a stated_value point by its stated form (D1-S24).
2. `[2.0.0_SA_COO~R1]` ff-4's GO; AMGT_CORPUS's leg p (dossier /12) rides it. 3. `[box-sync / MSTR]` Push the local commits.
