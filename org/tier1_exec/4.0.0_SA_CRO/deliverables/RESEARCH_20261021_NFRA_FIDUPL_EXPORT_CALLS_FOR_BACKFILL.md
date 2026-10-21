# RESEARCH 2026-10-21 -- NFRA_FIDUPL: export/backfill calls present vs absent in the HARs (names only)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 2.0.0_SA_COO~P1 msg 8918.
**Scanned:** all five Wealthscape HARs on dell1 (off git). Names/methods/body-key-names only; no values.

## Probe 1 -- standing-export retention (REPLAYABLE now; fully captured)

The Export Status list and download are both plain calls (HAR 3; documented in
`RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` section 5b):
- **List:** POST `/ssc/importexport/wc/channel/status/v1/status.json`, body keys `iEtype` (="E"), `dateString` (="YYYY-MM-DD"),
  `startPage`, `pageLength`. Returns `statusElements[]`, each with `fileType`, `fileName`, `profileId`, `requestId`,
  `fileStatusDescription` (COMPLETED), `fileCreatedTimestamp`, `fileDeliveredTimestamp`.
- **Download:** GET `/ssc/importexport/wc/channel/export/v1/downloadExport.do?fileName=&fileType=&profileId=&requestId=` (the four from
  the list row).
- **Retention ceiling:** the Export Status calendar reaches **120 days** back for files already generated. **Replay from the signed-in
  context, stepping `dateString` day by day; classify SERVED / EMPTY / REFUSED.** No new capture needed.

## Probe 2a -- transaction backfill WITHOUT a file export (REPLAYABLE; the useful find)

The on-screen transaction query IS captured (HAR 1/2) and takes a **custom date range**:
- POST `/ssc/transaction-history/wc/channel/api/v1/historical-transactions`, body keys include `timePeriodOption`,
  `customTimePeriodFromDate`, `customTimePeriodToDate`, `accounts` (array of `{accountNumber, accountSource, lineOfBusiness}`),
  `dateField`, `searchBy`, `cmType`, `currencyCode`, `securityId`, `transactionType`, `excludeCoreBrokerage`.
- Set **`timePeriodOption` = custom** and the two `customTimePeriod*Date` keys to pull any range. It returns `transactions[]` as JSON
  (the shape in the endpoint map). **This is a replayable adapter for transaction backfill**, stepping the from-date earlier until empty.
  Caveat: it is **per account** (`accounts[]`), so the whole book is many calls -- the COO can drive it per G / per account batch, or use it
  only to reach dates older than the file export serves.

## Probe 2b -- the file-export CREATE + the Historical export (NOT captured; this is the gap)

**No HAR contains the export-CREATE / run-submission call, nor the Historical Prices and Positions export.** The wizard's "Create File"
submission and the Historical export ran in pop-up windows that were never recorded (Andrew's step-4 was a screenshot, not a HAR). So:
- **The create-a-run call cannot be built as an adapter from existing captures.** To build it, we need ONE fresh capture of a Custom
  on-demand export being created with an earlier from-date, and of the Historical Prices & Positions export, with pop-up DevTools on.
- That capture can come from **the box's own wizard navigation** (the signed-in agent-driven Chrome walks the wizard and we record its
  calls) **or from Andrew** (one on-demand export + the Historical export with "auto-open DevTools for popups").

## Recommendation to the COO

1. **Cut probe 1 now** (status.json day-by-day + downloadExport.do) -- fully specified, replayable.
2. **For transactions older than the standing files, use probe 2a** (historical-transactions, custom range) as a replayable adapter.
3. **For the file-export create and the Historical (positions/balances) export, capture first** -- have the box's agent-driven Chrome walk
   the wizard once and record the create call; if that navigation can't be built, THAT is the one step to bring to Andrew (a single
   pop-up-DevTools capture). Until then, positions/balances backfill beyond the 120-day Export-Status window is unspecified.

## Not measured

- The export-create request and the Historical export (absent from all HARs; need one capture).
- Whether `historical-transactions` custom range has its own max look-back (the empty/refusal response will show it).

## Addendum (~14:16Z): the historical-transactions custom-range parameters (CTO 9100)

From the transaction-history JS bundle and the captured calls (names/enums only):
- **`timePeriodOption`** values (bundle `InputOptionModel`): `daysPast1, daysPast5, daysPast10, daysPast15, daysPast30, daysPast60,
  daysPast90, currentYear,` **`custom`**. For a backfill range use **`custom`**.
- **`searchBy`**: the captured calls use **`none`** (= no sub-search; the whole account). Other enum values seen: `cashManagement` (a
  filter). **Use `searchBy="none"`** for a full pull.
- **`dateField`**: `T` (trade date), as captured.
- **`customTimePeriodFromDate` / `customTimePeriodToDate`**: the range. Format not shown in captures (the captured calls were daysPast/
  currentYear with these null); it is almost certainly `MM/DD/YYYY` (matching the Historical export's `historicalDate`). Confirm on the
  first call.
- **`accounts`**: `[{accountNumber, accountSource:"BROK", lineOfBusiness:"IWS"}]` per account.
- Optional: `excludeCoreBrokerage` (bool), `cmType`, `currencyCode`, `securityId`, `transactionType` (null for a full pull).

**Full body for the probe:** `{timePeriodOption:"custom", customTimePeriodFromDate, customTimePeriodToDate, dateField:"T", searchBy:"none",
accounts:[...], excludeCoreBrokerage}`. P1 resumes the per-account transaction floor probe on this.
