# YCharts coverage for DEMQUE's requests: what exists, and the walk that would answer the rest

**By:** `4.0.0_SA_CRO~DELL1`, 2026-10-13 ~21:3xZ.
**Asked:** Andrew-direct ~21:1xZ, relayed by `1.0.0_SA_CTO~DELL1` msg 5208. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_211xZ_DELL1_SEAT_ALLOCATION_AND_YCHARTS_TO_CRO_DELL1.md`.
The goal: measure how much of DEMQUE's request items YCharts covers, especially CUSIP-level fixed income.
**Method:** read-only.
- In the repo, I read the YALP_MDSRC briefs and DEMQUE's CARD-A request files.
- On SharePoint, I read the `Shared` site through the gateway: listings, three READMEs, a server-side profile of the HAR, and one
  search.
- I made no YCharts call and opened no session.

## 1. The answer so far

**Nothing that exists answers the question.** No artifact anywhere tests YCharts against individual bonds or cash equivalents by
CUSIP.
- The May 2026 work mapped YCharts' internal API and proved coverage of **bond indices**, not bonds.
- Alyssa's only HAR records the **model-portfolio import** journey.
- Her own notes say her report workflow puts proxies in for "things YCharts cannot price (cash, FIA, buffer, fixed)". That
  points toward a coverage gap, but it is her practice, not a measurement.

So a short manual browser walk is needed. Section 4 lays it out.

## 2. Prior art in the repo (YALP_MDSRC, 2026-05)

- **The internal API is about six generic endpoints that take any entity type** (`docs/briefs/mdsrc-ycharts-internal-api-20260520.md`
  section 2.1): `/securities/securities_info`, `/charts/general_data.json`, `/charts/fund_data.json`, `/indices/table_data`,
  `/charts/scatter_plot_data.json` and `/calculations/*`. One `securities_info` call returned a stock, an ETF and a mutual fund
  together.
- **Fixed income was tested only as indices.** The Bloomberg Aggregate, 1-5 Gov/Credit, 1-3 Gov/Credit, TIPS, Municipal and High
  Yield all resolve through `/indices/table_data` (same brief, section 5). No individual bond, Treasury bill, CD or money-market fund
  was tested by CUSIP in any of the 23 YCharts briefs. Those briefs carry 90 fixed-income mentions; every one is about an index, an
  ETF classification, or a benchmark.
- **The known residue is a gap in finding symbols, not in data.** `securities_info` looks up an exact symbol and does not search.
  Four commodity symbols could not be guessed. The search endpoint was never located (section 5, P4). A CUSIP lookup hits exactly
  this gap: the walk has to find out whether YCharts' search accepts a CUSIP.
- **Session constraints** (section 3): YCharts allows one concurrent session. A human login evicts the automated one, and the
  automated one evicts the human. Every request needs an active authenticated probe first. Rate limits are unconfirmed.
- **The dormant pipeline** is three Terraform-declared Lambdas: `ycharts-session-probe`, `ycharts-session-capture` (both in
  `infra/aws/terraform/ycharts-pipeline/lambdas.tf`) and `ycharts-market-data-pull` (`market-data-pull.tf`). Their live state was
  not read.
- **A live user of the same seat:** `irpt-ycharts-generate` (`infra/aws/terraform/investor-reporting/ycharts/generate.tf`, IRPT on
  dell2) drives YCharts for investor reports. Any walk shares the one session with it and with Alyssa.

## 3. What Alyssa's SharePoint folder holds

She keeps it at site `Shared`, folder `Product-Alyssa/YCharts/`, split by step per her `MAP.md`.

| Step folder | Contents | Bearing on coverage |
|---|---|---|
| `01_request-intake` | README only | none |
| `02_holdings-prep` | README; `samples/ychart template.xlsx` (one ticker per row plus Dollars); `hars/` **empty** | Her README: "proxies for things YCharts cannot price (cash, FIA, buffer, fixed)". The upload is by ticker. The client-portfolio upload HAR it promises was never added. |
| `03_model-updates` | `hars/model update har.har`: 24,655,431 bytes, 207,924 lines, sha256 `70dc56e6...65ff`, recorded 2026-09-23 on `ycharts.com/model_portfolios/model/1728420/edit/` | The model-import journey, not security coverage. It **holds live session cookies**, so it must never be copied into git. It may show how holdings resolve on upload; that was not read. |
| `04_report-generation`, `05_delivery-and-filing` | README only | none |
| `Andrew Handoff/` | a yc-commentary skill and its zip | none |

**Elsewhere on the site:** templates (`YC * template.xlsx`, benchmark templates), `Ycharts updates instructions.docx` (2025-04-08),
and old PDF reports. None of them is a coverage capture.

## 4. The walk that would answer it (proposed, not started)

The question is two lookups per security: does YCharts resolve this CUSIP, and does it carry a price history for it.

1. **Sample.** About 20 bonds from the 370 the CTO's message names, and 20 of the 227 Cottonwood cash equivalents in
   `requests/MDPF_SECHIST-CARD-A-B1-FUND-TYPE.json` (CUSIPs only). The bond list's source file was not located: the "370 bonds"
   figure appears only in the CTO's message. 40 lookups is the cap.
2. **Driver and window.** One person signed in to YCharts (Alyssa, or Andrew) with devtools recording a HAR, in a window when the
   IRPT generator and Alyssa's own work are idle. The alternative is the dormant session pipeline driving a browser, but that evicts
   whoever is signed in. That choice is the one decision needed.
3. **Per CUSIP:** type it in the YCharts search box. If it resolves, open the security page and its price chart. Record what the
   search returns: the search call is the unknown endpoint, and the HAR captures it.
4. **Output:** a table of CUSIP, kind, resolves (yes/no), symbol, history (yes/no and first date). The HAR goes to
   `Product-Alyssa/YCharts/02_holdings-prep/hars/` per her map, never to git. Then a one-line coverage figure for each kind.
5. **No bulk pull.** No data is downloaded beyond what the pages render. The walk takes about 30 minutes.

## 5. Not checked

- The model-update HAR's content was not read; it is 24.6 MB and carries cookies.
- The live state of the three dormant Lambdas and of the stored session secret.
- Which CARD-A file carries the 370 bonds.
- Whether YCharts' Excel upload accepts a CUSIP column. Her template uses tickers only.
