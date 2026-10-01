# BRIEF -- rivalfunds BACKEND: the analytics layer and the AI synthesis (midstream, ETFS_RIVALS)

**Author:** `4.0.0_SA_CRO~RV`, 2026-10-01. **Mode:** `/brief-create --midstream`.
**Andrew-direct:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_194xZ_RIVALFUNDS_NEXT_CHALLENGES_TWO_BRIEFS.md`
(the directive plus both dictated transcripts, verbatim).
**Sibling brief (frontend):** `docs/briefs/rivalfunds-frontend-mcp-page-20261001.md`. The boundary between the two is in
Part II.
**Consumer:** `1.0.0_SA_CTO~Z`, `/endpoint --forward` at L2.

---

## PART 0 -- How the blind constraint was honoured, and WHERE IT BENT

- **Read, admissible:**
  - the ETFS_RIVALS PRD v0.7 (ENDPOINT and CONTRACTS);
  - Andrew's verbatim records;
  - the served reality, measured in my trace of today.
- **Where it bent:** in the same session, for the `/closer trace`
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md` @381bec5549), I read the
  round-4 decomposition, every task order's status line and the round-3 analysis. I also received the CTO's round-5
  ruling on three method defects (@4baf852611). That is the branch.
- **How I held the line:**
  - No outcome below restates a round-4 or round-5 cell: the revision contract, the GQGU route, the identity floors and
    the ID-change, flow-factor and label fixes appear only as preconditions in Part V.
  - The outcomes come from Andrew's two transcripts and the PRD's ENDPOINT.
- **Where a ratifying outcome could still enter:** O9 (operations). It overlaps work the branch is already doing. I kept
  it because Andrew named it ("this comprises the data side and ... the operations as well"), and I phrased it as what
  Andrew no longer has to do, not as a cell.

**Finding: the direction has SHARPENED, not changed.** Andrew's transcripts restate PRD FWD-5, 6, 7, 10 and 11 and add
four things the PRD does not carry:
1. **Calendar windows for performance (MTD, QTD, YTD).** The PRD's G7 uses 21/63/126 trading-day horizons for trade
   outcomes.
2. **A defined outside-world input set for the AI:** market-overview sentiment, global RSI, the daily word cloud, the
   news scanner and Data Harvest, and possibly web search.
3. **A chained, two-prompt AI structure** with context carried from one prompt to the next.
4. **No AI analysis of the benchmark funds.**

---

## PART I -- THE OUTCOME TERRITORY

### O1 -- THE CANDIDATE THREAD: Andrew reads where one rival's trading helped and hurt this year, and why the AI thinks so

**Who and journey:** Andrew opens the IDVZ group and picks one rival. He reads its year-to-date ten best and ten worst
securities and its five best and five worst sectors, then the AI's recent-activity account of that fund, each figure
traceable to the trades and prices it came from.

**Coarse grain:** one rival, one group, YTD only, prompt one only. It crosses every new layer once:
- daily prices for the fund's holdings;
- the ranking table;
- the AI step reading that table and one sentiment input;
- the served artifact the page reads.

Source: transcript 1, point one ("outperformance and underperformance ... by sector and by security"); transcript 2,
component 1 and AI prompt one.

### O2 -- Andrew ranks every fund's best and worst securities and sectors for MTD, QTD and YTD, by the same rules

For every fund in both groups, the ranking exists for each of the three windows:
- the rivals;
- the Opal funds IDVZ and PFOE;
- each group's benchmark (ACWI for IDVZ, IWM for PFOE).

Opal's own funds get no separate method (PRD FWD-11). Each ranking says what it ranks, over what window and out of how
many holdings, and a holding with no price is counted as missing.

Source: transcript 2, component 1; transcript 1, point one; Andrew-direct ~18:2xZ (controls); PRD FWD-6, FWD-11.

### O3 -- Andrew reads each fund's tilts and bets: where its buying has trended this year, by security and by sector

A naive year-to-date trend of each fund's buying activity, for:
- the same ten-best/ten-worst securities;
- the same five-best/five-worst sectors.

Each trend is summarised as a tilt or a bet. A trend is not presented as one that will continue indefinitely.

Source: transcript 1, point two ("projected trades ... summarized effectively as their tilts and bets, not only by
security, but also by sector"; "just because there is a trend does not mean it is expected to continue indefinitely");
transcript 2, component 2; PRD FWD-7(a).

### O4 -- Andrew sees whether each manager trades by system or by discretion, and the evidence for the call

Each fund carries a style read: systematic trading identified, or discretionary concentrated blocks. The evidence is
shown with it. The groups' index funds read as systematic on that same evidence before any label is shown.

Source: transcript 2, AI prompt two ("Is it more systematic? ... Is it more discretionary, just big concentrated
blocks?"); PRD FWD-10.

### O5 -- Andrew reads, per fund, what it has done in the last 30 days: anything unusual, its big wins and big losses

**AI prompt one**, for every rival and both Opal funds, never for a benchmark. Every figure in the text points to the
row it came from, and what was seen is kept apart from what is guessed.

Source: transcript 2 ("the first one is, what has this fund been doing? ... rolling 30-day view ... big wins ... big
losses"); PRD C-AI-GROUNDING.

### O6 -- Andrew reads the AI's verdict on each fund's direction: it corroborates, refutes or enriches the trend, and says what it expects next

**AI prompt two.** It reads:
- the outcome of O2 (component 1) and O3 (component 2);
- the style read (O4);
- the market sentiment (O7);
- what prompt one concluded.

It states what it believes is happening, what it expects the manager to do, what the manager has done right and wrong,
and what would prove it wrong.

Source: transcript 2 (prompt two, "corroborate, refute, or otherwise enrich"); transcript 1, point three; PRD FWD-7.

### O7 -- The AI weighs the broader market from Opal's own data before it reaches for the web

The analysis step can read:
- the market-overview sentiment layers: Fear & Greed with S&P 500 momentum, the put/call ratio, breadth, and the axis
  Andrew called "concentration" (open, Part VII);
- the global RSI;
- the daily word cloud, or its ranked form in the news scanner;
- the news scanner's articles;
- Opal Data Harvest.

Web search is a further, optional input. Andrew judged the internal route "may be an easier mechanism, frankly, than
web search". The access is light: a simple read of how each source is stored, with staging tables only where needed.

Source: transcript 1 (the sentiment list, "lightly and athletically incorporate"; "if we have to make any staging
tables, so be it").

### O8 -- The prompts run as one chained, cached sequence, so each step builds on the last

Per fund, prompt one runs and then prompt two, with the earlier context carried forward and cached. A later run can be
compared with what the earlier run said, and never rewrites it.

Source: transcript 2 ("they should be effectively cached. They should be run one after another so that it has the
context built up"); PRD FWD-7 ("a later grading cannot rewrite the earlier account").

### O9 -- Andrew does nothing by hand: every fund, benchmark and input arrives on schedule, and a missing one says so

Every input reaches the analytics layer each trading morning on a schedule:
- holdings for every fund, the Opal funds included;
- the benchmark funds;
- prices, returns and GICS for every held security;
- the sentiment inputs.

A missing or stale input is named on the output, never silently skipped.

Source: transcript 1 ("locked in bronze ingestion for all relevant funds including IDVZ and PFOE ... complete in silver
... tabled out in gold"; "this comprises the data side and ... the operations as well"); PRD FWD-3, FWD-9.

---

## PART II -- WHERE THE BOUNDARY SITS

- **This brief owns:**
  - the gold analytics behind O2-O4;
  - the AI step and its input access (O5-O8);
  - the scheduled arrival of every input (O9);
  - the served artifact the page reads (tables and AI text, with their vintages).
- **The frontend brief owns** how those artifacts are laid out on `mcp.opalinvest.dev/rivalfunds`: components, toggles,
  the fund selector, and moving the audit material out of the reading path. The seam is the served artifact: this side
  writes it, that side renders it. Andrew placed the AI's data access here ("that should probably be covered in the
  backend brief").
- **Relied on, not owned:**
  - **ETFS_RIVALS' existing spine** (collection, silver, G1 canonical shape, G2 coverage, G5 trades, G6 flow
    reconciliation) and the round-4/5 fixes in flight.
  - **The news scanner** (`opal-news-*` pipeline; owner per `NEWS_SCANNER_DEEP_DIVE_20260916.md`, 0.1.0 MarketIntelligence).
  - **The market-overview fetchers** (`opal-portal-fear-greed-fetcher`, the RSI producer).
  - **AMGT_HARVST** (Data Harvest, D5).
  - **The gateway's data catalog** (`app/refs/DATA_CATALOG.yaml`, `opal_discover` / `gateway_query_catalog`).
  - **ETFS_POSITIONING**, whose pull stays untouched (Andrew-direct 2026-09-30).
- **Never:** changing what the news scanner or the sentiment fetchers compute, or writing into their homes.
  `etfs-netassets-daily`. Any AI analysis of a benchmark fund.

## PART III -- THE QUALITATIVE BAR

- Andrew reads a manager's best and worst calls this year without opening Bloomberg or the fund's site.
- **Every ranking states:**
  - what it ranks: trade outcome, holding contribution or return (Part VII);
  - its window;
  - its denominator.

  A holding with no price reads as missing.
- **An AI paragraph is disputable line by line.** Every figure points to a row, the guess is labelled as a guess, and
  each expectation names what would contradict it. A trend the AI calls persistent says why. Andrew's bar: "just because
  there is a trend does not mean it is expected to continue indefinitely".
- **The AI never manufactures a trend from a stale series.** The gateway catalog already carries this guard for the
  keyword-history files (Part IV, finding 6), and the same applies to every sentiment input: an input's vintage travels
  with every claim that uses it.
- **Opal's funds and the rivals are measured by the same rules** (PRD FWD-11). The benchmarks are measured, never
  analysed by the AI.

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

1. **The analytics layer above the trade schedule does not exist.** `comp-find` over the rivalfunds package and its
   Lambda tree found no outcomes, rollups, style read, projections, peer comparison or AI step: 0 hits across 71 files
   (trace, 2026-10-01).
2. **Prices and GICS are thin, and the daily refresh is a no-op.**
   - G4 `security_market` holds one date (2026-09-29).
   - The morning enrichment step logs "landed" while pulling nothing: row ETFS_RIVALS-Z-S10 @4add024498, ruled into a
     fix by `2.0.0_SA_COO~RV` (amendment 3 @ab795cfa62).
   - Latest-report GICS sector fill: 0% for IDVZ, PFOE, BASG, BIDD, INEQ and SCHY, and 3-66% for the others; finer
     GICS levels 0%.
   - An MTD/QTD/YTD ranking needs a daily return for every held security from the start of the year.
3. **The Opal funds' history is short today.** IDVZ and PFOE hold 22 reports each, from 2026-08-21/24. Andrew-direct
   ~18:2xZ routes them through the rivalfunds Bloomberg queue. PFOE launched 2025-12-31, so its YTD is its whole life.
4. **Fear & Greed is a one-year rolling file.**
   - Location: `s3://opal-data-portal-v2/json/sentiment/fear-greed-index.json`, refreshed hourly by
     `opal-portal-fear-greed-fetcher` (env `MAX_HISTORY_DAYS=365`).
   - Measured content: 251 daily points for each of the seven components, 2025-10-01 to 2026-10-01. The components are
     `market_momentum_sp500`, `put_call_options`, `stock_price_breadth`, `stock_price_strength`,
     `market_volatility_vix`, `safe_haven_demand` and `junk_bond_demand`.
   - So it reaches further than the 90 days the portal shows, as Andrew remembered, but it is capped at a year, not
     appended forever.
   - None of the seven is named "concentration" (Part VII).
5. **The global RSI is served tiered:** `/api/general/json-tiered/market-overview/rsi-summary.json` carries asset-class
   RSI values with 7d-3y changes, and `rsi-details-{assetClass}.json` the detail. Its history depth is unmeasured.
6. **The word cloud has no kept history in S3.**
   - `keyword-sentiments.json` is rewritten daily: 45 keywords over a 7-day window.
   - The gateway catalog marks the per-keyword history files stale since 2026-04-07 and forbids joining them to live
     data to make a trend.
   - Dated stores do exist in the news pipeline: DynamoDB `opal-news-trending-daily` (20 rows a day) and
     `opal-keyword-intelligence` (keyed by keyword and date). Their retention is unmeasured.
7. **The news scanner carries known semantic defects.** Its 2026-09-16 deep dive (F1-F19) names three that every
   downstream number inherits: unparsed dates, neutral sentiment dropped from means, and direction by sign of a mean. An
   input read from it inherits whichever are still open.
8. **An LLM with web search is already running in the estate.** The keyword-intelligence generator runs an OpenAI model
   with two web searches per keyword, and Layer 3 curation runs a second model. PRD C-VENDOR already names OpenAI for
   these analyses.
9. **A typed, audited read path for agents exists:** `opal_discover` -> `gateway_query_catalog`, catalog-gated, capped
   and audited. Fear & Greed and keyword sentiment are catalogued (as `news.03`). **Rival funds are not catalogued**
   (`opal_discover("rival funds holdings trades")` -> not catalogued). A catalog row per rivalfunds table is a candidate
   for "what tooling or what tables should be accessible to it", without a new access mechanism.
10. **Data Harvest (AMGT_HARVST)** keeps every mention of a covered company with its provenance, graded by strength over
    time. How much of the rival funds' holdings it covers is unmeasured.
11. **The PRD already fixes how the AI may work** (C-AI-GROUNDING, C-GOLD-MODEL G7-G13): the model explains and never
    calculates, every figure cites a row, and a grading never rewrites an earlier account. This brief inherits those
    contracts and changes none.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The round-5 method fixes are served before any ranking or trend is computed from G5 (CTO ruling @4baf852611). The
  three fixes:
  - equal-value swaps stay trades;
  - degenerate windows are refused;
  - key resolution becomes its own label.
- A daily return series for every held security, back to at least the start of the year, with GICS for every holding.
- IDVZ and PFOE holdings history through the Bloomberg queue (Andrew-direct ~18:2xZ), and the CTO's amendment of PRD
  C-HOME-PRODUCER to match.
- Holdings, or a return series, for ACWI and IWM. Both are broad index funds, far larger than any rival, so the
  Bloomberg queue's capacity for them is a question to measure first.
- A decision on whether "outperformance" ranks returns, contributions or trade outcomes (Part VII), before O2 is built.
- **Vendor egress:**
  - The AI provider call is already authorised (PRD C-VENDOR, OpenAI).
  - Any web search from the pipeline needs Andrew's explicit word, as standing scope or per use (CLAUDE.md: availability
    is not authorization).
- Read access from the rivalfunds analysis step to the sentiment homes (`opal-data-portal-v2`, the news DynamoDB
  tables, the Data Harvest home), through a catalog row or a scoped grant. This is a served-read widening under the
  never-widen pair.
- No notifier (the standing moratorium). A missing input is carried on the output itself.

## PART VI -- STATUS, MARKED NOT OUTCOME-BEARING

**NOT OUTCOME-BEARING. A snapshot measured 2026-10-01 17:30Z-20:05Z; it ages.**
- Served: the 2026-10-01 page with 12 of 13 funds updated. G1/G2/G5/G6 cover 502 dates from 2024-09-30.
- Round 4 (RIV-d-5) was applying during the read.
- G3 holds one object and G4 one date.
- Fear & Greed's file was written at 2026-10-01 10:30Z (local listing) and keyword sentiments at 07:17Z.
- Rivalfunds is absent from the gateway catalog.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **What "outperforming" ranks.** Transcript 1 says by "reverse engineering trading". Transcript 2 says "top ten best
  performers ... bottom ten starting from the worst performers". The first reads as the outcome of the fund's trades,
  the second as its holdings' returns or contributions over the window. Both are named; L2 or Andrew picks one.
- **"Concentration of the market."** This is not one of Fear & Greed's seven components. The nearest are
  `stock_price_strength` (52-week highs vs lows) and `stock_price_breadth`. Which axis Andrew means is not resolved here.
- **The source of "global RSI"** is assumed to be the market-overview RSI summary. Its history depth is unmeasured.
- **Not measured:**
  - Data Harvest's overlap with the rivals' holdings;
  - the retention of the two news DynamoDB tables;
  - the Bloomberg queue's capacity for ACWI and IWM.
- **No prompt text, model choice, cache mechanism or table design is specified.** Those belong to the PRD and the
  decomposition.
- **No number in this brief is a threshold.** The windows (MTD/QTD/YTD, rolling 30 days) and the counts (ten and five)
  are Andrew's own words.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md
  PROJECT           ETFS_RIVALS (D5/ETFS); workstream registration is the CTO's call
  EXISTING PRD      org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.7; FWD-5/6/7/10/11, C-GOLD-MODEL,
                    C-AI-GROUNDING, C-VENDOR)
  SIBLING BRIEF     docs/briefs/rivalfunds-frontend-mcp-page-20261001.md
  SIBLING PROJECTS  ETFS_POSITIONING, AMGT_HARVST, the news scanner (owner 0.1.0 MarketIntelligence), the
                    market-overview fetchers, the gateway data catalog (NFRA_MCPINDEX lineage)
  PRIOR ART         trace org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md @381bec5549;
                    CTO ruling org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md @4baf852611;
                    Andrew-direct ...182xZ_ETFS_RIVALS_THREE_CALLS_ANSWERED.md @19c5277a57;
                    org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/NEWS_SCANNER_DEEP_DIVE_20260916.md;
                    portal/src/api/endpoints/sentiment.ts, market.ts (served sentiment and RSI paths);
                    keyword-intelligence-generator (LLM + web search prior art)
  MEASURED AT       2026-10-01 17:30Z-20:05Z (Part VI)
```
