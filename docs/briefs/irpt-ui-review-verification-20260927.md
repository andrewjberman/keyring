# Investor Reporting UI review -- walk verification, 2026-09-27

**By:** 4.0.0_SA_CRO, `/ui-walk` on Andrew's word. **Register:** `docs/briefs/irpt-ui-review-verification-20260927.json`, which this page is generated from. **Build:** portal local DEV `3f76cdb2`, the round-7 product code; origin/DEV `c3dd9ca9` carries none of it. **Clients:** the Cottonwood two-account client and the 49F three-account client, at 1440 px. The screenshots are numbered below; they stay local and gitignored.

## The answer

- **DSGN_IRPTV1 (2.0.0_SA_COO~D), 45 items all marked done:** **28 MET** on the page, **17 NOT MET**.
- **IRPT_BCKEND (2.0.0_SA_COO~M), 5 items:** 0 met, 5 not met. UIR-23, UIR-26 and UIR-50 Part A ride Monday's R4 publication.
- **7 new findings** from this walk (UIW-0927-01 to -07).
- A walk grades nothing. The CVO still grades round 7 on its own evidence.

## NOT MET -- DSGN_IRPTV1 (17)

| id | what the walk showed | shots |
|---|---|---|
| UIR-04 | Each option carries the firm TOKEN ('cottonwood', '49financial'), not its display name; the row layout is now uniform. | 003 |
| UIR-06 | Before a client is chosen the Performance area still shows figures (+10.00%, +2.00%, $2,500,000.00), now badged SAMPLE. | 001 |
| UIR-11 | The SAMPLE cards still render behind the open search list. | 003 |
| UIR-13 | The line reads 'cottonwood (Client)': the punctuation is fixed, the lower-case firm token is not. | 004 |
| UIR-15 | Both picker entries read '****9237 / BROKERAGE'; each shows 'value pending' or the whole refusal sentence, never a value. The 49F client's three entries are identical too. | 007, 008, 034 |
| UIR-17 | Over what lists the accounts with identical labels (2 x '****9237 / BROKERAGE', 3 x '****9079 / IRA'); distinct labels wait on UIR-26's data fix. | 005, 031 |
| UIR-20 | Export is live (purple) on the Analysis tab with no report generated; it is grey on Performance and Holdings. | 026, 029 |
| UIR-25 | The accounts pie draws every slice in the same cyan (#06b6d4) for both clients. | 009, 035 |
| UIR-30 | The firm token chip ('cottonwood', '49financial') still sits at the top right of Holdings. | 009, 035 |
| UIR-32 | The breadcrumb reads 'All holdings > Rebalancer strategy' and skips the account; the strategy shows '*9238' against the account's '****9237'; two masking styles. | 010 |
| UIR-34 | A level with one child still draws a one-slice pie (both clients). | 010, 040 |
| UIR-37 | Blue marks a model (Opal Conservative Growth; Opal Long Term) and Equity on the same page; orange marks a model (Opal Ultra Short-Term Income; Opal Short-Term) and Alternatives. | 010, 014, 040 |
| UIR-40 | With 'More holdings views' open the page carries four navy bands (Identity, Allocation, Securities map, Securities); the empty sample page carries three. | 001, 014, 015 |
| UIR-41 | With all accounts, the map's chips repeat each model once per account ('Model: Opal Conservative Growth' twice, and so on) with no account grouping. The one-account view passes. | 015 |
| UIR-45 | Two date formats remain ('September 22nd, 2026, 5:00p ET' and '2026-09-22'); the source line still reads 'Source: Opal Capital Analysis.' | 005, 010, 014 |
| UIR-46 | As UIR-25. | 009 |
| UIR-49 | As UIR-31 (met) and UIR-32 (not met). | 010 |

## NOT MET -- IRPT_BCKEND (5)

| id | what the walk showed | shots |
|---|---|---|
| UIR-03 | Options are still account registrations with raw type codes ('S1', 'IRA') and a masked tail. | 003 |
| UIR-23 | Holdings are still as of 2026-09-22 on Sunday 2026-09-27 (T-1 is Friday 2026-09-25); R4 enables the scheduled publication Monday. | 009 |
| UIR-26 | Account rows still carry identical labels; the own-mask labels ride Monday's R4 publication. | 009, 035 |
| UIR-48 | Model amounts are still exact target shares of the account (the model rows read exactly 60.70% / 16.00% / 20.00% / 3.30% of the account). | 010 |
| UIR-50 | PHYS still shows as Alternatives (orange) and VXX as Alternatives; the class writes ride Monday's R4 (Part A) and B2. | 014, 040, 051 |

## MET -- DSGN_IRPTV1 (28)

| id | what the walk showed | shots |
|---|---|---|
| UIR-01 | The search box focused and empty opens no list. | 002 |
| UIR-02 | The open list sits above the tab strip, every option fully visible. | 003 |
| UIR-05 | The empty-state line reads 'Choose a client to see its firm and accounts.' | 001 |
| UIR-07 | In Global mode, 'anna thiessen' lists the exact client first of 13 (server fix plus the page's Global merge). The reversed order was not walked. | 003 |
| UIR-08 | No option is covered; the occlusion check found 0. | 003 |
| UIR-09 | No spell-check underline on the typed query. | 003 |
| UIR-10 | The list states '13 MATCHED ACROSS FIRMS' and tags every option with its firm. | 003 |
| UIR-12 | WHO shows the client's name only; the accounts sit under Over what. | 004 |
| UIR-14 | The firm control reads 'Global (All)', which says the list is all firms. | 004 |
| UIR-16 | The Performance picker lists accounts only; no 'All accounts'. | 008 |
| UIR-18 | The refusal is plain words; its code sits behind 'Details'. | 007 |
| UIR-19 | A status icon beside navy text on white; no tinted block. | 007 |
| UIR-21 | The account picker and the period controls share one panel. | 007 |
| UIR-22 | The system facts sit behind 'About this scope'. | 005 |
| UIR-24 | The pie labels its slices with the table's names. | 009 |
| UIR-27 | Supervision and Advisory are not on the face; they sit behind the scope and report-details clicks. | 009 |
| UIR-28 | The card shows 'Unique accounts'; source dates and coverage are one click away, in one format there. | 009 |
| UIR-29 | One money format; the client total appears once. | 009, 014 |
| UIR-31 | Drilling into an account sets the account picker to it, and the two agree. | 010 |
| UIR-33 | Each view uses one base (the pie and the table agree at each level); the column still says only '% of total'. | 009, 010 |
| UIR-35 | No amount wraps at 1440 px. | 009, 014 |
| UIR-36 | As UIR-33. | 010 |
| UIR-38 | The chips are client language ('Primary', 'Custom', 'Opal model') and do not wrap. | 010 |
| UIR-39 | With all accounts, Allocation shows 2 of 2 bars (57.17% / 42.83%). | 015 |
| UIR-42 | Small items group into one labelled 'Other' tile. | 014, 015 |
| UIR-43 | Each security appears once in the map. | 014, 015 |
| UIR-44 | Every map colour is in the legend (Fixed Income, Equity, Alternatives, Other), and they are distinct. | 014, 015 |
| UIR-47 | As UIR-33. | 010 |

## New findings (proposed owner DSGN_IRPTV1, 2.0.0_SA_COO~D)

| id | surface | observed | acceptance | shots |
|---|---|---|---|---|
| UIW-0927-01 | holdings / securities table | Cash rows show 'not supplied' in the Ticker column (the 49F three-account client, 3 rows). | Cash rows name themselves ('Cash') and never print 'not supplied'. | 040 |
| UIW-0927-02 | analysis / inputs | The analysis input lists the included accounts as 'Account', 'Account' with no label or tail. | Each included account shows the same label and value the account picker shows. | 026, 029 |
| UIW-0927-03 | identity / loading | Right after a client is picked, the header reads 'value pending', 'not supplied', '0 accounts' until Holdings loads; the directory search answered UNEXPECTED twice at that step. | While a client loads, the header shows a loading state, never words that read as missing data. | 029 |
| UIW-0927-04 | performance / picker | The account picker's selected entry carries the whole refusal sentence ('... temporarily unavailable right now. It becomes available again once ...'). | A picker entry shows the account's label and value; a refusal is stated once, in the canvas. | 008 |
| UIW-0927-05 | holdings / report details | Report details shows the raw code 'HOLDINGS_READY' and 'Classification unknown for 41 of 41 holdings nodes -- ... partitions are shown as withheld'. | Report details speaks client language: no system codes, no 'nodes' or 'partitions'. | 014 |
| UIW-0927-06 | holdings / allocation | Allocation truncates the model label ('Rebalancer strateg...'). | No label is ellipsized at 1440 px. | 014, 015 |
| UIW-0927-07 | securities map / legend | The grouped small-items tile and the 'Other' asset class share one purple and one word. | The grouped tile reads 'Smaller holdings' (or similar) in a colour no class uses. | 014, 015 |

## Walker false positives (fixed in `.claude/skills/ui-walk/walk.mjs`)

- search:ranking '#5 of 17' for the Cottonwood query: the check counted the Firm <select> options (role=option) ahead of the list; the page showed the exact client first of 13. Fixed in walk.mjs (rank within the search's own listbox).
- search:ranking '#16 of 31' for the 49F query: the walker typed the second name onto the first query, so the box held both names run together. Fixed in walk.mjs (select-all + delete, then verify empty).

## What this does not claim

- Two clients, one walk. UIR-07's reversed order ('thiessen anna') was not walked.
- The 49F account's Performance figure never rendered within the walk's wait ('Loading'); this may be the engine's ~10 s compute, not a defect.
- UIR-37's 'canonical model colour' limb was not checked against `portal/src/lib/modelPortfolioColors.ts`; the verdict rests on the one-hue-two-meanings limb.
