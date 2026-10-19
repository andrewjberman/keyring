# RESEARCH 2026-10-19 -- Fidelity Wealthscape HAR: endpoint map, auth, data shape vs the Auto-Schwab loader

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Order:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1704Z_FIDELITY_WEALTHSCAPE_HAR_WALK.md`
**Risk class:** WORLD (vendor platform; read of a capture only, nothing sent to Fidelity) | **Status:** first pass, walk #2 requested

**Source:** Andrew's capture `wealthcentral.advisorchannel.com.har` (119 MB, 662 entries, 2026-10-19 17:08:26Z to
17:13:00Z): open the platform, search one Cottonwood client, walk that client's account dashboard. The HAR stays on
the dell1 box (`C:\Users\Test\Downloads\`). It carries live session cookies and client PII, and is never committed. This
file carries structure, field names and firm-level counts only. Analyzer: a stdlib redacting mapper in the session
scratchpad that prints field names and types only, never header, cookie or parameter values.

Prior pass on an older capture: `org/tier1_exec/1.0.0_SA_CTO/deliverables/WEALTHSCAPE_HAR_SCOPING_20260826.md`. The
custodian-feed background is in `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_CUSTODIAN_DIRECT_FEEDS_AND_FIDELITY_SAN.md`.

## 1. Headline

1. **The book is measured.** The book-of-business tile reads **4,959 open accounts, $1,563.1M assets under
   administration, as of 16-Oct-2026**. That is the T-1 business date on Monday 10-19, so Fidelity, like Schwab, serves
   prior-day close. `accountList.json` reports 5,197 accounts available (closed accounts included) and returns them
   2,000 per page. All 2,000 accounts on the captured page are custodian `FID`. 1,952 of them are line of business
   `IWS`, the rest FCS, FILI or PWI.
2. **This login is entitled to Fidelity's own file products.** The entitlement payloads (`siteEntitlements.json`,
   `containers.json`, `iws-container-webservice/services/entitlements`) name these features:
   - `Automated Bulk Download` and `Bulk Download`
   - `Portfolio Mgt Standard Export` and `Portfolio Mgt Custom Export`
   - `Positions Export` and `Historical Prices and Positions Export`
   - `Saved Exports` and `Import/Export Status`
   - `Integration Xchange_Transmissions`, `Integration Xchange_OutboundTransmissionsRulesManagement` and
     `Integration Xchange_AddOutboundTransmissionsRulesManagement`
   - `Integration Xchange_API`

   The last group is Fidelity's outbound transmission (the server-to-server file feed). This login appears able to
   view and add the transmission rules itself. An entitlement name is not an exercise: none of these pages was opened
   in this capture.
3. **None of the captured data calls covers the whole book.** Every positions, lots, transactions, balances and
   performance call takes one account number, or a list of account numbers. Pulling 4,959 accounts through these calls
   would mean roughly 20-30k requests every morning. The capture shows Akamai Bot Manager on the platform (cookies
   `_abck`, `bm_sz`, `bm_sv`, `ak_bmsc`, and sensor POSTs to an obfuscated path returning 202). The Terms of Use page
   `TOU_RIA.html` is also served. Treat per-account scraping as the fallback, not the design.
4. **Auth is not in this capture.** The first entry is already signed in: the request carries the session cookies
   (`ATC`, `FC`, `MC`, `RC`, `SC`) and its referer is `/container/home`. The login, any MFA and the device-trust steps
   were not recorded. The session limits it reports (`checkTimeoutTime.json`) are **4 h inactivity, about 10 h hard
   limit**. Schwab's `SDDSecure` refresh token has lasted about 10 months, so a Fidelity morning pull has to sign in
   every day. That makes the login flow the deciding unknown for the "same design" question.

## 2. Endpoint map (first-party, `https://wealthcentral.advisorchannel.com`)

Every data call sends the `XSRF-TOKEN` cookie value back as the `x-xsrf-token` header (or sends `x-requested-with`),
on top of the session cookies. `n` = calls in the capture.

| Family | Method + path | Request | Returns (grain) |
|---|---|---|---|
| Session | GET `/ssc/singlecontainer/wc/channel/app` | cookies | app shell; sets `XSRF-TOKEN`, `SSCSINGLECONTAINER`, `ATC` |
| Session | GET `/ssc/singlecontainer/wc/channel/checkTimeoutTime.json` | -- | inactivity / hard timeout seconds |
| Session | POST `/iws-container-webservice/services/createTkn` | -- | container token (`CONTAINERID` cookie) |
| Entitlements | GET `/ssc/menus/wc/channel/api/v2/{entitlements,siteEntitlements,containers}.json` | `entitlement`, `container` | what this login may see and do |
| Book | GET `/ssc/professional-platform-summary/wc/channel/v1/home/tiles/book-of-business` | `shouldExcludeClosed` | account count, AUA, as-of date (firm) |
| Book | POST `/ssc/accountsearch/wc/channel/accountList.json` | form: `length`, `accountNumber`, `sourceCode=BROK`, `custodianCode=FID` | **every account in the book**, paged 2,000: number, registration, owner, tax id, LOB, rep, `netWorth`, `netValue` |
| Book | POST `/ssc/accountsprofile/wc/channel/clientSearch/findClients.json` | paging, search name, scope | client (household) roster; 593 clients in "all clients" |
| Client | POST `/ssc/accountsprofile/wc/channel/clientSummary/getClientSummary.json` | clientId, paging | per-client account detail: about 90 fields (cash, MV, model, objective, rep, established date, custom fields) |
| Account | POST `/ssc/accountsearch/wc/channel/service/v1/verify.json` | accountNumber | account header: net worth, cash, margin, registration |
| Account | POST `/ssc/accountsprofilesummary/wc/channel/custprofile/customprofile.json` | number, custodian, source | profile: objective, model, address, contact |
| Balances | GET `/ssc/accountsbalances/wc/channel/balances/getbalances.json` | `AcctNum` | balance "bricklets" (display rows: closing, recent, change), account x as-of |
| Lots (open) | POST `/ssc/open-lots/wc/channel/api/v2/open-lots` | JSON `{accountNumbers:[...]}` | **open tax lots**: cusip, sedol, symbol, dateAcquired, quantity, market value, cost, cost/share, holding period, covered, wash flag |
| Lots (closed) | POST `/ssc/positions-apps/wc/channel/v1/previous-sales/retrieve-realized-gain-loss/{summary,detail}` | JSON `{accountNumbers, startDate, endDate}`, `offset` | **realized lots + per-security rollup**: acquisition/close dates, proceeds, basis, ST/LT gain, wash-sale amounts |
| Transactions | POST `/ssc/transaction-history/wc/channel/api/v1/historical-transactions` | JSON `{accounts:[{accountNumber,accountSource,lineOfBusiness}], timePeriodOption (daysPast1, currentYear, custom), dateField:"T", ...}` | **transactions**: trade/settle/entry/run dates, cusip, symbol, quantity, price, netAmount, commission, type, mnemonic |
| Income | POST `/ssc/tax-summary/wc/channel/v1/estimated-income-{summary,detail}`; GET `.../tax-income`, `.../realized-gain-loss` | accountList / accountNum | projected 12-month income per security; YTD tax summary |
| Options | POST `/OptionsPairingUIC/OPUIC/GetOptionPairData` | acctNum, groupBy | option positions and pairings |
| Cash | POST `/ssc/cashmanagement/wc/channel/api/v1/history` | accountList, category | money-movement history |
| Documents | GET `/ssc/account-documents/wc/channel/api/v1/statements/getDocumentsSearchResult` | account, date range | statement list (PDFs) |
| Performance | GET `/ssc/performance-measurement/wc/channel/v1/returns/{standard-period,time-series,historic,account-activity}`, `.../accounts/portfolios[/asset-allocations]`, `.../risk-metrics/accounts-summary`, `.../benchmarks/assignments`, `.../performance-reports/cycle-dates` | `accountNumbers=[...]`, `endDate`, `type=TIME_WEIGHTED` | TWR returns, allocation, risk metrics, account x period |

Legacy pages (`/ac/wc/channel/jsp/...`) redirect to `www2.advisorchannel.com` and return server-rendered HTML.
Examples: unknown-cost lots and dividend/capital-gain elections. They are not useful as a feed.

## 3. Data shape: Fidelity (as captured) vs Schwab silver

The Schwab side is from the converter source (`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, the
`schwab_schemas.py` and `silver_registry.py` files).

| Schwab silver | What it is | Fidelity source in this capture | Fit |
|---|---|---|---|
| `fact_acc` | account master | `accountList` + `getClientSummary.accountDetail` + `customprofile` | **close**: registration, tax status, owner, rep, established date, model, objective all present |
| `fact_rps` | positions, account x security x date | not called directly; derivable by summing `open-lots` (quantity, market value) per security | **derivable**: `Positions Export` is entitled but not walked |
| `fact_rps_s2` / `dim_balance` | balances | `getbalances` (UI display rows) + `accountList.netWorth` + clientSummary cash fields | **partial**: values arrive as formatted display strings, so they need flattening |
| `fact_trn` / `dim_transaction` | transactions | `historical-transactions` | **close**: the same core columns (trade/settle date, cusip, quantity, price, net amount, type) |
| `fact_sec` / `dim_asset` | security master + prices | only cusip, symbol and description inline; `Historical Prices and Positions Export` is entitled | **gap** until the export is seen |
| `fact_uln` / `fact_ult` | unrealized lots | `open-lots` | **close**: acquired date, quantity, cost, cost/share, market value, gain/loss, holding period, covered |
| `fact_rld/rlu/rlw/rly` | realized lots | `realized-gain-loss/detail.lots` | **close**: acquisition and close dates, proceeds, basis, ST/LT, wash-sale columns |
| -- | -- | performance family (TWR, risk, allocation) | **Fidelity only**; Schwab files carry no performance |

**Verdict on shape:** Fidelity covers the same five fact families Schwab feeds: accounts, positions/lots, balances,
transactions and realized lots. The column sets are close enough that the gold layer can share one canonical
account x security x date model. Silver cannot be the same code, though. These UI JSON payloads are display-shaped:
numbers arrive as strings, balances are nested as display rows, and calls are per account. The file exports
(section 4) are the likelier like-for-like counterpart to Schwab's SDD files. Their layout has not been seen yet.

## 4. Fit to the Auto-Schwab design

The Schwab design is in `data/assets/docs/SCHWAB_BOX_ARCHETYPE.md` and `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`.
It runs on a Windows box with a human-established session. EventBridge triggers SSM, which runs a scheduled task as
Administrator. The task enumerates and downloads the custodian's own daily files and lands them raw in
`opal-data-assets/<custodian>/<master>/bronze/{type}/{YYYYMMDD}/`. A silver Lambda then converts them. The schedule is
05:45-06:45 ET.

| Design element | Schwab | Fidelity, from this capture |
|---|---|---|
| Custodian file product | SDD daily files, enumerate + download REST | `Automated Bulk Download` / PM Standard Export / Positions Export are entitled; **endpoints not yet seen** |
| Credential life | refresh token, about 10 months | session about 10 h hard limit, so **a login every morning** |
| Login automation | none needed | **unknown**: login, MFA and device trust are not in the capture |
| Anti-bot | none observed | Akamai Bot Manager present: a headed real browser on the box, not raw HTTP replay |
| Server-to-server path | asked of Schwab Advisor Services | **Integration Xchange outbound transmissions, entitled on this login** |

**Recommended shape, provisional until walk #2:** one Windows box built to the same archetype (Schwab's box or a
twin). A headed browser signs in each morning with remembered-device trust, triggers or collects the day's Fidelity
bulk export files, and lands them raw in the Fidelity bronze tree. The address comes from `lib/opal_naming.py`
`address()`, never hand-typed. A Fidelity silver converter is registered beside the Schwab one, on the same 05:45-06:45
ET window. If walk #2 shows the outbound-transmission rules can be self-served, the SFTP feed replaces the browser leg
and lands in the same bronze tree.

## 5. Walk #2 -- what Andrew needs to capture

Before recording, open DevTools, go to the Network tab and tick **Preserve log** and **Disable cache**. Start on the
Fidelity login page, signed out. Save the result as one HAR.

1. **Sign in from scratch**, including whatever MFA step appears, and any "remember this device" choice. Record which
   MFA method it was (push, SMS, token).
2. **Exports**: open the export menu, then **Portfolio Mgt Standard Export** and **Positions Export**. Run one export
   for the whole book (or the Cottonwood group) and **download the file**. Repeat for transactions and for
   **Historical Prices and Positions Export** if offered.
3. **Automated Bulk Download**: open it and show what it offers (file types, schedule, retention). Download one file if
   one is available.
4. **Saved Exports** and **Import/Export Status**: open both.
5. **Integration Xchange, Transmissions**: open the outbound transmission rules and the add-rule screen, **without
   saving anything**. That shows whether an SFTP destination can be configured from this login.
6. Keep the downloaded export files beside the HAR. Their column layout is the fact-table shape that decides the silver
   converter.

The capture should be short: about 5 minutes, one client or group for any per-account step.

## 5a. Addendum 1 (~17:35Z): walk #2 results -- the files, the login, the export schedule

**Inputs:** five files Andrew exported from Wealthscape (`FI101626.{trn,ipn,sec,mvl,naa}`), the HAR
`wealthcentral.advisorchannel.com2.har`, and a screenshot of the Export Custom wizard. All stay in dell1 Downloads.
They hold client PII and are never committed.

**The files are Advent-format interface files, one set for the whole book, named `FI{MMDDYY}.*`.** The `101626` suffix
is Friday 16-Oct-2026, the T-1 business date. The format is fixed-width ASCII with CRLF line ends.

| File | Rows | Accounts | What it is | Columns, in order | Schwab counterpart |
|---|---|---|---|---|---|
| `.ipn` | 97,438 | 4,873 | positions as of the file date, written as `by` rows at closing price | account, code, date, security type, symbol, `@price`, source, quantity, then option and bond fields | `fact_rps` / `dim_position` |
| `.trn` | 401,593 | 4,955 | transactions, trade dates 2026-05-26 to 2026-10-16 (the export's date range) | account, code, trade date, security type, symbol, amount, cash/client, quantity, broker `NFSC`, commission, settle date, comment; `;` rows are comment continuations | `fact_trn` |
| `.sec` | 2,464 | -- | security master, keyed by security type + symbol | description, coupon/rate, issue and maturity dates, payment frequency, factor | `fact_sec` / `dim_asset` |
| `.mvl` | 2,436 | -- | closing prices (security type + symbol, price) | -- | prices in `fact_sec` |
| `.naa` | 5,007 | 5,007 | account master: names, address, tax and contact fields (PII) | -- | `fact_acc` |

- **Transaction codes:** by 166,752; dv 129,384; sl 63,459; dp 14,606; wd 6,859; in 5,658; plus ai, rc, ss, cs and
  a few upper-case codes.
- **Security types:** cs, mf, mm, fc, ca, ep, mb, gb, cb, cd, cl and others. Bond prices are quoted per 100 of par.
- **Reconciliation:** `.ipn` securities, valued at quantity x price (bonds per 100), sum to **$1,569.6M** against the
  book tile's **$1,563.1M** (+0.4%). The `CA` rows (29,495 of them, `dp` code) are not cash at that value: they sum to
  $4.98B. Their meaning is open.
- **Not in this file set:** open lots and realized lots (Schwab `fact_uln/ult/rld`) and balances (Schwab
  `fact_rps_s2`).

**Login, measured.** The flow runs as follows:
1. `www.wealthscape.com`, then POST `/auth/api/redirect-info`.
2. POST `wealthcentral.../auth/login`, which sends the username.
3. On `ecaap.advisorchannel.com`: POST `/user/factor/password/authentication`, then POST `/user/session/login`. That
   call returns the authenticator list: `OTPSMS`, `OTPVOICE`, `OTPREP`.
4. POST `/user/factor/otp/sms/authentication` sends the text, and a PUT to the same path submits `securityCode`.
5. POST `wealthcentral.../ssc/platform-authorization/api/v2/authorize`, then the app loads.

No remember-this-device step appeared, and a text-message code was required. Device profiling runs during login:
`cfa.fidelity.com` scripts, `online-metrix.net` (ThreatMetrix), and a probe of local ports including 3389 (RDP), 5900
(VNC) and 5939 (TeamViewer). A login from an RDP-managed EC2 box may therefore score as higher risk. Unattended daily
automation is blocked by the text-message code until one of these is decided: a human enters the code each morning, the
code goes to a number the box can read (a Terms of Use and policy call), or the official transmission is set up.

**Export scheduling (from Andrew's screenshot, not yet captured as traffic).** The wizard lives at
`/ssc/singlecontainer/wc/channel/app/tools/portfolio-exports/custom` and has five steps: Enter Criteria, Name File &
Choose Columns, Choose Filter, Create File, Verify. Step 4 offers two modes:
- **On Demand**: run manually from the Saved Exports view.
- **Automatically**: on chosen weekdays (Mon-Sun); "go to Export Status to download the file".

So a scheduled export is not pushed anywhere. It is **generated and parked in Export Status**, and still has to be
downloaded in a signed-in session. The export windows opened as pop-ups, which the main tab's DevTools did not record.
The Export Status list and download endpoints are therefore not yet measured.

**Backfill, as hypotheses to verify in the wizard:**
- **Transactions:** the `.trn` date range comes from step 1 Enter Criteria, so an on-demand export over a long range
  can backfill them.
- **Positions:** one approach is the `Historical Prices and Positions Export` entitlement, one as-of date per run.
  Another is to roll today's `.ipn` back through `.trn`, the way Advent rebuilds positions.

## 5b. Addendum 2 (~17:50Z): where scheduled exports land, and how to fetch them

**Inputs:** HAR `wealthcentral.advisorchannel.com3.har` (Export Status pop-up), the custom export's `prices.txt`, and
a screenshot of Import/Export Status. The screenshot's Domain column reads **ALONGSIDE, LLC**, so this book ($1.56B)
is the Alongside domain.

**The retrieval is two calls**, the counterpart of Schwab's FetchDetails + Download:

1. **List:** POST `/ssc/importexport/wc/channel/status/v1/status.json`, body
   `{"iEtype":"E","dateString":"YYYY-MM-DD","startPage":"1","pageLength":300}`, with the `x-xsrf-token` header. It
   returns `statusElements[]`, one row per generated file. Each row carries:
   - identity: `profileId`, `requestId`, `fileType`, `fileName`, `fileTypeDisp`;
   - schedule and format: `scheduleFlag`, `scheduledDaysDisp`, `importExportFormatDisp`;
   - outcome: `fileStatusDescription` (`COMPLETED`), `fileCreatedTimestamp` and `fileDeliveredTimestamp` (UTC).

   The calendar reaches back **120 days**, one `dateString` per day.
2. **Download:** GET `/ssc/importexport/wc/channel/export/v1/downloadExport.do?fileName=..&fileType=..&profileId=..&requestId=..`.
   All four values come from the list row. The app opens it with `window.open(url, "_blank")` (`bundle-v26.9.1.S1.js`,
   `handleCellSelection`), which is why a DevTools capture never records it. A sibling POST
   `/export/v1/downloadExport.json` exists in the bundle, but its caller is commented out.

**What is configured (read from status.json, 2026-10-19):**

| Profile | Format | Schedule | Files (`fileType`: name) |
|---|---|---|---|
| v1.0.0 | Standard Format A, fixed-width (`FL`) | on demand | `EXPBL` `FI{MMDDYY}.ipn`, `EXPRC` `.mvl`, `EXACC` `.naa`, `EXSEC` `.sec`, `EXTRN` `.trn` |
| v1.0.1 | **Custom, CSV (`CS`)**, every column selected | **all 7 days** | `EXACC` `account.txt` (141 cols), `EXPOS` `position.txt` (62), `EXBAL` `balance.txt` (43), `EXPRC` `prices.txt` (44), `EXSEC` `security.txt` (45), `EXTRN` `transact.txt` (66) |

- **Run time on save:** v1.0.1 generated as soon as it was saved. The request went in at 17:32:04Z; the files
  arrived between 17:32:07Z and 17:33:36Z, transactions last (91 s).
- **Recurring run time:** the status row's `scheduledTimeDisp` is empty, so the hour of the daily run is **not stated
  anywhere**. It is measured only by reading tomorrow's row.
- **Custom vs standard:** the custom set adds **balances** (`balance.txt`), which closes the Schwab `fact_rps_s2` gap.
  Its file names carry **no date** (`prices.txt` every day). So the business date must be read from the content: the
  first CSV field is `20261016`, the T-1 date. This is Schwab's rule (partition from AsOfDATE, never the file name)
  applied again.
- **`prices.txt`:** 2,464 rows, no header row, quoted CSV, business date first. It also carries CUSIP, exchange,
  symbol, description, asset class and security type.

**Fit to the Auto-Schwab design, revised:** the box signs in each morning and posts to status.json for today. For each
`COMPLETED` row of the scheduled profile it calls downloadExport.do and lands the raw bytes in Fidelity bronze under
the content's business date. A run manifest is written as in `sdd-daily-pull.ps1`. Each morning that is 7 calls plus
the login, not 20k per-account calls. The text-message code at login is still the one blocker to unattended operation
(section 5a).

**Backfill:**
- **Status history:** the 120-day calendar holds only files that were actually generated. The schedule started on
  2026-10-19, so it backfills nothing before that date.
- **Transactions:** an on-demand export with a date range in step 1 Enter Criteria (the standard `.trn` covered
  2026-05-26 to 2026-10-16). The status row's `exportFilterTransDateFrom/To` fields carry that range.
- **Positions and balances before 2026-10-19:** not in the custom export, which is as-of the latest date. The options
  are the `Historical Prices and Positions Export` entitlement (not yet walked), or rolling positions back through
  transactions.

## 6. Open items

- **Terms of Use:** read `TOU_RIA.html` for an automated-access clause before any scripted login. Owner: Andrew. The
  page was served in this capture but not reviewed here.
- **Masters:** the capture shows one firm book ($1.56B). Is it the Alongside umbrella that holds the Cottonwood,
  Inflection and 49 Financial books? Andrew's earlier $700M figure and this $1.56B differ. Owner: Andrew.
- The per-account JSON endpoints in section 2 remain the fallback source if exports are not automatable. Do not build
  on them until walk #2 settles section 4.
