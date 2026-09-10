# AMGT_RESAPP -- pre-brief working notes

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | **Status:** NOTES, not a brief.
**Purpose:** the discussion substrate Andrew asked for before `/brief-create`. Nothing here is
issued, nothing is dispatched, no register row is edited.

> Every figure below is MEASURED with its denominator and instrument named, or it is marked
> UNVERIFIED. Where a claim is about the live plane, the vintage is printed.

---

## 1. AUTHORITY -- Andrew-direct 2026-09-10, this session, VERBATIM

- *"We're going to take D5 to this device."*
- *"this will be a new project under D5, call it AMGT_RESAPP"*
- *"This is going to be a dashboard portal page called Security Analysis."*
- *"The scope of the project will be designing the frontend according to existing patterns."*
- *"This will be an internal tool so general API is fine."*
- *"I think we need to discuss this at length before attempting the brief"*

**EGRESS AUTHORIZATION, VERBATIM AND SCOPED:** *"you have egress to do whatever you need to do
just try to be ginger about data pulls, one security at a time, ideally one endpoint at a time
and if they have date picker dont go too historical."*
This is the per-use word that CLAUDE.md's vendor-egress rule requires. It carries its own care
constraint -- ONE security, ONE endpoint, SHALLOW history -- and that constraint travels with it.

**PLACEMENT.** The register (`org/missions/DIRECTIVES.yaml`, D5 block) carries a standing
Andrew-direct of 2026-08-27, verbatim: *"D0 D2 D3 D5 D10 D11 stay here until I say otherwise. the
rest is all on sitez."* The row states the duration clause is Andrew's to lift and nobody else's.
His word above IS the lift. **The register row is `0.0.0_AB_MSTR`'s to edit, not mine** -- flagged,
not actioned. D5's member set is presently `subgroups: []`, `projects: []`, so AMGT_RESAPP is the
directive's FIRST registered project.

---

## 2. THE SOURCE ASK

**Adam Muller (Head of Asset Management) -> Andrew, 2026-09-10T13:18:06Z, "Claude automation".**
Five limbs he wants automated:

1. A simple financial model
2. A company description including information on segments
3. The investment thesis
4. The risks
5. A bio of key management, usually the CEO

His only stated constraint: *"It doesn't have to mirror this formatting. But we want it to print
cleanly."* Attachments: the COPA and SAP research packs.

**Read the acceptance test carefully: Adam's deliverable is a PRINTED DOCUMENT.** Andrew's is a
dashboard page. These are not in conflict but they are not the same artifact, and §7 treats the
reconciliation as a design decision rather than an assumption.

---

## 3. MEASURED ESTATE

### 3.1 The research corpus ALREADY EXISTS

Location: `C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\` -- a SharePoint
library syncing live to this box (root mtime 2026-09-10 07:55). Instrument: filesystem census.

| Artifact | Measured |
|---|---|
| `Asset Management/Research/` | **89 name folders** (ASML .. Zurich), ex-US heavy, per-name subfolders holding pack + source `.docx` + primary PDFs + earnings releases |
| `Adam/NEW Research Pack Template 2026 03 09_v1.docx` | the blank template: 11 paragraphs, 3 tables, 1 image |
| SAP pack `.docx` | 133 paragraphs, 2 tables, **9 embedded charts** |
| COPA pack `.docx` | 85 paragraphs, 2 tables, **11 embedded charts** |

**Template structure (4 blocks):** `[PASTE EXCEL OUTPUT]` -> table `RECOMMENDATION` /
`COMPANY DESCRIPTION` -> two-column table `INVESTMENT THESIS | RISKS AND CONSDIERATIONS` -> bio
block. The misspelling `CONSDIERATIONS` appears in the template AND in the SAP pack, which is the
provenance evidence that SAP was cut from this template.

**The template is a FLOOR, not the pack.** Sections present in filled packs but absent from the
template:

- SAP: OTHER POSITIVES, OTHER NEGATIVES, **IMPACT OF ARTIFICIAL INTELLIGENCE**, Management/Board,
  COMMON STOCK COMPARISON
- COPA: MOAT, 2026 DYNAMICS, MANAGEMENT, OPERATIONAL DATA, HISTORICAL VALUATION, COMMON STOCK
  COMPARISON, FLEET PLAN, "CPA OWNS MOST OF ITS PLANES"

The analyst-specific sections are where the judgment lives. **An automation that fills only the
template's four blocks reproduces the skeleton and none of the value.** This is the single most
important framing point for scoping v1.

### 3.2 The "simple financial model" is fully specified and mechanical

`SAP FactSet Based ONE PAGER 2026 07 01_v1.xlsx`. Sheets: `__FDSCACHE__`, `_CIQHiddenCacheSheet`,
`Model NEW VERSION`, `Balance Sheet SAP-DE`, `Charts`, `Model`, `CSC`.

- **Header block:** ticker, name, sector, location, currency, fiscal yr, date of pricing, share
  price, market cap, net debt, EV, ADTV, short interest, shares out, float, beta, div yield
- **Financial Summary: 10 years x ~20 line items** -- Revenue + y/y, Operating Income + margin,
  EBITDA + margin, EPS recurring + y/y, BVPS + y/y, avg diluted shares + y/y, CapEx, FCF, DPS +
  y/y, and RANGE-valued Dividend Yield / FCF Yield / P/E / EV-EBITDA / P/B, FCF Margin, ROA, ROE
- **Scenario grid:** Upside / Base (/Downside) x 2026-2030, two independent valuation bridges --
  `EPS x multiple -> price -> return` AND `EBITDA x multiple -> EV -> mktcap -> price -> return`
- **Upside/Downside summary:** target, ratio, implied EV/EBITDA, implied P/E, return by year

**THREE VENDOR PLANES FEED ONE SHEET.** FactSet (`FG_COMPANY_NAME`, `FG_FACTSET_SECTOR`,
`FF_FISCAL_DATE`, `__FDSCACHE__`), CapIQ (`IQ_*` defined names, `_CIQHiddenCacheSheet`), and
Bloomberg -- the `CSC` sheet is pure BDP: `px_last`, `EQY_SH_OUT_REAL`,
`SHORT_AND_LONG_TERM_DEBT`, `BS_PFD_EQTY_&_HYBRID_CPTL`, `MINORITY_NONCONTROLLING_INTEREST`,
`CASH_AND_MARKETABLE_SECURITIES`, `CUR_MKT_CAP`, with tickers in Bloomberg format
(`VOD LN Equity`).

**FLAG, NOT A DEFECT CLAIM (needs Adam):** in the saved SAP workbook the `CSC` sheet holds a
TELECOM peer set (KPN, Vodafone, BT, Orange, Telenor, Telekom Austria, Rogers, Telus, Swisscom,
AT&T, Verizon, Telefonica) and its computed columns are cached as `#VALUE!`. Read with
`data_only=True`, so those are the values as last saved, not a live formula state.
**UNVERIFIED:** whether `CSC` is the source of the pack's COMMON STOCK COMPARISON section -- the
docx carries 9 embedded images and I have not traced which one. If it IS the source, a peer set
carried forward from a prior name is exactly the failure class automation removes.

### 3.3 Bloomberg -- what this box will and will not serve

Instrument: `integrations/bloomberg/READ_HERE.md` (mandatory read per CLAUDE.md).

| Surface | State |
|---|---|
| `ReferenceDataRequest` (BDP) | **SERVED** -- `mcp__bloomberg__bloomberg_reference_data` |
| `HistoricalDataRequest` (BDH) | **SERVED** -- `mcp__bloomberg__bloomberg_historical_data` |
| intraday bars | SERVED |
| **BQL (`//blp/bqlsvc`)** | **NOT ENTITLED** -- refuses every query incl. trivial ones. Service-level; Andrew's spend decision, tracked as a card |

**THREE PROPERTIES THAT SHAPE THE WHOLE DESIGN:**

1. **DERIVED FIELDS ARE CURRENT-DAY ONLY.** A `HistoricalDataRequest` returns ZERO rows for derived
   fields while `PX_LAST` returns a full series *in the same call* -- the control that makes it a
   property of the FIELDS, not the request. **There is no backfill. Every uncaptured day is gone
   permanently.** This makes Andrew's "save all their data timestamped" instinct *stronger than he
   stated it*: for derived fields the snapshot is not a convenience, it is the only copy that will
   ever exist.
2. **SIGN-IN IS A 2-PHASE, 2-ATTEMPT-BUDGET ACT** and the terminal signs out regularly
   (`could not start blpapi session to 127.0.0.1:8194` is named as "the most common failure by
   far"). A user-facing "run the analysis" button therefore has a dependency that is *routinely
   down* and cannot be silently retried.
3. **A field returning empty with no error has three indistinguishable causes** -- bad mnemonic,
   wrong request type, not entitled -- separable only by reading `__field_errors__`.

Also carried: **site-Z scheduled tasks run the WORKING TREE**, so an edit to a pipeline file on
this box IS a deploy the moment it touches disk.

### 3.4 Portal -- the patterns Andrew named all exist

- **"Market Overview" resolves to `/market` -> `MarketPerformance`** (also the default landing
  route and the `*` fallback). Its machinery: `pages/MarketPerformance/panels/SentimentPanel/`,
  `components/market-performance/SentimentGauge.tsx`,
  `components/market-performance/KeywordSentimentModal.tsx`, `api/endpoints/sentiment.ts`,
  `api/news_scanner/NEWSAPI_INTEGRATION.md`. Panels present: `ExecutiveSummaryPanel`,
  `SentimentPanel`.
- **Route order in `portal/src/App.tsx`:** `/security-scanner` (`:441`) -> `/ticket-center`
  (`:452`) -> `/portfolio-management` (`:460`). A `/security-analysis` route slots exactly where
  Andrew described. **GRAIN: that is the ROUTE order. I have not read the sidebar NAV order and
  they may differ.**
- **`SecurityScanner` is the skeleton to clone**, and it already answers two of Andrew's open
  design questions by precedent:

```
portal/src/pages/SecurityScanner/
  DESIGN_SPEC.md          <- 560 lines. THE PAGE-SPEC PRECEDENT.
  SecurityScanner.tsx
  components/  ScannerHeaderPanel.tsx  ScannerFilterToolbar.tsx  FactorChip.tsx
  hooks/       useScannerApi.ts  useScannerState.ts
  tabs/        UniverseScannerTab.tsx  UniverseDataTab.tsx  FactorBankTab.tsx
  utils/       asOf.ts  categoryOrder.ts  factorDescriptions.ts  quintileUtils.ts
  constants.ts  types.ts  index.ts
```

  -- `ScannerHeaderPanel.tsx` is the header-panel pattern; `tabs/` + shared
  `@/hooks/useTabNavigation` + `@/components/TabNavigation` is the tab pattern; `utils/asOf.ts` is
  the vintage-display convention.

- **The SecurityScanner precedent also sets the PROCESS**, and it matches Andrew's stated scope
  ("designing the frontend according to existing patterns") exactly: a `DESIGN_CONTRACT` +
  `DATA_CONTRACT` pair under `docs/architecture/`, then a `DESIGN_SPEC.md` carrying a shared-import
  table and a documented justification for every deviation -- under an explicit gate:
  *"no .tsx files written until approved."* Its stated design principle is
  *"mirrors PortfolioManagement's visual language as closely as possible."*

### 3.5 News and Seeking Alpha -- the asymmetry that matters

**Seeking Alpha: a 7-Lambda estate already in production.**
`seeking-alpha-{analysis-coordinator, analysis-listing-parser, analysis-scraper, dedup-coordinator,
news-coordinator, news-dedup, news-scraper}` + `infra/aws/terraform/seeking-alpha/main.tf` +
local scrapers under `data/seeking-alpha/scripts/`.

- **THE ONE-SHOT PRIMITIVE ANDREW ASKED ABOUT ALREADY EXISTS AND IS URL-GENERIC.**
  `infra/aws/lambda/seeking-alpha-analysis-scraper/lambda_function.py:159`
  `fetch_page_via_bright_data(url: str, api_key: str) -> str` -- Bright Data **"one_shotter"** API
  with browser rendering. It takes an arbitrary URL.
- **What is NOT ticker-addressable is the ORCHESTRATION around it:** `lambda_handler` reads
  `urls = batch['urls']` from `load_batch_from_s3(batch_id, date_str)` ->
  `seeking-alpha/analysis/batches/{date_str}/{batch_id}.json`, batches of 10, fed by a coordinator
  on a date listing. Output lands in S3 + DynamoDB keyed `article_date` + `url_hash`.
- **=> The gap is a thin ticker-addressable wrapper, not a scraper build.**
- ~~**SA articles ARE ticker-tagged.** `data/seeking-alpha/scripts/edge_scraper_enhanced.py:293-338`
  builds a validated per-article `tickers` array and emits it on the record
  (enumerate: 7 hits / 589 lines, all CODE band, 0 docstring/comment).~~
  ⛔ **FALSE OF THE LANDED CORPUS -- CORRECTED SAME DAY, see
  `AMGT_RESAPP_SA_CORPUS_STALENESS_20260910.md` s1/s3.** Measured **0 of 200** landed articles carry
  a populated `tickers` field. The line I cited is the LOCAL Edge scraper; the corpus was produced
  by the DEPLOYED Lambdas, and `tickers` is **absent from both** (`seeking-alpha-analysis-scraper`
  0 hits / 401 lines; `seeking-alpha-news-scraper` 0 hits / 296 lines). **I read the producer's CODE
  and wrote down a property of the ARTIFACT** -- the citation made a code-reading look like a
  measurement. Superseded by design anyway: Andrew ruled the source is the SA **symbol page**, not
  extraction over article bodies.

**The RSS/NewsAPI news corpus is NOT ticker-tagged at article level.**
`tools/news_scanner/` -- 4 layers, 600+ articles/day from 17-28 RSS feeds + NewsAPI, lands
`s3://opal-data-news-av/rss_bulk/`, DynamoDB for real-time queries, sentiment via 5 financial
dictionaries.

- Scoped census (3 news lambda dirs, 17 files): **2 hits** for `ticker|symbol`. The only real one is
  `infra/aws/lambda/news_layer3_curation/lambda_function.py:1900`
  `'affected_tickers': gpt_topic.get('affected_tickers', [])` -- a **GPT-derived attribute of a
  TRENDING TOPIC**, not a tag on an article.
- Widened UNSCOPED across `infra/aws/lambda` + `tools/news_scanner` + `data/seeking-alpha`
  (679 hits / 5,003 files; 118 first-party): article-level ticker handling clusters in the
  **portfolio/ETF pipelines** (`bd-pipeline`, `mdpf-pipeline`, `etfs-pipeline`, `ycharts-*`,
  `etf_classification.py`, `market-overview-tiered-generator`) and in the **SA scrapers** -- and in
  the RSS/NewsAPI news path only at topic level (`news_layer3_curation`,
  `semantic-news-layer3-curation`).

> **THEREFORE:** *"scan our news database for mentions of the stock"* is **available today against
> the SA corpus** and **requires a new entity-extraction leg for the RSS/NewsAPI corpus.** Those
> are two different pieces of work and the brief must not bundle them as one.

**Staleness flag:** `tools/news_scanner/README.md` says "Last Updated: November 22, 2025" and its
Quick Start cites `/mnt/c/Users/AndrewBerman/...` -- a WSL path from the OTHER device. The doc has
not been re-grounded on this fabric. Treat its claims as DESCRIPTIVE until re-measured.

### 3.6 `opal-data-research` does not exist yet

Instrument: `comp-find --corpus aws` (the live AWS plane).
**Vintage: estate as of 2026-09-10 12:24:50 UTC; stitch built 2026-09-10T03:01:17Z.**

- `'opal-data-research'` -> **0 hits across 2,382 aws nodes**
- `'research'` scoped to `S3_BUCKET` -> **0 hits across 34 bucket nodes** (drift: DECLARED=26,
  LIVE-INCREMENTAL=3, LIVE-no-DECLARED=5)

**QUALIFIER, per the tool's own footer:** a measured zero over what the graph MODELS, not a proof
of absence in AWS. Buckets ARE modelled (34 nodes, 5 of them LIVE-no-DECLARED), so confidence is
reasonable -- but the honest statement is **"measured zero, new mint expected"**, not "does not
exist."

---

## 4. ANDREW'S DESIGN POINTS -- reviewed one by one

| # | His point | What is measured | What is open |
|---|---|---|---|
| 1 | ad-hoc: user inputs a ticker | -- | **which UNIVERSE bounds it?** (see Q1) |
| 2 | lightweight cache/function so it autosuggests | candidate sources exist: the 89-name coverage list; SecurityScanner's universe; ETF holdings silver | source + refresh cadence |
| 3 | "and it runs the analysis" | -- | **this is the seam. See §5.** |
| 4 | historical searches save timestamped to `opal-data-research` | bucket is a new mint (3.6) | key layout, retention |
| 5 | user can "refresh" that research | -- | refresh = NEW versioned snapshot, never overwrite -- forced by 3.3(1) |
| 6 | header panel contents | `ScannerHeaderPanel.tsx` is the precedent | which fields (see Q3) |
| 7 | tabs e.g. New / History, and their order | `tabs/` + `useTabNavigation` + `TabNavigation` is the precedent | count + order (see Q3) |
| 8 | scan news DB for mentions + article link-outs | **SA corpus: available today (ticker-tagged). RSS/NewsAPI corpus: NOT ticker-tagged** (3.5) | whether v1 covers both |
| 9 | web search, last week, IR pages + trusted publications | not built | source allowlist = a curation decision, not a build one |
| 10 | "oneshot the security's page on SA" | **the primitive exists and is URL-generic** (3.5) | wrapper + which SA surface (ticker page vs analysis feed vs both) |
| 11 | nature of the AI Analysis run on the security | -- | **the biggest unscoped item. See Q2.** |
| 12 | "internal tool so general API is fine" | removes the partner-tenant auth/allowlist burden | still needs an auth'd route |

---

## 5. THE BIG CHALLENGE ANDREW NAMED -- Bloomberg sequencing

He is right that this is the hard part, and the shape of the difficulty is specific:

**The portal runs in AWS. Bloomberg DAPI is `127.0.0.1:8194` on THIS DESKTOP and nowhere else.**
A user clicking "Run" in a browser cannot reach it. Every design below is a way of crossing that
gap, and the choice is the sequencing decision:

- **(a) Desktop agent on a queue.** Portal enqueues a ticker; a process on this box drains it,
  pulls Bloomberg, writes `opal-data-research`, portal polls. *Pro:* true ad-hoc, matches Andrew's
  described UX. *Con:* latency is unbounded and honest only if the UI says so; dead when the
  terminal is signed out; a new standing process on this box.
- **(b) Pre-compute a bounded universe on the existing daily vehicle.** The 89 covered names get
  refreshed on the schedule that already runs here. Portal reads S3 only. *Pro:* no new seam, no
  live dependency, instant page. *Con:* not ad-hoc -- a name outside the 89 has no data.
- **(c) Hybrid.** (b) for the covered universe, (a) for anything new, with the UI distinguishing
  SERVED-FROM-SNAPSHOT from QUEUED. *This is my recommendation* and it is also the only one whose
  failure mode is legible to the user.

**Two things the UI must carry regardless of choice**, both forced by measurement not preference:

1. **A Bloomberg session-state indicator.** Sign-out is the most common failure by far and costs
   a 2-attempt budget to fix. A page that fails silently against a signed-out terminal will be
   read as a broken page.
2. **Every displayed number carries its vintage.** `utils/asOf.ts` already exists in
   SecurityScanner as the convention. Given 3.3(1) -- derived fields are current-day-only with no
   backfill -- a research snapshot that does not state its as-of is not interpretable a week later.

**And the volume question Andrew asked to assess ("the size of the data they really need"):**
the answer is bounded and knowable from §3.2 -- roughly **20 line items x 10 years, plus ~25 header
scalars, plus a peer block**, per name. That is small. The cost is not volume, it is **field
mapping**: which BDP mnemonics reproduce FactSet's `FG_*`/`FF_*` and CapIQ's `IQ_*` line items,
and which have no Bloomberg equivalent at this entitlement. **That mapping is the real v1 work
item and it should be its own task order.** Under Andrew's egress grant I can settle it empirically
one endpoint at a time.

---

## 6. RECONCILING ADAM'S PRINT PACK WITH ANDREW'S DASHBOARD

Not a conflict, but it must be decided rather than assumed. Proposed framing:
**one structured pack object, two renderers.**

```
   Bloomberg BDP/BDH  ---+
   news / SA corpus   ---+---> PACK OBJECT (versioned, in opal-data-research) ---+---> Security Analysis page
   web search leg     ---+          (the contract both renderers read)           +---> print artifact (.docx/PDF)
   AI analysis leg    ---+
```

The invariant worth writing into the brief: **the print artifact is generated from the pack object,
never screenshotted from the page.** Adam's acceptance test is "prints cleanly", and a React page
does not print cleanly by default.

**Scope note for the brief:** Andrew scoped this project as *"designing the frontend according to
existing patterns."* On that reading, v1's deliverable is the DESIGN_CONTRACT / DATA_CONTRACT /
DESIGN_SPEC set plus the page -- and the print renderer is a LATER project under D5, not this one.
The pack object still has to be specified now, because it is the frontend's data contract.

---

## 7. OPEN QUESTIONS FOR THE DISCUSSION

**Q1 -- What universe bounds the ticker input and its autosuggest?** Adam's 89 covered names? Any
listed security? The ETF holdings universe? This decides whether the page is a coverage tool or a
general research terminal, and it decides §5(b) vs §5(a).

**Q2 -- What IS the "AI Analysis"?** The least specified item and the one carrying the most value.
Candidate readings: (i) draft Adam's five limbs as prose from the assembled data; (ii) summarise
and rank the news/SA/web evidence; (iii) score the security against a house framework; (iv) all
three. Sub-question: is its output SAVED as part of the versioned snapshot (I think yes -- same
no-backfill logic) and is it re-run on refresh or diffed against the prior run?

**Q3 -- Header panel and tab shape.** My read of the precedent, to react to rather than adopt:
header = ticker / name / sector / country / price + change / market cap / as-of vintage /
Bloomberg session state. Tabs: `New` first (it is the verb), then `History`. Open: does a
*loaded* security replace the tab strip with a pack view, or become a third tab? And does
`History` mean "my past searches" or "past snapshots of THIS security"? Those are different
surfaces and I would build the second.

**Q4 -- v1 news scope.** SA corpus only (works today), or SA + an entity-extraction leg over the
RSS/NewsAPI corpus (new work, §3.5)? I would ship SA-only in v1 and file the RSS leg separately.

**Q5 -- Web-search leg source allowlist.** "IR pages or trusted publications" needs an enumerated
list to be buildable. Whose call -- Adam's, or ours to propose?

**Q6 -- Does the CSC peer set need Adam's input?** (§3.2 flag.) Related: is the peer set per-name
analyst judgment, or derivable (sector/size/geography)? If derivable, it automates; if judgment, it
is an input field.

**Q7 -- Register mechanics.** Confirm `0.0.0_AB_MSTR` moves D5 LAPTOP -> SITEZ and mints
AMGT_RESAPP as its first member project. Not mine to do.

---

## 8. WHAT I HAVE NOT MEASURED (stated so it is not mistaken for coverage)

- The portal's **sidebar NAV order** (I read the ROUTE order only).
- Which of the SAP pack's 9 embedded images is the COMMON STOCK COMPARISON, hence whether the
  `CSC` sheet is its source.
- The news **DynamoDB table schema itself** -- I inferred ticker-tagging absence from Lambda
  source, not from the table.
- Whether the SA estate's Lambdas are **currently running** (I read source + terraform, not
  invocation metrics).
- Any **live Bloomberg call**. Nothing has been pulled. The egress grant is unspent.
- `bloomberg_health` on this session -- unread.
