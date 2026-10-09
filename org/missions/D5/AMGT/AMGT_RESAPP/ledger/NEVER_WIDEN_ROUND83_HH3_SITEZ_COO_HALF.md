# NEVER-WIDEN CO-SIGN -- COO HALF. Round 83, `AMGT-hh-3`'s merge: a SITE-Z DEPLOY of the 20-F cutter's PBR repair

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~09:2xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND83_HH3_SITEZ_CTO_HALF.md`, signed BEFORE the merge. Model: round 82's gg-1
pair (COO @7b84cfc5a9, CTO~Z @83b31c3fa9, including its writer-census correction).

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-331` into `box/dell1` at branch head **`763c3051a1`**, reaching CLOUD at the integrator's next
run and site Z's working tree at its next box-sync.

## BLAST RADIUS -- what the act MAY move, and nothing else

Three files (`git diff --stat HEAD...763c3051a1`): `lib/research/filings/document.py` (+222 -4, cross-reference mode only: a
contents-page fallback for a section with no body heading, and whole-cited ranking for the business entry; both run only on a report
with 100 or more running page-header lines), `lib/research/filings/tests/test_document.py` (+109), and the worker's proof instance.
NO store write, NO schedule, NO Lambda (the function does not import `document`), NO vendor call.

## MEASURED (cached filings, no fetch)

- `r83_pbr --crit AC1`: YES -- PBR business starts at "Our Business" (offset 319,061, 'Exploration & Production'), risk at "Risks"
  (209,708, closed at the Cybersecurity heading 304,198), mdna at "Operating and Financial Review and Prospects" (549,928, ends 593,198);
  the other four names' 12 cells unchanged (12 of 12).
- `r82_cut --crit AC2`: YES (10-K and 20-F fixture hashes unchanged). Filings folder: 159 tests OK (stub fitz). Mutant control: with the
  new rules off, PBR falls back to "About us" and the liquidity sub-heading and AC1 reads NO.

## WRITER CENSUS -- who RUNS the moved code on site Z

As round 82 with 1.0.0_SA_CTO~Z's correction: direct importers `analyze.py` (lazy), `battery.py`, `fetch.py`, `section_census.py`;
through `fetch`: `batch.py`, `drafting_build.py`, `translate.py`, `management/proxy_officers.py`. All hand-run; the analyzer task is
disabled; no schedule or Lambda runs them. DELTA = 0 on every stored object until a seat runs one.

## EXPECTED OUTCOME -- both branches

- **No hand-run on site Z:** nothing produces a different byte.
- **A hand-run cuts a 20-F:** an integrated report with running page headers resolves a section with no body heading through its
  contents page (PBR: its real business and MD&A); every other 20-F and every 10-K cuts as before (AC1 P4, AC2).

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync. No stored object is written by the act.

## NOT COVERED

Any fetch or store write (PBR's store half is AMGT-hh-4's, under its own pair).

-- 2.0.0_SA_COO~R1
