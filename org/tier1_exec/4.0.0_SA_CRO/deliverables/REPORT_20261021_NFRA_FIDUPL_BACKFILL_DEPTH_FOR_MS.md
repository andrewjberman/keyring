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
