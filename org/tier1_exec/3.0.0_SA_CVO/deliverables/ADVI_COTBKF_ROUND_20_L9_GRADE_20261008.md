# ADVI_COTBKF round 20 -- L9 grade of CB20t2-AC3 (the rule (b) entry)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~18:4xZ. **Order:** `ADVI_COTBKF.TO-CB-t-2` (chain drained @16f0103204).
**Criterion (verbatim):** "the (b) entry's source line is the custodian's own designation of a core position (or its absence is stated
and the entry is off), and no MMF listed by census alone was added." **Ruling it applies:** `1.0.0_SA_CTO~DELL2` round-19 analysis
@c015b6de3d section 1 ("E2 records the custodian's designation as the source line. If no designation can be cited, the entry does not
land and the cell says so").

## Verdict: MET

1. **The designation half.** `deliverables/0.9.0_WK_ADVI_COTBKF~41/v2/sweep_regrade.md` states 316067107 OFF with
   `designation_source = None`. It also names the places searched:
   - the silver transactions fields: `Position_Type` reads CASH on 1,408,059 of 1,416,497 rows, for every security;
   - the silver positions fields;
   - the repo, by CUSIP and by "core position".

   It cites the round-19 CTO and CVO documents as behavior-based, which is the census, not a designation. That reading is right: my
   round-19 grade measured behavior only and named no custodian source.
2. **No MMF added by census.** sweeps-v2 holds exactly the two rule (a) members, FDIC66606 and FDIC66853, each sourced from its vendor
   description. The MMF behavior census is printed as a list only.
3. **This seat's own check.** I scanned the cached custodian extracts the chain reads for any column value naming core or sweep, and
   found none (dell2, `.scratch/advi_cotbkf/cache/`):
   - holdings: 1,452,421 rows; columns date, account_id, asset_name, ticker, units, cusip;
   - positions: 469 rows;
   - accounts: 994 rows.

## For the analysis (not part of the grade)

A designation, if one exists, sits outside what the chain reads: a custodian statement or account agreement. 316067107's first row is
2023-03-17 in every holding account, which is consistent with a custodian-level core selection on that date. That date is the place
to look in any statement set the laptop holds. The classing also bounds the stake: only 16 of the 163 D2-S29 movers hold 316067107, so
rule (b) can move at most 16. The 147 `neither` movers need their own cause.
