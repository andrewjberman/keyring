# BRIEF: DSGN_AMGTV1 -- the Security Analysis page rebuilt from the estate's own cards, modals and charts

**Author** `4.0.0_SA_CRO~Z` -- **Date** 2026-09-28 (walk 22:56Z-22:59Z; research 22:4xZ-23:3xZ; site Z, device
OPAL_BLOOMBERG) -- **Mode** NEW (a new project code; the page it redesigns is in flight under AMGT_RESAPP) --
**Consumer** `1.0.0_SA_CTO~Z`: `/endpoint --forward` at L2, then L3 registration and the L4 PRD.

**Andrew-direct 2026-09-28 ~22:3xZ (~18:3x ET) at the `4.0.0_SA_CRO~Z` terminal, verbatim in full at**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260928_223xZ_DSGN_AMGTV1_WALK_MEMO_UIWALK_FIXTURE_PORT_BRIEF.md`
(@699c9e1f9f). The operative sentences: *"I want to be reusing the same chart components and styliing where relevant
so we can expedite in-pattern design styling for the various surfaces covered by the AMGT "Security Analysis" Portal
page and application. All of this should be synthesized in a structured brief that covers the current state and how
it needs to be evolved which will be the basis for a new project, DSGN_AMGTV1, on this box the sitez box."*

**The inputs, in the order they were produced:**

| Input | Where | What it is |
|---|---|---|
| Andrew's walk memo | `docs/briefs/dsgn-amgtv1-walk-memo-transcript-20260928.md` | 18:11 voice memo, transcribed locally with openai-whisper `turbo`, split into sections M0-M15 by surface; cited below as `M<n>` |
| Andrew's 12 snapshots | `...\Pictures\Screenshots\AMGT_walk_v1\` (local, not committed) | the PNGs the memo names, 17:31-17:34 local |
| The /ui-walk | `tmp/ui-walk/20260928T225654Z/` (gitignored) | signed-in walk on localhost:5174: 8 lead-panel states, 3 names x 5 tabs, 33 screenshots, every one read |
| The findings register | `docs/briefs/dsgn-amgtv1-findings-20260928.json` | 42 findings `AMV-01..42`, each with outcome, owner, measured/inferred cause and an acceptance line; this brief's tables are generated from it |
| Four read-only research passes | this seat's research agents, 22:4xZ-23:3xZ | fixtures (portal code), classifier + Holdings Breakdown (code + DynamoDB), News Scanner + timeline (code + AWS), tab backends (code + deployed API) |

---

## PART 0 -- Inputs honoured, and where the frame bent

This is a NEW-mode brief: DSGN_AMGTV1 does not exist yet. But the page it redesigns belongs to AMGT_RESAPP (in
flight), its data comes from AMGT_HARVST and AMGT_CORPUS (in flight), and this seat wrote the 09-24 frontend pattern
brief for AMGT_RESAPP (`docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md`, cited as PB). So the blind rule
of midstream mode is worth stating even though it does not formally bind.

- **Honoured:** no AMGT_RESAPP task order was opened for this brief, and no project `phase` or `blocking` field was
  read. The outcomes below come from Andrew's memo and the served page as a user sees it.
- **Where it bent, twice:**
  1. The timeline research read one AMGT_HARVST task order (`HVST-a-2`) to localize the 404, and this seat then
     checked that order's preflight claim against the live IAM policy. The claim was false, and this seat filed row
     `AMGT_HARVST-Z-S36` (@f9acd618b1, ARMED, disarm owner `2.0.0_SA_COO~H`). That order is named in Part V only as a
     dependency. Nothing in Part I ratifies it.
  2. The tab-backend research read AMGT_CORPUS FWD numbers (FWD-10, -11, -12, -15) to find who owns the dossier and the
     unit map. They appear only in owner columns.
- **The 09-24 brief is the base, not the branch.** Some of its outcomes have landed (white tab panels, the seven stat
  tiles). The rest are carried here where Andrew's memo re-states them (Part IV.6). Where the memo changes one
  (seven tiles become four cards), the memo wins.

---

## PART I -- THE OUTCOME TERRITORY

The person is the portfolio manager or analyst on the asset management team who opens Security Analysis to find
names worth a look and decide whether one deserves a position. The content reference is what that person already
reads: the team's earnings updates (PB IV.8), which lead with a recommendation, a summary and short headed sections.

### O1 -- CANDIDATE THREAD: a PM finds a name by who it is, opens it, and reads it as cards

Sign in and open `/security-analysis`. Read today's Trending x Price list, where every row carries the company's
name, asset class, sub-asset class, period move and rank change. Click Valero. Read its header as four cards, and
open the Financials card's modal. Open the Thesis tab and read it as three cards beneath the principal chart. Open
the Recommendation card and see whose recommendation it is and where each citation comes from.
Coarse grain: one firm (Opal), one list (Trending x Price), one name, the default window, no export.
Valero is suggested because it is the one walked name whose Thesis, Exec Management and Posture all carry content
today; a name whose tabs are empty cannot carry the thread. SOURCE: M6, M7, M9, M14.

### O2 -- A PM identifies every ranked name by who it is and how it is classified, and how far it moved

Every row in all four lead-panel lists shows name, ticker, asset class, sub-asset class and sector from Opal's own
taxonomy, plus the period figure and a signed rank change since the last run. The rows sit in the Positioning page's
Holdings Breakdown pattern. The name comes from a stable key the page can rely on, not from vendor all-caps or a
Bloomberg identifier. SOURCE: M2, M4, M6, M14. Findings AMV-01..04, 09..11.

### O3 -- A PM reads how names moved over time without untangling a knot of lines

Rank or price history for ten or more names reads cleanly: ticks that do not collide, names instead of identifiers,
one legend, and a way to follow one name ("a more effective trend line function", M14). The visual form is an
open question (fork F1). SOURCE: M2, M3, M5, M14. Findings AMV-05, 06.

### O4 -- A PM reads a security's headline figures as four cards, each opening to the detail

The header holds no more than four stable cards (M7): Price (with market cap and volume), Financials (led by
enterprise value, with net debt), Market features (led by beta, with volatility), and Trading technicals (trend,
average volume, short interest). Each leads with one figure and opens a modal with the rest. Every money figure is in
the security's own currency. SOURCE: M7. Findings AMV-12..15.

### O5 -- A PM reads a security's story along a timeline spine

For a covered name, a dated spine shows publications, events and headlines, with a keyword cloud from the name's own
coverage. Opal Data Harvest publications lead and the News Scanner supplements. A name with coverage never reads
"none". SOURCE: M8, M15. Findings AMV-16..19.

### O6 -- A PM reads the Thesis as three cards and can trust where each line came from

Investment thesis, Risks and Recommendation are three cards beneath the principal chart (M9). Each opens a modal
where the sentences and their evidence live, instead of drop-downs on the tab face. Every citation names its document
in words. The Recommendation says whose view it is: the team's stated position, never a filing's tax sentence
presented as one. SOURCE: M9. Findings AMV-20..25.

### O7 -- A PM sees who runs the company, for every covered name

Exec Management shows officers with their source named, even when the filing's officer section is empty, through a
fallback chain (M10, fork F3). SOURCE: M10. Findings AMV-26..28.

### O8 -- A PM reads the comparable set as a clean table

Peers keeps what Andrew likes (M11: "I actually kind of like what we're displaying"). Tickers are readable, the
absent columns are disclosed once and elegantly, and no internal string such as "identity crosswalk/v1" appears.
SOURCE: M11. Findings AMV-29..32.

### O9 -- A PM reads the Model sheet in plain line names, and knows why a line is missing

Line names are words, not Bloomberg mnemonics. Each refused line says in one sentence whether the data is missing
or the display is (M12: "If that's just a back-end data issue, so be it. But if that's a lack of front-end adapter
... handle in this project"). The sheet's provenance is qualified. SOURCE: M12. Findings AMV-33..36.

### O10 -- A PM reads Posture as a verdict card with its reasons, or as an honest empty state

A call is a verdict card with numbered reason cards that open modals. No call is a designed empty state with its
as-of date, never a paragraph of machine reasoning. SOURCE: M13. Findings AMV-37, 38.

### O11 -- A reviewer cannot tell this page from /market or /positioning

Cards, modals, charts, empty states and footers are the estate's own fixtures (M13-M14: "we should not invent the
wheel ... reuse the fixtures we've already developed"). Every footer reads "timestamp | Source: X." (M4: "It is always
source and timestamp"). There is one dark band per mode and no raw code, id or storage path on the face.
SOURCE: M4, M13, M14. Findings AMV-07, 08, 17, 27, 39..42.

O1 is the thread and completes with round 1. O2 through O11 are the enrichment territory.

---

## PART II -- WHERE THE BOUNDARY SITS

**DSGN_AMGTV1 owns:**
- the presentation of `portal/src/pages/SecurityAnalysis/**`: the shell, the Lead Panel, the security header, the
  five tabs and their modals;
- the EXTRACTION of estate fixtures into shared modules where the page needs one that is not yet shared (Part IV.3):
  the classified-security table from Holdings Breakdown, a card-row-plus-dialog pattern, a white-ground chart modal
  body. Each extraction proves the source page renders identically before and after.

**DSGN_AMGTV1 relies on, and does not change:**

| Sibling | What it supplies | Named asks from this brief (Part V) |
|---|---|---|
| **AMGT_RESAPP** (the page's product project; the scoped API `lib/research/api/scoped_amgt.py`) | every payload the page renders | rank change on rows; classification join; currency per figure; score-tile states already served; posture re-run; peers dedupe and identity; exec roster re-run with fallback |
| **AMGT_HARVST** (`2.0.0_SA_COO~H`) | harvest gold, the timeline routes, the chatter ranking source | timeline mount + package + gold grant (HVST-a-1, HVST-a-2, rows Z-S35 and Z-S36); the 2026 backfill (FWD-9); a refresh schedule |
| **AMGT_CORPUS** | the research dossier (the team's recommendation, management passage and description) and the Model's unit map | a route serving the dossier (FWD-10, -11, -15); the unit map re-run (FWD-12, currently unowned) |
| **D4 POSN** (`etf-classifications` owner) | the canonical classifier table | AMGT rows written by POSN's writer, with the served-output sign-off COT and BD need (Part V) |
| **DS MarketIntelligence** (News Scanner) | scanner articles and the Topic Cloud feed | a per-security name match or keyword job, if fork F4 takes the scanner leg |
| **DSGN_REBRND** (D13) | `portal/DESIGN.md` C1-C14, the colour law | the white-ground variants of PanelHeader and PanelFooter (rows W1-S9, W2-S5) that this page needs to hold one band |

**A boundary rule the decomp should inherit.** A field the page needs and the payload does not carry is an ask to
the owning project, never a page-side computation. That covers rank change, classification, currency and the
recommendation's source. The page does not rank (`amgt-lead-panel.ts:21-23`) and does not guess a currency.

**Macro.** DSGN is directive D13's macro (DSGN_REBRND, DSGN_IRPTV1). DSGN_AMGTV1 is the natural third member. The
CTO registers it at L3.

---

## PART III -- THE QUALITATIVE BAR

- **A PM can dispute the density.** On a 1440x900 screen, a PM who opens a name reads its four header cards and the
  Thesis's three cards without scrolling. Today the header alone fills the first screen, and the PBR Thesis runs
  4,178 px when expanded.
- **A PM can dispute the identity.** No row, card, table or chart names a security by a code a PM would have to look
  up. Today every lead-panel row does.
- **A reviewer can dispute the pattern.** Put the page beside `/market`, `/positioning` and `/philosophy`: the cards,
  modals, chart axes, legends, tooltips, empty states and footers are the same components. The reviewer cannot tell
  which page was built first.
- **An auditor can dispute the evidence.** Every drafted sentence's passage is still one click away (now inside a
  modal) and still in the DOM when opened. Every figure's source and time are in a canonical footer.
- **A PM can dispute an empty state.** Every "nothing here" names what is missing in one plain sentence and whose
  it is to fill, and never contradicts another panel on the same screen. Today it does: AMV-08, AMV-19, AMV-23.

No number is set here beyond what Andrew said: "never more than ... four cards" (M7) and "three solid cards" (M9).

---

## PART IV -- THE SUBSTRATE: what exists, measured

### IV.1 Andrew's feedback by surface (the memo, split)

| Surface | Memo | What Andrew said, in short |
|---|---|---|
| Lead Panel, Breakout x Chatter chart | M1 | Empty ("No rank history has been requested ...") is a data issue; cleared for the frontend |
| Breakout x Price chart | M2 | Cannot tell prices, ranks or securities apart; identifiers such as 992 HK need a library; build the securities into the ETF classifier for asset class, sub-asset class and a stable name key; ranking lines fail at 10+; "we need another type of visual format ... something that we should discuss" |
| Trending x Chatter chart | M3 | X-axis ticks overlap the axis line; needs a better chart solution |
| Trending x Chatter list | M4 | A ranking list is right; add day-over-day +/- rank movement; show names; sparse, and BA/HD "show nothing"; footnotes are non-canonical ("It is always source and timestamp") |
| Trending x Price chart | M5 | Needs another representation for many names; stable names; "suboptimal in every conceivable way" |
| Trending x Price list | M6 | Good; more visual, less text; each row: name, ticker, period, price delta, rank, asset class, sub-asset class, industry/sector; reuse the Positioning ETFs-toggle Holdings Breakdown |
| Security header | M7 | Too much text; progressive disclosure; at most four consistent cards opening modals like the Philosophy cards: price (+market cap, volume), financials (lead EV; net debt), market features (lead beta; volatility), trading technicals (trend, avg volume, short interest) |
| Security timeline | M8, M15 | Could not load, so cannot judge; a timeline spine per security with keywords (word cloud) and headlines, led by Opal Data Harvest, supplemented by the News Scanner; harvest backfill "very shortly" |
| Thesis | M9 | How is the recommendation reached?; citations good but source unclear; too much text; three cards (investment thesis, risks, recommendation) beneath the principal charts, each a modal, not drop-downs |
| Exec Management | M10 | Empty when Lusha and Bloomberg have nothing; a third fallback: Claude web search or a Bright Data SERP |
| Peers | M11 | "Peers looks pretty good"; clean up the absent columns; random strings (identity crosswalk v1) must go |
| Model | M12 | A port of Adam's sheet, which should be qualified; explain every refused / not built / not measured line, and fix it here if it is a frontend adapter |
| Posture | M13 | Nothing displays; make it a template; cards and modals; a standard branded component architecture |
| Synthesis | M14 | Lead panel: Holdings Breakdown + the ETF classifier DynamoDB tables; charts from Factor Charts (Recharts); better labels and a trend-line function; Philosophy cards for qualitative content, the Global RSI and U.S. Regime modals for chart content |

### IV.2 What the /ui-walk measured (localhost:5174, 2026-09-28 22:56Z-22:59Z)

- **Coverage:** 8 lead-panel states (Trending/Breakout x Chatter/Price x list/chart), then 992 HK, PBR US and VLO US
  across the header and five tabs, with every `<details>` expanded. 33 screenshots, all read by eye. 0 writes
  attempted, all blocked by the guard. The account was disarmed afterwards, and a login with the walk password is
  refused (HTTP 401).
- **Checks:** 31 unique findings from 141 observations:
  - raw code on the face: 25;
  - tinted status block: 2;
  - two dark bands: 1 (on 9 steps);
  - text under 3:1 contrast: 1;
  - mixed money formats: 1;
  - mixed date formats: 1.
  All 31 map to register findings (`walk_check_map` in the register).
- **API:** the timeline returned HTTP 404 on 3 of 3 names; no other API issue. Console: the 3 matching 404s and 2
  login-probe 401s.
- **What the eye saw that the checks did not:**
  - the currency defect (AMV-13, confirmed in code);
  - the two contradictory empty states (AMV-08);
  - the breakout-vs-trending figure clash (AMV-11);
  - the VLO officer-parse split (AMV-28);
  - the Model table clipping at 1440 px (AMV-34);
  - VLO's "BETTER" verdict over an empty comparable pack (AMV-38).
- **Instrument change, stated:** the walker had no Security Analysis branch (its generic mode only loads a route).
  This seat added one: `walk.mjs` `walkSecurityAnalysis`, `--security`, and `UI_WALK_ROOT`, committed with this
  brief. It is the instrument the build rounds re-run.

### IV.3 The fixture port map: what exists, where, and where it lands

Every row is MEASURED at the cited lines by this seat's research pass. Paths are under `portal/src/` unless stated.

**(a) Holdings Breakdown and the ETF classifier, for the Lead Panel lists (O2)**
- **Holdings Breakdown is not a component.** It is inline JSX in `pages/Positioning/tabs/HoldingsTab.tsx:1283-1970`
  (a 1,973-line file).
  - Rows are `AttributionHolding` (`:122-148`): ticker, name, asset_class, sub_asset_class, industry_group, weight.
  - Rows are always regrouped by asset class (`:1525-1572`).
  - Colour comes from `ASSET_CLASS_COLORS` (`:161-189`), `subAssetBg` and `sectorRampColor` (`bookSet.ts:699`).
  - In ETFs mode the data is `/api/general/etfs/positioning_data.json`, and sub-asset class is the GICS sector.
  - **Port:** extract the colour maps and the class and sector cells into a shared `ClassifiedSecurityTable`, with
    grouping off by default so the producer's order holds. `HoldingsTab` then imports the same pieces, and
    `/positioning` must render identically before and after.
- **`etf-classifications`** (key `ticker`; indexes on asset_class and sub_asset_class):
  - 285 rows (full scan, no further page): 169 single stocks with a GICS sector as sub-asset class, and 0
    firm-tagged values.
  - Writers are two hand-run POSN seeders (`seed-etf-classifications.py`, `seed-etf-constituents.py`).
  - **Coverage:** 6 of the 32 names on the 09-25 Trending x Price list (BA, HD, INTU, NU, PBR, VLO). Missing
    include 992 HK, BP/ LN, 9433 JP, RWE GR, SAP GY, SSE LN, 2317 TT, COST, KMB, HAL, BABA and SLB.
  - No portal route reads it, and the scoped AMGT API role has no grant on it.
- **What the page has today:**
  - `identity crosswalk/v1` (236 records) carries no sector and a name on only 66, in vendor all-caps.
  - The header's "Information Technology -- CN" comes from each name's model block (`GICS_SECTOR_NAME`,
    `CNTRY_OF_DOMICILE`, `SecurityOverlay.tsx:212-245`), not from any taxonomy.
- **Port (the research recommendation, a decomp input):**
  - POSN's writer adds AMGT rows: US names by bare root, non-US by the Bloomberg form ("992 HK", which cannot collide
    with a bare-ticker lookup).
  - The scoped API joins them server-side and attaches `classification {name, asset_class, sub_asset_class}` per row.
  - The same API derives `prev_rank`/`rank_change` from the previous complete generation.
  - Andrew said "both the ETF classifier DynamoDB tables". Which second table he means is fork F2.

**(b) Philosophy cards and their modals, for qualitative content (O4, O6, O10)**
- The cards are inline `<button>`s in `pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx:183-214`.
  - The top is a navy `GraphicPanel` with a numeral and icon; the body is white, with eyebrow, title, tagline and
    "Read more".
  - The hover shadow at `:189` breaks C11.
- The modal is `HeroDialog` (`ui/components/graphic/HeroGraphic.tsx:121-192`) over the catalyst dialog
  (`@headlessui/react`).
  - Props: `open, onClose, eyebrow, title, subtitle, icon, meta, children, footer, size`.
  - The same file holds `DialogStamp`, the date/source footer (`:88-97`).
  - One dialog serves the whole strip, with previous/next navigation.
- It is already reused by `ModelPortfolioModal.tsx:168-234` (a two-column body plus `DialogStamp`), `EtfModal`,
  `SatelliteModal` and `CategoryViewTree`.
- **Lands as:** the Thesis's three cards; the Posture reason cards; the header card modals' shell.

**(c) The Global RSI and U.S. Regime modals, for chart content (O3, O4, O5)**
- **Trigger row:** `components/market-performance/SentimentGauge.tsx:121-175`, four cards (Daily Cloud, Global
  RSI, U.S. Regime, Fear & Greed), each a Panel with a `SmartPanelFooter` source/timestamp footer (`:379-424`).
- **RSI modal** (`RSIModal.tsx`):
  - Recharts area plus line with RSI zones (`:321-396`);
  - 90D/1Y/3Y period buttons and three native selects;
  - a stats row, then index cards.
- **Regime modal** (`MarketRegimeModal.tsx`): a stats row, a 192 px area-plus-line chart with labelled percentile
  lines (`:579-683`), and signal cards.
- **What to copy:** both space about 7 ticks evenly and format dates (RSI `:360-367`, Regime `:597-605`), and
  downsample long periods (RSI `:280-289`).
- **What not to copy.** Both are hand-rolled fixed overlays rather than HeroDialog, carry translucent white text
  (C5.8), and fill their period buttons purple (C8). **Port their LAYOUT into HeroDialog on a white ground with
  `Segmented` toggles, not their code.**
- **Lands as:** the header Price and Market-features card modals (a price trend with a period toggle); a rank-history
  modal; the timeline's detail view.

**(d) The charts on Model Portfolios and Factor Charts (O3)**
- **Stack** (`portal/package.json`): `recharts ^3.7.0`, `@visx/wordcloud ^3.12.0` and `@headlessui/react ^2.2.9`.
  There is no Apex; `SentimentGauge.tsx:269` holds dead Apex code in a comment.
- **Shared pieces:**
  - palette: `lib/chartColors.ts`;
  - legend: `ui/components/ChartLegend.tsx`, with optional toggles;
  - tooltip: `components/DataTooltip.tsx`;
  - period toggle: `Segmented`.
  - There is no shared axis wrapper; every chart sets its own ticks.
- **Chart types:**
  - Model Portfolios: pie, bar and stacked area (`ModelPortfolios.tsx:1380, :1886, :2099`), scatter, account area,
    an SVG quartile chart, and `BenchmarkHeatmap`. Its area chart repeats the rotated -45 degree tick defect.
  - Factor Charts: radar, bars, and two multi-series lines (`FactorTiltTimeSeriesTab.tsx:359`,
    `components/ModelTiltTimeSeriesView.tsx:343`).
- **Best fit for many series over time:** `ModelTiltTimeSeriesView`. Series are selectable (`:173-181`) and ticks
  thin themselves (`interval="preserveStartEnd" minTickGap={50}`, `:357-358`). With ChartLegend toggles, one name
  highlights and the rest recede. This is Andrew's "more effective trend line function". There is no bump chart in
  the estate.
- **What the page does today:** `RankedChart.tsx` labels every date at -35 degrees with `interval={0}` (`:218-225`),
  cycles five hard-coded colours (`:70-76`), uses the default legend plus a second point-count legend, hand-styles
  its tooltip, and keys lines by ticker.

**(e) The News Scanner pipeline and the Topic Cloud, for the timeline spine (O5)**
- **Pipeline:**
  - Producers: ingestion (`news_ingestion_scheduler`, 43 RSS feeds plus NewsAPI), FinBERT scoring, Layer-2
    clustering (`news_trending_analysis`, 11:15 and 21:15 UTC), Layer-3 curation, the portal publisher and
    keyword-intelligence write-ups.
  - Storage: `opal-news-articles` (365,162 items) and S3 `opal-data-portal-v2/json/sentiment/keyword-sentiments.json`.
  - Map: `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/NEWS_SCANNER_DEEP_DIVE_20260916.md`.
- **Freshness:** `keyword-sentiments.json` was written 2026-09-28 21:18:54Z. Against the trading-day frontier
  (Friday 09-25 answers Monday) it is current.
- **Topic Cloud** (`TopicCloud.tsx`, inside SentimentGauge's Daily Cloud card):
  - `@visx/wordcloud`, top 20 of 39 keywords; size from `size`/`count`, colour from a sentiment gradient
    (`:44-90`).
  - Clicking a word opens `KeywordSentimentModal` (which POSTs `/v1/sentiment/keyword-intelligence`).
  - It is purely presentational: input `{keyword, sentiment, count, size?}` + `onKeywordClick`. **Reusable
    unchanged** as a per-security keyword cloud.
- **The join problem, measured.** `opal-news-articles` carries 18 attribute names over the 756 items of 2026-09-26
  and no ticker, entity, FIGI or ISIN field. The cloud's 295 embedded articles carry none either. A test name match
  found Boeing 1, Apple 3, Costco 2, and Lenovo, Petrobras and Home Depot 0. **The scanner can only supplement,
  never lead**, which is Andrew's order.
- **Opal Data Harvest is keyed and leads:**
  - Gold tables `article_security_mention`, `chatter_daily` and `chatter_event` carry `security_key`.
  - `chatter_daily`: 50,997 rows = 191 securities x 267 days, 55 with any article day.
  - 263 mention pairs over 115 articles, and 8 events across 5 names.
  - 992 HK has 21 article days and a 2026-02-12 event ("Lenovo Posts Earnings Beat on AI-Driven Demand").
  - The newest article is 2026-09-15; 50,996 of 50,997 daily rows carry the retired status `DENIED`; the 2026
    backfill (FWD-9) was last graded NOT REALIZED.
- **The timeline component exists and fails for three stacked reasons (AMV-16):**
  - `TimelinePanel.tsx` calls `/security/{key}/timeline` and has a four-state harness.
  - The two routes are not mounted on the gateway, so they fall through to the news proxy's `$default`, whose
    route list is what prints on the page.
  - The deployed Lambda predates the handler and lacks pyarrow (row Z-S35).
  - The role has no `amgt/harvest/gold/` read, live or in Terraform (row Z-S36, this seat, measured).
- **The spine's data contract (the research recommendation):** one row per event,
  `{date, type, source, security_key, headline?, url?, strength?, keywords[], magnitude?, status}`.

  | Event type | Fed by | Gap |
  |---|---|---|
  | publication | harvest gold | backfill, schedule, grant |
  | publication burst | `chatter_event` | 8 so far |
  | news headline | the scanner | name match only |
  | keyword burst | nothing per security | a job that extracts phrases per security; the scanner's extractor in `news_trending_analysis` is portable |
  | price move | the Bloomberg rankings | hand-run |
  | filing | `sec/harvest/silver` | no route |

### IV.4 Backend, data or adapter: the classification Andrew asked for (M12)

Each empty or odd state was traced to the code that emits it and the payload behind it, on the deployed API for PBR
(read-only GET invokes).

| Surface | What shows | Class | Owner | In this project? |
|---|---|---|---|---|
| Breakout x Chatter | chart "not requested" vs list "EMPTY 189/191" | BACKEND-DATA + FRONTEND-ADAPTER | AMGT_HARVST (legacy chatter source; gold cutover refused at `NEVER_WIDEN_H03_2A_CTO_HALF.md:74,114`) + page | the chart's EMPTY state, yes |
| Header money tiles | "$" on HKD/BRL figures | FRONTEND + BACKEND-CONTRACT | page (`StatTile.tsx:54-61`) + AMGT_RESAPP (no currency per figure) | stop assuming "$", yes |
| Short Interest | "not carried on this payload" | FRONTEND-ADAPTER | page (`constants.ts:115` reads the percent field; PBR carries `SHORT_INT_RATIO`) | yes |
| Bloomberg session badge | "NOT REPORTED" | BACKEND-CONTRACT | AMGT_RESAPP (`scoped_amgt.py:2004` hard-codes UNKNOWN) | drop the badge, yes |
| Thesis description | "ABSENT" while the header shows one | FRONTEND-ADAPTER | page (`ThesisTab.tsx:211-242`) | yes |
| Thesis recommendation | filing "guidance" labelled Recommendation | DESIGN + BACKEND-CONTRACT | page + AMGT_CORPUS (the dossier's team view is unserved) | the label yes; the dossier route no |
| Thesis chart | ABSENT | BACKEND-DATA | AMGT_RESAPP | EMPTY state only |
| Exec Management | ZERO_OFFICERS / NO_OBJECT | BACKEND-DATA + DESIGN | AMGT_RESAPP (never re-run with the Bloomberg fallback) | the debug line and state, yes |
| Peers | scanner codes, self-in-set, 12 absent columns | BACKEND-DATA + DESIGN | AMGT_RESAPP peers engine | display, yes |
| Model refused rows | NOT-YET-BUILT on 138 of 282 PBR figures | BACKEND-DATA | unowned (likely AMGT_CORPUS FWD-12): `field_map.json` never re-run for 22 added mnemonics | one line per row, yes |
| Model score tiles | "not read" | FRONTEND-ADAPTER | page (`ModelTab.tsx:261-275` reads the wrong fields) | yes |
| Posture | stale 09-16 ABSENT whose reasons are now false | BACKEND-DATA | AMGT_RESAPP (`posture/judge.py`, hand-run) | EMPTY state, yes |

So of Andrew's "refused / not built / not measured" (M12): the Model rows are backend data. The score tiles, the
Thesis description, the short-interest tile and the currency are frontend adapters, and they belong to this project.

### IV.5 Primitives already in the estate (the 09-24 list, still true)

`Panel`, `PanelHeader`, `PanelFooter`/`SmartPanelFooter` (the "timestamp | Source: X." footer,
`PanelFooter.tsx:107-116`), `PanelEmpty`/`PanelLoading`/`PanelError`/`PanelNoPermission`, `Stat`, `MetricsRow`,
`Card`, `DataTooltip`, `HelperTip`, `ChartLegend`, `BenchmarkHeatmap`, `Segmented`, `HeroDialog`, `DialogStamp` and
`TopicCloud`. Two known divergences bound them:
- `PanelHeader` and `PanelFooter` are band-coloured on every ground (DSGN_REBRND W1-S9), which is why the page
  shows two bands (AMV-39);
- `ChartLegend`'s ink is written for the dark band.

### IV.6 The 09-24 pattern brief: what landed, what this brief carries

| PB outcome | State at this walk | Here |
|---|---|---|
| O1 Thesis on one screen | not landed (4,178 px expanded) | O6, re-shaped as three cards + modals |
| O2 figures as tiles | landed as seven tiles | O4 replaces seven tiles with four cards |
| O3 evidence folded | landed as `<details>` per sentence | O6 moves evidence into the modal (Andrew: no drop-downs) |
| O4 Model as a table | partly; refusal lines still per row with mnemonics | O9 |
| O5 Peers present columns | landed; absent list still long | O8 |
| O6 Posture verdict tile | not landed | O10 |
| O7 Lead Panel controls and footer | controls landed; footer not | O11 |
| O8 four designed states | partly (the timeline error, the chatter empty state) | O11 |
| O9 render check | not re-run for this brief | acceptance shape below |

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced. The owner is in brackets.

1. **Classifier rows for the AMGT universe exist and are read server-side** [POSN writer; AMGT_RESAPP API join and IAM
   grant]. Adding bare US rows (COST, KMB, HAL, BABA, SLB) changes the classification COT and BD will read once they
   re-point to this table (IRPT S173). That is a served-output move and needs its never-widen sign-off.
2. **Rows carry `rank_change` against the previous complete generation** [AMGT_RESAPP].
3. **Every money figure carries its currency on the payload** [AMGT_RESAPP; the producer's `EQY_FUND_CRNCY` is REFUSED
   today for PBR].
4. **The timeline routes answer with data**: mount, package with pyarrow, AND a gold read grant [AMGT_HARVST; rows
   Z-S35, Z-S36].
5. **Harvest gold is backfilled and refreshed on a schedule**, and the retired `DENIED` status is migrated
   [AMGT_HARVST FWD-9]. Andrew: the backfill is "very shortly" (M15).
6. **A per-security keyword source exists** for the cloud [new; owner to name; the scanner's phrase extractor is the
   prior art].
7. **The dossier is served**: the team's recommendation, management passage and description [AMGT_CORPUS FWD-10, -11,
   -15].
8. **The Model unit map covers every pulled mnemonic** [unowned; likely AMGT_CORPUS FWD-12]. Without it the Model tab
   stays about half refused whatever the frontend does.
9. **Posture is re-run on current inputs, and peers dedupe same-issuer lines and resolve identity** [AMGT_RESAPP].
10. **The exec roster is re-run with its fallback chain** [AMGT_RESAPP]. A roster-discovery mode for Lusha or a
    search source is new vendor work, on Andrew's per-use word (fork F3).
11. **Each fixture extraction leaves its source page unchanged** on a before/after render (`/positioning`,
    `/philosophy`, `/market`).
12. **White-ground PanelHeader and PanelFooter variants** [DSGN_REBRND W1-S9, W2-S5], or this page cannot hold one
    band.
13. **The instrument:** `/ui-walk --route /security-analysis --security ...` (the branch added here) plus
    `scripts/ui-smoke.mjs` for auth-stubbed renders. Each candidate is walked and its screenshots read.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured 2026-09-28. The clock is beside each item. Figures marked (R) were read by this seat's research agents under
this seat's credentials and not re-read by the author; the rest the author read directly.

- **Walk:** 22:56:54Z-22:59:07Z on localhost:5174. The shared portal working copy was on DEV 92a25762; the running
  bundle's commit was not recorded. Results: 33 screenshots, 31 check findings, timeline 404 on 3 of 3 names, 0 guard
  aborts, account disarmed with login REFUSED.
- **Lead-panel generations:**
  - Trending x Chatter 20260928T100014Z: 2 rows, both at 0 mentions.
  - Breakout x Chatter 20260928T100015Z: EMPTY, NO_SIGNAL_IN_WINDOW 189 of 191.
  - Price generations 20260926T110728Z: dated 2026-09-25, 32 rows.
- **Classifier (R), ~23:0xZ:** `etf-classifications` holds 285 rows and 6 of 32 ranked names.
- **Timeline (R, ~23:1xZ; the grant read by the author 23:1xZ):**
  - routes unmounted: 106 live gateway routes, 16 under `/api/scoped/amgt/`, 0 timeline;
  - Lambda last modified 2026-09-26T23:35Z;
  - role grants: 22 harvest resources, 0 gold.
- **Harvest gold (R):** newest `chatter_daily`/`article_security_mention` file 2026-09-24; `chatter_event` 2026-09-28;
  newest article 2026-09-15.
- **News Scanner (R):** `keyword-sentiments.json` 21:18:54Z and `trending/latest.json` 21:23:44Z, both current against
  the Friday 09-25 frontier.
- **Model (R):** PBR 282 checked figures: 144 PASS, 138 REFUSE, all NOT-YET-BUILT.
- **Posture (R):** PBR's object is dated 2026-09-16; the pool's newest posture write is 2026-09-18.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM, and the forks for Andrew

**Not claimed.**
- The walk read the dev build on 5174, not the served bundle, and not at mobile widths. The Starred-only view,
  Print, Export and Refresh were not exercised (Refresh and the star are writes the guard blocks).
- Three names were walked, not the universe. Most (R) figures come from one name (PBR) or one day's partition.
- The whisper transcript is uncorrected. Mis-hearings are glossed, not edited, and the surface split is this seat's
  reading of where Andrew moved between PNGs.
- No component was changed, nothing was deployed, and no vendor was called. The one IAM read was read-only.
- **Peer quality is not graded:** Netflix and Oracle as Lenovo peers, and Williams Companies as Valero's comparable.
  Andrew liked Peers as displayed; whether the peer sets are right is a question for AMGT_RESAPP.
- The DSGN_AMGTV1 code is Andrew's; its directive (D13 is the natural home) and its registration are the CTO's at L3.

**F1 -- The ranking-over-time form (Andrew: "something that we should discuss", M2).**
- (a) Keep a chart view and port `ModelTiltTimeSeriesView`: selectable series, thinned ticks, ChartLegend toggles so
  one name highlights.
- (b) Drop the chart view and fold history into the list: each row carries a small rank/price sparkline and the
  signed rank change.
- (c) Both.

**Recommendation: (c).** The list with sparklines answers "who moved" at a glance for any number of names. The
highlight chart answers "how" for the few a PM picks. Neither needs a new chart type.

**F2 -- Which "both" classifier tables (M14).**
- `etf-classifications` is canonical.
- The only other table of that shape is `bd-securities`, which was ruled non-canonical on 09-28: LLM-classified and
  partly firm-tagged.

**Recommendation: `etf-classifications` alone.** AMGT rows go in through POSN's writer, with non-US names keyed by
their Bloomberg form.

**F3 -- The exec-management fallback order (M10).**
- Andrew said Lusha, then Bloomberg, then Claude web search or a Bright Data SERP.
- As built: filing, then Bloomberg `COMPANY_EXEC_OFFICERS`, then Lusha (it only enriches officers already found and
  needs a declared domain), then a SERP on the CEO's name only.
- The research dossier already holds a cited management passage with no vendor call.

**Recommendation: filing -> dossier -> Bloomberg -> Lusha roster-by-domain -> search.** Each vendor leg runs on
Andrew's per-use word. The frontend's job is only to name each roster's source.

**F4 -- The timeline's News Scanner leg.** Scanner articles carry no identifiers.
- (a) Name-alias matching (sparse: 0 hits for Lenovo, Petrobras or Home Depot on a 756-item day).
- (b) Harvest only until the scanner tags entities.

**Recommendation: (b) for round 1, with (a) named as an enrichment.** Andrew already put Opal Data Harvest first
(M15).

**F5 -- Whether DSGN_AMGTV1 absorbs the 09-24 brief's open outcomes from AMGT_RESAPP.**
**Recommendation: yes.** One project owns the page's presentation; AMGT_RESAPP keeps the payloads. Otherwise two
projects edit `pages/SecurityAnalysis/**` in the same weeks.

---

## THE REGISTER, generated from `docs/briefs/dsgn-amgtv1-findings-20260928.json`

By owner: DSGN_AMGTV1 26; AMGT_RESAPP 9; AMGT_HARVST 4; AMGT_CORPUS 2; D4 POSN (etf-classifications writer) 1. Total 42. Acceptance lines and evidence are in the register, one per finding.

| ID | Surface | Observed | Outcome | Owner | Cause claim | Status | Memo |
|---|---|---|---|---|---|---|---|
| AMV-01 | lead-panel:list | Ranked rows show Bloomberg identifiers only (992 HK, BP/ LN, 2317 TT, WALMEX* MM) with no company name. | O2 | DSGN_AMGTV1 | measured | new | M2, M4, M6 |
| AMV-02 | lead-panel:classification | No asset class, sub-asset class or sector on any row; Andrew asks for the ETF-classifier taxonomy as the stable key the frontend relies on. | O2 | D4 POSN (etf-classifications writer) | measured | new | M2, M6, M14 |
| AMV-03 | lead-panel:list | The list is sparse text (ticker plus one caption line); Andrew wants the Positioning Holdings Breakdown fixture: rank, rank change, name, ticker, period delta, asset class, sub-asset class. | O2 | DSGN_AMGTV1 | measured | new | M4, M6, M14 |
| AMV-04 | lead-panel:list | No indication of how a name's rank moved since the last run (Andrew: a day-over-day plus or minus). | O2 | AMGT_RESAPP | inferred | new | M4 |
| AMV-05 | lead-panel:chart | Rotated x-axis date ticks overlap the axis line; every date is labelled. | O3 | DSGN_AMGTV1 | measured | new | M3 |
| AMV-06 | lead-panel:chart | Overlaid rank lines for 5 names are hard to follow and will not scale to 10+; legend repeats as a second 'N point(s)' line; hand colours. | O3 | DSGN_AMGTV1 | measured | new | M2, M5 |
| AMV-07 | lead-panel:footer | Footer prints producer strings ('Served by the producer partition TRENDING_CHATTER (movement dimension: MEASURED)', generation ids, coverage vintage, 'this list is older than the date req... | O11 | DSGN_AMGTV1 | measured | known | M4 |
| AMV-08 | lead-panel:empty-state | Breakout x Chatter: list says 'The committed ranking for BREAKOUT_CHATTER is EMPTY. NO_SIGNAL_IN_WINDOW for 189 of 191 candidate(s)'; chart says 'No rank history has been requested for th... | O11 | DSGN_AMGTV1 | measured | new | M1 |
| AMV-09 | lead-panel:data | Breakout x Chatter is empty on 09-26/27/28 (189 of 191 candidates no signal). Andrew classed it a data issue, not frontend. | O2 | AMGT_HARVST | measured | known | M1 |
| AMV-10 | lead-panel:data | Trending x Chatter ranks BA US #1 and HD US #2 at 'chatter 0/100 (0 mentions)'; Andrew: 'there is data for Boeing and Home Depot, and we're really just showing nothing'. | O2 | AMGT_HARVST | inferred | new | M4 |
| AMV-11 | lead-panel:list | Breakout x Price shows 992 HK '+0.13% (2026-08-26 -> 2026-09-25)' while Trending x Price shows '+21.60%' for the same name and window: two quantities in one visual form. | O2 | DSGN_AMGTV1 | inferred | new | M2 |
| AMV-12 | security-header | Selected-security header is 'text everywhere': 7 tiles, a description, a machine posture paragraph, a timeline error, a news block, two ranking blocks and a generation footnote. | O4 | DSGN_AMGTV1 | measured | known | M7 |
| AMV-13 | security-header:figures | 992 HK: Price 'HKD 36.58' but Market Cap '$454B' and EV '$65.14B' (EV below market cap with net debt $4.15B); PBR US: Market Cap '$129B', EV '$985B'. Local-currency values print with a do... | O4 | DSGN_AMGTV1 | measured | new | M7 |
| AMV-14 | security-header:figures | Unit words print as suffixes (PRICE, ABSOLUTE, MILLIONS, RATIO); Short Interest reads 'not carried on this payload' for PBR and 992 HK. | O4 | DSGN_AMGTV1 | measured | new | M7 |
| AMV-15 | security-header:strings | 'BLOOMBERG SESSION: NOT REPORTED', 'crosswalk vintage 2026-09-25', 'from bloomberg CIE_DES', and a MACHINE posture paragraph citing R-1, U-1, AMGT-s-1, F2/G-24. | O11 | DSGN_AMGTV1 | measured | known | M7, M11 |
| AMV-16 | timeline | 'The timeline could not be loaded' on 3 of 3 walked names; the panel prints the raw 404 body with the whole route list of another function. | O5 | AMGT_HARVST | measured | known | M8 |
| AMV-17 | timeline:error-state | The error state dumps the API error JSON and ~40 route paths on the face. | O11 | DSGN_AMGTV1 | measured | new | M8 |
| AMV-18 | timeline:design | No timeline spine exists to judge; Andrew wants a per-security spine with keywords (word cloud), headlines, led by Opal Data Harvest publications, News Scanner second, after the harvest b... | O5 | DSGN_AMGTV1 | measured | new | M8, M15 |
| AMV-19 | timeline:data | Header news reads 'No publisher item in the pool for this name' for 992 HK while harvest gold holds 21 article days and a 2026-02-12 event for it. | O5 | AMGT_HARVST | measured | new | M15 |
| AMV-20 | thesis | PBR Thesis expanded is 4,178 px tall at 1440 wide: every sentence carries a MACHINE chip, a PASS badge and a 'CITES N PASSAGES' <details> drop-down. | O6 | DSGN_AMGTV1 | measured | known | M9 |
| AMV-21 | thesis:recommendation | The RECOMMENDATION headline is a PFIC tax-status sentence (PBR) or a management demand quote (VLO); Andrew: 'I would love to know how we come to that conclusion'. | O6 | AMGT_CORPUS | measured | new | M9 |
| AMV-22 | thesis:citations | Citations read 'P0034 -- ACCESSION 000129281426002168 -- ITEM 3.D. RISK FACTORS / PARAGRAPH 35'; Andrew likes them but cannot tell where they came from. | O6 | DSGN_AMGTV1 | measured | new | M9 |
| AMV-23 | thesis:description | Thesis says 'Description: ABSENT -- no served D-1 company_description sentence ...' while the header shows Bloomberg's company description for the same name. | O6 | DSGN_AMGTV1 | measured | new | M9 |
| AMV-24 | thesis:chart | 'The chart: ABSENT -- the thesis driver ...' with a paragraph of series-matching detail where the principal chart should sit. | O6 | AMGT_RESAPP | measured | new | M9 |
| AMV-25 | thesis:coverage | 992 HK Thesis: subtitle 'read from none', body 'No drafted prose for this name yet.' | O6 | AMGT_RESAPP | measured | new | M9 |
| AMV-26 | exec-management | PBR: 'Exec Management: ABSENT (ZERO_OFFICERS)'; 992 HK: 'ABSENT (NO_OBJECT)'. Andrew wants a fallback chain: Lusha, then Bloomberg, then Claude web search or Bright Data SERP. | O7 | AMGT_RESAPP | measured | new | M10 |
| AMV-27 | exec-management:strings | Raw 'roster_status UNRESOLVED-SOURCE; roster_reason ... source_accession ...' line on the face. | O11 | DSGN_AMGTV1 | measured | new | M10 |
| AMV-28 | exec-management:parse | VLO: one officer named 'Senior Vice' with role 'President and Chief Financial Officer 45'; ages appended to roles ('President 60'); role start and tenure ABSENT for 5 of 5, printed in lar... | O7 | AMGT_RESAPP | inferred | new | M10 |
| AMV-29 | peers:absent-columns | '5 present / 12 absent of 17 declared CSC column(s)' plus a 12-line absent list under the table. | O8 | DSGN_AMGTV1 | measured | known | M11 |
| AMV-30 | peers:identifiers | Tickers print as scanner codes (268236, B09N7M, *ENB, BFZ7XB); 'identity crosswalk/v1 @ 2026-09-25' on every tab. | O8 | DSGN_AMGTV1 | measured | new | M11 |
| AMV-31 | peers:data | PBR's peer set includes Petrobras itself (common and preferred) and both China Shenhua share classes; the subject row's own price, EV and P/E read '--'. | O8 | AMGT_RESAPP | measured | new | M11 |
| AMV-32 | peers:currency | 992 HK subject row: 'Mkt Cap (USD mm) 456,119', the HKD figure labelled USD. | O8 | AMGT_RESAPP | inferred | new | M11 |
| AMV-33 | model:refused | Rows read 'REFUSED -- NET_INCOME: unit/sign convention is NOT-YET-BUILT, not MEASURED'; Andrew asks whether it is a backend data issue or a missing frontend adapter. | O9 | AMGT_CORPUS | measured | new | M12 |
| AMV-34 | model:layout | Row labels are Bloomberg mnemonics (SALES_REV_TURN, IS_OPER_INC, CF_FREE_CASH_FLOW); a PROVISIONAL chip under every cell (992 HK, VLO); the 2024-2025 columns clip at 1440 px. | O9 | DSGN_AMGTV1 | measured | known | M12 |
| AMV-35 | model:scores | ROBUSTNESS / PEERS V / DIVERGENCE D read 'not read'. | O9 | DSGN_AMGTV1 | measured | new | M12 |
| AMV-36 | model:provenance | Subtitle 'Adam's Model sheet, served from the model block -- nothing estimated in its place'; Andrew: the port should be qualified. | O9 | DSGN_AMGTV1 | measured | new | M12 |
| AMV-37 | posture:empty | PBR and 992 HK Posture: 'ABSENT' headline over a paragraph of machine reasoning; 'no UI of any kind'. | O10 | AMGT_RESAPP | measured | known | M13 |
| AMV-38 | posture:call | VLO: 'BETTER than Williams Companies, Inc.' as the headline while reason 5 says the comparable pack is essentially empty; S3 paths, run ids and the model name on the face; 9 of 20 cites u... | O10 | AMGT_RESAPP | measured | new | M13 |
| AMV-39 | page:bands | Security mode shows two dark bands: the identity header and each tab's PanelHeader. | O11 | DSGN_AMGTV1 | measured | known | M13 |
| AMV-40 | page:formats | Mixed formats on one page: '2026-09-22' and 'September 22nd, 2026'; 'USD 1,234' and '$1,234'. | O11 | DSGN_AMGTV1 | measured | new | -- |
| AMV-41 | page:contrast | The chart's 'rank' axis label measures under 3:1 contrast. | O11 | DSGN_AMGTV1 | measured | new | -- |
| AMV-42 | page:architecture | Andrew: 'I like to think of everything as cards and modals ... we should not invent the wheel. We should reuse the fixtures we've already developed.' | O11 | DSGN_AMGTV1 | measured | new | M13, M14 |

## Acceptance shape (for the PRD, not set here)

Each candidate:
- is walked with `/ui-walk --route /security-analysis --security <names>` and its screenshots read by a person;
- has its register findings graded against their acceptance lines;
- passes `design:bands`, `raw-code` and `format:*` with zero hits on the surfaces it touches.

Each extraction ships with before/after renders of its source page. The CVO grades JUDGMENT criteria at L9 on the
PNGs, citing the contract clause.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/dsgn-amgtv1-security-analysis-frontend-brief-20260928.md
  REGISTER          docs/briefs/dsgn-amgtv1-findings-20260928.json (42 findings AMV-01..42; coverage:
                    python docs/briefs/irpt-ui-review-coverage-check.py --register <register> <file>)
  TRANSCRIPT        docs/briefs/dsgn-amgtv1-walk-memo-transcript-20260928.md (M0-M15)
  RECORD            org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260928_223xZ_DSGN_AMGTV1_WALK_MEMO_UIWALK_FIXTURE_PORT_BRIEF.md
  PROJECT           DSGN_AMGTV1 -- NONE-YET (Andrew named it; the CTO registers at L3; D13 / macro DSGN is the natural home)
  EXISTING PRD      NONE. Page PRD: org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md
  PRIOR BRIEF       docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md (PB; F1 band fork resolved 09-24)
  SIBLING PROJECTS  AMGT_RESAPP, AMGT_HARVST (2.0.0_SA_COO~H), AMGT_CORPUS, D4 POSN (etf-classifications), DS
                    MarketIntelligence (News Scanner), DSGN_REBRND, DSGN_IRPTV1
  OPEN ROW          AMGT_HARVST-Z-S36 @f9acd618b1 (ARMED; the timeline gold grant) -- with Z-S35 (pyarrow)
  PRIOR ART         Holdings Breakdown (pages/Positioning/tabs/HoldingsTab.tsx:1283-1970); PhilosophyPillars + HeroDialog;
                    SentimentGauge card row; RSIModal / MarketRegimeModal layouts; ModelTiltTimeSeriesView;
                    ChartLegend, DataTooltip, PanelFooter/SmartPanelFooter, DialogStamp; TopicCloud; etf-classifications
  CONTRACT          portal/DESIGN.md C1-C14; portal/CLAUDE.md colour law
  INSTRUMENT        .claude/skills/ui-walk/walk.mjs (Security Analysis branch added with this brief); portal/scripts/ui-smoke.mjs
  MEASURED AT       walk 2026-09-28T22:56:54Z-22:59:07Z; research 22:4xZ-23:3xZ; IAM read 23:1xZ; portal DEV 92a25762
```
