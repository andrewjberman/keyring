# Investor Reporting -- the remaining UI issues, 2026-09-28 (one brief)

**Mode:** midstream on DSGN_IRPTV1 (with IRPT_BCKEND rows). **By:** 4.0.0_SA_CRO on Andrew's word: "When that UI-Walk completes, I want you to cross-reference it against the irpt-ui-cleanup-status-20260928.md brief that you developed from the second iteration of the ui-walk. Then synthesize the remaining issues into one brief."
**Register (the source of every table here):** `docs/briefs/irpt-ui-remaining-findings-20260928.json`. **Walk:** `/ui-walk --deep` `20260928T174953Z`, the same three clients as the morning walk, portal local DEV `28f5118c`, 167 screenshots, 0 blocked writes. The walker was disarmed at 18:04:14Z, and a login after disarm was refused.
**What this is:** a development read, not a CVO grade. It replaces the morning status (`irpt-ui-cleanup-status-20260928.md`) as the one list of what is still wrong.

## Part 0 -- the cross-reference in one table

The morning grade was 3 of 23 MET. On `28f5118c` the 23 UIC items read:

| grade | morning (`20260928T133602Z`) | now (`20260928T174953Z`) |
|---|---|---|
| MET | 3 | 3 |
| PARTIAL | 3 | 4 |
| NOT_MET | 16 | 15 |
| NOT_OBSERVED | 1 | 1 |

- **Moved:** UIC-23 went from NOT MET to PARTIAL (TO-IV-e-74 landed). Nothing else changed grade.
- **Landed but did not close its item:** TO-IV-e-70 (merged `602757a8`) changed the asset-class colours, not the accounts-pie palette, so UIC-11 stays NOT MET.
- **In flight, not graded:** ~D's closer-drive edits for UIC-10, UIC-12 and UIC-13 sit UNCOMMITTED in the portal working tree (18:03-18:04Z). They came after the Identity and Holdings steps for the INF and COT clients, so those steps graded committed code.
- **Morning new findings:** NEW-01 (YTD -100%) still reproduces, and ~P has measured its cause (row S177). NEW-02 (blank COT pie) did not reproduce.
- **Also carried:** the older review items still NOT MET on 09-27 (UIR-03, 23, 26, 34, 40, 45, 48, 50). **New today:** six (UIW-0928-01..06).

## Part I -- outcome territory

- **O1** Performance reads as a finished answer: no 'not supplied' tiles, no raw data dump, no system words on the face. (UIC-04, UIC-05)
- **O2** Every period button either answers or says in plain words why it cannot, over a real date range. (UIC-06, UIC-07)
- **O3** Holdings charts and lists stay legible at any account count: readable labels, distinct colours, negatives handled, long lists reachable, no empty levels or zero rows. (UIC-10, UIC-11, UIC-12, UIC-13, UIC-15, UIC-16, UIR-34, UIW-0928-05)
- **O4** No system name, code or unknown placeholder reaches the face or its first click. (UIC-03, UIC-09, UIC-14, UIC-17, UIW-0928-04)
- **O5** Analysis setup behaves like a form: a selection takes, defaults fit the client, errors wait for input. (UIC-18, UIC-19, UIC-20, UIC-21, UIC-22)
- **O6** The request list is the viewer's own and speaks client language. (UIC-23)
- **O7** A single account's Holdings view is complete: its rows, its total and its layout match that account every time. (UIW-0928-01, UIW-0928-02, UIW-0928-03)
- **O8** The data behind the page is current, correct and tells accounts apart. (NEW-01, UIR-26, UIR-03, UIR-23, UIR-48, UIR-50, UIW-0928-06)
- **O9** The page follows the design law: one navy band per page, one date format. (UIR-40, UIR-45)

## Part II -- the remaining findings (35)

| id | outcome | owner | now | morning | observed | acceptance | shots |
|---|---|---|---|---|---|---|---|
| UIC-03 | O4 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | Report details still shows 'Partial -- Qualified answer -- not a complete report', PERFORMANCE_PARTIAL, TIME_WEIGHTED, OPAL_ENGINE, a tenant id, two revision hashes and 'unknown' / 'not stated' fields. | Report details states the method and source in client words (for example 'Time-weighted, net of fees; Opal's performance engine'); codes and hashes stay out of the page. | #135 |
| UIC-04 | O1 | 2.0.0_SA_COO~D | PARTIAL | PARTIAL | The monthly table now states the missing benchmark once, but its account row still reads 'not supplied' for the account name and the ending value. | The monthly table lists only rows it can fill, or states once what is not available. | #135 |
| UIC-05 | O1 | 2.0.0_SA_COO~D | PARTIAL | PARTIAL | The picker keeps '<period> pending' after the figure renders (YTD 5.93% on screen, picker 'YTD pending'; 1Y -100.00% on screen, picker '1Y pending') and reads 'YTD pending' above a refusal. | The picker's figure follows the selected period and updates when it computes. | #134, #141, #071 |
| UIC-06 | O2 | 2.0.0_SA_COO~P | NOT_MET | NOT_MET | For the 49F three-account client, 3Y and Since inception answer 'Unavailable', the raw code UNSUPPORTED_OPERATION and a 'Contact support' button, with no plain words. | A window the service cannot answer says so in words (what is supported, what to choose instead); no code on the face. | #143, #144 |
| UIC-07 | O2 | 2.0.0_SA_COO~D | PARTIAL | PARTIAL | 'Since inception' now requests 'the account's first data point', but the same window answers UNSUPPORTED_OPERATION (UIC-06), so no since-inception figure is reachable. | 'Since inception' starts at the account's first data point (or its opening date). | #144 |
| UIC-09 | O4 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | While a report loads the canvas reads 'Loading  No source age yet'; a refusal reads 'Unavailable  No source age yet'. | Loading is a loading state with no system words; 'source age' never shows before a source exists. | #006, #138, #143 |
| NEW-01 | O8 | 2.0.0_SA_COO~P | NOT_MET | n/a | The smallest account of the 49F three-account client still answers -100.00% for YTD and for 1Y; the cumulative series starts at 0.00% and falls to -100.00% the next day. | An account with positive holdings never answers -100%; a first-day funding flow is not a return. | #139, #141 |
| UIC-10 | O3 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | With 4 (INF) or 11 (COT) accounts, the pie's slice labels overlap into an unreadable pile. **In flight:** ~D's closer-drive edit is in the portal working tree, UNCOMMITTED (mtime 18:03-18:04Z, after this walk's Identity and Holdings steps): DrillTree.tsx SMALL_SLICE_SHARE. Not walked; grade on the next walk after it commits. | Labels never overlap: small slices move to the legend (or a leader line). | #021, #086 |
| UIC-11 | O3 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | The accounts pie still draws 4 or 11 slices in a narrow grey ramp; neighbouring slices cannot be told apart. TO-IV-e-70 (merged 602757a8) moved the asset-class hues, not this palette. | Adjacent slices are distinguishable at a glance (a palette with enough separation for 11+ accounts). | #021, #086 |
| UIC-12 | O3 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | The COT eleven-account client's negative account (-4.59% of the client) still sits in the accounts table and legend beside the pie, and the table's shares include it. **In flight:** ~D's closer-drive edit is in the portal working tree, UNCOMMITTED (mtime 18:03-18:04Z, after this walk's Identity and Holdings steps): DrillTree.tsx partitionPieRows. Not walked; grade on the next walk after it commits. | A negative account is shown as a separate, labelled line (never as a pie slice), and the pie's shares sum to the positive total it states. | #086 |
| UIC-13 | O3 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | For the COT eleven-account client, Over what shows 10 rows and cuts the eleventh in half; there is no 'show all'. **In flight:** ~D's closer-drive edit is in the portal working tree, UNCOMMITTED (mtime 18:03-18:04Z, after this walk's Identity and Holdings steps): IdentityCard.tsx OVER_WHAT_SHOWN + 'Show all'. Not walked; grade on the next walk after it commits. | Every account is reachable from Over what (a 'show all' or a scroll affordance); no row is clipped. | #066, #086 |
| UIC-14 | O4 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | Source lines still name internal producers: Allocation and Securities map read 'Source: holdings_snapshot.build_orion_eclipse_meshed.', Performance reads 'Source: opal-gips-engine.', and the category card reads 'Source: Opal Capital Analysis.' rather than the data source. | The source line names the data source in client words (for example 'Black Diamond, as of ...'). | #040, #093, #134 |
| UIC-15 | O3 | 2.0.0_SA_COO~M | NOT_MET | NOT_MET | The Models dialog lists bare tickers with no security names; the securities table repeats the ticker in the name column (including 'FID:CASH'). | Every security shows its name beside its ticker. | #038, #027 |
| UIC-16 | O3 | 2.0.0_SA_COO~M | NOT_MET | NOT_MET | INF account labels still read '... / INDIVIDUAL RETIREMENT AC' on Identity, the pickers, the pie and Analysis. | An account's type reads in full ('Individual Retirement Account'). | #021, #009 |
| UIR-34 | O3 | 2.0.0_SA_COO~D | NOT_MET | n/a | Drilling an INF account opens a level with one row (one model) drawn as a one-slice pie; the COT drill does the same under 'Client'. | A drill level with one child is skipped (or shown as a line, not a pie). | #022, #025 |
| UIW-0928-05 | O3 | 2.0.0_SA_COO~D | NOT_MET | n/a | The All-accounts securities table for the INF four-account client lists dozens of model constituents at 0.00% and $0.00 (positions the accounts do not hold), making the page about 9,600 px tall. | The securities table lists only positions with a non-zero amount, or folds the zero rows into one stated line. | #027 |
| UIW-0928-01 | O7 | 2.0.0_SA_COO~D | NOT_MET | n/a | Choosing an account from the Holdings picker intermittently draws the account's total and category card but an EMPTY client-level table ('Supervision & Advisory', '% of the client', no rows): 5 of 13 account views captured (INF and COT). The other 8 show the account's rows under '% of this account'. | Every single-account view lists that account's rows (or a loading state until they arrive); an empty header-only table never shows beside a non-zero total. | #030, #031, #095, #097, #098 |
| UIW-0928-02 | O7 | 2.0.0_SA_COO~D | NOT_MET | n/a | On one COT account's view the 'Client' category card stretches to about 1,400 px of empty space, with its figure at the foot. | A category card is as tall as its content. | #097 |
| UIW-0928-03 | O7 | 2.0.0_SA_COO~D | NOT_MET | n/a | One COT account's own view reads Total Assets $0.00 with no rows; no COT account holds zero (the table's eleven rows are all non-zero, one negative). | An account's own view states that account's value; a negative account shows its negative value in words, never $0.00. | #095, #086 |
| UIC-17 | O4 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | 'About this scope' shows 'SCOPE AS OF: unknown' for all three clients. | The scope panel shows a real date or omits the field. | #005, #066, #133 |
| UIW-0928-04 | O4 | 2.0.0_SA_COO~D | NOT_MET | n/a | Opening one account's Holdings shows 'Ready  Business date age: 7d' over the raw code HOLDINGS_READY before the page fills (walker hit in both walks today, never registered). | The Holdings loading or ready state carries no system code; a data age, if shown, is in words against the trading calendar. | #153 |
| UIR-26 | O8 | 2.0.0_SA_COO~M | NOT_MET | n/a | Every account of a client carries the same label: eleven identical COT labels, three identical 49F labels, four identical INF labels, on Over what, both pickers, the pie legend and the Analysis account list. | Each account row shows its own masked tail and type. | #086, #134, #021, #124 |
| UIR-03 | O8 | 2.0.0_SA_COO~M | PARTIAL | n/a | A multi-account client now appears once, but the option's sub-line names ONE account's tail and type for the eleven-account client. | Each option names a client in client language; a client with several registrations appears once; no raw type code in the option. | #064 |
| UIR-23 | O8 | 2.0.0_SA_COO~M | NOT_MET | n/a | Holdings read as of 2026-09-22 on Monday 2026-09-28; the trading frontier (T-1) is Friday 2026-09-25, three trading days later. | Holdings read as of the last trading day (T-1), on a scheduled publication. | #021, #153 |
| UIR-48 | O8 | 2.0.0_SA_COO~M | NOT_OBSERVED | n/a | Not re-walked today (the clients walked did not reach it); carried as NOT MET from the 09-27 grade. | Model amounts are the sum of the positions held in that model (or are labelled as target allocations), and the residual is the true unassigned remainder. | none (not reached on this walk) |
| UIR-50 | O8 | 2.0.0_SA_COO~M | NOT_OBSERVED | n/a | Not re-walked today; carried as NOT MET from the 09-27 grade. | Every security the ETF Classifier table lists shows its classifier tag, never a collapsed class. | none (not reached on this walk) |
| UIW-0928-06 | O8 | 2.0.0_SA_COO~P | NOT_MET | n/a | Moving the COT eleven-account client from Performance to Holdings, POST /selections answered HTTP 500 once and the page logged 'IrRequestError: investor-reporting selection-create failed'; the next POST answered 200 and the page recovered. | Selection create answers every valid scope; a transient failure retries without a page error. | none (not reached on this walk) |
| UIR-40 | O9 | 2.0.0_SA_COO~D | NOT_MET | n/a | Pages still carry several full-width navy bands: 3 on the empty page, 7 on INF Holdings, 4 on 49F Performance. | One navy band per page (C3). | #001, #021, #134 |
| UIR-45 | O9 | 2.0.0_SA_COO~D | NOT_MET | n/a | Two date formats on one screen: 'September 22nd, 2026' beside '2026-09-25' in Identity, and 'Answered 2026-01-02' beside 'Answered January 2nd, 2026' on Performance. | One date format per page. | #005, #134 |
| UIC-18 | O5 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | Pressing 'Multi-Comp' leaves 'Variant: Overview (0 comparisons)' and shows 'Multi-Comp does not match 0 comparison(s); Overview does.'; the pressed card is barely distinguishable. | Pressing a card selects it visibly and the form asks for what that variant needs (for example 'Add at least two models'); no system sentence. | #128 |
| UIC-19 | O5 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | For multi-account clients the default report title still names ONE account ('<client> <one account> -- Overview'), and the title field is cut with trailing asterisks. | The default title names the client (and the variant), never one account of several. | #128, #064 |
| UIC-20 | O5 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | 'Enter the report recipient (up to 200 characters).' shows as a red error on load, before anything is typed. | Required-field messages appear after the user tries to generate (or leaves the field), not on load. | #124 |
| UIC-21 | O5 | 2.0.0_SA_COO~D | NOT_MET | NOT_MET | The comparison placeholder is still cut: 'Opal model or ETF symbo'. | No placeholder or label is truncated at 1440 px. | #128 |
| UIC-22 | O5 | 2.0.0_SA_COO~D | NOT_OBSERVED | NOT_OBSERVED | The snapshot line read 'as of 2026-09-22 Ready' on every capture; the transient before the read answers was not caught. | Analysis shows a loading state until the snapshot read answers; a refusal only after it answers. | #124 |
| UIC-23 | O6 | 2.0.0_SA_COO~D | PARTIAL | NOT_MET | TO-IV-e-74 landed: each row names the client and states its status in words ('Unavailable -- needs attention'). Still open: every row shows 'Open REQ-<hash> . revision 1', the READY job reads 'Ready -- ANALYSIS_READY', a running job reads 'Loading -- Running -- in progress', no row carries its variant or date, the list is not labelled as all requests for an admin, and 'No job submitted from this browser yet.' sits beside six listed requests. | The list shows the viewer's own requests (or is labelled as all requests for an admin), each by client name, variant and date, with a status in words; a READY job reads Ready. | #128 |

Grades: NOT_MET 27, NOT_OBSERVED 3, PARTIAL 5. Owners: 2.0.0_SA_COO~D 25, 2.0.0_SA_COO~M 7, 2.0.0_SA_COO~P 3. Shots are `20260928T174953Z#<n>` under the gitignored `tmp/ui-walk/`.

## Part III -- the bar (qualitative)

An advisor who opens any tab for a client with one account or eleven sees a finished page. Every figure is real and belongs to the account chosen. Every gap is one plain sentence. Every chart can be read without hovering. Every account can be told apart. No word on the page was invented by a system.

## Part IV -- the new findings, with cause

- **UIW-0928-05** (DSGN_IRPTV1, 2.0.0_SA_COO~D): The All-accounts securities table for the INF four-account client lists dozens of model constituents at 0.00% and $0.00 (positions the accounts do not hold), making the page about 9,600 px tall. *Cause (inferred):* The table appears to join the model's constituent list rather than the held positions; data owner ~M if the snapshot carries the zero rows.
- **UIW-0928-01** (DSGN_IRPTV1, 2.0.0_SA_COO~D): Choosing an account from the Holdings picker intermittently draws the account's total and category card but an EMPTY client-level table ('Supervision & Advisory', '% of the client', no rows): 5 of 13 account views captured (INF and COT). The other 8 show the account's rows under '% of this account'. *Cause (inferred):* Holdings GETs all returned 200; the empty view keeps the client-level shape, which suggests the drill tree's current node is not re-pointed to the newly chosen account on some selections (a render race, not a data gap).
- **UIW-0928-02** (DSGN_IRPTV1, 2.0.0_SA_COO~D): On one COT account's view the 'Client' category card stretches to about 1,400 px of empty space, with its figure at the foot. *Cause (measured):* 
- **UIW-0928-03** (DSGN_IRPTV1, 2.0.0_SA_COO~D): One COT account's own view reads Total Assets $0.00 with no rows; no COT account holds zero (the table's eleven rows are all non-zero, one negative). *Cause (inferred):* By position it is the third picker option, which matches the third table row, the negative account; a negative total floored or dropped to zero.
- **UIW-0928-04** (DSGN_IRPTV1, 2.0.0_SA_COO~D): Opening one account's Holdings shows 'Ready  Business date age: 7d' over the raw code HOLDINGS_READY before the page fills (walker hit in both walks today, never registered). *Cause (measured):* 
- **UIW-0928-06** (IRPT_BCKEND, 2.0.0_SA_COO~P): Moving the COT eleven-account client from Performance to Holdings, POST /selections answered HTTP 500 once and the page logged 'IrRequestError: investor-reporting selection-create failed'; the next POST answered 200 and the page recovered. *Cause (measured):* Walk netlog line 622 of 847 and findings.json console_errors; one occurrence, not reproduced. Filed as an IRPT_BCKEND surprise row, owner ~P (irpt-directory-search carries selection create).

## Part V -- closed or not reached on this walk

| id | verdict | note |
|---|---|---|
| UIC-01 | MET (held) | The missing benchmark and values are one plain line. |
| UIC-02 | MET (held) | The daily series sits behind one click. |
| UIC-08 | MET (held) | Refusals name the reason and who can fix it, codes behind 'Details'. |
| NEW-02 | NOT REPRODUCED | The COT eleven-account pie draws on 28f5118c (#086). Cause of the morning's blank pie not measured; ~D's in-flight partitionPieRows removes the sum<=0 path that blanks it. |
| UIR-30 | MET | The firm shows once on Identity (TO-IV-e-73 merged). |
| UIR-37 | MET on screen | Models are lavender and the allocation bar grey; asset classes keep blue, green and orange (#040, TO-IV-e-70). |
| UIR-32 / UIR-49 | NOT WALKED | The two-account client whose strategy tail differed was not in today's three-client walk. |

Walker hits dropped after reading the screenshot:

- pie wedge gap on the 49F account's model pie (#154, #155): The three shares sum exactly to the account total; the gap matches a capture taken mid-animation. Not confirmed; re-check on the next walk.
- design:contrast hits (Analysis, Models dialog): Not confirmed by eye, as on 09-27.
- console '[vite] Failed to reload DrillTree.tsx': ~D's mid-edit hot reload on the shared working tree, not a product defect.

## Part VI -- routing

- **DSGN_IRPTV1 findings** go to 1.0.0_SA_CTO and 2.0.0_SA_COO~D. Under the FAST lease each one is ~D's next closer-drive item (CTO placement `CTO_PLACEMENT_20260928_174xZ`).
- **IRPT_BCKEND findings** are surprise rows on the owning workstream: NEW-01 is S176/S177 (~P), UIR-23 is S152 (~M), and UIW-0928-06 is a new row (~P). UIC-06, UIC-15, UIC-16, UIR-03, UIR-26, UIR-48 and UIR-50 are already on their owners' records.
- ~D's suggested order: land the three in-flight items (UIC-10, 12, 13); then the per-account view (UIW-0928-01..03), because it shows a wrong or empty answer; then the no-system-words set (UIC-03, 09, 14, 17, UIW-0928-04); then Analysis (UIC-18..23).

## Part VII -- what this does not claim

- Three clients, one deep pass each, at 1440 px. A finding seen on one client may not hold for all, and one missing here may exist on others.
- Nothing behind a submit (a generated report, an export, an upload) was walked.
- The 49F Holdings steps may have run under a partial hot reload of ~D's in-flight edit. No finding here rests on those steps alone.
- UIW-0928-01 is intermittent: 5 of 13 captures. Its cause is inferred, not traced to a line.

## Refs

- REGISTER `docs/briefs/irpt-ui-remaining-findings-20260928.json`; morning status `docs/briefs/irpt-ui-cleanup-status-20260928.md`; prior registers `docs/briefs/irpt-ui-cleanup-findings-20260927.json`, `docs/briefs/irpt-ui-review-findings-20260926.json`
- PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`; surprise channel `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`
- Coverage: `python docs/briefs/irpt-ui-review-coverage-check.py --register docs/briefs/irpt-ui-remaining-findings-20260928.json docs/briefs/irpt-ui-remaining-brief-20260928.md`
