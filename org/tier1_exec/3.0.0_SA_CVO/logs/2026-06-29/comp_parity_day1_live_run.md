# comp-parity DAY-1 -- first live run (DATA_SSOTMG TO-4 cutover gate)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | COO-unblocked (xref fresh + gold exists -> drive day-1, don't wait)

## What ran
First live execution of the comp-parity engine (9a4f1b652) against real S3 data -- canonical/schwab/gold
06-24 vs BD-served 06-24, the G1 holdings surface, account-level market_value exact-tie.

## The architecture the run REVEALED: comp-parity is XREF-MEDIATED
- canonical account_id = Schwab-native `0010023253`; BD account_id = prefixed `z0812084971`. A RAW join = 0 matches.
- The engine CORRECTLY FAILed the raw join (n_compared=0) -- the keying-drift the design's keying-assertion was built to catch, confirmed real.
- Join path: account_xref (`schwab/silver/account_xref/date=20260629`, 6012 mappings) crosswalks `schwab_padded_id` <-> `bd_account_id`. So the FRESH-xref unblock is the prereq for the WHOLE per-account compare, not just the total-AUA gate -- without it nothing joins. **grounding: SOURCE-CONFIRMED** (the live parquet id-format samples + the xref schema).

## DAY-1 G1 result (xref-joined, account-level market_value)
- 5717 accounts compared. VERDICT **FAIL**: 2797 breaks the $1/1bp exact-tie. 177 canon-only / 294 bd-only.
- Engine ran end-to-end: load canonical + BD + xref -> grain-aggregate to account-level -> xref-join -> compare_exact_tie -> verdict. LIVE-PROVEN (not just unit-tested).

## 3 findings (the value of running day-1)
1. **Tolerance calibration:** most breaks are SMALL ($96/$121/$638 on $6-23K accounts) -- $1/1bp is likely too tight for holdings if canonical-06-24 / BD-06-24 priced on slightly different sources/times. Andrew owns the Class-A holdings tolerance number; the call is exact-tie-and-chase-the-small-deltas vs a small price-date band. **grounding: INFERRED (live-state-only)** -- the price-source-time hypothesis is not yet source-confirmed.
2. **A real DIG (-> DS):** account `0066026837` canon $651,546 vs BD $1,302,754 -- EXACTLY 2x. A likely BD-side double-count (dual-registration / lot-duplication). Routed to DS to ground. **grounding: INFERRED** -- the 2x is observed; the double-count mechanism needs DS source-confirm.
3. **Vintage alignment:** canonical 06-24 sums to $1.591B = the STALE-xref-era figure (06-24 gold built BEFORE the 06-29 xref repoint). Joining a stale-xref-built canonical via the fresh 06-29 xref => some of the 177/294 mismatch + breaks are xref-vintage drift. A CLEAN day-1 needs a POST-06-29 canonical run (canonical-vintage == xref-vintage). **grounding: SOURCE-CONFIRMED** (the $1.591B canonical sum vs the COO-stated fresh-xref $1.808B + the 06-24<06-29 build-vs-repoint dates).

## Streak
day-1 = FAIL -> streak stays 0 (correct). But this is a CALIBRATION+VINTAGE day-1, not a true parity-fail. The real clean-streak starts when (a) Andrew sets the Class-A tolerance, (b) a post-06-29 same-xref canonical runs.

## Next
- Andrew: the Class-A holdings tolerance number (exact-tie vs price-date band).
- base-DS: the `0066026837` 2x DIG + a post-06-29 canonical run (same-xref) to pair + the exact fresh-xref total-AUA figures.
- CVO: wire the remaining 10 surfaces' grain-aware loaders; re-run day-1 on the post-06-29 same-xref canonical; the total-AUA gate once base-DS hands the figures.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-parity (engine, live) | day-1 G1 xref-joined run | FAIL (2797/5717 breaks) -- engine LIVE-PROVEN end-to-end; 3 findings surfaced |
| live aws (s3/pyarrow) | canonical+BD+xref load, grain-aggregate, id-format ground | the keying-drift + xref-mediation + vintage findings |
