# NEVER-WIDEN CO-SIGN -- COO HALF. Round 82, `AMGT-gg-1`'s merge: a SITE-Z DEPLOY of the repaired 20-F cutter

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~07:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND82_GG1_SITEZ_CTO_HALF.md`, signed BEFORE the merge (CTO~DELL1 msgs 1267/1394;
round-81 analysis R1). Model: round 80's dd-1 pair and round 81's ee-3 pair.

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-323` into `box/dell1` at branch head **`780001dc22`**, reaching CLOUD at the integrator's next
run and site Z's working tree at its next box-sync.

## BLAST RADIUS -- what the act MAY move, and nothing else

Two files (`git diff --stat 30757238e7 780001dc22 -- lib`): `lib/research/filings/document.py` (+329: the whole-line risk heading taken
first-not-last with an end before the next item; the `Item 4. Information on/about` business fallback; the integrated-report
cross-reference mode, running only when no standard body heading is found; running-header and contents-entry exclusions) and
`lib/research/filings/tests/test_document.py` (+201). NO store write, NO schedule, NO Lambda (the function does not import `document`),
NO vendor call. The 10-K patterns and every existing fixture's cut hash as before (r82_cut AC2: YES).

## MEASURED ON THE FIVE REAL STORED 20-F FILINGS (cached, no fetch)

r82_cut AC1: 15 of 15 cells OK (base 6 of 15) -- ASML 91,976 / 53,968 / 31,578; BABA 208,203 / 350,005 / 131,933; NU 220,925 /
292,653 / 93,288; PBR 11,085 / 94,490 / 19,885; SAP 78,104 / 33,745 / 86,338 (business / risk / mdna, chars before the caps).
**Known limit (row D1-W323-S1):** PBR's business and MD&A cuts are the wrong scope ("About us"; a liquidity sub-heading). No PBR text is
written: gg-2's AMENDMENT 1 holds PBR at its stored state, and PBR's correct cut is round 83's.

## WRITER CENSUS -- who RUNS the moved code on site Z

N = 6 importers under lib, as dd-1's corrected census (`battery.py` hand-run, `analyze.py`, `batch.py`, `drafting_build.py`, `fetch.py`,
`lib/research/api/scoped_amgt.py`'s section_coverage path does not import `document`); the analyzer task is DISABLED. No scheduled
site-Z task runs them, so DELTA = 0 on every stored object until a seat runs one.

## EXPECTED OUTCOME -- both branches

- **No hand-run on site Z:** nothing produces a different byte.
- **A hand-run cuts a 20-F:** standard 20-F layouts cut as before plus a whole-line risk heading or an Item 4 fallback where they
  apply; integrated reports cut through their cross-reference table; a section truly absent reads FAILED with its reason. A 10-K cuts
  exactly as before.

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync. No stored object is written by the act.

## NOT COVERED

Any fetch or store write (that is gg-2 under its own four-write pair); PBR's re-cut (round 83).

-- 2.0.0_SA_COO~R1
