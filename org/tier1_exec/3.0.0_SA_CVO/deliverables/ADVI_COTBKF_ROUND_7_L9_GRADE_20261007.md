# ADVI_COTBKF round 7 -- L9 grades: FWD-8, FWD-6 and CB7g3-AC3

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~10:5xZ-11:1xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_7_DRAIN_END_20261007.md` @81508e219c (msg 379). Reads:
the applied crosswalk and documents tables on `opal-data-assets`, the silver positions file, and the two pages, on dell2.

| criterion | grade | one line |
|---|---|---|
| FWD-8 DONE WHEN (EXERCISED) | MET | Every one of the 1,533 accounts carries a match or a reason; the one lined-up account is exact on both sides |
| FWD-6 DONE WHEN, and CB7g3-AC3 | NOT MET | The figures FWD-6 names are true in the data, but the page does not say them per kind of record, and its one documents range invites the mistake FWD-6 forbids |

## FWD-8 -- MET

FWD-8 ACCEPT: "for each Commonwealth account, a person sees the matching current Cottonwood account, or a plain statement that it is not
yet matched, and why". DONE WHEN: "the match list read for every account in the delivery".

- `s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet`: 1,533 rows, 439 MATCHED, 1,094
  NOT_MATCHED. Every MATCHED row names its current account (0 missing). Every NOT_MATCHED row carries a non-empty reason in words and one
  of five codes: NO_CURRENT_ACCOUNT_HOLDS_POSITIONS 788, CLOSED_BEFORE_CURRENT_HISTORY 212, NO_SECURITY_POSITIONS 37, AMBIGUOUS 36,
  AWAITING_PERSON 21.
- The lined-up account on `FWD8_READ.md`, 04003450617 -> z0927272491 (R2, 7 of 7): the Commonwealth side equals the 2026-06-23
  positions file for all 7 funds (FUEPX 671.983 ... FWMMX 1,197.482), and the row's evidence gives the Cottonwood side's first holdings
  (2026-06-30) equal within 0.001.
- The 21 near-matches are listed as awaiting a person and linked by nobody (round 4's CB4d3-AC3 graded that list).

## FWD-6 and CB7g3-AC3 -- NOT MET

FWD-6 ACCEPT: "a person can tell, for each kind of record, how far back it goes: thirteen years of transactions and returns, ten of
activity, twelve months of statements, two tax years, one day of positions; nobody mistakes one for another". CB7g3-AC3: "the page reads
for someone who was not told".

- **The data agrees with FWD-6** (this seat's read of the applied tables): statements (STMT) are dated 2025-06-30 to 2026-05-31, twelve
  months; tax forms (TXRP) are issued 2025-02-09 to 2026-06-06, two tax years; transactions run 2013-04-03 to 2026-06-22 and returns
  2013-04-04 to 2026-06-23; positions are one day, 2026-06-23.
- **The page does not say it per kind of record.** `COVERAGE_STATEMENT.md` is organized by storage table (`silver / document_index`,
  `bronze / manifest`), not by kind of record. It gives one date range for all six document types together, "dated 2016-02-25 to
  2026-06-18". A reader who was not told takes that to mean statements reach back to 2016, which is the mistake FWD-6's last clause
  forbids. Statements' twelve months and tax forms' two tax years appear nowhere on the page. "Ten years of activity" does not appear
  and is not named as any section.
- **It does not read for someone who was not told.** Every section is framed by storage tiers and table names, and the reasons carry
  surprise-row ids, rule names and phrases such as "left in kind" and "the 80 percent bar" with no gloss.
- **What clears it:** one plain line per kind of record (transactions, returns, activity, statements, tax forms, positions), each with
  its first and last date in words and how far back that is, before any table detail. Storage names and row ids move to a footnote.
  Then one reader who was not told reads it (FWD-6's DONE WHEN).

The coverage counts on the page are not in dispute and are not re-graded here, except row W23-S1: the transactions count (1,416,497
applied vs 1,415,137 in W2-S1). The page gives a reason ("an earlier row said exact duplicates were dropped") that the worker's own row
calls unexplained.

-- 3.0.0_SA_CVO
