# Wealthscape HAR scoping — first pass, 2026-08-26 ~20:42Z (CTO terminal, read-only)

**Source:** two HAR recordings Andrew produced under his Wealthscape authorization (recorded
~16:35/16:37 local). Files remain at `C:\Users\AndrewBerman\Downloads\` and DO NOT enter the repo
— HAR captures carry session cookies/tokens. This doc carries derived structure only; no account
numbers, no client names, no header material.

## File verdicts

| file | size | verdict |
|---|---|---|
| `testing.har` | 23.3 MB | **NOT Fidelity** — a Bing/MSN/Edge new-tab session (320 entries, zero advisorchannel traffic). Discard for this purpose. |
| `testing2.har` | 107.8 MB | **THE capture** — 466 entries, 304 against `wealthcentral.advisorchannel.com` (Fidelity Wealthscape institutional), 152 JSON responses, 53 distinct API endpoints. |

## The API family that matters — `wealthcentral.advisorchannel.com/ssc/performance-measurement/wc/channel/v1/`

| endpoint | calls | params | response carries |
|---|---|---|---|
| `returns/standard-period` | 10 | type, endDate, lastCycleReturnInd, accountNumbers | per-account standard-period rate-of-return set (x2 periods in sample), GOF/NOF inception dates, account {number, source, firmId, startDate, csdnCode} |
| `returns/time-series` | 5 | accountNumbers, timePeriod, type, rateOfReturnType, benchmark, endDate | pretax time-series RoR per account + a parallel benchmark series block |
| `returns/historic` | 5 | type, frequency, timePeriod, endDate, accountNumbers | historical RoR at a chosen frequency (x10 periods in sample) |
| `performance-reports/cycle-dates` | 4 | accountNumber | the FULL report frame: beginning/ending fair value, totalNetAssets, numberOfPositions, taxLiabilityAmount, cycleDatesData, standardPeriods block, benchmarkCharacteristics, riskData, cashFlowData, gainLossData |
| `accounts/portfolios` | 4 | accountNumbers, type, assetClass, source | per-account allocation vectors (+ equityAnalysis / portfolioCharacteristics slots) |
| `accounts/portfolios/asset-allocations` | 4 | accountNumbers | allocation-only variant |
| `benchmarks/assignments` | 4 | accountNumber, isClientLevel | benchmark assignment (sample returned the error shape — likely unassigned account) |

Support surfaces also captured: `accountsearch/.../verify.json` (accountNetWorth, cashAvailable,
marginBalance, intraday performance change, owner name fields), `clientSearch/findClients.json`
(paged client roster with myClients/starred/allClients), `menus/.../entitlements.json` +
`siteEntitlements.json` (what this login may see), acct-cart, preferences.

## Product mapping (why this matters this week)

**This is account-grain performance data — returns (standard/historic/time-series), benchmark
series, allocations, fair-value/gain-loss frames — i.e., the exact input family ADVI Performance
Reporting consumes, from the FIDELITY custodial side.** The 49F source gaps + the parked
ADVI_49FSRC ingestion + ADVI_STITCH Phase B all pointed at "the Fidelity login" as their event;
this capture is the first measured view of what that login actually exposes.

## Constraints, measured from the capture

1. **Session-cookie auth, no public API grammar** — every call rides the logged-in Wealthscape
   session. There is no OAuth/token endpoint in the capture.
2. **Active anti-automation is PRESENT:** 6 POSTs to an obfuscated path
   (`/Ud8J6o/A5cB/FC/...`) — F5/Shape-style browser fingerprinting. Naive headless replay of the
   session will likely be challenged. The realistic ingestion shapes, in ascending effort:
   (a) periodic operator-assisted capture (Andrew or an authorized human drives; HAR/export lands
   in a drop zone — matches his "not a ton of usage" calibration); (b) an authorized
   headed-browser flow (Playwright on his session, human-present); (c) a vendor/data-feed
   arrangement with Fidelity (the clean long-term answer if volume grows).
3. **Volume is small** — one advisor book, low call counts; a daily or weekly pull is minutes,
   not a pipeline. Andrew's own read ("may not be a blocker if its difficult") is consistent with
   the capture: this scopes as a THIN source, not a heavy integration.

## Recommended next step (routed to COO for the ADVI lanes)

Treat this doc as the D0-input for the Fidelity-source scoping cell inside ADVI_49FSRC /
ADVI_STITCH Phase B: (1) enumerate which PERFRP view fields the Wealthscape family can supply vs
the 49F/SmartX side; (2) pick the ingestion shape (a) vs (b) with Andrew's usage calibration as
the prior; (3) NO automated egress or replay is authorized by this doc — vendor egress stays under
the standing per-use law; the capture analysis itself was local file reads only.

— 1.0.0_SA_CTO, first-pass scope; the HAR files stay Andrew's, derived structure only in-repo.
