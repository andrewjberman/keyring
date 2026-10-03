# DSGN_AMGTV1 -- Security Analysis UI/UX: one card style, a real timeline, pockets and modals, a collage, a "what changed" moment, rolling windows: MIDSTREAM brief (L1)

```
BRIEF PATH        docs/briefs/dsgn-amgtv1-security-analysis-uiux-brief-20261002.md
PROJECT           DSGN_AMGTV1 (D13), midstream
EXISTING PRD      org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md v0.8
ROUTE             4.0.0_SA_CRO~Z -> 1.0.0_SA_CTO~Z (filter, fold into /canonical-flow) -> 2.0.0_SA_COO~D
ANDREW'S WORD     org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261002_173xZ_SECURITY_ANALYSIS_UIUX_WALK_BRIEFS_TO_CTO_Z.md @a48c546a1c
FINDINGS REGISTER docs/briefs/amgt-security-analysis-ui-findings-20261002.json (36 findings, SAUX-01..36; the table below is generated from it)
SIBLING BRIEF     docs/briefs/amgt-harvst-news-sentiment-and-windows-brief-20261002.md (backend: sentiment and windows, 2.0.0_SA_COO~H)
EVIDENCE          org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/SECURITY_ANALYSIS_UIUX_20261002/PATTERN_MAP.md (current code + in-pattern components, file:line)
                  org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/SECURITY_ANALYSIS_UIUX_20261002/SENTIMENT_BUBBLE_FINDINGS.md (Topic Cloud layout and colorway, FinBERT)
WALKS             tmp/ui-walk/20261002T174112Z (this seat, 212 shots) and tmp/ui-walk/20261002T180024Z (another seat's walk on the same build); local, never committed
MEASURED AT       2026-10-02 17:41Z-18:1xZ, localhost:5174 dev build; portal working copy DEV a730d8ce (the running bundle's commit was not recorded)
```

## Andrew's items (verbatim in the record; numbered there N1-N10)

| N | his words, shortened (the record is the authority) |
|---|---|
| N1 | Lead Panel: light cards superimposed on the dark card. Stick to one style: light as in the /philosophy header, or the standard dark as in the /advisor-intelligence header and chart cards. /advisor-intelligence /book at L0 is a layout reference. |
| N2 | The timeline spine is poorly developed visually. Use the in-pattern chart library. |
| N3 | Hover a date and see key metrics (articles, sources, mention count) in the tooltip. |
| N4 | A layer of headlines and earnings releases, whatever was happening at a big spike, laid out chronologically on the spine. |
| N5 | Selected-date news and the most current news run together. Separate them; recent news probably goes above the spine. |
| N6 | Card everything into clear pockets with easy-to-read text. The main feature opens a modal in an existing pattern (the Market Overview topic-cloud analysis modal). |
| N7 | One bubble per security, alphabetical, too much scrolling. Use a collage like Topic Cloud's, centred on the largest. |
| N8 | The news scanner's FinBERT scoring in the Topic Cloud sentiment colorway (backend half: the sibling brief). |
| N9 | Model "what changed": larger, more of a moment, progressive disclosure, in-pattern components. |
| N10 | Replace month/earlier-month with rolling 30-day, 90-day and 365-day views. |

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- **Not read:** the project's task orders, `phase` and `blocking`.
- **Read:**
  - the PRD's ENDPOINT (FWD-1 to FWD-24);
  - the served page (two signed-in walks);
  - the portal code, for the pattern map.
- **Where it bent:**
  1. This seat read the RESAPP round-61 analysis this morning. It carries DSGN round-21 and round-23 rulings (page-side
     reason wording, `headline_reason`). So the brief knows the page owns reason wording. That is a ruling, not a task
     order, but it is branch knowledge.
  2. The second walk (`tmp/ui-walk/20261002T180024Z`) was run by another site-Z seat. Its existence says someone is walking
     this page today. Its screenshots are served reality and are used as such.
  3. The pattern fork read component code that this morning's DSGN rounds changed. A pattern found that way can ratify
     in-flight work. The table's "in-pattern" column was checked against components that predate this project (the
     /philosophy, /advisor-intelligence and Market Overview components), not against Security Analysis's own new components.
- **The endpoint is NOT unchanged.** Three outcomes in the ratified text collide with Andrew's word today, and the CTO decides
  each (section 0.1). The rest enriches the existing outcomes.

### 0.1 Where Andrew's word meets the ratified ENDPOINT (the CTO's fold)

| ENDPOINT outcome | what it says today | Andrew's word today | the collision |
|---|---|---|---|
| **FWD-12 x FWD-23** | FWD-12: "the identity header is that [ONE] band". FWD-23: "the panel's header and the selected-name header are built from the /philosophy fixture-card face". | N1: one style, never light cards on a dark card. | **Together these two outcomes produce the defect.** FWD-23's light cards are placed inside FWD-12's band (SAUX-01, SAUX-02). One of them changes. **Light:** FWD-12's band leaves the header, and DESIGN.md C3 names light as the conformant direction (register `references.contract_note`). **Dark:** FWD-23's /philosophy face leaves the header. Either way it is an ENDPOINT change, so `3.0.0_SA_CVO~Z` re-signs. |
| **FWD-21** | One bubble per security, sized for "the selected calendar month"; "a cursor steps this month, M-1, M-2". | N7 a collage centred on the largest; N8 sentiment colour; N10 rolling 30/90/365. | One bubble per security STAYS. Chatter is still only bubbles, which keeps Andrew's 10-01 "no other views". The calendar-month cursor and the layout change, and colour is added: an ENDPOINT restatement. |
| **FWD-22** | Horizontal bars, "one per security". | N7 names "the various chatter/price views" for too much scrolling. 94 bars make a 2,618px page (SAUX-20). | Bars STAY (Andrew 10-01: price is always bars). Whether the face shows the top movers with an expand, or all 94, is the CTO's call. **INFERRED** from N7's scroll complaint; Andrew did not name price bars specifically. |
| FWD-5 | "a dated line shows its articles, events and headlines". | N2-N6. | Enrichment, not a collision. The DONE WHEN gains a chart, hover metrics, a marked event layer, pockets and a modal. |
| (none) | The ENDPOINT has no outcome for the Model's "what changed". | N9. | **A new outcome** (O6 below). |

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1 of this addendum).** A PM opens Security Analysis on the default 30-day window. They see every
chattered name in one collage on one screen, and pick Boeing. On Boeing's header they read one card style. They hover the
timeline chart's biggest spike and read that day's articles, publishers and mentions. They see the event marked at the spike,
and click it to read the day in a modal. Coarse grain: one name, the default window, the live build.

The outcome numbers match the register's `outcome` field, so every SAUX row cites one.

### O1 -- A PM reads Security Analysis in one card style, top to bottom
- No light card or white control strip sits on a dark container, and the page carries at most one band.
- Light or dark is the CTO's pick (0.1). The references are the /philosophy header (light) and the /advisor-intelligence header
  and chart cards (dark). The /advisor-intelligence `/book` L0 composition (a KPI row, then the main chart, then a detail row)
  is the layout reference for the header region.
- N1. SAUX-01, 02, 05, 14.

### O2 -- A PM reads a company's coverage over time as a real chart, and sees why it spiked
- The timeline is a recharts chart (the portal's library, `portal/package.json`, recharts ^3.7.0) at a readable height, with
  dated axes and data colours. A status colour never paints a data series: today almost every bar is the "NOT SEARCHED" red
  (SAUX-07).
- Hovering a day shows the day's articles, publishers and mention count in the portal's one tooltip look (`DataTooltip`). The
  payload already serves these per day (PATTERN_MAP N3).
- Events and earnings releases are marked ON the chart at the spikes, chronologically, and each opens its detail. The harvest
  events are served today. Earnings dates are not (sibling brief PART II; SAUX-10).
- N2, N3, N4. SAUX-06, 07, 08, 09, 10.

### O3 -- A PM finds each kind of fact in its own pocket, and opens detail in the estate's modal
- Recent news sits in its own card, above the timeline. The selected day's articles open in a modal, not inline beneath the
  chart.
- Each pocket is a panel with a header. Article rows read in words, not system metadata.
- The modal is the page's shared `HeroDialog` (already used by `HeaderCards` and `ThesisCards`), carrying the content structure
  of Market Overview's `KeywordSentimentModal`: a summary, then drivers, then articles behind a toggle. `KeywordSentimentModal`
  itself is a hand-built overlay with translucent ink that breaks C5.8 on a light ground (PATTERN_MAP shared facts).
- N5, N6. SAUX-11, 12, 13, 15.

### O4 -- A PM sees every chattered name on one screen, the biggest at the centre
- Chatter is a collage: sorted by size, the largest at the centre, smaller outward. That is the Topic Cloud placement rule
  (`@visx/wordcloud`'s archimedean spiral).
- Built as a small deterministic spiral placement with no new dependency (`d3-hierarchy` and `d3-force` are absent), unless the
  CTO rules a dependency in.
- Labels never clip or run together. Price shows its movers without a 2,600px page (the CTO's call, 0.1).
- N7. SAUX-16, 17, 20.

### O5 -- A PM reads each name's coverage tone in Topic Cloud's colours
- Each bubble carries its period's tone in `getSentimentColor()`'s colorway (`TopicCloud.tsx:44-90`), extracted into ONE shared
  module. The portal holds three private copies of it today.
- A name with no scored articles is slate, and its hover says so.
- **The data half** (FinBERT over harvested articles, tone and voters on the payload) is the sibling brief's.
- N8. SAUX-18, 19.

### O6 -- A PM sees what changed in the model as the moment of the Model tab
- "What changed" sits at the top of the Model tab, in a panel with a header. It shows count tiles, then the changed lines as
  signed changes, then per-line detail on demand.
- It defaults to the latest version against the one before it, not the oldest against the newest (SAUX-23).
- Version times print in ET like the rest of the page.
- The data is already served (`compare.denominators`, `compared.changed[]`, PATTERN_MAP N9).
- N9. SAUX-23, 24, 25, 26.

### O7 -- A PM picks the last 30, 90 or 365 days on every period-bound face, and reads which window is shown
- 30D / 90D / 365D presets replace "Earlier month" / "Later month", rendered through the shared `Segmented` control.
- The labels and days come from the in-pattern `IndexPerformanceModal` presets (`IndexPerformanceModal.tsx:39-53`); Market
  Overview's 90D/1Y/3Y and Advisor Intelligence's Window presets are the same family.
- Every face states its window, Price included (SAUX-21).
- When the store is shorter than the window, the face says where the window starts (sibling brief O4).
- N10. SAUX-21, 27, 28.

### O8 -- A PM reads plain words and figures that agree with each other
- No system wording or raw code on the face.
- One name format, one money format and one time zone per page.
- Every figure carries its as-of date.
- No two figures for the same thing disagree without a label: Boeing reads -6.5% in the list and "#72, -4.71%" in its header
  (SAUX-22), and three market caps print on one page (SAUX-34).
- Inferred from N6's "easy to read text". SAUX-03, 04, 22, 29, 30, 31, 32, 33, 34, 35, 36.

## PART II -- WHERE THE BOUNDARY SITS

| owned here (DSGN_AMGTV1, 2.0.0_SA_COO~D) | relied on, owned elsewhere |
|---|---|
| Every face, layout, chart, tooltip, modal, control and word on `/security-analysis`, and the one shared sentiment-colour module | **AMGT_HARVST (2.0.0_SA_COO~H):** FinBERT tone, rolling-window counts, event density (sibling brief) |
| | **AMGT_RESAPP (2.0.0_SA_COO~Z):** the served route's data defects. These include the price-move disagreement (SAUX-22), the recent-news window (SAUX-12), model provenance (SAUX-25) and the name formats (SAUX-29). |
| | **Earnings and corporate-event dates (SAUX-10):** no owner yet. The CTO names one. |
| | **The ui-walk instrument (SAUX-35's walker side, the `--thread` bar wait):** the walker skill's owner. It does not block this project. |

## PART III -- THE QUALITATIVE BAR

- Put beside /philosophy (or /advisor-intelligence, whichever the CTO picks), a reviewer cannot point to a card that belongs to
  the other family.
- A PM explains a spike from the chart alone, without reading a list beneath it.
- A PM sees the whole period's chatter without scrolling, and can name the most-discussed name and its tone at a glance.
- A PM reading "what changed" can say, in one sentence, what moved in the model and by how much, without opening a list of
  timestamps.
- No figure on the page needs a second figure to be understood, and no two figures for one thing disagree without saying why.

## PART IV -- THE SUBSTRATE (findings; PATTERN_MAP.md carries file:line for each)

| # | finding | claim |
|---|---|---|
| S1 | The chart library is **recharts ^3.7.0**; there is no apexcharts (CTO msg 28611 fact 1; `portal/package.json:27-28`). The timeline is ALREADY a recharts `BarChart`, at 140px, with no date ticks, mounted inside the band. | measured |
| S2 | **No annotated time-series chart exists in pattern:** 0 files use `ReferenceDot`, and `ReferenceArea` only shades bands. The event layer is new composition from recharts' own `ReferenceArea`/`ReferenceLine`/`ReferenceDot`, with no new dependency. | measured |
| S3 | The light reference is `GraphicCard` on the canvas (/philosophy `PhilosophyPillars.tsx:162-213`). The dark reference is `PartnerAnalytics` "Assets Overview" (`Panel variant="mixed"` + `PanelHeader` + a recharts `ComposedChart`). The /book L0 reference is `CanonicalBookView`. | measured |
| S4 | The shared modal is `HeroDialog` (`HeroGraphic.tsx:121`), already on this page. `KeywordSentimentModal` is the content model, not the shell. | measured |
| S5 | The in-pattern rolling preset is 30D/90D/1Y/3Y in `IndexPerformanceModal.tsx:39-53`, rendered here through `Segmented` (`Controls.tsx:105-128`). | measured |
| S6 | The colorway is `getSentimentColor()` (`TopicCloud.tsx:44-90`), with three private copies in the portal (CTO msg 28611 fact 2). | measured |
| S7 | Topic Cloud is a word cloud (`@visx/wordcloud`, archimedean spiral), not circles. No circle-packing library is installed. | measured |
| S8 | The timeline payload already serves per day `articles_total`, the tier counts, `mention_count_total`, `publishers_distinct`, `trailing_7d_sum`, `trailing_30d_sum`, `z_score` and `breakout_ratio`. Only `mention_score` is charted. | measured |
| S9 | The Model compare payload already serves `compare.denominators` and `compared.changed[]`. | measured |

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The CTO's three calls in 0.1: the light-or-dark ground, the FWD-21 restatement, and the FWD-22 trim. FWD-12, FWD-21 and FWD-23
  are ENDPOINT text, so `3.0.0_SA_CVO~Z` re-signs.
- O5 and O7 rest on the sibling brief's served fields (tone, voters, `?days=`, the served window start).
- O2's earnings layer rests on a data owner the CTO names.
- O8's data disagreements (SAUX-22, 25, 29, 34) rest on AMGT_RESAPP.
- A colour rule for the sentiment ramp: C7 reads an ordered scale as a single-hue ramp, and the Topic Cloud ramp is diverging.
  It may need a ruled exemption like C4's (PATTERN_MAP N8). **INFERRED.**

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 17:41Z-18:1xZ on the local build. This ages; do not cut outcomes from it.
- Chatter is 57 names in a 4-column ticker-ordered grid, a 4,153px page. Price is 94 bars, a 2,618px page.
- The timeline is mostly red ("NOT SEARCHED"), its tooltip shows the search state only, and its events are a text list.
- The selected day's articles and the recent news run together in one column.
- "What changed" sits at the bottom of the Model tab, under 19 version timestamps.
- The walker reached every tab only in walk 2. In walk 1, the account menu stayed open and blocked the tab presses (SAUX-35).

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The running bundle's commit. The working copy read DEV a730d8ce.
- That the light ground is Andrew's preference. He offered both; C3 favours light. The CTO picks, or asks him.
- Where earnings dates come from.
- That every page path was walked. A walk is a sample: two names in walk 1, three in walk 2.
- That 8 of the 36 findings are causes: those are marked `inferred` in the register.
- Any decomposition, sequence or cell. That is step 5.

## THE REGISTER -- every finding, generated from docs/briefs/amgt-security-analysis-ui-findings-20261002.json

<!-- REGISTER-TABLE-START -->
| id | Andrew item | outcome | owner | claim | surface | observed | acceptance |
|---|---|---|---|---|---|---|---|
| SAUX-01 | N1 | O1 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | lead-panel | The Lead Panel is a dark container that holds a white control strip (Chatter/Price, All names/Starred only, the ticker search) under its own dark gradient 'What is moving' header, which repeats the page title's 'SECURITY ANALYSIS' as an eyebrow: a light strip superimposed on a dark card, and a band inside a band. | A screenshot of the Lead Panel shows one style throughout: either white panels with navy ink and at most one band on the page (the C3 direction, the /philosophy header style) or an all-dark panel with no white strip or white card inside it. |
| SAUX-02 | N1 | O1 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | name-overlay | The per-name header puts white-bodied cards with dark gradient tops (the 'BA US' identity card and the four PRICE / FINANCIALS / MARKET FEATURES / TRADING TECHNICALS cards) on the dark overlay container, the same light-on-dark mix as the Lead Panel. | The name header renders in the same single style chosen for the Lead Panel (SAUX-01): no white card sits on a dark container. |
| SAUX-03 | inferred | O3 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | name-overlay key figures | Each of the four header cards shows one figure at rest and opens a modal of two or three rows; one of those rows repeats a figure already on the face (Average volume is on the Price modal and on the Trading Technicals card). Four modals for nine figures is an unnecessary layer. | The header shows one key-figures card with every figure at rest (price, market cap, enterprise value, net debt, beta, average volume, short interest), or each opened modal adds only figures that are not on the face; no figure appears twice. |
| SAUX-04 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | financials modal | Hovering Enterprise value in the Financials modal shows a purple tooltip with the raw value '187187.819936', unit 'MILLIONS' and source 'bloomberg-dapi'. | The tooltip shows the formatted value and the source in words ('Bloomberg'), in the standard tooltip style; no unformatted number and no system source id appears. |
| SAUX-05 | inferred | O1 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | name-overlay | The filled purple Refresh button sits on the dark overlay container. | No #5F3BE3 filled button renders on a dark container; Refresh is a secondary control or sits on a white panel. |
| SAUX-06 | N2 | O2 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | mention timeline | The mention timeline is a hand-drawn bar strip: the y-axis runs 0 to 7.6 with no unit, the x-axis prints only the first and last dates, and the caption reads '275 of 275 day(s) rendered (no gap)'. | The timeline renders through the portal's in-pattern chart library with a labelled y-axis (articles per day) and month ticks on the x-axis; the 'rendered (no gap)' caption is gone. |
| SAUX-07 | N2 | O2 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | mention timeline | Almost every bar is red, the legend's colour for NOT SEARCHED (legend: COMPLETE purple, PARTIAL orange, NOT SEARCHED red), so the chart reads as a failure and the colour encodes search state, not mentions. | Bars are drawn in one data-family hue; search completeness is carried by a non-status cue (pattern or opacity, with a legend) or in the tooltip; no status colour paints a bar. |
| SAUX-08 | N3 | O2 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | mention timeline tooltip | Hovering a day shows only its search state ('October 2nd, 2026: partial day -- not the whole story for that day. Searched: Barron's.'): no article count, sources or mention count. | Hovering any day shows the date, article count, distinct publishers, mention count and the strongest headline, in the chart library's tooltip. |
| SAUX-09 | N4 | O2 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | mention timeline events | Coverage events are a text list under the chart ('COVERAGE EVENTS -- PRESS ONE TO OPEN ITS FIRST DAY' and one underlined line); nothing marks a spike on the chart itself, and VLO's timeline has no event element at all (walker check timeline:no-event-element). | Each event appears as a marker on the timeline at its date with a short headline label, chronologically, and pressing the marker opens that day. |
| SAUX-10 | N4 | O2 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | timeline route data | The timeline has no earnings-release layer and VLO has no events at all, so a spike with no multi-publisher burst carries no explanation. | The timeline route serves, per name, dated markers of two kinds -- coverage events with their lead headline and earnings releases with their date -- and a name with no burst still carries its earnings markers. |
| SAUX-11 | N5 | O3 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | selected-day and recent news | The selected day's articles ('SEPTEMBER 8TH, 2026'S ARTICLES, STRONGEST FIRST') and the recent news ('NEWS -- NEWEST FIRST ...') run together in one column with the same type, rules and colour; recent news sits below the day list and below the spine. | Recent news is its own card above the timeline; the selected day opens in its own card or modal, visually distinct from recent news, and the two never share one column. |
| SAUX-12 | inferred | O8 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | recent news data | The recent-news block for September 3rd to October 2nd shows one article (WSJ, September 3rd) while the opened day of September 8th, inside that window, lists 6 articles: the two lists disagree on what news exists. | The recent-news card lists the newest harvested articles for the name across all publishers in its window; every article the day view shows inside that window also appears there. |
| SAUX-13 | N6 | O3 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | day article rows | Each article row carries dense system metadata in small text ('named 15 times', 'in headline: yes', 'in lead: yes', coloured tier letters A/B/C). | Each article row shows headline, publisher and time at rest; mention count, headline and lead flags and tier open in the same modal pattern as the Market Overview topic analysis modal. |
| SAUX-14 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | day status text | 'NOT SEARCHED FOR THIS COMPANY DIRECTLY -- 6 ARTICLES FOUND IN OTHER SEARCHES' and 'NOT SEARCHED ON THIS DAY' are red #BE2D36 text on the dark container, measured 2.59:1; 'PARTIAL DAY -- NOT THE WHOLE STORY FOR THAT DAY' is orange warning-colour text. | No status-coloured text renders below 4.5:1; a search-state note is navy or band ink beside a status icon. |
| SAUX-15 | N6 | O3 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | name-overlay layout | The overlay stacks the company description, the posture line, a fund line, the timeline, the event list, the day's articles, the news, a social line and the chatter and breakout figures, all at rest above the tabs (about 1,100px), so every tab's content starts below the fold; the posture line and 'identity as of September 29th, 2026' repeat on the tabs. | At rest the overlay shows the identity, the key figures and the timeline; description, posture, social and chatter/breakout open from tiles or details; at 1440x900 the active tab's first panel starts inside the first viewport. |
| SAUX-16 | N7 | O4 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | chatter bubbles | Chatter draws one bubble per name in a 4-column grid ordered by ticker; September's 57 names take 15 rows (a 4,153px page), bubble sizes are hard to compare, and each label is larger than its bubble. | The Chatter face draws a packed collage centred on the largest bubble with sizes falling outward (the Topic Cloud layout), every name of the period visible in one panel at 1440x900 without scrolling. |
| SAUX-17 | inferred | O4 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | chatter bubble labels | Bubble labels clip at the panel edge and run into neighbours (a left-edge label loses its first letters; two adjacent labels print as one run-on line). | No bubble label is clipped or overlaps another; a long name wraps or shows in full on hover. |
| SAUX-18 | N8 | O4 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | chatter bubbles colour | Every bubble is the same blue; the face carries no sentiment. | Each bubble's fill encodes the name's article sentiment for the period on the Topic Cloud sentiment scale, with a legend; a name with no score shows a neutral fill and says so in its tooltip. |
| SAUX-19 | N8 | O5 | 2.0.0_SA_COO~H (AMGT_HARVST) | inferred | news-scanner sentiment data | No sentiment value is served for harvested articles or per name, so the page has nothing to colour by. | Every harvested article carries a FinBERT sentiment score with the scorer named, and the chatter route answers per name and period an article count plus a sentiment aggregate built from those scores. |
| SAUX-20 | inferred | O4 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | price bars | The Price face draws all 94 names as bars (a 2,618px page) and clips ten names with no visible full form (for example the Taiwan Semiconductor ADR and International Container Terminal Services). | At rest the Price face shows the top movers each side (gainers and losers) with the full list on demand; no name is clipped without a title or hover revealing it. |
| SAUX-21 | inferred | O7 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | price bars window | The Price face prints moves such as +34.0% and -18.0% with the caption 'Showing the Trending x Price list (movement is measured)' but never states the window the move is measured over. | The Price face states its window in words ('change over the last N days to <date>'), and the window follows the period preset (SAUX-27). |
| SAUX-22 | inferred | O8 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | price move disagreement | The Lead Panel lists The Boeing Co at -6.5% (row 41 of 94 on Trending x Price), while the name's overlay reads 'BREAKOUT (PRICE) #72 / -4.71%, up 16 places'; both say ranked October 1st, 2026. | The overlay shows the same measure and window as the face the name was opened from, or labels each measure and window; one name never shows two unlabelled moves. |
| SAUX-23 | N9 | O6 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | model what-changed | 'WHAT MOVED BETWEEN TWO VERSIONS' sits at the bottom of the Model tab, under a 19-line plain list of version timestamps; it is plain text lines ('Enterprise value: USD 194B to USD 187B') with no signed change, no percentage and no emphasis; it defaults to the oldest against the newest version, and other pairs often read '0 changed'. | 'What changed' is its own card near the top of the Model tab: a summary line (added, changed), then a table of changed figures with before, after, signed change and percentage change, defaulting to the latest two versions that differ; the version list collapses into the picker. |
| SAUX-24 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | model version times | Version times print in UTC ('The version of October 2nd, 2026, 15:49 UTC') while the rest of the page prints ET. | Every time on the page prints in ET in one format. |
| SAUX-25 | inferred | O8 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | model provenance | 'WHERE EACH INPUT CAME FROM' says '1 of 6 inputs have run' and that Filings, News, Social and Web have 'no source set up yet', while the same page shows a thesis read from the 10-K and harvested news. | The provenance block names each input that fed the page (filings, harvested news, Bloomberg) with its last run, consistent with what the page shows, behind a details toggle. |
| SAUX-26 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | model system facts | The Model tab prints system facts on its face: 'Showing 147 fiscal figures from the model block', 'No year-on-year growth rows: the model block serves none and this page computes none', '19 versions have landed; a refresh adds a version and never overwrites an earlier one', 'Re-running one input on its own is not available on this page yet'. | None of these sentences renders at rest; any that remains sits behind a details toggle in reader words. |
| SAUX-27 | N10 | O7 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | lead-panel period | Chatter's period is a calendar month stepped with 'Earlier month' / 'Later month' (October reads 'partial month: still being collected'); the Price face has no period control at all. | Both faces offer rolling 30D / 90D / 365D presets in the in-pattern segmented control, default 30D, and each caption names the window. |
| SAUX-28 | N10 | O7 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | lead-panel period data | The chatter counts are served per calendar month, so a rolling window cannot be drawn. | The lead-panel routes answer chatter counts (and the SAUX-19 sentiment aggregate) and price moves for rolling 30, 90 and 365-day windows ending at the last trading day. |
| SAUX-29 | inferred | O8 | 2.0.0_SA_COO~Z (AMGT_RESAPP) | inferred | security names | Names print in three formats: vendor capitals with share-class codes ('ALPHABET INC-CL A', 'ROCHE HOLDING AG-GENUSSCHEIN'), title case ('The Boeing Co'), and 'BOEING CO/THE (subject)' on Peers. | Every face prints one display name per security, in title case, with no share-class code. |
| SAUX-30 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | page wording | System wording on the face: the page subtitle 'Universe discovery, ranked server-side, above a per-name ...', 'Back to universe', '275 of 275 day(s) rendered (no gap)', 'no served drafted sentence carries this passage on this bundle', 'The drafted document does not say how many claims were held back uncited', 'tenure against the pool ... in a union of 250', 'Export rich text (.md)'. | None of the listed strings renders; each is replaced by reader words or moved behind a details toggle. |
| SAUX-31 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | unconnected fields | Fields with no source print as lines: 'Social: no source measured', 'MOST-DISCUSSED: NOT MEASURED', 'Trend is not in the data yet', and 'No profile (no match found)' on 8 of 12 officers. | A field with no source is not printed as a line; a panel with nothing to show renders one C12 empty state. |
| SAUX-32 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | exec management order | Officers are listed alphabetically by surname, so the chief executive sits in row 7 of 12. | Officers list the chief executive first, then the chief financial officer, then the rest by role rank. |
| SAUX-33 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | money format | Money prints as 'USD 1,234' and '$1,234' on one page. | Every money figure on the page uses one format. |
| SAUX-34 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | market cap vintages | Three market caps for one name show on one page with no reconciliation: USD 156B (Price modal), 159,623 (USD mm, Peers, as of September 24th) and 'USD 162B to USD 156B' (Model what-changed). | Each market-cap figure prints its as-of date beside it, or the page reads one vintage. |
| SAUX-35 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | inferred | account menu | The avatar's Settings / Log Out menu stays open after Escape and across later steps; while it was open the walker's tab presses failed. | Escape closes the account menu, and with the menu open a click on a tab still switches the tab. |
| SAUX-36 | inferred | O8 | 2.0.0_SA_COO~D (DSGN_AMGTV1) | measured | price details raw code | The Price face's Details disclosure prints 'generation 20261002T111010Z-a89fcf3c5f42 / state COMPLETE / 94 row(s) committed / coverage vintage bloomberg-dapi-boxsid'. | The Details disclosure states the price list's date and source in words, with no generation id or system state token. |

Counts: 2.0.0_SA_COO~D 29, 2.0.0_SA_COO~H 1, 2.0.0_SA_COO~Z 6 -- total 36. Dropped walker hits and their reasons: the register's `dropped` list (4).
<!-- REGISTER-TABLE-END -->
