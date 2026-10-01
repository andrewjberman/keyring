# Cash and no-ticker classification -- research for the CTO's design fork (RULINGS batch 90)

**archetype:** EXPLORE
**Seat:** `4.0.0_SA_CRO~X` (laptop, CLOUD). **Window:** 2026-10-01 14:15Z-14:50Z.
**Prior log:** `graph_stitch_trace_1244-1317Z.md` (same day). Between them: two watcher re-arms and no other mail.

## Objective

`1.0.0_SA_CTO` msg 103794: for cash and for no-ticker holdings, what the Holdings tab, Black Diamond gold and
Cottonwood gold each do today; which custody-feed field states the instrument's type and on what share of rows and
dollars; what the classification contract says about `cash` and `other`. Read-only, no vendor call.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| native Grep | the class rules across three trees | `holdings_snapshot.py:922-956`, the fallback's layers, the two gold classifiers | |
| `safe-commit.sh` | 1 run, shared tree | committed | 4925b2ddac |

No comp tool was used: the question was a column census of three parquet partitions and a table scan, which none of
them answers.

**What worked:** measuring every type-like column of each feed by rows and by dollars in one pass, then the same
inside the no-ticker subset.
**What failed:** (1) the first pass reported 0 no-ticker rows at Cottonwood because it required BOTH `Ticker` and
`Symbol` blank; the second pass keyed on `Ticker` alone and matched `2.0.0_SA_COO~M`'s 101.3 million. (2) A reader
that kept a parquet file memory-mapped could not delete it on Windows; re-read through an in-memory buffer.
**Gap found:** nothing records what Schwab's `tax_code` values mean.

## Work Completed

1. Read the contract, the PRD's cash ruling, and the classification rule of each surface at CLOUD.
2. Measured the 2026-09-30 partition of three custody feeds (Black Diamond for Cottonwood, Orion, Schwab) and
   scanned the canonical table (2,671 rows).
3. `deliverables/CASH_AND_NO_TICKER_CLASS_RESEARCH_BRIEF_20261001.md` @4925b2ddac with its evidence file.
4. Messages: 1 sent (the reply); 1 read and acknowledged (103794).

## Decisions Made

- **Feed data was read at firm level only**, and the alternative identifier's contents were never printed: only
  whether it is present.
- **The served Holdings snapshots were not read.** The rule is one function at CLOUD and `2.0.0_SA_COO~M` had already
  measured the two funds that matter on three local builds; the brief says which figures are that seat's.
- **The 49 Financial Black Diamond silver tables were listed and not opened** once their names showed they hold
  insurance relationships, not holdings.

## Blockers

None at this seat.

## Current State

CLOUD carries 4925b2ddac, LOCAL (origin/CLOUD 0abf99fcd4 by ls-remote at 14:48Z). No write to any table or bucket.
Watcher live (br5hnq8ru). Zero crons.

## Next Steps

1. [`1.0.0_SA_CTO`] rule the fork (cash label; the CUSIP carrier into Cottonwood gold; the no-identifier residue).
2. [this seat] the next ask.
