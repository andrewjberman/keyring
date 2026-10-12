# NFRA_CTLPLN PRD v0.28 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108610 (and msg 108611). 2026-10-12 ~15:4xZ.
**Verdict:** SIGNED.

## What was read

- PRD at 5a2b425 (v0.28), unchanged at HEAD. ratified-text half_hash `d9cecb0201a4887aba56e7120b73711ecff30c1c499b17d376d3d18fc434be53`.
- `git diff 0727ecb 5a2b425`: only FWD-28's class (ii) clause changes, plus the v0.28 addendum outside the section.

## Checks against the v0.27 refusal (review @67b765298a)

1. **Text matches code.** Class (ii) now reads "refuses any caller whose tier is not internal ... UNLESS its userType is Dev".
   That is `lambda_function.py:2112` at HEAD (`if tier == 'internal' or user_type == 'Dev'`), confirmed by printing the line.
2. **Named for what it is.** The text says the clause's "only reachable effect is to admit a Dev token on a non-Opal firm".
   "Defence-in-depth" is struck.
3. **Bounded in time and owned.** Removal at the next apply of this function (cell CT-aa-5, under a pair, round 11), and until
   then PRE-1's invariant (no Dev row on a non-internal firm) is the stated control. This is option (b) of the refusal.

## Notes (not blocking)

- PRE-1 is read at apply time, not continuously. Between applies the invariant is unmonitored. The window ends at CT-aa-5.
- The text now carries a code line reference and a version tag. Cut both when CT-aa-5 lands and the clause is gone.
