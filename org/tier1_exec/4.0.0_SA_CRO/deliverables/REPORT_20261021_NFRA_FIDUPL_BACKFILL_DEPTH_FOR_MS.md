# REPORT 2026-10-21 -- Fidelity backfill depth (first answer), for Andrew via ms

**Author:** 4.0.0_SA_CRO~FIDELITY (dell1), compiling the COO's measured run. **Order:** ms on Andrew's word (bus 02abe551) to drive the
backfill empirically. **Measured by** 2.0.0_SA_COO~P1 run 6 (2026-10-21 11:20-11:22Z, one sign-in, exit 0); source record
`org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FIDUPL_backfill_standing_export_earliest_dates_20261021.md` @6fcf10981e7.
Dates/bytes only; no account data.

## Headline

**The standing (scheduled) export only reaches back ~3 business days -- to 2026-10-16 -- because the scheduled profile was created on
2026-10-19 and Wealthscape only retains files it has generated.** Deeper history requires the Historical export route, which the COO walks
next (12:05Z). This is the first answer; a second follows after that walk.

## Earliest business date actually landed, per file type

| File type | earliest content date landed | note |
|---|---|---|
| account | **2026-10-16** | |
| position | **2026-10-16** | |
| balance | **2026-10-16** | |
| prices | **2026-10-16** | |
| security | **2026-10-16** | |
| transact | **2026-10-19** | the 2026-10-16 transactions file timed out on three runs (a known one-day gap) |

Three export days served (dateString 2026-10-19 / 20 / 21), landing content dates 2026-10-16, 2026-10-19 and 2026-10-20.

## Volume landed (bytes, standing export, three days)

| type | 20261016 | 20261019 | 20261020 | ~total |
|---|---|---|---|---|
| account | 3,794,179 | 3,794,367 | 3,797,333 | 11.4 MB |
| position | 30,326,543 | 30,334,785 | 30,333,376 | 91.0 MB |
| balance | 1,223,747 | 1,221,776 | 1,222,782 | 3.7 MB |
| prices | 645,722 | 646,731 | 647,773 | 1.9 MB |
| security | 655,578 | 656,599 | 657,657 | 2.0 MB |
| transact | -- | 602,207 | 235,734 | 0.8 MB |

About **111 MB across the three days.**

## The hard limit, with evidence

- Run 6 stepped the export-status `dateString` earlier day by day: 2026-10-19/20/21 **completed** (five files each; transact skipped by
  option); **2026-10-16 EMPTY; 2026-10-15 EMPTY**; 2026-10-14 retention tried x3, empty.
- **The limit is not a Wealthscape look-back cap -- it is that the scheduled profile has only existed since ~2026-10-19**, so there are no
  generated files before 2026-10-16 to retrieve. The 120-day Export-Status calendar is there, but it is empty before the profile started.

## Older history -- the second answer (pending, no Andrew act assumed yet)

Two routes, the COO's read-only agent walk ordered for 12:05Z:
1. **Historical Prices & Positions export** (Service menu) -- for positions/prices history; its create call was never captured, so the
   walk records it.
2. **Per-account historical transactions** (the `historical-transactions` API with a custom date range) -- replayable per account for
   transaction history well beyond three days.
I will send ms the depth these reach, and name precisely any single step that genuinely needs Andrew (e.g. a one-time back-dated export
profile), once the walk lands.

## Plain answer to ms

Standing export backfill: **to 2026-10-16** (transactions to 2026-10-19), ~111 MB, limited only by when the scheduled profile was created,
not by a Fidelity cap. Deeper history is being measured now via the Historical export and the per-account transaction range; result to
follow.

## SECOND ANSWER (2026-10-21 ~12:21Z) -- deeper history, per route; NO Andrew act required

Measured by the COO's read-only walks (probe 2b `bfeb73497a`; probe 2a the captured transaction API). Full backfill depth by file type:

| Data | Route | Reach | Andrew act? |
|---|---|---|---|
| positions, balances, prices | **Historical Prices & Positions export** -- POST `/export/v1/historicalExport.json` (keys `profileId, profileName, exportFormat, historicalDate MM/dd/yyyy, fileFormat, fileTypes` PBL/PRC/POS, `indicatorName`); 3 saved profiles reusable | **~120 days** (today-120 to yesterday) | **none** -- create call is known/replayable |
| transactions | **per-account historical-transactions API** (custom `from/to` date range) | the API serves long ranges (the standing `.trn` already spanned ~5 months); exact floor measured by stepping back | **none** -- replayable per account |
| accounts, securities | no historical export exists (reference/slowly-changing data) | current snapshot only | n/a |

**Net backfill depth:** positions/balances/prices **~120 days**; transactions **at least ~5 months, likely deeper** (empirical floor to be
confirmed by stepping the API back); accounts/securities are current-snapshot reference data. **No step requires Andrew** -- both deep
routes are replayable from the signed-in session; the only unmeasured detail is where the Historical export's output lands and its exact
column layouts, which one live request settles (the CTO schedules it; the box can run it).

**Plain second answer to ms:** we can backfill positions, balances and prices ~120 days, and transactions several months (deeper on
measure), with no action needed from Andrew. Accounts and securities are reference data with only a current snapshot.

## THIRD ANSWER (2026-10-21 ~14:15Z) -- the 120-day cap is NOT a hard cap (measured)

A live probe (COO record @3131b59046) stepped the Historical export's `historicalDate` back past 120 days: positions served to
**2026-06-15 (~128 days)**, prices to **2026-06-18 (~124 days)**. Older dates (150..730) were **accepted, not refused** -- they returned
"COMPLETED WITH ERRORS, file does not exist." So there is **no artificial 120-day cap**: the backfill reaches as far as Fidelity actually
holds the data (~4 months for positions/prices), and simply runs out beyond that with "no file," never a refusal. 15 files landed over 8
dates; as-of = the requested date. Transactions depth is being probed next (the per-account custom-range call, parameters now resolved).

**Plain:** positions/balances/prices backfill ~4 months (data-availability limit, not a 120 cap); transactions depth to follow.
