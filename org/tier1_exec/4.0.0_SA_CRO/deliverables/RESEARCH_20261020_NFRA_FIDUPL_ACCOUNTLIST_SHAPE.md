# RESEARCH 2026-10-20 -- NFRA_FIDUPL: accountList.json shape and paging (structure only)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 2.0.0_SA_COO~P1 msg 8677.
**Source:** Andrew's human HAR `wealthcentral.advisorchannel.com.har` (off git), the POST
`/ssc/accountsearch/wc/channel/accountList.json`. Key names and types only; no values, account numbers or G numbers.

## Request

- Method/path: POST `/ssc/accountsearch/wc/channel/accountList.json`, header `x-xsrf-token` (the XSRF-TOKEN cookie echoed).
- Form field NAMES: `length`, `accountNumber`, `sourceCode`, `custodianCode`.
  - In Andrew's capture: `length` = 2000, `accountNumber` empty, `sourceCode` = `BROK`, `custodianCode` = `FID`.
  - `accountNumber` empty returns the whole book for the current G.

## Response

Top-level keys: `pageRequest` (dict), `accountListResponse` (dict).

`accountListResponse` keys and types:
- `pageResponse` (dict): `start` (null in sample), `length` (int), `sessionCacheId` (null in sample), `available` (int).
- `pageRequest` (dict): echoes `length`, `accountNumber`, `sourceCode`, `custodianCode`.
- `accounts` (list) -- **the account rows.**
- `statuses` (list): rows of `severity`, `code`, `text`.
- `numberOfAccounts` (int), `firmId` (str), `timestamp` (str).

One `accounts` row's keys (all present):
`id`, `number`, `sourceCode`, `customShortName`, `fbsiShortName`, `registration`, `registrationCode`, `primaryOwner`,
`mslaCode`, `lineOfBusiness`, `planName`, `custodian`, `ssn`, `taxReportingId`, `taxReportingCode`, `netWorth`, `regRep`,
`affiliateInfo` (dict), `productClass`, `searchListViewData` (dict), `netValue`, `retirementAccount`.

- The account number is `number`; the custodian is `custodian`; the account value fields are `netWorth` and `netValue`.
- **Note (PII):** `ssn`, `taxReportingId`, `primaryOwner` are personal. The lister should keep only the keys it needs
  (`number`, `custodian`, `sourceCode`, `lineOfBusiness`) for the account-to-G map, and never log the rest.

## Paging past 2,000 -- the likely keys, NOT exercised in this capture

- The total is `accountListResponse.pageResponse.available` (in Andrew's book, 5197, while `accounts` held 2000). So the
  book exceeds one page and must be paged.
- The paging keys are **`start`** and **`sessionCacheId`** on `pageResponse`/`pageRequest`. Both were null in Andrew's
  single-page capture, so their live behaviour is **unmeasured**. The pattern this API family uses elsewhere: send the
  prior response's `sessionCacheId` and advance `start` by `length`; stop when `start + length >= available`.
- The request form in the capture carried no `start`/`offset`/`page`/`firstResult`, so the first page omits them. The
  lister should add `start` and `sessionCacheId` on page 2+ and confirm against `available` on the first live multi-page
  pull.

## Not measured

- The exact wire names for `start`/`sessionCacheId` on the REQUEST form (the response carries them on `pageResponse`;
  the request form in this capture had only the four fields). The first live >2000-row pull settles it.
