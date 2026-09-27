# Investor Reporting cleanup brief -- the evening walks of 2026-09-27

**Mode:** midstream on DSGN_IRPTV1 (with IRPT_BCKEND rows). **By:** 4.0.0_SA_CRO on Andrew's word: "do another /ui-walk across the Performance, Holdings and Analysis tabs and look for UI issues as you drill down through various client and analysis functions, i want another cleanup brief on a slug of issues".
**Register (the source of every table here):** `docs/briefs/irpt-ui-cleanup-findings-20260927.json`.
**Build walked:** portal local DEV `3b98939b` (round 8) at 1440 px, as the 49F three-account client, the INF four-account client, the COT eleven-account client, the COT two-account client.

## Part 0 -- how this was made, and where it bent

- Three walks: a re-grade (`20260927T200826Z`), a deep walk that pressed every enabled button on each tab (`20260927T203155Z`), and a stopped deep run whose INF screenshots are kept (`20260927T201809Z`). Every finding was confirmed on a screenshot, and a walker check was never taken as the verdict.
- **Where it bent:** the walker cannot submit (Generate, Review portfolio, uploads stay blocked by design), so nothing after a submit was seen. A dialog blocked the first deep run's tab switch; it was stopped, disarmed by hand, fixed, and re-run.

## Part I -- outcome territory

- **O1** Performance reads as a finished answer: no 'not supplied' tiles, no raw data dump, no system words on the face. (UIC-01, UIC-02, UIC-04, UIC-05)
- **O2** Every period button either answers or says in plain words why it cannot, over a real date range. (UIC-06, UIC-07)
- **O3** Holdings charts stay legible at any account count: readable labels, distinct colours, negatives handled, long lists reachable. (UIC-10, UIC-11, UIC-12, UIC-13, UIC-15, UIC-16)
- **O4** No system name, code or unknown placeholder reaches the face or its first click. (UIC-03, UIC-08, UIC-09, UIC-14, UIC-17)
- **O5** Analysis setup behaves like a form: a selection takes, defaults fit the client, errors wait for input. (UIC-18, UIC-19, UIC-20, UIC-21, UIC-22)
- **O6** The request list is the viewer's own and speaks client language. (UIC-23)

## Part II -- the findings (23)

| id | outcome | owner | observed | acceptance | shots |
|---|---|---|---|---|---|
| UIC-01 | O1 | 2.0.0_SA_COO~D | On a computed 49F report (YTD 5.93%), VS BENCHMARK, ENDING VALUE and BEGINNING VALUE all read 'not supplied'. | A computed report shows only the figures it has; a missing benchmark or value is one plain line, never three 'not supplied' tiles. | 20260927T200826Z#031 |
| UIC-02 | O1 | 2.0.0_SA_COO~D | Under the cumulative chart the page lists every daily point as a table row (about 185 rows), making the page over 6,000 px tall. | The daily series is one click away (or paged); the default view is the chart and the period figures. | 20260927T200826Z#031 |
| UIC-03 | O4 | 2.0.0_SA_COO~D | Report details on a computed report shows 'Partial -- Qualified answer -- not a complete report', PERFORMANCE_PARTIAL, TIME_WEIGHTED, OPAL_ENGINE and three revision hashes. | Report details states the method and source in client words (for example 'Time-weighted, net of fees; Opal's performance engine'); codes and hashes stay out of the page. | 20260927T200826Z#032 |
| UIC-04 | O1 | 2.0.0_SA_COO~D | The 'Monthly returns and accounts' table carries rows whose account, ending value and coverage cells read 'not supplied'. | The monthly table lists only rows it can fill, or states once what is not available. | 20260927T200826Z#032 |
| UIC-05 | O1 | 2.0.0_SA_COO~D | The account picker keeps 'YTD pending' (or 'YTD unavailable') after the YTD figure has rendered, and still says 'YTD' while 3Y or Since inception is selected. | The picker's figure follows the selected period and updates when it computes. | 20260927T200826Z#031, 20260927T203155Z#140 |
| UIC-06 | O2 | 2.0.0_SA_COO~P | For the 49F three-account client, 3Y and Since inception answer 'Unavailable' with the raw code UNSUPPORTED_OPERATION and a 'Contact support' button, no plain words. | A window the service cannot answer says so in words (what is supported, what to choose instead); no code on the face. Owner of the capability: IRPT_BCKEND (~P). | 20260927T203155Z#140, #141 |
| UIC-07 | O2 | 2.0.0_SA_COO~D | 'Since inception' requests 1970-01-01 to 2026-09-22 (INF and 49F clients). | 'Since inception' starts at the account's first data point (or its opening date). | 20260927T201809Z#018, 20260927T203155Z#141 |
| UIC-08 | O4 | 2.0.0_SA_COO~D | The INF refusal reads 'This account is not covered for performance reporting. It becomes available once this account is added to the covered set for this firm.' | The refusal names, in client words, why the figure is missing and who can make it available. | 20260927T201809Z#007 |
| UIC-09 | O4 | 2.0.0_SA_COO~D | While a report loads, the canvas reads 'Loading  No source age yet'; a refusal reads 'Unavailable  No source age yet'. | Loading is a loading state with no system words; 'source age' never shows before a source exists. | 20260927T203155Z#067, #140 |
| UIC-10 | O3 | 2.0.0_SA_COO~D | With 4 (INF) or 11 (COT) accounts, the pie's slice labels overlap into an unreadable pile. | Labels never overlap: small slices move to the legend (or a leader line). | 20260927T201809Z#022, 20260927T203155Z#086 |
| UIC-11 | O3 | 2.0.0_SA_COO~D | The accounts pie draws 4 or 11 slices in near-identical greys and dark navies; neighbouring slices cannot be told apart. | Adjacent slices are distinguishable at a glance (a palette with enough separation for 11+ accounts). | 20260927T201809Z#022, 20260927T203155Z#086 |
| UIC-12 | O3 | 2.0.0_SA_COO~D | One account of the COT eleven-account client is NEGATIVE (about -4.6% of the client) and sits in the accounts table and legend of a pie. | A negative account is shown as a separate, labelled line (never as a pie slice), and the pie's shares sum to the positive total it states. | 20260927T203155Z#086 |
| UIC-13 | O3 | 2.0.0_SA_COO~D | For the COT eleven-account client, the Over what list shows 10 rows and cuts the next one in half; there is no 'show all'. | Every account is reachable from Over what (a 'show all' or a scroll affordance); no row is clipped. | 20260927T203155Z#067, #086 |
| UIC-14 | O4 | 2.0.0_SA_COO~D | The Holdings footer reads 'Source: holdings_snapshot.build_cot.', an internal function name. | The source line names the data source in client words (for example 'Black Diamond, as of ...'). | 20260927T200826Z#015 (cropped) |
| UIC-15 | O3 | 2.0.0_SA_COO~M | INF model holdings list bare tickers (FDRXX, CIVIX, VO ...) with no security names. | Every security shows its name beside its ticker. | 20260927T201809Z#038 |
| UIC-16 | O3 | 2.0.0_SA_COO~M | INF account labels read '****9749 / INDIVIDUAL RETIREMENT AC' (the type text is cut off) on every surface. | An account's type reads in full ('Individual Retirement Account'). | 20260927T201809Z#007, #022 |
| UIC-17 | O4 | 2.0.0_SA_COO~D | 'About this scope' shows 'SCOPE AS OF: unknown' for every client walked (49F, INF, COT). | The scope panel shows a real date or omits the field. | 20260927T200826Z#005, 20260927T201809Z#007 |
| UIC-18 | O5 | 2.0.0_SA_COO~D | Pressing 'Multi-Comp' leaves 'Variant: Overview (0 comparisons)' and shows 'Multi-Comp does not match 0 comparison(s); Overview does.'; the selected card is barely distinguishable. | Pressing a card selects it visibly and the form asks for what that variant needs (for example 'Add at least two models'); no system sentence. | 20260927T203155Z#184 |
| UIC-19 | O5 | 2.0.0_SA_COO~D | For multi-account clients the default report title names ONE account ('<client> ****8774 / UTMA -- Overview'), and the title field shows the name with trailing asterisks. | The default title names the client (and the variant), never one account of several. | 20260927T203155Z#126, #184 |
| UIC-20 | O5 | 2.0.0_SA_COO~D | 'Enter the report recipient (up to 200 characters).' shows as a red error before anything has been typed. | Required-field messages appear after the user tries to generate (or leaves the field), not on load. | 20260927T200826Z#026, 20260927T203155Z#126 |
| UIC-21 | O5 | 2.0.0_SA_COO~D | The comparison input's placeholder is cut off: 'Opal model or ETF symbo'. | No placeholder or label is truncated at 1440 px. | 20260927T203155Z#126, #184 |
| UIC-22 | O5 | 2.0.0_SA_COO~D | While the snapshot loads, Analysis shows 'Holdings snapshot: none held -- Loading' and the red refusal 'No holdings snapshot is held for this scope.' for a client whose Holdings tab shows holdings. | Analysis shows a loading state until the snapshot read answers; a refusal only after it answers. | 20260927T200826Z#029 |
| UIC-23 | O6 | 2.0.0_SA_COO~D | Signed in as the admin walker, 'Your analysis requests' lists requests other principals submitted (windows 7-15), each as 'Open REQ-<24-hex> . revision 1' with 'Unavailable -- ANALYSIS_REQUIRES_ATTENTION' or 'Status unavailable' (including window 15's READY job). | The list shows the viewer's own requests (or is labelled as all requests for an admin), each by client name, variant and date, with a status in words; a READY job reads Ready. | 20260927T203155Z#126 |

Owners: 2.0.0_SA_COO~D 20, 2.0.0_SA_COO~M 2, 2.0.0_SA_COO~P 1.

## Part III -- the bar (qualitative)

An advisor who opens any of the three tabs for a client with one account or eleven sees a finished page: every figure it shows is real, every gap is one plain sentence, every chart is readable without hovering, and no word on the page is one a system invented.

## Part VI -- status (NOT outcome-bearing): the re-grade of the 17 items the morning walk found not met

Round 8 claimed 15 of the 17. On `3b98939b`: **8 MET**, 1 met page-side with its data still open, and 8 NOT MET.

| id | verdict | what the walk showed |
|---|---|---|
| UIR-04 | MET | Options show 'Cottonwood' / '49 Financial'. |
| UIR-06 | MET | The empty page shows grey placeholders, no figures. |
| UIR-11 | MET | No sample content behind the open search list. |
| UIR-13 | MET | 'Cottonwood (Client)'. |
| UIR-15 | PAGE MET, DATA OPEN | Each entry shows its value; the labels stay identical until UIR-26's labels (Monday). |
| UIR-17 | NOT MET | Over what still lists identical labels (data, UIR-26). |
| UIR-20 | MET | Export is grey on Analysis with no report. |
| UIR-25 | MET | Two accounts draw two distinct colours (but see UIC-11 at 4+ accounts). |
| UIR-30 | NOT MET | The display name is right, but the firm still shows twice (chip and identity line). |
| UIR-32 | NOT MET | The breadcrumb now names the account; the strategy still reads '*9238' against '****9237', two masking styles. |
| UIR-34 | NOT MET | A one-child level still draws a one-slice pie. |
| UIR-37 | NOT MET | Blue still marks a model and Equity; orange a model and Alternatives. |
| UIR-40 | NOT MET | Round 9: several navy bands remain (3 on the empty page). |
| UIR-41 | MET | Map chips are grouped by account. |
| UIR-45 | NOT MET | Two date formats remain, and the source line is now an internal name (UIC-14). |
| UIR-46 | MET | As UIR-25. |
| UIR-49 | NOT MET | As UIR-32. |

The five morning findings ~D built (UIW-0927-01, -02, -03, -06, -07) are all MET.

## Part VII -- what this does not claim

- Five clients across three firms, one pass each; a finding seen on one client may not hold for all, and one missing on these may exist on others.
- Nothing behind a submit (a generated report, an export, an upload) was walked.
- The design:contrast checks (under 3:1 on some Analysis and dialog text) were not confirmed by eye and are not findings here.
- Owners for IRPT_BCKEND rows are proposed, for the CTO to confirm.

## Refs

- BRIEF `docs/briefs/irpt-ui-cleanup-brief-20260927.md`; REGISTER `docs/briefs/irpt-ui-cleanup-findings-20260927.json`
- EXISTING PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`; prior register `docs/briefs/irpt-ui-review-findings-20260926.json`; morning verification `docs/briefs/irpt-ui-review-verification-20260927.md`
- MEASURED AT 2026-09-27 20:08-20:46Z (walks), on local DEV 3b98939b.
