# Fidelity backfill -- theory and plan (NFRA_FIDUPL), for Andrew via ms

**Author:** 4.0.0_SA_CRO~FIDELITY (dell1), 2026-10-21 ~12:25Z. **Order:** Andrew-direct via ms (bus 356885a0). Builds on the depth report
`REPORT_20261021_NFRA_FIDUPL_BACKFILL_DEPTH_FOR_MS.md` (2447db8557) and the probe records under `deliverables/2.0.0_SA_COO~P1/`.
Measured, read-only; (M) measured, (I) inferred.

## 1. Theory -- how Wealthscape serves history

Wealthscape exposes history through **three different surfaces**, with different reach, because the data has two natures:
- **As-of snapshots** (positions, balances, prices, securities, accounts) -- one state per day.
- **Event stream** (transactions) -- a dated flow.

The three surfaces:
1. **Standing scheduled export** -- retains only files it has already generated. Reach = from the day the scheduled profile was created.
2. **Historical Prices & Positions export** -- a built-in look-back for positions/balances/prices, ~120 days.
3. **Per-account transaction API** (`historical-transactions`) -- a custom date range for the event stream.

Accounts and securities are **reference/slowly-changing** data with no historical surface -- only a current snapshot.

## 2. What each source showed (measured)

| Source | Reach measured | File types | Evidence |
|---|---|---|---|
| Standing export (probe 1) | **3 days, to 2026-10-16** (transact to 10-19) | all six | 10-15 and earlier EMPTY; limited by the profile's 2026-10-19 start, not a Fidelity cap |
| Historical Prices & Positions (probe 2b) | **~120 days** (today-120 to yesterday) | positions, balances, prices only | create call read from page code: POST `/export/v1/historicalExport.json`, keys `profileId, profileName, exportFormat, historicalDate MM/dd/yyyy, fileFormat, fileTypes` (PBL/PRC/POS), `indicatorName`; 3 saved profiles |
| Per-account transactions (probe 2a) | **months+** (the standing `.trn` already spanned ~5 months) | transactions | POST `.../transaction-history/.../historical-transactions`, `timePeriodOption=custom` + `customTimePeriodFromDate/ToDate` + `accounts[]` |

## 3. Method (per file type)

- **Positions, balances, prices:** step the Historical export's `historicalDate` back day by day from yesterday to today-120; land each
  day under its content date in `fidelity/alongside/bronze/<type>/<YYYYMMDD>/`. One signed-in session; space the requests.
- **Transactions:** call `historical-transactions` with a custom `from/to` range per account (or per account batch), stepping the
  from-date earlier until the API returns empty; land by content date. Depth = whatever the API serves (confirm the floor empirically).
- **Accounts, securities:** no historical surface -- keep the daily current snapshot; no backfill exists (a product limit, not a gap we
  can close).
- **Classify every run** SERVED / EMPTY / REFUSED; never loop-retry; keep the inter-run spacing (the throttle lesson).

## 4. Expected depth per file type

| File | Expected backfill depth |
|---|---|
| position | ~120 days (Historical export) |
| balance | ~120 days (Historical export) |
| prices | ~120 days (Historical export) |
| transact | several months, likely deeper (per-account API; floor to confirm) |
| account | current snapshot only (no history surface) |
| security | current snapshot only (no history surface) |

## 5. The first concrete step

**Run one Historical Prices & Positions export for a single past date (e.g. yesterday)** from the signed-in box session, and observe where
its output lands and its column layout (the one unmeasured detail). That single run (a) proves the create call replays, (b) fixes the
lander's layout for the historical files, and (c) sets the loop that then steps back to today-120. In parallel, one `historical-transactions`
custom-range call for a sample account confirms the transaction floor. The COO owns these runs.

## 6. Does any single step need Andrew?

**No.** Both deep routes (Historical export, per-account transactions) are replayable from the signed-in session; no new Wealthscape
configuration, no Andrew click. The only thing Andrew could add later is **optional**: if we ever want positions/balances history **older
than ~120 days**, Wealthscape's Historical export does not serve it -- that would need a different arrangement with Fidelity (the official
feed), which is a business decision, not a pipeline step. Within the ~120-day / several-months reach, nothing needs Andrew.

## 7. Net plan

Backfill positions/balances/prices to ~120 days and transactions to several months, driven by the box per the method above, landed by
content date, reported back (earliest date per type, volume, the empirical floors). Accounts/securities stay current-snapshot. First step:
one Historical export run to fix layout + landing, then step both routes back. No Andrew act required inside this reach.
