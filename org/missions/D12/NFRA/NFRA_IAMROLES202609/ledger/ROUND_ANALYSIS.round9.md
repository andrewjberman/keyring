# NFRA_IAMROLES202609 -- ROUND-9 ANALYSIS: THE CLOSE

**By:** `1.0.0_SA_CTO~Z`, 2026-10-13 ~07:2xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33579,
`surprise-channel/remediations/REMEDIATION_v9.Z.md` @b589e3fad0 (MAY-CLOSE, 6 of 6 graded). **On:** Andrew-direct
2026-10-12 ~20:5xZ, item 1, VERBATIM: *"Dell boxes should not be curtailed. Is there further work slated on this project? I
think this one can be wound down/closed."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`. Route:
round-8 Addendum 2.

## Round 9, as read

All 6 orders are COMPLETE: z-1, z-3, z-5 and z-6 PASS; z-4 FAIL narrow; z-2 PASS bounded.
- **z-2's live leg passed twice.** Both post-delete bd chains read 29 of 29 keys fresh: 23:03Z to 01:12Z, and 04:03Z to
  06:14Z (`0.7.0_AE_CloudOps~IR` msg 33573, `round9/schwab/POST_APPLY.md` sections 4e and 4f @7ff6c7bdf7).
- Its NEVER-2 entry is CLOSED. Branch B did not occur, and the rollback was not used.

## Every outcome, graded at the close

| FWD | grade | where |
|---|---|---|
| FWD-1 the posture as a number | **REALIZED** | round 4, u-1 |
| FWD-2 never-used permissions per role | **REALIZED** | round 3 |
| FWD-3 what a policy requires of the caller | **REALIZED** | round 4, u-3 |
| FWD-4 every role in code or recorded with an owner | **REALIZED** | round 6. At the close, 16 of 16 rows are owned: 8 declared, 5 exempt, 2 deferred with a reopen condition, 1 retired, 0 unowned (slug v9) |
| FWD-5 narrow a permission and know beforehand what breaks | **REALIZED** | round 5 |
| FWD-6 a past clean-up can be checked | **REALIZED** | round 3 |
| FWD-7 unused vs unobservable | **REALIZED** | round 3 |
| FWD-8 re-run without hand work | **REALIZED** | round 4, u-2 |

**8 of 8 REALIZED.** Rounds 7 to 9 went beyond the endpoint as enrichment. They removed live grants on dead or claimable
names (x-2, x-5 with 12 ARNs, z-1, z-2 and z-3: 17 dead ARNs across 7 roles), deleted 2 policies, and unfroze the portal
yield curve (z-6).

## What outlives the project

Every row the slug carries keeps a live owner, and none is owned by the ended issuer `2.0.0_SA_COO~ZI`. In particular:
- **Z-C-S47 (z-4 FAIL):** the `opal*` creation grant becomes a constrained creation grant once a full CloudTrail census
  exists. Owner `0.7.0_AE_CloudOps~Z`.
- **Z-S44:** the S3-staged builder copies of 2026-06-29 still read `opal-data-schwab`. Owner `0.7.0_AE_CloudOps~Z`.
- **The R20 bridge (Z-S34, cutoff 2026-12-31):** carried by this seat.

Round-8 Addendum 1 (the dell agents' invoke narrowing) stays WITHDRAWN on Andrew's word.

## The CLOSE: ruled here; the flip waits on one artifact

The CTO rules the project CLOSED. The mechanical flip to `dep_stage: CLOSED` needs both close documents, and the R6 rule
in `.tools/missions-tree-index.py` refuses without them:
1. the COO's `ledger/COMPLETION_REPORT.round9.json`, written by a `2.0.0_SA_COO` lane. Round 8's report is also invalid
   against the schema.
2. then this seat's `ledger/COMPLETION_GRADES.round9.json`.

The issuer `2.0.0_SA_COO~ZI` has ended. Until a COO lane writes (1), the row reads `status: closing`,
`dep_stage: ROUND_CLOSE`. No work remains; only the paperwork does.

-- 1.0.0_SA_CTO~Z
