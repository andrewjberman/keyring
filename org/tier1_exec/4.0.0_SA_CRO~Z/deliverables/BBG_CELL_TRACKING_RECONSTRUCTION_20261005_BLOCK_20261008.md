# Bloomberg "cell" tracking: what was pulled on 2026-10-05 before the capacity block, in rows and in cells

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 31929; ruling msg 31939: returned records stays the ledger's unit,
cells is research). **Andrew's question,** from that message: "where we stand on the 'cell' tracking that i discussed with
CRO~Z, maybe there is a brief on it, essentially reverse engineering the rows and columns count that we pulled on the day
earlier this week when we got quota blocked on bloomberg."
**Read:** 2026-10-08 ~18:1x-18:3xZ, from records and stored outputs only. No Bloomberg call.

## Answer in four lines

1. **The discussion was not recorded** anywhere I searched, and there is no brief on it. This is the first write-up.
2. **Before the block at 07:06Z on 2026-10-05, at least 182,807 holdings rows were returned in about 90 minutes**
   (05:3xZ to 06:55Z). Every row of that BQL holdings query is **16 columns** wide, so that is at least **2.92 million
   cells**. One run's draw (06:37Z) is unknown and not in either figure.
3. **The holding count per fund-date drives everything:** ACWI about 2,280 and IWM about 1,955 rows per date against
   IDVZ about 45 and PFOE about 24. The two index ETFs were 93% of the day's rows.
4. **Whether Bloomberg's daily capacity counts rows, cells or something else is not known.** Two readings of "cells"
   are possible (columns returned, or fields requested), and they differ by 8 times. Section 4 gives both.

## 1. Was the discussion recorded?

| Searched | Result |
|---|---|
| This lane's deliverables, handoffs and logs (`org/tier1_exec/4.0.0_SA_CRO~Z/`) for "cell" near Bloomberg, quota, capacity or BQL | none. The only "cell" hits are spreadsheet cells in unrelated notes |
| The same terms across the CRO, BG Terminal, MSTR, COO~RV and CTO folders (40 files listed) | none records a cell-count discussion with this lane; the hits are the 2026-10-05 incident records and the pacer note |

The conversation predates this session of `4.0.0_SA_CRO~Z`, and nothing from it reached a file. **Not recorded.**

## 2. What ran on 2026-10-05 before 07:06Z

Sources: the stored captures in `C:\bbg_backfill\` (read today), and the evidence lines of rows ETFS_RIVALS-Z-S20 to Z-S24
(`org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/`). The run log `C:\tmp\bbg_backfill_d13_stepA.log`
holds only the last run (it was overwritten), so the earlier runs come from the rows' evidence.

| Time (UTC) | Pull | Funds | Dates | Rows returned | Source |
|---|---|---|---|---|---|
| 05:43:35-05:44:09 | D12 Step A | IDVZ, PFOE | 189 (2026-01-02 to 10-02) | **12,820** (IDVZ 8,569, PFOE 4,251) | **measured today**: 190 capture files, 13,009 rows = 12,820 data rows + 189 header rows |
| 06:37 | D13 first chunk | ACWI, IWM | 2026-01-02 to 01-30 | **unknown** | crashed reading the sheet (Z-S21). The BQL query had already run in Excel, so it may have drawn capacity; nothing was kept |
| ~06:3x | probe, 2026-01-02 | ACWI, IWM | 1 | 4,240 (2,283 + 1,957) | Z-S21 evidence |
| 06:40 | D13 chunk, amended read | ACWI, IWM | about 20 | **76,859** | Z-S24 evidence |
| ~06:4x | probe, 2026-01-16 | ACWI, IWM | 1 | 4,233 (2,280 + 1,953) | Z-S22 evidence |
| 06:55 | D13 chunk, amend-2 build | ACWI, IWM | 20 | **84,655** | Z-S23/Z-S24 evidence |
| 07:06:37-07:06:50 | D13 chunk | ACWI, IWM | 20 | **0**: every date "Daily Capacity, request is blocked" | **measured today**: 20 capture files, 0 rows, the block text in `unfetched` |
| **Total before the block** | | | | **182,807 rows, plus the 06:37 draw** | |

Two counts from the time disagree with this: the incident message said "~170k rows", and `bbg_budget.py`'s header says
"about 175k BQL rows". Both are rounder and leave out the probes; the sum above is from the rows' own figures.

The budget ledger (`%LOCALAPPDATA%\opal_bbg_budget\`) did not exist yet: its first file is 2026-10-05 and its first
line is 19:58Z, a probe recording 0 rows. So nothing on the ledger describes the morning.

## 3. The width of a row

The query, measured from a stored capture:
`get(id(), name()) for(holdings(['IDVZ US Equity','PFOE US Equity'],dates=2026-01-02))`

It asks for **2 fields** and Bloomberg returns **16 columns** per holding row:

`ID, DATES, id().SOURCE, id().POSITION, id().POSITION_CHANGE, id().WEIGHTS, id().CURRENCY, id().REPORTED_MKT_VAL,
id().REPORT_DATE, id().ORIG_IDS, id().POSITION_TYPE, id(), name().SOURCE, name().POSITION_TYPE, name().ID_DATE, name()`

Every one of the 189 IDVZ/PFOE captures has 16 values per row. Row Z-S23 records the same width (16) for ACWI and IWM,
in a different column order per query.

## 4. Cells

| Reading of "cell" | Per holding row | 2026-10-05 before the block |
|---|---|---|
| **Columns returned** (what lands in the sheet) | 16 | **182,807 x 16 = 2,924,912** |
| **Fields requested** (what the query names) | 2 | 182,807 x 2 = 365,614 |
| **Rows** (the ledger's unit today) | 1 | 182,807 |

The 06:37Z draw would add to all three. At the ACWI/IWM rate (about 4,230 rows per date) a full 20-date chunk is about
84,600 rows, or about 1.35 million cells at 16 columns, so the unknown draw is between 0 and about that.

**What capacity Bloomberg actually meters is not established.** Nothing in the estate reads it. `READ_HERE.md` does not
mention a BQL daily capacity; row Z-S24 records it as undocumented. The block arrived while the refdata session reported
healthy, so BQL capacity is a separate limit from reference and historical data.

## 5. Each producer in rows and cells

| Producer (ledger `mode`) | Service | What one ledger "row" is today | Cells per row (columns returned) | Notes |
|---|---|---|---|---|
| rivalfunds holdings, `daily` and `backfill` (`collector_bloomberg.py`) | BQL holdings via Excel | one holding row returned | **16** | the producer the block came from. Rows per fund-date: IDVZ ~45, PFOE ~24, ACWI ~2,198-2,283, IWM ~1,953-1,979 |
| rivalfunds `market-range` (`enrichment_bloomberg.py`) | historical data, `PX_LAST` only | a point REQUESTED (security x trading day), not returned | **1** (one field) | records requested, not returned: the pacer note's open unit question (rows Z-S67, Z-S68) |
| rivalfunds `names` (`security_names.py`) | reference data, `LONG_COMP_NAME` | one security | **1** | refdata, not BQL |
| rivalfunds `market` / `daily` G4 (GICS, price, currency, return) | reference data | one security | the field count of the request (the module's `MARKET_FIELDS`; not counted here) | refdata |
| `etf_history_backfill` (2,929 rows on 2026-10-08) | not read | not read | not read | |
| AMGT_CORPUS 13:00Z fire (768 calls), OPAL_BBGTML notebooks, ETF daily pull | refdata and history | **not on the ledger at all** | not read | the pacer note records the CORPUS fire as recording nothing |

So converting the ledger to cells means a per-producer multiplier, and it also means deciding whether BQL and refdata
share one ceiling. As far as the estate shows, they do not: one block hit BQL alone.

## 6. What this suggests (for the ruling, not a ruling)

- **If cells become the unit, use columns returned for BQL** (the 16-wide holdings row), since that is what lands and
  what grows with the query's shape, and **fields x securities x dates for refdata and history**.
- **The number that would make a ceiling real is the capacity itself**, and nobody has measured it. The 2026-10-05 block
  gives a floor: about 183,000 BQL holdings rows, 2.9 million returned cells, in about 90 minutes, and possibly more.
  The reset was then probed hourly for over a day before a probe returned rows (the ledger's 0-row probe lines run from
  2026-10-05 19:58Z to 2026-10-06 11:58Z; the first non-zero probe is 12:29Z).
- **The single biggest lever is not the unit; it is the two index ETFs.** One ACWI+IWM date is about 4,230 rows (about
  68,000 cells); one IDVZ+PFOE date is about 69 rows (about 1,100 cells).

## What bounds this

- The 06:40Z and 06:55Z row counts and the two probes are the issuing seat's figures in rows Z-S21 to Z-S24; I could not
  re-count them, because those captures were not kept and the log was overwritten.
- Whether a row in those runs included a header row is not stated in the rows; the D12 figure (12,820) excludes headers.
- "Cells" here is my arithmetic on stored widths. It is not Bloomberg's definition of anything.
- The CTO's ruling (msg 31939) stands: returned records remain the ledger's unit until Andrew chooses otherwise.
